# ADR-0003: Pipeline YAML contract — downstream consumer machine-readable 인터페이스

**상태**: Accepted
**날짜**: 2026-07-29 (effective, 1,259 entries 생성) / 2026-08-08 (ADR 형식화)
**결정자**: 사용자
**우선순위**: P1

## 컨텍스트

Language 위키는 두 다운스트림 컨슈머에게 학습 콘텐츠를 노출한다:

| 다운스트림 | 위치 | 소비 형태 |
|---|---|---|
| `lingotype` 게임 | `Game/lingotype/raw/{lang}_words.md` | vocabulary theme 파일을 게임 코퍼스로 큐레이션, `source: [[wikilink]]` 인용 |
| `.openclaw` workspace | `.openclaw/workspace/wiki/{lang}/_exposure_log.md` | vocabulary + culture 페이지에서 daily-exposure entry 풀 |

2026-07-29 직전 audit 에서 양 컨슈머의 machine-readable contract 가 **대부분 비어 있음** 이 발견되었다:

| 언어 | vocabulary theme 파일 | YAML Pipeline entries 채움률 |
|---|---|---|
| English | 9 | **3/9 (33%)** |
| Spanish | 23 | **4/23 (17%)** ← openclaw primary target |
| Japanese | 9 | **1/9 (11%)** ← openclaw primary target |
| Korean | 13 | 4/13 (31%) |
| Chinese | 5 | **1/5 (20%)** ← openclaw primary target |

결과:
- openclaw 가 Japanese/Spanish/Chinese vocabulary 에서 machine-readable 데이터 추출 불가
- 게임 측 `Game/lingotype/raw/{lang}_words.md` 의 cross-reference 검증 불가 (raw/ 는 정본이지만 wiki YAML 은 reference 표시 역할)
- 신규 vocabulary 추가 시 machine-readable 보장 메커니즘 부재

## 고려한 옵션

### Option 1: YAML 섹션을 수동 작성 (LLM 이 매번 입력) — 거절
- **장점**: 즉시 적용 가능
- **단점**: 작성 누락 빈번, 입력 오류 발생, scale 불가

### Option 2: 별도 데이터 파일 (`wiki/{Lang}/pipeline/{theme}.yaml`) 분리 — 거절
- **장점**: 마크다운 / YAML 관심사 분리
- **단점**: human-readable 와 machine-readable 의 single source-of-truth 가 분리 → drift 발생, LLM Wiki 3계층 패턴 위반

### Option 3: theme 파일 안에 `## Pipeline Form` YAML 섹션 (human + machine 동일 파일) — 채택
- **설명**: theme 파일의 말미에 human-readable 본문 다음 `## Pipeline Form (machine-readable)` 섹션을 둠. 각 `### {word}` 섹션에서 파생된 YAML entry 들을 코드블록으로 보유.
- **장점**:
  - 단일 source-of-truth (human + machine 동일 파일)
  - LLM Wiki 3계층 패턴과 정렬 (raw → wiki → schema)
  - 신규 vocabulary 추가 시 같은 theme 파일에서 양 표현 갱신
  - 코드블록 내 YAML → 컨슈머는 정규식/YAML parser 로 추출
- **단점**:
  - 코드블록 안 YAML syntax 검증 어려움 (사전 lint 필요)
  - theme 파일 사이즈 증가 (보통 +50-100%)

### Option 4: 사전 생성 스크립트 (`tools/generate_yaml.py`) + CI 검증 — 보조 채택
- **설명**: Option 3 의 YAML 섹션을 자동 생성하는 도구 + lint step
- **장점**:
  - 일관성 보장 (entry id 자동, 필드 검증)
  - 신규 vocabulary 추가 후 스크립트 재실행으로 자동 갱신
- **단점**: 도구 유지보수 필요

## 추천

**Option 3 + Option 4: theme 파일에 `## Pipeline Form` 섹션 + 자동 생성 도구.**

근거:
1. LLM Wiki 의 single source-of-truth 원칙 정렬
2. 다운스트림 컨슈머가 정규식/YAML parser 로 직접 추출 가능 (외부 API 의존 없음)
3. 자동 생성 도구가 일관성 + lint 역할

## 사용자 결정

[x] **Option 3 + Option 4: theme 파일 내 YAML 섹션 + 자동 생성 도구** (effective 2026-07-29)

## 결과 (Consequences)

### YAML entry 스키마 (필수 필드)
```yaml
- id: {stable unique identifier, snake_case}
  display: {학습자에게 보여지는 표제어}
  input: {타이핑/입력 시 사용하는 텍스트, 언어별 표기 차이 반영}
  meaning: {한국어 뜻 또는 짧은 정의}
  level: {A1-A2 / JLPT N5-N1 / TOPIK 1-6 / HSK 1-6 / CEFR}
  category: {theme stem (e.g., food-vocabulary, business-vocabulary)}
  source: "[[{theme-filename}]]"   # ADR-0001 theme-file 컨벤션 준수
```

