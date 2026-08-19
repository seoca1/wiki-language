# Content Pipeline: Language → OpenClaw Foreign Wiki

> **Last updated**: 2026-07-29 (Grammar pages count correction: Spanish grammar/ = 5 language-specific, plus 1 cross-language verb-conjugation-patterns.md in wiki/grammar/)

`Language/`는 학습 콘텐츠의 **단일 진실 공급원(single source of truth)** 이고, `.openclaw/workspace/wiki/{lang}/`은 그 콘텐츠를 일상 노출(daily exposure) 단위로 끌어와 독자가 매일 짧게 만나는 외래 위키로 운영된다. 동시에 `.openclaw` 산출물은 외부 발행(Notion / Hugo) 으로 흘러가지만, **외부 발행은 본 파이프라인의 사정권이 아니다**. 이 문서는 다운스트림인 Language 위키 측의 계약이다.

## 원칙

1. **Language는 학습 지식의 원천이다.** `.openclaw` 는 Language 위키에서 끌어온다.
2. **.openclaw 가 필요로 하는 콘텐츠가 Language에 없으면, Language에 먼저 추가한 후 .openclaw 로 끌어간다.**
3. **Language는 .openclaw 의 존재를 알지만 의존하지 않는다.** Language 위키는 .openclaw 없이도 독립적으로 성장할 수 있다.
4. **.openclaw 노출 단위(daily exposure row)는 Language 위키 페이지로 인용되어야 한다.** 인용 없는 노출 항목은 lint에서 결함으로 취급한다.
5. **.openclaw 원본(`.openclaw/workspace/wiki/{lang}/`)은 외부 발행 대상이라 변형 불가(immutable).** 실수가 발견되면 .openclaw 측을 직접 고치지 않고, Language 쪽을 먼저 고친 뒤 다시 끌어온다.

## 다운스트림 컨슈머

현재 알려진 다운스트림:

| 컨슈머 | 위치 | 소비 대상 | 비고 |
| --- | --- | --- | --- |
| `.openclaw-foreign-wiki` | `.openclaw/workspace/wiki/{lang}/` | `Language/wiki/{Language}/vocabulary/`, `expressions/`, `culture/`, `grammar/` | 일상 노출 풀(`_exposure_log.md`) 의 출처. 외부 발행(Notion / Hugo) 으로의 변환은 본 파이프라인 사정권 밖 |

`.openclaw` 의 일상 노출(daily exposure)은 학습자가 매일 짧게(예: 5분) Language 위키의 한 항목을 다시 만나게 하는 풀(pool) 기반 시스템이다. 풀 한 줄(row) 이 Language 위키 한 페이지(혹은 그 일부) 에 매핑된다.

## OpenClaw 측이 끌어가는 단위

`.openclaw` 는 다음 단위로 Language 위키를 소비한다:

| `.openclaw` 측 항목 | Language 위키 출처 |
| --- | --- |
| 일일 노출 1행 (`_exposure_log.md` Pool row) | `wiki/{Language}/vocabulary/{theme}.md` 안 `### {word}` 섹션, 또는 `wiki/{Language}/culture/{topic}.md` |
| 레슨 참조 1건 | `wiki/{Language}/grammar/{concept}.md` 안 문법 개념 페이지 |
| 어휘 테마 1건 | `wiki/{Language}/vocabulary/{theme}.md` 의 테마 단위 페이지 |
| 문화 페이지 1건 | `wiki/{Language}/culture/{topic}.md` |
| 문법 개념 1건 | `wiki/{Language}/grammar/{concept}.md` |

`.openclaw` 는 Language 위키 페이지의 YAML 부록(`## Pipeline Form (machine-readable)`)에서 다음 필드를 추출한다:

- `display` (표시형) — vocabulary 페이지 안 `### {word}` 섹션의 단어 자체
- `meaning` (뜻) — 한국어 번역 또는 영어 정의
- `level` (난이도) — CEFR, JLPT, TOPIK, HSK 등
- `category` (카테고리) — vocabulary 페이지의 태그 또는 분류
- `source` (Language 위키 페이지 인용) — `[[{theme-filename}]]` 단일 anchor

일상 노출 풀(`_exposure_log.md`) 에는 위에 더해 노출 시점의 메타(`date`, `duration_min`, `note`) 가 함께 기록된다.

## OpenClaw 측 노출 단위 형식

`.openclaw` 는 Language 위키에서 추출한 데이터를 다음 형식으로 큐레이션한다:

```yaml
# .openclaw/workspace/wiki/spanish/_exposure_log.md (Pool row)
- date: 2026-07-14
  source: "[[viajes]]"      # vault anchor — Language/wiki/Spanish/vocabulary/viajes.md (theme-file, per-word 페이지 미사용 컨벤션)
  duration_min: 5
  note: "Daily exposure — viaje vocab"
```

