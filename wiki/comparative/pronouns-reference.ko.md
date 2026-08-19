# 대명사 & 지시 — 다국어 비교 (한국어판)

> 원본: [[pronouns-reference]] (English) | 작성일: 2026-08-20 | ADR-0006
> **5개 언어 인칭대명사 시스템 비교**

---

## 빠른 참조 표

### 인칭 대명사

| 인칭 | English | Spanish | Japanese | Korean | Chinese |
|--------|---------|---------|----------|--------|---------|
| **1인칭 단수** | I | yo | 私 / 僕 / 俺 / わし | 나 / 저 | 我 / 咱 |
| **2인칭 단수** | you | tú / usted / vos | あなた / 君 / お前 / 貴方 | 너 / 당신 / 선생님 | 你 / 您 |
| **3인칭 단수** | he/she/it | él / ella | 彼 / 彼女 / あの人 | 그 / 그녀 / 그분 | 他 / 她 / 它 |
| **1인칭 복수** | we | nosotros/as | 私たち / 僕ら / 俺たち | 우리 / 저희 | 我们 / 咱们 |
| **2인칭 복수** | you (all) | vosotros/as / ustedes | あなたたち / 君たち | 너희 / 여러분 / 선생님들 | 你们 / 您们 |
| **3인칭 복수** | they | ellos / ellas | 彼ら / 彼女ら / あの人たち | 그들 / 그분들 | 他们 / 她们 / 它们 |

### 핵심 구조적 차이

| 기능 | English | Spanish | Japanese | Korean | Chinese |
|---------|---------|---------|----------|--------|---------|
| **의무?** | 예 (주어 필수) | 아니오 (pro-drop) | 아니오 (pro-drop, 맥락 의존) | 아니오 (pro-drop) | 아니오 (pro-drop) |
| **3인칭 단수 성** | 예 (he/she/it) | 예 (él/ella) | 아니오 (kare/kanojo = he/she but rarely used) | 아니오 (geu/geunyeo = he/she but rare) | 예 (tā/tā/tā — 같은 발음, 다른 한자) |
| **공손 인코딩** | 아니오 (어휘만) | 예 (tú/usted/vos) | 예 (대명사 선택 = 등록) | 예 (대명사 선택 = 등록) | 예 (nǐ/nín) |
| **포괄/배타 우리** | 아니오 | 아니오 | 아니오 (wareware = 격식 우리) | 아니오 (uri = 포괄 기본) | **예** (zánmen = 포괄, wǒmen = 배타) |
| **영 대명사 (pro-drop)** | 아니오 | **예** (표준) | **예** (표준) | **예** (표준) | **예** (표준) |

### 시제 대명사

| 거리 | English | Spanish | Japanese | Korean | Chinese |
|----------|---------|---------|----------|--------|---------|
| **근 (this)** | this | este/esta/esto | これ (kore) | 이거 / 이것 | 这 / 这个 |
| **중 (that near you)** | that | ese/esa/eso | それ (sore) | 그거 / 그것 | 那 / 那个 |
| **원 (that over there)** | that over there | aquel/aquella/aquello | あれ (are) | 저거 / 저것 | 那个 (far) |
| **장소 (here/there)** | here/there | aquí/allí/allá | ここ/そこ/あそこ | 여기/거기/저기 | 这里/那里/那儿 |

### 의문 대명사

| 의문 | English | Spanish | Japanese | Korean | Chinese |
|----------|---------|---------|----------|--------|---------|
| **누구** | who | quién | 誰 (だれ) | 누구 (nugu) | 谁 (shéi/shuí) |
| **무엇** | what | qué | 何 (なに/なん) | 무엇 / 뭐 (mueot/mwo) | 什么 (shénme) |
| **어느** | which | cuál | どれ (dore) | 어느 (eoneu) | 哪个 (nǎge) |
| **어디** | where | dónde | どこ (doko) | 어디 (eodi) | 哪里 / 哪儿 (nǎlǐ/nǎr) |
| **언제** | when | cuándo | いつ (itsu) | 언제 (eonje) | 什么时候 (shénme shíhou) |
| **왜** | why | por qué | なぜ (naze) / どうして (doushite) | 왜 (wae) | 为什么 (wèishénme) |
| **어떻게** | how | cómo | どう (dou) | 어떻게 (eotteoke) | 怎么 (zěnme) |
| **누구의** | whose | de quién | 誰の (dare no) | 누구 것 (nugu geot) | 谁的 (shéi de) |

