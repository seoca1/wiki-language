# 가족 & 친족 — Cross-Language Comparison (한국어판)

> 원본: [[family-kinship]] (English) | 작성일: 2026-08-19 | ADR-0006
> **5개 언어 가족·친족 비교** — English · Spanish · Japanese · Korean · Chinese

---

## 빠른 참조 표

### 🇰🇷 한국어 (가족) 어휘

| 한국어 | 의미 |
|--------|------|
| 가족 (gajok) | family |
| 아버지 (abeoji) | father (formal) |
| 어머니 (eomeoni) | mother (formal) |
| 형 (hyeong) | older-brother (male-speaker) |
| 누나 (nuna) | older-sister (male-speaker) |
| 오빠 (oppa) | older-brother (female-speaker) |
| 언니 (eonni) | older-sister (female-speaker) |
| 할아버지 (harabeoji) | grandfather (paternal) |
| 할머니 (halmeoni) | grandmother (paternal) |

### 🇯🇵 일본어 (家族) 어휘

| 일본어 | 의미 |
|--------|------|
| 家族 (kazoku) | family |
| 父 (chichi) | father (humble) |
| お父さん (otousan) | father (respectful) |
| 母 (haha) | mother (humble) |
| お母さん (okaasan) | mother (respectful) |
| お兄さん (oniisan) | older-brother |
| お姉さん (oneesan) | older-sister |
| お爺さん (ojiisan) | grandfather |
| お婆さん (obaasan) | grandmother |

### 🇬🇧 영어 어휘

- family
- father / dad / daddy
- mother / mom / mommy
- brother / sis
- grandfather / grandma
- uncle / aunt / cousin / nephew / niece

### 🇪🇸 스페인어 (familia) 어휘

| 스페인어 | 의미 |
|---------|------|
| familia | family |
| padre / papá | father / dad |
| madre / mamá | mother / mom |
| hermano / hermana | brother / sister |
| abuelo / abuela | grandfather / grandmother |
| tío / tía | uncle / aunt |
| primo / prima | cousin |
| sobrino / sobrina | nephew / niece |

### 🇨🇳 중국어 (家庭) 어휘

| 중국어 | 의미 |
|--------|------|
| 家庭 (jiātíng) | family |
| 父亲 (fùqin) | father (formal) |
| 爸爸 (bàba) | dad |
| 母亲 (mǔqin) | mother (formal) |
| 妈妈 (māma) | mom |
| 哥哥 (gēge) | older-brother |
| 姐姐 (jiějie) | older-sister |
| 爷爷 (yéye) | grandfather (paternal) |
| 奶奶 (nǎinai) | grandmother (paternal) |

### 문화적 관행

#### 🇰🇷 한국 고유
- 칠순 (chilsun) — 70th birthday celebration
- 제사 (jesa) — ancestral ritual
- 큰 (keun) — eldest line honorific prefix

#### 🇯🇵 일본 고유
- 敬老の日 (Keirō no Hi) — Respect for the Aged Day
- お盆 (Obon) — ancestral spirits festival
- 家族 (kazoku) — "ideal nuclear family" (post-war construction)

#### 🇪🇸 스페인 고유
- Compadrazgo — co-parenthood network
- Quinceañera — 15th birthday celebration (girls)
- Sobrina — emphasis on extended-family networks

#### 🇨🇳 중국 고유
- 孝顺 (xiàoshùn) — filial piety
- 宗族 (zōngzú) — clan system
- 春节 (Chūnji) — family reunion celebration
- 辈分 (bèifèn) — generational hierarchy

---

## 학습자 의사결정 가이드

- **마스터해야 할 첫 10 가족 어휘**:
  - EN: family, father, mother, brother, sister, son, daughter, grandfather, grandmother, uncle/aunt
  - ES: familia, padre, madre, hermano, hermana, hijo, hija, abuelo, abuela, tío/tía
  - JP: 家族(kazoku), 父(chichi)/お父さん(otousan), 母(haha)/お母さん(okaasan), 兄(ani)/弟(otōto), 姉(ane)/妹(imōto), 息子(musuko), 娘(musume), 祖父(sofu), 祖母(sobo), 伯父/叔父(oji)
  - KR: 가족, 아버지/아빠, 어머니/엄마, 형/오빠/남동생, 누나/언니/여동생, 아들, 딸, 할아버지, 할머니, 삼촌/이모/외삼촌
  - CH: 家庭(jiātíng), 父亲/爸爸, 母亲/妈妈, 哥哥/弟弟, 姐姐/妹妹, 儿子, 女儿, 爷爷, 奶奶, 伯父/叔叔

---

## 🇰🇷 한국어 학습자 노트 (Korean Learner Notes)

> 본 섹션은 한국어 학습자 대상의 추가 학습 가이드입니다.

