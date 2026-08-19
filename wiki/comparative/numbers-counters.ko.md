# 숫자 & 수량사 — 다국어 비교 (한국어판)

> 원본: [[numbers-counters]] (English) | 작성일: 2026-08-20 | ADR-0006
> **5개 언어 숫자 시스템 & 수량사(조사) 비교**

---

## 빠른 참조 표

### 기수 (1-10, 100, 1000, 10000)

| 숫자 | English | Spanish | Japanese | Korean (Sino) | Korean (Native) | Chinese |
|--------|---------|---------|----------|---------------|-----------------|---------|
| 0 | zero | cero | ゼロ / 零 | 영 / 공 | - | 零 / 〇 |
| 1 | one | uno | 一 (いち) | 일 | 하나 (han-) | 一 (yī) |
| 2 | two | dos | 二 (に) | 이 | 둘 (tu-) | 二 (èr) / 两 (liǎng) |
| 3 | three | tres | 三 (さん) | 삼 | 셋 (se-) | 三 (sān) |
| 4 | four | cuatro | 四 (よん/し) | 사 | 넷 (ne-) | 四 (sì) |
| 5 | five | cinco | 五 (ご) | 오 | 다섯 (da-) | 五 (wǔ) |
| 6 | six | seis | 六 (ろく) | 육 | 여섯 (yeo-) | 六 (liù) |
| 7 | seven | siete | 七 (なな/しち) | 칠 | 일곱 (il-) | 七 (qī) |
| 8 | eight | ocho | 八 (はち) | 팔 | 여덟 (yeo-) | 八 (bā) |
| 9 | nine | nueve | 九 (きゅう/く) | 구 | 아홉 (a-) | 九 (jiǔ) |
| 10 | ten | diez | 十 (じゅう) | 십 | 열 (yeol) | 十 (shí) |
| 20 | twenty | veinte | 二十 (にじゅう) | 이십 | 스물 (seumul) | 二十 (èrshí) |
| 100 | one hundred | cien / ciento | 百 (ひゃく) | 백 | 온 (on) | 一百 (yībǎi) |
| 1,000 | one thousand | mil | 千 (せん) | 천 | - | 一千 (yīqiān) |
| 10,000 | ten thousand | diez mil | 万 (まん) | 만 | - | 一万 (yīwàn) |
| 100,000,000 | hundred million | cien millones | 億 (おく) | 억 | - | 一亿 (yīyì) |

### 핵심 구조적 차이

| 기능 | English | Spanish | Japanese | Korean | Chinese |
|---------|---------|---------|----------|--------|---------|
| **기본 단위** | 1,000 (천) | 1,000 (mil) | 10,000 (만) | 10,000 (만) | 10,000 (万) |
| **큰 숫자 그룹** | 3자리 (천, 백만, 십억) | 3자리 | 4자리 (만, 억, 조) | 4자리 (만, 억, 조) | 4자리 (万, 亿, 兆) |
| **이중 시스템** | 아니오 | 아니오 | 아니오 | **예** (Sino-Korean + Native) | 아니오 (단 2 = 二/两) |
| **복합 0** | "one hundred **and** one" | "ciento uno" | "hyaku ichi" | "baek il" / "baek hana" | "yībǎi líng yī" |

### 서수

| 위치 | English | Spanish | Japanese | Korean | Chinese |
|----------|---------|---------|----------|--------|---------|
| 1st | first | primero / 1º | 一番目 (いちばんめ) | 첫째 / 제1 | 第一 (dì yī) |
| 2nd | second | segundo / 2º | 二番目 (にばんめ) | 둘째 / 제2 | 第二 (dì èr) |
| 3rd | third | tercero / 3º | 三番目 (さんばんめ) | 셋째 / 제3 | 第三 (dì sān) |
| nth | -th | -º / -ª | -番目 (-ばんめ) | -째 / 제- | 第- (dì-) |

- **Spanish**: *primero/tercero* drop -o before masculine noun (*primer libro, tercer piso*)
- **Japanese**: *dai-* prefix for formal (*dai-ikkai* = 第1回)
- **Korean**: *je-* (Sino) + *beonchae* for formal; native *cheot-/du-/se-* for informal
- **Chinese**: *dì-* prefix universally

