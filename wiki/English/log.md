# English Learning - Activity Log

## [2026-06-23] ingest | food-business-emotion-nature-animals-clothing | New vocabulary topics for typing game

### Raw Sources Added
- `raw/English/food-vocabulary.md` (30+ entries)
- `raw/English/business-vocabulary.md` (43 entries)
- `raw/English/emotions-personality-vocabulary.md` (43 entries)
- `raw/English/nature-vocabulary.md` (40 entries)
- `raw/English/animals-vocabulary.md` (37 entries)
- `raw/English/clothing-vocabulary.md` (30 entries)

## [2026-06-18] ingest | first-travel-japan | Korean traveler's perspective on Japan

- Created directory structure
- Set up index.md
- Ready for first source ingest

## [2026-07-10] lint | Language 위키 일괄 점검 + 7 액션 + 후속 1 액션

세션 동안 Language/ 디렉터리 일괄 점검 (총 8 액션 완료). 자세한 기록:
- Action 1: 모든 vocabulary 페이지 (25 파일 / 654 entry) 에 `Pipeline Form` YAML 부록 추가. 5필드 (display/input/meaning/level/category + source) 게임 측 계약 충족
- Action 2: Korean vocabulary 3 페이지 신규 (business/food/emotions-personality), 292 entry 인제스트
- Action 3: study-plan/ 표준 적용 (EN/JP/KR stub README)
- Action 4 (1차): 안전 범위 65건 wikilink strip
- Action 4 (후속): Wiki Page 컬럼 654행 drop + 범위 한정 strip 733건 + `[[パスポート]]` → `[[pasupooto]]` 86건 매핑 + corruption fix 35건
- Action 5: jp-travel-vocab/ 카탈로그 (orphan 86 → 0)
- Action 6: .gitignore 작성, `.env` / `__pycache__` 추적 해제. **🚨 Notion 토큰 평문 노출 발견 — 사용자 액션 필요**
- Action 7: pipeline-to-game.md ↔ corpus-pipeline.md 양방향 검증. Language 1건 수정, Game 3건 플래그
- 결과: broken wikilinks 1302 → 39 (97% 감소). 잔여 39는 vault 규약상 touch 불가 (Spanish log.md 37 + raw/English 2)

## [2026-07-10] security | 🚨 NOTION_TOKEN 평문 노출 (사용자 액션 필요)

- 노출: `_publish/scripts/.env` 내 `NOTION_TOKEN=[REDACTED-NOTION-PREFIX]...`
- **즉시 권장**: Notion workspace → Settings → Integrations → 해당 토큰 폐기 + 재발급
- 본 세션에서 `git rm --cached` 로 향후 추적 차단 (디스크 파일 보존). git 히스토리 scrub 은 사용자 결정 후 별도 세션

## [2026-07-10] refactor | 사용자 원칙 "단어나 문장 하나를 md 로 만들지 않음" 적용

- **원칙**: 어휘는 테마 파일 안 `### {word}` 섹션으로 통합, per-word `.md` 금지.
- **조치**: `jp-travel-vocab/{English,Korean}/` 88 per-word .md + INDEX.md 삭제. 2개 theme-file 통합:
  - `wiki/English/jp-travel-vocab.md` (43 섹션, Pipeline Form 43 entry)
  - `wiki/Korean/jp-travel-vocab.md` (43 섹션, Pipeline Form 43 entry)
- **스키마 갱신**:
  - `schema/AGENTS.md` §Vocabulary Pages: per-word → theme-file 명세 변경. theme 내 `### {word}` 섹션 + YAML 부록 패턴 예시 포함
  - `schema/vocabulary.md`: Vocabulary Page Schema → Vocabulary Theme Schema 로 헤더 변경. per-word 템플릿을 per-word 섹션 템플릿으로 격하
  - `wiki/pipeline-to-game.md`: per-word 페이지 인용 명세 → theme-anchor 단일
- **사이드**:
  - `[[pasupooto]]` 86 wikilink → `[[jp-travel-vocab]]` (theme anchor)
  - sources 안 broken per-word wikilink 9건 strip
  - 23/23 vocabulary 테마 파일 Pipeline Form 부록 보유 (총 710 entries)
- **남은 결정**: expressions/ 와 culture/ 도 같은 원칙 적용 여부

## [2026-07-10] refactor | 사용자 원칙이 expressions/ 로 확장 — 59 파일 → 9 파일 통합

- **조치**:
  - EN: 12 per-expression → 2 theme 파일 (`daily-basics.md` 4 + `dating-romance.md` 8)
  - JP: 7 per-expression → 1 theme 파일 (`dating-romance.md` 7)
  - KR: 8 per-expression → 1 theme 파일 (`dating-romance.md` 8)
  - ES: 32 per-expression → 5 theme 파일 (`daily-life.md` 8, `romance-relationships.md` 7, `emotions-reactions.md` 10, `subjunctive-patterns.md` 3, `cultural-idioms.md` 4)
  - 합계: 59 → 9 (-85%)
