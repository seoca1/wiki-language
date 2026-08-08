#!/usr/bin/env python3
"""
Generate / validate `## Pipeline Form (machine-readable)` YAML sections
in Language wiki vocabulary theme files.

ADR-0003 (Pipeline YAML contract) — all vocabulary theme files MUST have
this section. This tool:

1. **--generate** (default): regenerate Pipeline Form sections from parsed
   `### {word}` headings in each theme file. Idempotent.
2. **--validate**: parse existing YAML sections and report violations
   (missing fields, malformed YAML, id collisions, etc.).
3. **--dry-run**: preview changes without writing.

Per ADR-0003 schema, each entry must have:
  id, display, input, meaning, level, category, source

The `source` field uses bare-stem wikilink (e.g., `[[food-vocabulary]]`).

Usage:
  python3 Language/tools/generate_yaml_pipeline.py [--lang en] [--dry-run]
  python3 Language/tools/generate_yaml_pipeline.py --validate [--lang en]
  python3 Language/tools/generate_yaml_pipeline.py --help

Exit codes:
  0 = clean / regenerated successfully
  1 = violations found (validate mode)
  2 = runtime error
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

# Resolve Language/ absolute path from this script's location.
SCRIPT_DIR = Path(__file__).resolve().parent
LANG_DIR = SCRIPT_DIR.parent
WIKI_DIR = LANG_DIR / "wiki"

# Language code mapping (wiki subdir → short prefix in entry id).
LANG_PREFIX = {
    "English": "en",
    "Spanish": "es",
    "Japanese": "jp",
    "Korean": "kr",
    "Chinese": "zh",
}

# Required YAML fields per ADR-0003.
REQUIRED_FIELDS = ("id", "display", "input", "meaning", "level", "category", "source")

# Pipeline Form section header (case-insensitive matching).
PIPELINE_HEADER_RE = re.compile(
    r"^##\s+Pipeline Form(?:\s+\(machine-readable\))?\s*$",
    re.MULTILINE | re.IGNORECASE,
)
H3_RE = re.compile(r"^###\s+(.+?)\s*$", re.MULTILINE)
FRONT_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
INLINE_KV_RE = re.compile(r"\*\*([^*]+):\*\*\s*(.+)")
DEF_RE = re.compile(r"\*\*Definition:\*\*\s*(.+?)(?:\n|$)")


@dataclass
class YamlEntry:
    """Single Pipeline Form YAML entry."""
    id: str
    display: str
    input: str
    meaning: str
    level: str
    category: str
    source: str
    line_no: int = 0

    def to_yaml_line(self) -> str:
        """Format entry as YAML line (single-line dict form per existing convention)."""
        return (
            f'- {{ id: {self.id}, display: "{self.display}", '
            f'input: "{self.input}", meaning: "{self.meaning}", '
            f'level: "{self.level}", category: "{self.category}", '
            f'source: "{self.source}" }}'
        )


@dataclass
class ThemeFile:
    """Parsed vocabulary theme file."""
    path: Path
    lang: str
    lang_prefix: str
    level: str = "A1"  # default
    category: str = ""
    source_stem: str = ""
    words: list[str] = field(default_factory=list)
    existing_yaml: list[YamlEntry] = field(default_factory=list)
    has_pipeline_section: bool = False


def parse_frontmatter(text: str) -> dict[str, str]:
    """Extract YAML frontmatter key-value pairs."""
    m = FRONT_RE.search(text)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm


def parse_inline_level(text_no_front: str) -> Optional[str]:
    """Look for `**Level:** ...` inline marker (used by some Chinese files)."""
    m = re.search(r"\*\*Level:\*\*\s*([^\n]+)", text_no_front)
    if m:
        return m.group(1).strip()
    return None


def parse_definition_for_meaning(word_section: str) -> str:
    """Extract meaning from a word section's `**Definition:**` line."""
    m = DEF_RE.search(word_section)
    if m:
        return m.group(1).strip()
    return ""


def split_word_sections(text_no_front: str) -> dict[str, str]:
    """Split text into {word_name: section_text} for each `### {word}` heading.

    Sections run from one `### {word}` to the next `### {word}` or end-of-file.
    """
    matches = list(H3_RE.finditer(text_no_front))
    sections = {}
    for i, m in enumerate(matches):
        word = m.group(1).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text_no_front)
        sections[word] = text_no_front[start:end]
    return sections


