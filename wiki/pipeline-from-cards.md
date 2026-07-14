# Content Pipeline: Card News Archive → Language Wiki

> **Reverse complement** to `pipeline-to-openclaw.md`.
> `.openclaw` 는 Language → OpenClaw forward pipeline 의 source 가 아니지만,
> `.openclaw` 가 **daily exposure 결과로 생성하는 카드뉴스 slot [2]** 는
> Language 위키에 없는 신규 어휘·표현·문화 정보를 담고 있다.
> 이 파이프라인은 그 정보를 Language 위키로 끌어오는 보완 절차다.

---

## §원칙 (Principle)

1. **Language/wiki 가 initiator (pull).** OpenClaw 측에는 어떤 변경도 하지 않는다 (immutable, ADR-0061 §D1 일치).
2. **Card archives 는 read-only source.** `.openclaw/workspace/wiki/card_news/archive/` 의 어떤 파일도 수정·삭제하지 않는다.
3. **slot [2] 만 대상.** 슬롯 [1]/[3]/[4]/[5] 는 tech·finance·lifestyle·reflection 이므로 제외한다.
4. **Genuinely new 만 추출.** Language 위키에 이미 존재하는 어휘는 다시 추가하지 않는다 (anti-feedback-loop).
5. **Source citation 보존.** 추출된 모든 entry 는 출처 카드 날짜 + 슬롯을 명시한다: `Card News YYYY-MM-DD (slot [2])`.
6. **Checkpoint 기반 증분 실행.** 매 실행마다 `last_processed_date` 만 갱신하므로 무한정 늘어나는 목록을 두지 않는다.
7. **Complementary, not competing.** 기존 forward pipeline(`pipeline-to-openclaw.md`) 과 충돌하지 않으며, 게임 코퍼스(`pipeline-to-game.md`) 는 Language 위키 갱신분을 그대로 소비한다.

---

## §카드 식별 (Card Slot [2] Identification)

### Header 패턴

카드 슬롯 [2] 는 다음 패턴으로 식별한다:

```markdown
## 2️⃣ 🇪🇸 {제목}
### {부제}
**Category:** Language / {Spanish|Japanese|Chinese}
**Tags:** #{lang} #{category} #{level} #{topic}
```

언어 식별자(이모지 + Category 라인):

| 언어 | Header 이모지 | Category 패턴 |
| --- | --- | --- |
| 스페인어 (현재) | 🇪🇸 | `Language / Spanish` 또는 `Language / Culture` |
| 일본어 (예정) | 🇯🇵 | `Language / Japanese` |
| 중국어 (예정) | 🇨🇳 | `Language / Chinese` |

### 카드 포맷 진화 — 자동 감지 규칙

| 포맷 | 시기 | Key Concepts 필드 | Practical Tips 필드 | 비고 |
| --- | --- | --- | --- | --- |
| **옛 포맷** | 2026-06-22 ~ 2026-06-30 | ❌ 없음 → `**Vocabulary:**`, `**Expressions:**` 하위 섹션 사용 | `- ☑️ {sentence}` 패턴 동일 | 첫 스페인어 카드 |
| **신 포맷** | 2026-07-01 ~ 현재 | `- **{Term (한글)}:** definition` 불릿 | `- ☑️ *"{sentence}"* — {note}` 패턴 | Key Concepts bullet 도입 |

자동 감지 로직:
1. 카드 본문에서 `**Key Concepts:**` 존재 여부 확인
2. 없으면 → 옛 포맷 파서 (`**Vocabulary:**` + `**Expressions:**` 추출)
3. 있으면 → 신 포맷 파서 (`**Key Concepts:**` + `**Practical Tips:**` 추출)

### Required fields

추출 대상 카드는 다음 필드를 가져야 한다:

- `**Category:** Language / {Lang}` (필수)
- `**Exposure ID:** {type}:{name}` (권장 — 파일 라우팅에 사용)

`Exposure ID` 가 없으면 `Category` 의 보조 분류(`/ Spanish` 다음 단어, 예: `Culture`, `Daily`) 로 라우팅한다.

---

## §추출 규칙 (Extraction Rules)

### 신 포맷 (2026-07-01 ~)

| 카드 섹션 | 추출 대상 | 라우팅 |
| --- | --- | --- |
| `**Key Concepts:**` 의 `- **{Term (한글)}:** definition` | 신규 어휘 entry | `vocab:{category}` → 해당 theme 파일 (없으면 생성) |
| `**Practical Tips:**` 의 `- ☑️ *"{sentence}"* — {note}` | 예문 | 가장 관련 있는 `### {word}` 섹션의 `#### Examples` 하위 |
| `**Main Content:**` 단락 | 문화·맥락 | `culture:{topic}` → `culture/{topic-slug}.md` (없으면 생성) |
| `**Exposure ID:**` 값 | 라우팅 키 | 아래 §Exposure ID 매핑 표 참조 |

