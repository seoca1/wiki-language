# Language/raw/Chinese/ — README

> **상태 (status)**: 디렉토리 부재 — Chinese wiki 는 raw source 없이 인제스트 됨.

## 배경

`Language/raw/{English,Spanish,Japanese,Korean}/` 4개 언어 raw 는 모두 source-of-truth 자료 (교재, 기사, 원서) 가 `.md` 파일로 보존되어 있다. 반면 **Chinese raw 는 디렉토리 자체가 부재** (0 files) 인데, Chinese wiki (`wiki/Chinese/`) 는 27개 파일 (sources 8 + vocabulary 5 + expressions 4 + culture 4 + grammar 1 + study-plan README) 로 이미 인제스트 완료된 상태다.

## 워크플로 차이

다른 4개 언어 raw 는 다음 흐름을 따른다:
```
[교재·기사·원서 source]  →  Language/raw/{Lang}/{topic}.md  →  wiki/{Lang}/...
```

Chinese 는 다른 워크플로로 인제스트 되었다:
```
[외부 upstream source (web article / lesson platform / 교재 직접 인용)]
  ↓ 직접 인용 + 영어 summary 형태로 wiki/sources/{topic}-zh.md 작성
  ↓ raw 단계 생략
```

즉, Chinese source-summary 페이지 (`wiki/Chinese/sources/{topic}-zh.md`) 들은 다음을 자체 보유한다:
- `**Type:** lesson`
- `**Date Added:** 2026-07-13`
- `**Language Level:** beginner (HSK 1)`
- 영문 summary + Key Takeaways

raw 단계가 생략된 이유는 추정컨대:
1. Chinese source material 은 주로 web article / HSK 교재 직접 발췌 — copyright 민감
2. 2026-07-13 batch ingest 시 다른 4개 언어와 다른 파이프라인 사용 (lesson platform 기반)
3. 출처 URL/원문이 `.openclaw/workspace/wiki/chinese/` 어딘가에 보관되었을 가능성

## 향후 권고

| 옵션 | 설명 | trade-off |
|---|---|---|
| A. 그대로 유지 | wiki 가 self-contained, source citation 명확 | raw 단계 audit 시 Chinese 만 빈 셀 |
| B. `.openclaw/` 에서 raw 추출 | source-summary 의 upstream 원문/URL 채워서 `Language/raw/Chinese/{topic}.md` 신규 작성 | 시간/조사 비용 큼, 정확도 검증 필요 |
| C. 최소 placeholder | 본 README 만 두고 source-summary 페이지에 "원본 보존 위치: .openclaw/..." 주석 추가 | 간단, traceability 확보 |

현재 상태: **A** (그대로 유지). 추후 Chinese raw 보존 정책 결정 시 B 또는 C 채택.

## Source-summary 페이지 매핑

| Wiki source page | 추청 source type |
|---|---|
| `wiki/Chinese/sources/basic-particles-zh.md` | lesson (HSK 1 grammar) |
| `wiki/Chinese/sources/chinese-family-zh.md` | culture/lesson |
| `wiki/Chinese/sources/chinese-food-culture-zh.md` | culture/lesson |
| `wiki/Chinese/sources/daily-routine-zh.md` | lesson (vocabulary) |
| `wiki/Chinese/sources/greetings-zh.md` | lesson (HSK 1) |
| `wiki/Chinese/sources/pinyin-basics-zh.md` | lesson (pronunciation) |
| `wiki/Chinese/sources/tone-pairs-zh.md` | lesson (pronunciation) |
| `wiki/Chinese/sources/word-order-zh.md` | lesson (grammar) |

## 인용

- workspace `AGENTS.md` §2 ("raw/ - Immutable source materials organized by language") — Chinese 예외 케이스
- `Language/schema/AGENTS.md` L9 ("raw/ - Immutable source materials organized by language") — 동일 규약
- 2026-07-13 batch ingest 로그 (Chinese 예외 workflow)