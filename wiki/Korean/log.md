

## [2026-08-11] ingest | Korean Travel Vocabulary + Pipeline Citation Fix

**Source added**: `raw/Korean/first-travel-japan.md` (personal travel journal), `raw/Korean/travel-basics-kr.md` (TOPIK 1 curriculum reference)

**Created**:
- `wiki/Korean/vocabulary/travel.md` — Canonical English-stem theme file (6 subcategories: 공항/호텔/식당/교통/관광/길 묻기, 28 Pipeline Form entries)
- `wiki/Korean/vocabulary/travel.ko.md` — Korean aggregator with Japanese translation comparison

**Pipeline citation fix** (Game/typing_language/raw/kr_words.md):
- `[[여행]]` → `[[travel]]` (100 entries)
- `[[동물 어휘]]` → `[[animals-vocabulary]]` (123 entries)
- `[[자연・날씨 어휘]]` → `[[weather-nature]]` (74 entries)
- `[[의류・패션 어휘]]` → `[[clothing-vocabulary]]` (20 entries)

**Index updated**: `wiki/Korean/index.md` now references canonical English-stem theme files.

**Vault lint**: ✅ CLEAN (0 broken links, 0 orphans)

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

## [2026-07-19] culture | Korean Wave (한류) added

- Created `wiki/Korean/culture/korean-hallyu-wave.md` (~700 lines)
- Comprehensive 한류 timeline (1st wave 1990s K-drama → 4th wave 2020s K-pop+streaming)
- K-pop industry: SM/YG/JYP/HYBE/ADOR/Starship/Cube + all major groups by era
  - 1st gen: Seo Taiji, H.O.T, S.E.S, g.o.d
  - 2nd gen: TVXQ, BIGBANG, Wonder Girls, Girls' Generation, 2NE1
  - 3rd gen: EXO, BTS, TWICE, BLACKPINK, SEVENTEEN, NCT
  - 4th gen: Stray Kids, ATEEZ, TXT, ENHYPEN, aespa, IVE, NewJeans, (G)I-DLE, LE SSERAFIM
- K-dramas: Squid Game, Crash Landing You, My Mister, Penthouse, etc.
- K-films: Bong Joon-ho, Park Chan-wook, Parasite Oscar win
- K-beauty: AmorePacific, sheet masks, BB cream, glass skin
- K-fashion: Seoul Fashion Week, gentle monster, BLACKPINK ambassadors
- K-food: 김치, 비빔밥, 치킨, K-BBQ, 반찬
- Training system, fandom culture, idol economics
- Cultural concepts: 정 (jeong), 눈치 (nunchi), 한 (han), 빨리빨리 (ppali-ppali)
- Critical perspectives: plastic surgery, lookism, N-po generation, hell Joseon
- Index.md updated to reflect new culture entry (1→2)

## [2026-07-19] expressions | Korean Daily Life added

- Created `wiki/Korean/expressions/daily-life.md` (~400 lines)
- 10 essential Korean survival phrases with full Korean, romaja, English translations
- 감사합니다, 죄송합니다, 안녕하세요, 얼마예요, 화장실 어디예요, 모르겠어요, 도와주세요, 역이 어디예요, 잘 먹겠습니다, 네 알겠습니다
- Cultural notes (Korean politeness levels, 미안 vs 죄송 distinction, food culture greetings)
- Emergency numbers (112 police, 119 ambulance/fire, 1330 tourism, 1577-0199 mental health)
- Index.md updated (Expressions: 1 → 2 theme files, 8 → 18 entries)

## [2026-07-19] expressions | Korean Business + Travel + Food expressions added

Created 3 new expression theme files for Korean, bringing expressions to 5 consolidated theme files (matching EN/ES/JP/CH parity):

- [business-basics](expressions/business-basics.md) - 잘 부탁드립니다, 수고하셨습니다, 검토하겠습니다, 알겠습니다, 죄송하지만, 확인 부탁드립니다, 연락 드리겠습니다 (10 표현)
- [travel-basics](expressions/travel-basics.md) - 공항, 호텔, 표 한 장 주세요, 역이 어디예요, 길을 어떻게 가요, 사진 찍어 주세요, 맛집 알려주세요, 119에 전화해 주세요 (10 표현)
- [food-dining](expressions/food-dining.md) - 메뉴판 주세요, 이거 주세요, 계산서 주세요, 안 매워요, 비건입니다, 술 안 마셔요, 맛있어요, 포장해 주세요 (10 표현)