### 옛 포맷 (2026-06-22 ~ 2026-06-30)

| 카드 섹션 | 추출 대상 | 라우팅 |
| --- | --- | --- |
| `**Vocabulary:**` 의 `- **{Term} — {Korean}` | 신규 어휘 entry | `lesson:{name}` → category 기반 theme 파일로 fallback 라우팅 |
| `**Expressions:**` 의 `- **{Expression} — {Korean}` | 신규 어휘 entry | 동일 |
| `**Practical Tips:**` | 예문 | 동일 (신 포맷과 동일 처리) |

### Exclusion rules

다음은 **추출하지 않는다**:

- `Exposure ID: lesson:*` — lesson 은 forward pipeline 의 sources/ 영역이므로 추출 대상 아님
- `[[wikilink]]` 가 이미 Language 위키 stem 으로 resolve 되는 항목 — 중복
- 빈 Key Concepts / 빈 Vocabulary 섹션 — 추출할 것이 없음
- 카드 슬롯 [2] 외 모든 슬롯 — slot [1]/[3]/[4]/[5] 제외

---

## §Exposure ID → 타겟 매핑 표 (Deterministic Mapping)

| Exposure ID 패턴 | Target file (Spanish) | Fallback (없으면) |
| --- | --- | --- |
| `vocab:body` | `vocabulary/body-vocabulary.md` | 새로 생성 |
| `vocab:food` | `vocabulary/food-vocabulary.md` | |
| `vocab:family` | `vocabulary/family-vocabulary.md` | |
| `vocab:time` | `vocabulary/time-prepositions-vocabulary.md` | |
| `vocab:travel` | `vocabulary/viajes.md` | |
| `vocab:business` | `vocabulary/business-vocabulary.md` | |
| `vocab:emotion` | `vocabulary/emotions-personality-vocabulary.md` | |
| `vocab:nature` | `vocabulary/nature-vocabulary.md` | |
| `vocab:animal` | `vocabulary/animals-vocabulary.md` | |
| `vocab:clothing` | `vocabulary/clothing-vocabulary.md` | |
| `vocab:daily` | `vocabulary/daily-life-vocabulary.md` | |
| `vocab:adjective` | `vocabulary/adjectives-vocabulary.md` | |
| `vocab:polite` | `vocabulary/polite-expressions-vocabulary.md` | |
| `culture:tango` | `culture/tango-argentino.md` | |
| `culture:{topic}` | `culture/{topic-slug}.md` | 새로 생성 |
| `grammar:{concept}` | `grammar/{concept-slug}.md` | 새로 생성 |
| `lesson:*` | (SKIP — sources/ 영역) | 추출 안 함 |
| (Exposure ID 없음) | Category 보조 분류 기반 | "Culture" → `culture/{topic}.md`, 그 외 → `vocabulary/{category}-vocabulary.md` |

**Fallback 동작**: 매핑 표에 없는 category 면 theme 파일을 새로 만든다 (예: `vocab:transportation` → `vocabulary/transportation-vocabulary.md`). Language/schema/AGENTS.md 의 표준 헤더(`# {Theme} — {설명}`, `**Source:** ...`, `**Theme:**`, `**Level:** ...`) 로 초기화한다.

---

## §중복 제거 (Deduplication)

### 1. Scope: global

추출된 어휘 stem 을 `Language/wiki/Spanish/vocabulary/*.md` 의 **모든 파일**에서 검색한다. 단일 target theme 파일에만 비교하지 않는다 — 한 어휘가 다른 theme 에 이미 존재할 수 있기 때문이다.

### 2. Normalization for comparison only

비교 키만 정규화한다. canonical form 은 액센트를 보존한다.

```python
def normalize_for_dedup(stem: str) -> str:
    """비교 전용 정규화. 원본 stem 은 보존."""
    n = stem.lower()
    # Spanish accents
    n = n.replace('á','a').replace('é','e').replace('í','i')
    n = n.replace('ó','o').replace('ú','u').replace('ü','u')
    n = n.replace('ñ','n')
    # 공백 + 구두점
    n = ' '.join(n.split())
    return n
```

### 3. Accent collision guard

정규화 키는 같지만 원형이 다른 경우(예: `si`(if) vs `sí`(yes))는 다른 단어로 취급한다. 비교 로직:

