#!/usr/bin/env python3
"""
Auto-inject missing `category:` field into Game corpus YAML entries.

Background (Track E audit_downstream.py findings, 2026-08-08):
- Game/typing_language/raw/jp_words.md: 259 entries missing category
- Game/typing_language/raw/kr_words.md: 662 entries missing category
- All missing entries reference `[[basic-vocabulary]]` or `[[travel]]`

Strategy:
- For each entry missing `category:`, infer category from `source:` wikilink
- Map: `source: [[{theme}]]` → `category: {theme_stem_without_suffix}`
  - `[[basic-vocabulary]]` → `category: basic`
  - `[[travel]]` → `category: travel`
  - `[[food-vocabulary]]` → `category: food`
  - etc.

This is a coarse mapping (some entries in basic-vocabulary.md have sub-categories
like 'greeting', 'number', 'color'). For entries without sub-category hints,
this is the safest fallback consistent with existing entries that use
`category: basic` for basic-vocabulary references.

Usage:
  python3 Language/tools/add_game_category.py [--lang jp] [--dry-run]
  python3 Language/tools/add_game_category.py --help

Exit codes:
  0 = success (changes made or no changes needed)
  1 = error
  2 = runtime error
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Optional

# Resolve paths from script location
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent
GAME_RAW_DIR = PROJECT_ROOT / "Game" / "typing_language" / "raw"

# Pattern: capture {theme} from source: [[{theme}]]
SOURCE_FIELD_RE = re.compile(r'source:\s*"?\[\[([^\]]+)\]\]"?')

# Pattern: detect if entry has category field
CATEGORY_FIELD_RE = re.compile(r'\bcategory:')

# Pattern: YAML entry line (id-prefixed)
YAML_ENTRY_RE = re.compile(r"^(\s*)-\s*\{\s*id:\s*(\w+),(.*)\}\s*$")


def derive_category_from_source(source_wikilink: str) -> Optional[str]:
    """Derive category stem from source wikilink like `[[basic-vocabulary]]` → `basic`.

    Strategy:
    1. Strip [[ ]]
    2. Strip section anchor (#...)
    3. Strip `-vocabulary` suffix
    4. Take last component if path-style
    """
    inner = source_wikilink.strip("[]").strip()
    if "#" in inner:
        inner = inner.split("#", 1)[0]
    # Path-style (Language/Spanish/vocabulary/foo) → take last
    if "/" in inner:
        inner = inner.split("/")[-1]
    # Strip -vocabulary suffix
    if inner.endswith("-vocabulary"):
        inner = inner[: -len("-vocabulary")]
    return inner or None


def add_category_to_entry(line: str) -> tuple[str, bool]:
    """Add `category:` field to a single YAML entry line if missing.

    Returns (new_line, was_modified).
    """
    m = YAML_ENTRY_RE.match(line)
    if not m:
        return line, False

    indent, entry_id, fields_str = m.groups()

    # Skip sentence entries (they don't need category per ADR-0003 spec)
    if "_" in entry_id:
        prefix, num = entry_id.rsplit("_", 1)
        if len(prefix) == 3 and prefix.endswith("s") and prefix[:2].isalpha() and num.isdigit():
            return line, False

    # If category already present, skip
    if CATEGORY_FIELD_RE.search(fields_str):
        return line, False

    # Find source field
    source_match = SOURCE_FIELD_RE.search(fields_str)
    if not source_match:
        return line, False  # Can't infer without source

    category = derive_category_from_source(source_match.group(1))
    if not category:
        return line, False

    # Insert category before source field
    # Pattern: `, source: ...` → `, category: {category}, source: ...`
    new_fields = re.sub(
        r'(\s*,\s*source:\s*)',
        f', category: {category}\\1',
        fields_str,
        count=1,
    )

    new_line = f"{indent}- {{ id: {entry_id},{new_fields} }}"
    return new_line, True


def process_file(path: Path, dry_run: bool = False) -> tuple[int, int]:
    """Process one game corpus file.

    Returns (modified_count, missing_count).
    """
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)

    modified = 0
    missing_count = 0
    new_lines = []

    for line in lines:
        if YAML_ENTRY_RE.match(line):
            new_line, was_modified = add_category_to_entry(line.rstrip("\n"))
            if was_modified:
                missing_count += 1
                modified += 1
                new_lines.append(new_line + "\n")
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)

    if modified > 0 and not dry_run:
        new_text = "".join(new_lines)
        path.write_text(new_text, encoding="utf-8")

    return modified, missing_count


def is_sentence_id(entry_id: str) -> bool:
    """Detect sentence IDs (ens_001, jps_001, etc.) — skip these."""
    if "_" not in entry_id:
        return False
    parts = entry_id.rsplit("_", 1)
    if len(parts) != 2:
        return False
    prefix, num = parts
    return len(prefix) == 3 and prefix.endswith("s") and num.isdigit()


def discover_files(lang_filter: Optional[str]) -> list[Path]:
    """Find game corpus files."""
    results = []
    for path in sorted(GAME_RAW_DIR.glob("*_words.md")):
        if lang_filter and not path.stem.startswith(lang_filter):
            continue
        results.append(path)
    return results


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Auto-inject missing `category:` field into Game corpus YAML entries (Track E fix batch)."
    )
    parser.add_argument(
        "--lang",
        choices=["en", "es", "jp", "kr"],
        help="Process only this language (default: all 4)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without writing files",
    )
    args = parser.parse_args()

    files = discover_files(args.lang)
    if not files:
        print(f"[add_category] No game corpus files found (filter: lang={args.lang or 'all'})", file=sys.stderr)
        return 2

    total_modified = 0
    total_missing = 0
    for path in files:
        modified, missing = process_file(path, dry_run=args.dry_run)
        rel = path.relative_to(PROJECT_ROOT)
        marker = "[dry-run]" if args.dry_run else "[add_category]"
        if modified > 0:
            print(f"{marker} {rel}: +{modified} entries fixed ({missing} total missing)")
        else:
            print(f"{marker} {rel}: clean (0 missing)")
        total_modified += modified
        total_missing += missing

    print()
    if args.dry_run:
        print(f"[dry-run] Would modify {total_modified} entries ({total_missing} missing total)")
    else:
        print(f"[add_category] Modified {total_modified} entries ({total_missing} missing total)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
