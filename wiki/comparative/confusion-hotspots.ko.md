# 혼동 핫스팟 — Cross-Language Comparison (한국어판)

> 원본: [[confusion-hotspots]] (English) | 작성일: 2026-08-19 | ADR-0006
> **5개 언어 혼동 포인트 비교** — English · Spanish · Japanese · Korean · Chinese

---

## 빠른 참조 표

### 영어-스페인어 거짓 친구 (False Friends)

| 영어 단어 | 영어 의미 | 스페인어 유사 단어 | **실제 스페인어 의미** | 예시 |
|-------------|-----------------|----------------------|--------------------------|---------|
| **Embarazada** | (영어 대응어 없음) | Embarrassed | **임신한** | *Estoy embarazada* = "I'm pregnant" (NOT "embarrassed") |
| **Realizar** | Realize | Realize | **달성하다/수행하다** | *Realizar un proyecto* = "프로젝트 수행" |
| **Sensible** | Sensible | Sensible | **민감한** | *Eres muy sensible* = "당신은 매우 민감합니다" |
| **Exquisite** | Refined | Exquisito | **훌륭한 / 맛있는** | *Exquisito* = "delicious" (음식) |
| **Constipado** | (대응어 없음) | Constipated | **감기에 걸린** | *Estoy constipado* = "감기 걸렸어요" (변비 아님) |
| **Éxito** | Exit | Éxito (success) | **성공** | *Tener éxito* = "성공하다" |
| **Discutir** | Discuss | Discutir | **논쟁하다** | *Discutimos mucho* = "자주 다툼" |
| **Sopa** | Soap | Sopa | **수프** | *Sopa de pollo* = "닭고기 수프" |

### 영어-일본어 거짓 친구

| 영어 단어 | 영어 의미 | 일본어 유사 단어 | **실제 의미** | 예시 |
|-------------|-----------------|----------------------|-------------------|---------|
| **Manga** | (대응어 없음) | 漫画 (manga) | **만화/코믹** (애니메이션만 아님!) | 漫画を読む = 만화 읽기 |
| **Anime** | (대응어 없음) | アニメ | **애니메이션** (일본 스타일만 아님) | アニメ = animation |
| **Otaku** | (대응어 없음) | おたく | **덕후/오타쿠** (긍정적 뉘앙스 증가) | アニメオタク = 애니 덕후 |
| **Senpai** | (대응어 없음) | 先輩 | **선배** (노인 아님) | 田中先輩 = Tanaka 선배 |
| **Sensei** | (대응어 없음) | 先生 | **선생님/의사/대사** (전문가) | 医者先生 = 의사 선생님 |

### 영어-한국어 거짓 친구 (한국어 자체)

| 한국어 단어 | 의미 | 영어 유사 단어 | **영어 의미** | 예시 |
|-------------|-----------------|---------------------|-------------------|---------|
| **Oppa** | 오빠 (여자 → 남자) | Older brother | **오빠/남자친구** |  |
| **Unnie/Unni** | 언니 (남자 → 여자) | (대응어 없음) | **언니 (남자가 사용하는)** |  |
| **Hyung** | 형 (남자 → 남자) | (대응어 없음) | **형 (남자가 사용하는)** |  |
| **Noona** | 누나 (여자 → 여자) | (대응어 없음) | **누나 (여자가 사용하는)** |  |
| **Kimbap** | 김밥 | (대응어 없음) | **김밥** (스시 아님) |  |
| **Bulgogi** | 불고기 | (대응어 없음) | **불고기** |  |
| **Soju** | 소주 | (대응어 없음) | **소주** |  |
| **Hanbok** | 한복 | (대응어 없음) | **전통 한국 의상** |  |
| **Hallyu** | 한류 | (대응어 없음) | **Korean Wave** (문화 수출) |  |
| **Aegyo** | 애교 | (대응어 없음) | **Cute act / cuteness display** |  |
| **Daebak** | 대박 | (대응어 없음) | **Awesome / jackpot** |  |