### 부정/부정 의문 대명사

| 의미 | English | Spanish | Japanese | Korean | Chinese |
|---------|---------|---------|----------|--------|---------|
| **모두** | everyone | todos | 皆 (みな) / みんな | 모두 / 전부 | 大家 / 人人 |
| **누군가** | someone | alguien | 誰か (だれか) | 누군가 (nugunga) | 某人 / 谁 (shéi) |
| **아무도** | no one | nadie | 誰も...ない (dare mo...nai) | 아무도...않다 (amudo...anta) | 没人 / 谁都不 (shéi dōu bù) |
| **모든 것** | everything | todo | 全て (すべて) / みんな | 모든 것 / 전부 | 一切 / 全部 |
| **무언가** | something | algo | 何か (なにか) | 무언가 / 뭔가 (mueotnga/mwonga) | 某事 / 什么 (shénme) |
| **아무것도** | nothing | nada | 何も...ない (nani mo...nai) | 아무것도...않다 (amugeotdo...anta) | 没事 / 什么都没有 (shénme dōu méiyǒu) |
| **아무나** | anyone | cualquiera | 誰でも (だれでも) | 아무나 (amuna) | 谁都可以 (shéi dōu kěyǐ) |

### 재귀 & 호혜

| 종류 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **재귀** | myself/yourself... | me/te/se/nos/os/se | 自分 (じぶん) | 자기 (jagi) / 자신 (jasin) | 自己 (zìjǐ) |
| **호혜** | each other | el uno al otro / mutuamente | お互い (おたがい) | 서로 (seoro) | 彼此 / 互相 (bǐcǐ/hùxiāng) |

### 영 대명사 (Pro-Drop) 행동

| 언어 | 주어 drop | 목적어 drop | 소유 drop | 노트 |
|----------|--------------|-------------|----------------|-------|
| **English** | ❌ | ❌ | ❌ | 의무 주어 |
| **Spanish** | ✅ (표준) | ❌ (clitics 필수) | ❌ | *Hablo español* = "I speak Spanish" |
| **Japanese** | ✅ (표준) | ✅ (표준) | ✅ (표준) | 맥락 복원 의무 |
| **Korean** | ✅ (표준) | ✅ (표준) | ✅ (표준) | 주제/해설 구조가 복원 보조 |
| **Chinese** | ✅ (표준) | ✅ (표준) | ✅ (표준) | 주제 우세; null anaphora 만연 |

### 복원 전략
- **Spanish**: 동사 형태가 인칭/수 인코딩 (*hablo/hablas/habla/hablamos/habláis/hablan*)
- **Japanese/Korean**: 주제 조사 (*wa/は* vs *ga/が* vs *eun/은* vs *i/이*) + 경어 + 맥락
- **Chinese**: 주제-해설 구조 + 상 조사 + 어휘 맥락

### 다국어 간섭 맵

| 학습자 L1 → 목표 L2 | 일반적 오류 | 이유 |
|------------------------|---------------|-----|
| **EN → ES/JP/KR/CH** | 명시적 대명사 everywhere ("I think that he...") | L1 주어 필수; 목표 zero 허용 |
| **ES → JP/KR** | *tú* 등가물 (*anata/neo*) 모르는 사람에게 사용 | *Tú* = peer 기본; *anata/neo* = intimate |
| **JP/KR → CH** | *nín* (您) *anata/nan* 처럼 과용 | *Nín* = 특정 존경; 중국어는 호칭 더 사용 |
| **CH → ES** | *tú* 보편 사용 (*nín* 등가물 없음) | 중국어 *nǐ* 기본; 스페인어 *usted* 선택 필수 |
| **EN → JP/KR** | "you" → *anata/neo* 번역 | JP/KR에 중립 "you" 없음 |

---

## 학습자 의사결정 가이드

