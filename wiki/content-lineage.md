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
| `romance` | `wiki/Japanese/vocabulary/[[名前]], [[綺麗]], etc.` | 16 | `dating-romance-jp.md` |
| `food` | `wiki/Japanese/vocabulary/[[肉]], [[野菜]], etc.` | 25+ | ✅ raw 추가됨 |
| `business` | `wiki/Japanese/vocabulary/[[会議]], [[メール]], etc.` | 28+ | ✅ raw 추가됨 |
| `emotion` | `wiki/Japanese/vocabulary/[[嬉しい]], [[寂しい]], etc.` | 59 | ✅ raw 추가됨 |
| `nature` | `wiki/Japanese/vocabulary/[[太陽]], [[山]], etc.` | 60 | ✅ raw 추가됨 |
| `animals` | `wiki/Japanese/vocabulary/[[犬]], [[猫]], etc.` | 59 | ✅ raw 추가됨 |
| `clothing` | `wiki/Japanese/vocabulary/[[シャツ]], [[靴]], etc.` | 42 | ✅ raw 추가됨 |

### ⚠️ Gap: Wiki vs Game Corpus 불일치

**문제**: 일부 코퍼스 항목이 Wiki vocabulary 페이지 없이 Game에 존재함

| 카테고리 | Wiki vocabulary 있음? | Game corpus 있음? | 조치 필요 |
|---------|---------------------|------------------|----------|
| food | ❌ 없음 (raw 파일만) | ✅ 25 entries | Wiki vocabulary 추가 필요 |
| business | ❌ 없음 (raw 파일만) | ✅ 28 entries | Wiki vocabulary 추가 필요 |
| emotion | ❌ 없음 | ✅ 59 entries | Raw + Wiki + 인제스트 필요 |
| nature | ❌ 없음 | ✅ 60 entries | Raw + Wiki + 인제스트 필요 |
| animals | ❌ 없음 | ✅ 59 entries | Raw + Wiki + 인제스트 필요 |
| clothing | ❌ 없음 | ✅ 42 entries | Raw + Wiki + 인제스트 필요 |

---

## Korean / 한국어

### Raw Sources (Language/raw/Korean/)

| 파일명 | 주제 | 출처 | 인제스트 날짜 |
|--------|------|------|---------------|
| `topik1-starter.md` | TOPIK 1 기초 | 국립국어원, TOPIK 1-2급 어휘 | 2026-06-18 |
| `travel-basics-kr.md` | 한국 여행 기초 | 한국 여행 시나리오 | 2026-06-18 |
| `first-travel-japan.md` | 일본인眼中的韩国旅行 | 日本人の韓国旅行 note | 2026-06-18 |
| `dating-romance-kr.md` | 연애/로맨스 | 한국 드라마/영화 참고 | 2026-06-19 |
| `food-vocabulary.md` | 음식 어휘 | 국립국어원, TOPIK 2-3급 | 2026-06-22 |
| `business-vocabulary.md` | 비즈니스 | 국립국어원, TOPIK 2-3급 | 2026-06-22 |
| `emotions-personality-vocabulary.md` | 감정/성격 | 국립국어원, TOPIK 2-3급 | 2026-06-22 |
| `nature-vocabulary.md` | 자연/날씨 | 국립국어원, TOPIK N4-N5 | 2026-06-23 ✅新規 |
| `animals-vocabulary.md` | 동물 | 국립국어원, TOPIK N4-N5 | 2026-06-23 ✅新規 |
| `clothing-vocabulary.md` | 의류/패션 | 국립국어원, TOPIK N4-N5 | 2026-06-23 ✅新規 |

### Wiki Ingest (Language/wiki/Korean/)

