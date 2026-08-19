---
source: official-curriculum
type: raw-aggregation
language: French
created: 2026-08-14
---

# French — Raw Sources (Phase 15 seed)

법률 고지: 본 파일은 위키의 출처 추적용 메타데이터일 뿐, 본문 컨텐츠를 포함하지 않습니다.
본 디렉토리의 항목들은 위키 작성/큐레이션을 위한 참고 자료입니다.

## Phase 15 seed attribution

프랑스어 위키는 Phase 15 (French language scaffold)에서 처음 인제스트됩니다.
출처는 다음과 같이 분류합니다.

### Tier 1 — 공식 커리큘럼 (DELF A1 / A2 어휘 목록)

- 출처: France Éducation International — DELF A1/A2 wordlist (공공 도메인 reference list).
- 인제스트 범위: 인사, 숫자, 색상, 가족, 음식, 기본 동사.
- 위키 인제스트 위치: `wiki/French/vocabulary/basic-vocabulary.md`.

### Tier 2 — 일용어 / 음식 어휘

- 출처: Le Robert Micro (6e édition, 2021) — basic lexical coverage (citations only, no copy).
- 인제스트 범위: 카페/여행/음식 일상 어휘.
- 위키 인제스트 위치: `wiki/French/vocabulary/daily-life-vocabulary.md`, `food-vocabulary.md`.

### Tier 3 — 음식 / 비즈니스 어휘

- 출처: CNRTL (Centre National de Ressources Textuelles et Lexicales) — citations only.
- 인제스트 범위: 음식 카테고리, 비즈니스 이메일 어휘.
- 위키 인제스트 위치: `wiki/French/vocabulary/food-vocabulary.md`, `business-vocabulary.md`.

### Tier 4 — 여행 어휘

- 출처: Office du Tourisme de Paris — public tourism phrasebook.
- 위키 인제스트 위치: `wiki/French/vocabulary/travel-vocabulary.md`.

## 게임 코드 인용 컨벤션

`Game/lingotype/prototype/src/data/corpus.ts`의 FR 항목들은
`source: '[테마 stem]'` 필드로 위의 theme-file을 인용합니다.
wikilink target은 theme-file stem 이어야 합니다 (per-word 페이지 없음, §3.1.1 규약).

## 다음 단계 (위키 확장 시)

- DELF B1/B2 어휘 추가
- 프랑스 문학 발췌 (Camus, Saint-Exupéry)
- 프랑스 영화 인용 (Le Fabuleux Destin d'Amélie Poulain, etc.)
