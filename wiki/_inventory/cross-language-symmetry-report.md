# Cross-Language Symmetry Report

**Generated**: 2026-08-19
**Tool**: `tools/symmetry_check.py`
**Scope**: 5 main languages (EN/ES/JP/KR/ZH) + auxiliary (comparative, French, German)

## Coverage Summary

| Content Type | Lang | Files | YAML Cov |
|---|---|---:|---:|
| vocabulary | English | 40 | 100% |
| vocabulary | Spanish | 42 | 100% |
| vocabulary | Japanese | 40 | 100% |
| vocabulary | Korean | 48 | 100% |
| vocabulary | Chinese | 65 | 100% |
| vocabulary | French | 5 | 0% |
| vocabulary | German | 5 | 0% |
| expressions | English | 21 | 100% |
| expressions | Spanish | 21 | 100% |
| expressions | Japanese | 21 | 100% |
| expressions | Korean | 21 | 100% |
| expressions | Chinese | 21 | 100% |
| expressions | French | 1 | 0% |
| expressions | German | 1 | 0% |
| culture | English | 43 | n/a |
| culture | Spanish | 43 | n/a |
| culture | Japanese | 43 | n/a |
| culture | Korean | 46 | n/a |
| culture | Chinese | 43 | n/a |
| grammar | English | 6 | n/a |
| grammar | Spanish | 5 | n/a |
| grammar | Japanese | 6 | n/a |
| grammar | Korean | 6 | n/a |
| grammar | Chinese | 6 | n/a |
| sources | English | 21 | n/a |
| sources | Spanish | 34 | n/a |
| sources | Japanese | 22 | n/a |
| sources | Korean | 21 | n/a |
| sources | Chinese | 20 | n/a |
| study-plan | English | 1 | n/a |
| study-plan | Spanish | 4 | n/a |
| study-plan | Japanese | 1 | n/a |
| study-plan | Korean | 1 | n/a |
| study-plan | Chinese | 1 | n/a |

## Auxiliary Directories

| Directory | Files |
|---|---:|
| comparative | 65 |

## Detected Asymmetries

### 🔴 ALERT (7)

- **[vocabulary]** vocabulary: Chinese=65 vs French=5 (delta=60)
- **[expressions]** expressions: English=21 vs French=1 (delta=20)
- **[sources]** sources: Spanish=34 vs Chinese=20 (delta=14)
- **[vocabulary]** French/vocabulary: 0/5 files have Pipeline Form YAML (0%)
- **[vocabulary]** German/vocabulary: 0/5 files have Pipeline Form YAML (0%)
- **[expressions]** French/expressions: 0/1 files have Pipeline Form YAML (0%)
- **[expressions]** German/expressions: 0/1 files have Pipeline Form YAML (0%)

### 🟡 WARN (7)

- **[culture]** culture: Korean=46 vs English=43 (delta=3)
- **[study-plan]** study-plan: Spanish=4 vs English=1 (delta=3)
- **[adr-staleness]** ADR-0001 references missing path: `_inventory/BROKEN_WIKILINKS_2026-07-11.md`
- **[adr-staleness]** ADR-0001 references missing path: `_inventory/BROKEN_WIKILINKS_2026-07-11.md`
- **[adr-staleness]** ADR-0003 references missing path: `tools/generate_yaml.py`
- **[adr-staleness]** ADR-0004 references missing path: `wiki/Korean/comparative/politeness.md`
- **[adr-staleness]** ADR-0004 references missing path: `wiki/Korean/comparative/politeness.md`

### 🔵 INFO (2)

- **[adr-staleness]** Candidate `schema/vocabulary.md` appears resolved in ADR — promote or remove
- **[adr-staleness]** Candidate `tools/symmetry_check.py` appears resolved in ADR — promote or remove

## Resolution Status

Symmetry gaps fall into 3 buckets:

1. **Pilot-in-progress** (expected) — partial rollout already documented in `decisions/README.md`
2. **Known intentional** — French/German scaffolded-only by design per **ADR-0007** (2026-08-19, Option 2 Document); raw/ = Phase 15/16 seed README only. YAML 0% is intentional. Promote via ADR-0008 when user provides raw.
3. **Actionable** — needs follow-up session to close gap

### ADR Staleness Findings

- 🟡 ADR-0001 references missing path: `_inventory/BROKEN_WIKILINKS_2026-07-11.md`
- 🟡 ADR-0001 references missing path: `_inventory/BROKEN_WIKILINKS_2026-07-11.md`
- 🟡 ADR-0003 references missing path: `tools/generate_yaml.py`
- 🟡 ADR-0004 references missing path: `wiki/Korean/comparative/politeness.md`
- 🟡 ADR-0004 references missing path: `wiki/Korean/comparative/politeness.md`
- 🔵 Candidate `schema/vocabulary.md` appears resolved in ADR — promote or remove
- 🔵 Candidate `tools/symmetry_check.py` appears resolved in ADR — promote or remove

Run `python3 Language/tools/symmetry_check.py` after any batch to refresh this view.
