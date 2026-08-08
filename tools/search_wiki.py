#!/usr/bin/env python3
"""
Hybrid keyword search across Language wiki pages.

Lightweight alternative to `qmd` (per schema/AGENTS.md §Tools) — works
without external dependencies. Searches:

1. **Title** (H1 / page filename)
2. **Section headings** (H2 / H3 — direct match in heading line)
3. **Body** (full-text keyword match with surrounding context)

Filters:
- `--lang {en,es,jp,kr,zh}` — only this language
- `--page-type {vocabulary,expressions,culture,grammar,sources,study-plan,comparative}`
- `--include-yaml` — also search YAML pipeline entries (vocabulary only)
- `--limit N` — max results (default 20)

Output: ranked list of matches with file path, matched section, snippet.

Usage:
  python3 Language/tools/search_wiki.py "ttsumami"
  python3 Language/tools/search_wiki.py "subjunctive" --lang es
  python3 Language/tools/search_wiki.py "gustar" --page-type grammar
  python3 Language/tools/search_wiki.py "idol" --limit 10
  python3 Language/tools/search_wiki.py --help

Exit codes:
  0 = matches found
  1 = no matches
  2 = runtime error
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

# Resolve Language/ absolute path from this script's location.
SCRIPT_DIR = Path(__file__).resolve().parent
LANG_DIR = SCRIPT_DIR.parent
WIKI_DIR = LANG_DIR / "wiki"

LANG_DIRS = ("English", "Spanish", "Japanese", "Korean", "Chinese")
SHORT_TO_FULL = {
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
PAGE_TYPE_DIRS = {
    "vocabulary": "vocabulary",
    "expressions": "expressions",
    "culture": "culture",
    "grammar": "grammar",
    "sources": "sources",
    "study-plan": "study-plan",
}

# Heading regex — capture H1/H2/H3 with text
HEADING_RE = re.compile(r"^(#{1,3})\s+(.+?)\s*$", re.MULTILINE)
FRONT_RE = re.compile(r"\A---\n.*?\n---\n", re.DOTALL)
CODE_BLOCK_RE = re.compile(r"```.*?```", re.DOTALL)


@dataclass
class Match:
    """Single search match with context."""
    path: Path
    lang: str
    page_type: str
    heading: str  # closest preceding heading
    snippet: str  # text snippet around match
    score: int  # higher = more relevant


def get_page_type(path: Path) -> str:
    """Determine page type from path location."""
    parts = path.parts
    for i, part in enumerate(parts):
        if part in LANG_DIRS and i + 1 < len(parts):
            sub = parts[i + 1]
            if sub in PAGE_TYPE_DIRS.values():
                # Convert dir name to type name (e.g., 'study-plan' → 'study-plan')
                return sub
            if sub == "comparative":
                return "comparative"
    return "other"


def find_nearest_heading(text: str, position: int) -> str:
    """Find the most recent heading before `position`."""
    best = "(top of file)"
    for m in HEADING_RE.finditer(text):
        if m.start() > position:
            break
        best = m.group(2)
    return best


def make_snippet(text: str, position: int, query_len: int, ctx_chars: int = 80) -> str:
    """Extract a text snippet around the match position."""
    start = max(0, position - ctx_chars)
    end = min(len(text), position + query_len + ctx_chars)
    snippet = text[start:end].replace("\n", " ").strip()
    if start > 0:
        snippet = "..." + snippet
    if end < len(text):
        snippet = snippet + "..."
    return snippet


def search_file(path: Path, lang: str, query: str, include_yaml: bool) -> list[Match]:
    """Search a single file for query. Returns list of matches sorted by score."""
    text = path.read_text(encoding="utf-8")
    page_type = get_page_type(path)
    matches = []
    query_lower = query.lower()

    # Strip frontmatter + code blocks for body search
    text_searchable = FRONT_RE.sub("", text)
    if not include_yaml:
        text_searchable = CODE_BLOCK_RE.sub("", text_searchable)

    # 1. Title match (filename stem)
    if query_lower in path.stem.lower():
        matches.append(Match(
            path=path,
            lang=lang,
            page_type=page_type,
            heading="(filename)",
            snippet=path.stem,
            score=100,
        ))

    # 2. Heading match (H1/H2/H3)
    for m in HEADING_RE.finditer(text):
        heading_text = m.group(2)
        if query_lower in heading_text.lower():
            matches.append(Match(
                path=path,
                lang=lang,
                page_type=page_type,
                heading=f"H{m.group(1).count('#')}: {heading_text}",
                snippet=heading_text,
                score=80,
            ))

    # 3. Body keyword match
    body_lower = text_searchable.lower()
    pos = 0
    while True:
        idx = body_lower.find(query_lower, pos)
        if idx == -1:
            break
        heading = find_nearest_heading(text_searchable, idx)
        snippet = make_snippet(text_searchable, idx, len(query))
        # Score by frequency (more matches = higher), but cap
        n_total = body_lower.count(query_lower)
        matches.append(Match(
            path=path,
            lang=lang,
            page_type=page_type,
            heading=heading,
            snippet=snippet,
            score=min(50, 30 + n_total),
        ))
        pos = idx + 1

    # Deduplicate by (path, heading) — keep highest score
    seen = {}
    for m in matches:
        key = (m.path, m.heading)
        if key not in seen or seen[key].score < m.score:
            seen[key] = m

    return list(seen.values())


def discover_files(lang_filter: Optional[str], page_type_filter: Optional[str]) -> list[tuple[Path, str, str]]:
    """Discover wiki files matching filters. Returns (path, lang, page_type)."""
    results = []
    if lang_filter:
        canonical = SHORT_TO_FULL.get(lang_filter.lower())
        langs = [canonical] if canonical else []
    else:
        langs = list(LANG_DIRS)

    for lang in langs:
        wiki_lang = WIKI_DIR / lang
        if not wiki_lang.exists():
            continue
        for path in wiki_lang.rglob("*.md"):
            if path.name.endswith(".ko.md"):
                continue
            page_type = get_page_type(path)
            if page_type == "other":
                continue
            if page_type_filter and page_type != page_type_filter:
                continue
            results.append((path, lang, page_type))

    # Comparative
    if not page_type_filter or page_type_filter == "comparative":
        comp_dir = WIKI_DIR / "comparative"
        if comp_dir.exists():
            for path in comp_dir.glob("*.md"):
                if path.name.endswith(".ko.md"):
                    continue
                if path.stem in {"index", "log", "README", "FINAL_STATUS", "comparative-template"}:
                    continue
                results.append((path, "comparative", "comparative"))

    return results


def print_match(m: Match, rank: int, show_score: bool = False) -> None:
    """Pretty-print a single match."""
    rel = m.path.relative_to(LANG_DIR)
    snippet = m.snippet[:160]
    line = f"  [{rank:2}] {m.lang}/{rel}  ({m.page_type})"
    if show_score:
        line += f"  score={m.score}"
    line += f"\n       heading: {m.heading}"
    line += f"\n       match:   {snippet}"
    print(line)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Hybrid keyword search across Language wiki pages. "
                    "Lightweight alternative to qmd (no external deps)."
    )
    parser.add_argument("query", help="Search query (case-insensitive)")
    parser.add_argument(
        "--lang",
        choices=list(SHORT_TO_FULL.keys()),
        help="Only this language (en/es/jp/kr/zh)",
    )
    parser.add_argument(
        "--page-type",
        choices=list(PAGE_TYPE_DIRS.keys()) + ["comparative"],
        help="Only this page type",
    )
    parser.add_argument(
        "--include-yaml",
        action="store_true",
        help="Include YAML pipeline entries in body search (vocab files)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=20,
        help="Max results to display (default 20)",
    )
    parser.add_argument(
        "--show-score",
        action="store_true",
        help="Show match scores (for debugging)",
    )
    args = parser.parse_args()

    files = discover_files(args.lang, args.page_type)
    if not files:
        print(f"[search] No files found (lang={args.lang}, page_type={args.page_type})", file=sys.stderr)
        return 2

    all_matches: list[Match] = []
    for path, lang, _ in files:
        file_matches = search_file(path, lang, args.query, args.include_yaml)
        all_matches.extend(file_matches)

    # Sort by score (highest first), then by path for stable order
    all_matches.sort(key=lambda m: (-m.score, str(m.path)))

    if not all_matches:
        print(f"[search] No matches for '{args.query}'")
        print(f"  Searched: {len(files)} files")
        return 1

    # Deduplicate — same path should appear once with highest score
    seen_paths = set()
    deduped = []
    for m in all_matches:
        if m.path in seen_paths:
            continue
        seen_paths.add(m.path)
        deduped.append(m)

    # Apply limit
    limited = deduped[:args.limit]
    truncated = len(deduped) - len(limited)

    print(f"[search] '{args.query}' — {len(deduped)} files matched")
    print(f"  Searched: {len(files)} files")
    if args.lang:
        print(f"  Language: {args.lang}")
    if args.page_type:
        print(f"  Page type: {args.page_type}")
    if args.include_yaml:
        print(f"  YAML entries: included")
    print()
    for i, m in enumerate(limited, 1):
        print_match(m, i, args.show_score)

    if truncated > 0:
        print(f"\n  ... {truncated} more matches (use --limit {args.limit + truncated} to see all)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
