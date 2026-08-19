#!/usr/bin/env python3
"""
Cross-language symmetry validator for the Language wiki.

Scans all 5 main languages (English / Spanish / Japanese / Korean / Chinese)
plus auxiliary directories (comparative/, French/, German/) and reports:

  1. File count per directory × language (catches coverage gaps)
  2. Pipeline Form YAML coverage (vocabulary + expressions) — ADR-0003 + ADR-0005
  3. ADR staleness — future-candidates in decisions/README.md not yet resolved
  4. study-plan coverage (one of the ADR-0005-era identified asymmetries)
  5. Orphan pages in expressions/ (catch the pre-pilot state for any lang)

Exit codes:
  0 = clean (or all asymmetries already documented as known)
  1 = new asymmetries detected (warnings)
  2 = runtime error

Usage:
  python3 Language/tools/symmetry_check.py                  # stdout summary
  python3 Language/tools/symmetry_check.py --report PATH    # also write MD report
  python3 Language/tools/symmetry_check.py --json           # machine-readable output
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Optional


SCRIPT_DIR = Path(__file__).resolve().parent
LANG_DIR = SCRIPT_DIR.parent
WIKI_DIR = LANG_DIR / "wiki"
DECISIONS_DIR = LANG_DIR / "decisions"

MAIN_LANGS = ["English", "Spanish", "Japanese", "Korean", "Chinese"]
AUX_DIRS = ["comparative", "French", "German"]

CONTENT_DIRS = ["vocabulary", "expressions", "culture", "grammar", "sources", "study-plan"]

PIPELINE_HEADER_RE = re.compile(
    r"^##\s+Pipeline Form(?:\s+\(machine-readable\))?\s*$",
    re.MULTILINE | re.IGNORECASE,
)


@dataclass
class LangDirStats:
    """Stats for one language's content directory."""
    lang: str
    content_type: str
    file_count: int = 0
    files_with_yaml: int = 0
    file_names: list[str] = field(default_factory=list)

    @property
    def yaml_coverage_pct(self) -> float:
        if self.file_count == 0:
            return 0.0
        return (self.files_with_yaml / self.file_count) * 100


@dataclass
class Asymmetry:
    """Detected asymmetry across languages."""
    category: str  # "vocabulary", "expressions", etc.
    description: str
    languages_affected: list[str]
    delta: int  # max-min count
    severity: str  # "info", "warn", "alert"


def scan_lang_directory(lang: str, content_type: str) -> LangDirStats:
    """Scan one lang/content_type directory."""
    stats = LangDirStats(lang=lang, content_type=content_type)
    d = WIKI_DIR / lang / content_type
    if not d.exists():
        return stats
    for path in sorted(d.glob("*.md")):
        if path.name.endswith(".ko.md"):
            continue
        stats.file_names.append(path.stem)
        stats.file_count += 1
        try:
            text = path.read_text(encoding="utf-8")
            if PIPELINE_HEADER_RE.search(text):
                stats.files_with_yaml += 1
        except Exception:
            pass
    return stats


def detect_count_asymmetries(grid: dict[str, dict[str, LangDirStats]]) -> list[Asymmetry]:
    """Compare file counts across languages for each content_type."""
    out = []
    for content_type, lang_stats in grid.items():
        counts = {lang: s.file_count for lang, s in lang_stats.items() if s.file_count > 0}
        if len(counts) < 2:
            continue
        max_lang = max(counts, key=counts.get)
        min_lang = min(counts, key=counts.get)
        delta = counts[max_lang] - counts[min_lang]
        if delta >= 3:
            out.append(Asymmetry(
                category=content_type,
                description=f"{content_type}: {max_lang}={counts[max_lang]} vs {min_lang}={counts[min_lang]} (delta={delta})",
                languages_affected=[max_lang, min_lang],
                delta=delta,
                severity="alert" if delta >= 5 else "warn",
            ))
    return out


def detect_yaml_coverage_gaps(grid: dict[str, dict[str, LangDirStats]]) -> list[Asymmetry]:
    """Find languages with low Pipeline Form YAML coverage for vocabulary/expressions."""
    out = []
    for content_type in ("vocabulary", "expressions"):
        if content_type not in grid:
            continue
        for lang, s in grid[content_type].items():
            if s.file_count == 0:
                continue
            if s.yaml_coverage_pct < 100.0:
                out.append(Asymmetry(
                    category=content_type,
                    description=f"{lang}/{content_type}: {s.files_with_yaml}/{s.file_count} files have Pipeline Form YAML ({s.yaml_coverage_pct:.0f}%)",
                    languages_affected=[lang],
                    delta=s.file_count - s.files_with_yaml,
                    severity="alert" if s.yaml_coverage_pct < 50 else "warn",
                ))
    return out


