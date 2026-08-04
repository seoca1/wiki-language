# Chinese Learning Wiki - Index

Last updated: 2026-07-29 (cross-cutting comparative/grammar pages added) (index sync: added orphan pages from expressions/, sources/, culture/)

> Chinese (zh) is the **5th language** in the vault, expanding the prior 4-language footprint (English / Japanese / Korean / Spanish). This index follows the same pattern as the other languages' indexes; section headers and theme-file conventions are inherited from `Language/schema/AGENTS.md` (lines 267-294) and the `theme-file` convention established in the 2026-07-10 lint session (no per-word / per-expression `.md` files).

## Vocabulary

- [[time-vocabulary]] - Chinese 시간 어휘 (today/tomorrow/morning/afternoon/evening/night/weekend/hour) (5 theme files)

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
- [[time-zh]] - 时间 (Time) — 일상 시간 표현 (HSK 1-2)
- [[weather-zh]] - 天气 (Weather) — 기상 + 계절 (HSK 1-2)
- [[education-zh]] - 教育 (Education) — 학교/학습 어휘 (HSK 2-3)
- [[education-vocabulary]] - 교육 어휘 (multi-language comparison)

## Expressions

- [[common-phrases]] - Chinese 핵심 일상 표현 (greeting/clarification/request/question) (5 theme files / ~60 entries)

The Chinese expressions section was expanded on 2026-07-19 from scaffold state to 5 theme files. All follow the theme-file convention (one theme file per category, with per-expression `## {entry}` sections) and contain bilingual (zh-KO) phrasebook with usage notes.

- [[daily-basics]] — 매일 기본 표현 (15 핵심 표현 + 紧急 호출)
- [[dating-romance]] — 연애 표현 (12 표현, 缘分, 相亲, 老公/老婆)
- [[business-basics]] — 비즈니스 표현 (10 표현, 报价, 合同, 发票, 请多关照)
- [[travel-basics]] — 여행 표현 (10 표현, 机场, 出租车, 酒店, 报警)
- [[food-dining]] — 식당 표현 (10 표현, 菜单, 买单, 不要辣, 我吃素)

## Culture (4 entries)

The Chinese culture section was expanded on 2026-07-19 with 4 comprehensive essay-length pages.

- [[chinese-dating-culture]] — Chinese Dating Culture — 相亲, 90/00后 세대, 결혼 시장 변화
- [[chinese-cuisine-culture]] — Chinese Cuisine Culture — 8대 菜系, 차 문화, 테이블 매너, 현대 트렌드
- [[family-and-filial-piety]] — Chinese Family & Filial Piety — 孝, 421困境, 4-2-1 구조, 가족 명절
- [[chinese-workplace-culture]] — Chinese Workplace Culture — Guanxi, Mianzi, Banquet, 996, N-po Generation, Civil Service Exam

## Sources (8 processed)

The Chinese sources section absorbed lesson files from `.openclaw/workspace/wiki/chinese/lessons/` on 2026-07-13 (4 files) and expanded with culture source pages on 2026-07-19 (5 files). Each source page follows the Source Summary format from `Language/schema/AGENTS.md` lines 225-265 (Type / Date Added / Language Level + Summary / Key Takeaways / Vocabulary Extracted / Expressions Extracted / Cultural Insights / Notes).

### Lesson Sources (4)

- [[pinyin-basics-zh]] — Pinyin Basics (Pinyin_Basics.md). HSK 1 beginner. Lesson on the romanization system (21 initials + 38 finals + 4 tones).
- [[tone-pairs-zh]] — Tone Pairs (Tone_Pairs_Chinese.md). HSK 1 beginner. Tone sandhi rules (3+3, 一, 不).
- [[greetings-zh]] — Greetings and Self-Introduction (Greetings_Chinese.md). HSK 1 beginner. 20 greetings + 是 (shì) self-intro pattern.
- [[daily-routine-zh]] — Daily Routine in Chinese (Daily_Routine_Chinese.md). HSK 1-2 beginner. Time + verb pattern + 17 routine verbs.

### Culture & Grammar Sources (4)