### 수량사 / 분류사 (The Big Divergence)

> **English/Spanish**: 의무 수량사 없음 — "three apples" = *tres manzanas*
> **Japanese/Korean/Chinese**: **의무** — 명사는 수량사 없이 셀 수 없음

#### Japanese Counters (助数詞)

| Counter | Kanji | Use For | 1 | 2 | 3 | 10 |
|---------|-------|---------|---|---|---|---|
| General objects | 個 | Small objects, apples, eggs | ひとつ | ふたつ | みっつ | とお |
| People | 人 | Humans | ひとり | ふたり | さんにん | じゅうにん |
| Long objects | 本 | Pens, bottles, umbrellas | いっぽん | にほん | さんぼん | じゅっぽん |
| Flat objects | 枚 | Paper, tickets, shirts | いちまい | にまい | さんまい | じゅうまい |
| Machines/Cars | 台 | Cars, computers, TVs | いちだい | にだい | さんだい | じゅうだい |
| Floors | 階 | Building floors | いっかい | にかい | さんがい | じゅっかい |
| Times/Occurrences | 回 | Times doing something | いっかい | にかい | さんかい | じゅっかい |
| Minutes | 分 | Minutes | いっぷん | にふん | さんぷん | じゅっぷん |
| Hours (duration) | 時間 | Hours | いちじかん | にじかん | さんじかん | じゅうじかん |
| Age | 歳 | Years old | いっさい | にさい | さんさい | じゅっさい |
| Animals (small) | 匹 | Cats, dogs, fish | いっぴき | にひき | さんびき | じゅっぴき |
| Books | 冊 | Books, magazines | いっさつ | にさつ | さんさつ | じゅっさつ |
| Cups/Bowls | 杯 | Drinks, bowls of rice | いっぱい | にはい | さんばい | じゅっぱい |

**음성 규칙**:
- *h/b/p* alternation (本: *hon/bon/pon*)
- *s/sh* alternation (分: *fun/pun*)
- *k/g* alternation (階: *kai/gai*)

#### Korean Counters (수사 + 단위 명사) — Native vs Sino

