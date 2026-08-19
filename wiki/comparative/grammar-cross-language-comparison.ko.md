# 문법 5언어 비교 — Cross-Language Comparison (한국어판)

> 원본: [[grammar-cross-language-comparison]] (English) | 작성일: 2026-08-19 | ADR-0006
> **5개 언어 문법 구조 비교** — English · Spanish · Japanese · Korean · Chinese

---

## 빠른 참조 표

| 기능 | English | Spanish | Japanese | Korean | Chinese |
|---------|---------|---------|----------|--------|---------|
| **어순** | SVO | SVO | SOV | SOV | SVO |
| **시제 표지** | 형태적 (eat/ate) | 형태적 (-é/-ió) | 형태적 (た形) | 형태적 (았/었) | 상(相) 조사 (了/过) |
| **상 시스템** | 진행 (-ing), 완료 (have+V-ed) | 진행 (-ndo), 완료 (-ado) | -te iru (진행), -te shimau (완료) | -고 있다 (진행), -아/어 있다 (상태) | 着 (진행), 了 (완료), 过 (경험) |
| **관사** | a / an / the | el / la / un / una | 없음 | 없음 | 없음 |
| **성** | 없음 (자연 성별) | 남성 / 여성 | 없음 | 없음 | 없음 |
| **동사 격식** | 없음 | 제한적 (usted 동사 형태) | 완전 시스템 (keigo) | 완전 시스템 (합쇼체/해요체) | 없음 |
| **복수 표지** | -s (규칙) | -s/-es | 복수화 たち (tachi) 선택 | 복수화 들 (deul) 선택 | 없음 (맥락) |
| **의문문 표지** | 도치 / 상승 억양 | ¿...? + 도치 | か (ka) | 까? (kka?) / 니? (ni?) | 吗 (ma) |
| **부정** | don't / not | no / -ar/-er/-ir 변화 | ない (nai) / ません (masen) | 안 (an) / -지 않다 (-ji anhda) | 不 (bù) / 没 (méi) |
| **대명사 생략** | 필수 | 필수 | 흔함 (영대명사) | 흔함 | 흔함 |

---

## 어순 상세

| 어순 | 언어 | 예시 |
|-------|-----------|---------|
| **SVO (주어-동사-목적어)** | English, Spanish, Chinese | "I eat apples." / "Como manzanas." / "我吃苹果。" |
| **SOV (주어-목적어-동사)** | Japanese, Korean | "私はりんごを食べる" (Watashi wa ringo o taberu) / "나는 사과를 먹다" (Naneun sagwa-reul meokda) |

### 한국어 화자에 대한 시사점

한국어는 **SOV 어순** + 다양한 조사 활용 → 일본어 와 매우 유사한 구조. 영어/스페인어/중국어 (SVO) 학습 시 동사 위치 변경 필요.

---

## 시제 vs 상(相)

| 개념 | English | Spanish | Japanese | Korean | Chinese |
|---------|---------|---------|----------|--------|---------|
| **단순 과거** | ate | comí | 食べた (tabeta) | 먹었다 (meogeotda) | 吃了 (chī le) |
| **현재 진행** | is eating | está comiendo | 食べている (tabete iru) | 먹고 있다 (meokgo itda) | 吃着 (chī zhe) |
| **경험** | have eaten | he comido | 食べたことがある (koto ga aru) | 먹어 본 적 있다 (meogeo bon jeok itda) | 吃过 (chī guò) |
| **미래** | will eat | comerá | 食べるだろう (darō) | 먹을 것이다 (meogeul geosida) | 会吃 (huì chī) |

### 한국어 화자에 대한 시사점

- 한국어 시제: 과거/현재/미래 3단계 — 영어 시제와 유사.
- 일본어 시제: 과거/비과거 2단계 — 영어/한국어보다 단순.
- 중국어: **시제 없음**, 상(相) 조사 사용 — 영어/일본어/한국어와 매우 다른 시스템.

---

## 관사 & 한정사

| 유형 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **정관사** | the | el / la | (없음) | (없음; 그 "geu") | (없음; 这 "zhè") |
| **불완정 관사** | a / an | un / una | (없음) | (없음; 한 "han") | (없음) |
| **지시** | this / that | este / ese | これ / それ (kore/sore) | 이 / 그 (i/geu) | 这 / 那 (zhè/nà) |
| **소유** | my, your, his | mi, tu, su | 私の (watashi no) | 나의 (na-ui) | 我的 (wǒ de) |

### 한국어 화자에 대한 시사점

