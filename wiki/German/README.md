# German Wiki

> **상태**: 🟡 Scaffolded-only (ADR-0007, 2026-08-19)
> **언어**: German (Deutsch)
> **대상**: 5 main languages (EN/ES/JP/KR/ZH) 외 7번째 옵션
> **Promotion trigger**: 사용자가 `raw/German/` 에 source 파일 추가 시

## 현재 상태

| 영역 | 파일 | 비고 |
|---|---|---|
| vocabulary | 5 (basic / daily-life / food / travel / business) | theme-file (ADR-0001) |
| expressions | 1 (polite-expressions) | ADR-0001 정렬 |
| culture / grammar / sources / study-plan | 0 | 미정 |
| raw/ | 1 (README — Phase 16 seed attribution) | Goethe-Zertifikat A1 + Langenscheidt + DWDS + DZT |
| Pipeline Form YAML | 0% | raw 부재로 machine-readable 생성 불가 |

## ADR-0007 결정 (Option 2: Document)

German 위키는 의도적으로 **scaffolded-only** 상태로 유지됩니다. 자세한 사유:
- ADR-0002 의 "5언어 병렬" invariant 유지 (5 main langs: EN/ES/JP/KR/ZH)
- 사용자 raw 제공 시 즉시 promote 가능 (Option 1 으로 진화)
- 현재 우선순위는 5개 메인 언어 콘텐츠 깊이

## Promote 시 필요한 작업 (사용자 raw 제공 시)

1. **ADR-0008 (또는 ADR-0007 amendment) 작성** — German promote 결정
2. **ADR-0002 갱신** — 5언어 invariant → 7언어 (French/German 추가)
3. **raw/German/ 에 source 파일 추가** — textbook chapter, article, novel excerpt 등
4. **wiki/German/vocabulary/** 확장 — theme-file 신규 작성 (basic-vocabulary 외 4+ 파일)
5. **ADR-0003 Pipeline YAML** 생성 — `tools/generate_yaml_pipeline.py --lang de`
6. **ADR-0005 Expressions YAML** 생성 — `wiki/German/expressions/*.md`
7. **comparative/ German 컬럼 추가** — greetings, food, business 등 다국어 페이지
8. **`symmetry_check.py` main_langs 갱신** — German 추가

## 독일어 입력 방식 메모 (Promote 시 필요)

- 움라우트(`ä`, `ö`, `ü`)와 `ß` (Eszett / scharfes S) — DIN 5007 규약으로 ASCII 폴백 가능 (`ae`, `oe`, `ue`, `ss`)
- 합성어 (Komposita): 여러 명사를 결합 (Donaudampfschifffahrtsgesellschaftskapitän 등)
- 관사의 성 (Genus): der (m), die (f), das (n) — 모든 명사가 세 가지 성별 중 하나에 속함

## 관련 문서

- `../../decisions/0007-french-german-scaffolded-state.md` — ADR-0007 본문
- `../../raw/German/README.md` — Phase 16 seed attribution (Goethe-Zertifikat, Langenscheidt, DWDS, DZT)
- `../../tools/symmetry_check.py` — German 의 0% YAML 경고는 **known intentional**

## 다음 단계 (사용자 결정 시)

- Goethe-Zertifikat A2/B1 어휘 추가
- 독일 문학 발췌 (Goethe, Schiller, Kafka, Brecht)
- 독일 영화/TV 인용 (Tatort, Dark)
- 분리동사 (trennbare Verben) 문법 노트
- 격 변화표 (Deklination) / 동사 변화표 (Konjugation) grammar 페이지