### 영어-중국어 거짓 친구

| 영어 단어 | 영어 의미 | 중국어 유사 단어 | **실제 의미** | 예시 |
|-------------|-----------------|---------------------|-------------------|---------|
| **Tea** | 차 | 茶 (chá) | **차** | OK |
| **Dim sum** | (대응어 없음) | 点心 (diǎnxīn) | **간식/브런치 음식** |  |
| **Kung fu** | (대응어 없음) | 功夫 (gōngfu) | **기술/노력/무술** | 功夫 = "노력" 의미도 |
| **Tofu** | (대응어 없음) | 豆腐 (dòufu) | **두부** | 豆 = 콩, 腐 = 썩은 |
| **Wok** | (대응어 없음) | 锅 (guō) | **냄비/팬** (wok 만 아님) | 锅 = 모든 조리 냄비 |

### 발음 혼동 (영어 화자)

#### 스페인어에서

| 영어 화자 발음 | 올바른 발음 | 이유 |
|----------------------|------------|-----|
| "Hespañol" | "Español" (ehs-pah-nyohl) | 영어 "e" = "ee", 스페인어 "e" = "eh" |
| "Gracias" as "GRAH-see-as" | "GRAH-syahs" | "c" before "e/i" = "s" 발음 |
| "Vaya" as "VAY-ah" | "BAH-yah" (부드러운 b/v) | b/v = 동일 발음 |
| "Hola" with TH | "OH-lah" | 스페인어 "h" 무음 |

#### 일본어에서

| 영어 화자 발음 | 올바른 발음 | 이유 |
|----------------------|------------|-----|
| "Hai" as English "Hi" | "Hah-ee" | "ai" = "ah-ee" (2 모라) |
| "Desu" as "Day-su" | "Des" (s 가벼움) | "u" 가 일부 맥락에서 무성화 |
| "Ri" as "ree" | "Ree" | "i" not "ee" — 일본어에 "ee" 없음 |

#### 한국어에서

| 영어 화자 발음 | 올바른 발음 | 이유 |
|----------------------|------------|-----|
| "Annyeonghaseyo" with clear TH | "An-nyeong-ha-se-yo" | "th" 발음 없음 |
| "Kimchi" as "Kim-chee" | "Kim-chi" (글라이드 없음) | "i" 짧음, "ee" 아님 |
| "Bulgogi" as "Bul-go-gee" | "Bul-go-gi" | "gi" 가 "gee" 아님 |

### 문법 혼동

#### 시제/상 혼동

| L1 → L2 | 일반 오류 | 이유 |
|---------|--------------|-----|
| **EN → ES** | "If I **will go**" → "*Si **iré***" (틀림) | 스페인어 si 절에 미래 시제 미사용 → *Si **voy*** |
| **EN → JP** | "I **have gone**" → "I **go**" | 일본어 현재완료 없음; 과거 (*itta*) 만 |
| **EN → KR** | "I **will go** tomorrow" → "I **go** tomorrow" | 한국어는 종종 미래 시제 생략; *내일 갈게* 가능 |
| **EN → CH** | "I **am eating**" → "I **eat**" | 중국어는 상(相), 시제 아님; *我在吃* (진행) vs *我吃* (습관) |

#### 경어/격식 혼동

| L1 → L2 | 일반 오류 | 이유 |
|---------|--------------|-----|
| **EN → ES** | "tú" with strangers | 스페인어는 라틴아메리카에서 기본 *usted* |
| **EN → JP** | Plain form with strangers | 일본어는 기본 *desu/masu* |
| **EN → KR** | Plain form with elders | 한국어는 기본 *haeyo/hapsyo* |
| **EN → CH** | No honorific for elders | 중국어는 您 + 직함 |

### 숫자 & 날짜 혼동

