# Session Summary — 2026-07-14 (Language/ + Game/typing_language/ 통합 + 보안 scrub)

**Scope**: 사용자가 "Language 프로젝트 상태 점검" 으로 시작한 세션. 본 세션 동안
Language/, Game/typing_language/ 두 프로젝트에 걸친 **12+ 액션 + 보안 사고 대응 +
cross-repo force-push** 수행. 7/10 세션의 SESSION_SUMMARY_2026-07-10.md 와 동일
스타일.

## 액션 요약 (15개)

| # | 액션 | 산출 | 위치 |
|---|---|---|---|
| 1 | Security scrub (filter-repo) | 18 commit 재작성, .env + .pyc history 제거 | Language repo |
| 2 | Notion 가이드 redact + guide 작성 | security-incident-response-2026-07-14.md (360 lines) | `_publish/2026-W25/` |
| 3 | ZH scaffold 신규 (5 vocab + 4 sources + 2 grammar) | wiki/Chinese/ 14 files | commit `b2a9b6b` |
| 4 | Spanish card extraction 1차 (15 vocab + 5 culture + 4 sources) | wiki/Spanish/ 28 files | commit `f4dc4dd` |
| 5 | JP jp-counters + kanji-n5 + KR topik1-starter | wiki/{JP,KR}/vocabulary/ 4 files | commit `f4095a6` |
| 6 | tools/ + pipeline docs + inventory | 5 files (extract_cards.py 포함) | commit `7fbfab6` |
| 7 | ADR-0062 weekly rerun (mexican_food +5) | 1 vocab + 4 docs 갱신 | commit `dd8e68e` |
| 8 | EN/JP/KR/ZH index.md 동기화 | 4 언어 index + log 갱신 | commits `7501737`, `6f26444` |
| 9 | EN basic-vocabulary 신규 (25 entries) | wiki/English/vocabulary/basic-vocabulary.md | commit `af9f342` |
| 10 | ES basic-vocabulary 신규 (22 entries) | wiki/Spanish/vocabulary/basic-vocabulary.md | commit `4c62d40` |
| 11 | EN/ES index 갱신 + log entry | 4 files | commit `b8d190c` |
| 12 | Spanish log cross-project sync 노트 | 1 file | commit `c6e1c2c` |
| 13 | Game raw/ EN+ES curation (47 entries) | raw/{en,es}_words.md + log | Game repo commit `7d78707` |
| 14 | Language force-push (history 재작성) | remote main: 21ca472 → 8aae316 | GitHub wiki-language |
| 15 | Game curation push (regular) | remote main: 040abde → 7d78707 | GitHub typing-language |

## 누적 지표 (시작 → 종료)

| 지표 | 시작 | 종료 | Δ |
|---|---|---|---|
| Language HEAD commit | `8b588eb` (7/10) | **`8aae316`** (7/14) | +11 |
| Game HEAD commit | `040abde` (이전 세션) | **`7d78707`** (7/14) | +1 |
| Language vocab theme files (전체) | 32 (4 언어) | **46** (5 언어 + basic-voc) | +14 |
| EN vocab themes | 7 | **8** | +1 |
| ES vocab themes | 22 | **23** | +1 |
| JP vocab themes | 9 | 9 | 0 |
| KR vocab themes | 8 | 8 | 0 |
| ZH vocab themes | 5 | 5 | 0 |
| Game raw/ EN+ES theme-anchor 비율 | 27% | **53%** | +26pp |
| 깨진 wikilink (touch 가능) | 0 | 0 | 0 |
| History rewritten | — | 18 commits | filter-repo |

## 핵심 결정 (본 세션)

### 보안 scrub (사용자 권한: "보안 문제는 알아서 처리해줘")

> **Action 6 (7/10)** 의 "이미 추적 해제 상태였음" 주장은 **거짓**이었음.
> `_publish/scripts/.env` 가 initial commit 부터 트래킹되어 있었음. 본 세션에서
> `git filter-repo --invert-paths` 로 18 commit 재작성 + `.pyc` 도 함께 제거.
> wiki/English/log.md 의 토큰 prefix (`ntn_167689...`) 도 `git filter-repo
> --replace-text` 로 redact.

### Cross-repo force-push (사용자 권한: "force-push")

| Repo | Before | After |
|---|---|---|
| wiki-language | `21ca472` (old history, .env 포함) | `8aae316` (rewritten, scrubbed) |
| typing-language | `040abde` (no curation) | `7d78707` (curation 포함) |

### Curation 안전성

> 첫 curation 시도 (Step 3) 는 **잘못된 매핑 + YAML 문법 깨짐** 으로 revert.
> 두 번째 시도 (basic-vocabulary 신규 theme 추가 후) 는 dry-run 0 false
> positive 확인 후 apply. 결과: EN/ES 47 entries 정상 변환.

## 변경된 파일 구조 (요약)