### 한국어 화자가 다른 4개 언어 가족 어휘를 배울 때 흔히 마주치는 함정

1. **4-방향 형제 호칭의 한국 고유성**:
   - 한국어는 형제 호칭에 4가지 (오빠/누나/형/언니) — 다른 4개 언어에 없는 시스템. 영어 "older brother" 단순, 일본어 兄/姉/兄さん/お姉さん, 중국어 哥哥/姐姐.
   - **함정**: 한국어 학습자가 영어 "older brother" 를 오빠/형 으로 단순 매핑 → 한국에서는 화자 성별에 따라 다름 (여성→남자 = 오빠, 남성→남자 = 형).
   - **훈련법**: 4-방향 호칭 매트릭스 — 화자 여성 → 남자 연상 = 오빠, 여자 연상 = 언니 / 화자 남성 → 남자 연상 = 형, 여자 연상 = 누나. 영어 단순화 (older brother/sister) 와 구분.

2. **"제사(Jesa)" 의 한국 조상 의례**:
   - 한국어 "제사" = 조상 숭배 의례 (음력 추석/설날/기일) — 일본어 お盆 (Obon) 과 중국어 祭祖 (jìzǔ) 와 유사.
   - **함정**: 한국어 학습자가 일본어 お盆 와 동일시 → 한국 제사 의 절차/음식/제기 차이 무시.
   - **훈련법**: 제사 어휘화 — 제사 지내다/제사 상/제기 (祭器)/제물. 일본어 お盆/お彼岸/日本式霊祭 와 비교.

3. **"호칭 -님" 시스템의 한국 고유성**:
   - 한국어는 가족 호칭에 -님 (존경) 결합 — 한국어만 직접 결합. 아버지→어머님이 아니라 아버지/어머니 그대로 사용. 그러나 다른 가족에게는 -님 사용 (아버님/어머님/오라버님).
   - **함정**: 한국어 학습자가 일본어 先生 (sensei) 의 단일 존경과 동일시 → 한국어는 -님 결합이 가변적 (일부 호칭만).
   - **훈련법**: -님 결합 매트릭스 — 아버지 (님 없음) / 아버님 (존경) / 어머님 (존경) / 시어머님 (시댁 어머니 존경) / 선생님 (교사 존경). 일본어 先生 와 다른 구조.

4. **"효도(Hyodo/孝)" 의 동아시아 공유와 차이**:
   - 한국어 "효도" + 중국어 孝 + 일본어 孝 (kō) = 부모 공경. 그러나 현대 한국에서 효도 의식 변화.
   - **함정**: 한국어 학습자가 영어 "filial piety" 를 고대 개념으로만 이해 → 현대 한국/중국/일본 모두 변화.
   - **훈련법**: 한자 孝 의 JP (kō) / CH (xiào) / KR (효) 매칭 + 현대 변형 학습. 모시는 (방문) vs 효도 (전통) 차이.

5. **"큰(Keun)" 한국 장자 어휘**:
   - 한국어 "큰" = eldest line 존경 접두사 (큰아버지 = 큰 아버지 = eldest uncle). 다른 4개 언어에는 없는 호칭.
   - **함정**: 한국어 학습자가 "큰" 을 단순 "big" 으로 번역 → 한국 장자 문화 무시.
   - **훈련법**: 큰 어휘 학습 — 큰아버지/큰어머니/큰집. 중국어 伯父 (bófù, eldest uncle) / 伯母 (bómǔ, eldest aunt) 와 비교.

### 학습 전략

1. **우선순위 1**: 한국어 4-방향 형제 호칭 (오빠/누나/형/언니) 마스터 + 화자 성별 매핑.
2. **우선순위 2**: 시댁/외가 4가지 (시아버지/시어머니/장인/장모) + 한자 舅/姑/岳父/岳母 매핑.
3. **우선순위 3**: 한자 가족 어휘 매칭 — 父/母/兄/姐/弟/妹 의 JP/KR/CN 발음.
4. **우선순위 4**: -님 호칭 결합 매트릭스 (아버님/어머님/시어머님/선생님) 학습.
5. **우선순위 5**: 효도 (KR) / 孝 (JP/CN) / filial piety (EN) 의 현대적 변형.

---

## 관련 페이지

- `[[theme-vocabulary]]`
- `[[culture]]`
- `[[index]]`
- `[[untranslatable-concepts]]`
- `[[greetings]]`

## 출처

- 관련: `Language/wiki/{Korean,Japanese,English,Spanish,Chinese}/vocabulary/`
- 관련: `Language/wiki/{Korean,Japanese,English,Spanish,Chinese}/culture/`

---

**원본 (영어)**: [[family-kinship]] | **관련 미러**: [[family-kinship.es|Spanish]] · [[family-kinship.ja|Japanese]] · [[family-kinship.zh|Chinese]] | **정책**: ADR-0006