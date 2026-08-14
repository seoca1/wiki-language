#!/usr/bin/env python3
"""
Generate / validate `## Pipeline Form (machine-readable)` YAML sections
in Language wiki theme files (vocabulary + expressions).

ADR-0003 (vocabulary YAML contract) + ADR-0005 (expressions YAML contract).
This tool:

1. **--generate** (default): regenerate Pipeline Form sections from parsed
   headings in each theme file. Idempotent.
2. **--validate**: parse existing YAML sections and report violations
   (missing fields, malformed YAML, id collisions, etc.).
3. **--dry-run**: preview changes without writing.

Per ADR-0003 / ADR-0005 schema, each entry must have:
  id, display, input, meaning, level, category, source

The `source` field uses bare-stem wikilink (e.g., `[[food-vocabulary]]`).

Heading conventions:
  Vocabulary  (ADR-0001): `### {word}` (H3)
  Expressions (ADR-0005): `## {expression}` (H2, schema/AGENTS.md template)
                          OR `### {expression}` (H3, legacy convention in some files)

The expressions mode auto-detects per-file which heading depth carries the
expressions, excluding known non-expression sections (Pipeline Form, Sources,
Related Themes, Quick Reference, etc.).

Usage:
  python3 Language/tools/generate_yaml_pipeline.py [--lang en] [--dry-run]
  python3 Language/tools/generate_yaml_pipeline.py --validate [--lang en]
  python3 Language/tools/generate_yaml_pipeline.py --content-type expressions --lang kr
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
H2_RE = re.compile(r"^##\s+(?!Pipeline Form|Quick Reference|Related|Themes|Pages|Sources|Cultural\s+Background|Similar\s+Expressions|Pattern|Examples?|Mini|Memory\s+Tip|Common\s+Mistakes)(.+?)\s*$", re.MULTILINE)
FRONT_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
INLINE_KV_RE = re.compile(r"\*\*([^*]+):\*\*\s*(.+)")
DEF_RE = re.compile(r"\*\*Definition:\*\*\s*(.+?)(?:\n|$)")

MEANING_FIELD_RE = re.compile(
    r"\*\*(?:Meaning|의미|Definition|Definición|意味)[:：]?\*\*\s*[:：]?\s*(.+?)(?:\n|$)",
    re.MULTILINE,
)
CHINESE_MEANING_RE = re.compile(r"\*\*英文[:：]\*\*\s*(.+?)(?:\n|$)")
CHINESE_PINYIN_RE = re.compile(r"\*\*拼音[:：]\*\*\s*([^\n]+)")
CHINESE_HSK_RE = re.compile(r"\*\*HSK[:：]\*\*\s*(\d+)")
LITERAL_FIELD_RE = re.compile(
    r"\*\*(?:Literal\s+Translation|직역|Traducción\s+literal|直訳|直譯)[:：]?\*\*\s*[:：]?\s*(.+?)(?:\n|$)",
    re.MULTILINE,
)
REGISTER_FIELD_RE = re.compile(
    r"\*\*(?:Register|사용\s+맥락|Contexto\s+de\s+uso|レジスター|격식)[:：]?\*\*\s*[:：]?\s*(.+?)(?:\n|$)",
    re.IGNORECASE,
)


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
    literal: str = ""
    register: str = ""

    def to_yaml_line(self) -> str:
        """Format entry as YAML line (single-line dict form per existing convention)."""
        def q(v: str) -> str:
            return "'" + v.replace("'", "''") + "'"
        extra = ""
        if self.literal:
            extra += f", literal: {q(self.literal)}"
        if self.register:
            extra += f", register: {q(self.register)}"
        return (
            f"- {{ id: {q(self.id)}, display: {q(self.display)}, "
            f"input: {q(self.input)}, meaning: {q(self.meaning)}, "
            f"level: {q(self.level)}, category: {q(self.category)}, "
            f"source: {q(self.source)}{extra} }}"
        )


@dataclass
class ThemeFile:
    """Parsed theme file (vocabulary or expressions)."""
    path: Path
    lang: str
    lang_prefix: str
    content_type: str = "vocabulary"  # "vocabulary" or "expressions"
    level: str = "A1"  # default
    category: str = ""
    source_stem: str = ""
    words: list[str] = field(default_factory=list)  # vocab words OR expressions
    expressions: list[str] = field(default_factory=list)  # alias when content_type=expressions
    existing_yaml: list[YamlEntry] = field(default_factory=list)
    has_pipeline_section: bool = False
    heading_depth: str = "h3"  # "h2" or "h3" (expressions mode only)


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
    m = CHINESE_MEANING_RE.search(word_section)
    if m:
        return m.group(1).strip()
    return ""


def parse_chinese_pinyin(word_section: str) -> str:
    """Extract pinyin from a Chinese word section's `**拼音:**` line."""
    m = CHINESE_PINYIN_RE.search(word_section)
    if m:
        return m.group(1).strip()
    return ""


