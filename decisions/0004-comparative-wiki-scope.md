# ADR-0004: comparative/ 위키 스코프 — cross-language 비교 페이지 통합 정책

**상태**: Accepted
**날짜**: 2026-07-19 (comparative 신규, 28+ 페이지) / 2026-08-04 (35+ 페이지 확장) / 2026-08-08 (ADR 형식화)
**결정자**: 사용자
**우선순위**: P2

## 컨텍스트

Language 위키는 5개 언어 (EN/ES/JA/KO/ZH) 가 **독립적인 wiki** 로 운영된다 (ADR-0002). 그러나 학습자는 종종 cross-language 비교를 원한다:

- "5개 언어에서 politeness 어떻게 표현하나?"
- "한국어 한자어와 일본어 漢語の 대응 관계는?"
- "스페인 subjuntivo 와 한국어 -(으)면 의 관계는?"

이런 cross-cutting 주제는 다음을 만족해야 한다:
1. **5개 언어 동시 비교** — 한 언어에 종속되지 않음
2. **per-language 위키 와 양방향 연결** — 단방향이 아닌 양방향 backreference
3. **재사용 가능** — 같은 주제를 단일 페이지로 통합 (5개 페이지 중복 방지)
4. **신규 cross-cutting 주제 추가 시 위치 결정 명확**

2026-07-19 부터 `wiki/comparative/` 디렉토리를 신설하여 cross-language 비교 페이지를 통합했다. 2026-08-04 batch 로 23 페이지 추가되어 현재 44 페이지 보유.

## 고려한 옵션

### Option 1: 5개 언어 wiki 에 동시 cross-language 페이지 생성 (예: `wiki/Korean/comparative/politeness.md` + 동등 4개) — 거절
- **장점**: per-language 위키 와 단일 디렉토리
- **단점**:
  - 5개 언어 × cross-cutting 주제 = 페이지 폭증 (44 × 5 = 220 페이지)
  - 동일 내용을 5번 작성 → 동기화 부담 막대
  - 신규 cross-cutting 추가 시 5개 wiki 동시 갱신 필요
  - 백링크 분산 → graph view 가 cross-cutting 발견 어려움

### Option 2: cross-language 통합 위키 (`wiki/comparative/`) 단일 디렉토리 — 채택
- **장점**:
  - 44 페이지 단일 위치 → cross-cutting 페이지 응집
  - 동일 주제 1회 작성 → 동기화 부담 0
  - 5개 언어 wiki 모두에서 inbound link 1개로 discover 가능
  - graph view 가 comparative 를 cross-language 허브로 시각화
- **단점**:
  - per-language 위키 와 분리 → 디렉토리 추가
  - inbound link 명시적 추가 필요 (orphan 방지, 2026-07-28 batch 에서 처리)

### Option 3: cross-language page 를 per-language 위키 의 단일 페이지 (e.g., `wiki/Korean/comparative/politeness.md`) 에 배치 — 부분 채택
- **장점**: per-language 별 자기 cross-reference 가독성
- **단점**: 5개 위키 동시 작성 부담은 Option 1 과 동일 (다만 stem 이 다름)
- **검토**: comparative 단일 + per-language reference 가 더 가벼움

### Option 4: cross-language 페이지 폐기, 사용자 prompt 시 synthesis 생성 — 거절
- **장점**: 페이지 0
- **단점**: synthesis 재계산 비용, cross-language 발견성 0, LLM Wiki compounding 원칙 위반

## 추천

**Option 2: cross-language 통합 위키 `wiki/comparative/` 단일 디렉토리 + 양방향 reference.**

근거:
1. LLM Wiki compounding 원칙: 1회 작성, 영구 참조, 재사용 가능
2. 5개 언어 wiki 의 Cross-Language Comparisons 섹션이 양방향 backreference 역할
3. 신규 cross-cutting 추가 시 위치 결정 명확 (comparative/ 에 1페이지)

## 사용자 결정

[x] **Option 2: comparative/ 통합 + per-language 양방향 reference** (effective 2026-07-19)

## 결과 (Consequences)

### comparative/ 디렉토리 layout
```
wiki/comparative/
├── index.md                       # master navigation hub
├── log.md                         # comparative 추가/변경 이력
├── master-cheatsheet.md           # 5개 언어 1-page quick reference
├── comparative-template.md        # 신규 페이지 작성 템플릿
├── FINAL_STATUS.md                # status doc (meta)
└── {topic}.md                     # cross-language 비교 페이지 (44개)
```

