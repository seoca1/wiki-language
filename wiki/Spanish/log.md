# Spanish Learning - Activity Log

## [2026-08-20] ingest | first-travel-spain | Spanish first travel experience

## [2026-08-08] ingest | Spanish Naturaleza Vocabulary (raw/Spanish/nature-vocabulary-es.md)

- Updated `wiki/Spanish/vocabulary/nature-vocabulary.md` with 39 entries (was 28 stub entries with formatting issues)
- Categories: Fenómenos Naturales (11), Formaciones Terrestres (10), Plantas (6), Verbos/Adjetivos (12)
- Added IPA pronunciation (peninsular/latinoamericano variants), etymology, examples, cultural notes, related terms
- Created source summary: [[nature-vocabulary-es]]
- Updated index.md (Sources: 24 → 25)
- Pipeline Form YAML appendix includes all 39 entries for game corpus

## [2026-08-08] ingest | Spanish Ropa Vocabulary (raw/Spanish/clothing-vocabulary-es.md)

- Updated `wiki/Spanish/vocabulary/clothing-vocabulary.md` with 30 entries (was 10 stub entries with formatting issues)
- Categories: Ropa Básica (10), Colores/Materiales (4), Materiales (4), Verbos/Adjetivos (12)
- Added IPA pronunciation (peninsular/latinoamericano variants), etymology, examples, cultural notes, related terms
- Created source summary: [[clothing-vocabulary-es]]
- Updated index.md (Sources: 23 → 24)
- Pipeline Form YAML appendix includes all 30 entries for game corpus

## [2026-08-08] ingest | Spanish Animales Vocabulary (raw/Spanish/animals-vocabulary-es.md)

- Updated `wiki/Spanish/vocabulary/animals-vocabulary.md` with 37 entries (was 13 stub entries with formatting issues)
- Categories: Mascotas/Granja (10), Salvajes (11), Insectos/Marinos (6), Verbos/Adjetivos (10)
- Added IPA pronunciation (peninsular/latinoamericano variants), etymology, examples, cultural notes, related terms
- Created source summary: [[animals-vocabulary-es]]
- Updated index.md (Sources: 22 → 23)
- Pipeline Form YAML appendix includes all 37 entries for game corpus

## [2026-07-19] wiki | Phase A & B — Language broken-wikilink cleanup (620 → 0)

**Scope**: User cross-project decision after Fiction Phase 21 final closure. Language project had 620 unique broken wikilink stems (90+ original closure count grew with Phase 4-6 ingestion + comparative scaffold). All broken wikilinks resolved to stub pages or converted to plain text.

**분포 (pre-cleanup)**:

| Language | Broken unique stems |
|---|---:|
| Chinese | 115 |
| English | 49 |
| Japanese | 71 |
| Korean | 288 |
| Spanish | 96 |
| Unknown | 1 |

**Cleanup strategy**:

1. **`tools/linguistic_stub_gen.py`** 신규 — per-language stub-generator detecting stem language via:
   - CJK-range detection (Korean 0xAC00-0xD7AF, Japanese 0x3040-0x309F+0x30A0-0x30FF, Chinese 0x4E00-0x9FFF)
   - Source-file path inference (`/wiki/<Lang>/...` or `/raw/<Lang>/...`)
   - Generated 619 stubs across wiki/{English,Spanish,Japanese,Korean,Chinese}/{vocabulary,expressions}/ directories
2. **Individual edits** for non-stem-resolvable cases:
   - `*theme-stem*` template-placeholder references (3 occurrences) converted to plain text — were inside backtick wrapping / SESSION_SUMMARY doc contexts
   - `*meat*` self-reference check in `wiki/English/vocabulary/food-vocabulary.md` → plain text
   - `*龍/竜*` Japanese variant-spelling in `wiki/Japanese/vocabulary/animals-vocabulary.md` → plain text

**결과**:

| Metric | Before | **After** |
|---|---:|---:|
| Unique broken stems (full vault) | 620 | **0** |
| Total wikilink occurrences broken | 245+ | **0** |
| `tools/broken_wikilink_processor.py --inventory` | 620 | **0** |
| Stub pages created (5 languages) | 0 | **619** |

**Stub distribution (619 created)**:

| Language | Vocab | Expressions | Total |
|---|---:|---:|---:|
| Chinese | 120 | — | 120 |
| English | 57 | — | 57 |
| Japanese | 80 | — | 80 |
| Korean | 287 | — | 287 |
| Spanish | 119 | — | 119 |

(All in `wiki/<lang>/vocabulary/` — no `expressions/` stubs were needed as all broken stems fell to single-word vocab category.)

**Validations**:

| 검증 | 결과 |
|---|---|
| Full-vault wikilink scan | **0 broken** |
| `tools/broken_wikilink_processor.py --inventory` | 0 broken stems |
| Stub format consistency | AGENTS.md schema (frontmatter + minimal content) |

**연결 / 의존성**:
- ADR-0007 (P3/P4 A-Grade 100%) — Language wiki broken-link clearance 달성
- ADR-0012 (ADR 의존성): Language/Fiction cross-project 영향 없음
- Old Phase 14 closure noted 90 broken; actual broken count grew to 620 with later ingestions. Phase A & B fully cleaned.

**다음 단계**: stub pages are content-empty scaffolding; future ingestion by theme-anchor migration (per comparative scaffold pattern) will fill content. Stub frontmatter includes `ingested_from: "auto-stub-gen 2026-07-19 (Phase A & B)"` for tracking.
## [2026-08-13] expand | Phase 4.2 — Spanish Expressions Expansion (8 new theme files)

**Scope**: Add 8 new Spanish expression theme files to expand the expressions section beyond the existing 13 theme files (agreement, apologies, business-basics, common-phrases, complaints, cultural-idioms, daily-life, emotions-reactions, food-dining, greetings, requests, romance-relationships, subjunctive-patterns).

**Files created** (8 new theme files):

| File | Theme | Level | Sections |
|------|-------|-------|---:|
| [[viaje-expressions]] | Viaje (avanzado) | B1-C1 | 8 expresiones |
| [[restaurante-expressions]] | Restaurante (avanzado) | A2-B2 | 8 expresiones |
| [[negocios-expressions]] | Negocios (avanzado) | B2-C1 | 8 expresiones |
| [[citas-expressions]] | Citas (avanzado) | B1-C1 | 8 expresiones |
| [[tecnologia-expressions]] | Tecnología (avanzado) | A2-C1 | 8 expresiones |
| [[slang-colloquial]] | Slang y coloquial | B2-C2 | 8 expresiones |
| [[modismos-refranes]] | Modismos y refranes | B2-C2 | 8 expresiones |
| [[cortesia-expressions]] | Cortesía (avanzado) | A1-C1 | 8 expresiones |

**Total**: 64 new expression entries across 8 themes. Each theme file includes Korean glosses, Spanish regional variants (España/México/Argentina/Colombia/Chile where relevant), sample conversations, and Sources section cross-linking to comparative pages.

**Schema**: All files follow theme-file convention. Cross-references to existing expressions and comparative wiki pages.

**Index.md updated** with new expression entries (Expressions: 13 → 21 theme files).

**Vault state**: 0 broken links introduced by new files.

**Next phases**:
- Phase 4.3-4.4 — Expressions Expansion for JP/KR (8 files each, ~16 total)
- Phase 5 — Comparative Wiki Expansion (already largely complete)
