

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
- Cross-references to: [[expressions/travel-basics]], [[expressions/daily-life]], [[transportation]], [[travel-essentials]], [[numbers-counters]], [[time-calendar]], [[index]], [[korean-hallyu-wave]], [[korean-family-holidays]]

Index.md updated (Vocabulary: 8 → 9 theme files)

Final vault-wide wikilink audit: 859 files, 1729 wikilinks, 0 broken.

## [2026-07-19] culture | Korean Workplace Culture + Korean Family Holidays added

Two new comprehensive Korean culture pages added, bringing Korean to 4 culture pages (matching EN/JP/CN, while Spanish has 14):

- [[culture/korean-workplace-culture]] - Korean Workplace Culture — Sunbae/Hubae hierarchy, Nunchi (reading the room), Hoesik (company dinner), drinking culture, salary systems, MZ Generation trends, 996/Worabal/Yanolza (2026-07-19 신규)
- [[culture/korean-family-holidays]] - Korean Family Holidays — Seollal/Chuseok ancestral rites, Sebae bow, Charye memorial food, Songpyeon rice cake, gift-giving customs, family address systems (2026-07-19 신규)

Index.md updated (Culture: 2 → 4 entries)

Final vault-wide wikilink audit: 860 files, 1739 wikilinks, 0 broken ✅

## [2026-07-19] vocab | Korean vocabulary consolidation (theme files)

Consolidated fragmented per-word vocabulary stubs into 3 proper theme files per schema/AGENTS.md theme-file convention:

- [[vocabulary/transportation]] - 교통 어휘 (Transportation) — 자동차, 지하철, 기차, 버스, 택시, 비행기 (2026-07-19 신설, 통합 theme file)
- [[vocabulary/weather-nature]] - 날씨·자연 어휘 (Weather & Nature) — 사계절, 날씨 현상, 자연 환경 (2026-07-19 신설, 통합 theme file)
- [[vocabulary/body-family]] - 신체·가족 어휘 (Body & Family) — 신체 부위, 가족 관계, 외모, 성격 (2026-07-19 신설, 통합 theme file)

Index.md updated (Vocabulary theme files: 8 → 9 total theme files with consolidated content; ~280+ per-word stubs now point to theme files)
