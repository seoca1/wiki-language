# Language/raw/Chinese/ — README

> **상태 (status)**: 25+ historical files + Option B policy (effective 2026-08-20)
> **Canonical source for NEW Chinese content**: `.openclaw/workspace/wiki/chinese/`
> **Policy decision**: `Language/decisions/README.md` §향후 결정 후보 — "RESOLVED 2026-08-20 (Option B)"

## 배경 (Background)

`Language/raw/{English,Spanish,Japanese,Korean}/` 4개 언어 raw 는 모두 source-of-truth 자료 (교재, 기사, 원서) 가 `.md` 파일로 보존되어 있다. `Language/raw/Chinese/` 는 2026-07-13 batch ingest 시점에 다른 4개 언어와 다른 파이프라인으로 인제스트 되었다 — 일부 파일은 직접 작성, 일부는 OpenClaw 추출 mirror.

## Option B Policy (effective 2026-08-20)

NEW Chinese content 의 canonical source 는 OpenClaw runtime 이다:

```
[외부 source (web article / HSK 교재 / lesson platform)]
  ↓ OpenClaw runtime 자동 추출
.openclaw/workspace/wiki/chinese/{culture,grammar,lessons,vocabulary}/
  ↓ OpenClaw pipeline mirror
wiki/Chinese/...
```

`Language/raw/Chinese/` 의 역할:
- **Historical content** 보존 (25+ files, 2026-07-13 batch)
- **Direct user-provided raw materials** (예: 사용자가 직접 붙여넣은 HSK 교재 발췌, 여행 raw)
- **OpenClaw 가 추출하지 못한 특수 source** (예: 비공개 lesson platform)

`Language/raw/Chinese/` 가 canonical 이 **아닌** 이유:
- workspace §1 의 "`.openclaw/workspace/wiki/ — Foreign Language Wiki 외부 작업공간 (OpenClaw 런타임, Language 위키 미러)" 정의에 따라 OpenClaw 가 canonical
- 다른 4개 언어와 다른 governance (raw 직접 작성 vs OpenClaw 추출) 통일
- 5언어 平行 구조 (ADR-0002) 의 architectural consistency

## Historical content (25+ files, 2026-07-13 batch)

| File pattern | Count | Source type |
|---|---:|---|
| `*-zh.md` (body, food, family, ...) | 24 | 직접 작성 / lesson platform 발췌 |
| `first-travel-china.md` | 1 | user-provided travel raw (76KB) |
| `README.md` | 1 | 본 문서 |

각 파일의 source citation 은 `wiki/Chinese/sources/{topic}-zh.md` 의 frontmatter (`**Type:**`, `**Date Added:**`, `**Language Level:**`) 참조.

## OpenClaw canonical source reference

| File / directory | Purpose |
|---|---|
| `.openclaw/workspace/wiki/chinese/_Chinese_MOC.md` | Chinese MOC (Map of Content) |
| `.openclaw/workspace/wiki/chinese/_exposure_log.md` | Daily exposure tracking |
| `.openclaw/workspace/wiki/chinese/culture/` | Culture extraction target |
| `.openclaw/workspace/wiki/chinese/grammar/` | Grammar extraction target |
| `.openclaw/workspace/wiki/chinese/lessons/` | HSK lesson extraction target |
| `.openclaw/workspace/wiki/chinese/vocabulary/` | Vocabulary extraction target |

**Note**: `.openclaw/workspace/wiki/` 는 OpenClaw runtime mirror 이므로 AI 직접 수정 금지. 본 README 는 `.openclaw/` 가 canonical 임을 document 만 할 뿐, `.openclaw/` 자체에 변경을 가하지 않는다.

## See also

- `.openclaw/workspace/wiki/chinese/_Chinese_MOC.md` — Chinese MOC
- `wiki/Chinese/index.md` — Language wiki index
- `Language/decisions/README.md` — Option B resolution entry
- `Language/decisions/0002-5-language-parallel-structure.md` — 5언어 平行 구조 (Chinese raw Option A exception 과 정렬)
- workspace `AGENTS.md` §1 — `.openclaw/workspace/wiki/` canonical 정의

## 변경 이력

- 2026-07-13: 디렉토리 초기 배치 (25+ files, batch ingest)
- 2026-08-20: Option B policy effective — `.openclaw/` 가 canonical source 임을 document. 기존 "디렉토리 부재" 잘못된 표현 제거.