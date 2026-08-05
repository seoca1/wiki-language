# Learning Activities — Historical Scripts

> **상태**: 2026 batch language learning activity scripts (one-off tools).
> 더 이상 active development 도중이 아니며, 신규 vocabulary ingest / learning flow 구현 시 참고용으로 보존됨.

## 배경

2026 Language learning session 들에서 사용된 일회성 학습 활동 스크립트들. 각 스크립트는 특정 학습 활동의 prototype 으로 개발되었으나, 정식 Language 프로젝트 표준 워크플로에 편입되지 않은 채 workspace `scripts/` 에 누적되어 있었음.

본 디렉토리로 이동 정리:
- 신규 ingest 시 vocabulary card extraction 패턴 참조
- 향후 learning activity prototype 구현 시 출발점

## 스크립트 분류

### Quiz / 학습 활동 (`quiz-*`, `cl-*`, `vocab-*`)

| 파일 | 용도 |
|---|---|
| `cl-quiz-gen.py` | Cross-language quiz generation (EN ↔ ES ↔ JP ↔ KR ↔ CH) |
| `quiz-gen-v3.py` | Quiz generation v3 — theme-based vocabulary test |
| `quiz-realtime.py` | Real-time quiz analytics dashboard |
| `vocab-quiz-system.py` | Vocabulary quiz system — SRS-style scheduling |
| `mastery-tracker.py` | Vocabulary mastery tracker — spaced repetition |
| `review-scheduler.py` | Review scheduling algorithm |
| `native-lang-support.py` | Native language UI support |

### 진행 / 분석 (`*-progress-*`, `*-analytics`)

| 파일 | 용도 |
|---|---|
| `activity-analytics.py` | Activity log 분석 |
| `content-stats-v2.py` | Content statistics v2 |
| `progress-tracker.py` | Overall learning progress tracking |
| `fed-learning-session.py` | Federated learning session manager |
| `fed-progress-v2.py` | Federated progress aggregation v2 |

### 발음 / 음성 (`*pron*`, `voice*`)

| 파일 | 용도 |
|---|---|
| `ai-pron-scorer.py` | AI pronunciation scoring |
| `pronunciation-feedback.py` | Pronunciation feedback generation |
| `voice-interface.py` | Voice-based learning interface |

### Personal / Reports (`*personal*`, `*report*`)

| 파일 | 용도 |
|---|---|
| `personal-collector.py` | Personal vocabulary collector |
| `search-history.py` | Search history analytics |
| `realtime-tm.py` | Real-time text-meaning lookups |
| `final-280-report.py` | Final report generation (Day 280 milestone) |
| `final-290-report.py` | Final report generation (Day 290 milestone) |

### CI / Shell

| 파일 | 용도 |
|---|---|
| `ci_local.sh` | Local CI runner shell script |

## 통합 후보

다음 스크립트들은 향후 Language 학습 시스템 정식 기능으로 통합 가능:
- `mastery-tracker.py` (SRS 로 통합)
- `review-scheduler.py` (SRS scheduler 로 통합)
- `cl-quiz-gen.py` (cross-language quiz generator)

## 제외 (roguelike_sprawl 전용)

다음 스크립트는 roguelike_sprawl 게임 audio 진단 전용이므로 `Game/roguelike_sprawl/scripts/` 에 위치 (2026-08-05 이동, 이전 workspace `scripts/` → 프로젝트 scripts/):
- `audio-doctor.py` (7 refs)
- `verify_sounds.py` (9 refs)

## 인용

- workspace `AGENTS.md` §6 (cross-project dependencies) — Language ↔ Game roguelike_sprawl 흐름
- `Language/schema/AGENTS.md` §3 (ingest workflow)
- `Language/log.md` §historical ingest sessions (2026-07 batch)
