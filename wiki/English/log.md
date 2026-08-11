# English Learning - Activity Log

## [2026-08-08] ingest | English Nature Vocabulary (raw/English/nature-vocabulary.md)

- Updated `wiki/English/vocabulary/nature-vocabulary.md` with 39 entries (was 2 stub entries)
- Categories: Natural Phenomena (11), Landforms (10), Plants (6), Verbs/Adjectives (12)
- Added IPA pronunciation, etymology, examples, cultural notes, related terms for each entry
- Created source summary: [[sources/nature-vocabulary]]
- Updated index.md (Sources: 19 → 20)
- Pipeline Form YAML appendix includes all 39 entries for game corpus

## [2026-08-08] ingest | English Emotions & Personality Vocabulary (raw/English/emotions-personality-vocabulary.md)

- Updated `wiki/English/vocabulary/emotions-personality-vocabulary.md` with 41 entries (merged with existing detailed 25 entries)
- Categories: Basic Emotions (11), Positive Personality Traits (13), Negative Personality Traits (6), Emotion Verbs (11)
- Added IPA pronunciation, etymology, examples, cultural notes, related terms for each entry
- Created source summary: [[sources/emotions-personality-vocabulary]]
- Updated index.md (Sources: 18 → 19)
- Pipeline Form YAML appendix includes all 41 entries for game corpus

## [2026-08-08] ingest | English Clothing Vocabulary (raw/English/clothing-vocabulary.md)

- Updated `wiki/English/vocabulary/clothing-vocabulary.md` with 30 entries (was 6 stub entries)
- Categories: Basic Clothing (10), Colors & Materials (4), Fabric Materials (4), Verbs/Adjectives (12)
- Added IPA pronunciation, etymology, examples, cultural notes, related terms for each entry
- Created source summary: [[sources/clothing-vocabulary]]
- Updated index.md (Sources: 17 → 18)
- Pipeline Form YAML appendix includes all 30 entries for game corpus

## [2026-08-08] ingest | English Business Vocabulary (raw/English/business-vocabulary.md)

- Updated `wiki/English/vocabulary/business-vocabulary.md` with 52 entries (was 9 tech-only stub entries)
- Categories: Email/Correspondence (11), Meetings & Work (10), Corporate Structure (11), Phone/Communication (4), Business Expressions (4), Communication & Technology (8 merged from existing)
- Added IPA pronunciation, etymology, examples, cultural notes, related terms for each entry
- Created source summary: [[sources/business-vocabulary]]
- Updated index.md (Sources: 16 → 17)
- Pipeline Form YAML appendix includes all 52 entries for game corpus

## [2026-08-08] ingest | English Animals Vocabulary (raw/English/animals-vocabulary.md)

- Updated `wiki/English/vocabulary/animals-vocabulary.md` with 37 entries (was 6 stub entries)
- Categories: Pets & Farm (10), Wild Animals (11), Insects & Marine (6), Verbs/Adjectives (10)
- Added IPA pronunciation, etymology, examples, cultural notes, related terms for each entry
- Created source summary: [[sources/animals-vocabulary]]
- Updated index.md (Sources: 15 → 16)
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
   - `[[theme-stem]]` template-placeholder references (3 occurrences) converted to plain text — were inside backtick wrapping / SESSION_SUMMARY doc contexts
   - `[[meat]]` self-reference check in `wiki/English/vocabulary/food-vocabulary.md` → plain text
   - `[[龍/竜]]` Japanese variant-spelling in `wiki/Japanese/vocabulary/animals-vocabulary.md` → plain text

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

## [2026-07-19] culture | English-Speaking Workplace Culture added

- Created `wiki/English/culture/english-workplace-culture.md` (~400 lines)
- Comprehensive guide to Anglophone business culture (US/UK/CA/AU)
- Topics: directness, hierarchy, communication styles, meeting culture, common idioms, salary/compensation, leave policies
- Includes extensive list of workplace idioms ("touch base", "boil the ocean", "low-hanging fruit", etc.)
- Per-country comparison: US flat/individualist vs UK consensus vs AU "tall poppy syndrome"
- Industry-specific dress codes, remote work culture, performance reviews
- DEI concepts, "drinking from the firehose", "deep dive" jargon
- Index.md updated to reflect new culture entry (1→2)

## [2026-07-19] expressions | English Daily Life added

- Created `wiki/English/expressions/daily-life.md` (~400 lines)
- 10 essential English survival phrases with cultural notes
- Thank you, Excuse me, Hello, How much, Bathroom, Don't understand, Help, Station, Enjoy meal, Yes I understand
- Regional variants: UK (loo, cheers, sorry) vs US (bathroom, thank you) vs AU (g'day, no worries) vs CA (washroom)
- Emergency numbers (911 US/CA, 999 UK, 000 AU, 112 EU)
- Cultural notes on tipping, tax inclusion, card preference
- Index.md updated (Expressions: 2 → 3 theme files, 12 → 22 entries)

## [2026-07-19] expressions | English Business + Travel expressions added

Created 2 new expression theme files for English, bringing expressions to 5 total:

- [business-basics](expressions/business-basics.md) - Thank you for your email, I would appreciate it if, Best regards, I'll follow up next week, I'll get back to you on that, Thank you for your time, Per our discussion, I'd like to schedule a meeting, Thanks for the update, Could you please... (10 표현)
- [travel-basics](expressions/travel-basics.md) - Where is the airport, hotel, train station, Can I have a ticket to ___, How much is a taxi, How do I get to ___, Help, Call 911!, Can you take a photo of me, Where can I find a good restaurant (10 表現)

Index.md updated (Expressions: 3 → 5 theme files, 22 → 42 entries)

## [2026-07-19] culture | English School Culture + Holidays added

Two new comprehensive English culture pages added, bringing English to 5 culture pages (matching ES/KR/CN/JP range):

- [[culture/english-school-life]] - English-Speaking School Culture — US/UK/CA/AU K-12 + college, SAT/A-Levels, prom, dorm life, Ivy League vs Oxbridge (2026-07-19 신규)
- [[culture/english-holidays]] - English-Speaking Holidays — Thanksgiving, Christmas, Halloween, July 4, ANZAC, Remembrance, Black Friday, religious observances (2026-07-19 신규)

Index.md updated (Culture: 2 → 5 entries)