def parse_existing_yaml(text: str) -> list[YamlEntry]:
    """Parse existing `## Pipeline Form` section entries (single-line dict form).

    Matches lines like:
      - { id: en_food_001, display: "meat", ..., source: "[[food-vocabulary]]" }
    """
    section_m = PIPELINE_HEADER_RE.search(text)
    if not section_m:
        return []

    # Section ends at next ## heading or EOF
    section_start = section_m.end()
    rest = text[section_start:]
    next_h2 = re.search(r"^##\s+", rest, re.MULTILINE)
    section_text = rest[: next_h2.start()] if next_h2 else rest

    entries = []
    for line_no, line in enumerate(section_text.splitlines(), 1):
        line = line.strip()
        if not line.startswith("- {"):
            continue
        # Strip "- {" prefix and "}" suffix
        body = line[3:].rstrip("}").strip()
        # Parse key: value, ...
        fields = {}
        # Regex captures key: value (value can be quoted)
        for km in re.finditer(r'(\w+):\s*("[^"]*"|[^\s,][^,]*)', body):
            k = km.group(1).strip()
            v = km.group(2).strip().strip('"').strip("'")
            fields[k] = v
        if all(f in fields for f in REQUIRED_FIELDS):
            entries.append(YamlEntry(
                id=fields["id"],
                display=fields["display"],
                input=fields["input"],
                meaning=fields["meaning"],
                level=fields["level"],
                category=fields["category"],
                source=fields["source"],
                line_no=line_no,
            ))
    return entries


def make_entry_id(lang_prefix: str, category: str, n: int) -> str:
    """Build entry id: `{lang_prefix}_{category_snake}_{NNN}`."""
    # Convert category to snake_case-ish (replace - and spaces with _)
    cat_snake = category.replace("-", "_").replace(" ", "_")
    return f"{lang_prefix}_{cat_snake}_{n:03d}"


def derive_category(filename_stem: str, frontmatter: dict[str, str]) -> str:
    """Derive category from filename or frontmatter.

    Filename patterns:
      food-vocabulary.md        → food-vocabulary (EN/KO)
      food-vocabulary-es.md     → food-vocabulary (ES, but actual files use food-vocabulary.md)
      body-zh.md                → body-zh (ZH)
      food-vocabulary-jp.md     → food-vocabulary (JP, but actual files use food-vocabulary.md)

    Frontmatter `category:` field is the most reliable signal.
    """
    fm_cat = frontmatter.get("category", "").strip()
    if fm_cat:
        return fm_cat
    # Fallback: strip language suffix from filename
    stem = filename_stem
    for suffix in ("-es", "-jp", "-kr", "-ko", "-zh"):
        if stem.endswith(suffix):
            stem = stem[: -len(suffix)]
            break
    return stem


def derive_source_stem(filename_stem: str, frontmatter: dict[str, str]) -> str:
    """Derive `source:` stem (without `[[...]]`).

    Priority:
    1. frontmatter `source:` field (canonical)
    2. filename stem (with language suffix stripped)
    """
    fm_src = frontmatter.get("source", "").strip()
    if fm_src:
        return fm_src
    stem = filename_stem
    for suffix in ("-es", "-jp", "-kr", "-ko", "-zh"):
        if stem.endswith(suffix):
            stem = stem[: -len(suffix)]
            break
    return stem


def parse_theme_file(path: Path, lang: str, lang_prefix: str) -> ThemeFile:
    """Parse a vocabulary theme file into structured data."""
    text = path.read_text(encoding="utf-8")
    frontmatter = parse_frontmatter(text)
    inline_level = parse_inline_level(FRONT_RE.sub("", text, count=1))
    text_no_front = FRONT_RE.sub("", text, count=1)

    level = frontmatter.get("level") or inline_level or "A1"
    category = derive_category(path.stem, frontmatter)
    source_stem = derive_source_stem(path.stem, frontmatter)

    sections = split_word_sections(text_no_front)
    # Preserve order from `### {word}` matches (split_word_sections already does this)
    words = list(sections.keys())
    existing_yaml = parse_existing_yaml(text)
    has_pipeline = bool(PIPELINE_HEADER_RE.search(text))

    return ThemeFile(
        path=path,
        lang=lang,
        lang_prefix=lang_prefix,
        level=level,
        category=category,
        source_stem=source_stem,
        words=words,
        existing_yaml=existing_yaml,
        has_pipeline_section=has_pipeline,
    )