### 6 카테고리 (페이지 분류)
1. **Core Linguistic Systems** — politeness-honorifics, greetings, numbers-counters, pronouns-reference, negation, mood-systems, tense-aspect-systems
2. **Situational / Thematic** — travel (tour-guide), food-dining, business-email, dating-romance, shopping, health-body, time, transportation, weather-seasons
3. **Cultural Concepts** — untranslatables, cultural-values, gestures-body-language, idioms-proverbs, slang-colloquial, holidays-celebrations
4. **Learning Strategy** — writing systems (자음/모음/한자/히라가나/병음), pronunciation-challenges, grammar-difficulty-map, learning-resources, confusion-hotspots
5. **Modern / Contemporary** — tech-internet, literature-media, family-kinship, education-student-life, emotions
6. **Reference** — README, log, comparative-template, master-cheatsheet, FINAL_STATUS

### Inclusion criteria (신규 페이지 추가 기준)
comparative/ 에 페이지를 추가하는 경우 **다음 중 하나 이상** 만족:
- 2개 이상 언어에 동일/유사한 개념이 존재 (예: politeness 는 5언어 모두 존재)
- 한 언어에 untranslatable 개념이 있어 다른 언어의 대응 표현 조사 필요
- 5개 언어 동시 학습자에게 cross-reference 가 학습 흐름에 도움

### 양방향 reference 규약
- **comparative/ 페이지**: `wiki/{Lang}/vocabulary/{theme}` 또는 `wiki/{Lang}/culture/{topic}` 로 outbound link 보유
- **per-language `index.md`**: `## Cross-Language Comparisons` 섹션에 relevant comparative 페이지 stem 들을 wikilink 로 명시
- **per-language `culture/{topic}.md`**: 가능하면 comparative/ 페이지로 outbound link (예: Spanish `siesta-tradicion-verano` → `comparative/lunch-and-rest-patterns`)

### Per-language index.md 표준 섹션
```markdown
## Cross-Language Comparisons

- [[comparative-page-1]] — 주제 설명
- [[comparative-page-2]] — 주제 설명
- [[master-cheatsheet]] — 5개 언어 1-page reference
```

### Orphan 방지 정책
- comparative/ 의 모든 페이지는 **최소 1개 inbound link** 보유 필수 (per-language index.md 또는 다른 comparative 페이지)
- 신규 페이지 추가 시 `wiki/comparative/index.md` "Last updated" 갱신
- 주기적 lint (`audit_vault.py` orphan check) 로 검증

### 강제되는 결정
- 신규 cross-cutting 페이지는 반드시 `comparative/` 에 배치 — per-language 위키 에 cross-language 페이지 생성 금지
- 모든 per-language `index.md` 는 Cross-Language Comparisons 섹션 보유
- comparative/ 페이지는 최소 2개 언어 outbound link 보유 권장

### 향후 결정
- comparative/ 페이지 카탈로그 자동 동기화 도구 (`comparative/ 가 추가되면 모든 per-language index.md 의 Cross-Language Comparisons 자동 업데이트` 검토)
- 다국어 comparative 페이지 (현재 영어만 — 향후 KO/JA/ZH parallel 번역 검토)
- cross-cutting 페이지 추가 시 categories 자동 분류 (현재 수동)

## 영향 받는 항목

- `Language/schema/AGENTS.md` L328-333 (Multi-language Workflow — comparative 위키 통합)
- 5개 per-language `wiki/{Lang}/index.md` Cross-Language Comparisons 섹션
- `wiki/comparative/index.md` — master navigation hub, 6 카테고리 분류
- `Language/log.md` 2026-07-19, 2026-07-29, 2026-08-04 entries (comparative 확장)

## 관련 결정

- ADR-0001 (Theme-file 컨벤션) — per-language vocabulary 가 단일 언어 페이지, comparative 는 cross-language
- ADR-0002 (5언어 병렬 구조) — 5언어 모두 comparative/ 와 양방향 reference
- ADR-0003 (Pipeline YAML contract) — comparative/ 페이지는 YAML 대상 아님 (주로 prose synthesis)

## 변경 이력

- 2026-07-19: comparative/ 디렉토리 신설, 28+ 페이지 초기 배치
- 2026-07-28: comparative/* 위키링크 활성화 (orphan 35 → 12, backtick 제거 + stem 축약)
- 2026-07-29: 6 cross-cutting 페이지 추가 (mood-systems, tense-aspect-systems, etc.)
- 2026-08-04: 23 페이지 추가 (comparative/ 35+ → 44 페이지, commit `2e50f1e`)
- 2026-08-08: ADR 형식화 (배치 governance, batch A)