풀 한 행이 Language 위키 한 페이지에 매핑되는 것이 이상적이다. 풀 전체는 `language: spanish` 같은 헤더로 묶고, 각 행은 단일 `source` anchor 만 갖는다. `.openclaw` 가 외부 발행(Notion / Hugo) 으로 변환할 때는 이 풀을 그대로 직렬화(serialization) 한다. **Language 측을 수정하지 않고 .openclaw 풀만 갱신하는 것은 허용되지 않는다** — Language 가 정본이므로, 풀의 의미가 어긋났다면 Language 부터 고친다.

## 작업 흐름 (.openclaw 가 새 콘텐츠를 요구할 때)

`.openclaw` 측에서 신규 노출·레슨·문화 콘텐츠가 필요할 때:

```
[.openclaw] "스페인어 viaje 테마 일일 노출이 필요해"
  ↓
[에이전트] Language/wiki/Spanish/vocabulary/viajes.md 확인
  ↓ (있으면)
[에이전트] → .openclaw/workspace/wiki/spanish/_exposure_log.md 에 인용과 함께 풀 행 추가
  ↓ (없으면)
[에이전트] Language/raw/Spanish/ 에 출처(교재·기사·원서) 추가
  → Language/wiki/Spanish/ 인제스트 (vocabulary 페이지 생성)
  → .openclaw/workspace/wiki/spanish/_exposure_log.md 에 인용과 함께 풀 행 추가
```

### 단계별 체크리스트

1. **Language 위키 점검**: `wiki/{Language}/vocabulary/`, `expressions/`, `culture/`, `grammar/` 에서 필요한 항목 검색
2. **부족하면 Language에 먼저 추가**:
   - `raw/{Language}/` 에 출처 추가 (원본은 절대 수정 금지)
   - 인제스트: vocabulary / expression / culture / grammar 페이지 생성
   - `index.md`, `log.md` 갱신
3. **.openclaw 노출 풀로 큐레이션**:
   - `.openclaw/workspace/wiki/{lang}/_exposure_log.md` 에 풀 행 추가
   - `source` 필드에 Language 위키 페이지 anchor (`[[wikilink]]`)
   - `date`, `duration_min`, `note` 등 노출 시점 메타 명시
4. **.openclaw 측 메타 갱신**:
   - `.openclaw/workspace/wiki/{lang}/index.md` 갱신
   - `.openclaw/workspace/log.md` 갱신 (선택)

## Language 에이전트가 지켜야 할 약속

`.openclaw` 에서 콘텐츠를 끌어갈 때 다음을 보장한다:

- **vocabulary 페이지에 `display`, `meaning`, `level`, `category` 메타가 명시되어야 한다.** 풀 행의 `source` 가 가리키는 anchor 가 식별 가능해야 한다.
- **문화·문법 페이지에는 짧은 요약(1~2문장) + 예문이 제공되어야 일일 노출 5분 안에 학습자가 다시 만날 수 있다.** 풀 한 행은 그 짧은 요약을 가리킬 뿐, 전체 페이지를 매번 읽게 해선 안 된다.
- **인용이 가능한 모든 사실 단언에 원문/출처가 포함되어야 한다** (.openclaw 가 이를 다시 인용하여 외부 발행한다).
- **노출 빈도가 높은 vocabulary / culture 페이지는 우선순위가 높다.** .openclaw 풀은 결국 "Language 위키에서 자주 다시 만나고 싶은 페이지" 의 큐레이션이다.

## 동기화 트리거

언제 Language 에이전트가 `.openclaw` 측 풀을 점검해야 하는가:

| 트리거 | 점검 위치 |
| --- | --- |
| 새 언어 추가 (예: Chinese 신규) | `.openclaw/workspace/wiki/{lang}/` 디렉토리 및 `_exposure_log.md` 존재 여부 |
| 어휘 대량 추가 (50+ 단어) | 해당 언어의 `_exposure_log.md` 풀 확장 제안 (테마 1~2개 신규 row 추가) |
| 테마 재구성 (`vocabulary/{theme}.md` 분할·합병) | 기존 풀의 `source` anchor 가 깨질 수 있으므로 풀 재매핑 |
| 외부 발행 변경 (Notion → Hugo 등) | 본 파이프라인과 무관 — `.openclaw` 자체 정책 |

## 양방향 링크