def parse_chinese_hsk(word_section: str) -> str:
    """Extract HSK level from a Chinese word section's `**HSK:**` line."""
    m = CHINESE_HSK_RE.search(word_section)
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


def parse_theme_file(path: Path, lang: str, lang_prefix: str, content_type: str = "vocabulary") -> ThemeFile:
    """Parse a theme file (vocabulary or expressions) into structured data."""
    text = path.read_text(encoding="utf-8")

    if any(marker in text[:300] for marker in ("→ See [[", "superseded by", "redirect stub", "redirect to")):
        return ThemeFile(
            path=path,
            lang=lang,
            lang_prefix=lang_prefix,
            content_type=content_type,
            level="A1",
            category=derive_category(path.stem, {}),
            source_stem=path.stem,
            words=[],
            existing_yaml=[],
            has_pipeline_section=False,
        )

    frontmatter = parse_frontmatter(text)
    inline_level = parse_inline_level(FRONT_RE.sub("", text, count=1))
    text_no_front = FRONT_RE.sub("", text, count=1)

    level = frontmatter.get("level") or inline_level or "A1"
    category = derive_category(path.stem, frontmatter)
    source_stem = derive_source_stem(path.stem, frontmatter)

    if content_type == "expressions":
        headings, depth = detect_expression_headings(text_no_front)
        words = headings
        heading_depth = depth
    else:
        sections = split_word_sections(text_no_front)
        words = list(sections.keys())
        heading_depth = "h3"

    existing_yaml = parse_existing_yaml(text)
    has_pipeline = bool(PIPELINE_HEADER_RE.search(text))

    return ThemeFile(
        path=path,
        lang=lang,
        lang_prefix=lang_prefix,
        content_type=content_type,
        level=level,
        category=category,
        source_stem=source_stem,
        words=words,
        expressions=words if content_type == "expressions" else [],
        existing_yaml=existing_yaml,
        has_pipeline_section=has_pipeline,
        heading_depth=heading_depth,
    )


def detect_expression_headings(text_no_front: str) -> tuple[list[str], str]:
    """Detect expression headings in expression theme file (ADR-0005).

    Returns (list_of_expression_titles, heading_depth) where heading_depth is
    "h2" or "h3" depending on which convention the file uses.

    Heuristic: prefer H2 when it carries expressions (per schema/AGENTS.md L155-200).
    Fall back to H3 only when the file uses the legacy vocabulary-style convention
    (e.g., English/Spanish/Chinese common-phrases.md, Korean agreement/apologies).
    """
    h2_candidates = [m.group(1).strip() for m in H2_RE.finditer(text_no_front)]
    h3_matches = list(H3_RE.finditer(text_no_front))
    h3_candidates = [m.group(1).strip() for m in h3_matches]

    h2_filtered = filter_expression_headings(h2_candidates, depth="h2")
    h3_filtered = filter_expression_headings(h3_candidates, depth="h3")

    if len(h2_filtered) >= 2:
        return h2_filtered, "h2"
    return h3_filtered, "h3"


