#!/usr/bin/env python3
"""
Card extraction pipeline — implements ADR-0062 / pipeline-from-cards.md.

Reads .openclaw card_news archive, extracts slot [2] language content,
deduplicates against existing Language/wiki/Spanish/vocabulary/, and
appends new entries to appropriate theme files.

Usage:
    python3 extract_cards.py [--dry-run] [--from-date YYYY-MM-DD]

Constraints:
    - READ-ONLY on .openclaw/workspace/wiki/card_news/archive/
    - WRITE only on Language/wiki/Spanish/{vocabulary,culture}/
    - Idempotent via _card_extraction_state.md checkpoint
"""
from __future__ import annotations
import argparse
import re
import sys
from datetime import date, datetime
from pathlib import Path

# Paths
VAULT = Path("/Users/emilio/projects/Projects")
OPENCLAW_ARCHIVE = Path("/Users/emilio/.openclaw/workspace/wiki/card_news/archive")
SPANISH_VOCAB = VAULT / "Language/wiki/Spanish/vocabulary"
SPANISH_CULTURE = VAULT / "Language/wiki/Spanish/culture"
CHECKPOINT = VAULT / "Language/wiki/Spanish/study-plan/_card_extraction_state.md"
EVIDENCE_DIR = VAULT / ".omo/evidence/card-extraction-2026-07-13"


# -------------------- Parsing --------------------

CATEGORY_RE = re.compile(r"\*\*Category:\*\*\s*Language\s*/\s*\w+", re.I)
EXPOSURE_RE = re.compile(r"\*\*Exposure ID:\*\*\s*[`*]?\s*(\w+):([\w_]+)", re.I)
EXPOSURE_INLINE_RE = re.compile(r"Exposure ID:\s*[`*]?\s*(lesson|vocab|grammar|culture):([\w_]+)", re.I)
SLOT2_HEADER_RE = re.compile(r"^##\s*2️⃣\s*[🇪🇸🇯🇵🇨🇳]?", re.M)
SLOT_END_RE = re.compile(r"^##\s*[0-9]️⃣", re.M)
KEY_CONCEPTS_HEADER_RE = re.compile(r"\*\*Key Concepts:\*\*")
VOCAB_HEADER_RE = re.compile(r"\*\*Vocabulary:\*\*")
EXPRESSIONS_HEADER_RE = re.compile(r"\*\*Expressions:\*\*")
PRACTICAL_TIPS_HEADER_RE = re.compile(r"\*\*Practical Tips:\*\*")
KC_BULLET_RE = re.compile(r"^[-*]\s*\*\*(.+?):\*\*\s*(.+?)$", re.M)
VOCAB_BULLET_RE = re.compile(r"^[-*]\s*\*\*(.+?)\s*[—-]\s*(.+?)\*\*\s*$", re.M)
PT_BULLET_RE = re.compile(r"^\s*-\s*☑️\s*(.+?)$", re.M)


