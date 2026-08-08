# Language Tools

> **Parent**: `Language/` LLM Wiki project
> **Updated**: 2026-08-08 (Track C tooling upgrade)

This directory contains Language-specific Python utilities for wiki maintenance, vocabulary ingest, schema validation, and learning activity generation.

## Structure

```
Language/tools/
├── audit_vault.py                  # Symlink → ../../../audit_vault.py (workspace root)
├── generate_yaml_pipeline.py       # ★ Track C — Pipeline YAML generator/validator (ADR-0003)
├── validate_schema.py              # ★ Track C — Page format validator (vocab/culture/grammar/sources)
├── search_wiki.py                  # ★ Track D — Hybrid keyword search (lightweight qmd alternative)
├── audit_downstream.py             # ★ Track E — Cross-project consumer audit (Game + openclaw)
├── add_game_category.py            # ★ Bonus — Auto-inject category field (Track E fix batch)
├── broken_wikilink_processor.py   # Broken wikilink inventory + stub generator
├── extract_cards.py               # Card News Archive → vocabulary extraction
├── linguistic_stub_gen.py         # Auto-generate linguistic stub pages
├── ingest_2026-07-16/             # Historical 2026-07-16 batch (8 scripts + README) — ARCHIVED
└── learning_activities/          # Educational activity scripts (21 .py + README)
```

## Tools

### Active — Maintenance (Tracks C + D + E, 2026-08-08)

| Tool | Purpose | Usage |
|------|---------|-------|
| **`audit_vault.py`** (symlink) | Vault-wide wikilink lint (symlink-aware, 2026-08-07 fix) | `python3 Language/tools/audit_vault.py` |
| **`generate_yaml_pipeline.py`** ★ Track C | Generate / validate `## Pipeline Form` YAML sections in vocabulary theme files (ADR-0003) | `python3 Language/tools/generate_yaml_pipeline.py [--validate] [--lang en] [--dry-run]` |
| **`validate_schema.py`** ★ Track C | Validate wiki page schemas (vocabulary / expressions / culture / grammar / sources / study-plan / comparative) | `python3 Language/tools/validate_schema.py [--lang es] [--page-type culture]` |
| **`search_wiki.py`** ★ Track D | Hybrid keyword search across wiki pages (lightweight qmd alternative, no external deps) | `python3 Language/tools/search_wiki.py "query" [--lang es] [--page-type grammar] [--limit 10]` |
| **`audit_downstream.py`** ★ Track E | Audit downstream consumers (Game corpus + openclaw exposure logs) — verifies cross-project citations | `python3 Language/tools/audit_downstream.py [--target game\|openclaw\|all] [--lang en]` |
| **`add_game_category.py`** ★ Bonus | Auto-inject missing `category:` field into Game corpus YAML entries (from Track E findings) | `python3 Language/tools/add_game_category.py [--lang jp] [--dry-run]` |
| **`broken_wikilink_processor.py`** | Find broken wikilinks, generate stub pages | `python3 Language/tools/broken_wikilink_processor.py --inventory` |
| **`extract_cards.py`** | Extract vocabulary from card news archives | `python3 Language/tools/extract_cards.py` |
| **`linguistic_stub_gen.py`** | Generate linguistic stub pages with metadata | `python3 Language/tools/linguistic_stub_gen.py` |

### search_wiki.py — detail (Track D)

Lightweight `qmd` alternative per `schema/AGENTS.md` §Tools. Searches:
1. **Filename** (path stem)
2. **Section headings** (H1 / H2 / H3)
3. **Body** (full-text keyword match with surrounding context)

Filters: `--lang {en,es,jp,kr,zh}`, `--page-type {vocabulary,expressions,culture,grammar,sources,study-plan,comparative}`, `--include-yaml`, `--limit N`.