- 한국어에 관사 없음 → 영어/스페인어 학습 시 "a/the" 필수 사용 학습.
- 스페인어 정관사 4형태 (el/los/la/las) + 불완정 관사 4형태 (un/unos/una/unas) — 한국어 학습자에게 매우 낯설.
- 중국어/일본어도 관사 없음 → 3개 언어 모두 관사 결여.

---

## 언어별 상세

### 🇬🇧 영어 (English)
- **핵심 용어**: SVO, 관사 (a/an/the), 시제-상, do-support
- **패턴**: 시제 의무; 단수 가산 명사에 관사 필수
- **출처**: `[[grammar-overview]]`

### 🇪🇸 스페인어 (Spanish)
- **핵심 용어**: SVO, 성 일치, ser vs estar, 가정법 (subjuntivo)
- **패턴**: 동사가 인칭/수에 따라 활용; 가정법 = 의문/욕구/감정
- **지역 변이**: Voseo (Rioplatense); Vosotros (스페인) vs ustedes (라틴아메리카)
- **출처**: `[[grammar-overview]]`

### 🇯🇵 일본어 (Japanese)
- **핵심 용어**: SOV, 조사 (は/が/を/に/で/へ), keigo
- **패턴**: 화제-주석 (は/가); 동사 항상 마지막
- **Keigo / 경어**: 尊敬語 (존경), 謙譲語 (겸양), 丁寧語 (정중)
- **출처**: `[[grammar-overview]]`

### 🇰🇷 한국어 (Korean)
- **핵심 용어**: SOV, 조사 (은/는/이/가/를/을), 말투 단계
- **패턴**: 화제 는/은, 주어 가/이; 동사 항상 마지막
- **말투 단계**: 합쇼체 격식 / 해요체 정중 / 해체 비격식 / 하소서체 문어
- **출처**: `[[grammar-overview]]`

### 🇨🇳 중국어 (Chinese)
- **핵심 용어**: SVO, 상(相) 조사 (了/过/着), 양사
- **패턴**: 동사 활용 없음; 상(相) 조사가 시간 경과 표지
- **격식 / 존경**: 您 (nín) 존경; 양사 필수 (个/本/杯/张)
- **출처**: `[[grammar-overview-zh]]`

---

## 핵심 대조 (종합)

| 대조 | 학습자 시사점 |
|------|----------------|
| **어순 계열** | EN/ES/CH = SVO; JP/KR = SOV. SOV 학습자는 JP/KR 직접 매핑 가능 |
| **관사** | EN/ES는 가산 명사에 관사 필수; JP/KR/CH 없음 |
| **격식 깊이** | JP/KR는 동사 기반 완전 격식 시스템; EN/ES/CH는 대명사/어휘 의존 |
| **시제 vs 상** | EN/ES는 형태적 시제; CH는 상(相) 조사; JP/KR은 혼합 |

---

## 학습자 의사결정 가이드

