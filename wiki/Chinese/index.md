# Chinese Learning Wiki - Index

Last updated: 2026-07-13 (grammar ingest: basic-particles + word-order)

> Chinese (zh) is the **5th language** in the vault, expanding the prior 4-language footprint (English / Japanese / Korean / Spanish). This index follows the same pattern as the other languages' indexes; section headers and theme-file conventions are inherited from `Language/schema/AGENTS.md` (lines 267-294) and the `theme-file` convention established in the 2026-07-10 lint session (no per-word / per-expression `.md` files).

## Vocabulary (5 theme files)

The Chinese vocabulary section landed its first 5 theme files on 2026-07-13 from the OpenClaw raw batch. All entries carry a Pipeline Form YAML appendix at the bottom of each file (5-field schema + `source` anchor per `wiki/pipeline-to-game.md` L33-39). All entries preserve the OpenClaw pinyin notation (tone marks), with numbered-pinyin variants in the YAML `input` field so the game pipeline can pick whichever form it needs.

- [[body-zh]] — 신체 부위 (身体部位). 11 words (HSK 1-2).
- [[colors-zh]] — 색깔 (颜色). 11 words (HSK 1-2).
- [[family-zh]] — 가족 호칭 (家庭成员). 11 words (HSK 1-2).
- [[measure-words-zh]] — 양사 (量词). 11 words (HSK 1-2).
- [[numbers-zh]] — 숫자 (数字). 12 words (HSK 1).

Planned future theme families (mirroring the other languages):

- Travel — 旅行 — airport, hotel, restaurant, transportation, directions
- Food & Restaurant — 食物与餐厅 — ingredients, dishes, beverages, dining
- Business — 商务 — email, meetings, corporate vocabulary
- Emotions & Personality — 情绪与性格 — feelings, traits, verbs
- Nature & Weather — 自然与天气 — phenomena, landforms, plants
- Animals — 动物 — pets, wild animals, insects, marine life
- Clothing & Fashion — 服装与时尚 — garments, materials, colors

## Expressions (0 theme files / 0 entries)

The Chinese expressions section is empty at scaffold time. The plan is to follow the theme-file convention (one theme file per category, with per-expression `### {entry}` sections) rather than per-expression pages.

- _No theme files yet. Pending first ingest._

## Culture (0 entries)

The Chinese culture section is empty at scaffold time. Future entries will cover high-level topics (festivals, regional differences, language policy, cuisine culture, etc.) and will be written as essay-length pages, not as per-fact pages.

- _No entries yet. Pending first ingest._

## Sources (4 processed)

The Chinese sources section absorbed 4 lesson files from `.openclaw/workspace/wiki/chinese/lessons/` on 2026-07-13. Each source page follows the Source Summary format from `Language/schema/AGENTS.md` lines 225-265 (Type / Date Added / Language Level + Summary / Key Takeaways / Vocabulary Extracted / Expressions Extracted / Cultural Insights / Notes).

- [[pinyin-basics-zh]] — Pinyin Basics (Pinyin_Basics.md). HSK 1 beginner. Lesson on the romanization system (21 initials + 38 finals + 4 tones).
- [[tone-pairs-zh]] — Tone Pairs (Tone_Pairs_Chinese.md). HSK 1 beginner. Tone sandhi rules (3+3, 一, 不).
- [[greetings-zh]] — Greetings and Self-Introduction (Greetings_Chinese.md). HSK 1 beginner. 20 greetings + 是 (shì) self-intro pattern.
- [[daily-routine-zh]] — Daily Routine in Chinese (Daily_Routine_Chinese.md). HSK 1-2 beginner. Time + verb pattern + 17 routine verbs.

## Grammar (2 entries)

The Chinese grammar section was initialized on 2026-07-13 with 2 entries absorbed from `.openclaw/workspace/wiki/chinese/grammar/`. Each page is HSK 1-2 beginner level with detailed Korean learner notes (한국어 학습자 주의 / 한국 한자음 ≠ 중국 병음 warning).

- [[basic-particles]] — 기본 조사 (的/了/在/有) — 소유격/완료/위치/소유 4종 + 한국어 비교 + 5단계 학습법 + 실전 회화
- [[word-order]] — 어순 (Word Order, 语序) — SVO 구조 + 한국어 SOV 와의 차이 + 20 흔한 어순 패턴 + 의문문/부정

## Conventions

This wiki follows the same conventions as the other Language wikis:

- **Theme-file convention**: vocabulary and expressions live as theme files (e.g. `food-vocabulary.md`), with per-word / per-expression sections inside. No single-word or single-sentence `.md` files.
- **Pipeline Form YAML**: every vocabulary page carries the game-pipeline YAML appendix (5 fields: `display` / `input` / `meaning` / `level` / `category` + `source`) so the typing game at `Game/typing_language/` can ingest via theme-anchor citations.
- **Wikilinks**: Obsidian stem matching; cross-references should use `[[wikilink]]` form.
- **raw/ is read-only**: the `raw/Chinese/` directory is owned by upstream sources. This wiki writes only to `wiki/Chinese/`.
- **log.md**: every change appends a `## [YYYY-MM-DD] {kind} | {summary}` entry to `log.md` for parseability.

## See also

- `Language/schema/AGENTS.md` — Index Format spec (lines 267-294)
- `Language/wiki/English/index.md` — English index (reference pattern)
- `Language/wiki/Korean/index.md` — Korean index (reference pattern)
- `Language/wiki/Spanish/index.md` — Spanish index (most complete pattern)
- `Language/wiki/content-lineage.md` — content lineage across languages
- `.openclaw/workspace/wiki/Chinese/` — OpenClaw runtime workspace for Chinese (cross-project pipeline)
