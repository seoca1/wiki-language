#!/usr/bin/env python3
"""Add YAML frontmatter to expression theme files that lack it.

Targets the 65 expression files (13 per language × 5 languages) identified by
the 2026-08-14 symmetry check as missing frontmatter (title/language/category/
level/source). Reads the `**Level:**` (or `**Nivel:**` / `**レベル:**` / `**레벨:**`)
marker from each file's content to populate the `level:` field; defaults to
"A1-A2" when no level marker is found.

Idempotent: skips files that already have frontmatter (start with `---` line).

Usage:
  python3 Language/tools/add_expression_frontmatter.py [--dry-run] [--lang kr]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
LANG_DIR = SCRIPT_DIR.parent
WIKI_DIR = LANG_DIR / "wiki"

MAIN_LANGS = ["English", "Spanish", "Japanese", "Korean", "Chinese"]

LEVEL_PATTERNS = [
    re.compile(r"\*\*Level:\*\*\s*([A-Za-z0-9\-/]+)"),
    re.compile(r"\*\*Nivel:\*\*\s*([A-Za-z0-9\-/]+)"),
    re.compile(r"\*\*レベル:\*\*\s*([A-Za-z0-9\-/]+)"),
    re.compile(r"\*\*레벨:\*\*\s*([A-Za-z0-9\-/]+)"),
    re.compile(r"\*\*레벨\s*[:：]\*\*\s*([A-Za-z0-9\-/]+)"),
]


def has_frontmatter(text: str) -> bool:
    return text.lstrip().startswith("---")


def extract_level(text: str) -> str:
    for pat in LEVEL_PATTERNS:
        m = pat.search(text[:1500])
        if m:
            return m.group(1).strip()
    return "A1-A2"


def build_frontmatter(stem: str, lang: str, level: str) -> str:
    title = f"{stem} ({lang}) expressions"
    return (
        "---\n"
        f'title: "{title}"\n'
        f'language: "{lang}"\n'
        f'category: "{stem}"\n'
        f'level: "{level}"\n'
        "---\n\n"
    )


def add_frontmatter_to_file(path: Path, lang: str, dry_run: bool) -> tuple[bool, str]:
    text = path.read_text(encoding="utf-8")
    if has_frontmatter(text):
        return False, f"  = SKIP (has frontmatter): {path.name}"
    level = extract_level(text)
    stem = path.stem
    fm = build_frontmatter(stem, lang, level)
    new_text = fm + text
    if dry_run:
        return True, f"  + would ADD frontmatter (level={level}): {path.name}"
    path.write_text(new_text, encoding="utf-8")
    return True, f"  + ADDED frontmatter (level={level}): {path.name}"


def discover_missing_files(lang: str) -> list[Path]:
    d = WIKI_DIR / lang / "expressions"
    if not d.exists():
        return []
    out = []
    for path in sorted(d.glob("*.md")):
        if path.name.endswith(".ko.md"):
            continue
        if not has_frontmatter(path.read_text(encoding="utf-8")):
            out.append(path)
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description="Add YAML frontmatter to expression theme files.")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")
    parser.add_argument("--lang", choices=[l.lower() for l in MAIN_LANGS], help="Process only this language")
    args = parser.parse_args()

    langs = [args.lang.capitalize()] if args.lang else MAIN_LANGS
    total_added = 0
    total_skipped = 0

    for lang in langs:
        files = discover_missing_files(lang)
        print(f"[frontmatter] {lang}: {len(files)} files need frontmatter")
        for path in files:
            changed, msg = add_frontmatter_to_file(path, lang, args.dry_run)
            if changed:
                total_added += 1
            else:
                total_skipped += 1
            print(msg)
        print()

    print(f"Summary: {total_added} added, {total_skipped} skipped")
    if args.dry_run:
        print("(dry-run mode: no files written)")
    return 0


if __name__ == "__main__":
    sys.exit(main())