### ID 컨벤션
- 형식: `{lang}_{theme}_{NNN}` (예: `es_food_vocabulary_001`, `jp_food_vocabulary_001`, `zh_body_001`)
- 안정성: theme 파일 내 단어 순서 유지 → ID 가 merge/reorder 시 보존됨
- 신규 vocabulary 는 기존 최대 NNN + 1 로 부여

### Display / Input 필드
- **display**: 학습자에게 보여지는 형태 (예: 스페인어 "carne", 일본어 "肉")
- **input**: 타이핑 게임 등에서 입력 받을 때의 형태 (예: 한자 → 히라가나 변환, 중국어 → pinyin 숫자표기)
- 예외:
  - Chinese `input` 은 숫자 pinyin (`ni3 hao3`) — 가독성 위해 본문은 tone-marked (`nǐ hǎo`)
  - Japanese `input` 은 hiragana 우선 (kanji 입력 시 reading fallback)
  - Spanish `input` 은 `display` 와 동일 (Spanish 는 발음 변화 적음)

### Source 필드 (필수 인용)
- 모든 entry 의 `source` 는 `[[{theme-filename}]]` — theme-file stem (ADR-0001 §컨벤션)
- 컨슈머가 vault-wide stem matching 으로 resolve 가능 (2026-07-22+ lint 도입)
- 절대 path-style (`[[../{Lang}/vocabulary/{theme}]]`) 금지 — vault-wide stem 매칭이 처리 불가

### 파일 위치 표준
```markdown
# {Theme} — {한 줄 설명}

**Source:** [[{source-slug}]]
**Theme:** {Travel & Tourism, Food, ...}
**Level:** ...

{theme 본문}

---

## Pipeline Form (machine-readable)

> Generated for downstream consumers (`Game/lingotype/raw/{lang}_words.md`).
> Schema reference: `wiki/pipeline-to-game.md` L33-39, L92.
> The body above remains the human-readable form and is the source of truth.

```yaml
- { id: es_food_vocabulary_001, display: "carne", input: "carne", meaning: "Meat (animal flesh).", level: "A1", category: "food-vocabulary", source: "[[food-vocabulary]]" }
- { id: es_food_vocabulary_002, display: "pescado", input: "pescado", meaning: "Fish.", level: "A1", category: "food-vocabulary", source: "[[food-vocabulary]]" }
# ...
```
```

### 1,259 entries 생성 (2026-07-29 batch)
| 언어 | theme 파일 | YAML entries |
|---|---|---|
| English | 9 | 111 |
| Spanish | 23 | 276 |
| Japanese | 9 | 267 |
| Korean | 13 | 549 |
| Chinese | 5 | 56 |
| **합계** | **59** | **1,259** |

### 다운스트림 contract
- **게임 (`Game/lingotype/raw/{lang}_words.md`)**: YAML entry 의 `source: [[{theme-stem}]]` 인용 + `display/input/meaning/level/category` 5필드 활용
- **openclaw (`.openclaw/workspace/wiki/{lang}/_exposure_log.md`)**: vocabulary entries + culture 페이지 `## Ejemplos` 섹션 daily-exposure 풀

### 강제되는 결정
- 모든 vocabulary theme 파일은 `## Pipeline Form` 섹션 보유 필수
- 모든 entry 의 `source` 필드는 theme-file stem (ADR-0001 정렬)
- 모든 entry 의 `id` 는 `{lang}_{theme}_{NNN}` 형식

### 향후 결정
- `tools/generate_yaml_pipeline.py` 정식 canonical 화 (현재 /tmp 일회성 스크립트 → 재사용 가능 도구)
- Expression pages 의 machine-readable contract (현재 vocabulary 만 정의 — expressions 는 추가 검토)
- Culture pages 의 5-min readiness 표준 (ADR-0004 §comparative 와 정렬)

## 영향 받는 항목

- `Language/schema/AGENTS.md` L130-141 (Vocabulary 페이지 형식)
- `Language/wiki/pipeline-to-game.md` — 게임 측 consumer contract
- `Language/wiki/pipeline-to-openclaw.md` — openclaw 측 consumer contract
- `Game/lingotype/AGENTS.md` §1.5 — 게임 raw/ 의 source: `[[theme-stem]]` 인용 규약
- `Language/log.md` 2026-07-29 entries (배치 YAML 생성)

## 관련 결정

- ADR-0001 (Theme-file 컨벤션) — `### {word}` 섹션이 YAML entry 의 source-of-truth
- ADR-0002 (5언어 병렬 구조) — 5언어 모두 동일 YAML schema 적용

## 변경 이력

- 2026-07-29: theme 파일 YAML 섹션 보강 + 1,259 entries 생성 (effective)
- 2026-07-29: `pipeline-to-openclaw.md` "Current State" 섹션 추가
- 2026-08-08: ADR 형식화 (배치 governance, batch A)