**Examples:**
```bash
python3 Language/tools/search_wiki.py "gustar"                   # 12 files
python3 Language/tools/search_wiki.py "subjuntivo" --lang es     # 12 Spanish files
python3 Language/tools/search_wiki.py "tonkatsu"                 # 3 files (한자 + 히라가나)
python3 Language/tools/search_wiki.py "hanja"                    # 9 cross-language files
python3 Language/tools/search_wiki.py "siesta" --page-type culture  # 6 culture pages
```

**Why Python (not qmd)?** `qmd` not installed and Obsidian Dataview plugin not enabled. This tool provides ~80% of qmd's value at zero dependencies. Supports CJK characters (Korean / Japanese / Chinese) and emoji.

Exit codes: 0 = matches found, 1 = no matches, 2 = runtime error.

### wiki/_templates/ — detail (Track D)

`Language/wiki/_templates/` contains 6 markdown templates + README for quick-start scaffolding of new wiki pages:

| Template | Use for |
|---|---|
| `vocabulary-theme.md.template` | new vocabulary theme file |
| `expression-theme.md.template` | new expression theme file |
| `culture-page.md.template` | new culture page |
| `grammar-page.md.template` | new grammar page |
| `source-page.md.template` | new source summary |
| `comparative-page.md.template` | new comparative page |

Usage:
```bash
cp Language/wiki/_templates/vocabulary-theme.md.template \
   Language/wiki/Spanish/vocabulary/transportation-vocabulary.md
# Edit the copy to fill placeholders
```

After creating from template, validate:
```bash
python3 Language/tools/validate_schema.py --lang es --page-type vocabulary
```

### audit_downstream.py — detail (Track E)

Cross-project contract validator per ADR-0003 + schema §Downstream Consumers. Verifies two downstream consumers:

**1. Game corpus (`Game/typing_language/raw/{lang}_words.md`)** — typing_language game
- Each YAML entry MUST have: `id`, `display`, `meaning` (or sentence marker), `level`, `category`, `source`
- `source:` MUST be a wikilink (`[[theme-filename]]`) and MUST resolve to a Language wiki vocabulary theme file
- Sentence entries (`ens_001`, `jps_001`, etc.) — `meaning:` field optional, `display:` IS the sentence

**2. Openclaw (`/Users/emilio/.openclaw/workspace/wiki/{lang}/_exposure_log.md`)** — daily exposure log
- `vault:` wikilink references MUST resolve to actual Language wiki files (Language/... path)
- Cross-language paths supported (e.g., `Language/Spanish/vocabulary/daily-life-vocabulary#levantarse`)

Usage:
```bash
python3 Language/tools/audit_downstream.py --target game          # Game corpus only
python3 Language/tools/audit_downstream.py --target openclaw     # Openclaw only
python3 Language/tools/audit_downstream.py --target all           # Both (default)
python3 Language/tools/audit_downstream.py --target game --lang jp  # Specific language
```

**Findings (2026-08-08):**
- Openclaw: **0 violations** — all vault references resolve ✓
- Game: **921 violations** (all in JP 259 + KR 662 — missing `category:` field)
- Game source citations: **0 broken** — all wikilinks resolve correctly to Language wiki ✓

Exit codes: 0 = clean, 1 = violations, 2 = runtime error.

### add_game_category.py — detail (Bonus batch, 2026-08-08)

Auto-injects missing `category:` field into Game corpus YAML entries.

**Background**: Track E audit found 921 Game corpus entries (JP 259 + KR 662) missing `category:` field per ADR-0003 schema. All missing entries reference `[[basic-vocabulary]]` or `[[travel]]`.

**Strategy**: For each entry missing `category:`, derive category from `source:` wikilink (e.g., `[[basic-vocabulary]]` → `category: basic`). Idempotent — re-runnable.

Usage:
```bash
python3 Language/tools/add_game_category.py --dry-run    # Preview
python3 Language/tools/add_game_category.py             # Apply (JP + KR)
python3 Language/tools/add_game_category.py --lang jp   # Single language
```

**Result (2026-08-08)**: 921 entries fixed → Game corpus **0 violations** ✓

### generate_yaml_pipeline.py — detail