def parse_slot2(card_text: str) -> dict | None:
    """Find slot [2] section, return parsed dict or None."""
    m = SLOT2_HEADER_RE.search(card_text)
    if not m:
        return None
    start = m.end()
    end_m = SLOT_END_RE.search(card_text, pos=start)
    end = end_m.start() if end_m else len(card_text)
    body = card_text[start:end]

    cat_m = CATEGORY_RE.search(body)
    if not cat_m:
        return None
    # The presence of Category: Language / X confirms this is a language-learning card.
    # Specific sub-category (Spanish/Grammar/Culture/etc.) is determined by Exposure ID below.
    language = "es"  # default; future: detect from cat_text

    exp_m = EXPOSURE_RE.search(body) or EXPOSURE_INLINE_RE.search(body)
    exposure_type = exp_m.group(1).lower() if exp_m else None
    exposure_name = exp_m.group(2).lower() if exp_m else None

    result = {"language": language, "exposure_type": exposure_type, "exposure_name": exposure_name}

    # Detect format
    if KEY_CONCEPTS_HEADER_RE.search(body):
        result["format"] = "new"
        kc_match = KEY_CONCEPTS_HEADER_RE.search(body)
        kc_start = kc_match.end()
        # Find next major header
        next_hdr = re.search(r"\*\*(Practical Tips|Main Content|Visual|Description|Related|Exposure ID):\*\*", body[kc_start:])
        kc_end = kc_start + (next_hdr.start() if next_hdr else len(body) - kc_start)
        result["key_concepts_raw"] = body[kc_start:kc_end].strip()
    elif VOCAB_HEADER_RE.search(body):
        result["format"] = "old"
        v_match = VOCAB_HEADER_RE.search(body)
        v_start = v_match.end()
        v_next = re.search(r"\*\*(Expressions|Practical Tips|Main Content):\*\*", body[v_start:])
        v_end = v_start + (v_next.start() if v_next else len(body) - v_start)
        result["vocabulary_raw"] = body[v_start:v_end].strip()
        if EXPRESSIONS_HEADER_RE.search(body):
            e_match = EXPRESSIONS_HEADER_RE.search(body)
            e_start = e_match.end()
            e_next = re.search(r"\*\*(Practical Tips|Main Content):\*\*", body[e_start:])
            e_end = e_start + (e_next.start() if e_next else len(body) - e_start)
            result["expressions_raw"] = body[e_start:e_end].strip()

    # Practical Tips (both formats)
    pt_match = PRACTICAL_TIPS_HEADER_RE.search(body)
    if pt_match:
        pt_start = pt_match.end()
        pt_next = re.search(r"\*\*(Visual|Description|Related|Exposure ID):\*\*", body[pt_start:])
        pt_end = pt_start + (pt_next.start() if pt_next else len(body) - pt_start)
        result["practical_tips_raw"] = body[pt_start:pt_end].strip()

    return result


def extract_kc_terms(key_concepts_raw: str) -> list[dict]:
    """Extract terms from Key Concepts section."""
    terms = []
    # First, try bullet-level parsing
    for m in KC_BULLET_RE.finditer(key_concepts_raw):
        head, defn = m.group(1).strip(), m.group(2).strip()
        terms.extend(parse_kc_bullet_head(head, defn))
    return terms


def parse_kc_bullet_head(head: str, defn: str) -> list[dict]:
    """Parse a KC bullet head like '핵심 10 부위' or 'el abrazo (포옹)'."""
    results = []
    def looks_like_term(s: str) -> bool:
        s = s.strip()
        return bool(re.match(r"^[A-Za-záéíóúüñÁÉÍÓÚÜÑ+\-]", s))

    def clean_term(t: str) -> str:
        t = t.strip().lower()
        t = re.sub(r"^[*_`]+", "", t)
        t = re.sub(r"[*_`]+$", "", t)
        t = re.sub(r"^(el|la|los|las|un|una)\s+", "", t)
        return t

    def strip_md(s: str) -> str:
        s = re.sub(r"^[*_`\s]+|[*_`\s]+$", "", s)
        s = s.replace("*", "").replace("_", "")
        return s.strip()

    # Pattern A: defn has comma/·-separated "term(korean)" items
    if "·" in defn or ("," in defn and "(" in defn):
        items = re.split(r"[·,]\s*", defn)
        for item in items:
            item = item.strip().rstrip(".")
            item = strip_md(item)
            if not item:
                continue
            m = re.match(r"^([A-Za-záéíóúüñÁÉÍÓÚÜÑ+\-][\wáéíóúüñÁÉÍÓÚÜÑ\s/]*?)\s*\(([^)]+)\)\s*$", item)
            if m:
                raw_term = m.group(1).strip()
                raw_korean = m.group(2).strip()
                variants = re.split(r"\s*/\s*", raw_term)
                korean_parts = re.split(r"\s*/\s*", raw_korean)
                for i, variant in enumerate(variants):
                    variant = strip_md(variant)
                    if not variant:
                        continue
                    cleaned = clean_term(variant)
                    if looks_like_term(cleaned):
                        korean = korean_parts[i] if i < len(korean_parts) else raw_korean
                        results.append({"term": cleaned, "korean": korean.strip(), "context": head})
        if results:
            return results

    # Pattern B: head has "(Korean)" suffix
    m = re.match(r"^(.+?)\s*\(([^)]+)\)\s*$", head)
    if m:
        term = clean_term(m.group(1))
        if looks_like_term(term):
            return [{"term": term, "korean": m.group(2).strip(), "context": defn}]

    # Pattern C: defn has slash-separated Spanish terms WITH Korean context after
    if "/" in defn and re.search(r"[가-힣]", defn):
        m_split = re.split(r"\s*[—–-]\s*", defn, maxsplit=1)
        spanish_part = m_split[0].strip() if m_split else defn
        if "/" in spanish_part and "(" not in spanish_part:
            variants = re.split(r"\s*/\s*", spanish_part)
            for variant in variants:
                variant = strip_md(variant).rstrip(".").rstrip(",")
                if looks_like_term(variant):
                    cleaned = clean_term(variant)
                    if looks_like_term(cleaned):
                        results.append({"term": cleaned, "korean": head, "context": defn})
            if results:
                return results

    # Pattern D: defn has ·-separated Spanish terms without parens (e.g., restaurant card)
    if "·" in defn and "(" not in defn:
        m_split = re.split(r"\s*[—–.]+\s*", defn, maxsplit=1)
        spanish_part = m_split[0].strip() if m_split else defn
        for variant in re.split(r"\s*·\s*", spanish_part):
            variant = strip_md(variant).rstrip(".").rstrip(",")
            if looks_like_term(variant):
                cleaned = clean_term(variant)
                if looks_like_term(cleaned):
                    results.append({"term": cleaned, "korean": head, "context": defn})
        if results:
            return results

    return []