| Wiki 섹션 | 해당 Raw 파일 | vocabulary/ 항목 수 |
|-----------|---------------|-------------------|
| Travel (여행) | `travel-basics-kr.md`, `first-travel-japan.md` | ~42 |
| Romance (로맨스) | `dating-romance-kr.md` | ~20 |
| Food (음식) | `food-vocabulary.md` | 51 entries |
| Business (비즈니스) | `business-vocabulary.md` | 45 entries |
| Emotions (감정/성격) | `emotions-personality-vocabulary.md` | 41 entries |
| Nature (자연) | `nature-vocabulary.md` | 39 entries ✅新規 |
| Animals (동물) | `animals-vocabulary.md` | 37 entries ✅新規 |
| Clothing (의류) | `clothing-vocabulary.md` | 33 entries ✅新規 |

### Game Corpus Mapping (prototype/src/data/corpus.ts)

| 코퍼스 카테고리 | 출처 Wiki 페이지 | 코퍼스 Entry 수 | 상태 |
|----------------|----------------|----------------|------|
| `basic` | `wiki/Korean/vocabulary/*` | - | 위키와 동기화됨 |
| `travel` | `wiki/Korean/vocabulary/*` | ~42 | 위키와 동기화됨 |
| `romance` | `wiki/Korean/vocabulary/*` | ~20 | 위키와 동기화됨 |
| `food` | `wiki/Korean/vocabulary/*` | 51 | 위키와 동기화됨 |
| `business` | `wiki/Korean/vocabulary/*` | 45 | 위키와 동기화됨 |
| `emotion` | `wiki/Korean/vocabulary/*` | 41 | 위키와 동기화됨 |
| `nature` | `wiki/Korean/vocabulary/*` | 39 | ✅ raw+wiki 추가됨 |
| `animals` | `wiki/Korean/vocabulary/*` | 37 | ✅ raw+wiki 추가됨 |
| `clothing` | `wiki/Korean/vocabulary/*` | 33 | ✅ raw+wiki 추가됨 |

---

## Spanish / Español

### Raw Sources (Language/raw/Spanish/)

| 파일명 | 주제 | 출처 | 인제스트 날짜 |
|--------|------|------|---------------|
| `first-travel-spain.md` | 스페인 여행 | 스페인 여행 시나리오 | 2026-06-18 |
| `el-ahogado-mas-hermoso-del-mundo.md` | 가르마르케르 단편 | 문학 원문 | 2026-06-16 |
| `como-agua-para-chocolate-cap1.md` | 라몬의 소설 | 문학/요리 단원 | 2026-06-16 |
| `notes-in-spanish-listening-log.md` | 듣기 로그 | 스페인어 청취 학습 | 2026-06-16 |
| `notes-in-spanish-planes-de-verano.md` | 여름 계획 회화 | B1-B2 회화 자료 | 2026-06-16 |
| `dating-romance-es.md` | 연애/로맨스 | Aula Internacional, Sueña, DELE | 2026-06-19 |
| `food-vocabulary-es.md` | 음식/레스토랑 | ESL 음식 어휘 | 2026-06-23 ✅新規 |
| `business-vocabulary-es.md` | 비즈니스 | DELE 비즈니스 어휘 | 2026-06-23 ✅新規 |
| `emotions-personality-vocabulary-es.md` | 감정/성격 | DELE 감정 어휘 | 2026-06-23 ✅新規 |
| `nature-vocabulary-es.md` | 자연/날씨 | DELE 자연 어휘 | 2026-06-23 ✅新規 |
| `animals-vocabulary-es.md` | 동물 | DELE 동물 어휘 | 2026-06-23 ✅新規 |
| `clothing-vocabulary-es.md` | 의류/패션 | DELE 의류 어휘 | 2026-06-23 ✅新規 |

### Wiki Ingest (Language/wiki/Spanish/)

| Wiki 섹션 | 해당 Raw 파일 | vocabulary/ 수 | culture/ 수 |
|-----------|---------------|---------------|------------|
| Travel | `first-travel-spain.md` | ~42 | - |
| Romance | `dating-romance-es.md` | 20 | 1 |
| Literary Sources | `el-ahogado...`, `como-agua...` | 8+12=20 | 4 |
| Listening Notes | `notes-in-spanish-listening-log.md` | 8 | 2 |
| Food | `food-vocabulary-es.md` | 30+ | - |
| Business | `business-vocabulary-es.md` | 43+ | - |
| Emotions | `emotions-personality-vocabulary-es.md` | 43+ | - |
| Nature | `nature-vocabulary-es.md` | 40+ | - |
| Animals | `animals-vocabulary-es.md` | 37+ | - |
| Clothing | `clothing-vocabulary-es.md` | 30+ | - |

