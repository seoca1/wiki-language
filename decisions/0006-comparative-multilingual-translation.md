# ADR-0006: comparative/ 다국어 parallel translation policy

**상태**: Accepted
**날짜**: 2026-08-19 (effective)
**결정자**: 사용자
**우선순위**: P2
**관련 ADR**: ADR-0004 (comparative wiki scope)

## 컨텍스트

ADR-0004 는 `wiki/comparative/` 가 **EN 중심 cross-language reference** 임을 정의했다. 65개 페이지가 모두 영어로 작성되어 있으며, 5개 언어 컬럼 (English / Spanish / Japanese / Korean / Chinese) 으로 side-by-side 비교 테이블을 보유한다.

2026-08-08~14 의 future-candidates 에 "comparative/ 페이지 다국어 parallel 번역 (현재 영어만)" 항목이 반복 등재되었으나 결정되지 않았다. 5개 언어 사용자가 (각 언어 모국어로 comparative 를 읽고 싶어할 때) 현재는 영어를 통해야 한다 — 특히 Korean learner (사용자 본인 포함) 의 경우 한국어 직접 가이드가 없다.

65 페이지 × 4 미번역 언어 (ES/JP/KR/ZH) = **260개 mirrored 파일** 이 필요하다. 이는 workspace AGENTS.md §6 의 "한 세션에 너무 많은 파일 변경" 규약을 초과하지만, 사용자 명시적 결정으로 단일 세션 실행 가능 (2026-08-19).

## 고려한 옵션

### Option 1: 다국어 페이지 안 inline section 으로 통합 — 거절
- **설명**: 각 comparative 페이지 안에 ## 한국어 가이드 / ## 日本語ガイド 등 inline 섹션 추가
- **장점**: 파일 수 증가 없음 (65 페이지 그대로)
- **단점**:
  - 페이지 비대화 (각 페이지가 5배 길어짐)
  - LLM Wiki 3계층 (raw → wiki → schema) 의 single source-of-truth 원칙 약화
  - wikilink 가중치 (per-language anchor) 가 깨짐

### Option 2: `wiki/comparative/{topic}.{lang}.md` 별도 파일 — 채택
- **설명**: 각 comparative 페이지를 4개 미번역 언어에 대해 별도 mirrored 파일로 생성. 원본 EN 페이지 유지, 데이터 테이블은 보존, **내러티브/합성 섹션만** 번역.
- **장점**:
  - 파일 분리 → 각 언어 페이지 독립 진화 가능
  - wikilink target 명확 (per-language anchor)
  - EN 원본 보존 (영어 사용자 reference + machine consumer 통합)
  - downstream consumer (Game/openclaw) 에 영향 없음 (원본 EN 만 인용)
- **단점**:
  - 260 mirrored 파일 추가 → 65 EN + 260 mirror = 325 total comparative/ 파일
  - 동기화 부담 — EN 원본 변경 시 mirror 갱신 필요
  - 첫 번째 실행 비용이 큼 (사용자 명시적 single-session override 로 처리)

### Option 3: 별도 `wiki/{Lang}/comparative/` 디렉토리 (per-language) — 거절
- **설명**: 각 언어 wiki 하위에 comparative/ 디렉토리 생성, 그 안에 language-localized 버전 배치
- **장점**: per-language wiki 완전 자립 (ADR-0002 §invariant 정렬)
- **단점**:
  - wikilink 깨짐 — `wiki/Spanish/comparative/greetings.md` 가 `wiki/comparative/greetings.md` 와 cross-reference 해야 함
  - 5개 언어 × 65 페이지 = 325 파일 + EN 원본 = 총 390 파일, Option 2 와 동일
  - comparative/ 의 "단일 cross-language reference" 컨셉 손상

### Option 4: hybrid — `wiki/comparative/{topic}.{lang}.md` + per-language 학습 노트 — 부분 채택
- **설명**: Option 2 + 각 미러 페이지 끝에 "per-language 학습 노트" 섹션 추가 (해당 언어 학습자 대상 추가 가이드)
- **장점**: pure 번역 + 학습 컨텍스트 추가 가치
- **단점**: 작성 부담 증가

## 추천

**Option 2 + Option 4 의 부분 결합: `wiki/comparative/{topic}.{lang}.md` 별도 파일 + 학습자 대상 context 노트 (해당 언어 wikilink + 학습 strategy).**

근거:
1. 파일 분리로 각 언어 독립 진화 가능
2. wikilink 단절 없음 (모든 언어 페이지가 EN 원본 + cross-language tables 보유)
4. 학습자 대상 추가 컨텍스트 (한국어 학습자 → 한국어 위키 페이지 인용 빈도 ↑)
5. downstream consumer 무영향 (Game/openclaw 는 EN 원본만 사용)