| 숫자 | 혼동 | 올바른 | 위치 |
|--------|-------------|---------|-------|
| **1,000** | "1" + ",000" | 천 | EN |
| **1.000** | "1" + ".000" | 천 | ES/DE |
| **1,000** | "1" + "000" | 천 (구분자 없음) | CN/JP |
| **10,000** | "Ten thousand" | "One wan/man/wàn" | EN/JP/KR/CN |
| **100,000,000** | "억" | "Yi" (亿) | CN |

### 날짜 형식 혼동

| 형식 | 읽기 | 국가 |
|--------|---------|---------|
| **07/19/2026** | 7월 19일 (US) / 19 7월 (UK) | US vs UK |
| **2026/07/19** | 연도 먼저 | CN/JP/KR |
| **19.07.2026** | 2026년 7월 19일 | DE/ES |
| **19/07/2026** | 2026년 7월 19일 | UK/ES |
| **2026.07.19** | 연도 먼저 | KR (현대) |

### 자주 혼동되는 맞춤법/문법 쌍

| 언어 | 쌍 | 기억법 |
|----------|------|---------|
| **EN** | there/their/they're | "there" 안에 "here" |
| **EN** | your/you're | "you're" = "you are" |
| **EN** | its/it's | "it's" = "it is" |
| **EN** | affect/effect | "affect" = 동사; "effect" = 명사 (보통) |
| **ES** | por/para | *por* = 이유; *para* = 목적 |
| **ES** | si/sí | *si* = if; *sí* = yes |
| **JP** | いる/ある | *iru* = 의인; *aru* = 무생물 |
| **KR** | 을/를 | 목적어 조사 (자음/모음 뒤) |
| **KR** | 이/가 | 주어 조사 (자음/모음 뒤) |
| **KR** | 은/는 | 보조사 (자음/모음 뒤) |
| **CH** | 的/得/地 | *的* (de = 형용사), *得* (dé = 보어), *地* (dì = 부사) |
| **CH** | 在/再 | *zài* = ~에; *zài* (4성) = 다시 |

---

## 학습자 의사결정 가이드

- **마스터해야 할 첫 10 표현 (거짓 친구 회피)**:
  - EN: Estoy embarazada = "I'm pregnant" (not embarrassed)
  - ES: Discutir = "to argue" (not discuss)
  - JP: マンション = "apartment" (not mansion)
  - JP: パンツ = "underwear" (not pants)
  - KR: 김밥 = "kimbap" (not sushi)
  - CH: 送钟 (시계 선물) 피하기
  - CH: 送绿帽 (녹색 모자) 피하기

---

## 🇰🇷 한국어 학습자 노트 (Korean Learner Notes)

> 본 섹션은 한국어 학습자 대상의 추가 학습 가이드입니다.

### 한국어 화자가 다른 4개 언어에서 흔히 마주치는 혼동 함정

1. **스페인어 "estar embarazada" 의 임신 오해**:
   - 한국어 학습자는 "embarazada" 를 embarrassed (당황한) 으로 오해 — 스페인어에서 임신.
   - **함정**: "I'm embarrassed" = "Estoy avergonzado/a" (성별 일치). "I'm pregnant" = "Estoy embarazada".
   - **훈련법**: 스페인어 거짓 친구 20개 표 작성 (embarazada/realizar/sensible/discutir/sopa/éxito 등) — 한국어 학습자가 가장 자주 오류 내는 항목.

2. **일본어 マンション 의 맨션 오해**:
   - 한국어 학습자가 일본어 マンション (manshon) 를 "대저택 (mansion)" 으로 오해 — 일본어에서는 "아파트" 의미.
   - **함정**: 한국어 "맨션" = 고급 아파트, 일본어 マンション = 모든 아파트. 영어 Mansion (대저택) 과 정반대.
   - **훈련법**: 일본어 한자 차용어의 의미 변화 학습 — マンション (아파트) / バイキング (뷔페) / ハンドル (운전대) / コンセント (콘센트) / ノート (공책, not note).

