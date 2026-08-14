# ADR-0005: Expressions YAML contract — `## {expression}` 머리글에서 machine-readable 인터페이스

**상태**: Accepted
**날짜**: 2026-08-14 (effective)
**결정자**: 사용자
**우선순위**: P1
**관련 ADR**: ADR-0001 (theme-file), ADR-0002 (5언어 병렬), ADR-0003 (vocabulary YAML), ADR-0004 (comparative)

## 컨텍스트

ADR-0003 는 vocabulary theme 파일(`### {word}` 머리글)에 한정된 YAML pipeline 계약을 정의했다.
2026-07-29 batch 에서 1,259 vocabulary entries 가 생성되어 `Game/typing_language/raw/{lang}_words.md` 가
이 contract 를 안정적으로 소비하고 있다.

같은 batch 에서 5개 언어의 표현(idiom·숙어·관용구) 페이지 일부(`wiki/{Lang}/expressions/{theme}.md`)에도
YAML Pipeline Form 섹션이 작성되었으나, **두 가지 일관성 결함** 이 발견되었다:

| 결함 | 사례 | 영향 |
|---|---|---|
| (1) **ID 형식 비일관** | `req_001`, `complaints_001` (Korean expressions) | ADR-0003 의 `{lang}_{theme}_{NNN}` 형식과 불일치 → 컨슈머 파서 분기 필요 |
| (2) **적용 범위 불균형** | 5개 언어 × 21 expression theme = 105 파일 중 **4 파일/언어 = 20 파일만 YAML 보유 (19%)** | 85 파일은 machine-readable 형태 부재 → 표현 콘텐츠가 게임·flashcard 다운스트림으로 흐르지 못함 |

`schema/expression.md` (tier-1: Literal Translation / Meaning / Usage Context / Examples 3+ / Cultural Background / Similar Expressions 2+ / Sources 1+) 가 human 본문 표준이지만,
**downstream machine consumer (typing_language 게임, future SRS/Anki export, flashcard 앱)** 가
요구하는 최소 필드는 vocabulary 와 동일한 7 필드(id/display/input/meaning/level/category/source) 이다.

## 고려한 옵션

### Option 1: Expressions 에는 별도 YAML 스키마 정의 — 거절
- **장점**: expression 의 풍부한 메타(tier-1 7개 필드 + tier-2 4개 필드) 를 모두 노출 가능
- **단점**: vocabulary 와 다운스트림 파서가 분기 → consumer 복잡도 증가, schema fragmentation

### Option 2: Vocabulary 와 동일한 7필드 + 선택 필드(literal, register) — 채택
- **장점**:
  - ADR-0003 vocabulary 와 동일한 downstream contract → 단일 consumer 구현
  - expression 고유 정보(literal 직역, register 격식) 는 옵션으로 첨부 가능
  - 기존 4×5=20 expression YAML 의 6필드(display/input/meaning/level/category/source) 와 호환
- **단점**:
  - 표현의 tier-1 메타 (Usage Context, Pattern, Cultural Background) 는 YAML 에 안 들어감 — human 본문이 source-of-truth
  - 옵션 필드(literal, register) 가 일부 파일만 보유 → consumer 가 optional 처리 필요

### Option 3: 표현은 별도 `wiki/{Lang}/expressions/_pipeline/{theme}.yaml` 분리 — 거절
- **장점**: human / machine 관심사 분리
- **단점**: ADR-0003 (Option 3 거절) 의 single source-of-truth 원칙 위반, drift 발생 가능

## 추천

**Option 2: vocabulary 와 동일한 7필드 필수 + 옵션 필드(literal, register) 두 개.**

근거:
1. ADR-0003 의 single source-of-truth 원칙 정렬 (theme 파일 안에 YAML)
2. downstream consumer (typing_language 게임 등) 가 vocabulary / expression 구분 없이 단일 파서로 처리 가능
3. 기존 작성된 20 expression YAML 파일은 ID 형식만 마이그레이션하면 그대로 호환

## 사용자 결정

[x] **Option 2: vocabulary 와 동일한 7필드 + 옵션 literal/register** (effective 2026-08-14)

## 결과 (Consequences)

### YAML entry 스키마

**Required 필드 (7개, ADR-0003 동일)**:
```yaml
- id: kr_requests_001                # {lang}_{theme}_{NNN} 형식
  display: "~해 주세요"               # 학습자에게 보이는 표현 (target language)
  input: "~hae juseyo"               # 타이핑 입력 형태
  meaning: "Please do ~ (polite casual)"  # 한국어 뜻 또는 짧은 정의
  level: "A2"                        # A1-C1 / CEFR / JLPT / TOPIK / HSK
  category: "requests"               # theme stem
  source: "[[requests]]"             # ADR-0003 정렬 — bare stem wikilink
```

**Optional 필드 (2개, expression 전용)**:
```yaml
  literal: "주세요 (= please give)"  # 직역 — cross-language 비교 시 유용
  register: "polite-casual"          # formal / semi-formal / casual / slang / literary
```

옵션 필드는 human 본문에서 명확히 추출 가능한 경우에만 포함. 누락되어도 validate 통과.