| 필요한 표현 | EN | ES | JP | KR | CH |
|----------------|----|----|-----|----|----|
| **"I (polite)"** | I | yo | わたし (watashi) | 저 (jeo) | 我 (wǒ) |
| **"I (casual male)"** | I | yo | ぼく (boku) / おれ (ore) | 나 (na) | 我 (wǒ) |
| **"You (polite)"** | you | usted | (name)-san | (name)-ssi/nim | 您 (nín) |
| **"You (casual)"** | you | tú / vos | (name)-kun/chan | 너 (neo) | 你 (nǐ) |
| **"We (inclusive)"** | we | nosotros | わたしたち (watashitachi) | 우리 (uri) | 咱们 (zánmen) |
| **"We (exclusive)"** | we | nosotros | わたしたち (watashitachi) | 우리 (uri) / 저희 (jeohui) | 我们 (wǒmen) |
| **"He/She (respectful)"** | he/she | él/ella | あのかた (ano kata) | 그분 (geu bun) | 他/她 (tā) |
| **"This one"** | this one | este | これ (kore) | 이거 (igeo) | 这个 (zhège) |
| **"Who?"** | who? | quién? | だれ (dare)? | 누구 (nugu)? | 谁 (shéi)? |
| **"Nobody"** | nobody | nadie | だれもいない (dare mo inai) | 아무도 없다 (amudo eopda) | 没人 (méi rén) |

---

## 🇰🇷 한국어 학습자 노트 (Korean Learner Notes)

> 본 섹션은 한국어 학습자 대상의 추가 학습 가이드입니다.

### 한국어 화자가 다른 4개 언어 대명사 시스템을 학습할 때 흔히 마주치는 함정

1. **"당신 (dangsin)" 의 한국어 함정**:
   - 한국어 "당신" = 2인칭 단수이지만 **공손 단어 아님** — (1) 부부/연인 사이 (2) 시/노래 (3) 적대/다툼 시 (4) 번역 시 영어 "you" 매핑 (X). 일상 사용 부적절.
   - 영어 "you" = 보편, 캐주얼/격식 모두 무관.
   - 일본어 "あなた" = 친밀, 부부/연인/문맥, 격식 시 사용 자제.
   - **함정**: 한국어 학습자가 영어/스페인어 "you"를 "당신/당신들"로 번역 → 부적절. 영어 "you" 무난, 한국어 "당신" 위험.
   - **훈련법**: 한국어 **"당신 사용 자제"** 원칙 학습. 영어 "you"는 보편 사용, 한국어 "당신"은 피하고 이름+님/씨/직함 사용.

2. **영 대명사 (pro-drop) 한국어/일본어/중국어 vs 영어 의무**:
   - 한국어/일본어/중국어/스페인어: 주어/목적어 자유 생략. "밥 먹었어요" (X: 나는 밥을 먹었어요) 정상.
   - 영어: 주어 의무. "I ate" (O), "Ate" (X, "I" 생략 불가).
   - **함정**: 한국어 학습자가 영어에 영 대명사 패턴 적용 → "Ate rice" (X) vs "I ate rice" (O). 영어는 주어 필수.
   - **훈련법**: 영 대명사 메트릭스 — 한국어/일본어/중국어/스페인어 = 주어 생략 가능, 영어 = 주어 필수. **영어 학습 시 영 대명사 사용 자제**.

3. **"우리 (uri)" vs "저희 (jeohui)" 의 한국어 자제**:
   - 한국어: 우리 (캐주얼) / 저희 (겸양) — "우리 회사" (O) / "저희 회사" (격식).
   - 영어: we (캐주얼/격식).
   - 일본어: わたしたち (격식 우리) / 僕ら / 俺たち (캐주얼).
   - 중국어: 我们 (wǒmen, 배타 우리) / 咱们 (zánmen, 포괄 우리).
   - **함정**: 한국어 학습자가 "우리"를 모든 4개 언어에 동일하게 사용 → 영어 "we"는 캐주얼/격식 모두 OK, 중국어 "咱们"는 포괄 우리 (you+me+others) — 배타 의미 다름.
   - **훈련법**: 우리 (uri) vs 저희 (jeohui) — **포괄 vs 겸양** 매트릭스. 중국어 我们 (배타) vs 咱们 (포괄) 명시 학습.

