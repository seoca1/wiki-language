# Session Summary — 2026-07-10 (Language/ + Game/typing_language/ 통합 정리)

**Scope**: 사용자가 `Language 경로 점검` 요청으로 시작한 세션. 본 세션 동안 Language/ + Game/typing_language/ 두 프로젝트에 걸친 12+ 액션 수행.

**핵심 결정 — 정착된 원칙**:

> **"단어나 문장 하나를 별도 `.md` 로 만들지 않는다"** (사용자 선언, 2026-07-10)
>
> 모든 어휘/표현은 `wiki/{Lang}/{vocabulary,expressions}/{theme}.md` 같은 **테마 파일**에 통합하고,
> 단일 단어·관용구는 그 안 `### {word}` 또는 `## {expression}` 섹션이 된다.
> 게임 측 source citation도 동일한 theme-anchor 컨벤션: `[[{theme}]]`.

## 액션 요약 (12개)

| # | 액션 | 산출 | 파일 |
|---|---|---|---|
| 1 | vocabulary YAML 5필드 부록 | 25 파일 / 654 entry | `wiki/*/vocabulary/*.md` (전부) |
| 2 | Korean vocab 3개 인제스트 | 292 entry / 12 OCR 노이즈 제외 | `wiki/Korean/vocabulary/{business,food,emotions-personality}-vocabulary.md` (신규) |
| 3 | study-plan/ 표준화 | EN/JP/KR stub README + index 참조 | `wiki/{EN,JP,KR}/study-plan/README.md` (신규) |
| 4 (1차) | 안전 wikilink strip | 65건 (formatting 한정) | `wiki/content-lineage.md`, `_publish/`, `wiki/EN/sources/*` |
| 4 (후속) | Wiki Page col drop + パスポート 매핑 | 73 테이블 / 654 행 drop; 86 `[[パスポート]]` → `[[pasupooto]]` | `wiki/*/vocabulary/*.md` (전부) |
| 5 | jp-travel-vocab/ 카탈로그 | orphan 86 → 0 | `wiki/{EN,KR}/jp-travel-vocab/INDEX.md` (신규) |
| 6 | .gitignore + 시큐어 위생 | .gitignore 작성, .env / __pycache__ 추적 해제 | `.gitignore` (신규) |
| 7 | 양방향 contract 검증 | Language 1건 수정, Game 3건 플래그 | `wiki/pipeline-to-game.md` |
| 8 | Wiki Page col drop + corruption fix | 35건 `[[word]]word` corruption 보정 | `wiki/Spanish/vocabulary/*.md` 등 |
| 9 | **jp-travel-vocab/ 통합** | 88 per-word → 2 theme 파일 | `wiki/{EN,KR}/jp-travel-vocab.md` (신규), `jp-travel-vocab/` 폴더 삭제 |
| 10 | **expressions/ 통합** | 59 per-expression → 9 theme 파일 | `wiki/{EN,JP,KR,ES}/expressions/{theme}.md` (신규) |
| 11 | Game contract sync (cross-project) | 필드 schema, source 명세, location map 갱신 | `Game/typing_language/wiki/corpus-pipeline.md` + AGENTS.md + languages/korean.md |
| 12 | Fiction cross-link (vault-wide) | 96 → 13 orphan (ko/ 번역 INDEX + output/ → works/ 매핑) | `Fiction/derivative/sprawl-trilogy/INDEX.md` + 8 `wiki/works/*.md` |

## 누적 지표

| 지표 | 시작 | 현재 |
|---|---|---|
| Language/ wiki/ .md 파일 | ~280+ | **121** |
| Language/ per-item .md (단어/표현 1개당) | 145 | **0** |
| Language/ vocabulary theme 파일 | 25 | 30 (jp-travel 통합 포함) |
| Language/ expression theme 파일 | 0 | 9 |
| Language/ Pipeline Form YAML entries | 0 | 1,034 |
| Language/ broken wikilink | 1,302 | 86 (모두 immutable) |
| Language/ touch 가능 broken | 1,302 | **0** |
| Game/typing_language/ total broken | 35 | 23 (raw 12 + immutable 11) |
| Fiction/ orphan (improved detection) | 96 | **13** |

## 원칙 적용 범위

| 영역 | 적용 |
|---|---|
| vocabulary (per-word) | ✅ `### {word}` 섹션 |
| expressions (per-idiom) | ✅ `## {expression}` 섹션 |
| jp-travel-vocab (per-word) | ✅ 단일 theme 파일 통합 |
| culture (per-topic) | ❌ 미적용 (multi-paragraph essay 단위) |
| sources (per-source) | ❌ 미적용 (출처 1건 = 페이지 1건 자연) |

## 알려진 잔여 (touch 가능 scope = 0)

| 위치 | 개수 | 이유 |
|---|---|---|
| `Language/wiki/Spanish/log.md` | 59 | append-only history (immutable) |
| `Language/_publish/2026-W25/*.md` | 26 | published guides (별도 결정) |
| `Language/schema/AGENTS.md` | 1 | 의도된 `[[{theme-filename}]]` template placeholder |
| `Game/typing_language/raw/{lang}_words.md` | 12 | read-only (AGENTS.md §2) |
| `Game/typing_language/log.md` | 3 | append-only history |
| `Game/typing_language/AGENTS.md` | 3 | 의도된 `[[{theme}]]` template placeholder |
| `Game/typing_language/corpus-sync-plan.md` | 2 | `[[word]]` YAML 예시 inline code 안 (false positive) |
| `Game/typing_language/wiki/corpus-pipeline.md` | 1 | template placeholder |
| `Fiction/derivative/_system/*` + `schema/skills/*` | 11 | utility 문서 (의도적 standalone) |
| `Fiction/output/*` (kr 번역) | 0 | Action 14 로 works/ 에 cross-link 완료 |
| `Fiction/derivative/sprawl-trilogy/ko/*` | 0 | Action 13 로 INDEX.md 에 39 매핑 추가 |

## 사용자 결정 사항 (세션 내)

- "단어나 문장 하나를 .md 로 만들지 않는다" — 원칙 선언 (vocabulary, expressions, jp-travel-vocab 에 적용)
- 🚨 Notion API 토큰 노출 무시 (회전/히스토리 scrub 안 함) — **vault의 `_publish/scripts/.env` 에 `NOTION_TOKEN` 평문으로 남아 있음. 보안을 신경 쓸 경우 별도 액션 필요**
- Game 측 wiki/ 수정 허락 (cross-project 규약 일시 면제)
- 가장 보수적 옵션 선택 (Action 4 안전 strip 65건 한정, 표현 통합 시 per-file .md 0건)

## 후속 후보 (사용자 결정 대기)

| 항목 | 노트 |
|---|---|
| Game corpus (`raw/{lang}_words.md`) 재큐레이션 | per-word → theme-anchor — read-only 권한 필요 |
| Game/roguelike_sprawl/ 점검 | 214 orphan — 코드+wiki 혼합, 별도 점검 가치 |
| Game/typing_language/AGENTS.md §4 갱신 | 언어별 섹션의 source 명세 일관성 추가 검토 |
| Git commit 일괄 처리 | 본 SESSION_SUMMARY 작성을 포함한 commit 진행 |

## 참고

- 자세한 작업 흐름: 각 언어 `wiki/{Lang}/log.md` 의 2026-07-10 엔트리 참조
- Game 측 cross-sync: `Game/typing_language/log.md` 의 2026-07-10 contract sync 엔트리 참조
- 이전 vault-wide 정리: `VAULT_AUDIT_REPORT.md`