## 사용자 결정

[x] **Option 2 + 4 부분 결합: `wiki/comparative/{topic}.{lang}.md` 별도 + 학습자 context 노트** (effective 2026-08-19)

## 결과 (Consequences)

### 파일 명명 + 위치

| 언어 | 파일 패턴 | 예시 |
|---|---|---|
| English (원본) | `wiki/comparative/{topic}.md` | `wiki/comparative/greetings.md` |
| Spanish | `wiki/comparative/{topic}.es.md` | `wiki/comparative/greetings.es.md` |
| Japanese | `wiki/comparative/{topic}.ja.md` | `wiki/comparative/greetings.ja.md` |
| Korean | `wiki/comparative/{topic}.ko.md` | `wiki/comparative/greetings.ko.md` |
| Chinese | `wiki/comparative/{topic}.zh.md` | `wiki/comparative/greetings.zh.md` |

### 번역 정책 (Quality bar)

1. **번역 범위**: **내러티브 + 합성 섹션만**. 데이터 테이블 (5언어 컬럼) + 외부 wikilink 보존.
2. **섹션 보존**: EN 원본 의 모든 ## 섹션 헤더 유지 (번역 + 영문 병기 가능, e.g., "## Key Contrasts (핵심 대조)").
3. **wikilink 보존**: 모든 wikilink 는 EN stem 그대로 유지 (`[[greetings]]`, `[[travel-essentials]]` 등).
4. **학습자 context 노트**: 미러 페이지 끝에 "## {Language} 학습자 노트" 섹션 추가. 해당 언어 학습자가 마주치는 일반적인 함정/전이 오류/추천 학습 전략.
5. **한국어 mirror 가 가장 상세**: 사용자가 한국어 사용자이므로, 한국어 mirror 에 학습 strategy + 워크플로우 + 비교 시사점 추가.

### 인덱스 갱신

`wiki/comparative/index.md` 에 각 페이지별 미러 링크 추가:

| Page | EN | ES | JP | KR | ZH |
|---|---|---|---|---|---|
| [[greetings]] | EN | [[greetings.es]] | [[greetings.ja]] | [[greetings.ko]] | [[greetings.zh]] |

### 동기화 정책 (신규)

- EN 원본 갱신 시, 4개 mirror 의 갱신 필요 — **mirror 갱신 우선순위** = KR (사용자 모국어) > ZH > JP > ES
- mirror 갱신은 별도 세션 (단일 세션에 너무 많은 파일 변경 금지 원칙 준수)
- `tools/symmetry_check.py` 가 mirror 파일 부재 감지 → ADR-0006 violation 으로 warn

### 강제되는 결정

- 모든 신규 comparative/ 페이지는 EN 작성 후 4개 mirror 생성 의무 (단, 미러는 사용자 우선순위 결정)
- 기존 65 EN 페이지 의 mirror 작업은 **사용자 명시적 세션 요청 시에만** 진행 (단일 세션 부담)
- mirror 파일은 EN 원본의 머신 consumer 호환성 보장 (wikilink 동일)

### 향후 결정

- mirror 동기화 자동화 (EN 변경 감지 → mirror regeneration script)
- comparative/ 페이지 작성 정책 (EN 우선 vs 5언어 동시)
- 한국어 mirror 깊이 우선 정책의 정확성 (사용자 학습 데이터 축적 후 재평가)

## 영향 받는 항목

- `wiki/comparative/index.md` — 신규 컬럼 추가 (mirror 링크)
- 65 EN 페이지 × 4 mirror = **260 파일 신규 생성**
- `tools/symmetry_check.py` — comparative/ mirror coverage detector 추가 가능
- `log.md` — 진행 단계별 entry append

## 관련 결정

- ADR-0004 (comparative wiki scope) — 본 ADR 의 토대
- ADR-0001 (theme-file convention) — comparative 는 페이지 단위 (theme-file 예외)
- ADR-0002 (5언어 병렬) — mirror 파일은 comparative/ 하위 (per-language 아님)
- `Game/lingotype/AGENTS.md` §1.5 — downstream consumer 는 EN 원본만 인용, mirror 영향 없음

## 변경 이력

- 2026-08-19: ADR 신규 (effective) — Option 2 + 4 부분 결합 채택
- 2026-08-19: 65 EN 페이지 × 4 언어 mirror 실행 (사용자 명시 single-session override)
- 2026-08-19: pilot 1 페이지 ([[greetings]]) + index 갱신