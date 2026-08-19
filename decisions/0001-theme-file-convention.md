# ADR-0001: Theme-file 컨벤션 — 단어/표현당 별도 페이지 금지

**상태**: Accepted
**날짜**: 2026-07-10 (effective) / 2026-08-08 (ADR 형식화)
**결정자**: 사용자
**우선순위**: P1

## 컨텍스트

Language 위키는 2026-06~07 에 걸쳐 빠르게 확장되며 모든 단어·표현·관용구를 **개별 `.md` 파일**로 만드는 패턴을 사용했다. 그 결과:

- 2026-07 시점: per-word stub 파일 **624+ 개** 자동 생성됨 (KO 288, ZH 119, ES 96, JP 71, EN 49)
- `_inventory/BROKEN_WIKILINKS_2026-07-11.md` 에 broken inventory 68건 누적
- graph view 가 단어 단위로 fragmentation → Obsidian 백링크 패널이 거의 무용
- 신규 vocabulary 추가 시 파일 단위 frontmatter / index 갱신 / log 기록 부담이 선형 증가

같은 시기에 `Game/lingotype/raw/{lang}_words.md` 가 게임 코퍼스를 위해 vocabulary 항목을 가져와야 하는데, per-word 페이지 형식이 YAML 머신러더블 export 와 충돌했다.

## 고려한 옵션

### Option 1: 그대로 유지 (per-word 페이지)
- **장점**: 단어 단위 주소 (`[[사랑]]`) 가능, Obsidian 백링크 명확
- **단점**: 파일 수 폭증, lint false positive 증가, 신규 단어 추가 비용 선형, YAML 머신러더블 export 비효율
- **검토 결과**: 624+ 파일 증가 추세로 지속 불가능

### Option 2: Theme-file 통합 (추천) — 채택
- **설명**: vocabulary 와 expression 을 **테마 단위 파일** (`{theme}.md`) 로 통합. 개별 단어는 그 안의 `### {word}` 섹션. wikilink 는 theme-file 의 section anchor 로 resolve.
- **장점**:
  - 파일 수 안정 (vocabulary theme ~15개/언어)
  - `### {word}` 섹션이 YAML 머신러더블 export 의 자연스러운 단위
  - vault lint 가 section-anchor matching 으로 모든 `[[word]]` 링크 resolve (2026-07-22+)
  - graph view 가 theme 단위로 응집 → 학습 흐름 가시화
  - 신규 단어 추가는 theme 파일에 `### ` 섹션 append → 비용 0
- **단점**:
  - 단어별 독립 페이지 부재 (Obsidian 백링크는 section anchor 단위로 동작)
  - per-word 페이지에 익숙한 워크플로 변경 필요

### Option 3: 데이터베이스 (SQLite, Notion DB) 전환
- **장점**: 정규화된 query, 빠른 검색
- **단점**: markdown wiki 컨벤션 파괴, Obsidian graph view 손실, 마이그레이션 비용 막대
- **검토 결과**: over-engineering, 거절

## 추천

**Option 2: Theme-file 통합.**

근거:
1. LLM Wiki 3계층 (raw → wiki → schema) 패턴과 자연스럽게 정렬
2. YAML pipeline entries 의 source-of-truth 위치
3. 게임/오픈클로 다운스트림 컨슈머가 같은 파일을 두 번 (human/machine) 활용 가능
4. Obsidian 의 section anchor 지원으로 단어 단위 link 유지

## 사용자 결정

[x] **Option 2: Theme-file 통합** (effective 2026-07-10)

## 결과 (Consequences)

### 채택된 구조
- **Vocabulary**: `wiki/{Language}/vocabulary/{theme}.md` 안에 `### {word}` 섹션들
- **Expression**: `wiki/{Language}/expressions/{theme}.md` 안에 `## {expression}` 섹션들 (관용구는 예/메타가 풍부해 보조 schema `schema/expression.md` tier-2/3 필드 활용)
- **예외**: 게임 측 미션 대사 (NPC 라인) 같이 다중 문장 + 강한 문맥 의존이면 별도 페이지 허용

### 페이지 형식
```markdown
# {Theme} — {한 줄 설명}

**Source:** [[{source-slug}]]
**Theme:** {Travel & Tourism, Food, ...}
**Level:** A1-A2 | JLPT N5 | TOPIK 2-3 | ...

## {subgroup (optional)}

### {word 1}

**Part of Speech:** ...
**Definition:** ...
**Romaja / IPA / Pronunciación:** ...
**Etymology:** ...

#### Examples
- ...

#### Related Terms
- [[synonym]]
- [[antonym]]

#### Cultural Notes
...

#### Sources
- [[source-title]]
```

### 실행 (Cleanup)
- 2026-08-04 commit `d5b396c` (refactor(Language): theme-file convention cleanup) — 624 per-word 스텁 파일 일괄 삭제
- `_inventory/BROKEN_WIKILINKS_2026-07-11.md` 삭제 (vault lint 으로 대체)
- vault-wide stem matching 도입 (2026-07-22+) 으로 `[[word]]` 가 theme-file 의 `### {word}` 섹션으로 자동 resolve

### 강제되는 결정
- 모든 vocabulary theme 파일은 `## Pipeline Form (machine-readable)` YAML 섹션 필수 (ADR-0003)
- 모든 per-language `index.md` 는 theme 파일 stem 으로 카탈로그화
- 신규 vocabulary 추가는 theme 파일에 `### {word}` append — 신규 파일 생성 금지 (예외: NPC dialogue)

### 향후 결정
- 신규 expression 추가 시 단일 페이지 vs theme 통합 결정 기준 (게임 대사/관용구/속담 분류)
- Theme 파일 분할 기준 (vocabulary 30+ 단어 시 subgrouping 검토)

## 영향 받는 항목

- `Language/schema/AGENTS.md` L74-77 (Vocabulary 컨벤션), L148-153 (Expression 컨벤션)
- `Language/log.md` 2026-07-10 entry, 2026-08-04 batch
- 모든 vocabulary/expressions 신규 파일은 theme 통합

## 관련 결정

- ADR-0003 (Pipeline YAML contract) — theme-file 의 `### {word}` 가 YAML entry 의 source-of-truth
- ADR-0004 (comparative wiki scope) — per-language theme 와 cross-language comparative 의 분리 원칙
- `Game/lingotype/AGENTS.md` §1.5 — 게임 측 raw/ entry 가 source: `[[theme-stem]]` 으로 인용

## 변경 이력

- 2026-07-10: 컨벤션 effective (per-word 페이지 → theme-file 통합)
- 2026-08-04: 624 per-word 스텁 일괄 삭제 (commit `d5b396c`)
- 2026-08-08: ADR 형식화 (배치 governance, batch A)
