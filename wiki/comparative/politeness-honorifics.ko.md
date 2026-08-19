# 공손 & 경어 — 다국어 비교 (한국어판)

> 원본: [[politeness-honorifics]] (English) | 작성일: 2026-08-20 | ADR-0006
> **5개 언어 공손 & 경어 시스템 전체 비교**

---

## 빠른 참조 표

| 기능 | English | Spanish | Japanese | Korean | Chinese |
|---------|---------|---------|----------|--------|---------|
| **문법적 인코딩** | 어휘 선택만 | 대명사 (tú/usted) + 동사 형태 | 동사 형태 (keigo) + 어휘 | 동사 어미 (경어 단계) + 경어 명사/동사 | 어휘 선택 + 경어 호칭 + 您 (nín) |
| **단계 수** | 2-3 (격식/중립/캐주얼) | 2-3 (tú/usted/vosotros) | 3-4 (캐주얼/정중/경어/겸양) | 4-6 (해체/해요체/합쇼체/하소서체 + 혼합) | 2-3 (중립/您/경어 호칭) |
| **대명사 구분** | you (보편) | tú / usted / vosotros / ustedes | あなた / 君 / お前 / 貴方 (종종 생략) | 너 / 당신 / 선생님/님 (회피) | 你 / 您 / 诸位 / 先生/女士 |
| **동사 형태 변화** | 아니오 | 예 (2인칭/3인칭) | 예 (광범위) | 예 (광범위) | 최소 (일부 suppletive 형태) |
| **경어 어휘** | 제한적 (sir/ma'am, 호칭) | Don/Doña, usted 형태 | 尊敬語 / 謙譲語 / 丁寧語 | 존댓말 / 높임말 (특수 동사/명사) | 尊称, 敬语 (您, 贵姓, 등) |
| **상대 지위** | 맥락 의존 | 예 (나이, 친밀) | 중심 (내/외) | 중심 (나이, 위계) | 중심 (나이, 위계, 關係) |
| **내 그룹 vs 외 그룹** | 약함 | 중립 (usted default out-group) | 근본 (내/외) | 근본 (내사람/남) | 근본 (自己人/外人) |

---

## 핵심 대조 (종합)

| 대조 | 학습자 함의 |
|----------|--------------------------|
| **문법적 vs 어휘적** — JP/KR/ES는 문법에 공손 인코딩; EN/CH는 어휘 사용 | JP/KR 학습자는 동사 패러다임 조기 마스터 필수; EN/CH 학습자는 기본 문법 + 공손 어휘로 가능 |
| **기본 타인 등록** — ES: *usted* (LatAm) / *tú* (Spain 청년); JP: *desu/masu*; KR: *haeyoche*; CH: *nín* + 호칭 | 타겟 지역별 기본 선택: Mexico → *usted*; Tokyo → *desu/masu*; Seoul → *haeyoche*; Beijing → *nín* + 호칭 |
| **내/외 그룹 (uchi/soto, 내사람/남)** — JP/KR에 중심; EN 약함; ES/CH 중립 | JP/KR에서 잘못된 등록은 내 그룹에 차갑게, 외 그룹에 무례. 그룹 경계 먼저 학습. |
| **나이 vs 호칭 기반** — KR/CH 호칭+님/先生 필수; JP -san/様; ES Don/Doña + usted; EN Mr/Ms | KR/CH에서 직함 없이 이름 = 무례. 모든 역할 호칭 암기 (팀장님, 王老师, 部長様, Don Juan) |
| **등록 협상** — KR 명시적 ("우리 반말 해요"); JP 암묵적 (keigo drop); ES 명시적 ("tuteame"); CH 암묵적 (您 drop) | KR 학습자: "언제 반말 할까요?" 스크립트 연습. JP 학습자: keigo drop 신호 주시. ES 학습자: "¿Puedo tutearte?" |

---

## 학습자 의사결정 가이드

> **목표별 우선순위**:
> - **생존/여행**:
>   - EN: "Please/Thank you/Excuse me" + 양태 동사
>   - ES: *usted* 형태 + *por favor/gracias* (어디서나 통용)
>   - JP: *desu/masu* + *sumimasen/arigatou* (90% 상호작용 커버)
>   - KR: *haeyoche* (-요 어미) + *juseyo/mianhamnida* (안전한 기본)
>   - CH: *nín* + *qing/xiexie/duibuqi* + 호칭 (服务员, 师傅)
> - **비즈니스**:
>   - EN: 헷징, 수동태, "I would appreciate," 호칭
>   - ES: *ustedeo* + *usted* 동사 형태 + *Don/Doña* + 격식 클로징 (*Atentamente, Cordialmente*)
>   - JP: 전체 *keigo* (sonkeigo/kenjougo/bikago) + *keigo* 이메일 템플릿 + *meishi* 교환 에티켓
>   - KR: *hapsyoche* (-ㅂ니다) + 경어 명사/동사 + 호칭+님 + 절 깊이
>   - CH: *nín* + 贵姓/请教/拜访 + 호칭 (总监, 经理, 老师) + 请/麻烦您
> - **사교/연애/친구**:
>   - EN: 이름 기반 빠름, 구동사, 슬랭
>   - ES: *tuteo* 협상 (*¿Puedo tutearte?*) → 지역 규범 다양
>   - JP: *tameguchi* 전환 (보통 3번째 만남 / 음주 후) — 연장자가 제안할 때까지 대기
>   - KR: *banmal* 협상 (*우리 반말 해요*) — 보통 어린 사람이 연장자에게 친밀 형성 후 제안
>   - CH: *nín* drop → *nǐ*, given name / nickname / 哥/姐 — *guanxi* 심화에 따름
> - **학술/격식 문어**:
>   - EN: 수동태, 명사화, 헷징, 인용 스타일
>   - ES: *ustedeo*, 비인칭 *se*, 격식 문맥 가정법
>   - JP: *dearu/da* (plain) 논문; *desu/masu* 프레젠테이션; *kanbun* 레거시 형태
>   - KR: *hapsyoche* + 경어 + 한자어 (한자어)
>   - CH: 문어 등록 (书面语) — 之/其/乃/乎, 4자 성어, 수동태 被/由

---

## 🇰🇷 한국어 학습자 노트 (Korean Learner Notes)

> 본 섹션은 한국어 학습자 대상의 추가 학습 가이드입니다.

### 한국어 화자가 다른 4개 언어 공손/경어 시스템을 학습할 때 흔히 마주치는 함정

1. **한국어 경어 6단계 vs 다른 4개 언어 2-3단계의 정밀도 차이**:
   - 한국어 공손: 하소서체/합쇼체/해요체/해체/반말 + 존경/겸양/평어 = **6-12단계** 가능. 가장 세밀한 시스템.
   - 영어 2-3단계 (formal/neutral/informal) / 스페인어 2-3단계 (tú/usted/vosotros) / 일본어 3-4단계 / 중국어 2-3단계.
   - **함정**: 한국어 학습자가 다른 4개 언어의 단순 공손 시스템에 한국어 정밀도 기대 → 잘못된 등록 (예: 영어 비즈니스 이메일 캐주얼).
   - **훈련법**: **한국어 경어가 가장 세밀** — 다른 4개 언어는 단순화. 영어 비즈니스 = 항상 격식 (please/thank you/Could you), 캐주얼 = friends only. 한국어처럼 어르신/평생 친구/직장 동료 별도 단계 없음.

2. **존경 동사 (honorific verb) vs 단순 대명사 교체**:
   - 한국어 동사 자체가 변형: 먹다 → 잡수시다, 자다 → 주무시다, 있다 → 계시다. 주어가 받는 높임.
   - 영어: 대명사만 (you), 동사 변형 없음.
   - 스페인어: usted 사용 시 3인칭 동사 (come usted = come). 대명사 교체 + 동사 일치.
   - 중국어: 대명사 교체 (nǐ → nín), 동사 변형 없음.
   - **함정**: 한국어 학습자가 영어/중국어에 "존경 동사" 기대 → 영어 "you eat → usted eat (X)" 어색. 영어는 "you eat" 동일.
   - **훈련법**: 한국어 = **동사 자체 변형** (존경/겸양 동사) vs 영어/중국어 = **대명사만 교체** vs 스페인어 = 대명사 + 3인칭 동사 일치 vs 일본어 = 동사 변형 + 명사 교체. **4개 메커니즘** 명시적 학습.

3. **"내 사람/남" 한국어 문화의 특수성**:
   - 한국어: 내 그룹(우리 가족, 친한 친구, 우리 회사) vs 외 그룹(낯선 사람, 경쟁사). **명확한 구분**이 등록에 영향.
   - 영어/스페인어/중국어: 내/외 구분 약함/중립. 영어 "we" vs "they" 맥락 의존.
   - **함정**: 한국어 학습자가 영어/스페인어 비즈니스 이메일에서 "우리 회사 (our company)" 직접 번역 → 영어 비즈니스 이메일 = 회사는 3인칭 ("our company will..."), 캐주얼 표현 사용 자제.
   - **훈련법**: 한국어 "우리" vs 다른 언어 "we/nosotros" — 한국어는 소속 의식 강함, 영어/스페인어는 개인주의. 비즈니스 이메일에서 우리/they 사용 패턴 학습.

4. **반말 협상 (banmal negotiation) 의 명시성**:
   - 한국어: "우리 반말 해요?" 명시적 협상. 연장자/윗사람이 먼저 제안하는 게 일반.
   - 영어/스페인어: first-name basis, *tuteo* 자연스러움 (명시적 협상 덜함).
   - 일본어: *tameguchi* 전환 (음주 후 / 3번째 만남) — 연장자가 제안.
   - **함정**: 한국어 학습자가 영어/스페인어 first-name basis를 "반말 협상"처럼 명시적 시도 → 어색. 영어는 자연스러운 first-name 사용.
   - **훈련법**: "우리 반말 해요?" 스크립트 (한국어) vs 영어 first-name 자연 사용 vs 스페인어 *tuteo* ("¿Puedo tutearte?") — **문화별 명시성/암묵성 학습**.

5. **나이 (age) 의 한국어 위계 시스템**:
   - 한국어: 1세 이상 차이 = 경어 의무. 같은 나이 = "언제 반말 할까요?" 협상.
   - 영어/중국어: 나이 무관, 호칭/직함 사용.
   - 스페인어: 나이 + 호칭 (Don/Doña, usted).
   - 일본어: 선배/후배 위계 (senpai/kouhai) + 경어.
   - **함정**: 한국어 학습자가 영어 비즈니스에서 "나이가 어려 보이시네요" 같은 나이 언급 → 영어권에서는 부적절.
   - **훈련법**: 5개 문화 나이/위계 시스템 비교 — 한국어 1세 단위, 일본어 선후배, 영어/중국어 무관, 스페인어 나이 + 호칭.

### 학습 전략

1. **우선순위 1**: 한국어 경어 6단계 마스터 — 하소서체/합쇼체/해요체/해체/반말 + 존경/겸양/평어. **한국어 고유 시스템** 다른 언어와 비교 불가.
2. **우선순위 2**: 5개 언어 공손 시스템 메커니즘 비교 — 한국어/일본어 = 동사 형태 변형 vs 영어/중국어 = 어휘 + 대명사 vs 스페인어 = 대명사 + 3인칭 동사. **4개 메커니즘** 명시적 구분.
3. **우선순위 3**: 존경 동사 (honorific verb) 한국어 마스터 — 먹다/잡수시다, 자다/주무시다, 있다/계시다. 다른 4개 언어에 동사 변형 없음.
4. **우선순위 4**: 내/외 그룹 (우리/남) 문화 학습 — 한국어 특유의 소속 의식. 비즈니스/사교/가족 문맥별 그룹 경계 명시.
5. **우선순위 5**: 반말 협상 (banmal negotiation) 스크립트 — "우리 반말 해요?" 명시적 협상. 영어 first-name 자연 사용 vs 비교.

### 관련 한국어 위키 페이지

- [[speech-levels-ko]] — 한국어 경어 단계 (해체/해요체/합쇼체/하소서체)
- [[polite-expressions-comparison]] — 기본 공손 표현
- [[greetings]] — 인사 의례와 공손
- [[business-email]] — 격식 문어 공손
- [[dating-romance]] — 등록 협상 (반말)
- [[untranslatable-concepts]] — 정/눈치/체면 등 한국어 공손 관련 개념

---

## 관련 페이지

- `[[greetings]]` — 인사 의례가 공손 인코딩
- `[[pronouns-reference]]` — 대명사 시스템이 경어 구조 반영
- `[[business-email]]` — 문어 등록 비교
- `[[dating-romance]]` — 친밀성 등록 협상

## 출처

- English: `[English/vocabulary/basic-vocabulary]`, `[English/culture/english-dating-culture]`
- Spanish: `[Spanish/vocabulary/polite-expressions-vocabulary]`, `[Spanish/culture/espana-vs-latinoamerica-registro]`
- Japanese: `[Japanese/vocabulary/business-vocabulary]`, `[Japanese/culture/japanese-dating-culture]`
- Korean: `[Korean/vocabulary/emotions-personality-vocabulary]`, `[Korean/culture/korean-dating-culture]`
- Chinese: `[Chinese/vocabulary/body-zh]`, `[Chinese/sources/greetings-zh]`

---

**원본 (영어)**: [[politeness-honorifics]] | **관련 미러**: [[politeness-honorifics.es|Spanish]] · [[politeness-honorifics.ja|Japanese]] · [[politeness-honorifics.zh|Chinese]] | **정책**: ADR-0006