Replaces ad-hoc `/tmp/generate_yaml_v2.py` scripts (used 2026-07-29 to create 1,259 entries). Now canonicalized as `tools/generate_yaml_pipeline.py`.

**Modes:**
- `--generate` (default): Regenerate `## Pipeline Form (machine-readable)` YAML sections from parsed `### {word}` headings. Idempotent.
- `--validate`: Report schema violations (id prefix, missing fields, path-style sources, duplicate IDs, entry count mismatch). No writes.
- `--dry-run`: Preview changes (use with --generate).

**Schema (ADR-0003):**
```yaml
- { id: en_food_vocabulary_001, display: "meat", input: "meat", meaning: "고기", level: "A1", category: "food-vocabulary", source: "[[food-vocabulary]]" }
```

**Filter:** `--lang {en,es,jp,kr,zh}` (process only one language)

**Exit codes:** 0 = clean / regenerated, 1 = violations (validate mode), 2 = runtime error.

### validate_schema.py — detail

Validates broader page format conventions per ADR-0001, ADR-0002, ADR-0003, and `Language/schema/AGENTS.md`.

**Page types validated:**
- `vocabulary`: frontmatter (level/source/category) + `## Pipeline Form` + `## Sources` + ≥1 `### {word}` sections
- `expressions`: frontmatter + `## Sources` + `## {expression}` sections
- `culture`: `**Overview:**` + `## Key Points` + `## Sources` + word count threshold
  - Spanish: also requires `## Ejemplos` (openclaw contract)
- `grammar`: Korean summary block (EN/JA/KO only) + sources section + word count
- `sources`: `**Type:**` + `**Date Added:**` + `**Language Level:**` + `## Summary` + `## Sources`
- `study-plan`: loose (no strict checks)
- `comparative`: word count threshold

**Filters:** `--lang {en,es,jp,kr,zh}`, `--page-type {vocabulary,expressions,culture,grammar,sources,study-plan,comparative}`

**Exit codes:** 0 = clean, 1 = violations, 2 = runtime error.

### One-off / Historical

| Tool | Purpose | Usage |
|------|---------|-------|
| **`add_frontmatter.py`** | Add YAML frontmatter to Language vocabulary files (one-off batch, 2026-07-10 era) | `python3 Language/tools/add_frontmatter.py` |

### Historical (per-batch README)

| Batch | Location | README |
|---|---|---|
| 2026-07-16 | `ingest_2026-07-16/` | [README](ingest_2026-07-16/README.md) |

### Ingest consolidation note (Track C2 — partial)

`tools/ingest_2026-07-16/` 의 8 scripts 는 2026-07-16 의 table-format → theme-file 일회성 변환 batch (이미 완료, archived). 신규 vocabulary ingest 시:

1. **신규 vocabulary 가 theme file 형식이라면**: `generate_yaml_pipeline.py` 가 YAML 자동 생성 → ingest 도구 불필요
2. **신규 vocabulary 가 다른 형식 (table / CSV / JSON)이라면**: `tools/ingest_*.py` 신규 작성 (one-off) → 완료 후 `ingest_YYYY-MM-DD/` 하위 디렉토리에 archive

향후 ingest batch 가 발생하면 위 패턴 따름. 별도 canonical `tools/ingest_word.py` 는 작성하지 않음 (포맷이 다양해 single tool 어려움).

## Conventions

- Python 3.11+
- Each tool self-documents via `argparse --help`
- All scripts are idempotent (re-runnable without side effects)
- Validate mode preferred before generate mode (catch issues first)
- Historical batches preserved for reference, not active maintenance

## See also

- `Language/schema/AGENTS.md` §3 — Ingest workflow
- `Language/decisions/0003-pipeline-yaml-contract.md` — Pipeline YAML contract (ADR-0003)
- `Language/decisions/0001-theme-file-convention.md` — Theme-file convention (ADR-0001)
- `Language/log.md` — historical batch log entries
- `audit_vault.py` (workspace root) — vault-wide wikilink lint
