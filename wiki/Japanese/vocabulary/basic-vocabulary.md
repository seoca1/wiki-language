---
title: "Basic Vocabulary — Japanese"
created: 2026-07-30
phase: "JP corpus aggregator"
description: "Common Japanese vocabulary spanning greetings, numbers, colors, food, animals, kanji_basic. Aggregates 548 JP corpus citations that previously had no resolvable theme-file target."
language: ja
---

# Basic Vocabulary — Japanese (基本語彙)

> **Aggregator 페이지**: 이 페이지는 `Game/typing_language/raw/jp_words.md` 코퍼스의 `source: [[basic-vocabulary]]` 인용을 resolve하기 위해 생성됨 (2026-07-30). JP corpus 548 entries (전체의 92.7%) 가 이 theme-file을 인용함.

## 카테고리 분포

| 카테고리 | JP | KO | ES | EN |
|---|--:|--:|--:|--:|
| greeting | 6 | 6 | 7 | 5 |
| number | 20 | 10 | 13 | 12 |
| color | 4 | 11 | 11 | 11 |
| food | 15 | 19 | 15 | 15 |
| animal | 8 | 12 | 8 | 9 |
| kanji_basic | 70 | 0 | 0 | 0 |
| body | 10 | 10 | 6 | 6 |
| family | 15 | 15 | 9 | 8 |
| time | 30 | 20 | 14 | 15 |
| nature | 25 | 15 | 12 | 15 |
| misc | 345+ | (in other vocab themes) | | |
| **Total** | **548** | — | — | — |

## 게재 단어 (대표 샘플)

### 인사 (Greetings) — 6 entries
- こんにちは (konnichiwa) — hello
- おはよう (ohayou) — good morning
- こんばんは (konbanwa) — good evening
- ありがとう (arigatou) — thank you
- さようなら (sayounara) — goodbye
- すみません (sumimasen) — excuse me

### 숫자 (Numbers) — 20 entries (jp_007~jp_026)
- 一 (いち/ichi) — one
- 二 (に/ni) — two
- 三 (さん/san) — three
- 四 (よん/yon, し/shi) — four
- 五 (ご/go) — five
- 六 (ろく/roku) — six
- 七 (なな/nana, しち/shichi) — seven
- 八 (はち/hachi) — eight
- 九 (きゅう/kyuu, く/ku) — nine
- 十 (じゅう/juu) — ten
- ... (百/千/万 extended)

### 색깔 (Colors) — 4 entries
- あか (あか/aka) — red
- あお (あお/ao) — blue
- しろ (しろ/shiro) — white
- くろ (くろ/kuro) — black

### 음식 (Food) — 15+ entries
- みず (みず/mizu) — water
- ごはん (ごはん/gohan) — rice/meal
- さかな (さかな/sakana) — fish
- ... (greetings, food staples)

### 동물 (Animals) — 8 entries
- ねこ (ねこ/neko) — cat
- いぬ (いぬ/inu) — dog
- ... (common animals)

### 한자 기초 (Kanji Basic) — 70 entries (jp_030~jp_099)
- 一, 二, 三, 四, 五, 六, 七, 八, 九, 十, 人, 日, 月, 火, 水, 木, 金, 土, 山, 川, ... (JLPT N5 한자 set)

## 왜 aggregator 페이지인가?

다른 언어 (EN/ES/KR) 에는 `basic-vocabulary.md` 가 vocabulary/ 디렉토리에 직접 존재함:
- `Language/wiki/English/vocabulary/basic-vocabulary.md` (88 EN 인용)
- `Language/wiki/Spanish/vocabulary/basic-vocabulary.md` (76 ES 인용)
- `Language/wiki/Korean/vocabulary/basic-vocabulary.md` — 한국어에서는 `topik1-starter.md` 가 유사 역할

JP 는 2026-07-10 테마 파일 컨벤션 (per-word .md 금지) 적용 시점에 basic-vocabulary.md 생성이 누락됨. 본 페이지로 그 갭 마감.

## 인제스트 출처

모든 entry는 다음 중 하나의 출처에서 인용:
- **JLPT N5 단어 목록** (일본어 능력시험 N5 급 어휘)
- **Genki I & II** 교재 (일본어 입문)
- **Tae Kim's Guide to Learning Japanese** (온라인 문법 가이드)

## 게임 통합

`prototype/src/data/jp_corpus.ts` 자동 로드:
- `source: [[basic-vocabulary]]` 인용 entry는 이 페이지의 display/meaning 필드를 사용
- JLPT N5 한자 entry는 `kanji-n5.md` 도 자동 cross-reference

## Sources

- `Game/typing_language/raw/jp_words.md` (548 entries)
- `Language/wiki/Japanese/vocabulary/numbers-vocabulary.md` (cross-reference for detailed number forms)
- `Language/wiki/Japanese/vocabulary/colors-vocabulary.md` (cross-reference for color vocabulary)
- `Language/wiki/Japanese/kanji-n5.md` (cross-reference for kanji_n5 entries)