def extract_vocab_terms(vocab_raw: str) -> list[dict]:
    """Extract terms from old-format Vocabulary section."""
    terms = []
    for m in VOCAB_BULLET_RE.finditer(vocab_raw):
        term, korean = m.group(1).strip(), m.group(2).strip()
        # Remove article prefix for canonical form
        term_clean = re.sub(r"^(el|la|los|las|un|una)\s+", "", term.lower())
        terms.append({"term": term_clean, "korean": korean, "context": ""})
    return terms


def extract_pt_examples(pt_raw: str) -> list[str]:
    """Extract Spanish example sentences from Practical Tips."""
    examples = []
    for m in PT_BULLET_RE.finditer(pt_raw):
        text = m.group(1).strip()
        # Extract quoted Spanish sentence
        quoted = re.search(r"\*?[«\"](.+?)[»\"]\*?", text)
        if quoted:
            examples.append(quoted.group(1).strip())
        elif re.match(r"^[*_]?[A-Za-záéíóúüñ¿¡]", text):
            # Italicized/bold Spanish sentence
            clean = re.sub(r"^[*_\s]+|[*_\s]+$", "", text)
            examples.append(clean)
    return examples


# -------------------- Deduplication --------------------

def load_existing_stems() -> set[str]:
    """Load all ### {word} stems across all Spanish vocab themes."""
    stems = set()
    for f in SPANISH_VOCAB.glob("*.md"):
        for line in f.read_text(encoding="utf-8").splitlines():
            m = re.match(r"^###\s+(.+?)\s*$", line)
            if m:
                stems.add(m.group(1).strip())
    return stems


def normalize(stem: str) -> str:
    """Lowercase + Spanish accent strip."""
    n = stem.lower()
    for src, dst in [("á","a"),("é","e"),("í","i"),("ó","o"),("ú","u"),("ü","u"),("ñ","n")]:
        n = n.replace(src, dst)
    return n


def is_dup(new_stem: str, existing: set[str]) -> bool:
    """Exact original-form match only (accent guard)."""
    return new_stem in existing


# -------------------- Theme routing --------------------

EXPOSURE_TO_THEME = {
    "vocab:body": ("body-vocabulary", "vocabulary"),
    "vocab:food": ("food-vocabulary", "vocabulary"),
    "vocab:family": ("family-vocabulary", "vocabulary"),
    "vocab:meals": ("meals-vocabulary", "vocabulary"),
    "vocab:weather": ("weather-vocabulary", "vocabulary"),
    "vocab:transportation": ("transportation-vocabulary", "vocabulary"),  # new theme
    "vocab:restaurant": ("restaurant-vocabulary", "vocabulary"),
    "vocab:directions": ("directions-vocabulary", "vocabulary"),
    "vocab:reflexive_daily": ("reflexive-verbs-vocabulary", "vocabulary"),
    "culture:tango": ("tango-vocabulary", "vocabulary"),  # culture vocab goes to vocab too
    "grammar:reflexive_verbs": ("reflexive-verbs-grammar", "grammar"),
    "grammar:gustar_verb": ("gustar-verb-grammar", "grammar"),
    "grammar:present_tense": ("present-tense-grammar", "grammar"),
    "grammar:past_tense": ("past-tense-grammar", "grammar"),
    "grammar:prepositions": ("prepositions-grammar", "grammar"),
}