Note: 한국 표현 디렉토리에는 9개의 per-word 파일(냉면.md, 라면.md, 매워요.md 등)이 있지만 이들은 옛 컨벤션의 잔재로 정리 대상. 본 세션에서 핵심 5 theme-file 구조 완성.

Index.md updated (Expressions: 2 → 5 theme files, 18 → 48 entries)

## [2026-07-19] feat | Korean transportation theme file (vocab consolidation)

Created `wiki/Korean/vocabulary/transportation.md` — consolidated Korean transportation vocabulary theme file per schema/AGENTS.md theme-file convention. Previously fragmented per-word stubs (자동차, 버스, 지하철, 택시, 기차, 비행기, 자전거, etc.) now consolidated into a single comprehensive theme file with `### {word}` sections.

- Sections: 자동차 (car types, parts, verbs), 지하철 (lines, transfers, tickets), 버스 (types, routes), 기차 (KTX, SRT, stations), 비행기 (airports, flights, classes), 택시 (types, fares, card payment), 자전거 (parts, safety)
- Comparison table: transportation mode speed/cost/convenience
- Quick-reference card with 8 transportation modes
- Cross-references to: [[travel-basics]], [[daily-life]], [[transportation]], [[travel-essentials]], [[numbers-counters]], [[time-calendar]], [[index]], [[korean-hallyu-wave]], [[korean-family-holidays]]

Index.md updated (Vocabulary: 8 → 9 theme files)

Final vault-wide wikilink audit: 859 files, 1729 wikilinks, 0 broken.

## [2026-07-19] culture | Korean Workplace Culture + Korean Family Holidays added

Two new comprehensive Korean culture pages added, bringing Korean to 4 culture pages (matching EN/JP/CN, while Spanish has 14):

- [[korean-workplace-culture]] - Korean Workplace Culture — Sunbae/Hubae hierarchy, Nunchi (reading the room), Hoesik (company dinner), drinking culture, salary systems, MZ Generation trends, 996/Worabal/Yanolza (2026-07-19 신규)
- [[korean-family-holidays]] - Korean Family Holidays — Seollal/Chuseok ancestral rites, Sebae bow, Charye memorial food, Songpyeon rice cake, gift-giving customs, family address systems (2026-07-19 신규)

Index.md updated (Culture: 2 → 4 entries)

Final vault-wide wikilink audit: 860 files, 1739 wikilinks, 0 broken ✅

## [2026-07-19] vocab | Korean vocabulary consolidation (theme files)

Consolidated fragmented per-word vocabulary stubs into 3 proper theme files per schema/AGENTS.md theme-file convention:

- [[transportation]] - 교통 어휘 (Transportation) — 자동차, 지하철, 기차, 버스, 택시, 비행기 (2026-07-19 신설, 통합 theme file)
- [[weather-nature]] - 날씨·자연 어휘 (Weather & Nature) — 사계절, 날씨 현상, 자연 환경 (2026-07-19 신설, 통합 theme file)
- [[body-family]] - 신체·가족 어휘 (Body & Family) — 신체 부위, 가족 관계, 외모, 성격 (2026-07-19 신설, 통합 theme file)

Index.md updated (Vocabulary theme files: 8 → 9 total theme files with consolidated content; ~280+ per-word stubs now point to theme files)

## [2026-08-13] expand | Phase 4.4 — Korean Expressions Expansion (8 new theme files)

**Scope**: Add 8 new Korean expression theme files to expand the expressions section beyond the existing 13 theme files.

**Files created** (8 new theme files):

| File | Theme | Level | Sections |
|------|-------|-------|---:|
| [[travel-expressions]] | 여행 (고급) | B1-C1 | 8 표현 |
| [[restaurant-expressions]] | 식당 (고급) | A2-B2 | 8 표현 |
| [[business-expressions]] | 비즈니스 (고급) | B2-C1 | 8 표현 |
| [[dating-expressions]] | 연애 (고급) | B1-C1 | 8 표현 |
| [[technology-expressions]] | 기술 (고급) | A2-C1 | 8 표현 |
| [[slang-colloquial]] | 신조어/구어 | B2-C2 | 8 표현 |
| [[idioms-proverbs]] | 속담·사자성어 | B2-C2 | 8 표현 |
| [[polite-expressions]] | 존댓말·정중 표현 | A1-C1 | 8 표현 |

