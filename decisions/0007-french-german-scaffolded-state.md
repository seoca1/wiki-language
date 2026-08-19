# ADR-0007: French/German scaffolded state — promote / document / sunset 결정

**상태**: Accepted
**날짜**: 2026-08-19 (effective)
**결정자**: 사용자
**우선순위**: P2
**관련 ADR**: ADR-0002 (5언어 병렬 — 예외 인정)

## 컨텍스트

ADR-0002 는 5개 메인 언어(EN/ES/JP/KR/ZH) 의 병렬 구조를 정의한다. 그러나 `Language/wiki/French/` 와 `Language/wiki/German/` 는 **scaffolded-only** 상태로 존재한다:

| 언어 | wiki/ 파일 | raw/ 파일 | YAML 커버리지 |
|---|---|---|---|
| French | 7 (1 index + 1 log + 5 vocabulary) | 1 (README 만) | 0% |
| German | 7 (1 index + 1 log + 5 vocabulary) | 1 (README 만) | 0% |

이 상태는 2026-07~08 의 ADR-0001 + ADR-0002 governance batch 에서 "scope creep 방지" 로 의도적으로 유지되었다 — 5개 언어에 콘텐츠를 집중하기 위함. 그러나 `decisions/README.md` future-candidates 에 "French/German scaffolded 상태 결정 (promote / document / sunset 결정 필요)" 으로 2026-08-08 부터 미해결로 남아있다.

`tools/symmetry_check.py` 가 매 실행마다 🔴 ALERT 4건 (vocabulary/expressions 0% YAML) + 🟡 WARN 1건 (vocabulary 5 vs main 40+) 을 보고한다. 이는 의미 있는 시그널이지만 무시하면 ADR/README 비대화 위험이 있다.

## 고려한 옵션

### Option 1: Promote — French/German 을 6/7번째 메인 언어로 격상
- **장점**: 다국어 학습 폭발적 확장, comparative/ 가 5→7언어로 풍부, downstream consumer (Game/openclaw) 가 즉시 활용 가능
- **단점**:
  - raw/ 콘텐츠 부재 (textbook·article·원서 없음) → wiki 가 비어 있음
  - ingest 비용 막대 (사용자 raw 제공 필수 — game의 Phase C1-C4 와 동일 구조적 blocker)
  - ADR-0002 의 "5언어 병렬" invariant 깨짐 → ADR 갱신 또는 ADR-0008 supersede 필요
  - 현재 ~63 ahead-of-origin push backlog 에 또 +60~80 commits 가산

### Option 2: Document — scaffolded-only 상태를 명시화 + ADR/README 갱신
- **장점**:
  - 즉시 적용 가능 (소규모: ADR + README + index 갱신 + ~2 README 파일 작성)
  - future-candidates 항목 제거 → ADR/README 비대화 차단
  - symmetry_check.py 의 French/German 경고를 **known intentional** 로 분류 → 노이즈 감소
  - 사용자가 raw 소스를 제공할 때 즉시 promote 가능 (Option 1 로 진화)
- **단점**:
  - 실제 학습 콘텐츠는 추가되지 않음
  - scaffolded 가 영구화될 위험 (사용자 모르고 방치)

### Option 3: Sunset — French/German wiki/raw 모두 삭제
- **장점**: 코드베이스 청결, ALERT 0건, future-candidates 해결
- **단점**:
  - reversible 하지 않음 — git history 는 남지만 사용자 워크플로가 "다시 scaffold" 해야 함
  - comparative/ 의 French/German 레퍼런스 (예: family-kinship, idioms-proverbs 등) 가 깨질 수 있음
  - ADR-0002 의 5언어 invariant 와 모순되지 않지만 (scaffold 가 없으면 5언어만 존재), "옵션" 자체의 부재는 사용자가 잊어버리면 재발

### Option 4: Hybrid — French/German + Chinese raw 정책 통합 (Option B/C 검토와 함께)
- **장점**: 두 결정이 모두 raw/ 정책 관련 → 동시 처리 효율
- **단점**: 책임 영역이 섞임, ADR 가 무거워짐, 사용자 결정 부담 가중

