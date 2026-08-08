#!/usr/bin/env python3
"""
Fix missing `level:` field in vocabulary theme file frontmatter.

Handles 3 cases:
1. File has frontmatter but no `level:` → add `level:` line
2. File has inline `**Level:**` but no frontmatter → create frontmatter from inline
3. File has frontmatter `level:` → skip (already correct)

Usage:
  python3 Language/tools/add_vocabulary_level.py [--dry-run]
  python3 Language/tools/add_vocabulary_level.py --help

Exit codes:
  0 = success
  1 = error
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

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

FRONT_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
INLINE_LEVEL_RE = re.compile(r"\*\*Level:\*\*\s*([^\n]+)")


def has_frontmatter(text: str) -> bool:
    return bool(FRONT_RE.match(text))


def has_frontmatter_level(text: str) -> bool:
    """Check if frontmatter has `level:` field."""
    if not has_frontmatter(text):
        return False
    fm = FRONT_RE.match(text).group(1)
    for line in fm.splitlines():
        if line.strip().startswith("level:"):
            return True
    return False


def get_inline_level(text: str) -> str | None:
    """Extract level from inline `**Level:**` marker."""
    m = INLINE_LEVEL_RE.search(text)
    if m:
        return m.group(1).strip()
    return None


def add_level_to_frontmatter(text: str, level: str) -> str:
    """Add `level:` line to existing frontmatter."""
    m = FRONT_RE.match(text)
    fm_body = m.group(1)
    # Append level: line at end of frontmatter
    new_fm = fm_body.rstrip() + f'\nlevel: "{level}"'
    new_text = f"---\n{new_fm}\n---\n" + text[m.end():]
    return new_text


def create_frontmatter(text: str, level: str, lang: str) -> str:
    """Create frontmatter block at start of file from inline metadata.

    Uses inferred theme/category/source from existing frontmatter-less file.
    Falls back to 'mixed' / 'vocabulary' / 'unknown' defaults.
    """
    # Try to infer theme from filename or existing inline Source
    theme_match = re.search(r"\*\*Theme:\*\*\s*([^\n]+)", text)
    theme = theme_match.group(1).strip() if theme_match else "vocabulary"
    source_match = re.search(r"\*\*Source:\*\*\s*\[\[([^\]]+)\]\]", text)
    source = source_match.group(1) if source_match else "unknown"
    # Use simple category (strip -vocabulary suffix)
    category = source.replace("-vocabulary", "") if source != "unknown" else "mixed"

    fm = (
        f'---\n'
        f'category: "{category}"\n'
        f'theme: "{theme}"\n'
        f'level: "{level}"\n'
        f'source: "{source}"\n'
        f'---\n\n'
    )
    return fm + text.lstrip()


def process_file(path: Path, dry_run: bool = False) -> tuple[bool, str]:
    """Process a vocabulary theme file.

    Returns (modified, msg).
    """
    text = path.read_text(encoding="utf-8")

    # Skip .ko.md (translation pairs)
    if path.name.endswith(".ko.md"):
        return False, "  - (skipped .ko.md)"

    # Already has frontmatter level
    if has_frontmatter_level(text):
        return False, "  = already has level:"

    inline_level = get_inline_level(text)

    if has_frontmatter(text):
        if inline_level:
            new_text = add_level_to_frontmatter(text, inline_level)
            if not dry_run:
                path.write_text(new_text, encoding="utf-8")
            return True, f"  + added `level: \"{inline_level}\"` to existing frontmatter"
        else:
            # No inline level — use generic default
            new_text = add_level_to_frontmatter(text, "A1-B1")
            if not dry_run:
                path.write_text(new_text, encoding="utf-8")
            return True, f"  + added `level: \"A1-B1\"` (no inline available)"
    else:
        # No frontmatter — create from inline metadata
        if inline_level:
            lang_short = path.parent.parent.name.lower()
            new_text = create_frontmatter(text, inline_level, lang_short)
            if not dry_run:
                path.write_text(new_text, encoding="utf-8")
            return True, f"  + created frontmatter with level: \"{inline_level}\""
        else:
            return False, "  - (no inline level either — manual fix needed)"


def discover_files(lang_filter: str | None) -> list[Path]:
    """Find vocabulary theme files with missing frontmatter level."""
    results = []
    langs = [SHORT_TO_FULL[lang_filter.lower()]] if lang_filter else list(LANG_DIRS)
    for lang in langs:
        vocab_dir = WIKI_DIR / lang / "vocabulary"
        if not vocab_dir.exists():
            continue
        for path in sorted(vocab_dir.glob("*.md")):
            if path.name.endswith(".ko.md"):
                continue
            text = path.read_text(encoding="utf-8")
            if not has_frontmatter_level(text):
                results.append(path)
    return results


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Fix missing `level:` field in vocabulary theme file frontmatter."
    )
    parser.add_argument(
        "--lang",
        choices=list(SHORT_TO_FULL.keys()),
        help="Only this language (default: all 5)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without writing",
    )
    args = parser.parse_args()

    files = discover_files(args.lang)
    if not files:
        print(f"[fix_level] No files need fixing", file=sys.stderr)
        return 0

    total_modified = 0
    for path in files:
        rel = path.relative_to(LANG_DIR)
        modified, msg = process_file(path, dry_run=args.dry_run)
        marker = "[dry-run]" if args.dry_run else "[fix_level]"
        print(f"{marker} {rel}")
        print(msg)
        if modified:
            total_modified += 1

    print()
    if args.dry_run:
        print(f"[dry-run] Would modify {total_modified} files")
    else:
        print(f"[fix_level] Modified {total_modified} files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
