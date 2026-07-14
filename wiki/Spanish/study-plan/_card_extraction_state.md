---
last_processed_date: 2026-07-13
last_processed_filename: 2026-07-13.md
last_extraction_run: 2026-07-14T10:17:10.925289
extracted_count:
  vocab_terms: 5
  example_sentences: 21
  culture_expansions: 0
target_card_count: 16
total_extraction_runs: 1
errors: []
---

# Card Extraction State — Spanish

> **This file tracks the Language → OpenClaw Card News extraction pipeline state.**
> **Do not edit manually** — updated by the extraction pipeline (Wave 7 of ADR-0062).

Last extraction run: 2026-07-14T10:17:10.925298
Last processed: 2026-07-13 (2026-07-13.md)

## Stats

- Cards processed: 16
- Cards skipped (lesson:*): 5
- Cards skipped (date): 24
- Terms extracted: 74
- Terms skipped (duplicate): 69
- Terms written: 5
- Examples extracted: 21
- Errors: 0

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
#   extracted_count: { vocab_terms: 0, example_sentences: 0, culture_expansions: 0 }
```