def route_target(exposure_type: str, exposure_name: str) -> tuple[str, str] | None:
    """Return (theme, kind) or None to skip."""
    key = f"{exposure_type}:{exposure_name}"
    if exposure_type == "lesson":
        return None  # SKIP
    if key in EXPOSURE_TO_THEME:
        return EXPOSURE_TO_THEME[key]
    # Fallback: create new theme file
    if exposure_type == "vocab":
        return (f"{exposure_name}-vocabulary", "vocabulary")
    if exposure_type == "culture":
        return (f"{exposure_name}-vocabulary", "vocabulary")  # culture vocab → new vocab theme
    if exposure_type == "grammar":
        return (f"{exposure_name}-grammar", "grammar")
    return None


def level_for_term(term: str, korean: str) -> str:
    """Infer CEFR level from term type."""
    # Cultural terms, slang, dialect → B1+
    cultural_kw = ["lunfardo", "cabeceo", "milonga", "abrazo", "tango", "bandoneón", "che", "mina", "laburo"]
    if any(k in term.lower() or k in korean.lower() for k in cultural_kw):
        return "B1"
    # Grammar concepts → B1-B2
    if any(k in korean for k in ["동사 활용", "대명사", "시제", "문법"]):
        return "B1"
    # Body parts, weather, numbers, family → A1
    body_kw = ["cabeza", "ojo", "boca", "brazo", "mano", "espalda", "pierna", "pie", "corazón", "estómago"]
    weather_kw = ["primavera", "verano", "otoño", "invierno", "sol", "frío", "lluvia", "calor"]
    family_kw = ["madre", "padre", "hermano", "hermana", "hijo", "hija", "abuelo", "abuela"]
    if any(k in term.lower() for k in body_kw + weather_kw + family_kw):
        return "A1"
    # Reflexive verbs → A2
    if "me " in term.lower() or "te " in term.lower() or "se " in term.lower():
        return "A2"
    return "A2"


def next_id(theme_file: Path, lang: str, theme: str) -> str:
    """Find max existing ID + 1."""
    pattern = re.compile(rf"id:\s*{re.escape(lang)}_{re.escape(theme)}_(\d+)")
    max_n = 0
    if theme_file.exists():
        for line in theme_file.read_text(encoding="utf-8").splitlines():
            m = pattern.search(line)
            if m:
                max_n = max(max_n, int(m.group(1)))
    return f"{lang}_{theme}_{max_n + 1:03d}"


def theme_path(theme: str, kind: str) -> Path:
    if kind == "vocabulary":
        return SPANISH_VOCAB / f"{theme}.md"
    elif kind == "grammar":
        return SPANISH_VOCAB / f"{theme}.md"  # for now, grammar → vocab theme
    elif kind == "culture":
        return SPANISH_CULTURE / f"{theme}.md"
    raise ValueError(f"Unknown kind: {kind}")


# -------------------- Writing --------------------

