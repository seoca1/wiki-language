# 가족 역할 & 친족 — Cross-Language Comparison (한국어판)

> 원본: [[family-roles-comparison]] (English) | 작성일: 2026-08-19 | ADR-0006
> **5개 언어 가족 역할 비교** — English · Spanish · Japanese · Korean · Chinese

---

## 빠른 참조 표

### 직계 가족

| 관계 | English | Spanish | Japanese | Korean | Chinese |
|----------|---------|---------|----------|--------|---------|
| **아버지** | Father | Padre | 父 (chichi casual) / 父親 (chichioya formal) | 아버지 (abeoji) / 부 (bu, formal written) | 父亲 (fùqin) / 爸爸 (bàba) |
| **어머니** | Mother | Madre | 母 (haha casual) / 母親 (hahaoya formal) | 어머니 (eomeoni) / 모 (mo, formal written) | 母亲 (mǔqin) / 妈妈 (māma) |
| **아들** | Son | Hijo | 息子 (musuko) | 아들 (adeul) | 儿子 (érzi) |
| **딸** | Daughter | Hija | 娘 (musume) | 딸 (ttal) | 女儿 (nǚ'ér) |
| **형 (오빠)** | Older brother | Hermano mayor | 兄 (ani) | 형 (hyeong, of male) / 오빠 (oppa, female speaker) | 哥哥 (gēge) |
| **남동생** | Younger brother | Hermano menor | 弟 (otōto) | 남동생 (namdongsaeng) | 弟弟 (dìdi) |
| **누나 (언니)** | Older sister | Hermana mayor | 姉 (ane) | 누나 (nuna, of male) / 언니 (eonni, female speaker) | 姐姐 (jiějie) |
| **여동생** | Younger sister | Hermana menor | 妹 (imōto) | 여동생 (yeodongsaeng) | 妹妹 (mèimei) |

### 조부모

| 관계 | English | Spanish | Japanese | Korean | Chinese |
|----------|---------|---------|----------|--------|---------|
| **할아버지 (부계)** | Grandfather | Abuelo | 祖父 (sofu) | 할아버지 (harabeoji) | 爷爷 (yéye) |
| **할머니 (부계)** | Grandmother | Abuela | 祖母 (sobo) | 할머니 (halmeoni) | 奶奶 (nǎinai) |
| **외할아버지 (모계)** | Grandfather | Abuelo materno | 外祖父 (gaisofu) | 외할아버지 (oe-harabeoji) | 外公 (wàigōng) |
| **외할머니 (모계)** | Grandmother | Abuela materna | 外祖母 (gaisobo) | 외할머니 (oe-halmeoni) | 外婆 (wàipó) |

### 확장 가족

| 관계 | English | Spanish | Japanese | Korean | Chinese |
|----------|---------|---------|----------|--------|---------|
| **삼촌 (부계)** | Uncle | Tío | 伯父 (oji) / 叔父 (oji) | 삼촌 (samchon) | 伯父 / 叔叔 |
| **외삼촌 (모계)** | Uncle | Tío materno | 舅父 (oji) | 외삼촌 (oe-samchon) | 舅父 / 舅舅 |
| **이모/고모** | Aunt | Tía | 伯母 (oba) / 叔母 (oba) | 이모 (imo, maternal) / 큰어머니 (keun-eomeoni) | 伯母 / 姑姑 |
| **사촌 (남)** | Cousin | Primo | いとこ (itoko) | 사촌 (sachon) | 表兄弟 / 堂兄弟 |
| **조카 (남)** | Nephew | Sobrino | 甥 (oi) | 조카 (joka, nephew/niece) | 侄子 (zhízi) |
| **조카 (여)** | Niece | Sobrina | 姪 (mei) | 조카 (joka) | 侄女 (zhínǚ) |

### 시댁/외가 (동아시아 특유의 복잡성)

| 관계 | English | Spanish | Japanese | Korean | Chinese |
|----------|---------|---------|----------|--------|---------|
| **시아버지** | Father-in-law | Suegro | 舅 (shūto, husband of daughter) / 姑 (shūto, father of spouse — opposite!) | 시아버지 (siabeoji, husband's father) | 公公 (gōnggōng) |
| **시어머니** | Mother-in-law | Suegra | 姑 (shūtobo) / 舅 (shūtobo — varies) | 시어머니 (sieomeoni) | 婆婆 (pópo) |
| **자형/매형** | Brother-in-law (sister's husband) | Cuñado | 義兄 (gikei) / 義弟 (gitei) | 자형 (jahyeong, older sister's husband) / 매형 (maehyeong) | 姐夫 (jiěfu) |
| **형수/嫂子** | Sister-in-law (brother's wife) | Cuñada | 義姉 (gishi) / 義妹 (gimai) | 형수 (hyeongsu, older brother's wife) | 嫂子 (sǎozi) |

### 배우자 & 파트너

| 용어 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **남편** | Husband | Esposo / Marido | 夫 (otto) / ご主人 (goshujin — polite) | 남편 (nampyeon) | 丈夫 (zhàngfu) |
| **아내** | Wife | Esposa / Mujer | 妻 (tsuma) / 奥さん (okusan — polite) | 아내 (anae) | 妻子 (qīzi) |
| **남자친구** | Boyfriend | Novio | 彼氏 (kareshi) | 남자친구 | 男朋友 |
| **여자친구** | Girlfriend | Novia | 彼女 (kanojo) | 여자친구 | 女朋友 |
| **약혼자** | Fiancé / Fiancée | Novio / Novia (compromise) | 婚約者 (kon'yakusha) | 약혼자 (yakhonja) | 未婚夫 / 未婚妻 |

### 문화 개념

| 개념 | English | Spanish | Japanese | Korean | Chinese |
|---------|---------|---------|----------|--------|---------|
| **친족 복잡성** | 단순 (uncle = uncle) | 중간 (tío/tía) | 높음 (舅/姑 구분) | 최고 (시/외 family 분리) | 높음 (舅父/姑父 구분) |
| **연상 의식** | 덜 강조 | Tío mayor vs menor | 매우 중요 (兄/弟, 姉/妹) | 결정적 (형/동생, 누나/동생) | 중요 (哥哥/弟弟) |
| **존경 가족 호칭** | 캐주얼 | 캐주얼 | 다수 (お父さん/お母さん) | 다수 (아버지/어머니) | 캐주얼 (爸爸/妈妈) |
| **가족 격식** | 제한적 | Tío vs tía | 광범위 | 가장 광범위 | 중간 |

---

## 언어별 상세

### 🇬🇧 영어 (English)
- **핵심 용어**: "Relative" (일반); "Immediate family" vs "Extended family"
- **패턴**: 단순 호칭; 가족 간 first name 가능
- **출처**: `[[family-vocabulary]]`

### 🇪🇸 스페인어 (Spanish)
- **핵심 용어**: "Familia" (family), "Pariente" (relative), "Primo" (cousin)
- **패턴**: 성 일치: tío/tía, primo/prima; "Sobrino" vs "sobrino" by gender
- **출처**: `[[family-vocabulary]]`

### 🇯🇵 일본어 (Japanese)
- **핵심 용어**: 家族 (kazoku = family), 親戚 (shinseki = relatives); 義理 (giri = in-law)
- **패턴**: 여러 단어 for same relation (兄/兄さん); 엄격한 연상 표지 (兄/弟, 姉/妹)
- **출처**: `[[family-vocabulary]]`

### 🇰🇷 한국어 (Korean)
- **핵심 용어**: 가족 (gajok), 친척 (chincheok); 시 (in-laws wife's family) vs 외 (in-laws husband's family)
- **패턴**: 형제 호칭에 화자 성별이 영향 (형/오빠); 엄격한 연상
- **출처**: `[[family-vocabulary]]`

### 🇨🇳 중국어 (Chinese)
- **핵심 용어**: 家庭 (jiātíng = family), 亲戚 (qīnqi = relatives); 长辈 (zhǎngbèi = elder generation)
- **패턴**: 舅/姑 구분 (모계 vs 부계 시댁); 지역 변이
- **출처**: N/A — 중국어 가족 테마 미정

---

## 핵심 대조 (종합)

| 대조 | 학습자 시사점 |
|------|----------------|
| **친족 복잡성** | KR > JP > ZH > ES > EN — 한국어가 가장 분화된 친족 용어 보유 |
| **연상 언어** | 동아시아 언어 모두 형제 연상 표지; 서양 언어는 미표지 |
| **시부모 정확성** | 동아시아 언어는 모계 vs 부계 시부모 구분; 영어 합병 |
| **가족 가치** | 동아시아 문화 (특히 CN/KR) 계층 강조; 서양 문화 더 평등적 |

---

## 학습자 의사결정 가이드

- **마스터해야 할 첫 10 가족 용어**:
  - EN: father, mother, brother, sister, son, daughter, grandfather, grandmother, uncle, aunt
  - ES: padre, madre, hermano, hermana, hijo, hija, abuelo, abuela, tío, tía
  - JP: 父(chichi), 母(haha), 兄(ani), 姉(ane), 息子(musuko), 娘(musume), 祖父(sofu), 祖母(sobo), 伯父/叔父(oji), 伯母/叔母(oba)
  - KR: 아버지, 어머니, 형/오빠, 누나/언니, 아들, 딸, 할아버지, 할머니, 삼촌, 이모/고모
  - CH: 父亲, 母亲, 哥哥, 姐姐, 儿子, 女儿, 爷爷, 奶奶, 伯父/叔叔, 伯母/姑姑

---

## 🇰🇷 한국어 학습자 노트 (Korean Learner Notes)

> 본 섹션은 한국어 학습자 대상의 추가 학습 가이드입니다.

### 한국어 화자가 다른 4개 언어 가족 역할을 배울 때 흔히 마주치는 함정

1. **"시(Si)/외(Oe)" 시부모 호칭 시스템의 한국 특수성**:
   - 한국어는 시부모를 4가지로 구분 — 시아버지 (남편 아버지) / 시어머니 (남편 어머니) / 장인 (아내 아버지) / 장모 (아내 어머니). 일본어 舅/姑 (shūto/shūtobo) 와 중국어 公公/婆婆 (gōnggōng/pópo) 도 구분하나 시스템 다름.
   - **함정**: 한국어 학습자가 영어 "father-in-law" 단순 사용 → 한국에서는 부부 누구의 부모인지에 따라 호칭 다름.
   - **훈련법**: 시댁/외가 매트릭스 — 시아버지/시어머니 (시댁) vs 장인/장모 (외가) — 한자 舅/姑 vs 岳父/岳母 매핑.

2. **4-방향 형제 호칭의 한국 고유성**:
   - 한국어는 형제 호칭에 4가지 (오빠/누나/형/언니) — 다른 4개 언어에 없는 시스템. 영어 older brother/sister 단순, 일본어 兄/弟/姉/妹 (성별 무관), 중국어 哥哥/弟弟/姐姐/妹妹 (성별 무관).
   - **함정**: 한국어 학습자가 영어 "older brother" 를 오빠/형 으로 단순 매핑 → 한국에서는 화자 성별에 따라 다름 (여성→남자 = 오빠, 남성→남자 = 형).
   - **훈련법**: 4-방향 호칭 매트릭스 — 화자 여성 → 남자 연상 = 오빠, 여자 연상 = 언니 / 화자 남성 → 남자 연상 = 형, 여자 연상 = 누나. 일본어 兄/弟 와의 차이 인지.

3. **"조카(Joka)" 의 성별 무관**:
   - 한국어 "조카" 는 남/여 조카 모두에 사용 — 영어 nephew/niece, 스페인어 sobrino/sobrina, 일본어 甥/姪, 중국어 侄子/侄女 의 성별 구분 없음.
   - **함정**: 한국어 학습자가 영어에서 nephew/niece 구분 → 한국에서는 조카 통일.
   - **훈련법**: 조카 어휘 학습 — 조카 (성별 무관) / 조카 남/조카 녀 (성별 구분 시). 한자 甥/姪/侄子/侄女 매핑.

4. **"약혼(Yakhon)" 의 한국 한자어**:
   - 한국어 "약혼" = 한자 約婚 — 결혼 약속 상태. 일본어 婚約 (kon'yaku), 중국어 订婚 (dìnghūn) 와 매칭.
   - **함정**: 한국어 학습자가 영어 "engagement" 를 약혼 으로 단순 번역 → 약혼 의 한자 차용 어휘 (약 = 약속, 혼 = 혼인) 모르면 어려움.
   - **훈련법**: 한자 결혼 어휘 매칭 — 婚/約/嫁/娶 의 JP/KR/CN 발음 + 의미.

5. **"남자친구/여자친구" 의 한국 직접 명명**:
   - 한국어 "남자친구" "여자친구" = boyfriend/girlfriend 직접 명명 — 일본어 彼氏/彼女 (kareshi/kanojo) / 중국어 男朋友/女朋友 / 스페인어 novio/novia / 영어 boyfriend/girlfriend.
   - **함정**: 한국어 학습자가 일본어 彼女 를 여자친구 로 번역 → 彼女 가 일상에서 "그녀/여자" 의미로도 사용되어 혼란. 중국어 女朋友 도 일상에서 "여자 친구" 의미.
   - **훈련법**: 연인 호칭 맥락 학습 — 彼氏/彼女/남자친구/여자친구/男朋友/女朋友 는 모두 "연인" 의미이나 일상 맥락에서 다른 의미 가능.

### 학습 전략

1. **우선순위 1**: 한국어 4-방향 형제 호칭 (오빠/누나/형/언니) 마스터 + 화자 성별 매핑.
2. **우선순위 2**: 시댁/외가 4가지 (시아버지/시어머니/장인/장모) + 한자 舅/姑/岳父/岳母 매핑.
3. **우선순위 3**: 조카 어휘 + 한자 甥/姪/侄子/侄女 매핑.
4. **우선순위 4**: 한자 가족 어휘 매칭 — 父/母/兄/姐/弟/妹 의 JP/KR/CN 발음.
5. **우선순위 5**: 연인 호칭 (彼氏/彼女/남자친구/여자친구/男朋友/女朋友) 의 맥락별 사용.

---

## 관련 페이지

- `[[greetings]]` — 가족 인사
- `[[dating-romance]]` — 로맨틱 관계
- `[[politeness-honorifics]]` — 언어와 가족 계층

## 출처

- `wiki/English/vocabulary/family-vocabulary.md`
- `wiki/Spanish/vocabulary/family-vocabulary.md`
- `wiki/Japanese/vocabulary/family-vocabulary.md`
- `wiki/Korean/vocabulary/family-vocabulary.md`
- 한국 친족 용어 (인류학 참고서)

---

**원본 (영어)**: [[family-roles-comparison]] | **관련 미러**: [[family-roles-comparison.es|Spanish]] · [[family-roles-comparison.ja|Japanese]] · [[family-roles-comparison.zh|Chinese]] | **정책**: ADR-0006