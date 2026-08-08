# ADR-0002: 5개 언어 병렬 구조 + Chinese raw 예외

**상태**: Accepted
**날짜**: 2026-07-13 (Chinese 추가) / 2026-08-08 (ADR 형식화)
**결정자**: 사용자
**우선순위**: P1

## 컨텍스트

Language 위키는 **5개 언어** (English, Spanish, Japanese, Korean, Chinese) 를 동등 우선순위로 유지한다. 2026-07-13 batch ingest 로 Chinese 가 5번째 언어로 추가되었다.

5개 언어 wiki 의 디렉토리 구조는 다음을 만족해야 한다:
1. **병렬성** — 모든 언어가 동일 디렉토리 layout (`vocabulary/`, `expressions/`, `culture/`, `sources/`, `study-plan/`, `grammar/`) 보유
2. **독립성** — 한 언어 wiki 가 다른 언어 wiki 에 의존하지 않음 (다운스트림 컨슈머가 어느 언어든 단독 사용 가능)
3. **일관성** — 페이지 형식 표준 (`schema/AGENTS.md` §3) 이 5개 언어 모두에 동일 적용
4. **language-specific special considerations** — 각 언어의 고유 특성 (한자, 한자어, 조사, 성조, 양사 등) 만 보조 schema 에 반영

### Chinese raw 예외

다른 4개 언어 (`English, Spanish, Japanese, Korean`) 는 `raw/{Language}/` 에 source-of-truth 자료가 `.md` 로 보존된다:

```
[교재·기사·원서 source]  →  Language/raw/{Lang}/{topic}.md  →  wiki/{Lang}/...
```

반면 **Chinese** 는 다음의 이유로 raw 단계가 부재한다 (옵션 채택은 후술):
- 2026-07-13 batch ingest 시 web article / HSK 교재 / lesson platform 발췌 형태로 진행
- copyright 민감 (특히 web article) — 원문 보존보다 wiki 내 citation 으로 처리
- 출처 URL 이 source-summary 페이지에 자체 기록 (각 페이지가 `**Type:**`, `**Date Added:**`, `**Language Level:**` 메타 보유)

## 고려한 옵션 (raw 단계 정책)

### Option A: 그대로 유지 (raw 단계 부재를 policy exception 으로 인정) — 채택
- **장점**:
  - wiki 가 self-contained, source citation 명확
  - 추가 작업 0
- **단점**:
  - raw 단계 audit 시 Chinese 만 빈 셀
  - 5언어 raw/ 대칭성 깨짐

### Option B: `.openclaw/` 에서 raw 추출
- **설명**: source-summary 의 upstream 원문/URL 채워서 `Language/raw/Chinese/{topic}.md` 신규 작성
- **장점**: 5언어 대칭 회복, raw 단계 citation 강화
- **단점**:
  - 시간/조사 비용 큼
  - 정확도 검증 필요 (URL drift, site 구조 변경 등)
  - copyright 검토 필요

### Option C: 최소 placeholder
- **설명**: 본 README 만 두되 source-summary 페이지에 "원본 보존 위치: .openclaw/..." 주석 추가
- **장점**: 간단, traceability 확보
- **단점**: raw 단계 자체는 여전히 부재

## 추천

**5언어 병렬 구조 유지 + raw 단계에 한해 Option A (그대로 유지) 채택.**

근거:
1. Language 위키의 단일 진실 공급원 (Single Source of Truth) 은 wiki 자체 — raw 는 그 위계의 한 단계일 뿐
2. Chinese source-summary 페이지 8개 모두 `## Sources` 섹션 보유 (2026-07-28 batch) — wiki 내 traceability 확보
3. Option B 는 정확도 검증 비용이 막대하나 5언어 대칭성 회복 이득은 비교적 작음
4. 향후 Chinese raw 보존 정책 결정 시 Option B 또는 C 로 전환 검토 가능 (아래 §향후 결정)

## 사용자 결정

[x] **5언어 병렬 구조 + Chinese raw 예외 Option A** (effective 2026-07-13, ADR 형식화 2026-08-08)

## 결과 (Consequences)

### 채택된 5언어 디렉토리 layout
```
wiki/{English,Spanish,Japanese,Korean,Chinese}/
├── index.md                 # master index + Cross-Language Comparisons section
├── log.md                   # activity log
├── vocabulary/              # theme files (ADR-0001)
├── expressions/             # theme files (ADR-0001)
├── culture/                 # per-topic pages
├── sources/                 # source summaries
├── study-plan/              # 개인 학습 계획 (per-language 독립)
└── grammar/                 # EN/JA/KO 는 향후 보강 (현재 ZH 2 + ES 5)
```