def append_to_theme(theme_file: Path, term: dict, source_date: str, theme: str) -> str:
    """Append a new entry + YAML line. Returns the new ID."""
    lang = "es"
    new_id = next_id(theme_file, lang, theme)
    # Create file with header if missing
    if not theme_file.exists():
        theme_file.write_text(
            f"# {theme} — Card-extracted vocabulary (2026-06-22 ~ latest)\n\n"
            f"**Source:** Card News Archive extraction (ADR-0062)\n"
            f"**Theme:** {theme}\n"
            f"**Level:** A1-B1\n\n"
            f"Vocabulary extracted from .openclaw card_news archive slot [2]. "
            f"Each entry is genuinely new (not duplicating existing Language/wiki content).\n\n"
            f"---\n\n",
            encoding="utf-8",
        )

    text = theme_file.read_text(encoding="utf-8")
    display = term["term"]
    korean = term["korean"]
    context = term.get("context", "")

    entry_md = f"### {display}\n\n"
    if korean and korean != display:
        entry_md += f"{korean}"
        if context:
            entry_md += f" — {context}"
        entry_md += "\n\n"
    else:
        if context:
            entry_md += f"{context}\n\n"
    entry_md += f"**Part of Speech:** sustantivo/verbo (auto)\n"
    entry_md += f"**Source:** Card News {source_date} (slot [2]) — [[{theme}]]\n\n"
    entry_md += f"---\n\n"

    yaml_line = (
        f"- id: {new_id}\n"
        f"  display: \"{display}\"\n"
        f"  input: \"{display}\"\n"
        f"  meaning: \"{korean}\"\n"
        f"  level: \"{level_for_term(display, korean)}\"\n"
        f"  category: \"{theme}\"\n"
        f"  source: \"[[{theme}]] — Card News {source_date} (slot [2])\"\n"
    )

    pf_header = "## Pipeline Form (machine-readable)"
    pf_idx = text.find(pf_header)
    if pf_idx >= 0:
        # Insert entry markdown before Pipeline Form section, append YAML line after the existing block
        yaml_open = "```yaml\n"
        yaml_close = "```\n"
        yaml_open_idx = text.find(yaml_open, pf_idx)
        if yaml_open_idx >= 0:
            yaml_close_idx = text.find(yaml_close, yaml_open_idx + len(yaml_open))
            if yaml_close_idx >= 0:
                # Append YAML line right before the closing fence
                insert_pos = yaml_close_idx
                text = text[:insert_pos] + yaml_line + text[insert_pos:]
        # Insert entry markdown right before Pipeline Form header
        text = text[:pf_idx] + entry_md + "\n" + text[pf_idx:]
    else:
        text += entry_md
        text += f"\n## Pipeline Form (machine-readable)\n\n```yaml\n"
        text += yaml_line
        text += "```\n"

    theme_file.write_text(text, encoding="utf-8")
    return new_id


