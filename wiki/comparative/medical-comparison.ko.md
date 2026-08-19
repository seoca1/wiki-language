# 의료 & 건강 — 다국어 비교 (한국어판)

> 원본: [[medical-comparison]] (English) | 작성일: 2026-08-20 | ADR-0006
> **5개 언어 의료/건강 어휘 비교**

---

## 빠른 참조 표

### 의료 전문가

| 전문가 | English | Spanish | Japanese | Korean | Chinese |
|--------------|---------|---------|----------|--------|---------|
| **의사** | Doctor / Physician | Doctor / Médico | 医者 (isha) / 医師 (ishi) | 의사 (uisa) | 医生 (yīshēng) / 大夫 (dàifu) |
| **치과 의사** | Dentist | Dentista | 歯科医 (shikai) | 치과 의사 (chigwa uisa) | 牙医 (yáyī) |
| **간호사** | Nurse | Enfermero / Enfermera | 看護師 (kangoshi) | 간호사 (ganhosa) | 护士 (hùshì) |
| **약사** | Pharmacist | Farmacéutico | 薬剤師 (yakuzaishi) | 약사 (yaksa) | 药剂师 (yàojìshī) |
| **외과 의사** | Surgeon | Cirujano | 外科医 (gekai) | 외과 의사 (oegwa uisa) | 外科医生 (wàikē yīshēng) |
| **소아과 의사** | Pediatrician | Pediatra | 小児科医 (shōnikai) | 소아과 의사 (soagwa uisa) | 儿科医生 (érkē yīshēng) |
| **정신과 의사** | Psychiatrist | Psiquiatra | 精神科医 (seishinkai) | 정신과 의사 (jeongsingwa uisa) | 精神科医生 (jīngshénkē yīshēng) |

### 병원 과

| 과 | English | Spanish | Japanese | Korean | Chinese |
|------------|---------|---------|----------|--------|---------|
| **내과** | Internal medicine | Medicina interna | 内科 (naika) | 내과 (naegwa) | 内科 (nèikē) |
| **외과** | Surgery | Cirugía | 外科 (geka) | 외과 (oegwa) | 外科 (wàikē) |
| **소아과** | Pediatrics | Pediatría | 小児科 (shōnika) | 소아과 (soagwa) | 儿科 (érkē) |
| **정형외과** | Orthopedics | Ortopedia | 整形外科 (seikeigeka) | 정형외과 (jeonghyeong oegwa) | 骨科 (gǔkē) |
| **피부과** | Dermatology | Dermatología | 皮膚科 (hifuka) | 피부과 (pibugwa) | 皮肤科 (pífūkē) |
| **이비인후과** | ENT / Otolaryngology | Otorrinolaringología | 耳鼻咽喉科 (jibi inkōka) | 이비인후과 (ibiinhugwa) | 耳鼻喉科 (ěrbíhóukē) |
| **안과** | Ophthalmology | Oftalmología | 眼科 (ganka) | 안과 (angwa) | 眼科 (yǎnkē) |
| **심장내과** | Cardiology | Cardiología | 循環器科 (junkankika) | 순환기과 (sunhwangigwa) | 心内科 (xīnnèikē) |
| **산부인과** | OB/GYN | Ginecología / Obstetricia | 産婦人科 (sanfujinka) | 산부인과 (sanbuingwa) | 妇产科 (fùchǎnkē) |
| **응급** | Emergency | Urgencias | 救急 (kyūkyū) / 救急外来 | 응급 (eunggeup) | 急诊 (jízhěn) |

### 신체 시스템