| 언어 | Language 위키 | `.openclaw` 위키 | `.openclaw` daily exposure |
| --- | --- | --- | --- |
| English | `Language/wiki/English/` | (해당 없음) | (해당 없음) |
| Spanish | `Language/wiki/Spanish/` | `.openclaw/workspace/wiki/spanish/` | `.openclaw/workspace/wiki/spanish/_exposure_log.md` |
| Japanese | `Language/wiki/Japanese/` | `.openclaw/workspace/wiki/japanese/` | `.openclaw/workspace/wiki/japanese/_exposure_log.md` |
| Korean | `Language/wiki/Korean/` | (해당 없음) | (해당 없음) |
| Chinese | `Language/wiki/Chinese/` (신규) | `.openclaw/workspace/wiki/chinese/` | `.openclaw/workspace/wiki/chinese/_exposure_log.md` |

English 과 Korean 은 일상 노출 대상이 아니므로 `.openclaw` 위키를 두지 않는다. Chinese 는 신규로 Language 위키부터 만든 뒤 `.openclaw` 위키를 함께 연다. 다른 언어가 노출 대상으로 추가될 때 이 표에 행을 더한다.

## Current State (2026-07-29)

Language wiki 가 openclaw contract 보완 상태 (post-language-expansion):

### Vocabulary theme files (YAML pipeline entries)

`.openclaw` 가 machine-readable 로 추출 가능한 `## Pipeline Form (machine-readable)` YAML section 보유:

| Language | Files | YAML entries | Source |
| --- | --- | --- | --- |
| English | 9 | 111 | [Oxford 3000 + OEC] |
| Spanish | 23 | 276 | [es_words.md](https://github.com/seoca1/lingotype) + comparative research |
| Japanese | 9 | 267 | [jp_words.md] + JLPT reference |
| Korean | 13 | 549 | [kr_words.md] + TOPIK reference |
| Chinese | 5 | 56 | [Chinese HSK 1-2 curriculum] |
| **Total** | **59** | **1,259** | — |

### Culture pages (5-min daily exposure readiness)

`.openclaw` 가 5-min daily exposure 풀에 포함할 수 있는 culture 페이지 (summary + examples + 2+ citations + 200+ words 충족):

| Language | Ready | Total | Examples section |
| --- | --- | --- | --- |
| English | 5/5 | 5 | `## Examples` |
| Spanish | 14/14 | 14 | `## Ejemplos` |
| Japanese | 5/5 | 5 | `## 例文` (reibん) |
| Korean | 4/4 | 4 | `## 예문` (yesmun) |
| Chinese | 4/4 | 4 | `## 示例` (shili) |
| **Total** | **32/32** | **32** | — |

### Grammar pages

`.openclaw` 가 레슨 참조로 끌어갈 수 있는 grammar 페이지:

| Language | Files | Status |
| --- | --- | --- |
| English | 0 | **Gap** — raw/ 에 grammar source 부재, 신규 raw ingest 후 작성 필요 |
| Spanish | 5 | ✓ (gustar, preposiciones, presente, preterito, reflexivos) — language-specific grammar |
| Japanese | 0 | **Gap** — raw/ 에 grammar source 부재 |
| Korean | 0 | **Gap** — raw/ 에 grammar source 부재 |
| Chinese | 2 | ✓ |

추가: `wiki/grammar/verb-conjugation-patterns.md` (cross-language: **6 pages**, ES verb paradigm + comparative cross-references) — 1 file 추가 가능.

Grammar 페이지가 0 인 언어 (EN/JA/KO) 는 `.openclaw` 가 grammar/ 디렉토리에서 콘텐츠를 끌어갈 수 없으므로, 새 raw source ingest 시 grammar 페이지 동시 생성을 우선순위로 한다.

### Cross-cutting comparative pages

5개 언어 비교 페이지 (`wiki/comparative/`) — `.openclaw` 가 cross-language 풀에 활용 가능:

| Page | Language pairs |
| --- | --- |
| [[tradiciones-veraniegas]] | ES ↔ JP ↔ KR ↔ EN ↔ ZH (siesta vs. 昼寝 vs. 낮잠 vs. power nap) |
| [[lengua-espanola-hispanohablantes]] | ES regional dialects |
| [[mood-systems]] | indicative vs. subjunctive across 5 langs |
| [[tense-aspect-systems]] | tense/aspect comparison |
| [[lunch-and-rest-patterns]] | midday meal/rest across 5 cultures |
| [[diatopic-variation-patterns]] | regional dialect patterns across 5 langs |

## 관련 문서

- 게임 측 파이프라인: `Language/wiki/pipeline-to-game.md`
- `.openclaw` 측 작업 규약: `.openclaw/workspace/AGENTS.md`
- `.openclaw` 언어별 위키: `.openclaw/workspace/wiki/{lang}/`
- `.openclaw` 일상 노출 풀: `.openclaw/workspace/wiki/{lang}/_exposure_log.md`
- LLM Wiki 표준: `Language/schema/AGENTS.md`
- Cross-cutting comparative: `Language/wiki/comparative/index.md`