4. **호칭+직함 의무 사용의 한국어/중국어/일본어 vs 영어**:
   - 한국어: 이름+님/씨/직함 필수. "김 과장님", "선생님" 호칭.
   - 중국어: 姓+직함 (王经理, 李老师) 필수. 이름 단독 사용 시 무례.
   - 일본어: 姓+さん/様/くん/ちゃん 호칭.
   - 영어: 이름/성이름 모두 OK, 직함 무관.
   - **함정**: 한국어 학습자가 영어 비즈니스에서 직함 무관하게 "Mr. Kim" 또는 "John" 자유 사용 → 한국 비즈니스에서는 "김 과장님" 필수. 호칭 생략 시 무례.
   - **훈련법**: 호칭+직함 매트릭스 — 한국어/중국어/일본어 의무, 영어 선택. **5개 언어 호칭 규칙 학습**.

5. **3인칭 대명사 "그/그녀/그분" 의 한국어 자제**:
   - 한국어 "그/그녀" = he/she but **드물게 사용**. 대부분 이름/직함/관계로 대체. "그분"은 존경형.
   - 영어 he/she 필수.
   - 스페인어 él/ella 필수 (성별 인코딩).
   - 일본어 彼/彼女 존재하지만 번역투 — "あの人" 선호.
   - **함정**: 한국어 학습자가 영어/스페인어 he/she를 한국어 "그/그녀"로 직역 → 부자연스러움. 한국어는 "그 사람", "이 분", "박 선생님" 등 사용.
   - **훈련법**: 3인칭 대명사 5개 언어 비교 — 한국어/일본어 자제 (이름/관계), 영어/스페인어 의무 (성별 인코딩), 중국어 그/她 단어 발음 동일.

### 학습 전략

1. **우선순위 1**: 한국어 "당신 (dangsin) 사용 자제" 원칙 — 영어 "you" 보편 ≠ 한국어 "당신" 보편. **이름+님/씨/직함** 사용 매트릭스.
2. **우선순위 2**: 영 대명사 (pro-drop) 5개 언어 매트릭스 — 한국어/일본어/중국어/스페인어 = 주어 자유 생략, 영어 = 주어 필수. **영어 학습 시 영 대명사 사용 자제**.
3. **우선순위 3**: "우리 (uri)" vs "저희 (jeohui)" + 중국어 我们 (배타) vs 咱们 (포괄) — **포괄 vs 배타 우리** 명시 학습. 4개 메커니즘 구분.
4. **우선순위 4**: 호칭+직함 의무 사용 — 한국어/중국어/일본어 = 의무, 영어 = 선택. **5개 언어 호칭 규칙 매트릭스**.
5. **우선순위 5**: 3인칭 대명사 자제 vs 의무 — 한국어/일본어 자제 (이름/관계), 영어/스페인어 의무 (성별 인코딩), 중국어 他/她 한자 구분 (발음 동일). **3인칭 5개 언어 사용 규칙 학습**.

### 관련 한국어 위키 페이지

- [[politeness-honorifics]] — 대명사 선택이 경어 인코딩
- [[greetings]] — 인사 호칭
- [[business-email]] — 문어 대명사 관행
- [[negation]] — 부정 대명사 (nobody, nothing)
- [[pronouns-reference]] — 대명사 전체

---

## 관련 페이지

- `[[politeness-honorifics]]` — 대명사 선택이 경어 인코딩
- `[[greetings]]` — 인사 호칭
- `[[business-email]]` — 문어 대명사 관행
- `[[negation]]` — 부정 대명사 (*nadie, dare mo...nai, amudo...*)

## 출처

- English: `[English/vocabulary/basic-vocabulary]`
- Spanish: `[Spanish/vocabulary/basic-vocabulary]`, `[Spanish/culture/espana-vs-latinoamerica-registro]`
- Japanese: `[[index]]`, `[Japanese/culture/japanese-dating-culture]`
- Korean: `[[index]]`, `[Korean/culture/korean-dating-culture]`
- Chinese: `[Chinese/sources/greetings-zh]`, `[Chinese/vocabulary/family-zh]`

---

**원본 (영어)**: [[pronouns-reference]] | **관련 미러**: [[pronouns-reference.es|Spanish]] · [[pronouns-reference.ja|Japanese]] · [[pronouns-reference.zh|Chinese]] | **정책**: ADR-0006