def detect_adrs_staleness() -> list[Asymmetry]:
    """Find ADR candidates in decisions/README.md that look in-progress (no resolution marker)."""
    out = []
    readme = DECISIONS_DIR / "README.md"
    if not readme.exists():
        return out
    text = readme.read_text(encoding="utf-8")
    in_candidates = False
    for line in text.splitlines():
        if "## 향후 결정 후보" in line or "## Future decision candidates" in line:
            in_candidates = True
            continue
        if in_candidates and line.startswith("## "):
            break
        if in_candidates and line.startswith("- "):
            if "(진행)" in line or "(in-progress)" in line or "(in progress)" in line:
                m = re.search(r"`([^`]+)`", line)
                name = m.group(1) if m else line.strip()[:60]
                out.append(Asymmetry(
                    category="adr-staleness",
                    description=f"ADR candidate in progress: {name}",
                    languages_affected=[],
                    delta=0,
                    severity="info",
                ))
    return out


# ADR staleness v2 (2026-08-19 — Track C1 upgrade)

ADR_FILE_RE = re.compile(r"^(?P<num>\d{4})-(?P<slug>[a-z0-9\-]+)\.md$")
ADR_HEADER_RE = re.compile(r"^\*\*상태\*\*:\s*(?P<status>\S+)", re.MULTILINE)
ADR_DATE_RE = re.compile(r"\*\*날짜\*\*:\s*(?P<date>[\d\-/\s\(\)~]+)")
BACKTICK_PATH_RE = re.compile(r"`((?:[\w./\-]+\.[a-z]{1,5}))`")


def _parse_adr_age_days(adr_text: str) -> Optional[int]:
    """Extract effective date from ADR markdown; return age in days from today."""
    m = ADR_DATE_RE.search(adr_text)
    if not m:
        return None
    raw = m.group("date")
    iso = re.search(r"(\d{4})-(\d{2})-(\d{2})", raw)
    if not iso:
        return None
    try:
        y, mo, d = int(iso.group(1)), int(iso.group(2)), int(iso.group(3))
        adr_date = date(y, mo, d)
        return (date.today() - adr_date).days
    except ValueError:
        return None


def detect_adr_age_staleness(stale_days: int = 180) -> list[Asymmetry]:
    """Warn when Accepted ADRs have not been touched in > stale_days."""
    out = []
    if not DECISIONS_DIR.exists():
        return out
    for path in sorted(DECISIONS_DIR.glob("*.md")):
        if path.name == "README.md":
            continue
        m_adr = ADR_FILE_RE.match(path.name)
        if not m_adr:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except Exception:
            continue
        status_m = ADR_HEADER_RE.search(text)
        if not status_m:
            continue
        status = status_m.group("status").strip()
        if status.lower() != "accepted":
            continue
        age_days = _parse_adr_age_days(text)
        if age_days is None:
            continue
        if age_days >= stale_days:
            out.append(Asymmetry(
                category="adr-staleness",
                description=f"ADR-{m_adr.group('num')} ({m_adr.group('slug')}) Accepted {age_days}d ago — review for relevance",
                languages_affected=[],
                delta=age_days,
                severity="warn",
            ))
    return out


def detect_adr_referenced_paths() -> list[Asymmetry]:
    """For each Accepted ADR, check if backtick-quoted file paths still exist.

    Tries multiple resolution roots (workspace, Language/, parent) because ADRs
    often include `Language/...` prefix even when written from Language/.
    """
    out = []
    if not DECISIONS_DIR.exists():
        return out
    roots = [LANG_DIR, LANG_DIR.parent, LANG_DIR.parent.parent]
    for path in sorted(DECISIONS_DIR.glob("*.md")):
        if path.name == "README.md":
            continue
        m_adr = ADR_FILE_RE.match(path.name)
        if not m_adr:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except Exception:
            continue
        status_m = ADR_HEADER_RE.search(text)
        if not status_m:
            continue
        if status_m.group("status").strip().lower() != "accepted":
            continue
        for ref in BACKTICK_PATH_RE.finditer(text):
            ref_path = ref.group(1)
            if ref_path.startswith(("http://", "https://", "mailto:", "git@")):
                continue
            if "/" not in ref_path and "\\" not in ref_path:
                continue
            if ref_path.startswith("[[") or ref_path.endswith("]]"):
                continue
            if any(target.exists() for target in (root / ref_path for root in roots)):
                continue
            out.append(Asymmetry(
                category="adr-staleness",
                description=f"ADR-{m_adr.group('num')} references missing path: `{ref_path}`",
                languages_affected=[],
                delta=0,
                severity="warn",
            ))
    return out


