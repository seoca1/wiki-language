# Language Decisions — Index

**최종 갱신**: 2026-08-08
**총 ADR 수**: 4
**규약**: 최상위 `AGENTS.md` — "Accepted ADR은 immutable. 변경 필요 시 신규 ADR 작성."

---

## 상태 범례

- **Draft**: 작성 중, 사용자 결정 대기
- **Accepted**: 결정됨. 변경 시 새 ADR 작성 필요
- **Deprecated**: 더 이상 유효하지 않음. 사유 명시
- **Superseded by ADR-XXXX**: 새 결정으로 대체됨

---

## ADR 인덱스

| # | 제목 | 상태 | 날짜 | 우선순위 |
|---|---|---|---|---|
| 0001 | [Theme-file 컨벤션 — 단어/표현당 별도 페이지 금지](0001-theme-file-convention.md) | **Accepted** | 2026-07-10 (effective) / 2026-08-08 (ADR 형식화) | P1 |
| 0002 | [5개 언어 병렬 구조 + Chinese raw 예외](0002-5-language-parallel-structure.md) | **Accepted** | 2026-07-13 (effective) / 2026-08-08 (ADR 형식화) | P1 |
| 0003 | [Pipeline YAML contract — downstream consumer machine-readable 인터페이스](0003-pipeline-yaml-contract.md) | **Accepted** | 2026-07-29 (effective) / 2026-08-08 (ADR 형식화) | P1 |
| 0004 | [comparative/ 위키 스코프 — cross-language 비교 페이지 통합 정책](0004-comparative-wiki-scope.md) | **Accepted** | 2026-07-19 (effective) / 2026-08-08 (ADR 형식화) | P2 |

---

## 결정 영향 그래프

| 결정 | 영향 받는 영역 | 강제 사항 |
| --- | --- | --- |
| 0001 (Theme-file) | 모든 vocabulary/expressions 신규 파일 | per-word 별도 페이지 금지, theme 파일에 `### {word}` 섹션 |
| 0002 (5언어 병렬) | 5개 per-language wiki layout | 동일 디렉토리 layout + Chinese raw 예외 (Option A) |
| 0003 (Pipeline YAML) | 모든 vocabulary theme 파일 | `## Pipeline Form` YAML 섹션 + 7필드 (id/display/input/meaning/level/category/source) |
| 0004 (comparative) | cross-language 페이지 추가 | comparative/ 단일 위치 + per-language 양방향 reference |

### 핵심 invariant (모든 ADR 합집합)
1. **단일 진실 공급원 (Single Source of Truth)**: wiki 가 raw 보다 우선, theme-file 의 human 본문이 machine-readable YAML 보다 우선
2. **5언어 독립 + 양방향**: 각 언어 wiki 는 독립적으로 동작 가능 + comparative/ 로 cross-reference
3. **컨슈머 분리**: Language 위키는 다운스트림 (게임, openclaw) 없이도 독립 성장, 다운스트림은 Language 의 YAML 을 인용만 함

---

## 노트

- Language/ vault 는 LLM Wiki 3계층 (raw/wiki/schema) + comparative analysis 위주
- 게임/파이썬/도구 관련 ADR 은 roguelike_sprawl/decisions/ 참조
- 단편/스토리 관련 ADR 은 Fiction/decisions/ 참조 (Fiction wiki 가 게임의 primary source)
- 본 ADR 들은 모두 **retrospective documentation** — 실제 컨벤션은 effective date 부터 이미 적용 중이었음, 2026-08-08 에 ADR 형식으로 형식화

---

## 향후 결정 후보

- `schema/vocabulary.md` vs 별도 `decisions/vocabulary-schema.md` 분리 필요 여부 (현재 schema/ 보조 파일 유지)
- Chinese raw 정책 전환 (Option B = .openclaw/ 추출, Option C = placeholder) 검토
- EN/JA/KO `wiki/{Lang}/grammar/` 디렉토리 보강 (현재 부재, ZH 2 + ES 5 보유)
- Expression pages machine-readable contract (현재 vocabulary 만 YAML 정의)
- 5개 언어 일관성 검증 자동화 (cross-language symmetry check 도구)
- comparative/ 페이지 다국어 parallel 번역 (현재 영어만)
- `tools/generate_yaml_pipeline.py` 정식 canonical 화 (현재 /tmp 일회성 스크립트)

---

## 변경 이력

- 2026-07-28: 디렉토리 신규 (workspace audit 후속, Language/log.md 와 동시)
- 2026-08-08: 배치 governance — 4 ADR 추가 (theme-file, 5-language, YAML contract, comparative scope)
  - 모두 retrospective documentation — effective date 는 각 ADR 의 컨벤션이 실제 적용된 시점
  - 신규 architectural 결정은 아님, 기존 implicit 결정을 immutable 형식으로 보존