| 시스템 | English | Spanish | Japanese | Korean | Chinese |
|--------|---------|---------|----------|--------|---------|
| **심혈관** | Cardiovascular | Cardiovascular | 循環器系 (junkankikei) | 순환기계 (sunhwangigye) | 心血管系统 (xīnxuèguǎn) |
| **호흡기** | Respiratory | Respiratorio | 呼吸器系 (kokyūkikei) | 호흡기계 (hoheopigye) | 呼吸系统 (hūxī) |
| **소화기** | Digestive | Digestivo | 消化器系 (shōkakikei) | 소화기계 (sohwagigye) | 消化系统 (xiāohuà) |
| **신경** | Nervous | Nervioso | 神経系 (shinkeikei) | 신경계 (singlyeonggye) | 神经系统 (shénjīng) |
| **근골격** | Musculoskeletal | Musculoesquelético | 筋骨格系 (kinkokkakukei) | 근골격계 (geungolgyeoggye) | 肌肉骨骼系统 (jīròu gǔgé) |
| **면역** | Immune | Inmunitario | 免疫系 (men'ekikei) | 면역계 (myeonyeonggye) | 免疫系统 (miǎnyì) |
| **내분비** | Endocrine | Endocrino | 内分泌系 (naibunpitsukei) | 내분비계 (naebunbigye) | 内分泌系统 (nèifēnmì) |

### 일반 증상

| 증상 | English | Spanish | Japanese | Korean | Chinese |
|---------|---------|---------|----------|--------|---------|
| **발열** | Fever | Fiebre | 熱 (netsu) | 열 (yeol) / 발열 (bal-yeol) | 发烧 (fāshāo) |
| **두통** | Headache | Dolor de cabeza | 頭痛 (zutsū) | 두통 (dutong) | 头痛 (tóutòng) |
| **기침** | Cough | Tos | 咳 (seki) | 기침 (gichim) | 咳嗽 (késòu) |
| **목 아픔** | Sore throat | Dolor de garganta | 喉の痛み (nodo no itami) | 목 아픔 (mok apeum) | 喉咙痛 (hóulóng tòng) |
| **복통** | Stomachache | Dolor de estómago | 腹痛 (fukutsū) | 복통 (boktong) | 胃痛 (wèitòng) / 肚子痛 |
| **메스꺼움** | Nausea | Náusea | 吐き気 (hakike) | 메스꺼움 (meseukkeo um) | 恶心 (ěxīn) |
| **어지러움** | Dizziness | Mareo | めまい (memai) | 어지러움 (eojireo um) | 眩晕 (xuànyùn) |
| **피로** | Fatigue | Fatiga | 疲労 (hirō) | 피로 (piro) | 疲劳 (píláo) |
| **설사** | Diarrhea | Diarrea | 下痢 (geri) | 설사 (seolsa) | 腹泻 (fùxiè) |
| **발진** | Rash | Sarpullido / Erupción | 発疹 (hosshin) | 발진 (baljin) | 皮疹 (pízhěn) |

---

## 핵심 대조 (종합)

| 대조 | 통찰 |
|----------|---------|
| **의사 어원** | EN "doctor" (Latin), ES "médico" (Latin) — JP 医者 / KR 의사 / CN 医生는 모두 한자 한자어 — 라틴 차용 없음 |
| **한자 공유** | JP/KR/CN은 의료 어휘 한자 공유 (医, 病院/医院, 内科/내과/内科) — 같은 한자 어원, 다른 발음 |
| **전문의 명명** | CJK는 복합어 (内科) 선호; EN/ES는 라틴/그리스 (cardiology / cardiología) |
| **전통 의학** | CN 中医 (zhōngyī) / KR 한의학 (hanuihak) / JP 漢方 (kanpō) — 통합 전통 의학 시스템; ES/EN은 동등한 통합 시스템 없음 |
| **신체부위 + 아프다 패턴** | 한국어 고유 패턴: 신체의 일부 + 아프다 (예: 배가 아파요 = stomach hurts); 다른 언어는 "[명사] 아픔" 구조 |

---

## 학습자 의사결정 가이드

> **의료 필수 어휘**:
> - Hospital: hospital / 病院(byōin) / 병원(byeongwon) / 医院(yīyuàn)
> - Doctor: doctor / 医者(isha) / 의사(uisa) / 医生(yīshēng)
> - Fever: fiebre / 熱(netsu) / 열(yeol) / 发烧(fāshāo)
> - Headache: dolor de cabeza / 頭痛(zutsū) / 두통(dutong) / 头痛(tóutòng)
> - Pharmacy: farmacia / 薬局(yakkyoku) / 약국(yakguk) / 药店(yàodiàn)

> **한자 공유 활용**: JP/KR/CN 의료 어휘는 한자 공유 — 의사 = 医者 = 醫(yī). 한자 학습 시 세 언어 동시 효율적 학습 가능.

---

## 🇰🇷 한국어 학습자 노트 (Korean Learner Notes)

> 본 섹션은 한국어 학습자 대상의 추가 학습 가이드입니다.

### 한국어 화자가 다른 4개 언어 의료 어휘를 학습할 때 흔히 마주치는 함정

1. **한자 한자어의 한국어 한자음 vs 일본 음/중국 음 혼동**:
   - 같은 한자 의료 어휘도 발음이 다름. 예: 病院: 한국 한자음 "병원" vs 일본 음 "びょういん (byōin)" vs 중국 음 "yīyuàn".
   - **함정**: 한국 한자음으로 일본어/중국어 의료 어휘 발음 추정 → 의사소통 실패. 예: 한국어 "내과 (naegwa)" vs 일본어 "ないか (naika)" vs 중국어 "nèikē" — 발음 다름.
   - **훈련법**: 의료 한자 50자 한자어 — 한국 한자음 + 일본 음(음독) + 중국 병음(pinyin) 별도 매트릭스 학습. 한자 = 3개국, 발음 = 3세트.

2. **"아프다" 패턴의 한국어 특수성**:
   - 한국어는 "[신체부위] + 가/이 + 아프다" 패턴 고유. 예: "배가 아파요" (stomach hurts), "머리가 아파요" (head hurts).
   - 다른 언어는 "[명사] + ache/hurt" 구조. 예: 영어 "I have a headache", 스페인어 "Me duele la cabeza", 일본어 "頭が痛い (atama ga itai)", 중국어 "头疼 (tóuténg)".
   - **함정**: 한국어 패턴 그대로 다른 언어에 적용 → "머리가 아파요" → "Head is hurt" 식 어색한 직역.
   - **훈련법**: 한국어의 "배 + 가 + 아파요" vs 영어 "have a stomachache" — **구조 차이** 인지를 먼저 학습.

3. **존경 동사 (honorific verb) 필수성**:
   - 한국어는 의료 관련 동사도 존경 사용. "어디가 아프세요?" (정중) vs "어디가 아파?" (캐주얼). 또한 "아프다/편찮으시다" (격식 어르신).
   - **함정**: 영어 "Are you sick?" 단일 형태로 한국어 4단계 경어 모두 시도 → 어색.
   - **훈련법**: 의료 상황 경어 — 환자 어르신에게 "어디가 편찮으세요?", 동년배 "어디 아파?", 아이 "어디 아파?". 4단계 모두 연습.

4. **한의학 vs 양의학 병행**:
   - 한국에서는 한의학(韓醫學)과 양의학(洋醫學) 모두 공식 의료 시스템. 한약, 침구, 부항, 척추 교정 모두 일반 의료 행위.
   - **함정**: 한의학 = "보완 의학"으로 간주 → "비과학적"으로 폄하. 또는 한의학 어휘 무지 → 한의원/한약 이름 부재.
   - **훈련법**: 한의학 기본 어휘 학습 — 한의원, 한약, 침, 부항, 척추, 경락, 기(氣), 한열(寒熱). 영어 "alternative medicine" 매핑 적절.

5. **의료 시스템 차이**:
   - 한국: 국민건강보험(NHI) 전 국민 강제, 본인부담 낮음. 약국 처방전 의존.
   - 일본: 건강보험 전 국민, 본인부담 30%. 약국 처방전.
   - 중국: 都市职工基本医疗保险, 본인부담 다양. 약국 처방전.
   - 미국: 보험 의무 아님, 본인부담 높음. 약국 처방전 (OTC vs 처방).
   - **함정**: 한국 시스템 기준으로 다른 국가 의료 시스템 추정 → 보험 적용/약값 혼란.
   - **훈련법**: 5개국 의료 시스템 비교 학습 — 보험, 본인부담, 처방전 vs OTC, 응급실 비용.

### 학습 전략

1. **우선순위 1**: 의료 한자 한자어 한자 동시 학습 — 의사/医師/醫(yī), 병원/病院/yīyuàn, 약/薬/yào, 열/熱/rè. 한자 30자 학습으로 3개국 의료 어휘 동시 습득.
2. **우선순위 2**: "아프다" 한국어 고유 패턴 + 다른 4개 언어의 "have a [symptom]" 구조 매트릭스 — 한국어 5개 증상 × 5개 언어.
3. **우선순위 3**: 의료 상황 경어 — "어디가 아프세요?" (정중) / "어디가 편찮으세요?" (격식 어르신) / "어디 아파?" (캐주얼). 환자/의사/약사/간호사 별 경어.
4. **우선순위 4**: 한의학 기본 어휘 — 한의원, 한약, 침, 부항, 기(氣), 경락. 한국 문화 이해에 필수.
5. **우선순위 5**: 의료 시스템 비교 — 5개국 보험/본인부담/약국 시스템. 해외 의료 접근 시 사전 지식 필수.

### 관련 한국어 위키 페이지

- [[health-body]] — 신체 부위 어휘
- [[numbers-counters]] — 약/주사/날짜 수량사
- [[travel-essentials]] — 해외 응급 의료
- [[shopping-money]] — 약국/약 구매
- [[korean-dating-culture]] — 한국 문화 (한의학 포함)

---

## 관련 페이지

- `[[health-body]]` — 신체 부위 및 기본 건강
- `[[shopping-money]]` — 약국 구매
- `[[travel-essentials]]` — 해외 응급 의료 상황

## 출처

- 5개 언어 의료 어휘 일반 의료 용어 참조
- 모든 5개 언어 wiki: 의료 테마 미인제스트 — 관련 어휘는 per-language wiki 참조

---

**원본 (영어)**: [[medical-comparison]] | **관련 미러**: [[medical-comparison.es|Spanish]] · [[medical-comparison.ja|Japanese]] · [[medical-comparison.zh|Chinese]] | **정책**: ADR-0006
