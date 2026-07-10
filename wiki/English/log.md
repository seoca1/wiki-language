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