def filter_expression_headings(headings: list[str], depth: str) -> list[str]:
    """Remove non-expression headings (subsections, references, etc.)."""
    out = []
    for h in headings:
        if not h:
            continue
        h_lower = h.lower()
        if depth == "h2":
            if h.startswith("Pipeline Form"):
                continue
            if h.startswith("Quick Reference") or h.startswith("Quick"):
                continue
            if h_lower.startswith("related themes") or h_lower.startswith("related pages"):
                continue
            if h_lower.startswith("sources"):
                continue
            if h_lower.startswith("cultural background") or h_lower.startswith("cultural notes"):
                continue
            if h_lower.startswith("similar expressions"):
                continue
            if h_lower.startswith("pattern"):
                continue
            if h_lower.startswith("mini-dialogue"):
                continue
            if h_lower.startswith("memory tip"):
                continue
            if h_lower.startswith("common mistakes"):
                continue
            if h.startswith("#") or h.startswith(">"):
                continue
        else:
            if h_lower.startswith("usage") and depth == "h3":
                continue
            if h_lower.startswith("variations") and depth == "h3":
                continue
            if h_lower.startswith("responses") and depth == "h3":
                continue
            if h_lower.startswith("cultural notes") and depth == "h3":
                continue
            if h_lower.startswith("sources") and depth == "h3":
                continue
            if h_lower.startswith("examples") and depth == "h3":
                continue
            if h_lower.startswith("mini-dialogue") and depth == "h3":
                continue
        out.append(h)
    return out


def split_expression_sections(text_no_front: str, depth: str) -> dict[str, str]:
    """Split text into {expression_name: section_text} for the given heading depth."""
    pattern = H2_RE if depth == "h2" else H3_RE
    matches = list(pattern.finditer(text_no_front))
    sections = {}
    for i, m in enumerate(matches):
        name = m.group(1).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text_no_front)
        sections[name] = text_no_front[start:end]
    return sections


def parse_expression_meaning(expr_section: str) -> str:
    """Extract meaning from an expression section.

    Tries (in order): Meaning / 의미 / Definition / Definición / 意味.
    Falls back to first non-empty line if none found.
    """
    m = MEANING_FIELD_RE.search(expr_section)
    if m:
        text = m.group(1).strip()
        text = re.sub(r"\([^)]*\)", "", text).strip()
        text = re.sub(r"\s+", " ", text)
        return text[:200]
    return ""


def parse_expression_literal(expr_section: str) -> str:
    """Extract optional literal translation from expression section."""
    m = LITERAL_FIELD_RE.search(expr_section)
    if m:
        return m.group(1).strip()[:200]
    return ""


def parse_expression_register(expr_section: str) -> str:
    """Extract optional register / speech-level marker from expression section."""
    m = REGISTER_FIELD_RE.search(expr_section)
    if m:
        return m.group(1).strip()[:80]
    return ""


ROMANIZATION_HEADING_RE = re.compile(r"\(([^()]+(?:\([^()]*\)[^()]*)*)\)")
LATIN_CHAR_RE = re.compile(r"[A-Za-z]")


def parse_expression_input_from_heading(heading_text: str) -> str:
    """Extract romaja/pinyin from a heading like '~해 주세요 (~hae juseyo, please do ~)'.

    Strategy: among all parenthesized groups in the heading, pick the one with the
    highest Latin character ratio (typically the romaja/pinyin). Falls back to the
    original heading text when no parenthesized group is found.
    """
    candidates = ROMANIZATION_HEADING_RE.findall(heading_text)
    if not candidates:
        return heading_text
    best = max(candidates, key=lambda c: (len(LATIN_CHAR_RE.findall(c)), len(c)))
    first_segment = best.split(",", 1)[0].strip()
    return first_segment or heading_text