def build_yaml_section(theme: ThemeFile) -> str:
    """Build the `## Pipeline Form (machine-readable)` section content.

    Preserves existing YAML entries' `meaning`/`category`/`level` data
    where possible. Only the `id` field is regenerated with correct prefix.
    """
    # Index existing entries by display name for data preservation
    existing_by_display = {e.display: e for e in theme.existing_yaml}

    lines = []
    lines.append("## Pipeline Form (machine-readable)")
    lines.append("")
    lines.append(
        "> Generated for downstream consumers (`Game/typing_language/raw/{lang}_words.md`)."
    )
    lines.append(
        "> Schema reference: `wiki/pipeline-to-game.md` L33-39, L92."
    )
    lines.append(
        "> The body above remains the human-readable form and is the source of truth."
    )
    lines.append("")
    lines.append("```yaml")
    for n, word in enumerate(theme.words, 1):
        # Get existing entry data if available (preserve meaning/category/level)
        existing = existing_by_display.get(word)
        if existing:
            meaning = existing.meaning
            level = existing.level or theme.level
            category = existing.category or theme.category
        else:
            # New heading without existing YAML entry — parse from body
            sections = split_word_sections(FRONT_RE.sub("", theme.path.read_text(encoding="utf-8"), count=1))
            word_section = sections.get(word, "")
            meaning = parse_definition_for_meaning(word_section)
            level = theme.level
            category = theme.category

        display = word
        inp = display
        entry_id = make_entry_id(theme.lang_prefix, theme.category, n)
        entry = YamlEntry(
            id=entry_id,
            display=display,
            input=inp,
            meaning=meaning,
            level=level,
            category=category,
            source=f"[[{theme.source_stem}]]",
        )
        lines.append(entry.to_yaml_line())
    lines.append("```")
    lines.append("")
    return "\n".join(lines)


def regenerate_file(theme: ThemeFile, dry_run: bool = False) -> tuple[bool, str]:
    """Replace `## Pipeline Form` section in theme file.

    Returns (changed, summary_msg).
    """
    text = theme.path.read_text(encoding="utf-8")
    new_section = build_yaml_section(theme)

    if not PIPELINE_HEADER_RE.search(text):
        # No existing section → append to end
        new_text = text.rstrip() + "\n\n" + new_section
        if dry_run:
            return True, f"  + would APPEND Pipeline Form section ({len(theme.words)} entries)"
        theme.path.write_text(new_text, encoding="utf-8")
        return True, f"  + APPENDED Pipeline Form section ({len(theme.words)} entries)"

    # Replace existing section
    section_m = PIPELINE_HEADER_RE.search(text)
    section_start = section_m.start()
    rest = text[section_m.end():]
    next_h2 = re.search(r"^##\s+", rest, re.MULTILINE)
    if next_h2:
        section_end = section_m.end() + next_h2.start()
        # Keep any content after the Pipeline Form section (next ## heading onward)
        after = text[section_end:]
    else:
        section_end = len(text)
        after = ""

    new_text = text[:section_start] + new_section + after
    if new_text == text:
        return False, "  = unchanged"

    if dry_run:
        return True, f"  ~ would UPDATE Pipeline Form section ({len(theme.words)} entries)"
    theme.path.write_text(new_text, encoding="utf-8")
    return True, f"  ~ UPDATED Pipeline Form section ({len(theme.words)} entries)"


def validate_file(theme: ThemeFile) -> list[str]:
    """Return list of validation violations for theme file."""
    violations = []

    if not theme.has_pipeline_section:
        violations.append("missing `## Pipeline Form` section")
        return violations  # can't validate entries without section

    if not theme.existing_yaml:
        violations.append("Pipeline Form section exists but no parseable entries")
        return violations

    # Per-entry checks (ADR-0003 schema)
    for entry in theme.existing_yaml:
        # Source must use bare stem (no path-style prefix)
        src_inner = entry.source.strip("[]")
        if "/" in src_inner or "\\" in src_inner:
            violations.append(
                f"line {entry.line_no}: source uses path-style: {entry.source}"
            )
        # ID prefix must match language (e.g., en_, es_, jp_, kr_, zh_)
        expected_prefix = theme.lang_prefix
        if not entry.id.startswith(f"{expected_prefix}_"):
            violations.append(
                f"line {entry.line_no}: id `{entry.id}` doesn't start with `{expected_prefix}_` (ADR-0003)"
            )
        # Level should not be empty
        if not entry.level:
            violations.append(f"line {entry.line_no}: empty level")
        # Category should not be empty (lenient — subcategories within theme are OK)
        if not entry.category:
            violations.append(f"line {entry.line_no}: empty category")
        # Display should not be empty
        if not entry.display:
            violations.append(f"line {entry.line_no}: empty display")

    # Check id uniqueness within file
    ids = [e.id for e in theme.existing_yaml]
    dup = [i for i, c in Counter(ids).items() if c > 1]
    for d in dup:
        violations.append(f"duplicate id `{d}`")

    # Check entry count matches `### {word}` heading count
    n_headings = len(theme.words)
    n_entries = len(theme.existing_yaml)
    if n_headings != n_entries:
        violations.append(
            f"entry count mismatch: {n_headings} `### {{word}}` headings vs {n_entries} YAML entries"
        )

    return violations


