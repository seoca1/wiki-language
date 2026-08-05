#!/usr/bin/env python3
"""Add YAML frontmatter to Language vocabulary files."""

import re
from pathlib import Path

LANG_DIR = Path("/Users/emilio/projects/Projects/Language/wiki")

# Map of language to directory
LANGUAGES = ["Korean", "English", "Spanish", "Japanese", "Chinese"]

# Pattern to extract blockquote metadata
METADATA_PATTERN = re.compile(
    r"> \*\*Source:\*\*\s*\[?\[?([^\]]+)\]?\]?\s*\n"
    r"> \*\*Theme:\*\*\s*([^\n]+)\s*\n"
    r"> \*\*Level:\*\*\s*([^\n]+)",
    re.MULTILINE
)

# Pattern to extract Category from Theme line
CATEGORY_PATTERN = re.compile(r"> \*\*Category:\*\*\s*([^\n]+)")

# Pattern to extract Korean style metadata (with 한자 descriptions)
KR_METADATA_PATTERN = re.compile(
    r"> \*\*Source:\*\*\s*\[?\[?([^\]]+)\]?\]?\s*\n"
    r"> \*\*Category:\*\*\s*([^\n]+)\s*\n"
    r"> \*\*Level:\*\*\s*([^\n]+)",
    re.MULTILINE
)


def add_frontmatter(file_path: Path) -> None:
    """Add YAML frontmatter to a vocabulary file."""
    content = file_path.read_text(encoding="utf-8")

    # Skip if already has YAML frontmatter
    if content.startswith("---"):
        return

    # Try to extract metadata from blockquote format
    source = None
    theme = None
    level = None
    category = None

    # Try the English/Spanish format (Source, Theme, Level)
    m = re.search(
        r"> \*\*Source:\*\*\s*\[?\[?([^\]]+?)\]?\]?\s*\n"
        r"> \*\*Theme:\*\*\s*([^\n]+?)\s*\n"
        r"> \*\*Level:\*\*\s*([^\n]+?)(?:\n|$)",
        content
    )
    if m:
        source = m.group(1).strip()
        theme = m.group(2).strip()
        level = m.group(3).strip()

    # Try the Korean format (Source, Category, Level)
    if not source:
        m = re.search(
            r"> \*\*Source:\*\*\s*\[?\[?([^\]]+?)\]?\]?\s*\n"
            r"> \*\*Category:\*\*\s*([^\n]+?)\s*\n"
            r"> \*\*Level:\*\*\s*([^\n]+?)(?:\n|$)",
            content
        )
        if m:
            source = m.group(1).strip()
            category = m.group(2).strip()
            level = m.group(3).strip()
            # Derive theme from category
            theme = category

    # Try to extract just Category if nothing else found
    if not category:
        m = re.search(r"> \*\*Category:\*\*\s*([^\n]+)", content)
        if m:
            category = m.group(1).strip()
            theme = category

    # Derive category from title or filename if not found
    if not category:
        # Try to extract from filename (e.g., "business-vocabulary.md" -> "business")
        filename = file_path.stem
        for suffix in ["-vocabulary", "-grammar"]:
            if filename.endswith(suffix):
                category = filename[:-len(suffix)]
                break
        if not category:
            category = file_path.stem

    # Build YAML frontmatter
    frontmatter_lines = ["---"]
    if source:
        frontmatter_lines.append(f'source: "{source}"')
    if category:
        frontmatter_lines.append(f'category: "{category}"')
    if level:
        frontmatter_lines.append(f'level: "{level}"')
    if theme:
        frontmatter_lines.append(f'theme: "{theme}"')
    frontmatter_lines.append("---")
    frontmatter_lines.append("")

    frontmatter = "\n".join(frontmatter_lines) + "\n"

    # Remove existing blockquote metadata if present
    lines = content.split("\n")
    new_lines = []
    skip_block = False
    for i, line in enumerate(lines):
        if line.startswith("> **") and not skip_block:
            skip_block = True
            continue
        if skip_block:
            if line.startswith(">"):
                continue
            elif line.strip() == "":
                skip_block = False
                # Check if next non-blank line starts with new content (not > or --)
                for j in range(i+1, min(i+5, len(lines))):
                    if lines[j].strip() and not lines[j].startswith(">") and not lines[j].startswith("#"):
                        skip_block = False
                        new_lines.append(line)
                        break
                continue
            else:
                skip_block = False
                new_lines.append(line)
        else:
            new_lines.append(line)

    new_content = frontmatter + "\n".join(new_lines)

    file_path.write_text(new_content, encoding="utf-8")
    print(f"Added frontmatter to {file_path.name}")


def main() -> None:
    count = 0
    for lang in LANGUAGES:
        vocab_dir = LANG_DIR / lang / "vocabulary"
        if vocab_dir.exists():
            for md_file in vocab_dir.glob("*.md"):
                add_frontmatter(md_file)
                count += 1
    print(f"\nProcessed {count} vocabulary files")


if __name__ == "__main__":
    main()
