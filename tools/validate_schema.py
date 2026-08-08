#!/usr/bin/env python3
"""
Validate Language wiki page schemas (vocabulary, expressions, culture,
grammar, sources, study-plan, comparative).

Companion to `generate_yaml_pipeline.py` (which only handles vocabulary YAML).
This tool validates the broader page format conventions per ADR-0001, ADR-0002,
ADR-0003, and `Language/schema/AGENTS.md`.

Usage:
  python3 Language/tools/validate_schema.py [--lang en] [--page-type vocabulary]
  python3 Language/tools/validate_schema.py --help

Exit codes:
  0 = clean (0 violations)
  1 = violations found
  2 = runtime error
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

# Resolve Language/ absolute path from this script's location.
SCRIPT_DIR = Path(__file__).resolve().parent
LANG_DIR = SCRIPT_DIR.parent
WIKI_DIR = LANG_DIR / "wiki"

# Per-language wiki subdirectories.
LANG_DIRS = ("English", "Spanish", "Japanese", "Korean", "Chinese")

# Page type → directory mapping
PAGE_TYPE_DIRS = {
    "vocabulary": "vocabulary",
    "expressions": "expressions",
    "culture": "culture",
    "grammar": "grammar",
    "sources": "sources",
    "study-plan": "study-plan",
}

# Frontmatter / inline metadata markers
FRONT_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
INLINE_SOURCE_RE = re.compile(r"\*\*Source:\*\*\s*([^\n]+)")
INLINE_THEME_RE = re.compile(r"\*\*Theme:\*\*\s*([^\n]+)")
INLINE_LEVEL_RE = re.compile(r"\*\*Level:\*\*\s*([^\n]+)")
INLINE_TYPE_RE = re.compile(r"\*\*Type:\*\*\s*([^\n]+)")
INLINE_DATE_RE = re.compile(r"\*\*Date Added:\*\*\s*([^\n]+)")
KOREAN_SUMMARY_RE = re.compile(r"> 🇰🇷 \*\*한국어 요약", re.IGNORECASE)


@dataclass
class PageReport:
    """Single page validation report."""
    path: Path
    lang: str
    page_type: str
    violations: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.violations


def get_page_type(path: Path) -> str:
    """Determine page type from directory location.

    Returns: 'vocabulary', 'expressions', 'culture', 'grammar', 'sources',
             'study-plan', 'comparative', or 'other'.
    """
    parts = path.parts
    # Find the position of {Lang} in path
    for i, part in enumerate(parts):
        if part in LANG_DIRS:
            if i + 1 < len(parts):
                sub = parts[i + 1]
                if sub in PAGE_TYPE_DIRS:
                    return sub
                elif sub == "comparative":
                    return "comparative"
            return "other"
    return "other"


def has_frontmatter(text: str) -> bool:
    return bool(FRONT_RE.match(text))


def has_korean_summary(text: str) -> bool:
    return bool(KOREAN_SUMMARY_RE.search(text))


def has_sources_section(text: str) -> bool:
    """Check for `## Sources` or `## 출처` heading."""
    return bool(re.search(r"^##\s+(Sources|출처|Fuente|出典|来源)\s*$", text, re.MULTILINE | re.IGNORECASE))


def has_pipeline_section(text: str) -> bool:
    return bool(re.search(r"^##\s+Pipeline Form(?:\s+\(machine-readable\))?\s*$", text, re.MULTILINE | re.IGNORECASE))


def has_overview(text: str) -> bool:
    # Accept both `**Overview:**` (no space) and `**Overview**: ` (space, no closing **)
    return bool(re.search(r"\*\*Overview:?\*\*?", text))


def has_key_points(text: str) -> bool:
    return bool(re.search(r"^##\s+(Key Points|주요 포인트)\s*$", text, re.MULTILINE | re.IGNORECASE))


def has_ejemplos(text: str) -> bool:
    """For Spanish/Chinese culture pages (openclaw contract)."""
    return bool(re.search(r"^##\s+(Ejemplos|例)\s*$", text, re.MULTILINE | re.IGNORECASE))


def word_count(text: str) -> int:
    """Approximate word count (whitespace-separated tokens)."""
    return len(text.split())


def validate_vocabulary_page(path: Path, lang: str, text: str) -> list[str]:
    """Validate vocabulary theme file schema.

    Per ADR-0001 (theme-file) + ADR-0003 (Pipeline YAML):
    - frontmatter with `level:` field (or inline `**Level:**` fallback)
    - `## Pipeline Form` YAML section
    - Top-level `## Sources` section is OPTIONAL — many existing files
      have per-word `#### Sources` instead. Schema doesn't require top-level.
    - One or more `### {word}` sections
    """
    violations = []

    if not has_frontmatter(text):
        violations.append("missing frontmatter (expected `level:` / `source:` / `category:` fields)")
    else:
        fm = {}
        for line in FRONT_RE.match(text).group(1).splitlines():
            if ":" in line and not line.startswith(" "):
                k, _, v = line.partition(":")
                fm[k.strip()] = v.strip().strip('"').strip("'")
        if not fm.get("level"):
            # Fallback: check inline `**Level:**`
            if not INLINE_LEVEL_RE.search(text):
                violations.append("missing `level:` field (neither frontmatter nor inline)")

    if not has_pipeline_section(text):
        violations.append("missing `## Pipeline Form (machine-readable)` section (ADR-0003)")

    n_h3 = len(re.findall(r"^###\s+", text, re.MULTILINE))
    if n_h3 == 0:
        violations.append("no `### {word}` sections found (theme file should have ≥1 word)")

    return violations


def validate_culture_page(path: Path, lang: str, text: str) -> list[str]:
    """Validate culture page schema.

    Per schema/AGENTS.md §3.4:
    - Overview (inline `**Overview:**` OR `## Overview` heading)
    - Key Points or equivalent (Key Values / Setting / Themes / etc.)
    - Sources section (English or localized)
    - Optional: `## Ejemplos` for Spanish (openclaw contract)
    - Word count threshold (≥200 recommended)

    Existing culture files use multiple schema variants:
    - Older: inline `**Overview:**` + `## Key Points`
    - Newer: `## Overview` + `## Key Values` / `## Setting` / etc.
    Both forms accepted.
    """
    violations = []

    # Overview: inline OR `## Overview` heading
    if not has_overview(text):
        if not re.search(r"^##\s+Overview\s*$", text, re.MULTILINE | re.IGNORECASE):
            violations.append("missing `**Overview:**` line (or `## Overview` heading)")

    # Key Points / Key Values / Setting / Themes (any h2 section besides Sources/Ejemplos)
    if not has_key_points(text):
        # Check for any h2 heading (excluding Sources/Ejemplos/Summary/Pipeline)
        h2_sections = re.findall(r"^##\s+([^\n]+)$", text, re.MULTILINE)
        substantive = [s for s in h2_sections if not re.search(
            r"^(Sources|출처|Resumen|Ejemplos|例|Summary|Pipeline|Key\s*Points|Key\s*Values|Setting|Themes|Overview)$",
            s.strip(), re.IGNORECASE
        )]
        if not substantive:
            violations.append("missing `## Key Points` section (or similar h2 like `## Key Values` / `## Setting`)")

    if not has_sources_section(text):
        violations.append("missing `## Sources` section")

    # Spanish culture pages additionally need Ejemplos (openclaw contract)
    if lang == "Spanish" and not has_ejemplos(text):
        violations.append("missing `## Ejemplos` section (openclaw contract for Spanish culture)")

    # Word count threshold (soft warning — not a hard violation)
    wc = word_count(text)
    if wc < 200:
        violations.append(f"word count {wc} < 200 (recommend ≥300 for culture pages)")

    return violations


def validate_grammar_page(path: Path, lang: str, text: str) -> list[str]:
    """Validate grammar page schema.

    Per the 6 grammar pages added in Track B1 (EN/JA/KO) and pre-existing
    Spanish/Chinese grammar pages:
    - EN/JA/KO: Korean summary block (`> 🇰🇷 **한국어 요약`)
    - ES/ZH: bilingual Korean explanation acceptable
    - All: sources section (English `## Sources` or localized `## 출처`/`## Fuente`/`## 출처 (Fuente)`)
    """
    violations = []

    # Korean summary block required only for EN/JA/KO (Track B1 convention)
    # ES/ZH grammar pages use Korean inline explanation instead
    if lang in ("English", "Japanese", "Korean") and not has_korean_summary(text):
        violations.append("missing `> 🇰🇷 **한국어 요약 (Korean Summary)**` block (Track B1 convention)")

    # Sources section — accept English or localized variants
    if not has_sources_section(text):
        # Try additional patterns for Spanish/Chinese (which may use inline or different heading)
        if not re.search(r"##\s+(출처|원본|Fuente|出所|来源)", text, re.IGNORECASE):
            violations.append("missing `## Sources` / `## 출처` / `## Fuente` section")

    # Grammar pages should have meaningful content
    wc = word_count(text)
    if wc < 200:
        violations.append(f"word count {wc} < 200 (grammar pages should have ≥300 words)")

    return violations


def validate_source_page(path: Path, lang: str, text: str) -> list[str]:
    """Validate source summary page schema.

    Per schema/AGENTS.md §3.5:
    - `**Type:**` (textbook/novel/article/blog)
    - `**Date Added:**` YYYY-MM-DD (or frontmatter `date_added:`)
    - `**Language Level:**` (or frontmatter `language_level:`)
    - `## Summary` section
    - `## Sources` is OPTIONAL — some sources are self-citing (no separate source)

    Many existing source files use frontmatter (`date_added:`, `language_level:`)
    instead of inline `**Date Added:**`. Accept both.
    """
    violations = []

    if not INLINE_TYPE_RE.search(text):
        violations.append("missing `**Type:**` field")

    # Date: inline OR frontmatter
    if not INLINE_DATE_RE.search(text):
        if has_frontmatter(text):
            fm_body = FRONT_RE.match(text).group(1)
            if not re.search(r"^date_added:", fm_body, re.MULTILINE):
                violations.append("missing `**Date Added:**` field (YYYY-MM-DD) — also no `date_added:` in frontmatter")
        else:
            violations.append("missing `**Date Added:**` field (YYYY-MM-DD)")

    # Language Level: inline OR frontmatter
    if not re.search(r"\*\*Language Level:\*\*", text):
        if has_frontmatter(text):
            fm_body = FRONT_RE.match(text).group(1)
            if not re.search(r"^language_level:", fm_body, re.MULTILINE):
                violations.append("missing `**Language Level:**` field — also no `language_level:` in frontmatter")
        else:
            violations.append("missing `**Language Level:**` field")

    # ## Summary — required, accept many localized variants
    # Summary equivalents: Overview, Key Extractions, Key Points, 핵심, Núcleo, 核心, etc.
    summary_patterns = (
        r"^##\s+("
        r"Summary|Resumen|요약|핵심|주요\s*포인트|"
        r"まとめ|概要|総括|核心|ゲーム\s*活用|"
        r"总结|摘要|"
        r"Overview|"
        r"N[uú]cleo|Core|Key\s*(Extractions|Summary|Points)"
        r")"
    )
    if not re.search(summary_patterns, text, re.MULTILINE | re.IGNORECASE):
        violations.append("missing `## Summary` section (or localized variant: Overview/Resumen/요약/핵심/まとめ/总结)")

    return violations


def validate_expressions_page(path: Path, lang: str, text: str) -> list[str]:
    """Validate expression theme file schema (per ADR-0001).

    Per schema/AGENTS.md §3.2:
    - frontmatter with `level:` (or inline `**Level:**` fallback)
    - Multiple `## {expression}` OR `### {expression}` sections
    - `## Sources` is OPTIONAL — not all expression files have top-level Sources

    Existing expression files use both `## {expression}` (older) and
    `### {expression}` (newer convention) headings. Accept both.
    """
    violations = []

    if not has_frontmatter(text):
        if not INLINE_LEVEL_RE.search(text):
            violations.append("missing frontmatter (expected `level:` / `source:` / `category:` fields)")
    else:
        fm = {}
        for line in FRONT_RE.match(text).group(1).splitlines():
            if ":" in line and not line.startswith(" "):
                k, _, v = line.partition(":")
                fm[k.strip()] = v.strip().strip('"').strip("'")
        if not fm.get("level") and not INLINE_LEVEL_RE.search(text):
            violations.append("missing `level:` field (neither frontmatter nor inline)")

    n_h2_or_h3 = len(re.findall(r"^#{2,3}\s+", text, re.MULTILINE))
    if n_h2_or_h3 == 0:
        violations.append("no expression sections found (expect `## {expression}` or `### {expression}` headings)")

    return violations


def validate_comparative_page(path: Path, lang: str, text: str) -> list[str]:
    """Validate comparative wiki page schema (per ADR-0004).

    Per ADR-0004:
    - `> **Theme:**` or intro section
    - Cross-language references
    - Inbound link from per-language index.md (orphan check is separate)
    """
    violations = []

    wc = word_count(text)
    if wc < 100:
        violations.append(f"word count {wc} < 100 (comparative pages should have ≥200 words)")

    return violations


def validate_study_plan_page(path: Path, lang: str, text: str) -> list[str]:
    """Validate study-plan page schema (looser convention).

    Per schema/AGENTS.md §3.6:
    - Personal study plans, weekly rotations, output workflows
    - Loose format — primarily narrative
    """
    # Study-plan pages are loosely formatted; only check for some content
    return []


def validate_page(path: Path, lang: str, page_type: str) -> PageReport:
    """Validate a single page based on its page type."""
    text = path.read_text(encoding="utf-8")
    report = PageReport(path=path, lang=lang, page_type=page_type)

    if page_type == "vocabulary":
        report.violations = validate_vocabulary_page(path, lang, text)
    elif page_type == "expressions":
        report.violations = validate_expressions_page(path, lang, text)
    elif page_type == "culture":
        report.violations = validate_culture_page(path, lang, text)
    elif page_type == "grammar":
        report.violations = validate_grammar_page(path, lang, text)
    elif page_type == "sources":
        report.violations = validate_source_page(path, lang, text)
    elif page_type == "comparative":
        report.violations = validate_comparative_page(path, lang, text)
    elif page_type == "study-plan":
        report.violations = validate_study_plan_page(path, lang, text)
    # Other types (log.md, index.md, etc.) skipped.

    return report


def discover_pages(lang_filter: str | None, page_type_filter: str | None) -> list[tuple[Path, str, str]]:
    """Discover all wiki pages and their (path, lang, page_type).

    Returns list of tuples.
    """
    # Map short codes and lowercased full names to canonical LANG_DIRS entries
    short_to_full = {
        "en": "English",
        "es": "Spanish",
        "jp": "Japanese",
        "kr": "Korean",
        "zh": "Chinese",
        "english": "English",
        "spanish": "Spanish",
        "japanese": "Japanese",
        "korean": "Korean",
        "chinese": "Chinese",
    }

    results = []
    if lang_filter:
        canonical = short_to_full.get(lang_filter.lower())
        langs = [canonical] if canonical else []
    else:
        langs = list(LANG_DIRS)
    for lang in langs:
        wiki_lang = WIKI_DIR / lang
        if not wiki_lang.exists():
            continue
        for path in sorted(wiki_lang.rglob("*.md")):
            # Skip per-word .ko.md translation pair files
            if path.name.endswith(".ko.md"):
                continue
            page_type = get_page_type(path)
            if page_type == "other":
                continue
            if page_type_filter and page_type != page_type_filter:
                continue
            results.append((path, lang, page_type))

    # Comparative pages
    if not page_type_filter or page_type_filter == "comparative":
        comp_dir = WIKI_DIR / "comparative"
        if comp_dir.exists():
            for path in sorted(comp_dir.glob("*.md")):
                if path.name.endswith(".ko.md"):
                    continue
                # Skip meta/status files
                if path.stem in {"index", "log", "README", "FINAL_STATUS", "comparative-template"}:
                    continue
                results.append((path, "comparative", "comparative"))

    return results


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate Language wiki page schemas. ADRs 0001-0004 + schema/AGENTS.md."
    )
    parser.add_argument(
        "--lang",
        choices=["en", "es", "jp", "kr", "zh", "english", "spanish", "japanese", "korean", "chinese"],
        help="Process only this language (default: all 5)",
    )
    parser.add_argument(
        "--page-type",
        choices=["vocabulary", "expressions", "culture", "grammar", "sources", "study-plan", "comparative"],
        help="Process only this page type (default: all)",
    )
    parser.add_argument(
        "--show-ok",
        action="store_true",
        help="Show files with no violations too (verbose)",
    )
    args = parser.parse_args()

    pages = discover_pages(args.lang, args.page_type)
    if not pages:
        print(f"[validate] No pages found (lang={args.lang}, page_type={args.page_type})", file=sys.stderr)
        return 2

    # Group violations by (lang, page_type)
    by_type: dict[str, list[PageReport]] = defaultdict(list)
    for path, lang, page_type in pages:
        report = validate_page(path, lang, page_type)
        by_type[page_type].append(report)

    total_violations = 0
    files_with_violations = 0
    files_clean = 0
    for page_type in sorted(by_type):
        reports = by_type[page_type]
        n_violations = sum(len(r.violations) for r in reports)
        n_bad = sum(1 for r in reports if not r.ok)
        n_ok = sum(1 for r in reports if r.ok)
        total_violations += n_violations
        files_with_violations += n_bad
        files_clean += n_ok

        print(f"\n=== {page_type.upper()} ({len(reports)} files) ===")
        for r in reports:
            if r.ok:
                if args.show_ok:
                    rel = r.path.relative_to(LANG_DIR)
                    print(f"  [ok] {r.lang}/{rel}")
                continue
            rel = r.path.relative_to(LANG_DIR)
            print(f"  [FAIL] {r.lang}/{rel}")
            for v in r.violations:
                print(f"    - {v}")

    print()
    print(f"=== Summary ===")
    print(f"Pages scanned: {len(pages)}")
    print(f"Files with violations: {files_with_violations}")
    print(f"Files clean: {files_clean}")
    print(f"Total violations: {total_violations}")

    if total_violations == 0:
        print("[validate] CLEAN")
        return 0
    print("[validate] VIOLATIONS FOUND")
    return 1


if __name__ == "__main__":
    sys.exit(main())