| Counter | Use For | Native (1-99) | Sino-Korean (100+) | Notes |
|---------|---------|---------------|-------------------|-------|
| 개 (gae) | General objects | 하나, 둘, 셋... | 일개, 이개... | Default fallback |
| 명 (myeong) | People (polite) | 한 명, 두 명 | 일 명, 이 명 | Use *bun* for honorific |
| 분 (bun) | People (honorific) | 한 분, 두 분 | - | Elders, customers |
| 마리 (mari) | Animals | 한 마리, 두 마리 | - | |
| 권 (gwon) | Books | 한 권, 두 권 | - | |
| 장 (jang) | Flat things (paper, tickets) | 한 장, 두 장 | - | |
| 대 (dae) | Machines, cars | 한 대, 두 대 | - | |
| 병 (byeong) | Bottles | 한 병, 두 병 | - | |
| 잔 (jan) | Cups/glasses | 한 잔, 두 잔 | - | |
| 그릇 (geureut) | Bowls | 한 그릇, 두 그릇 | - | |
| 번 (beon) | Times | 한 번, 두 번 | - | |
| 시 (si) | Hour (o'clock) | 한 시, 두 시 | - | Native for hour |
| 분 (bun) | Minute | 한 분(?) → 일 분 | - | Sino for minute |
| 살 (sal) | Age | 한 살, 두 살 | - | Native |
| 세 (se) | Age (formal) | - | 일 세, 이 세 | Sino |

**핵심 규칙**: 고유 한국어 숫자 (1-99) + 고유 수량사; 한자 한국어 + 한자 수량사. *Age* uses native (*sal*) or Sino (*se*).

#### Chinese Counters / Measure Words (量词)

| Measure Word | Pinyin | Use For | Example |
|--------------|--------|---------|---------|
| 个 | gè | General (default) | 三个苹果 (3 apples) |
| 位 | wèi | People (polite) | 两位客人 (2 guests) |
| 只 | zhǐ | Animals (small) | 一只猫 (1 cat) |
| 条 | tiáo | Long thin things (fish, rivers, pants) | 一条鱼 (1 fish) |
| 张 | zhāng | Flat things (paper, tickets, beds) | 三张票 (3 tickets) |
| 本 | běn | Books | 两本书 (2 books) |
| 双 | shuāng | Pairs (shoes, chopsticks) | 一双筷子 (1 pair chopsticks) |
| 辆 | liàng | Vehicles | 一辆车 (1 car) |
| 台 | tái | Machines, electronics | 一台电脑 (1 computer) |
| 杯 | bēi | Cups/glasses | 一杯水 (1 glass water) |
| 碗 | wǎn | Bowls | 两碗饭 (2 bowls rice) |
| 次 | cì | Times | 去过三次 (went 3 times) |
| 遍 | biàn | Times (complete cycles) | 读了两遍 (read twice) |

**Special**: *两 (liǎng)* not *二 (èr)* before classifiers for "two" — *两个人*, *两本书*.

---

## 숫자 관련 문화적 노트

### Japanese
- **4 (shi/yon)** & **9 (ku/kyuu)** — avoided in hospitals, hotels, gifts (*shini* = death, *ku* = suffering)
- **선물 금전**: 홀수 선호 (3, 5, 7); 4, 9, 짝수 회피
- **손가락 셈**: 검지 = 1, 검지+중지 = 2... 엄지 접힘 = 5

### Korean
- **4 (사)** — *테트라포비아*, 4층 엘리베이터 "F" 표기
- **추석/설날**: 흰 봉투 돈, 홀수 금액
- **나이**: 한국식 나이 = (현재 연도 - 출생 연도) + 1 (1월 1일 모두 +1)

### Chinese
- **4 (sì)** — 회피 (*사 = 죽음 sǐ*과 동음); 8 (bā) = 행운 (*발 fā*); 6 (liù) = 순탄 (*류 liú*)
- **전화번호/차번호**: 8 프리미엄, 4 회피
- **홍바오 (red envelopes)**: 짝수 금액 (4 제외); 666, 888, 999 행운

### Spanish
- **Billions**: *billón* = 10¹² (long scale) vs 미국 *billion* = 10⁹ — 금융 번역 함정
- **소수점 구분자**: 쉼표 (1,5 = 1.5); 천 단위 구분자: 점 또는 공백 (1.000 or 1 000)

### English
- **And**: "one hundred **and** one" (UK) vs "one hundred one" (US)
- **큰 숫자**: short scale (million=10⁶, billion=10⁹, trillion=10¹²)

---

## 학습자 의사결정 가이드

| 학습 언어 | 먼저 마스터 | 이유 |
|-----------------|--------------|-------|
| **Japanese** | *hon, mai, hiki, kai, fun, sai* + 1-10 irregular forms | 일상 셈의 80% 커버 |
| **Korean** | 고유어 1-10 + *gae, myeong, mari, jang, beon, si, sal* | 고유 숫자 + 상위 7 수량사 = 생존 |
| **Chinese** | *ge, wei, zhang, ben, tiao, liang, bei, ci* + 两 vs 二 rule | *ge* 보편 fallback; *两* 수량사 앞 의무 |
| **Spanish** | 기수 1-100 + *millón/millones* 일치 (*un millón DE*) | *Millón* requires *de*; *cien* vs *ciento* |
| **English** | 서수 접미사 (-st, -nd, -rd, -th) + 숫자 앞 "a/an" | "a hundred" vs "one hundred" |

### 다국어 연습 시나리오

#### "맥주 3병 주문"
- EN: "Three beers, please."
- ES: "Tres cervezas, por favor."
- JP: "ビールを三本ください。" (*biiru o san-bon kudasai*)
- KR: "맥주 세 병 주세요." (*maekju se byeong juseyo*)
- CH: "来三瓶啤酒。" (*lái sān píng píjiǔ*)

#### "남동생 2명 있습니다"
- EN: "I have two younger brothers."
- ES: "Tengo dos hermanos menores."
- JP: "弟が二人います。" (*otouto ga futari imasu*) — *futari* (2 people)
- KR: "남동생이 둘 있어요." (*namdongsaeng-i dul isseoyo*) — native *dul*
- CH: "我有两个弟弟。" (*wǒ yǒu liǎng gè dìdi*) — *liǎng* + *ge*

#### "일본 5번째"
- EN: "This is my fifth time in Japan."
- ES: "Es la quinta vez que voy a Japón."
- JP: "日本に来るのは五回目です。" (*nihon ni kuru no wa go-kaime desu*)
- KR: "일본에 온 게 다섯 번째예요." (*ilbon-e on ge daseot beonjjae-yeyo*)
- CH: "这是我第五次来日本。" (*zhè shì wǒ dì wǔ cì lái Rìběn*)

---

## 핵심 대조 (종합)

| 대조 | 통찰 |
|----------|---------|
| **이중 숫자 시스템** | 한국어만 1-99 고유어 + 100+ 한자어 이중 시스템. 일본어/중국어/스페인어/영어는 단일 (단 2 = 두/两 만 예외) |
| **큰 숫자 단위** | CN/JP/KR 만(10,000) 단위, EN/ES 천 단위. 1억 = 100 million. 1조 = 1 trillion (단 한국 1조 = 10¹², 미국 trillion) |
| **수량사 의무성** | JP/KR/CH 의무 / EN/ES 선택. 영어 "three apples" = 스페인어 "tres manzanas" (수량사 없음) |
| **단위 1의 발음 변화** | 일본어 카운터 1/6/8/10 발음 변화 (히토, 로쿠, 하치, 토 vs いち, ろく, はち, とお). 한국어 시간/분 한자어 변화 (한 시, 일 분). |
| **4의 회피** | 일본어 4 (시=死), 중국어 4 (스이=死), 한국어 4층 F 표기. 영어/스페인어 4 무회피 |

---

## 🇰🇷 한국어 학습자 노트 (Korean Learner Notes)

> 본 섹션은 한국어 학습자 대상의 추가 학습 가이드입니다.

### 한국어 화자가 다른 4개 언어 숫자/수량사를 학습할 때 흔히 마주치는 함정

1. **한국어 이중 숫자 시스템의 고유성**:
   - 한국어는 1-99 고유어 (하나, 둘, 셋...) + 100+ 한자어 (백, 천, 만...). 일본어/중국어/스페인어/영어는 단일 시스템.
   - **함정**: 한국어 학습자가 다른 4개 언어에 이중 시스템 매핑 시도 → 실패. 일본어/중국어는 단일 한자, 영어/스페인어 단일 라틴.
   - **훈련법**: 한국어 이중 시스템의 **고유성** 인지. 다른 언어 학습 시 단일 시스템으로 학습.

2. **시/분 시간 한자어 vs 수량사 고유어 구분**:
   - 한국어 시간: "한 시" (고유어 시), "한 분" (한자어 분, 그러나 발음상 한 분 OK). "한 시간" (시간 단위 = 한 + 시간).
   - **함정**: "한 분" — 분이 한자어 분(分)이지만 한국어 발음은 "한 분" (고유어 패턴) 사용. 그러나 격식에서는 "일 분".
   - **훈련법**: 시간(시/분/년) = 한자어, 사람/동물/사물(개/명/마리) = 고유어 — 수량사 매트릭스. 단, 일상에서는 시간/수량사 모두 고유어 패턴 사용.

3. **수량사 의무 사용의 한국어/일본어/중국어 동일성**:
   - JP/KR/CH 모두 수량사 의무. "3 사과" → 한국어 "3 사과" (X) vs "3개 사과" (O) / 일본어 "3 りんご" (X) vs "3個のりんご" (O) / 중국어 "3 苹果" (X) vs "3个苹果" (O).
   - EN/ES는 수량사 선택. "three apples" (O), "3 manzanas" (O) — 수량사 없이 가능.
   - **함정**: 한국어 학습자가 영어/스페인어에 한국어 패턴 적용 → 영어 "three apples"를 "three 개 apples" 식 적용 (X).
   - **훈련법**: JP/KR/CH = 수량사 의무, EN/ES = 선택 — **2개 시스템** 명시적 구분. 영어/스페인어 학습 시 수량사 무사용 가능.

4. **"두/二/两" 변형**:
   - 중국어: "2명" → "两个人" (两 gè rén, O) / "二个人" (X). 수량사 앞에는 两 (liǎng) 사용, 二는 다른 문맥.
   - 한국어: "두 명" (O) / "이 명" (X, 일반적). 그러나 200 = "이백" (Sino) vs "이백 명" (200명).
   - **함정**: 중국어 "两"의 특수성 — 二 대신 两 사용 시점 학습 필수. 한국어 "두"는 한자어 2 (이) 와 구분 — "두 명" (O) vs "이 명" (X).
   - **훈련법**: 중국어 两 vs 二 매트릭스 — 수량사 앞 = 两 (两本书). 한국어 두 vs 이 — 단위 명사 앞 = 두 (두 명), 단독 또는 한자어 100+ = 이 (이백).

5. **4의 회피 (테트라포비아)**:
   - 한국어 4층 = F층 (엘리베이터). 일본어 4 = shi (死 = 죽음). 중국어 4 = sì (死 = 죽음).
   - 영어/스페인어 4 무회피. 그러나 영어/스페인어 "thirteen" 행운 vs 한국어/중국어/일본어 4 회피 비교.
   - **함정**: 4 회피는 동아시아 문화. 영어권 호텔 4층 = 4층 (F 없음).
   - **훈련법**: 5개 문화 숫자 회피 매트릭스 — 4 (KR/CN/JP), 13 (서양 일부), 7 (서양 행운), 8 (CN 행운), 9 (JP 회피). **문화별 숫자 회피 학습**.

### 학습 전략

1. **우선순위 1**: 한국어 이중 숫자 시스템 마스터 — 고유어 1-99 + 한자어 100+. **한국어 고유 메커니즘**, 다른 언어와 다름.
2. **우선순위 2**: JP/KR/CH 수량사 의무 vs EN/ES 선택 — 5개 언어 수량사 매트릭스. 한국어 학습자가 EN/ES 학습 시 수량사 무사용 가능.
3. **우선순위 3**: 시/분 시간 한자어 vs 사람/동물/사물 고유어 매트릭스 — 한국어 시간 = 한자어 (시/분/년), 단위 명사 = 고유어 (개/명/마리). 한자 매핑 가능 여부 사전.
4. **우선순위 4**: 만 단위 매트릭스 — KR/CN/JP 동일 (1만, 1억, 1조) vs EN/ES 천 단위 (1,000 = 1 thousand). 1억 = 100 million = 1 億 (JP) = 一亿 (CN). 1조 = 1 trillion (CN/JP 10¹²) vs 한국 1조 10¹².
5. **우선순위 5**: 문화별 숫자 회피 — 4 (KR/CN/JP), 13 (서양 일부), 8 (CN 행운), 9 (JP 회피), 7 (서양 행운). **동아시아 4 회피** 명시 학습.

### 관련 한국어 위키 페이지

- [[time-calendar]] — 시간 표현 (한자어 시간)
- [[greetings]] — 시간 기반 인사
- [[travel-essentials]] — 가격/날짜/시간
- [[food-dining]] — 음식 수량사
- [[politeness-honorifics]] — 경어 수량사 (분)

---

## 관련 페이지

- `[[greetings]]` — 시간 표현 사용
- `[[travel-essentials]]` — 가격, 날짜, 스케줄
- `[[food-dining]]` — 음식 수량사
- `[[politeness-honorifics]]` — 경어 수량사 (*bun, wei, mei, sama*)

## 출처

- English: `[English/vocabulary/basic-vocabulary]`
- Spanish: `[Spanish/vocabulary/basic-vocabulary]`, `[Spanish/vocabulary/time-prepositions-vocabulary]`
- Japanese: `[Japanese/vocabulary/jp-counters]`, `[Japanese/vocabulary/kanji-n5]`, `[Japanese/sources/2026-07-13_Kanji_N5_100]`
- Korean: `[[index]]`, `[Korean/vocabulary/topik1-starter]`, `[Korean/sources/daily-life-basics]`
- Chinese: `[Chinese/vocabulary/numbers-zh]`, `[Chinese/vocabulary/measure-words-zh]`, `[Chinese/sources/pinyin-basics-zh]`

---

**원본 (영어)**: [[numbers-counters]] | **관련 미러**: [[numbers-counters.es|Spanish]] · [[numbers-counters.ja|Japanese]] · [[numbers-counters.zh|Chinese]] | **정책**: ADR-0006