- [[basic-particles-zh]] — Basic Particles (的/了/在/有). HSK 1-2. 소유격/완료/위치/소유 4종 + 한국어 비교.
- [[word-order-zh]] — Word Order (语序). HSK 1-2. SVO 구조 + 한국어 SOV 와의 차이.
- [[chinese-family-zh]] — Chinese Family Source. 가족 문화, 孝道, 421 family.
- [[chinese-food-culture-zh]] — Chinese Food Culture Source. 8대 菜系, 차 문화.

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

## Round 2 — Index Reconciliation (2026-07-30)

> Orphan pages reconciled from filesystem. Descriptions from each file's Overview section.

### Expressions (added 3)
- [[expressions/greetings]] — Chinese 问候表达 — 你好、初次见面、您好 (5+ entries)
- [[expressions/apologies]] — Chinese 道歉表达 — 对不起、抱歉、请原谅 (5+ entries)
- [[expressions/agreement]] — Chinese 同意表达 — 好、是的、可以、没错 (5+ entries)

### Vocabulary (added 11)
- [[vocabulary/family-vocabulary]] — Chinese 家庭词汇 — 父母/兄弟姐妹/亲戚 (5+ entries)
- [[vocabulary/colors-vocabulary]] — Chinese 颜色词汇 — 基本颜色表达 (5+ entries)
- [[vocabulary/months-vocabulary]] — Chinese 月份词汇 — 一月~十二月 + 季节 (5+ entries)
- [[vocabulary/technology-vocabulary]] — Chinese 技术词汇 — 计算机/互联网/数字 (5+ entries)
- [[vocabulary/ordinal-numbers-vocabulary]] — Chinese 序数词汇 — 第一、第二、第三... (5+ entries)
- [[vocabulary/weekdays-vocabulary]] — Chinese 星期词汇 — 周一~周日 (5+ entries)
- [[vocabulary/weather-vocabulary]] — Chinese 天气词汇 — 晴/雨/雪/阴 + 气象表达 (5+ entries)
- [[vocabulary/transportation-vocabulary]] — Chinese 交通词汇 — 汽车/地铁/公交/出租车 (5+ entries)
- [[vocabulary/directions-vocabulary]] — Chinese 方向词汇 — 东/西/南/北 + 位置表达 (5+ entries)
- [[vocabulary/health-vocabulary]] — Chinese 健康词汇 — 医院/症状/身体 (5+ entries)
- [[vocabulary/numbers-vocabulary]] — Chinese 数字词汇 — 一~十 + 基本数字 (5+ entries)

### Study Plan (added 1)
- [[study-plan/README]] — Chinese study-plan placeholder — meets AGENTS.md 7-subdirectory requirement

## Cross-Language Comparisons

See [[index]] for systematic EN/ES/JP/KR/CH comparisons. Especially relevant for Chinese:

- [[politeness-honorifics]] — 您 vs 你; titles (王老师, 张经理) default address
- [[numbers-counters]] — Mandatory **measure words** (个/位/只/条/张); 两 vs 二 before classifiers
- [[cultural-values]] — **Guanxi** (关系), **Mianzi** (面子), **Yuanfen** (缘分), **Chiku** (吃苦)
- [[family-kinship]] — 爷爷/外公 (paternal vs maternal) split; 表/堂 cousin distinction
- [[food-dining]] — 8大菜系 vs 5-language food comparison
- [[writing-systems]] — Simplified vs Traditional; pinyin; radicals
- [[dating-romance]] — 缘分, 相亲, 老公/老婆 vs EN/ES/JP/KR
- [[mood-systems]] — Chinese modal adverbs (会/要) vs Spanish subjunctive / JP-KR mood suffixes
- [[tense-aspect-systems]] — Chinese aspect particles (了/过) vs tense-heavy systems
- [[diatopic-variation-patterns]] — Chinese 普通话/粤语/闽南语/吴语 (most divergent of 5 langs)
- [[tradiciones-veraniegas]] — Chinese 午休 (wǔxiū, 30-60 min) vs Spanish siesta
- [[lunch-and-rest-patterns]] — Chinese 11:30-12:30 lunch + 午休 culture
- [[master-cheatsheet]] — One-page essential reference per language