def build_yaml_section(theme: ThemeFile) -> str:
    """Build the `## Pipeline Form (machine-readable)` section content.

    Preserves existing YAML entries' `meaning`/`category`/`level` data
    where possible. Only the `id` field is regenerated with correct prefix.

    Supports both vocabulary (ADR-0003) and expressions (ADR-0005) — expressions
    additionally extract optional `literal` and `register` fields.
    """
    existing_by_display = {e.display: e for e in theme.existing_yaml}

    text_no_front = FRONT_RE.sub("", theme.path.read_text(encoding="utf-8"), count=1)
    if theme.content_type == "expressions":
        sections = split_expression_sections(text_no_front, theme.heading_depth)
    else:
        sections = split_word_sections(text_no_front)

    lines = []
    lines.append("## Pipeline Form (machine-readable)")
    lines.append("")
    if theme.content_type == "expressions":
        lines.append(
            "> Generated for downstream consumers (`Game/typing_language/raw/{lang}_expressions.md`)."
        )
        lines.append(
            "> Schema: ADR-0005 — `## {expression}` (H2/H3) → 7 required fields + optional literal/register."
        )
    else:
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
        existing = existing_by_display.get(word)
        word_section = sections.get(word, "")

        if existing:
            meaning = existing.meaning
            level = existing.level or theme.level
            category = existing.category or theme.category
            literal = existing.literal
            register = existing.register
        else:
            if theme.content_type == "expressions":
                meaning = parse_expression_meaning(word_section)
                literal = parse_expression_literal(word_section)
                register = parse_expression_register(word_section)
            else:
                meaning = parse_definition_for_meaning(word_section)
                literal = ""
                register = ""
            level = theme.level
            category = theme.category

        display = word
        if theme.content_type == "expressions":
            inp = parse_expression_input_from_heading(word)
        elif theme.lang == "Chinese":
            pinyin = parse_chinese_pinyin(word_section)
            hsk = parse_chinese_hsk(word_section)
            if pinyin:
                display = f"{word} ({pinyin})"
                inp = pinyin
            else:
                inp = word
            if hsk:
                level = hsk
        else:
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
            literal=literal,
            register=register,
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
    files = discover_theme_files(args.lang, args.content_type)
    if not files:
        print(f"[generate] No theme files found (filter: lang={args.lang or 'all'}, content_type={args.content_type})", file=sys.stderr)
        return 2

    total_changed = 0
    total_unchanged = 0
    total_entries = 0
    for path, lang, content_type in files:
        lang_prefix = LANG_PREFIX[lang]
        theme = parse_theme_file(path, lang, lang_prefix, content_type=content_type)
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
    files = discover_theme_files(args.lang, args.content_type)
    if not files:
        print(f"[validate] No theme files found (filter: lang={args.lang or 'all'}, content_type={args.content_type})", file=sys.stderr)
        return 2

    total_violations = 0
    files_with_violations = 0
    for path, lang, content_type in files:
        lang_prefix = LANG_PREFIX[lang]
        theme = parse_theme_file(path, lang, lang_prefix, content_type=content_type)
        if not theme.words and not theme.has_pipeline_section:
            text = path.read_text(encoding="utf-8")
            if any(m in text[:300] for m in ("→ See [[", "superseded by", "redirect stub", "redirect to")):
                continue
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


def discover_theme_files(lang_filter: Optional[str], content_type: str = "vocabulary") -> list[tuple[Path, str, str]]:
    """Discover theme files under Language/wiki/{Lang}/{content_type}s/.

    Returns list of (path, lang_name, content_type).
    """
    results = []
    short_to_full = {v: k for k, v in LANG_PREFIX.items()}
    lang_full = short_to_full.get(lang_filter, lang_filter)

    types_to_scan = ["vocabulary", "expressions"] if content_type == "all" else [content_type]

    for ctype in types_to_scan:
        for lang in LANG_PREFIX:
            if lang_filter and lang != lang_full:
                continue
            dir_path = WIKI_DIR / lang / ctype
            if not dir_path.exists():
                continue
            for path in sorted(dir_path.glob("*.md")):
                if path.name.endswith(".ko.md"):
                    continue
                results.append((path, lang, ctype))
    return results


def build_arg_parser() -> argparse.ArgumentParser:
    """Build CLI argument parser."""
    p = argparse.ArgumentParser(
        description="Generate / validate Pipeline Form YAML sections in Language wiki theme files. ADR-0003 (vocabulary) + ADR-0005 (expressions)."
    )
    p.add_argument(
        "--lang",
        choices=["en", "es", "jp", "kr", "zh"],
        help="Process only this language (default: all 5)",
    )
    p.add_argument(
        "--content-type",
        choices=["vocabulary", "expressions", "all"],
        default="vocabulary",
        help="Which content type to process (default: vocabulary)",
    )
    mode = p.add_mutually_exclusive_group()
    mode.add_argument(
        "--generate",
        action="store_true",
        default=True,
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
