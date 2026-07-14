# Chinese Learning - Activity Log

## [2026-07-13] scaffold | Chinese(zh) wiki 초기 스캐폴드 생성

- Language vault 5번째 언어 스캐폴드 생성: `wiki/Chinese/` (English/Japanese/Korean/Spanish 이후)
- 디렉터리 5개: vocabulary / expressions / culture / sources / study-plan
- 파일 7개:
  - `wiki/Chinese/index.md` (4 standard sections: Vocabulary / Expressions / Culture / Sources, 5th language 노트 포함)
  - `wiki/Chinese/log.md` (본 로그)
  - `wiki/Chinese/vocabulary/.gitkeep`
  - `wiki/Chinese/expressions/.gitkeep`
  - `wiki/Chinese/culture/.gitkeep`
  - `wiki/Chinese/sources/.gitkeep`
  - `wiki/Chinese/study-plan/README.md` (스키마 충족용 stub)
- 컨벤션 적용:
  - theme-file convention (per-word / per-expression `.md` 금지) — schema/AGENTS.md 및 2026-07-10 lint 세션 원칙
  - Pipeline Form YAML 부록 예정 (todo 12 이후 인제스트 시)
  - raw/ 는 read-only (현재 raw/Chinese/ 비어있음)
- 크로스 프로젝트 노트:
  - `.openclaw/workspace/wiki/Chinese/` 와 분리 — OpenClaw 런타임 작업공간은 별도
  - 게임 (`Game/typing_language/`) 측 중국어 프로필/코퍼스는 추후 별도 태스크

## 다음 단계

- todo 12: 첫 출처 raw 인제스트 (예: HSK 1 단어장 / 기초 회화 / 중국 음식 어휘 등)
- todo 이후: `wiki/Chinese/vocabulary/{theme}.md` 페이지 시드 + Pipeline Form YAML 부착
- ADR (필요 시): 중국어 입력 방식 결정 (병음 입력 / 주음부호 / 한자 직입력)
- 결정 후 `Game/typing_language/wiki/languages/chinese.md` 작성
- 결정 후 `Game/typing_language/raw/zh_words.md` 골격 작성

## [2026-07-13] ingest | OpenClaw Chinese wiki 흡수 (4 sources + 5 vocab themes)

- 첫 번째 인제스트: `.openclaw/workspace/wiki/chinese/` 의 lesson 4개 + vocabulary 5개를 vault 내 `wiki/Chinese/` 로 흡수.
- **변경 파일 11개:**
  - `wiki/Chinese/sources/pinyin-basics-zh.md` (40 lines) — Source Summary format 적용, [[numbers-zh]] [[body-zh]] [[family-zh]] [[colors-zh]] 어휘 앵커 포함.
  - `wiki/Chinese/sources/tone-pairs-zh.md` (40 lines) — 성조 변화 규칙 (3+3, 一, 不) 요약.
  - `wiki/Chinese/sources/greetings-zh.md` (41 lines) — 인사 20개 + 是 (shì) 자기소개 패턴.
  - `wiki/Chinese/sources/daily-routine-zh.md` (41 lines) — 시간 + 동사 패턴 + 17 routine verbs.
  - `wiki/Chinese/vocabulary/body-zh.md` (314 lines, 11 words) — 신체 부위.
  - `wiki/Chinese/vocabulary/colors-zh.md` (302 lines, 11 words) — 색깔.
  - `wiki/Chinese/vocabulary/family-zh.md` (301 lines, 11 words) — 가족 호칭.
  - `wiki/Chinese/vocabulary/vocabulary/measure-words-zh.md` (302 lines, 11 words) — 양사.
  - `wiki/Chinese/vocabulary/numbers-zh.md` (335 lines, 12 words) — 숫자.
  - `wiki/Chinese/index.md` — Vocabulary section (0→5 themes), Sources section (0→4 sources), Last updated 갱신.
  - `wiki/Chinese/log.md` — 본 entry append.
- **컨벤션 적용:**
  - 모든 vocab 파일에 `### {word}` 섹션 + 5-field YAML (id/display/input/meaning/level/category/source) Pipeline Form 부록.
  - 모든 source 파일에 Source Summary format (Type / Date Added / Language Level + Summary / Key Takeaways / Vocabulary Extracted / Expressions Extracted / Cultural Insights / Notes) 적용.
  - Vault theme anchor 사용: `[[body-zh]]`, `[[numbers-zh]]`, etc.
  - Pinyin 표기 보존: OpenClaw 원본의 tone mark 표기 유지, YAML input 필드는 번호형으로 변환 (게임 파이프라인 호환).
- **크로스 프로젝트 노트:**
  - `.openclaw/workspace/wiki/chinese/` 원본은 절대 수정하지 않음.
  - 다른 언어 wiki (English/Japanese/Korean/Spanish) 미수정.
  - 게임 측 `Game/typing_language/raw/zh_words.md` 파이프라인은 추후 별도 태스크 (현재 task는 wiki side 만 완료).

## [2026-07-13] ingest | Chinese grammar 2 entries | basic-particles + word-order

- **신규 파일**:
  - `wiki/Chinese/grammar/basic-particles.md` (의/료/재/有 4종 조사, 330줄 원본 기반)
  - `wiki/Chinese/grammar/word-order.md` (SVO 어순, 338줄 원본 기반)
- **Source**: `.openclaw/workspace/wiki/chinese/grammar/` (외부 작업공간)
- **Level**: HSK 1-2 (Beginner)
- **구조**:
  - 한국어 요약 (Korean Summary) — 5-6 핵심 포인트 + 한국 한자음 ≠ 중국 병음 warning
  - 조사/어순 규칙 + 사용 패턴 (한국어 vs 중국어 비교 표)
  - 자주 하는 실수 5가지 (한국어 학습자 관점)
  - 단계별 학습법 (Level 1~5 / 1~4)
  - 실전 회화 / 30 실전 문장
  - Sources (원본 .openclaw 경로 + 직접 링크) / Related (다른 wiki 페이지)
- **cross-references**:
  - basic-particles ↔ word-order (서로 링크)
  - both → pinyin-basics-zh, daily-routine-zh, greetings-zh, family-zh
- **wiki/Chinese/grammar/** 디렉토리 최초 생성
- **인덱스 갱신**: Chinese index.md 에 Grammar (2 entries) 섹션 추가, Last updated 갱신