## 추천

**Option 2: Document — scaffolded-only 상태 명시화 + 향후 raw 제공 시 즉시 promote 가능성 보존.**

근거:
1. **현재 사용자 우선순위**: 5개 메인 언어 콘텐츠 깊이 우선. French/German 은 명시적 사용자 요청 없이는 우선순위 낮음.
2. **즉시 가치**: ADR + README 갱신으로 ADR 비대화 차단 + symmetry_check 노이즈 감소.
3. **Reversibility**: raw 제공 시 Option 1 로 진화 가능 (Option 3 과 달리 irreversible 아님).
4. **convergent with downstream**: lingotype 게임의 future 언어 로드맵이 Chinese(ZH) 확장에 집중 — French/German 게임 통합은 별도 ADR 필요.

## 사용자 결정

[x] **Option 2: Document — scaffolded-only 상태 명시화** (effective 2026-08-19)

## 결과 (Consequences)

### 즉시 적용
1. **ADR-0002 갱신**: 5언어 병렬 invariant 유지, French/German 을 "scaffolded by design" 으로 명시 (§결과에 새 bullet 추가)
2. **`wiki/French/README.md` + `wiki/German/README.md` 갱신**: scaffolded 상태 + raw/ 비어 있음 + 사용자 raw 제공 시 promote 가능성을 첫 줄에 명시
3. **`decisions/README.md` future-candidates 갱신**: "French/German scaffolded 결정" 항목 **resolved** 마커 추가, ADR-0007 cross-reference
4. **`tools/symmetry_check.py` 갱신**: French/German ALERT/WARN 을 "known intentional" 으로 분류 (resolution_status bucket 2 에 매핑)
5. **`log.md` append**: `[2026-08-19] governance | ADR-0007 French/German scaffolded decision`

### Promote 전환 조건 (미래)
- 사용자가 `raw/French/` 또는 `raw/German/` 에 **유효한 source 파일** (textbook chapter, article, novel excerpt) 추가
- ADR-0008 (또는 ADR-0007 amendment) 로 "promote to main language" 결정
- ADR-0002 invariant 갱신 (5언어 → 7언어)
- symmetry_check.py 갱신 (main_langs 리스트에 French/German 추가)
- 1 세션 = 1 언어 ingest (ADR-0001 theme-file + ADR-0003 YAML + ADR-0005 expression YAML 모두 적용)

### 강제되는 결정
- French/German wiki 의 vocabulary/expressions/theme 파일은 **현재 상태 유지** (5 vocab + 1 expression each)
- French/German 의 Pipeline YAML 커버리지는 **0% 유지** (raw 부재 시 machine-readable 생성 불가)
- symmetry_check.py 의 French/German ALERT 는 **의도적** (Option 2 결정이 활성인 한)

### 향후 결정
- French/German **promote** 시점: 사용자 raw 제공 + 별도 ADR-0008
- Chinese raw 정책 (Option B = .openclaw/ 추출, Option C = placeholder) — 별도 ADR 검토

## 영향 받는 항목

- `Language/decisions/README.md` — future-candidates 갱신, ADR count 5→6
- `Language/decisions/0002-5-language-parallel-structure.md` — §결과 에 scaffolded 명시 추가
- `Language/wiki/French/README.md` (NEW if not exists) / 갱신
- `Language/wiki/German/README.md` (NEW if not exists) / 갱신
- `Language/tools/symmetry_check.py` — French/German classification 갱신
- `Language/log.md` — 2026-08-19 entry 추가

## 관련 결정

- ADR-0001 (theme-file) — French/German 5 vocab + 1 expression 도 동일 컨벤션 준수
- ADR-0002 (5언어 병렬) — French/German 은 의도적 예외 (scaffolded-only)
- ADR-0003 (Pipeline YAML) — raw 부재로 YAML 생성 불가 (의도적 0%)
- ADR-0005 (Expressions YAML) — 동일 (의도적 0%)

## 변경 이력

- 2026-08-19: ADR 신규 (effective) — Option 2 Document 채택