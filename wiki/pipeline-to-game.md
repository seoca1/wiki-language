# Content Pipeline: Language → Game

`Language/`는 학습 콘텐츠의 **단일 진실 공급원(single source of truth)** 이고, `Game/typing_language/`는 그 콘텐츠를 게임용으로 큐레이션하여 소비한다. 이 문서는 다운스트림(콘텐츠가 흘러가는 쪽)인 Language 위키 측의 계약이다.

## 원칙

1. **Language는 학습 지식의 원천이다.** 게임은 Language 위키에서 끌어온다.
2. **게임이 필요로 하는 콘텐츠가 Language에 없으면, Language에 먼저 추가한 후 게임으로 반영한다.**
3. **Language는 게임의 존재를 알지만 의존하지 않는다.** Language 위키는 게임 없이도 독립적으로 성장할 수 있다.
4. **모든 게임 코퍼스 항목은 Language 위키 페이지로 인용되어야 한다.** 인용 없는 게임 콘텐츠는 lint에서 결함으로 취급한다.

## 다운스트림 컨슈머

현재 알려진 다운스트림:

| 컨슈머 | 위치 | 소비 대상 | 비고 |
| --- | --- | --- | --- |
| `typing_language` 게임 | `Game/typing_language/` | `wiki/{Language}/vocabulary/`, `expressions/`, `culture/` | 게임용 코퍼스(`raw/{lang}_words.md`)의 출처 |

향후 추가될 수 있는 다운스트림: 다른 게임, 플래시카드 앱, 블로그 자동 생성 등.

## 게임 측이 끌어가는 단위

게임은 다음 단위로 Language 위키를 소비한다:

| 게임 측 항목 | Language 위키 출처 |
| --- | --- |
| 단어 1개 (`display` + `input` + `meaning` + `level` + `category`) | `wiki/{Language}/vocabulary/{theme}.md` 안 `### {word}` 섹션 (테마 파일 안 YAML 부록이 게임 직결 단위) |
| 표현 1개 (숙어·관용구) | `wiki/{Language}/expressions/{theme}.md` 안 `## {expression}` 섹션 (vocabulary 와 동일한 theme-file 컨벤션, 2026-07-10 갱신) |
| 문화 컨텍스트 1건 (스테이지 설명, NPC 대사 등) | `wiki/{Language}/culture/{topic}.md` |
| 난이도 라벨 (CEFR, JLPT, TOPIK 등) | `wiki/{Language}/sources/*.md` 의 출처 메타 |

게임은 Language 위키 페이지의 YAML 부록(`## Pipeline Form (machine-readable)`)에서 다음 필드를 추출한다:

- `display` (표시형) — vocabulary 페이지 안 `### {word}` 섹션의 단어 자체
- `input` (입력형) — 예: 일본어 로마자, 스페인어 원형, 한국어 로마자
- `meaning` (뜻) — 한국어 번역 또는 영어 정의
- `level` (난이도) — vocabulary 페이지의 메타 또는 출처 메타
- `category` (카테고리) — vocabulary 페이지의 태그 또는 분류
- `source` (Language 위키 페이지 인용) — `[[{theme-filename}]]` 단일 anchor (per-word 페이지 미사용 컨벤션과 일치)

## 게임 측 반출 형식

게임은 Language 위키에서 추출한 데이터를 다음 형식으로 큐레이션한다:

```yaml
# Game/typing_language/raw/{lang}_words.md
- id: kr_001
  display: 한국          # Language 위키 표기 그대로
  input: hangug          # 게임 입력 방식(로마자 등)
  meaning: 한국          # 또는 영어 정의
  level: 1               # TOPIK 1~6 또는 Language 정의 등급
  category: country      # Language 위키의 태그
  source: "[[topik1-starter]]"   # Language 위키 theme-file 인용 (필수) — per-word 페이지 미사용 (2026-07-10 컨벤션)
```

`source` 필드는 **반드시** Language 위키 페이지(`[[wikilink]]`)여야 한다. raw 코퍼스 파일 자체에 출처 문장을 함께 적어도 좋다.

## 작업 흐름 (게임이 새 콘텐츠를 요구할 때)

