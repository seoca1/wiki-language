---
source: official-curriculum
type: raw-aggregation
language: German
created: 2026-08-14
---

# German — Raw Sources (Phase 16 seed)

법률 고지: 본 파일은 위키의 출처 추적용 메타데이터일 뿐, 본문 컨텐츠를 포함하지 않습니다.
본 디렉토리의 항목들은 위키 작성/큐레이션을 위한 참고 자료입니다.

## Phase 16 seed attribution

독일어 위키는 Phase 16 (German language scaffold)에서 처음 인제스트됩니다.
출처는 다음과 같이 분류합니다.

### Tier 1 — 공식 커리큘럼 (Goethe-Zertifikat A1 / Start Deutsch 1 어휘 목록)

- 출처: Goethe-Institut — Start Deutsch 1 / A1 wordlist (공공 도메인 reference list).
- 인제스트 범위: 인사, 숫자, 색상, 가족, 음식, 기본 동사, 관사 (der / die / das).
- 위키 인제스트 위치: `wiki/German/vocabulary/basic-vocabulary.md`.

### Tier 2 — 일용어 어휘

- 출처: Langenscheidt Grundwortschatz Deutsch (aktuelle Ausgabe) — basic lexical coverage (citations only, no copy).
- 인제스트 범위: 카페·식당·쇼핑·일상 동사.
- 위키 인제스트 위치: `wiki/German/vocabulary/daily-life-vocabulary.md`, `food-vocabulary.md`.

### Tier 3 — 음식 / 비즈니스 어휘

- 출처: DWDS (Digitales Wörterbuch der deutschen Sprache) — Berlin-Brandenburgische Akademie der Wissenschaften, 공공 reference.
- 인제스트 범위: 음식 카테고리, 비즈니스 이메일 어휘.
- 위키 인제스트 위치: `wiki/German/vocabulary/food-vocabulary.md`, `business-vocabulary.md`.

### Tier 4 — 여행 어휘

- 출처: Deutsche Zentrale für Tourismus (DZT) — public tourism phrasebook.
- 위키 인제스트 위치: `wiki/German/vocabulary/travel-vocabulary.md`.

## 독일어 입력 방식 메모

독일어 입력 시 특이 사항:

- 움라우트(`ä`, `ö`, `ü`)와 `ß` (Eszett / scharfes S) 처리 — DIN 5007 규약으로 ASCII 폴백 가능 (`ae`, `oe`, `ue`, `ss`)
- 합성어 (Komposita): 여러 명사를 결합하여 새 단어를 만듦 (Donaudampfschifffahrtsgesellschaftskapitän 등)
- 관사의 성 (Genus): der (m), die (f), das (n) — 모든 명사가 세 가지 성별 중 하나에 속함

## 게임 코드 인용 컨벤션

`Game/typing_language/prototype/src/data/corpus.ts`의 DE 항목들은
`source: '[테마 stem]'` 필드로 위의 theme-file을 인용합니다.
wikilink target은 theme-file stem 이어야 합니다 (per-word 페이지 없음, §3.1.1 규약).

## 다음 단계 (위키 확장 시)

- Goethe-Zertifikat A2/B1 어휘 추가
- 독일 문학 발췌 (Goethe, Schiller, Kafka, Brecht)
- 독일 영화/TV 인용 (Tatort, Dark)
- 분리동사 (trennbare Verben) 문법 노트
- 격 변화표 (Deklination) / 동사 변화표 (Konjugation) grammar 페이지