3. **일본어 パンツ 의 팬티 오해**:
   - 한국어 학습자가 일본어 パンツ (pantsu) 를 "바지 (pants)" 로 오해 — 일본어에서는 "속옷 (underwear)" 의미. 일본어 바지 = ズボン (zubon).
   - **함정**: 일본 의류 매장에서 "パンツ 있어요?" = "속옷 있어요?" — 매우 당황스러운 상황 발생.
   - **훈련법**: 일본어 외래어 발음 유사 단어의 의미 차이 표 — パンツ (속옷) vs ズボン (바지) / スマート (날씬한) vs Smart / バイキング (뷔페) vs Viking.

4. **중국어 功夫 (gōngfu) 의 다의성**:
   - 한국어 학습자는 功夫 를 "쿵푸 (kung fu, 무술)" 로만 인식 — 중국어에서는 "노력/기술" 의미도.
   - **함정**: "他的功夫很好" = "그의 노력/기술이 좋다" (무술 아님). "练功夫" = "기술을 익히다" (일반 의미).
   - **훈련법**: 중국어 功夫 의 두 가지 의미 학습 — 무술 (kung fu) / 노력·기술 (effort, skill). 맥락별 사용 학습.

5. **영어 R/L 발음의 한국어 화자 어려움**:
   - 한국어 ㄹ 발음과 영어 R/L 모두 어려운 — 한국어 화자는 "rice" 와 "lice" 를 혼동.
   - **함정**: "He wrote a letter" (그는 편지를 썼다) vs "He right a latter" (✗) — 발음 구분 실패.
   - **훈련법**: 영어 R/L 최소 쌍 (right/light, read/lead, road/load) 50개 훈련. 한국어 화자는 ㄹ (양순음 + 탄음) 을 영어 R/L 의 중간 어딘가로 발음 — 의식적으로 후치경음/측음 분리.

### 학습 전략

1. **우선순위 1**: 스페인어 거짓 친구 20개 (embarazada, realizar, discutir 등) + 한국어 학습자 빈도 높은 오류 매핑.
2. **우선순위 2**: 일본어 한자 차용어의 의미 변화 20개 (マンション, パンツ, スマート, バイキング, ハンドル 등).
3. **우선순위 3**: 영어 R/L 발음 최소 쌍 50개 훈련 (rice/lice, right/light, read/lead).
4. **우선순위 4**: 중국어 다의 한자 (功夫, 行, 长, 重) 의 맥락별 의미 학습.
5. **우선순위 5**: 문화적 금기 (시계 선물, 녹색 모자, 빨간 잉크) 의 언어별 학습.

---

## 관련 페이지

- `[[untranslatable-concepts]]` — 문화 의존 단어 혼동
- `[[politeness-honorifics]]` — 격식 혼동
- `[[pronouns-reference]]` — 대명사 혼동
- `[[pronunciation-challenges]]` — 발음 혼동
- `[[writing-systems]]` — 문자 혼동
- `[[grammar-difficulty-map]]` — 문법 혼동 패턴
- `[[idioms-proverbs]]` — 속담 번역 오류
- `[[slang-colloquial]]` — 속어 거짓 친구
- `[[food-dining]]` — 메뉴/예절 혼동
- `[[numbers-counters]]` — 숫자 혼동
- `[[time-calendar]]` — 날짜 형식 혼동

## 출처

- L2 오류에 관한 문법적 문헌 (Selinker 1972, Ellis 1994, Richards 1974)
- 구체적 오류 카탈로그: Marckwardt (1958) 영어 오류, Pinilla (2002) 스페인어 오류
- 교수 경험 (FSI, ACTFL 능력 등급)
- `[English/vocabulary/basic-vocabulary]`
- `[Spanish/vocabulary/basic-vocabulary]`
- `[[index]]`
- `[Chinese/sources/pinyin-basics-zh]`

---

**원본 (영어)**: [[confusion-hotspots]] | **관련 미러**: [[confusion-hotspots.es|Spanish]] · [[confusion-hotspots.ja|Japanese]] · [[confusion-hotspots.zh|Chinese]] | **정책**: ADR-0006