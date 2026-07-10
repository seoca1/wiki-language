# 학습자료와 Language Wiki 출처 연관성 / Content Lineage Map

> 이 문서는 각 언어 학습 자료의 출처와 게임 코퍼스로의 흐름을 추적한다.
> **Raw Source → Wiki Page → Game Corpus** 파이프라인을 시각화한다.

---

## Overview / 개요

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                          CONTENT PIPELINE                                     │
│                                                                              │
│  ┌─────────────┐     ┌─────────────────┐     ┌──────────────────────────┐   │
│  │  Raw Source │ ──▶ │  Wiki Ingest    │ ──▶ │  Game Corpus (corpus.ts) │   │
│  │  (출처 원문)  │     │  (인제스트)       │     │  (게임용 코퍼스)          │   │
│  └─────────────┘     └─────────────────┘     └──────────────────────────┘   │
│         │                    │                            │                 │
│         ▼                    ▼                            ▼                 │
│  - 원서/교재/기사     - vocabulary/           - prototype/src/data/       │
│  - 출처 명시          - expressions/          - corpus.ts                 │
│  - 인용 포맷:         - culture/              - stages.ts                │
│    > **출처**: ...    - index.md 갱신                                    │
│                       - log.md 기록                                      │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Japanese / 日本語

### Raw Sources (Language/raw/Japanese/)

| 파일명 | 주제 | 출처 | 인제스트 날짜 |
|--------|------|------|---------------|
| `first-travel-korea.md` | 한국 여행 (일본인 시점) | 일본인 여행자의 한국 경험 노트 | 2026-06-18 |
| `travel-basics-jp.md` | 일본어 여행 기초 | JLPT N5, 일본어 학습 교재 | 2026-06-18 |
| `dating-romance-jp.md` | 연애/로맨스 | 恋愛会話・デート・告白 | 2026-06-19 |
| `food-vocabulary-jp.md` | 음식/레스토랑 | JLPT N4-N5, 음식 교재 | 2026-06-23 ✅新規 |
| `business-vocabulary-jp.md` | 비즈니스 | JLPT N3-N4, 비즈니스 교재 | 2026-06-23 ✅新規 |
| `emotions-personality-vocabulary-jp.md` | 감정/성격 | JLPT N4-N5 감정 어휘 | 2026-06-23 ✅新規 |
| `nature-vocabulary-jp.md` | 자연/날씨 | JLPT N4-N5 자연 어휘 | 2026-06-23 ✅新規 |
| `animals-vocabulary-jp.md` | 동물 | JLPT N4-N5 동물 어휘 | 2026-06-23 ✅新規 |
| `clothing-vocabulary-jp.md` | 의류/패션 | JLPT N4-N5 의류 어휘 | 2026-06-23 ✅新規 |

### Wiki Ingest (Language/wiki/Japanese/)

| Wiki 섹션 | 해당 Raw 파일 | vocabulary/ 항목 수 | expressions/ 항목 수 |
|-----------|---------------|--------------------|--------------------|
| Travel (첫 여행 경험) | `first-travel-korea.md` | ~42 | ~1 |
| Romance/Dating (연애 테마) | `dating-romance-jp.md` | 16 | 6 |
| Food (음식) | `food-vocabulary-jp.md` | 30+ (partial) | 0 |
| Business (비즈니스) | `business-vocabulary-jp.md` | 28+ (partial) | 0 |
| Emotions (감정) | `emotions-personality-vocabulary-jp.md` | ~43 | 0 |
| Nature (자연) | `nature-vocabulary-jp.md` | 40+ (partial) | 0 |
| Animals (동물) | `animals-vocabulary-jp.md` | 37+ (partial) | 0 |
| Clothing (의복) | `clothing-vocabulary-jp.md` | 30+ (partial) | 0 |

### Game Corpus Mapping (prototype/src/data/corpus.ts)

| 코퍼스 카테고리 | 출처 Wiki 페이지 | 코퍼스 Entry 수 | 비고 |
|----------------|----------------|----------------|------|
| `travel` | `wiki/Japanese/vocabulary/*` | ~42 | `first-travel-korea.md` |
| `romance` | `wiki/Japanese/vocabulary/名前, 綺麗, etc.` | 16 | `dating-romance-jp.md` |
| `food` | `wiki/Japanese/vocabulary/肉, 野菜, etc.` | 25+ | ✅ raw 추가됨 |
| `business` | `wiki/Japanese/vocabulary/会議, メール, etc.` | 28+ | ✅ raw 추가됨 |
| `emotion` | `wiki/Japanese/vocabulary/嬉しい, 寂しい, etc.` | 59 | ✅ raw 추가됨 |
| `nature` | `wiki/Japanese/vocabulary/太陽, 山, etc.` | 60 | ✅ raw 추가됨 |
| `animals` | `wiki/Japanese/vocabulary/犬, 猫, etc.` | 59 | ✅ raw 추가됨 |
| `clothing` | `wiki/Japanese/vocabulary/シャツ, 靴