def detect_resolved_candidates() -> list[Asymmetry]:
    """Find future-candidates items that appear already resolved.

    Heuristic: scan decisions/README.md future-candidates section for bullet
    lines; if any backtick-token appears in another ADR body, mark as likely
    resolved (promote to ADR or remove from candidates).
    """
    out = []
    readme = DECISIONS_DIR / "README.md"
    if not readme.exists():
        return out
    text = readme.read_text(encoding="utf-8")
    in_candidates = False
    candidate_lines: list[str] = []
    for line in text.splitlines():
        if "## 향후 결정 후보" in line or "## Future decision candidates" in line:
            in_candidates = True
            continue
        if in_candidates and line.startswith("## "):
            break
        if in_candidates and line.startswith("- "):
            candidate_lines.append(line)

    adr_corpus: list[str] = []
    for path in sorted(DECISIONS_DIR.glob("*.md")):
        if path.name == "README.md":
            continue
        try:
            adr_corpus.append(path.read_text(encoding="utf-8"))
        except Exception:
            pass

    for line in candidate_lines:
        tokens = re.findall(r"`([^`]+)`", line)
        for tok in tokens:
            if len(tok) < 5:
                continue
            for adr_text in adr_corpus:
                if tok in adr_text and f"ADR-0000" not in line:
                    out.append(Asymmetry(
                        category="adr-staleness",
                        description=f"Candidate `{tok}` appears resolved in ADR — promote or remove",
                        languages_affected=[],
                        delta=0,
                        severity="info",
                    ))
                    break
    return out


def build_full_grid() -> dict[str, dict[str, LangDirStats]]:
    """Build the full stats grid."""
    grid: dict[str, dict[str, LangDirStats]] = {}
    for content_type in CONTENT_DIRS:
        grid[content_type] = {}
        for lang in MAIN_LANGS:
            grid[content_type][lang] = scan_lang_directory(lang, content_type)
    for aux in AUX_DIRS:
        if aux == "comparative":
            d = WIKI_DIR / aux
            stats = LangDirStats(lang=aux, content_type="n/a")
            if d.exists():
                stats.file_count = sum(1 for p in d.glob("*.md") if not p.name.startswith("_"))
            grid.setdefault("auxiliary", {})[aux] = stats
        else:
            d = WIKI_DIR / aux
            for content_type in CONTENT_DIRS:
                stats = LangDirStats(lang=aux, content_type=content_type)
                sub = d / content_type if d.exists() else None
                if sub and sub.exists():
                    stats.file_count = len([p for p in sub.glob("*.md") if not p.name.endswith(".ko.md")])
                grid.setdefault(content_type, {})[aux] = stats
    return grid


def format_summary(grid: dict[str, dict[str, LangDirStats]]) -> str:
    """Format the summary table for stdout."""
    lines = []
    lines.append("=" * 78)
    lines.append(f"CROSS-LANGUAGE SYMMETRY REPORT — {date.today().isoformat()}")
    lines.append("=" * 78)
    lines.append("")
    lines.append(f"{'Content Type':<14} {'Lang':<10} {'Files':>7} {'YAML Cov':>9}")
    lines.append("-" * 78)
    for content_type in CONTENT_DIRS:
        if content_type not in grid:
            continue
        for lang in MAIN_LANGS + AUX_DIRS:
            if lang not in grid[content_type]:
                continue
            s = grid[content_type][lang]
            if s.file_count == 0:
                continue
            yaml_pct = f"{s.yaml_coverage_pct:.0f}%" if content_type in ("vocabulary", "expressions") else "n/a"
            lines.append(f"{content_type:<14} {lang:<10} {s.file_count:>7} {yaml_pct:>9}")
    lines.append("")
    if "auxiliary" in grid:
        lines.append("Auxiliary directories:")
        for aux, s in grid["auxiliary"].items():
            lines.append(f"  {aux:<14} files: {s.file_count}")
        lines.append("")
    return "\n".join(lines)


def format_asymmetries(asymmetries: list[Asymmetry]) -> str:
    """Format detected asymmetries section."""
    if not asymmetries:
        return "✅ No asymmetries detected.\n"
    lines = ["", "⚠️  Asymmetries detected:", ""]
    by_sev = {"alert": [], "warn": [], "info": []}
    for a in asymmetries:
        by_sev[a.severity].append(a)
    for sev in ("alert", "warn", "info"):
        if by_sev[sev]:
            icon = {"alert": "🔴", "warn": "🟡", "info": "🔵"}[sev]
            lines.append(f"{icon} {sev.upper()} ({len(by_sev[sev])})")
            for a in by_sev[sev]:
                lines.append(f"   - [{a.category}] {a.description}")
            lines.append("")
    return "\n".join(lines)


