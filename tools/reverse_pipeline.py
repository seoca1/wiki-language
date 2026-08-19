#!/usr/bin/env python3
"""Reverse-pipeline citation auditor.

Scans `Game/lingotype/raw/{lang}_words.md` corpus files for
`source: [[theme-filename]]` references and verifies each stem resolves to
an existing file under `Language/wiki/{Lang}/vocabulary/` or
`Language/wiki/{Lang}/expressions/`.

Per ADR-0001 theme-file convention and `Game/typing_language/AGENTS.md`
§1.5, every corpus entry must cite a theme-filename that exists in the
Language wiki. This tool surfaces entries whose citation target is
missing, suggesting the Language wiki needs the corresponding theme
file (rather than the corpus pointing elsewhere).

Usage:
  python3 Language/tools/reverse_pipeline.py            # all langs
  python3 Language/tools/reverse_pipeline.py --lang en # one lang
  python3 Language/tools/reverse_pipeline.py --json     # machine-readable
  python3 Language/tools/reverse_pipeline.py --report PATH

Exit codes:
  0 = clean (no missing citations)
  1 = missing citations detected
  2 = runtime error
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


SCRIPT_DIR = Path(__file__).resolve().parent
LANG_DIR = SCRIPT_DIR.parent
WORKSPACE_DIR = LANG_DIR.parent
WIKI_DIR = LANG_DIR / "wiki"
GAME_CORPUS_DIR = WORKSPACE_DIR / "Game" / "lingotype" / "raw"

LANG_MAP = {"en": "English", "es": "Spanish", "jp": "Japanese", "kr": "Korean"}
SOURCE_RE = re.compile(r"source:\s*\[\[([^\]]+)\]\]")


@dataclass
class CitationFinding:
    lang: str
    source_stem: str
    entry_count: int = 0


@dataclass
class CitationReport:
    findings: list[CitationFinding] = field(default_factory=list)
    total_entries: int = 0
    total_unique_sources: int = 0


def collect_corpus_sources(lang_code: str) -> tuple[int, dict[str, int]]:
    """Return (total_entries, {source_stem: count}) for one corpus file."""
    corpus_path = GAME_CORPUS_DIR / f"{lang_code}_words.md"
    if not corpus_path.exists():
        return 0, {}
    text = corpus_path.read_text(encoding="utf-8")
    sources: dict[str, int] = defaultdict(int)
    total = 0
    for line in text.splitlines():
        if line.lstrip().startswith("- {") or line.lstrip().startswith("-"):
            total += 1
        m = SOURCE_RE.search(line)
        if m:
            sources[m.group(1).strip()] += 1
    return total, dict(sources)


def check_source_exists(lang_code: str, stem: str) -> bool:
    """Resolve a source stem in the Language wiki for the given language."""
    lang_dir = WIKI_DIR / LANG_MAP[lang_code]
    for sub in ("vocabulary", "expressions"):
        candidate = lang_dir / sub / f"{stem}.md"
        if candidate.exists():
            return True
    return False


def build_report(langs: list[str]) -> CitationReport:
    rep = CitationReport()
    for code in langs:
        total, sources = collect_corpus_sources(code)
        rep.total_entries += total
        rep.total_unique_sources += len(sources)
        for stem, count in sorted(sources.items()):
            if not check_source_exists(code, stem):
                rep.findings.append(CitationFinding(
                    lang=code, source_stem=stem, entry_count=count
                ))
    return rep


def format_summary(rep: CitationReport) -> str:
    lines = [
        "=" * 78,
        f"REVERSE-PIPELINE CITATION REPORT — {date.today().isoformat()}",
        "=" * 78,
        "",
        f"Game corpus total entries scanned: {rep.total_entries}",
        f"Game corpus total unique source citations: {rep.total_unique_sources}",
        f"Missing Language wiki targets: {len(rep.findings)}",
        "",
    ]
    if not rep.findings:
        lines.append("✅ All corpus source citations resolve to Language wiki pages.")
        return "\n".join(lines)
    lines.append("⚠️  Missing citations detected:")
    lines.append("")
    by_lang: dict[str, list[CitationFinding]] = defaultdict(list)
    for f in rep.findings:
        by_lang[f.lang].append(f)
    for lang_code, items in sorted(by_lang.items()):
        lines.append(f"  [{lang_code}] {len(items)} missing:")
        for it in sorted(items, key=lambda x: -x.entry_count):
            lines.append(
                f"    - {it.source_stem:<50} (cited by {it.entry_count} entries)"
            )
        lines.append("")
    lines.append("Recommendation: create the cited theme file in")
    lines.append("Language/wiki/{Lang}/{vocabulary,expressions}/{stem}.md,")
    lines.append("then run `generate_yaml_pipeline.py` to seed YAML.")
    return "\n".join(lines)


def format_markdown_report(rep: CitationReport) -> str:
    lines = [
        "# Reverse-Pipeline Citation Report",
        "",
        f"**Generated**: {date.today().isoformat()}",
        f"**Tool**: `tools/reverse_pipeline.py`",
        f"**Scope**: Game corpus (`Game/lingotype/raw/{{lang}}_words.md`) × Language wiki themes",
        "",
        "## Summary",
        "",
        f"- Game corpus entries scanned: **{rep.total_entries}**",
        f"- Game corpus unique source citations: **{rep.total_unique_sources}**",
        f"- Missing Language wiki targets: **{len(rep.findings)}**",
        "",
    ]
    if not rep.findings:
        lines.append("✅ All corpus source citations resolve to Language wiki pages.")
    else:
        lines.append("## Missing Citations (per language)")
        lines.append("")
        by_lang: dict[str, list[CitationFinding]] = defaultdict(list)
        for f in rep.findings:
            by_lang[f.lang].append(f)
        for lang_code, items in sorted(by_lang.items()):
            lang_name = LANG_MAP[lang_code]
            lines.append(f"### {lang_name} (`{lang_code}_words.md`) — {len(items)} missing")
            lines.append("")
            lines.append("| Stem | Cited by | Action |")
            lines.append("|---|---:|---|")
            for it in sorted(items, key=lambda x: -x.entry_count):
                lines.append(
                    f"| `{it.source_stem}` | {it.entry_count} entries | create `Language/wiki/{lang_name}/vocabulary/{it.source_stem}.md` |"
                )
            lines.append("")
        lines.append("## Recommended Next Steps")
        lines.append("")
        lines.append("For each missing stem:")
        lines.append("1. Add raw source to `Language/raw/{Lang}/` (textbook, article, etc.)")
        lines.append("2. Create theme file `Language/wiki/{Lang}/vocabulary/{stem}.md` with `### {word}` sections")
        lines.append("3. Run `tools/generate_yaml_pipeline.py --lang {lang}` to seed Pipeline Form YAML")
        lines.append("4. Update `Language/wiki/{Lang}/index.md` to include new theme file")
        lines.append("5. Append `## [YYYY-MM-DD] ingest | {stem}` to `Language/log.md`")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--lang", choices=list(LANG_MAP), help="restrict to one language")
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    parser.add_argument("--report", help="write Markdown report to this path")
    args = parser.parse_args()

    langs = [args.lang] if args.lang else list(LANG_MAP)
    rep = build_report(langs)

    if args.json:
        out = {
            "date": date.today().isoformat(),
            "total_entries": rep.total_entries,
            "total_unique_sources": rep.total_unique_sources,
            "findings": [
                {"lang": f.lang, "source_stem": f.source_stem, "entry_count": f.entry_count}
                for f in rep.findings
            ],
        }
        print(json.dumps(out, indent=2, ensure_ascii=False))
        return 1 if rep.findings else 0

    print(format_summary(rep))
    if args.report:
        report_path = Path(args.report)
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(format_markdown_report(rep), encoding="utf-8")
        print(f"\nMarkdown report written to: {report_path}")
    return 1 if rep.findings else 0


if __name__ == "__main__":
    sys.exit(main())