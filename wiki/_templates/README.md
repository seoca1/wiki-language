# Language Wiki Templates

> **Parent**: `Language/wiki/_templates/`
> **Added**: 2026-08-08 (Track D — Discovery upgrade)

Quick-start scaffolding for new wiki pages. Templates follow `Language/schema/AGENTS.md` §3 page format standards and ADRs 0001-0004.

## Usage

Copy a template to the target location, then fill in the placeholders:

```bash
# Example: create a new vocabulary theme file
cp Language/wiki/_templates/vocabulary-theme.md.template \
   Language/wiki/Spanish/vocabulary/transportation-vocabulary.md
# Then edit the file to replace placeholders like {theme-name}, {word1}, etc.
```

Templates use `{placeholder}` syntax for values to be filled in. Lines starting with `# TODO:` are reminders to complete during filling.

## Available Templates

| Template | For | Output Location | Format Standard |
|---|---|---|---|
| `vocabulary-theme.md.template` | vocabulary/{theme}.md | `wiki/{Lang}/vocabulary/` | ADR-0001 + ADR-0003 (Pipeline YAML) |
| `expression-theme.md.template` | expressions/{theme}.md | `wiki/{Lang}/expressions/` | ADR-0001 + schema §3.2 |
| `culture-page.md.template` | culture/{topic}.md | `wiki/{Lang}/culture/` | schema §3.4 + openclaw Ejemplos (ES) |
| `grammar-page.md.template` | grammar/{topic}.md | `wiki/{Lang}/grammar/` | Track B1 + ADR-0002 |
| `source-page.md.template` | sources/{source-title}.md | `wiki/{Lang}/sources/` | schema §3.5 |
| `comparative-page.md.template` | comparative/{topic}.md | `wiki/comparative/` | ADR-0004 |

## Per-Language Notes

### Korean
- Speech level: 해요체 (default), 합쇼체 (formal), 해체 (casual)
- 한자 (hanja) for Sino-Korean words where useful
- Irregular conjugations (ㄷ/ㅂ/ㅅ/ㅎ/르) flagged
- Particles: 은/는 (topic) / 이/가 (subject) distinction

### Japanese
- Furigana (ruby text) for kanji
- Politeness level: casual / polite / honorific
- Particles: は/が/を/に/で distinction
- Kanji readings in hiragana

### Spanish
- Regional variants: España vs LatAm
- tú vs usted (register)
- Conjugation tables for verbs
- Gender / plural forms

### English
- Learner mistakes + false cognates
- Phrasal verbs (highly idiomatic)
- Register: formal / informal / slang

### Chinese
- Tones (mā/má/mǎ/mà/ma) — 4 tones + neutral
- Simplified vs Traditional
- 量词 (measure words) — e.g., 个/条/只/张/本
- HSK 1-6 scale (not JLPT/TOPIK)
- Pinyin: tone-marked (nǐ hǎo) for body, numbered (ni3 hao3) for YAML `input` field
- Bilingual zh ↔ KO parallel display (user is Korean speaker)

## Validation

After creating a page from a template, validate it:

```bash
python3 Language/tools/validate_schema.py --lang {lang} --page-type {type}
```

Or regenerate Pipeline YAML for new vocabulary themes:

```bash
python3 Language/tools/generate_yaml_pipeline.py --lang {lang}
```

## See also

- `Language/schema/AGENTS.md` §3 — Page format standards
- `Language/decisions/0001-theme-file-convention.md` — Theme-file convention
- `Language/decisions/0003-pipeline-yaml-contract.md` — YAML schema (7 fields)
- `Language/decisions/0004-comparative-wiki-scope.md` — Comparative page criteria
- `Language/tools/validate_schema.py` — Page format validator
- `Language/tools/generate_yaml_pipeline.py` — Pipeline YAML generator