### Game Corpus Mapping (prototype/src/data/corpus.ts)

| 코퍼스 카테고리 | 출처 Wiki 페이지 | 코퍼스 Entry 수 | 비고 |
|----------------|----------------|----------------|------|
| `travel` | `wiki/Spanish/vocabulary/*` | ~42 | |
| `romance` | `wiki/Spanish/vocabulary/*` | 20 | |
| `food` | `wiki/Spanish/vocabulary/*` | 42+ | ✅ raw 추가됨 |
| `business` | `wiki/Spanish/vocabulary/*` | 28+ | ✅ raw 추가됨 |
| `emotion` | `wiki/Spanish/vocabulary/*` | 60+ | ✅ raw 추가됨 |
| `nature` | `wiki/Spanish/vocabulary/*` | 60+ | ✅ raw 추가됨 |
| `animals` | `wiki/Spanish/vocabulary/*` | 60+ | ✅ raw 추가됨 |
| `clothing` | `wiki/Spanish/vocabulary/*` | 42+ | ✅ raw 추가됨 |

---

## English / English

### Raw Sources (Language/raw/English/)

| 파일명 | 주제 | 출처 | 인제스트 날짜 |
|--------|------|------|---------------|
| `travel-basics.md` | 여행 기초 | ESL 학습 자료 | 2026-06-18 |
| `first-travel-japan.md` | 일본 여행 (영어 화자) | 일본 여행 시나리오 | 2026-06-19 |
| `dating-romance.md` | 연애/로맨스 | 영어권 데이트 문화 | 2026-06-19 |
| `food-vocabulary.md` | 음식/레스토랑 | ESL 음식 어휘 | 2026-06-23 ✅新規 |
| `business-vocabulary.md` | 비즈니스 | TOEIC 비즈니스 어휘 | 2026-06-23 ✅新規 |
| `emotions-personality-vocabulary.md` | 감정/성격 | ESL 감정 어휘 | 2026-06-23 ✅新規 |
| `nature-vocabulary.md` | 자연/날씨 | ESL 자연 어휘 | 2026-06-23 ✅新規 |
| `animals-vocabulary.md` | 동물 | ESL 동물 어휘 | 2026-06-23 ✅新規 |
| `clothing-vocabulary.md` | 의류/패션 | ESL 의류 어휘 | 2026-06-23 ✅新規 |

### Wiki Ingest (Language/wiki/English/)

| Wiki 섹션 | 해당 Raw 파일 | vocabulary/ 항목 수 |
|-----------|---------------|-------------------|
| Travel | `travel-basics.md`, `first-travel-japan.md` | ~47 |
| Romance | `dating-romance.md` | 20 |
| Food | `food-vocabulary.md` | 25+ |
| Business | `business-vocabulary.md` | 28+ |
| Emotions | `emotions-personality-vocabulary.md` | 60+ |
| Nature | `nature-vocabulary.md` | 60+ |
| Animals | `animals-vocabulary.md` | 60+ |
| Clothing | `clothing-vocabulary.md` | 42+ |

### Game Corpus Mapping (prototype/src/data/corpus.ts)

| 코퍼스 카테고리 | 출처 Wiki 페이지 | 코퍼스 Entry 수 | 비고 |
|----------------|----------------|----------------|------|
| `travel` | `wiki/English/vocabulary/*` | ~47 | |
| `romance` | `wiki/English/vocabulary/*` | 20 | |
| `food` | `wiki/English/vocabulary/*` | 25+ | ✅ raw 추가됨 |
| `business` | `wiki/English/vocabulary/*` | 28+ | ✅ raw 추가됨 |
| `emotion` | `wiki/English/vocabulary/*` | 60+ | ✅ raw 추가됨 |
| `nature` | `wiki/English/vocabulary/*` | 60+ | ✅ raw 추가됨 |
| `animals` | `wiki/English/vocabulary/*` | 60+ | ✅ raw 추가됨 |
| `clothing` | `wiki/English/vocabulary/*` | 42+ | ✅ raw 추가됨 |

