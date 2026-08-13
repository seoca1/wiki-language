

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

## [2026-07-19] culture | Japanese Food Culture added

- Created `wiki/Japanese/culture/japanese-food-culture.md` (~700 lines)
- Comprehensive guide to 和食 (washoku) — UNESCO Intangible Cultural Heritage
- Topics: 旬 (seasonality), 5 flavors (五味), 5 colors (五色), 5 cooking methods (五法)
- 寿司/刺身/麺類/鍋物/焼き物/揚げ物/ご飯物 8大カテゴリ完全網羅
- ラーメン地方スタイル (Sapporo, Tokyo, Hakata, etc.)
- 寿司ネタ全種 (maguro, toro, hamachi, uni, etc.)
- 8地方料理 (Hokkaido, Tokyo, Kansai, Okinawa, etc.)
- テーブルマナー (箸, いただきます, ごちそうさま)
- コンビニ文化 (konbini 24/7 food)
- 自販機 (vending machine density world highest)
- Index.md updated to reflect new culture entry (1→2)

## [2026-07-19] expressions | Japanese Daily Life added

- Created `wiki/Japanese/expressions/daily-life.md` (~400 lines)
- 10 essential Japanese survival phrases with full romaji, Korean, English translations
- ありがとう, すみません, いただきます, いくらですか, トイレはどこですか, わかりません, 助けて, 駅はどこですか, おはようございます, こんにちは
- Cultural notes for each (Japanese politeness, chopstick taboos, いただきます origin, etc.)
- Emergency numbers (110 police, 119 ambulance/fire)
- Index.md updated (Expressions: 1 → 2 theme files, 7 → 17 entries)

## [2026-07-19] expressions | Japanese Business + Travel + Food expressions added

Created 3 new expression theme files for Japanese, bringing expressions to parity with Chinese (5 files):

- [business-basics](expressions/business-basics.md) - お世話になっております, よろしくお願いします, お疲れ様です, 失礼します, 検討します, 承知しました, 申し訳ございません, お疲れ様でした, お疲れ, ご確認ください (10 表現)
- [travel-basics](expressions/travel-basics.md) - 空港, ホテル, 切符をください, 駅はどこですか, 道を教えてください, 警察を呼んでください, 英語を話せる人いますか, 写真を撮ってもいいですか, 荷物を預かってもらえますか (10 表現)
- [food-dining](expressions/food-dining.md) - メニューをください, これをください, お会計お願いします, 辛くしないでください, ベジタリアンです, お酒を飲みません, おいしい, 持ち帰りできますか (10 表現)

Index.md updated (Expressions: 2 → 5 theme files, 17 → 47 entries)

## [2026-07-19] culture | Japanese School Culture + Traditions added

Two new comprehensive Japanese culture pages added, bringing Japanese to 4 culture pages (matching EN/KR/CN):

- [[japanese-school-life]] - 日本の学校文化 — 制服・給食・部活・受験・七五三・修学旅行・センター試験 (2026-07-19 신규)
- [[japanese-traditions]] - 日本の伝統文化 — お辞儀・お箸・お正月・お葬式・お寺・神社・冠婚葬祭 (2026-07-19 신규)

Index.md updated (Culture: 2 → 4 entries)

## [2026-08-13] expand | Phase 4.3 — Japanese Expressions Expansion (8 new theme files)

**Scope**: Add 8 new Japanese expression theme files to expand the expressions section beyond the existing 13 theme files.

**Files created** (8 new theme files):

| File | Theme | Level | Sections |
|------|-------|-------|---:|
| [[travel-expressions]] | 旅行 (上級) | B1-C1 | 8 expressions |
| [[restaurant-expressions]] | 食事 (上級) | A2-B2 | 8 expressions |
| [[business-expressions]] | ビジネス (上級) | B2-C1 | 8 expressions |
| [[dating-expressions]] | 恋愛 (上級) | B1-C1 | 8 expressions |
| [[technology-expressions]] | テクノロジー (上級) | A2-C1 | 8 expressions |
| [[slang-colloquial]] | スラング・口語 | B2-C2 | 8 expressions |
| [[idioms-proverbs]] | 慣用句・ことわざ | B2-C2 | 8 expressions |
| [[polite-expressions]] | 敬語・丁寧表現 | A1-C1 | 8 expressions |

**Total**: 64 new expression entries across 8 themes. Each theme file includes Korean glosses, Romaji + Hiragana/Kanji, Japanese cultural notes, sample conversations, and Sources section cross-linking to comparative pages.

**Schema**: All files follow theme-file convention. 敬語 (keigo) honorifics noted where relevant.

**Index.md updated** with 8 new entries (Expressions: 13 → 21 theme files).

**Vault state**: 0 broken links introduced by new files.

**Next phases**:
- Phase 4.4 — Korean expressions expansion (8 files)