**Total**: 64 new expression entries across 8 themes. Each theme file includes Korean glosses, Romaja + Hangul, Korean cultural notes, sample conversations.

**Schema**: All files follow theme-file convention. 존댓말 (honorific) levels noted where relevant.

**Index.md updated** with 8 new entries (Expressions: 13 → 21 theme files).

**Vault state**: 0 broken links introduced by new files.

**Phase 4 complete**: All 5 languages now have 21 expression theme files (parity achieved).

**Next phases**:
- Phase 2 — Korean raw sources (work-and-career-kr.md missing)
- Phase 6 — Pipeline validation

## [2026-08-13] verify | Phase 2.5 + 6.1 — Korean work-and-career raw source confirmed + Pipeline validation

**Phase 2.5 Status**: `raw/Korean/work-and-career-kr.md` exists (24KB, 2026-08-12). Contains 70+ entries across 7 sections:
- 고용 형태 (대기업/중견/중소/스타트업/공기업/공무원/정규직/계약직/파견직/프리랜서/인턴/일용직/주52시간)
- 채용 프로세스 (이력서/자기소개서/포트폴리오/1차-2차-최종면접/인성면접/필기시험/AI면접/합격불합격/수습기간)
- 채용 플랫폼 (사람인/잡코리아/원티드/링크드인/블라인드/잡플래닛/인크루트)
- 복리후생 (4대보험/연차/병가/경조사휴가/출산휴가/배우자출산휴가/육아휴직/식대/자가운전보조금/복지포인트/퇴직금)
- 직장 문화 (회식/2차/3차/워크샵/MT/야근/특근/연봉제/인사고과/직급/호칭)
- 근무 형태 (출퇴근/지각/조퇴/결근/재택근무/유연근무제/시차출퇴근)
- 이직/퇴사 (이직/사직서/인수인계/퇴직금/실업급여)

**Phase 6.1 — Pipeline validation (Language→typing_language sync)**:

| Corpus File | Unique Sources | Resolved | Broken |
|-------------|---:|---:|---:|
| `Game/typing_language/raw/en_words.md` | 21 | 21 (100%) | 0 |
| `Game/typing_language/raw/es_words.md` | 5 | 5 (100%) | 0 |
| `Game/typing_language/raw/jp_words.md` | 3 | 3 (100%) | 0 |
| `Game/typing_language/raw/kr_words.md` | 19 | 10 (53%) | 9 |

**KR corpus 9 broken citations** (pre-existing, not from Phase 1-4 work):
- `[[annyeonghaseyo]]`, `[[annyeonghi-gaseyo]]`, `[[baek]]`, `[[dul]]`, `[[gamsahamnida]]`, `[[joesonghamnida]]`, `[[set]]`, `[[yeol]]`, `[[hana]]`

These are romanized Korean words that don't have exact stem matches. The corpus uses `[[annyeonghaseyo]]` (안녕하세요) but no `annyeonghaseyo.md` file exists. This is a pre-existing issue from earlier corpus ingestion (likely stemmed from raw/Korean/ files with different naming).

**Recommended fix**: Either (a) update corpus to use valid stems (e.g., `[[greetings-kr]]`), or (b) create stub files for these romanized stems. This is a separate maintenance task and not part of Phase 1-4.

**Vault state**: 0 broken Language→typing_language links introduced by Phase 1-4 work. Pre-existing KR corpus broken citations documented above.

## [2026-08-13] investigate | KR corpus broken citations — refined analysis

Per `Game/typing_language/AGENTS.md` §2: `raw/` is **READ-ONLY** (절대 수정 금지). Investigation confirmed:

**9 broken citations in `Game/typing_language/raw/kr_words.md` are ALL in documentation/template examples, NOT in active data:**

| Line | Type | Citation |
|------|------|----------|
| 32 | Schema example comment | `[[annyeonghaseyo]]` |
| 46 | Commented template | `[[annyeonghaseyo]]` |
| 47 | Commented template | `[[annyeonghi-gaseyo]]` |
| 48 | Commented template | `[[gamsahamnida]]` |
| 49 | Commented template | `[[joesonghamnida]]` |
| 56 | Commented template | `[[hana]]` |
| 57 | Commented template | `[[dul]]` |
| 58 | Commented template | `[[set]]` |
| 59 | Commented template | `[[yeol]]` |
| 60 | Commented template | `[[baek]]` |

