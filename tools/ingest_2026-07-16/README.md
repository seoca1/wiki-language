# Ingest 2026-07-16 — Historical Vocabulary Conversion Scripts

> **상태**: 일회성 vocabulary 변환 batch (2026-07-16). 더 이상 active 사용 안 함.
> 변환 대상은 이미 완료되어 `Language/wiki/{Lang}/vocabulary/` 에 theme file 형식으로 보존됨.

## 배경

2026-07-16 batch ingest 시, EN/JP/ES 어휘 자료가 **table format** (markdown table with `| 한글 | 로마자 | 의미 |`) 으로 존재했음. 이를 `Language/schema/AGENTS.md` 의 vocabulary 페이지 표준 형식 (theme-file + `### {word}` sections + YAML pipeline form) 으로 변환할 필요가 있었음.

`Language/wiki/{Lang}/vocabulary/table-format/` 디렉토리에 있던 table-format 어휘 파일들을 일괄 변환하여 표준 형식으로 재저장.

## 스크립트 목록

| 파일 | 언어 | 변환 대상 |
|---|---|---|
| `convert_english_vocab.py` | EN | table-format → theme-file |
| `convert_japanese_vocab.py` | JP | table-format → theme-file |
| `convert_japanese_vocab_section.py` | JP | 섹션 분리 variant |
| `convert_spanish_vocab.py` | ES | table-format → theme-file (v1) |
| `convert_spanish_vocab_v2.py` | ES | v2 (column mapping fix) |
| `convert_spanish_vocab_v3.py` | ES | v3 (final) |
| `convert_vocab_to_full_format.py` | generic | 공통 변환 로직 (POS hints, category mapping) |
| `enhance_spanish_vocab.py` | ES | 추가 enhancement (examples 보강) |

## 사용법 (참고용)

```bash
# 변환 실행 (이미 완료된 상태이므로 재실행 시 idempotent)
python3 Language/tools/ingest_2026-07-16/convert_english_vocab.py
python3 Language/tools/ingest_2026-07-16/convert_vocab_to_full_format.py
```

## 현재 상태

- **변환 결과**: `Language/wiki/English/vocabulary/`, `Language/wiki/Japanese/vocabulary/`, `Language/wiki/Spanish/vocabulary/` 에 표준 형식으로 저장됨
- **재실행 필요성**: 없음 (table-format 소스 파일은 이미 제거됨)
- **보존**: 향후 table-format 자료 재수신 시 (e.g., 신규 교재 ingest) 재사용 가능

## 검증

- 2026-07-19 vault lint: 0 broken wikilinks
- 2026-07-28 Spanish vocab 100% filled: 206/206 entries complete
- 모든 vocabulary theme file 이 `Language/schema/AGENTS.md` §페이지 형식 표준 준수

## 인용

- workspace `AGENTS.md` §5 (log 기록) — 본 batch 후 log 갱신 완료
- `Language/log.md` §5 (vocabulary 정규화 batch)
