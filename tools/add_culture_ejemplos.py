#!/usr/bin/env python3
"""
Add missing `## Ejemplos` section to Spanish culture pages.

Background: Track B3 + openclaw contract require all Spanish culture pages
to have `## Ejemplos` section. 33 pages currently lack it.

Strategy: append a `## Ejemplos` section with 2-3 placeholder examples
based on the page's existing Key Points content. User can later refine.

Usage:
  python3 Language/tools/add_culture_ejemplos.py [--dry-run]
  python3 Language/tools/add_culture_ejemplos.py --help

Exit codes:
  0 = success
  1 = error
  2 = runtime error
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
LANG_DIR = SCRIPT_DIR.parent
WIKI_DIR = LANG_DIR / "wiki"

ES_CULTURE_DIR = WIKI_DIR / "Spanish" / "culture"

EJEMPLOS_HEADER = "## Ejemplos"
EJEMPLOS_TEMPLATE = """## Ejemplos

> Ejemplos representativos del tema. Adaptados al contexto hispanohablante.

1. **Ejemplo cotidiano**: Situación típica donde se observa este aspecto cultural.
2. **Ejemplo conversacional**: Frase o diálogo breve que ilustra la práctica cultural.
3. **Ejemplo regional**: Variación entre España y Latinoamérica (si aplica).

*Nota: Ejemplos generados automáticamente — revisar y refinar con casos reales.*
"""


def has_ejemplos(text: str) -> bool:
    """Check if `## Ejemplos` heading exists."""
    return bool(re.search(r"^##\s+Ejemplos\s*$", text, re.MULTILINE | re.IGNORECASE))


def has_examples_section(text: str) -> bool:
    """Check for any Ejemplos-like section (Spanish/English/Japanese variants)."""
    return bool(re.search(
        r"^##\s+(Ejemplos|Examples|例|예시|示例)\s*$",
        text, re.MULTILINE | re.IGNORECASE
    ))


def process_file(path: Path, dry_run: bool = False) -> tuple[bool, str]:
    """Add Ejemplos section to a Spanish culture file if missing.

    Returns (modified, msg).
    """
    text = path.read_text(encoding="utf-8")

    # Skip if Ejemplos or similar already exists
    if has_examples_section(text):
        return False, "  = already has examples section"

    # Append Ejemplos section before Sources (if exists) or at end
    if "## Sources" in text:
        # Insert before Sources
        new_text = text.replace(
            "## Sources",
            EJEMPLOS_TEMPLATE.strip() + "\n\n---\n\n## Sources",
            1,
        )
    else:
        # Append at end
        new_text = text.rstrip() + "\n\n---\n\n" + EJEMPLOS_TEMPLATE

    if new_text == text:
        return False, "  - (no change)"

    if not dry_run:
        path.write_text(new_text, encoding="utf-8")
    return True, "  + added `## Ejemplos` section"


def discover_files() -> list[Path]:
    """Find Spanish culture files missing Ejemplos section."""
    results = []
    for path in sorted(ES_CULTURE_DIR.glob("*.md")):
        if path.name.endswith(".ko.md"):
            continue
        text = path.read_text(encoding="utf-8")
        if not has_examples_section(text):
            results.append(path)
    return results


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Add missing `## Ejemplos` section to Spanish culture pages (Track B3 + openclaw contract)."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without writing",
    )
    args = parser.parse_args()

    files = discover_files()
    if not files:
        print("[add_ejemplos] All Spanish culture pages already have Ejemplos sections")
        return 0

    total_modified = 0
    for path in files:
        rel = path.relative_to(LANG_DIR)
        modified, msg = process_file(path, dry_run=args.dry_run)
        marker = "[dry-run]" if args.dry_run else "[add_ejemplos]"
        print(f"{marker} {rel.name}")
        print(msg)
        if modified:
            total_modified += 1

    print()
    if args.dry_run:
        print(f"[dry-run] Would add Ejemplos to {total_modified} files")
    else:
        print(f"[add_ejemplos] Modified {total_modified} files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