### Chinese source-summary 페이지 표준
모든 Chinese `wiki/Chinese/sources/*.md` 페이지는 다음을 보유:
- `**Type:**` (lesson / culture / literature / web article)
- `**Date Added:**` (YYYY-MM-DD)
- `**Language Level:**` (HSK 1-6)
- `## Sources` 섹션 (원본 URL / 출처, 2026-07-28 batch 로 추가됨)
- 영문 summary + Key Takeaways

### Language-specific 필드 (보조 schema)
| 언어 | 보조 schema 파일 | 특수 필드 |
|---|---|---|
| Korean | `schema/vocabulary.md` | 한자 (Sino-Korean), speech level (해체/해요체/합쇼체), irregular conjugation (ㄷ/ㅂ/ㅅ/ㅎ/르), 조사 |
| Japanese | `schema/vocabulary.md` | furigana, kanji 분리, politeness level (casual/polite/honorific) |
| Spanish | `schema/vocabulary.md` | regional variant (ES vs LATAM), gender/plural, tú/usted, conjugation |
| English | `schema/vocabulary.md` | learner mistakes, phrasal verbs, register (formal/informal/slang) |
| Chinese | `schema/vocabulary.md` | tone (mā/má/mǎ/mà/ma), 简体/번체, 量词, HSK 1-6, character vs word, pinyin (mā vs ma1) |

### 강제되는 결정
- 신규 언어 추가 시 `wiki/{NewLang}/` layout + `raw/{NewLang}/` 가 본 ADR 의 5언어 구조와 정렬 필수
- Chinese raw 는 현행 Option A 유지 — 변경 시 신규 ADR 작성
- Per-language `index.md` 는 Cross-Language Comparisons 섹션으로 `wiki/comparative/*` 와 양방향 연결 (ADR-0004)

### 향후 결정
- Chinese raw 정책 (Option B 또는 C) 전환 — 정확도 검증 후 별도 ADR
- EN/JA/KO `wiki/{Lang}/grammar/` 디렉토리 보강 (현재 부재)
- Language-specific 보조 schema 통합 (현재 `vocabulary.md` 만 — `expression.md`, `culture.md` 의 per-language 필드 보강)

### Chinese raw 정책 Option B/C 전환 조건 (2026-08-08 추가)

**Option B (`.openclaw/` 추출) 의 사전 조건:**
- `.openclaw/workspace/wiki/chinese/` 디렉토리에 원본 source 보존 확인
- 2026-08-08 vault audit 결과: `.openclaw/workspace/wiki/chinese/` 디렉토리 자체가 부재 (Option B 실행 불가)
- 향후 `.openclaw/` 에 Chinese raw 가 보존될 경우 Option B 검토 가능

**Option C (placeholder + pointer):**
- source-summary 페이지에 "원본 보존 위치: .openclaw/..." 주석 추가
- 단, 2026-08-08 현재 pointer 대상 부재 → 주석 추가만 가능 (raw 단계 부재는 동일)

**현재 결론 (2026-08-08):**
- Option A 유지 (그대로)
- 변경 조건: `.openclaw/workspace/wiki/chinese/` 가 향후 보존되거나, Chinese raw 재수집 시 별도 ADR 로 B 또는 C 채택
- Chinese raw 부재는 정책 예외 (policy exception) 로 인정되며, ADR-0002 immutable 범위 외

## 영향 받는 항목

- `Language/schema/AGENTS.md` §1 (Architecture), §2 (Special Considerations per language)
- `Language/raw/Chinese/README.md` — Option A 상태 명시
- 모든 per-language `wiki/{Lang}/index.md` — Cross-Language Comparisons 섹션
- `Language/log.md` 2026-07-13 entry (Chinese 추가), 2026-07-28 (## Sources 추가)

## 관련 결정

- ADR-0001 (Theme-file 컨벤션) — 모든 5언어 vocabulary/expressions 가 동일 패턴 적용
- ADR-0003 (Pipeline YAML contract) — 5언어 모두 YAML entries 보유
- ADR-0004 (comparative wiki scope) — per-language 와 comparative 의 분리 원칙

## 변경 이력

- 2026-07-13: Chinese 가 5번째 언어로 추가, raw 단계 부재 (Option A 적용)
- 2026-07-28: 모든 Chinese source-summary 페이지에 `## Sources` 섹션 추가 (traceability)
- 2026-08-08: ADR 형식화 (배치 governance, batch A)