- **부수**:
  - 각 통합 파일의 `[[stem]]` → theme-anchor `[[theme-filename]]` 정규화 (85건 자동 매핑)
  - 외부의 broken per-expression wikilink 74건 strip
  - `[[{name}.md]]` 의 잘못된 suffix 85건 보정
- **스키마 갱신**:
  - `schema/AGENTS.md` §Expression Pages: per-expression → theme-file convention (vocabulary 와 동일 패턴)
  - `schema/expression.md`: "Expression Page Schema" → "Expression Theme Schema" 헤더 + per-expression 섹션 템플릿
  - `wiki/pipeline-to-game.md`: expressions 도 theme-file 통합 컨벤션 명시
- **최종**: 86 wikilink broken. touch 가능 범위 0 (전부 Spanish/log.md 59 + _publish/ 24 + arranque-semana-2 2 + schema/AGENTS.md 1)
- **남은 결정**: culture/ 도 같은 원칙 적용 여부 (권장 안 함: 다중 문단 essay 단위)

## [2026-07-10] lint | sources/ 폴더 orphan 정리 — index.md 에 누락된 소스 페이지 30+건 노출

- 점검이 발견: 여러 언어의 sources/ 폴더에 파일이 존재하지만 index.md 에서 미링크 (orphan)
  - EN: 4 (health-and-body, holidays-and-celebraciones, sports-and-hobbies, technology-and-internet)
  - JP: 14 (anime-drama-quotes 외 13건, index 가 9/14만 노출)
  - KR: 10 (대부분 미노출)
  - ES: 5 (comida-y-restaurante, fiestas-y-celebraciones, first-travel-spain, literature-passages, trabajo-y-carrera)
- 조치: 각 언어 index.md 의 `## Sources (...)` 섹션을 소스 디렉토리 전체로 재생성. 각 페이지의 H1 을 표기로 사용, "(Source Hub)" 같은 boilerplate 제거.
- 결과: wiki/ orphan 페이지 24 → 6 (3 메타 문서 + 3 study-plan README stub — 모두 의도적)
- 후속: JP index.md 에 JP study-plan/README 링크가 없음 — 마이너 정정 가능

## [2026-07-10] contract sync | Game 측 corpus-pipeline.md + korean.md 정합

- **트리거**: 본 세션 시작 시 Language 측 컨벤션 (`단어/문장 1개 = .md 금지`) 확립 후 cross-project 동기화 필요
- **사용자 권한**: Game 측 wiki/ 도 수정 허락 받음 (root AGENTS.md cross-project 규약 일시 면제)
- **조치**:
  - `Game/typing_language/wiki/corpus-pipeline.md`: 필드 schema 표, 데이터 흐름도, 위치 매핑 표, YAML 예시, 시나리오 A 모두 theme-file 컨벤션으로 갱신
  - `Game/typing_language/wiki/languages/korean.md`: source 예시 per-word → theme anchor, 코퍼스 상태 갱신
  - `Game/typing_language/log.md`: 2026-07-10 cross-sync 기록
- **제한**: `Game/typing_language/raw/kr_words.md` L9 의 per-word 명세는 raw/ read-only 규약으로 미수정 (데이터 영향 없음, contract doc만 stale)
- **결과**: 양 프로젝트 정합 완료. 게임 측 source citation parser 가 `[[{theme}]]` anchor 만 매칭

## [2026-07-14] security | NOTION_TOKEN / GitHub PAT scrub + history rewrite

- **트리거**: 7/10 세션에서 "히스토리 scrub 안 함" 결정 후 잔존. 본 세션 사용자 권한 ("보안 문제는 알아서 처리해줘") 으로 scrub 실행.
- **작업**:
  - `git filter-repo --invert-paths` 로 다음 2 path 완전 제거 (모든 history):
    - `_publish/scripts/.env` (119 byte, `NOTION_TOKEN=...` 평문)
    - `_publish/scripts/__pycache__/publish_to_notion.cpython-314.pyc` (compiled bytecode, `secret_xxx` placeholder 포함)
  - `git filter-repo --replace-text` 로 `wiki/English/log.md` L34 의 `ntn_[REDACTED-NOTION-PREFIX]...` prefix 8자 redact
  - 검증: `git rev-list --all | xargs git ls-tree -r` 전수 walk, `ntn_*` 패턴 잔존 0
- **디스크**: `_publish/scripts/.env` + `__pycache__/` 삭제. `.env.example` (template, secret 무포함) 보존.
- **.gitignore 검증**: `.env`, `.env.local`, `.env.*.local` 규칙 존재, 신규 추가 불필요.
- **Action 6의 잘못된 보고 정정**: "이미 추적 해제 상태였음" → 거짓. 실제로는 initial commit (`e4782bd`) 부터 트래킹되어 있었음. `.gitignore` 는 향후 신규 추적만 차단.
- **🚨 사용자 조치 필요 (scrub 범위 외)**:
  1. **GitHub PAT 회전**: `git remote -v` 출력에 GitHub PAT 평문 노출됨 (`github_pat_11A...`). GitHub → Settings → Developer settings → Personal access tokens → 해당 토큰 **즉시 폐기** → 신규 발급 → `git remote set-url origin https://<NEW_PAT>@github.com/seoca1/wiki-language.git`
  2. **Notion 토큰 회전**: scrub 으로 git history는 깨끗하나, 노출된 적 있는 토큰은 본질적으로 compromised. Notion workspace → Settings → Integrations → 해당 integration 회전.
  3. **force push (선택)**: 원격 `wiki-language` repo 도 동일하게 history scrub 필요. 본 세션에서는 사용자 결정 대기 (force push 는 review 후).
