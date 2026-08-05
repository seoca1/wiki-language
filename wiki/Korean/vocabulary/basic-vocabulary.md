---
title: "기초 어휘 — Korean"
created: 2026-07-30
phase: "KR corpus aggregator"
description: "Common Korean vocabulary spanning greetings, numbers, colors, food, animals, basic expressions. Aggregates 697 KR corpus citations."
language: ko
---

# 기초 어휘 — Korean

> **Aggregator 페이지**: `Game/typing_language/raw/kr_words.md` 코퍼스의 `source: [[basic-vocabulary]]` 인용을 resolve하기 위해 2026-07-30 생성됨. KR corpus 697 entries (전체의 54.8%) 가 이 theme-file을 인용함.

## 카테고리 분포

| 카테고리 | 인용 수 |
|---|--:|
| greeting | 50+ |
| number | 100+ |
| color | 50+ |
| food | 80+ |
| animal | 50+ |
| basic-response | 50+ |
| misc (dating-culture, family terms, etc.) | 300+ |
| **Total** | **697** |

## 게재 단어 (대표 샘플)

### 인사 (Greetings) — 대표 50+
- 안녕하세요 (annyeonghaseyo) — hello (polite)
- 안녕 (annyeong) — hello (casual)
- 안녕히 가세요 (annyeonghi gaseyo) — goodbye (to person leaving)
- 안녕히 계세요 (annyeonghi gyeseyo) — goodbye (to person staying)
- 안녕히 주무세요 (annyeonghi jumuseyo) — good night
- 잘 가 (jal ga) — bye (casual)
- 잘 자 (jal ja) — good night (casual)
- 안녕히 (annyeonghi) — peacefully
- 처음 뵙겠습니다 (cheoeom boepseumnida) — nice to meet you (formal)
- 만나서 반가워요 (mannaseo bangawoyo) — glad to meet you

### 숫자 (Numbers) — 100+ entries
- 하나 (hana) — one (순 우리말)
- 둘 (dul) — two
- 셋 (set) — three
- 넷 (net) — four
- 다섯 (daseot) — five
- 여섯 (yeoseot) — six
- 일곱 (ilgop) — seven
- 여덟 (yeodeol) — eight
- 아홉 (ahop) — nine
- 열 (yeol) — ten
- 한 (han) — one (Sino-Korean, 한자)
- 이 (i) — two (Sino)
- 삼 (sam) — three (Sino)
- ... (일, 이, 삼, 사, 오, 육, 칠, 팔, 구, 십 + 십의 단위들)

### 색깔 (Colors) — 50+ entries
- 빨강 (ppal gang) — red
- 파랑 (pa rang) — blue
- 노랑 (no rang) — yellow
- 초록 (cho rok) — green
- 보라 (bo ra) — purple
- 분홍 (bun hong) — pink
- 검정 (geom jeong) — black
- 하양 (ha yang) — white
- 주황 (ju hwang) — orange
- 갈색 (gal saek) — brown

### 음식 (Food) — 80+ entries
- 밥 (bap) — rice/meal
- 물 (mul) — water
- 김치 (gim chi) — kimchi
- 불고기 (bul go gi) — bulgogi
- 비빔밥 (bi bim bap) — bibimbap
- 떡볶이 (tteok bokki) — tteokbokki
- 라면 (ra myeon) — ramen
- 김밥 (gim bap) — kimbap
- ... (Korean cuisine staples + basic foods)

### 동물 (Animals) — 50+ entries
- 개 (gae) — dog
- 고양이 (go yang i) — cat
- 새 (sae) — bird
- 물고기 (mul go gi) — fish
- 소 (so) — cow
- 말 (mal) — horse
- 돼지 (dwae ji) — pig
- 양 (yang) — sheep
- 닭 (dak) — chicken
- 토끼 (to kki) — rabbit
- 쥐 (jwi) — mouse
- 호랑이 (ho rang i) — tiger
- 곰 (gom) — bear
- 사자 (sa ja) — lion

### 기본 응답 (Basic Responses)
- 네 (ne) — yes
- 아니요 (a ni yo) — no
- 괜찮아요 (gwaen chan ha yo) — it's okay
- 알겠습니다 (al get seum ni da) — I understand (formal)
- 몰라요 (mol la yo) — I don't know
- 미안합니다 (mi an ham ni da) — I'm sorry (formal)
- 감사합니다 (gam sa ham ni da) — thank you (formal)
- 고마워요 (go ma wo yo) — thank you (casual)

## 왜 aggregator 페이지인가?

다른 언어 (EN/ES) 에는 `basic-vocabulary.md` 가 vocabulary/ 디렉토리에 직접 존재함:
- `Language/wiki/English/vocabulary/basic-vocabulary.md` (88 EN 인용)
- `Language/wiki/Spanish/vocabulary/basic-vocabulary.md` (76 ES 인용)
- KR 에서는 `topik1-starter.md` 가 TOPIK 1 입문 어휘 (32 entries) 를 담당하지만, JP의 basic-vocabulary 같은 aggregator 역할은 없었음.

본 페이지로 그 갭 마감.

## 인제스트 출처

모든 entry는 다음 중 하나의 출처에서 인용:
- **TOPIK 1~2 어휘 목록** (한국어 능력시험)
- **연세 한국어 1~2** 교재
- **Korean for Beginners** (TTMIK — Talk To Me In Korean)
- **Standard Korean Dictionary** (표준국어대사전)

## 게임 통합

`prototype/src/data/kr_corpus.ts` 자동 로드:
- `source: [[basic-vocabulary]]` 인용 entry는 이 페이지의 display/jamo/meaning 필드를 사용
- TOPIK 1 입문 entry는 `topik1-starter.md` 와 자동 cross-reference

## Sources

- `Game/typing_language/raw/kr_words.md` (697 entries)
- `Language/wiki/Korean/vocabulary/topik1-starter.md` (TOPIK 1 cross-reference)
- `Language/wiki/Korean/vocabulary/greetings-vocabulary.md` (greetings cross-reference)
- `Language/wiki/Korean/vocabulary/numbers-vocabulary.md` (numbers cross-reference)
- `Language/wiki/Korean/vocabulary/colors-vocabulary.md` (colors cross-reference)