---

## ⚠️ 누락된 Wiki Vocabulary 페이지 (Japanese 기준)

Game 코퍼스에 있는 항목 중 Wiki vocabulary 페이지 상태:

### Food Category (25 entries)
✅ Raw `food-vocabulary-jp.md` 추가됨
✅ Wiki vocabulary 페이지 40+ pages 생성됨

### Business Category (28 entries)
✅ Raw `business-vocabulary-jp.md` 추가됨
✅ Wiki vocabulary 페이지 43 pages 생성됨

### Emotions Category (59 entries)
✅ Raw `emotions-personality-vocabulary-jp.md` 추가됨
✅ Wiki vocabulary 페이지 37 pages 생성됨

### Nature Category (60 entries)
✅ Raw `nature-vocabulary-jp.md` 추가됨
✅ Wiki vocabulary 페이지 35 pages 생성됨

### Animals Category (59 entries)
✅ Raw `animals-vocabulary-jp.md` 추가됨
✅ Wiki vocabulary 페이지 35 pages 생성됨

### Clothing Category (42 entries)
✅ Raw `clothing-vocabulary-jp.md` 추가됨
✅ Wiki vocabulary 페이지 27 pages 생성됨

---

##Lint Rule / 인용 규칙

AGENTS.md 규칙:
> **`raw/{lang}_words.md` 의 모든 항목은 `source: [[...]]` 필드로 Language 위키 페이지를 인용해야 한다.**

**현재 상태 (2026-06-23)**:
- corpus.ts: JP 223 entries, EN 164 entries, ES 71 entries → 개별 위키 페이지 참조
- KR: 296 entries → topic-level 유지 (한글↔로마자 매칭 문제)
- EN/ES wiki: 235개 stub 페이지 생성됨

**위키 Topic Pages 추가 (2026-06-23)**:
- JP: food-vocabulary.md, business-vocabulary.md, emotions-personality-vocabulary.md, nature-vocabulary.md, animals-vocabulary.md, clothing-vocabulary.md
- EN: food-vocabulary.md, business-vocabulary.md, emotions-personality-vocabulary.md, nature-vocabulary.md, animals-vocabulary.md, clothing-vocabulary.md
- ES: food-vocabulary.md, business-vocabulary.md, emotions-personality-vocabulary.md, nature-vocabulary.md, animals-vocabulary.md, clothing-vocabulary.md

---

## 다음 단계 / Next Steps

### 완료 ✅
1. **JP Raw Sources 추가**: 모든 주제용 raw 파일 추가
2. **JP Wiki Ingest**: vocabulary 페이지 180+ 생성
3. **JP index.md**: 히라가나 병기 추가 완료
4. **JP log.md 갱신**: 인제스트 활동 로그 기록 완료
5. **EN/ES Raw Sources 추가**: 모든 주제용 raw 파일 추가
6. **Source 필드 추가**: corpus.ts 엔트리에 `source` 필드 추가
7. **위키 Topic Pages 추가**: JP/EN/ES 모든 topic-level 위키 페이지 생성
8. **WordEntry.type.ts**: `source?: string` 필드 추가
9. **KR Raw Sources 추가**: nature, animals, clothing raw 파일 추가
10. **개별 Source 참조 (2026-06-23)**: JP/EN/ES corpus source를 topic-level에서 개별 page-level로 변경

### 남은 작업 ⚠️
1. **세부 위키 페이지 완성**: EN/ES stub 페이지들을 실제 컨텐츠로 채우기
2. **Language wiki git 추적**: `git init` 후 커밋 (현재 위키는 git 관리 안됨)