게임 측에서 신규 단어·표현·문화 콘텐츠가 필요할 때:

```
[Game] "한국어 인사말 10개가 필요해"
  ↓
[에이전트] Language/wiki/Korean/vocabulary/ 확인
  ↓ (있으면)
[에이전트] → Game/typing_language/raw/kr_words.md 에 인용과 함께 큐레이션
  ↓ (없으면)
[에이전트] Language/raw/Korean/ 에 출처(교재·기사·원서) 추가
  → Language/wiki/Korean/ 인제스트 (vocabulary 페이지 생성)
  → Game/typing_language/raw/kr_words.md 에 인용과 함께 큐레이션
```

### 단계별 체크리스트

1. **Language 위키 점검**: `wiki/{Language}/vocabulary/`, `expressions/` 에서 필요한 항목 검색
2. **부족하면 Language에 먼저 추가**:
   - `raw/{Language}/` 에 출처 추가 (원본은 절대 수정 금지)
   - 인제스트: vocabulary / expression / culture 페이지 생성
   - `index.md`, `log.md` 갱신
3. **게임 코퍼스로 큐레이션**:
   - `Game/typing_language/raw/{lang}_words.md` 에 항목 추가
   - `source` 필드에 Language 위키 페이지 링크
4. **게임 측 메타 갱신**:
   - `Game/typing_language/wiki/languages/{lang}.md` (언어별 페이지) 갱신
   - `Game/typing_language/index.md`, `log.md` 갱신

## Language 에이전트가 지켜야 할 약속

게임에서 콘텐츠를 끌어갈 때 다음을 보장한다:

- **vocabulary 페이지에 `display`, `meaning`, `level/category` 메타가 명시되어야 한다.**
- **표현·문화 페이지에는 활용 맥락과 예문이 충분히 제공되어야 게임 미션 대사·스테이지 묘사로 가공 가능하다.**
- **인용이 가능한 모든 사실 단언에 원문/출처가 포함되어야 한다** (게임은 이를 다시 인용).

## 동기화 트리거

언제 Language 에이전트가 게임 측을 점검해야 하는가:

| 트리거 | 점검 위치 |
| --- | --- |
| 새 언어 추가 | `Game/typing_language/wiki/languages/{lang}.md` 존재 여부 |
| 난이도 체계 변경 (예: A1~C2 → TOPIK 1~6) | 게임 측 `wiki/languages/{lang}.md` 의 레벨 표 동기화 |
| 대량의 vocabulary 추가 (50+) | 게임 코퍼스도 함께 확장 제안 |

## 양방향 링크

| 언어 | Language 위키 | 게임 언어 페이지 | 게임 코퍼스 |
| --- | --- | --- | --- |
| English | `Language/wiki/English/` | `Game/typing_language/wiki/languages/english.md` | `Game/typing_language/raw/en_words.md` |
| Spanish | `Language/wiki/Spanish/` | `Game/typing_language/wiki/languages/spanish.md` | `Game/typing_language/raw/es_words.md` |
| Japanese | `Language/wiki/Japanese/` | `Game/typing_language/wiki/languages/japanese.md` | `Game/typing_language/raw/jp_words.md` |
| Korean | `Language/wiki/Korean/` | `Game/typing_language/wiki/languages/korean.md` | `Game/typing_language/raw/kr_words.md` |

## 관련 문서

- 게임 측 파이프라인: `Game/typing_language/wiki/corpus-pipeline.md`
- 게임 측 언어 페이지: `Game/typing_language/wiki/languages/*.md`
- 게임 측 원본 코퍼스: `Game/typing_language/raw/*_words.md`
- LLM Wiki 표준: `Language/schema/AGENTS.md`
- **Cross-Language Comparisons**: `Language/wiki/comparative/index` — 5언어 (EN/ES/JP/KR/CH) 비교 페이지 24개. 게임이 다국어 캐릭터를 표현할 때(예: NPC 대사 다국어 버전) 참조 가능. 특히 `politeness-honorifics`, `greetings`, `pronouns-reference` 페이지가 게임 콘텐츠 큐레이션에 직접 활용 가능.