```python
def is_duplicate(new_stem: str, existing_stems: set[str]) -> bool:
    """원형이 정확히 일치할 때만 중복으로 본다."""
    return new_stem in existing_stems
```

정규화는 키 충돌 방지를 위한 보조 수단일 뿐, 매칭 자체는 원형 정확 일치로 한다.

### 4. Multi-word expressions

여러 단어로 된 표현(예: `dar la vuelta`, `el abrazo`, `tener hambre`)은 **단일 stem**으로 취급한다. 비교 시 공백·구두점 차이로 split 하지 않는다.

### 5. Verbatim definition check (anti-feedback-loop)

카드의 definition 텍스트가 기존 entry 의 `meaning` 과 **verbatim 으로 동일**하면 순환(feedback loop) 으로 간주하고 skip 한다.

```python
def is_verbatim_reprint(card_def: str, existing_meanings: set[str]) -> bool:
    """카드 정의가 기존 entry 와 verbatim 동일하면 skip."""
    norm = ' '.join(card_def.lower().split())
    return norm in existing_meanings
```

체크 대상: 기존 theme 파일의 각 `### {word}` 섹션 안 `Meaning:` 또는 본문 첫 줄 (theme 파일 포맷에 따라 다름).

---

## §형식 변환 (Format Transformation)

### 입력 (카드)

```markdown
**Key Concepts:**
- **Lunfardo (룬파르도):** 부에노스아이레스 항구의 은어
- **Cabeceo (카베세오):** 눈짓으로 신청. 말없이 "출래?"를 던지는 미묘한 아이컨택 규칙
```

### 출력 (Language/wiki vocabulary entry)

```markdown
### lunfardo

룬파르도 — 부에노스아이레스 항구의 은어

**Part of Speech:** sustantivo masculino
**Source:** Card News 2026-07-12 (slot [2]) — [[tango-argentino]]

#### Examples

- (Practical Tips 에서 lunfardo 관련 예문이 있으면 여기에)

---

### cabeceo

카베세오 — 눈짓으로 신청. 말없이 "출래?"를 던지는 미묘한 아이컨택 규칙

**Part of Speech:** sustantivo masculino
**Source:** Card News 2026-07-12 (slot [2]) — [[tango-argentino]]

---
```

### 7-field YAML Appendix

theme 파일의 `## Pipeline Form (machine-readable)` 섹션에 append:

```yaml
- id: es_{theme}_{NNN}
  display: "lunfardo"
  input: "lunfardo"
  meaning: "룬파르도 — 부에노스아이레스 항구의 은어"
  level: "B1"
  category: "{theme}"
  source: "[[{theme-file}]] — Card News 2026-07-12 (slot [2])"
```

### ID 생성 규칙

`{lang}_{theme}_{NNN}` 패턴:
- `{lang}` = `es` (스페인어), `ja` (일본어), `zh` (중국어)
- `{theme}` = theme 파일 stem 또는 category slug (예: `tango`, `body`, `daily_life`)
- `{NNN}` = 대상 theme 파일의 YAML entries 중 가장 큰 숫자 + 1

```python
def next_id(theme_file: Path, lang: str, theme: str) -> str:
    """해당 theme 파일의 YAML 중 가장 큰 ID + 1."""
    pattern = re.compile(rf"id:\s*{lang}_{re.escape(theme)}_(\d+)")
    max_n = 0
    for line in theme_file.read_text().splitlines():
        m = pattern.search(line)
        if m:
            max_n = max(max_n, int(m.group(1)))
    return f"{lang}_{theme}_{max_n + 1:03d}"
```

### Level 추론 규칙

| 어휘 유형 | Level |
| --- | --- |
| 숫자·색깔·신체 부위·가족·기본 명사 | A1 |
| 일반 동사·형용사·일상 표현 | A2 |
| 문화 용어·지역 은어·전통 관련 | A2-B1 |
| 관용구·속어·방언·전문 용어 | B1-B2 |

카드에 명시적 level tag (`#A1`, `#A2-B1` 등) 가 있으면 그 값을 우선한다.

### Practical Tips 예문 배치

Practical Tips 의 `- ☑️ *"{sentence}"* — {note}` 항목은:

1. 예문에 등장하는 스페인어 단어를 stem 화 (예: `"¿Quieres bailar un tango conmigo?"` → `quieres`, `bailar`, `tango`, `conmigo`)
2. 각 stem 중 **이번 카드에서 새로 추출되는 term** 또는 **target theme 의 primary term** 의 `### {word}` 섹션 아래 `#### Examples` 에 추가
3. 예문이 여러 term 에 해당하면 가장 specific 한 term (예: theme 이 `tango` 이면 `tango` > `bailar`) 에 배치