# Local Counter import (avoid top-level if not needed)
from collections import Counter


def cmd_generate(args: argparse.Namespace) -> int:
    """Generate / regenerate Pipeline Form sections."""
    files = discover_theme_files(args.lang)
    if not files:
        print(f"[generate] No theme files found (filter: lang={args.lang or 'all'})", file=sys.stderr)
        return 2

    total_changed = 0
    total_unchanged = 0
    total_entries = 0
    for path, lang in files:
        lang_prefix = LANG_PREFIX[lang]
        theme = parse_theme_file(path, lang, lang_prefix)
        changed, msg = regenerate_file(theme, dry_run=args.dry_run)
        if changed:
            total_changed += 1
        else:
            total_unchanged += 1
        total_entries += len(theme.words)
        rel = path.relative_to(LANG_DIR)
        marker = "[dry-run]" if args.dry_run else "[generate]"
        print(f"{marker} {lang}/{rel.name}{msg}")

    print()
    print(f"Summary: {total_changed} changed, {total_unchanged} unchanged, {total_entries} total entries")
    if args.dry_run:
        print("(dry-run mode: no files written)")
    return 0


def cmd_validate(args: argparse.Namespace) -> int:
    """Validate existing Pipeline Form sections."""
    files = discover_theme_files(args.lang)
    if not files:
        print(f"[validate] No theme files found (filter: lang={args.lang or 'all'})", file=sys.stderr)
        return 2

    total_violations = 0
    files_with_violations = 0
    for path, lang in files:
        lang_prefix = LANG_PREFIX[lang]
        theme = parse_theme_file(path, lang, lang_prefix)
        violations = validate_file(theme)
        if violations:
            files_with_violations += 1
            total_violations += len(violations)
            rel = path.relative_to(LANG_DIR)
            print(f"[validate] {lang}/{rel.name}")
            for v in violations:
                print(f"  - {v}")
        # else: silently OK

    print()
    if total_violations == 0:
        print(f"[validate] CLEAN — {len(files)} files, 0 violations")
        return 0
    print(f"[validate] {total_violations} violations in {files_with_violations} / {len(files)} files")
    return 1


def discover_theme_files(lang_filter: Optional[str]) -> list[tuple[Path, str]]:
    """Discover all vocabulary theme files under Language/wiki/{Lang}/vocabulary/.

    Returns list of (path, lang_name).
    """
    results = []
    # Map short code → full lang name (also accept full name)
    short_to_full = {v: k for k, v in LANG_PREFIX.items()}
    lang_full = short_to_full.get(lang_filter, lang_filter)

    for lang in LANG_PREFIX:
        if lang_filter and lang != lang_full:
            continue
        vocab_dir = WIKI_DIR / lang / "vocabulary"
        if not vocab_dir.exists():
            continue
        for path in sorted(vocab_dir.glob("*.md")):
            # Skip per-word `.ko.md` translation pair files
            if path.name.endswith(".ko.md"):
                continue
            results.append((path, lang))
    return results


def build_arg_parser() -> argparse.ArgumentParser:
    """Build CLI argument parser."""
    p = argparse.ArgumentParser(
        description="Generate / validate Pipeline Form YAML sections in Language wiki vocabulary theme files. ADR-0003."
    )
    p.add_argument(
        "--lang",
        choices=["en", "es", "jp", "kr", "zh"],
        help="Process only this language (default: all 5)",
    )
    mode = p.add_mutually_exclusive_group()
    mode.add_argument(
        "--generate",
        action="store_true",
        default=True,  # default mode
        help="Generate / regenerate Pipeline Form sections (default)",
    )
    mode.add_argument(
        "--validate",
        action="store_true",
        help="Validate existing Pipeline Form sections (report violations, no writes)",
    )
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without writing (use with --generate)",
    )
    return p


def main() -> int:
    parser = build_arg_parser()
    args = parser.parse_args()

    if args.validate:
        return cmd_validate(args)
    return cmd_generate(args)


if __name__ == "__main__":
    sys.exit(main())
