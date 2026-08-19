#!/usr/bin/env python3
"""
Audit downstream consumers of Language wiki content.

Per ADR-0003 (Pipeline YAML contract) and schema/AGENTS.md §Downstream
Consumers, Language wiki is the single source of truth for downstream:

1. **Game/lingotype/raw/{lang}_words.md** — game corpus (E1)
   - Each YAML entry MUST have `source:` field with bare-stem wikilink
   - The `source:` MUST resolve to a file in Language/wiki/{Lang}/vocabulary/

2. **.openclaw/workspace/wiki/{lang}/_exposure_log.md** — daily exposure log (E2)
   - `vault:[[Language/...]]` references MUST resolve
   - Openclaw is at /Users/emilio/.openclaw/ (system volume)

Usage:
  python3 Language/tools/audit_downstream.py --target game
  python3 Language/tools/audit_downstream.py --target openclaw
  python3 Language/tools/audit_downstream.py --target all
  python3 Language/tools/audit_downstream.py --target game --lang en
  python3 Language/tools/audit_downstream.py --help

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
from typing import Optional

SCRIPT_DIR = Path(__file__).resolve().parent
LANG_DIR = SCRIPT_DIR.parent
PROJECT_ROOT = LANG_DIR.parent
WIKI_DIR = LANG_DIR / "wiki"

# Game corpus location (typing_language)
GAME_RAW_DIR = PROJECT_ROOT / "Game" / "lingotype" / "raw"

# Openclaw workspace location (system volume, outside project)
OPENCLAW_ROOT = Path("/Users/emilio/.openclaw/workspace/wiki")

# Language code mapping
LANG_PREFIX = {
    "English": "en",
    "Spanish": "es",
    "Japanese": "jp",
    "Korean": "kr",
    "Chinese": "zh",
}
# Reverse mapping (for game/openclaw file naming)
SHORT_TO_FULL = {
    "en": "English",
    "es": "Spanish",
    "jp": "Japanese",
    "kr": "Korean",
    "zh": "Chinese",
}

# Regex for YAML single-line dict entries (game corpus format)
GAME_YAML_RE = re.compile(
    r"^\s*-\s*\{\s*id:\s*(\w+),(.*)\}\s*$",
    re.MULTILINE,
)

# Known field names in game corpus YAML entries
KNOWN_FIELDS = ("id", "display", "meaning", "input", "level", "category", "source", "accentMode", "note", "license", "romaji", "license", "tags", "image", "audio")

# Pattern to find ANY `\w+:` field boundary (catches unknown fields too)
ANY_FIELD_RE = re.compile(r'(?:^|[\s,])(\w+):\s?')

# Regex for extracting one field at a time (used iteratively)
# Wikilink variant `[[...]]` is matched first to avoid truncating at inner `]`.
SINGLE_FIELD_RE = re.compile(r'\s*(\w+):\s*(\[\[[^\]]*\]\]|"[^"]*"|[^\s,][^,]*)')

# Pattern to find a known field name at the current position
FIELD_BOUNDARY_RE = re.compile(r'(?:^|[,\s])(\w+):\s')

# Regex for openclaw vault:[[...]] references
VAULT_REF_RE = re.compile(r"vault:\[\[([^\]]+)\]\]")

# Regex for openclaw markdown wikilinks [[...]]
WIKILINK_RE = re.compile(r"(?<!`)\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")

# Regex for openclaw vault:[[...]] references
VAULT_REF_RE = re.compile(r"vault:\[\[([^\]]+)\]\]")

# Regex for openclaw markdown wikilinks [[...]]
WIKILINK_RE = re.compile(r"(?<!`)\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")


@dataclass
class GameEntry:
    """Parsed Game corpus YAML entry."""
    raw_line: str
    line_no: int
    lang: str
    id: str = ""
    display: str = ""
    meaning: str = ""
    level: str = ""
    category: str = ""
    source: str = ""
    extra_fields: dict[str, str] = field(default_factory=dict)


@dataclass
class Violation:
    """Single audit violation."""
    target: str  # 'game' | 'openclaw'
    file: str
    line_no: int
    entry_id: str
    msg: str


def parse_game_entry(raw_line: str, line_no: int, lang: str) -> GameEntry:
    """Parse a single-line YAML dict entry from game corpus.

    Strategy: split fields_str by KNOWN_FIELDS boundaries. For each known
    field, capture everything from that field name to the next field name
    as the value. This handles unquoted commas in `display:` (sentences).
    """
    m = GAME_YAML_RE.match(raw_line)
    if not m:
        return GameEntry(raw_line=raw_line, line_no=line_no, lang=lang)

    entry_id = m.group(1).strip()
    fields_str = m.group(2)

    entry = GameEntry(
        raw_line=raw_line,
        line_no=line_no,
        lang=lang,
        id=entry_id,
    )

    # Build list of (field_name, start_pos) tuples by finding ANY field pattern
    field_positions = []
    for fm in ANY_FIELD_RE.finditer(fields_str):
        field_positions.append((fm.start(), fm.group(1)))
    field_positions.sort()

    if not field_positions:
        return entry

    # Now extract values using the field positions
    for i, (start, fname) in enumerate(field_positions):
        # Value starts after "fname: "
        colon_space_end = fields_str.find(":", start) + 2  # past ": "
        # Value ends at next field start (or end of string)
        if i + 1 < len(field_positions):
            value_end = field_positions[i + 1][0]
            # Strip trailing comma
            if fields_str[value_end - 1] == ",":
                value_end -= 1
        else:
            value_end = len(fields_str)

        # Extract raw value, strip leading/trailing whitespace
        raw_value = fields_str[colon_space_end:value_end].strip()
        # Strip surrounding quotes if present
        if (raw_value.startswith('"') and raw_value.endswith('"')) or \
           (raw_value.startswith("'") and raw_value.endswith("'")):
            raw_value = raw_value[1:-1]
        value = raw_value.strip()

        if fname == "id":
            entry.id = value
        elif fname == "display":
            entry.display = value
        elif fname == "meaning":
            entry.meaning = value
        elif fname == "level":
            entry.level = value
        elif fname == "category":
            entry.category = value
        elif fname == "source":
            entry.source = value
        else:
            entry.extra_fields[fname] = value

    return entry


def is_sentence_entry(entry_id: str) -> bool:
    """Detect sentence entries (id like ens_001, jps_001, ess_001, krs_001).

    Sentence entries don't require `meaning:` field — display text IS the sentence.
    """
    if "_" not in entry_id:
        return False
    parts = entry_id.rsplit("_", 1)
    if len(parts) != 2:
        return False
    prefix, num = parts
    # Sentence pattern: <2-letter lang><s>_<NNN>
    if len(prefix) == 3 and prefix.endswith("s") and prefix[:2].isalpha():
        return num.isdigit()
    return False


def build_language_stem_index() -> dict[str, list[Path]]:
    """Build {stem: [paths]} index of Language wiki vocabulary theme files.

    Returns a dict mapping bare stem → list of matching files.
    Multiple files may share a stem (e.g., 'food-vocabulary' in EN/JP/KO).
    """
    stem_index: dict[str, list[Path]] = defaultdict(list)
    for lang in LANG_PREFIX:
        vocab_dir = WIKI_DIR / lang / "vocabulary"
        if not vocab_dir.exists():
            continue
        for path in vocab_dir.glob("*.md"):
            if path.name.endswith(".ko.md"):
                continue
            stem_index[path.stem].append(path)
    return stem_index


def source_resolves(source_wikilink: str, lang: str, stem_index: dict[str, list[Path]]) -> tuple[bool, str]:
    """Check if `source_wikilink` (e.g., `[[basic-vocabulary]]`) resolves.

    Returns (resolved, detail).
    """
    # Strip [[...]] brackets
    inner = source_wikilink.strip("[]").strip()
    # Strip section anchor
    if "#" in inner:
        inner = inner.split("#", 1)[0]
    # Strip path-style prefix
    if "/" in inner:
        inner = inner.split("/")[-1]
    if not inner:
        return False, "empty source reference"

    # Check stem in index
    if inner in stem_index:
        matches = stem_index[inner]
        # Filter to matching language
        lang_matches = [p for p in matches if f"/{lang}/" in str(p)]
        if lang_matches:
            return True, f"resolved to {lang_matches[0].relative_to(PROJECT_ROOT)}"
        # Any language match
        return True, f"resolved to {matches[0].relative_to(PROJECT_ROOT)} (cross-language stem)"

    return False, f"no Language wiki file with stem `{inner}`"


def audit_game_corpus(lang_filter: Optional[str], stem_index: dict[str, list[Path]]) -> list[Violation]:
    """Audit Game/lingotype/raw/{lang}_words.md for ADR-0003 compliance."""
    violations = []

    if not GAME_RAW_DIR.exists():
        violations.append(Violation(
            target="game",
            file=str(GAME_RAW_DIR),
            line_no=0,
            entry_id="",
            msg=f"Game raw directory not found: {GAME_RAW_DIR}",
        ))
        return violations

    # Find all _words.md files
    for path in sorted(GAME_RAW_DIR.glob("*_words.md")):
        # Extract lang from filename (en_words.md → en)
        lang_short = path.stem.replace("_words", "")
        lang_full = SHORT_TO_FULL.get(lang_short, lang_short.capitalize())
        if lang_filter and lang_short != lang_filter:
            continue

        text = path.read_text(encoding="utf-8")
        n_entries = 0
        for line_no, line in enumerate(text.splitlines(), 1):
            line = line.strip()
            if not line.startswith("- {"):
                continue
            entry = parse_game_entry(line, line_no, lang_full)
            n_entries += 1
            entry_id = entry.id or f"(line {line_no})"

            # Detect sentence entries — they don't need `meaning:` field
            is_sentence = is_sentence_entry(entry_id)

            # Check required fields
            if not entry.id:
                violations.append(Violation(
                    target="game",
                    file=str(path.relative_to(PROJECT_ROOT)),
                    line_no=line_no,
                    entry_id=entry_id,
                    msg="missing `id:` field",
                ))
            if not entry.display:
                violations.append(Violation(
                    target="game",
                    file=str(path.relative_to(PROJECT_ROOT)),
                    line_no=line_no,
                    entry_id=entry_id,
                    msg="missing `display:` field",
                ))
            if not entry.meaning and not is_sentence:
                violations.append(Violation(
                    target="game",
                    file=str(path.relative_to(PROJECT_ROOT)),
                    line_no=line_no,
                    entry_id=entry_id,
                    msg="missing `meaning:` field (or `source:` for sentence entries)",
                ))
            if not entry.level:
                violations.append(Violation(
                    target="game",
                    file=str(path.relative_to(PROJECT_ROOT)),
                    line_no=line_no,
                    entry_id=entry_id,
                    msg="missing `level:` field",
                ))
            if not entry.category:
                violations.append(Violation(
                    target="game",
                    file=str(path.relative_to(PROJECT_ROOT)),
                    line_no=line_no,
                    entry_id=entry_id,
                    msg="missing `category:` field",
                ))

            # Source field — required by ADR-0003
            if not entry.source:
                violations.append(Violation(
                    target="game",
                    file=str(path.relative_to(PROJECT_ROOT)),
                    line_no=line_no,
                    entry_id=entry_id,
                    msg="missing `source:` field (ADR-0003 requires citation to Language wiki)",
                ))
                continue

            # Source must be wikilink format
            if not entry.source.startswith("[[") or not entry.source.endswith("]]"):
                violations.append(Violation(
                    target="game",
                    file=str(path.relative_to(PROJECT_ROOT)),
                    line_no=line_no,
                    entry_id=entry_id,
                    msg=f"`source:` not in wikilink format: {entry.source}",
                ))
                continue

            # Source must resolve
            resolved, detail = source_resolves(entry.source, lang_full, stem_index)
            if not resolved:
                violations.append(Violation(
                    target="game",
                    file=str(path.relative_to(PROJECT_ROOT)),
                    line_no=line_no,
                    entry_id=entry_id,
                    msg=f"`source:` broken — {detail}",
                ))

    return violations


def build_language_path_index() -> dict[str, Path]:
    """Build {vault-path: abs-path} index for Language wiki files.

    Used for resolving `vault:[[Language/Spanish/vocabulary/foo]]` paths.
    """
    path_index: dict[str, Path] = {}
    for path in WIKI_DIR.rglob("*.md"):
        if path.name.endswith(".ko.md"):
            continue
        # Relative path from PROJECT_ROOT, with "Language/" prefix
        rel = "Language/" + str(path.relative_to(LANG_DIR))
        path_index[rel] = path
        # Also index by bare stem
        path_index[path.stem] = path
    return path_index


def resolve_vault_ref(ref: str, lang: str, path_index: dict[str, Path]) -> tuple[bool, str]:
    """Resolve a vault reference like `Language/Spanish/vocabulary/food-vocabulary#tapas`.

    Returns (resolved, detail).
    """
    # Strip section anchor
    target = ref.split("#", 1)[0]
    if not target:
        return False, "empty vault reference"

    # Direct match (Language/Spanish/vocabulary/food-vocabulary)
    if target in path_index:
        return True, f"resolved to {path_index[target].relative_to(PROJECT_ROOT)}"

    # Bare stem match (just `food-vocabulary`)
    bare_stem = target.split("/")[-1]
    if bare_stem in path_index:
        return True, f"resolved (bare stem) to {path_index[bare_stem].relative_to(PROJECT_ROOT)}"

    return False, f"no Language file matches `{target}`"


def audit_openclaw(lang_filter: Optional[str], path_index: dict[str, Path]) -> list[Violation]:
    """Audit .openclaw/workspace/wiki/{lang}/_exposure_log.md for vault:[[Language/...]] references."""
    violations = []

    if not OPENCLAW_ROOT.exists():
        violations.append(Violation(
            target="openclaw",
            file=str(OPENCLAW_ROOT),
            line_no=0,
            entry_id="",
            msg=f"openclaw workspace not found: {OPENCLAW_ROOT}",
        ))
        return violations

    for log_path in sorted(OPENCLAW_ROOT.glob("*/_exposure_log.md")):
        lang_short = log_path.parent.name  # e.g., "korean", "spanish"
        if lang_filter:
            # Match either short code (korean → ko) or lang dir name
            mapped = SHORT_TO_FULL.get(lang_filter, lang_filter.capitalize())
            if lang_short.lower() != lang_filter and mapped.lower() != lang_short.lower():
                continue

        text = log_path.read_text(encoding="utf-8")
        for line_no, line in enumerate(text.splitlines(), 1):
            for m in VAULT_REF_RE.finditer(line):
                ref = m.group(1).strip()
                resolved, detail = resolve_vault_ref(ref, lang_short, path_index)
                if not resolved:
                    violations.append(Violation(
                        target="openclaw",
                        file=str(log_path.relative_to(OPENCLAW_ROOT.parent.parent)),
                        line_no=line_no,
                        entry_id=ref,
                        msg=f"broken vault reference — {detail}",
                    ))

    return violations


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Audit downstream consumers of Language wiki content (ADR-0003 + schema §Downstream)."
    )
    parser.add_argument(
        "--target",
        choices=["game", "openclaw", "all"],
        default="all",
        help="Which downstream to audit (default: all)",
    )
    parser.add_argument(
        "--lang",
        choices=["en", "es", "jp", "kr", "zh", "english", "spanish", "japanese", "korean", "chinese"],
        help="Only this language",
    )
    args = parser.parse_args()

    # Build indices once
    stem_index = build_language_stem_index()
    path_index = build_language_path_index()

    violations: list[Violation] = []

    if args.target in ("game", "all"):
        violations.extend(audit_game_corpus(args.lang, stem_index))

    if args.target in ("openclaw", "all"):
        violations.extend(audit_openclaw(args.lang, path_index))

    # Group by target
    by_target: dict[str, list[Violation]] = defaultdict(list)
    for v in violations:
        by_target[v.target].append(v)

    for target in sorted(by_target):
        items = by_target[target]
        print(f"\n=== {target.upper()} ({len(items)} violations) ===")
        for v in items[:50]:  # limit output
            print(f"  [{v.file}:{v.line_no}] {v.entry_id}")
            print(f"    - {v.msg}")
        if len(items) > 50:
            print(f"  ... and {len(items) - 50} more")

    print()
    print(f"=== Summary ===")
    print(f"Total violations: {len(violations)}")
    if violations:
        by_target_counts = {t: len(v) for t, v in by_target.items()}
        for t, c in by_target_counts.items():
            print(f"  {t}: {c}")
        return 1
    print("[audit] CLEAN")
    return 0


if __name__ == "__main__":
    sys.exit(main())
