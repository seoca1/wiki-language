# Korean Learning - Activity Log

## [2026-06-23] ingest | nature-vocabulary | Korean nature & weather vocabulary

- 출처: `raw/Korean/nature-vocabulary.md` (자연/날씨 어휘)
- 인제스트 → nature 관련 wiki vocabulary 페이지 추가
- 코퍼스 추가: `Game/typing_language/prototype/src/data/corpus.ts` 에 한국 자연/날씨 단어 60개 추가 (kr_n_001 ~ kr_n_060)
- index.md 갱신: Nature & Weather 섹션 추가
- source: [[nature-vocabulary]]

## [2026-06-23] ingest | animals-vocabulary | Korean animals vocabulary

- 출처: `raw/Korean/animals-vocabulary.md` (동물 어휘)
- 인제스트 → animals 관련 wiki vocabulary 페이지 추가
- 코퍼스 추가: `Game/typing_language/prototype/src/data/corpus.ts` 에 한국 동물 단어 59개 추가 (kr_a_001 ~ kr_a_059)
- index.md 갱신: Animals 섹션 추가
- source: [[animals-vocabulary]]

## [2026-06-23] ingest | clothing-vocabulary | Korean clothing & fashion vocabulary

- 출처: `raw/Korean/clothing-vocabulary.md` (의류/패션 어휘)
- 인제스트 → clothing 관련 wiki vocabulary 페이지 추가
- 코퍼스 추가: `Game/typing_language/prototype/src/data/corpus.ts` 에 한국 의류 단어 42개 추가 (kr_c_001 ~ kr_c_041)
- index.md 갱신: Clothing & Fashion 섹션 추가
- source: [[clothing-vocabulary]]

## [2026-06-23] expand | stage expansion | 140 stages with 4 new themes

- 신규 주제 3개 추가: Nature, Animals, Clothing
- 각 언어별 코퍼스 추가 (EN/ES/JP/KR)
- 각 주제별 Tier 1~4 스테이지 추가
- 전체 스테이지: 69개 → 140개
- 빌드/테스트 통과
- source: [[nature-vocabulary]], [[animals-vocabulary]], [[clothing-vocabulary]]

## [2026-06-23] expand | emotion corpus | Emotions corpus for all languages

- 감정/성격 코퍼스 EN/ES/JP 추가
- 기존 KR 감정 코퍼스 (kr_e_001 ~ kr_e_060) 활용
- 각 언어별 Tier 1~5 스테이지 추가
- source: [[emotions-personality-vocabulary]]

## [2026-06-22] ingest | emotions-personality-vocabulary | Korean emotions & personality vocabulary

- 출처: `raw/Korean/emotions-personality-vocabulary.md` (TOPIK 2-3급 감정/성격 어휘)
- 인제스트 → emotions/personality 관련 wiki vocabulary 페이지 (partial)
- 코퍼스 추가: `Game/typing_language/prototype/src/data/corpus.ts` 에 한국 감정/성격 단어 50개 추가 (kr_e_001 ~ kr_e_060)
- index.md 갱신: Emotions & Personality 섹션 추가
- source: [[emotions-personality-vocabulary]]

## [2026-06-22] ingest | business-vocabulary | Korean business vocabulary

- 출처: `raw/Korean/business-vocabulary.md` (TOPIK 2-3급 비즈니스 어휘)
- 인제스트 → business 관련 wiki vocabulary 페이지 (partial)
- 코퍼스 추가: `Game/typing_language/prototype/src/data/corpus.ts` 에 한국 비즈니스 단어 50개 추가 (kr_b_001 ~ kr_b_063)
- index.md 갱신: Business/Corporate 섹션 추가
- source: [[business-vocabulary]]

## [2026-06-22] ingest | food-vocabulary | Korean food & restaurant vocabulary

- 출처: `raw/Korean/food-vocabulary.md` (TOPIK 1-2급 음식 어휘,国立국어원)
- 인제스트 → food 관련 wiki vocabulary 페이지 (partial)
- 코퍼스 추가: `Game/typing_language/prototype/src/data/corpus.ts` 에 한국 음식 단어 40개 추가 (kr_f_001 ~ kr_f_063)
- index.md 갱신: Food & Restaurant 섹션 추가
- source: [[food-vocabulary]]

## [2026-06-18] ingest | first-travel-japan | First Japan travel experience vocabulary

## [2026-06-18] init | Wiki initialized

- Created directory structure (raw/Korean/, wiki/Korean/ + vocabulary, expressions, culture, sources)
- Set up index.md
- Ready for first source ingest

## [2026-06-18] pipeline | Language ↔ Game 파이프라인 연계

- `Game/typing_language/` 와 다운스트림 파이프라인 연결
- 게임 측 한국어 프로필 골격 작성: `Game/typing_language/wiki/languages/korean.md`
- 게임 측 한국어 코퍼스 골격 작성: `Game/typing_language/raw/kr_words.md` (`source: [[wikilink]]` 인용 패턴)
- 게임 측 입력 방식 ADR 작성: `Game/typing_language/decisions/0009-kr-input.md` (Draft, 사용자 결정 대기)
- 양방향 가이드: `Language/wiki/pipeline-to-game.md`, `Game/typing_language/wiki/corpus-pipeline.md`

## 다음 단계

- ADR-0009 결정 (국립국어원 로마자 표기법 / 발음 변동 매핑 깊이)
- 결정 후 `Language/raw/Korean/` 에 첫 출처(TOPIK 1 단어장 등) 추가
- 인제스트 → `Language/wiki/Korean/vocabulary/` 페이지 시드
- 게임 코퍼스 `Game/typing_language/raw/kr_words.md` 에 인용과 함께 실제 항목 추가

## [2026-06-18] ingest | TOPIK 1 Starter

- 출처: `raw/Korean/topik1-starter.md` (TOPIK 1급 기출 어휘, 국립국어원)
- 인제스트 → vocabulary 페이지 15개 생성 (greetings, numbers 1~5·10, country, food, school, time 등)
- expression 2개 (만나서 반갑습니다, 오늘 날씨가 좋아요)
- `index.md` 갱신
- ADR-0009 Accepted → 옵션 A (로마자 직접 매핑) 채택

## 결정 후 작업

- ✅ `Game/typing_language/prototype/src/input/KoreanHandler.ts` 작성 (JP 핸들러 패턴 동일)
- ✅ `Game/typing_language/prototype/src/data/corpus.ts` KR_WORDS 추가 (15개 + 2개 문장)
- ✅ `Game/typing_language/prototype/src/data/stages.ts` kr_easy_1, kr_easy_2 추가
- ✅ `Game/typing_language/prototype/src/ui/Menu.tsx` 한국어 섹션 추가
- ✅ `Game/typing_language/prototype/src/types.ts` Language union에 'kr' 추가
- ✅ 캐릭터 한복 외형 자동 적용 (CulturalAppearance)