- **마스터해야 할 첫 10 문법 개념**:
  - EN: SVO word order, articles (a/an/the), present tense, past tense (-ed), future (will), do-support, question inversion, negation (don't), progressive (-ing), plural (-s)
  - ES: SVO, ser/estar, gender agreement (el/la), present tense (-ar/-er/-ir), subjunctive, vosotros vs ustedes, negative (no), reflexive (se), preterite vs imperfect, conditional
  - JP: SOV, particles (は/が/を/に), verb groups (Group 1/2), te-form, past tense (た形), keigo, counters, negative (ない), conditional (ば/たら), honorific verbs (いらっしゃる/おっしゃる)
  - KR: SOV, particles (은/는/이/가/을/를), speech levels (합쇼체/해요체), past tense (았/었), future (겠), honorific (시/으시), counters, negation (안/-지 않다), causative (-게), passive (-아지다)
  - CH: SVO, aspect particles (了/过/着), measure words (个/本/杯/张), tones (4), A-not-A questions, ba-sentences (把), bei-sentences (被), comparison (比), modal particles (吧/呢/吗)

---

## 🇰🇷 한국어 학습자 노트 (Korean Learner Notes)

> 본 섹션은 한국어 학습자 대상의 추가 학습 가이드입니다.

### 한국어 화자가 다른 4개 언어 문법을 배울 때 흔히 마주치는 함정

1. **시제 vs 상(相) 의 시스템 차이**:
   - 한국어는 시제 3단계 (과거/현재/미래) — 영어/스페인어와 유사. 그러나 중국어는 시제 없음, 상(相) 조사 (了/过/着) 사용.
   - **함정**: 한국어 학습자가 중국어 회화에서 "昨天吃了" 의 "吃了" 를 단순 과거 → 사실 "了" 는 완료 상(相) 표지, 과거 시제가 아님. 미래/반복도 상(相) 으로 표현.
   - **훈련법**: 시제 vs 상(相) 매트릭스 — — 한국어 시제 → 영어 시제 → 스페인어 시제 → 일본어 시제 → 중국어 상(相) 조사. 중국어 학습 시 시제 변환 의식.

2. **관사의 부재 vs 존재**:
   - 한국어에는 관사 없음 ("I saw **a cat**" → "고양이를 봤어" - a 없음). 그러나 영어/스페인어는 필수.
   - **함정**: 한국어 학습자가 영어에서 "I saw cat" 처럼 관사 생략 → 매우 부자연스러움. 스페인어에서도 마찬가지 ("Vi gato" ✗).
   - **훈련법**: 관사 필수 매트릭스 — EN a/the 필수 / ES el/la/un/una 필수 / JP/KR/CH 없음. 영어 학습 시 모든 가산 명사에 관사 의식.

3. **부정 부호의 위치**:
   - 한국어 "안 먹어요" = 부사 안 + 동사 → 부사 위치. 영어 "don't eat" = 도치 보조. 스페인어 "no come" = 부사 위치. 일본어 食べない = 어미 변화. 중국어 不吃 / 没吃 = 부사 위치.
   - **함정**: 한국어 학습자가 일본어 부정 "食べない" 를 "食べあん" 으로 단순 부사 추가 → 사실 어미 -nai 가 동사에 결합.
   - **훈련법**: 부정 부호 위치 매트릭스 — KR 안+동사 / EN do+not+V / ES no+V / JP V+nai / CH 不+ V. 5개 언어 부정 위치 차이 학습.

4. **시제 표현의 일본어 vs 영어 차이**:
   - 한국어 학습자가 일본어 학습 시 가장 혼란: 일본어 는 과거/비과거 2단계 (食べた vs 食べる) — 한국어 과거/현재/미래 3단계보다 단순.
   - **함정**: "I have eaten" (영어 현재완료) → 일본어 "食べた" (단순 과거) 와 매핑이 매우 까다로움. "내일 먹었어" 같은 모순 표현 회피.
   - **훈련법**: 시제 단순화 — — JP 과거(た形) = KR 과거(았/었) + 단순화. EN 현재완료 vs JP 과거 의 차이 (현재완료 = 경험/결과, JP 과거 = 단순 과거).

5. **조사의 차이**:
   - 한국어 조사 (은/는/이/가/을/를/에/에서/와/의) vs 일본어 조사 (は/が/を/に/で/へ/の/と) vs 중국어 없음/介词 (在/从/跟) vs 영어 전치사.
   - **함정**: 한국어 학습자가 일본어 에서 -을/를 → 을 (o) 로 단순 매핑 → 사실 은/는 vs は/가 의 미묘한 차이 있음.
   - **훈련법**: 조사 비교 매트릭스 — — KR 은/는/이/가/을/를 vs JP は/が/を + 차이점 학습. 중국어介词 vs 영어 전치사 와의 차이.

### 학습 전략

1. **우선순위 1**: 한국어 문법 시스템 (SOV + 조사 + 말투 + 시제) 마스터 — 다른 4개 언어 학습의 토대.
2. **우선순위 2**: 어순 비교 (SOV ↔ SVO) 자동화 — 영어/스페인어/중국어 학습 시 필수.
3. **우선순위 3**: 시제 시스템 5언어 매핑 — 한국어 3단계 vs 영어/스페인어 시제 vs 일본어 2단계 vs 중국어 상(相).
4. **우선순위 4**: 조사 vs 전치사 — 한국어 조사 vs 일본어 조사 vs 영어 전치사 vs 중국어 介词 비교.
5. **우선순위 5**: 격식 시스템 — 한국어 합쇼체 vs 일본어 keigo vs 스페인어 usted vs 중국어 您.

---

## 관련 페이지

- `[[grammar-difficulty-map]]` — 기능별 난이도 순위
- `[[tense-aspect-systems]]` — 시제 vs 상(相) 심층 분석
- `[[politeness-honorifics]]` — 완전 keigo / 말투 시스템
- `[[mood-systems]]` — 직설법 vs 가정법
- `[[pronouns-reference]]` — 대명사 시스템과 영대명사

## 출처

- 영어: `[[grammar-overview]]`
- 스페인어: `[[grammar-overview]]`
- 일본어: `[[grammar-overview]]`
- 한국어: `[[grammar-overview]]`
- 중국어: `[[grammar-overview-zh]]`

---

**원본 (영어)**: [[grammar-cross-language-comparison]] | **관련 미러**: [[grammar-cross-language-comparison.es|Spanish]] · [[grammar-cross-language-comparison.ja|Japanese]] · [[grammar-cross-language-comparison.zh|Chinese]] | **정책**: ADR-0006