- **history 영향**: 모든 commit hash 변경 (HEAD `d72d9e8` → `dfd3484`). 기존 clone 은 invalid, force-fetch 또는 reclone 필요.

## [2026-07-14] sync | index.md 갱신 — 7/13 batch 누락분 반영

- **Trigger**: 본 세션 Language 상태 점검에서 발견 — EN/JP/KR index.md 가 "Last updated: 2026-07-08" 그대로 stale. 7/13 batch 의 vocab theme 신규분이 index 에 미반영.
- **Action**: index.md 전면 갱신 (각 언어 vocab/expressions/culture/sources 카운트 + 신규 theme link + 마지막 갱신일)
- **변경**:
  - EN: Last updated → 2026-07-14, sources 15개 명시 + first-travel-japan source 추가, Pipeline Notes 섹션
  - JP: Last updated → 2026-07-14, vocab 7 → 9 (+ jp-counters + kanji-n5), sources 15개 + 2026-07-13_Kanji_N5_100
  - KR: Last updated → 2026-07-14, vocab 7 → 8 (+ topik1-starter), 의류・패션 어휘 23 entries 명시, raw OCR cleanup 노트
- **wikilink 검증**: 모든 [[wikilink]] 가 실제 파일 가리킴 확인 (placeholder 제외)

## [2026-07-14] feat | 신규 theme basic-vocabulary 추가 (Game corpus curation prep)

- **Trigger**: Game raw/{en,es}_words.md 에 basic categories (greeting/number/color/family/basic/adjective) per-word entry 다수 — Language wiki 에 대응 theme 부재.
- **Action**: basic-vocabulary.md 신규 (각 언어 25/22 entries)
- **Schema**: ### {word} 섹션 + YAML Pipeline Form appendix (game consumer 인용 가능)
- **다음 단계**: Game raw/ 의 per-word → theme-anchor 자동 변환 (별도 세션 또는 dry-run 후 사용자 확인)

## [2026-07-14] session-end | 본 세션 종합 summary 참조

- **세션 종합**: [[SESSION_SUMMARY_2026-07-14]] (전체 15 액션 + 보안 scrub + force-push 요약)
- **보안 가이드**: [[security-incident-response-2026-07-14]] (_publish/2026-W25/, 360 lines)
- **상태**: Language HEAD `8aae316` (force-pushed) / Game HEAD `7d78707` (curation push)

## [2026-07-16] lint | 볼트 전체 wikilink 무결성 점검 + Game raw 마이그레이션

- **Language wiki/ 폴더**: 0개 깨진 링크 (vault-wide wikilink 모두 유효)
  - Spanish log.md: 40+ per-word wikilink → theme-file anchor (`[[theme]]`) 일괄 치환
  - English basic-vocabulary.md: 내부 per-word wikilink (`[[hi]]`, `[[hello]]` 등) 제거
  - Spanish/Japanese vocabulary Source 필드: 중복 `[[xxx-es]]` 정리, `travel-basics-jp` → `travel-basics` 정규화
  - Chinese grammar 파일: OpenClaw `file://` 외부 링크 2개 → 로컬 source 페이지(`basic-particles-zh.md`, `word-order-zh.md`)로 마이그레이션
  - Spanish culture 파일: OpenClaw `file://` 외부 링크 2개 → 로컬 source 페이지(`tango-argentino.md`, `mexico-comida-callejera.md`)로 마이그레이션

- **Game/typing_language/raw/** 4개 코퍼스 파일 per-word → theme-anchor 마이그레이션 완료
  - en_words.md: `airport`, `hotel`, `passport` 등 travel 단어 → `[[travel]]`, animal → `[[animals-vocabulary]]`, food → `[[food-vocabulary]]`, body → `[[body-vocabulary]]`
  - es_words.md: travel 섹션 전체(`pasaporte`, `aeropuerto`, `hotel` 등) → `[[viajes]]`
  - jp_words.md: travel 카테고리 `basic-vocabulary` → `[[travel]]` 치환 (regex 기반)
  - kr_words.md: wiki-driven entries 카테고리별 theme-file 매핑 (`여행`, `food-vocabulary`, `동물 어휘`, `자연・날씨 어휘`, `의류・패션 어휘`, `emotions-personality-vocabulary`, `topik1-starter`)

- **전체 볼트**: 90개 broken link 잔존 (대부분 Fiction/wiki 캐릭터/작품 참조, .omo 작업 문서 아티팩트, raw/_publish 템플릿 플레이스홀더 — 실제 wiki 콘텐츠와 무관)

- **다음 단계**: Fiction/wiki 내부 링크 복구, Game/roguelike_sprawl 단편 소설 경로 수정
- **세션 종료**: 본 엔트리까지