### ID 컨벤션

- 형식: `{lang}_{theme}_{NNN}` (예: `kr_requests_001`, `es_daily_life_005`)
- 기존 비일관 ID (예: `req_001`, `complaints_001`) 는 본 ADR 의 tool extension 으로 자동 마이그레이션
- 안정성: theme 파일 내 `## {expression}` 순서 유지 → ID merge/reorder 시 보존

### Heading 파싱 규칙

| 콘텐츠 종류 | 머리글 깊이 | 파싱 도구 | 파일 위치 |
|---|---|---|---|
| Vocabulary | `### {word}` (H3) | `generate_yaml_pipeline.py --content-type vocabulary` (default) | `wiki/{Lang}/vocabulary/*.md` |
| Expression | `## {expression}` (H2) | `generate_yaml_pipeline.py --content-type expressions` | `wiki/{Lang}/expressions/*.md` |

### Display / Input 필드 — 언어별 규칙 (ADR-0003 정렬)

| 언어 | display | input |
|---|---|---|
| English | `"How are you?"` | 동일 (대부분) |
| Spanish | `"¿Cómo estás?"` | 동일 (발음 변화 적음) |
| Japanese | `"ありがとうございます"` | `"arigatō gozaimasu"` (히라가나 우선) |
| Korean | `"~해 주세요"` | `"~hae juseyo"` (로마자) |
| Chinese | `"你好吗?"` | `"ni3 hao3 ma?"` (numbered pinyin, 본문은 tone marks) |

### Source 필드 (필수 인용)

모든 entry 의 `source` 는 `[[{theme-filename}]]` — ADR-0001 / ADR-0003 정렬.
컨슈머가 vault-wide stem matching 으로 resolve.

### 파일 위치 표준

```markdown
# {Theme} — {한 줄 설명}

> **Theme:** {Daily Life / Romance & Relationships / ...}
> **Level:** A1-B2 (idioms)

{theme 본문 — tier-1 필드 포함}

---

## Pipeline Form (machine-readable)

> Generated for downstream consumers (`Game/typing_language/raw/{lang}_words.md`).
> Schema reference: ADR-0005 + `wiki/pipeline-to-game.md`.
> The body above remains the human-readable form and is the source of truth.

```yaml
- { id: kr_requests_001, display: "~해 주세요", input: "~hae juseyo", meaning: "Please do ~ (polite casual)", level: "A2", category: "requests", source: "[[requests]]" }
# ...
```
```

### 강제되는 결정

- 모든 expression theme 파일은 `## Pipeline Form` 섹션 보유 필수 (vocabulary 와 동일한 lint 강제)
- 모든 entry 의 `source` 필드는 theme-file stem (ADR-0001 정렬)
- 모든 entry 의 `id` 는 `{lang}_{theme}_{NNN}` 형식 (기존 4-letter prefix 사용 금지)
- 옵션 필드(literal, register) 는 human 본문에 근거가 있을 때만 포함

### 도구 변경

`tools/generate_yaml_pipeline.py` 확장:
- `--content-type {vocabulary|expressions|all}` (default: vocabulary, 하위호환)
- expressions 모드: `wiki/{Lang}/expressions/*.md` 스캔 + `## {expression}` (H2) 파싱
- ID 자동 생성: `{lang}_{theme}_{NNN}` (기존 short-prefix 마이그레이션 지원)
- 의미(meaning) 자동 추출: H2 섹션 안의 `**Meaning:**` / `**의미:**` / `**Definition:**` 라인 매칭

## 적용 계획

| 단계 | 범위 | 상태 |
|---|---|---|
| Pilot | Korean (21 파일: 4 migrate + 17 generate) | **2026-08-14 진행** |
| Rollout | EN / ES / JP / ZH (84 파일: 80 generate + 16 migrate) | 다음 세션 |

PILOT 의 검증 통과 후 ROLLOUT 진행.

## 영향 받는 항목

- `Language/schema/AGENTS.md` L155-200 (Expression 페이지 형식) — `## Pipeline Form` 섹션 예시 추가 (PILOT 후)
- `Language/tools/generate_yaml_pipeline.py` — `--content-type` 추가
- `Language/wiki/pipeline-to-game.md` L29 — expressions 항목 machine-readable contract 명시 (PILOT 후)
- `Game/typing_language/raw/{lang}_expressions.md` — 신규 (typing_language 측 ROLLOUT 후)
- `Language/log.md` — 2026-08-14 batch entries

## 관련 결정

- ADR-0001 (Theme-file 컨벤션) — `## {expression}` 머리글이 YAML entry 의 source-of-truth
- ADR-0002 (5언어 병렬 구조) — 5언어 모두 동일 YAML schema 적용
- ADR-0003 (vocabulary YAML contract) — 본 ADR 의 직접 모티브
- ADR-0004 (comparative scope) — comparative/ 페이지의 cross-reference 는 본 ADR 의 영향을 받지 않음 (별도 schema)

## 변경 이력

- 2026-08-14: ADR 작성 (effective), 7필드 + 옵션 2필드, H2 파싱, {lang}_{theme}_{NNN} ID 마이그레이션 결정