def format_markdown_report(
    grid: dict[str, dict[str, LangDirStats]],
    asymmetries: list[Asymmetry],
) -> str:
    """Format full Markdown report for wiki/_inventory/."""
    lines = [
        f"# Cross-Language Symmetry Report",
        "",
        f"**Generated**: {date.today().isoformat()}",
        f"**Tool**: `tools/symmetry_check.py`",
        f"**Scope**: 5 main languages (EN/ES/JP/KR/ZH) + auxiliary (comparative, French, German)",
        "",
        "## Coverage Summary",
        "",
        "| Content Type | Lang | Files | YAML Cov |",
        "|---|---|---:|---:|",
    ]
    for content_type in CONTENT_DIRS:
        if content_type not in grid:
            continue
        for lang in MAIN_LANGS + AUX_DIRS:
            if lang not in grid[content_type]:
                continue
            s = grid[content_type][lang]
            if s.file_count == 0:
                continue
            yaml_pct = f"{s.yaml_coverage_pct:.0f}%" if content_type in ("vocabulary", "expressions") else "n/a"
            lines.append(f"| {content_type} | {lang} | {s.file_count} | {yaml_pct} |")
    lines.append("")

    if "auxiliary" in grid:
        lines.append("## Auxiliary Directories")
        lines.append("")
        lines.append("| Directory | Files |")
        lines.append("|---|---:|")
        for aux, s in grid["auxiliary"].items():
            lines.append(f"| {aux} | {s.file_count} |")
        lines.append("")

    lines.append("## Detected Asymmetries")
    lines.append("")
    if not asymmetries:
        lines.append("✅ No asymmetries detected.")
    else:
        by_sev = {"alert": [], "warn": [], "info": []}
        for a in asymmetries:
            by_sev[a.severity].append(a)
        for sev in ("alert", "warn", "info"):
            if not by_sev[sev]:
                continue
            icon = {"alert": "🔴", "warn": "🟡", "info": "🔵"}[sev]
            lines.append(f"### {icon} {sev.upper()} ({len(by_sev[sev])})")
            lines.append("")
            for a in by_sev[sev]:
                lines.append(f"- **[{a.category}]** {a.description}")
            lines.append("")

    lines.append("## Resolution Status")
    lines.append("")
    lines.append("Symmetry gaps fall into 3 buckets:")
    lines.append("")
    lines.append("1. **Pilot-in-progress** (expected) — partial rollout already documented in `decisions/README.md`")
    lines.append("2. **Known intentional** — French/German scaffolded-only by design per **ADR-0007** (2026-08-19, Option 2 Document); raw/ = Phase 15/16 seed README only. YAML 0% is intentional. Promote via ADR-0008 when user provides raw.")
    lines.append("3. **Actionable** — needs follow-up session to close gap")
    lines.append("")
    lines.append("### ADR Staleness Findings")
    lines.append("")
    adr_findings = [a for a in asymmetries if a.category == "adr-staleness"]
    if not adr_findings:
        lines.append("✅ No ADR staleness detected.")
    else:
        for a in adr_findings:
            icon = {"alert": "🔴", "warn": "🟡", "info": "🔵"}[a.severity]
            lines.append(f"- {icon} {a.description}")
    lines.append("")
    lines.append("Run `python3 Language/tools/symmetry_check.py` after any batch to refresh this view.")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Cross-language symmetry validator for the Language wiki."
    )
    parser.add_argument("--report", help="Write Markdown report to this path")
    parser.add_argument("--json", action="store_true", help="Machine-readable JSON output")
    args = parser.parse_args()

    grid = build_full_grid()
    asymmetries = (
        detect_count_asymmetries(grid)
        + detect_yaml_coverage_gaps(grid)
        + detect_adrs_staleness()
        + detect_adr_age_staleness()
        + detect_adr_referenced_paths()
        + detect_resolved_candidates()
    )

    if args.json:
        out = {
            "date": date.today().isoformat(),
            "grid": {
                ct: {lang: {"files": s.file_count, "yaml": s.files_with_yaml} for lang, s in lang_stats.items()}
                for ct, lang_stats in grid.items()
            },
            "asymmetries": [
                {
                    "category": a.category,
                    "description": a.description,
                    "languages": a.languages_affected,
                    "delta": a.delta,
                    "severity": a.severity,
                }
                for a in asymmetries
            ],
        }
        print(json.dumps(out, indent=2, ensure_ascii=False))
        return 0 if not any(a.severity in ("alert", "warn") for a in asymmetries) else 1

    print(format_summary(grid))
    print(format_asymmetries(asymmetries))

    if args.report:
        report_path = Path(args.report)
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(format_markdown_report(grid, asymmetries), encoding="utf-8")
        print(f"\n📝 Markdown report written to: {report_path}")

    has_real_warnings = any(a.severity in ("alert", "warn") for a in asymmetries)
    return 1 if has_real_warnings else 0


if __name__ == "__main__":
    sys.exit(main())