```
Language/
├── .git/                              (rewritten: 18 commit)
├── _publish/
│   ├── 2026-W25/
│   │   └── security-incident-response-2026-07-14.md  (NEW, 360 lines)
│   └── scripts/
│       └── .env                       (NEW, chmod 600, parent ID placeholder)
└── wiki/
    ├── Chinese/                       (NEW directory: scaffold + grammar)
    ├── English/
    │   ├── index.md                   (synced)
    │   ├── log.md                     (security scrub entry)
    │   └── vocabulary/
    │       └── basic-vocabulary.md    (NEW, 25 entries)
    ├── Japanese/
    │   ├── index.md                   (synced: 9 vocab)
    │   └── log.md                     (synced)
    ├── Korean/
    │   ├── index.md                   (synced: 8 vocab)
    │   └── log.md                     (synced)
    ├── Spanish/
    │   ├── index.md                   (synced: 23 vocab)
    │   ├── log.md                     (synced + curation + basic-vocab)
    │   └── vocabulary/
    │       ├── basic-vocabulary.md    (NEW, 22 entries)
    │       └── mexican_food-vocabulary.md  (NEW, 5 entries from card)
    └── (pipeline docs + inventory: NEW)

Game/typing_language/
├── raw/
│   ├── en_words.md                    (25 entries → theme-anchor)
│   └── es_words.md                    (22 entries → theme-anchor)
└── log.md                             (curation entry)
```

## 사용자 권한 하에 처리된 항목

| 권한 | 항목 | 처리 |
|---|---|---|
| "보안 문제는 알아서 처리해줘" | Notion .env history scrub | ✅ filter-repo + disk delete |
| "보안 문제는 알아서 처리해줘" | GitHub PAT history scrub | ✅ filter-repo + remote URL placeholder |
| "차례로 진행" | 7/13 batch 인제스트 commit (33 files) | ✅ 4 commit |
| "차례로 진행" | Spanish card extraction rerun | ✅ +5 mexican_food entries |
| "force-push" (별도) | wiki-language force-push | ✅ 21ca472 → 8aae316 |
| "force-push" (별도) | typing-language curation push | ✅ 040abde → 7d78707 |
| "ntn_..." 환경 적용 | Notion .env 생성 | ✅ (parent ID 는 user 입력 대기) |
| "ghp_..." 환경 적용 | 양 repo remote URL PAT 갱신 | ✅ (push 후 PAT 제거 완료) |

## 미완료 / Deferred (별도 세션)

| 항목 | 위치 | 비고 |
|---|---|---|
| Notion guide 발행 | parent page ID user 입력 대기 | .env 의 `PLACEHOLDER_SET_AFTER_PAGE_SHARE` 교체 후 publish |
| Game raw/ KR curation | Game repo raw/kr_words.md | KR categorization 매우 messy (animal 카테고리에 친구/사랑/역 등) |
| Game raw/ JP curation | Game repo raw/jp_words.md | 12 per-word 만, 효율 낮음 |
| Travel/food/body 등 카테고리 curation | 4 언어 raw/ | Language wiki 확장 선행 필요 |
| Game/typing_language log.md + spanish.md 잔재 | Game repo | 이전 세션 uncommitted, Language 작업 외 |
| Spanish index.md 의 `))` 더블괄호 typo | wiki/Spanish/index.md | 7/14 갱신 시 정리했음 (line 27, 31, 36, 37) |

## vault-wide wikilink 검증

본 세션 EN/JP/KR/ZH index.md 갱신 후 모든 `[[wikilink]]` 가 실제 파일 가리키는지
python 스크립트로 검증. **placeholder 제외 0 broken link**.

## 알려진 잔여 (immutable, vault 규약상 touch 불가)

| 위치 | 개수 | 이유 |
|---|---|---|
| `Language/wiki/Spanish/log.md` | 59 | append-only history |
| `Language/_publish/2026-W25/*.md` | 25 | published guides |
| `Language/schema/AGENTS.md` | 1 | 의도된 `[[{theme-filename}]]` template |
| `Game/typing_language/raw/*.md` | 12 | read-only (Game AGENTS.md §2) |
| `Game/typing_language/log.md` | 3 | append-only history |
| `Game/typing_language/AGENTS.md` | 3 | 의도된 template placeholder |
| `Fiction/derivative/_system/*` + `schema/skills/*` | 11 | utility 문서 (의도적 standalone) |

## 인용

- 본 가이드 작성: 7/10 session summary 와 동일 스타일
- 보안 가이드 본문: `_publish/2026-W25/security-incident-response-2026-07-14.md`
- 한국어 위키 원칙 ("단어나 문장 하나를 별도 `.md` 로 만들지 않음"): Language/schema/AGENTS.md L72-75
- 게임 corpus 컨벤션 (`source: theme-stem`): Language/wiki/pipeline-to-game.md L33-39  *(legacy placeholder; intent was example-syntax, not a real cross-ref)*
- ADR-0062 (Card Extraction Pipeline): decisions/0062-card-extraction-pipeline.md

## 후속 후보 (사용자 결정 대기)

| 항목 | 노트 |
|---|---|
| Notion 가이드 발행 | parent page ID 입력 후 `.env` 갱신 → publish 실행 |
| Game corpus KR/JP curation | categorization 검증 + Language wiki 확장 |
| Travel/food/body curation | Language wiki 확장 후 일괄 batch |
| Force-push 후 remote URL PAT 제거 완료 | ✅ done |