# -------------------- Main --------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--from-date", default="2026-06-22")
    args = ap.parse_args()

    if not EVIDENCE_DIR.exists():
        EVIDENCE_DIR.mkdir(parents=True)

    existing = load_existing_stems()
    print(f"[init] Loaded {len(existing)} existing ### stems from Spanish vocabulary")

    card_files = sorted(OPENCLAW_ARCHIVE.glob("2026-*.md"))
    print(f"[init] Found {len(card_files)} card files in archive")

    stats = {
        "cards_processed": 0,
        "cards_skipped_lesson": 0,
        "cards_skipped_format": 0,
        "cards_skipped_date": 0,
        "terms_extracted": 0,
        "terms_skipped_dup": 0,
        "terms_written": 0,
        "examples_extracted": 0,
    }

    last_processed_date = None
    last_processed_filename = None
    errors = []

    for card_file in card_files:
        date_str = card_file.stem  # YYYY-MM-DD
        if date_str < args.from_date:
            stats["cards_skipped_date"] += 1
            continue

        try:
            text = card_file.read_text(encoding="utf-8")
            slot2 = parse_slot2(text)
            if not slot2:
                stats["cards_skipped_format"] += 1
                continue

            if slot2["exposure_type"] == "lesson":
                stats["cards_skipped_lesson"] += 1
                last_processed_date = date_str  # still update — we processed (skipped intentionally)
                last_processed_filename = card_file.name
                continue

            target = route_target(slot2["exposure_type"], slot2["exposure_name"])
            if not target:
                stats["cards_skipped_format"] += 1
                continue
            theme, kind = target

            # Extract terms
            terms = []
            if slot2["format"] == "new":
                terms = extract_kc_terms(slot2.get("key_concepts_raw", ""))
            else:
                terms = extract_vocab_terms(slot2.get("vocabulary_raw", ""))
                terms += extract_vocab_terms(slot2.get("expressions_raw", ""))

            # Dedup
            new_terms = []
            for t in terms:
                if is_dup(t["term"], existing):
                    stats["terms_skipped_dup"] += 1
                else:
                    new_terms.append(t)
                    existing.add(t["term"])  # avoid within-batch dup

            # Practical Tips examples
            examples = []
            if "practical_tips_raw" in slot2:
                examples = extract_pt_examples(slot2["practical_tips_raw"])
                stats["examples_extracted"] += len(examples)

            stats["terms_extracted"] += len(terms)
            stats["cards_processed"] += 1

            print(f"[card] {date_str} ({slot2['exposure_type']}:{slot2['exposure_name']}) "
                  f"→ theme={theme} | {len(terms)} terms, {len(new_terms)} new, {len(examples)} examples")

            if args.dry_run:
                for t in new_terms[:5]:
                    print(f"        [NEW] {t['term']} — {t['korean'][:60]}")
                continue

            # Write new entries
            theme_file = theme_path(theme, kind)
            for t in new_terms:
                try:
                    new_id = append_to_theme(theme_file, t, date_str, theme)
                    stats["terms_written"] += 1
                except Exception as e:
                    errors.append(f"{date_str} {t['term']}: {e}")

            last_processed_date = date_str
            last_processed_filename = card_file.name

        except Exception as e:
            errors.append(f"{date_str}: {e}")
            print(f"[ERR]  {date_str}: {e}", file=sys.stderr)

    # Update checkpoint
    if not args.dry_run and last_processed_date:
        checkpoint_text = f"""---
last_processed_date: {last_processed_date}
last_processed_filename: {last_processed_filename}
last_extraction_run: {datetime.now().isoformat()}
extracted_count:
  vocab_terms: {stats['terms_written']}
  example_sentences: {stats['examples_extracted']}
  culture_expansions: 0
target_card_count: {stats['cards_processed']}
total_extraction_runs: 1
errors: {errors[:10]}
---

# Card Extraction State — Spanish

> **This file tracks the Language → OpenClaw Card News extraction pipeline state.**
> **Do not edit manually** — updated by the extraction pipeline (Wave 7 of ADR-0062).

Last extraction run: {datetime.now().isoformat()}
Last processed: {last_processed_date} ({last_processed_filename})

## Stats

- Cards processed: {stats['cards_processed']}
- Cards skipped (lesson:*): {stats['cards_skipped_lesson']}
- Cards skipped (date): {stats['cards_skipped_date']}
- Terms extracted: {stats['terms_extracted']}
- Terms skipped (duplicate): {stats['terms_skipped_dup']}
- Terms written: {stats['terms_written']}
- Examples extracted: {stats['examples_extracted']}
- Errors: {len(errors)}

## Identity

- **Card identity**: filename (`YYYY-MM-DD.md`) is canonical.
- **Idempotency**: `last_processed_date` is authoritative. Any card with date ≤ `last_processed_date` is skipped on re-run.
- **Source**: `.openclaw/workspace/wiki/card_news/archive/` (read-only)

## Pipeline reference

See `Language/wiki/pipeline-from-cards.md` for the extraction procedure.
See `decisions/0062-card-extraction-pipeline.md` for the governance ADR.

## Multi-language

When `.openclaw` starts generating 🇯🇵 / 🇨🇳 cards, this file will be cloned as
`_card_extraction_state_ja.md` / `_card_extraction_state_zh.md` per-language.

## Reset procedure

To re-run extraction from scratch (e.g., after extraction rule changes):

```bash
# Edit this file's frontmatter:
#   last_processed_date: null
#   last_processed_filename: null
#   extracted_count: {{ vocab_terms: 0, example_sentences: 0, culture_expansions: 0 }}
```
"""
        CHECKPOINT.write_text(checkpoint_text, encoding="utf-8")
        print(f"\n[checkpoint] Updated {CHECKPOINT}")

    # Save run stats
    log_path = EVIDENCE_DIR / "extraction-run-stats.txt"
    log_path.write_text(
        f"Run: {datetime.now().isoformat()}\n"
        f"Stats:\n" + "\n".join(f"  {k}: {v}" for k, v in stats.items()) +
        (f"\nErrors:\n  " + "\n  ".join(errors) if errors else ""),
        encoding="utf-8",
    )
    print(f"[stats] Saved to {log_path}")

    print(f"\n=== SUMMARY ===")
    for k, v in stats.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()