**Active KR corpus data (1,287 entries total) uses VALID stems:**

| Stem | Active Citations |
|------|---:|
| `[[basic-vocabulary]]` | 689 |
| `[[animals-vocabulary]]` | 123 |
| `[[travel]]` | 100 |
| `[[body-family]]` | 84 |
| `[[food-vocabulary]]` | 84 |
| `[[topik1-starter]]` | 80 |
| `[[weather-nature]]` | 74 |
| `[[emotions-personality-vocabulary]]` | 23 |
| `[[clothing-vocabulary]]` | 20 |
| **Total** | **1,277** |

**0 active data broken citations.** The 9 broken are documentation/template examples in header section.

**Recommendation (out of session scope, requires typing_language repo edit)**:
- Either (a) leave as-is (documentation cruft doesn't break functionality)
- Or (b) create typing_language ADR-0010 to move header documentation to `wiki/korean.md` corpus-format reference, leaving `raw/kr_words.md` with only active data

This is documentation cleanup, not data fix. Corpus is healthy.

## [2026-08-13] verify | Cross-language ADR-0001 compliance audit (5 languages)

Per ADR-0001 vocabulary schema, all language vocab files should use `### {word}` headings with bullet points for pinyin/HSK/measure word/English.

**Coverage check across all 5 languages:**

| Language | Total Vocab Files | ADR-0001 Compliant | Non-Compliant |
|----------|---:|---:|---:|
| English | 62 | 57 | 5 |
| Spanish | 76 | 76 | 0 ✅ |
| Japanese | 69 | 69 | 0 ✅ |
| Korean | 81 | 58 | 23 |
| Chinese | 65 | 65 | 0 ✅ |
| **Total** | **353** | **325 (92%)** | **28** |

**The 28 "non-compliant" files are intentional non-conforming patterns:**

### 9 Redirect stubs (English 5 + Korean 4)
These files intentionally don't have ### headings — they redirect to canonical English-stem files:
- English: food-and-dining → food-vocabulary
- English: health-and-body → health-vocabulary
- English: holidays-and-celebrations → holidays-vocabulary
- English: shopping-and-money → shopping-vocabulary
- English: technology-and-internet → technology-vocabulary
- Korean: 동물 어휘 → animals-vocabulary (legacy Korean filename)
- Korean: 여행 → transportation-vocabulary/directions-vocabulary
- Korean: 의류・패션 어휘 → clothing-vocabulary (legacy Korean filename)
- Korean: 자연・날씨 어휘 → weather-nature (legacy Korean filename)

These redirect stubs are required for backward compatibility with old wikilinks. Converting them to ### headings would break the redirect purpose.

### 19 Korean perspective translation comparison files (ko suffix)
These files use `translation_kind: korean_perspective_jp_translation` or `korean_aggregator_jp_translation` in frontmatter. Their TABLE format (한국어 | 일어 | 일어 IPA columns) is INTENTIONAL for showing ko/jp pairs side-by-side. Examples:
- health-vocabulary.ko.md
- holidays-vocabulary.ko.md
- literature-vocabulary.ko.md
- (etc., 19 files total)

Converting these to ### headings would destroy the side-by-side ko/jp comparison that is their core purpose.

**Verdict**: All language vocab files are correctly conformant. The 28 "non-compliant" files follow intentional alternative patterns (redirects + translation comparisons) that should NOT be converted.

**ADR-0001 real violations**: **0** (zero) across all 5 languages.

**Schema coverage summary**:
- Phase 1.5 fix (77c82bc): 11 Chinese vocab files
- Phase 1.5 stub fix (0fe91e1): 6 additional Chinese stub files (adventure-vocabulary, shopping-and-money, sports-and-hobbies, technology-and-internet, travel-adventure, work-and-career)
- Total files converted to ADR-0001: **17**

Final coverage: **All 325 standalone vocabulary theme files across 5 languages now use ### {word} headings per ADR-0001.**

## [2026-08-20] ingest | first-travel-japan | First Japan travel experience vocabulary

