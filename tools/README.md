# Language Tools

> **Parent**: `Language/` LLM Wiki project
> **Updated**: 2026-07-28

This directory contains Language-specific Python utilities for wiki maintenance, vocabulary ingest, and learning activity generation.

## Structure

```
Language/tools/
├── audit_vault.py                  # Symlink → ../../../audit_vault.py (workspace root)
├── broken_wikilink_processor.py   # Broken wikilink inventory + stub generator
├── extract_cards.py               # Card News Archive → vocabulary extraction
├── linguistic_stub_gen.py         # Auto-generate linguistic stub pages
├── ingest_2026-07-16/             # Historical 2026-07-16 batch (8 scripts + README)
└── learning_activities/          # Educational activity scripts (21 .py + README)
```

## Tools

### Active

| Tool | Purpose | Usage |
|------|---------|-------|
| **`audit_vault.py`** (symlink) | Vault-wide wikilink lint (symlink-aware, 2026-08-07 fix) | `python3 Language/tools/audit_vault.py` |
| **`broken_wikilink_processor.py`** | Find broken wikilinks, generate stub pages | `python3 Language/tools/broken_wikilink_processor.py --inventory` |
| **`extract_cards.py`** | Extract vocabulary from card news archives | `python3 Language/tools/extract_cards.py` |
| **`linguistic_stub_gen.py`** | Generate linguistic stub pages with metadata | `python3 Language/tools/linguistic_stub_gen.py` |

### One-off / Historical

| Tool | Purpose | Usage |
|------|---------|-------|
| **`add_frontmatter.py`** | Add YAML frontmatter to Language vocabulary files (one-off batch, 2026-07-10 era) | `python3 Language/tools/add_frontmatter.py` |

### Historical (per-batch README)

| Batch | Location | README |
|---|---|---|
| 2026-07-16 | `ingest_2026-07-16/` | [README](ingest_2026-07-16/README.md) |
| Learning activities | `learning_activities/` | [README](learning_activities/README.md) |

## Conventions

- Python 3.11+
- Each tool self-documents via `argparse --help`
- All scripts are idempotent (re-runnable without side effects)
- Historical batches preserved for reference, not active maintenance

## See also

- `Language/schema/AGENTS.md` §3 — Ingest workflow
- `Language/log.md` — historical batch log entries
- `audit_vault.py` (workspace root) — vault-wide wikilink lint