---

## §체크포인트 (Checkpoint)

### 파일 위치

`Language/wiki/Spanish/study-plan/_card_extraction_state.md` (스페인어)
`Language/wiki/Spanish/study-plan/_card_extraction_state_ja.md` (일본어, 추후)
`Language/wiki/Spanish/study-plan/_card_extraction_state_zh.md` (중국어, 추후)

### Frontmatter 스키마

```yaml
---
last_processed_date: YYYY-MM-DD      # 가장 최근에 처리한 카드 날짜
last_processed_filename: YYYY-MM-DD.md # 가장 최근에 처리한 카드 파일명
last_extraction_run: ISO-8601 timestamp
extracted_count:
  vocab_terms: N
  example_sentences: N
  culture_expansions: N
target_card_count: N       # 이번 실행에서 발견한 카드 수
total_extraction_runs: N
errors: []                 # 에러 메시지 목록
---
```

### Idempotency

재실행 시 `last_processed_date >= 카드날짜` 이면 skip. 동일 카드를 두 번 처리하지 않는다.

### 무한정 증가 방지

`processed_cards: [...]` 같은 무한정 늘어나는 목록은 두지 않는다. `last_processed_date` + `last_processed_filename` 만으로 충분하다.

---

## §주기적 운영 (Periodic Operation)

### 수동 실행 절차

```bash
# 1. 현재 상태 확인
cat Language/wiki/Spanish/study-plan/_card_extraction_state.md

# 2. .openclaw 카드 아카이브 immutable 검증용 hash snapshot
mkdir -p .omo/evidence/pre-state
find ~/.openclaw/workspace/wiki/card_news/archive/ -name "*.md" \
    -exec shasum {} \; > .omo/evidence/pre-state/card-archive-hashes.txt

# 3. 추출 실행 (Wave 7 절차)
#    - checkpoint 의 last_processed_date 이후 카드들을 순회
#    - 각 카드에서 slot [2] 추출 → 중복 체크 → 변환 → append
#    - checkpoint 갱신

# 4. immutable 검증 (post-extraction)
find ~/.openclaw/workspace/wiki/card_news/archive/ -name "*.md" \
    -exec shasum {} \; > /tmp/card-archive-hashes-after.txt
diff .omo/evidence/pre-state/card-archive-hashes.txt /tmp/card-archive-hashes-after.txt
# diff 가 비어있으면 immutable 유지 확인
```

### 주기

- **Weekly (default)**: 매주 일요일 실행 — cron `0 9 * * 0` 형태 (`.openclaw` 외부)
- **On-demand**: 사용자가 "카드 추출 실행해줘" 라고 요청할 때
- **Multi-language trigger**: `.openclaw` cron 이 🇯🇵/🇨🇳 카드 생성을 시작하면 즉시 1회 실행 후 weekly 로 전환

### 안전 장치

1. **Pre-hash snapshot** 은 매 실행마다 남긴다 (`.omo/evidence/pre-state/card-archive-hashes-{timestamp}.txt`)
2. **Diff 검증** 은 실행 직후 자동 실행
3. **에러 누적**: 동일 카드에서 3회 연속 파싱 실패 시 `errors: [...]` 에 기록하고 skip (다음 실행에서 재시도 안 함)

---

## §다국어 확장 (Multi-language Readiness)

`.openclaw` cron 이 🇯🇵 (일본어) 또는 🇨🇳 (중국어) 카드 생성을 시작할 때:

1. `Language/wiki/{Ja|Zh}/study-plan/_card_extraction_state_{ja|zh}.md` 생성 (스페인어 템플릿 복제)
2. §Exposure ID 매핑 표를 해당 언어 theme 파일에 맞게 조정
3. Level 추론 규칙을 JLPT / HSK 기준으로 변경
4. 카드 식별 헤더를 `🇯🇵` / `🇨🇳` 로 변경

본 파이프라인의 골격(slot [2] 식별, 중복 제거, 변환, 체크포인트) 은 그대로 유지된다.

---

## §참고 (References)

- ADR-0062 — 본 파이프라인 거버넌스
- ADR-0061 — OpenClaw ↔ Vault Language Wiki Integration (companion ADR)
- `Language/wiki/pipeline-to-openclaw.md` — forward pipeline
- `Language/wiki/pipeline-to-game.md` — Language → 게임 코퍼스
- `Language/schema/AGENTS.md` — vocabulary 페이지 포맷 명세
- `.openclaw/workspace/wiki/card_news/archive/` — read-only 입력 소스