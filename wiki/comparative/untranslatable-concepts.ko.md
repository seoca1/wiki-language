# 번역 불가 개념 — 다국어 비교 (한국어판)

> 원본: [[untranslatable-concepts]] (English) | 작성일: 2026-08-20 | ADR-0006
> **5개 언어의 문화 의존 어휘 — 직접 1:1 번역 불가**

---

## 빠른 참조 표

### 영어 고유 개념

| 단어 | 설명 | 문화 맥락 |
|------|-------|------------------|
| **Awkward** | 사회적 불편함, 어색함 | 사회적 유연성 중시; "awkward turtle" 밈 |
| **Serendipity** | 우연한 발견 | Horace Walpole 신조어 (1754); 혁신 문화에서 중시 |
| **Bureaucracy** | 과도한 행정 절차 | Weberian 유산; "red tape" 별도 개념 |
| **Privacy** | 혼자 있을 권리, 개인정보 통제 | 법적 권리 (수정헌법 4조); "사생활 기대" |
| **Accountability** | 행동/결과 책임 | 기업/정치 문화; "책임 묻기" |
| **Empowerment** | 타인에게 권한/자신감 부여 | 경영/자기계발 담론; "여성 임파워먼트" |
| **Multitasking** | 동시 다중 작업 | 중시 기술; 원래 컴퓨팅 용어 (1960s) |
| **Proactive** | 문제 사전 대응 | 비즈니스 전문어 (Covey 1989); 반응적의 반대 |
| **Burnout** | 만성 직장 스트레스 소진 | WHO ICD-11 (2019); "조용한 사직" 관련 |
| **Imposter syndrome** | 증거에도 불구하고 사기꾼 느낌 | 고성과자 문화; Clance & Imes (1978) |

### 스페인어 고유 개념

| 단어 | 설명 | 문화 맥락 |
|------|-------|------------------|
| **Sobremesa** | 식사 후 식탁에서 대화하며 머무는 시간 | 가족/사회 의식; 30분-2시간; "삶이 일어나는 곳" |
| **Duende** | 예술(플라멩코)에서의 고조된 감정/영감 | Lorca의 이론; "기술 너머의 신비한 힘" |
| **Estrenar** | 무언가를 처음 사용/착용 | 새 것의 의식; *estrenar coche, zapatos, traje* |
| **Merienda** | 가벼운 오후 식사/간식 (5-7pm) | 문화 기관; *bocadillo, fruta, yogur* |
| **Tertulia** | 비공식 문학/예술 모임 | 카페 문화; *tertulia literaria, política, musical* |
| **Desvelado** | 잠 못 자다, 늦게 깨어있다 | *Estar desvelado*; 불면증과 구별 |
| **Friolero/a** | 쉽게 추위를 타는 사람 | *Tener frío* vs *ser friolero*; 체질적 특성 |
| **Tocayo/a** | 같은 이름을 가진 사람 | *Mi tocayo Juan*; 즉각적 친족 유대 |
| **Vergüenza ajena** | (타인에 대한) 간접적 부끄러움 | "스페인 shame"; *me da vergüenza ajena* |
| **Convivencia** | 함께 조화롭게 살기, 공존 | 학교/가치; *educación para la convivencia* |
| **Madrugar** | 매우 일찍 일어나다 | *Madrugar para trabajar*; 노력 미덕 |
| **Trasnochar** | 밤새 깨어있다 | *Trasnochar estudiando*; *madrugar*의 반대 |
| **Ponerse las pilas** | 동기부여/진지해지기 (문자: 배터리 넣기) | 노력 활성화 관용구 |
| **Dar la lata** | 지속적으로 성가시게 하다 (문자: 캔 주기) | *No me des la lata* |
| **Estar en las nubes** | 멍때리기, 산만함 (문자: 구름에 있다) | *Anda en las nubes* |

### 일본어 고유 개념

| 단어 | Reading | 설명 | 문화 맥락 |
|------|---------|-------|------------------|
| **侘寂** | わびさび (wabi-sabi) | 불완전, 무상, 불완벽함의 아름다움 | 다도; *kintsugi* (금 수리); 선(禪) 미학 |
| **木漏れ日** | こもれび (komorebi) | 나무 사이로 비치는 햇빛 | 시적 자연 관찰; *mono no aware* |
| **物の哀れ** | もののあわれ (mono no aware) | 사물의 패노스, 무상함에 대한 민감성 | *Heike Monogatari*; 벚꽃 구경 |
| **金継ぎ** | きんつぎ (kintsugi) | 도자기 금박으로 수리 | 불완전함 = 역사; 회복 은유 |
| **おもてなし** | おもてなし (omotenashi) | 이기적이지 않은 환대, 니즈 예측 | 서비스 문화; 팁 기대 안 함; *ichigo ichie* |
| **一期一会** | いちごいちえ (ichigo ichie) | 일생일대의 만남 | 다도; 각 만남 소중히 |
| **森林浴** | しんりんよく (shinrin-yoku) | 삼림욕, 자연 요법 | 예방 의학; 피톤치드; 1980s 신조어 |
| **過労死** | かろうし (karōshi) | 과로로 인한 사망 | 사회 문제; 1970s 인정; 노동법 개혁 |
| **引きこもり** | ひきこもり (hikikomori) | 사회적 위축, 급성 고립 | 청년 현상; 1M+ 추정; 가족 부담 |
| **義理** | ぎり (giri) | 사회적 의무, 책임 (vs *ninjo* = 참된 감정) | 선물 (*giri-choco*); 직장 역학 |
| **人情** | にんじょう (ninjo) | 인간적 감정, 연민 (vs *giri*) | *Giri-ninjo* 갈등 (드라마) |
| **空気を読む** | くうきをよむ (kuuki o yomu) | 분위기 읽기, 명시 안 된 맥락 감지 | 고맥락 문화; KY (kuuki yomenai) = 사회성 부족 |
| **諦め** | あきらめ (akirame) | 체념, 수용, 놓아주기 | 불교 *akirameru*; 패배 아닌 명확성 |
| **頑張る** | がんばる (ganbaru) | 최선 다하기, 인내, 버티기 | 보편 격려; *ganbatte* |
| **しょうがない** | しょうがない (shou ga nai) | 어쩔 수 없다 | 스토아적 수용; *shikata nai* |

### 한국어 고유 개념

| 단어 | 한자 | 설명 | 문화 맥락 |
|------|--------|-------|------------------|
| **한** | 한 (han) | 깊은 슬픔, 원한, 미해결 비애 | 집단 트라우마 (식민지, 전쟁, 분단); *han-puri* (해소) |
| **정** | 정 (jeong) | 깊은 애정, 애착, 시간 경과 후 형성 | *Jeong-i deulda* (애착); *jeong-i meolda* (거리 두기); 사랑 아님 |
| **눈치** | 눈치 (nunchi) | 사회적 tact, 상황 읽기, 기분 측정 | *Nunchi boida* (tact 있음); *nunchi eopda* (무지); 생존 기술 |
| **효도** | 효도 (hyodo) | 부모 봉양 효도 | 유교 핵심; *hyodo-hada*; 보호자 정부 보조금 |
| **체면** | 체면 (chemyeon) | 사회적 체면, 존엄, 공적 평판 | *Chemyeon seuda* (체면 살리다); *chemyeon gujjida* (체면 잃다) |
| **우정** | 우정 (ujeong) | 깊은 우정, 편의 너머의 충성 | *Ujeong-i dupeotda* (우정 깊어짐); *chingu*와 구별 |
| **맛** | 맛 (mat) | 풍미, 맛, 상황의 "느낌/분위기" | *Mat-eopda* (맛 없다/심심); *mat-jip* (맛집) |
| **소확행** | 소확행 (so-hwak-haeng) | 작지만 확실한 행복 | 2010s 트렌드 (일본어 *shōkōfuku*); 커피, 산책, 책 |
| **케렌시아** | 케렌시아 (kerensia) | 개인 안식처, 재충전 안전 공간 | 스페인어 *querencia* 차용; *nae kerensia* (나의 은신처) |
| **인연** | 인연 (inyeon) | 카르마적 연결, 운명적 관계 | 불교 기원; *inyeon-iilda* (운명); *inyeon-i eopda* |
| **손님** | 손님 (sonnim) | 손님, 고객 — 최고 존중 | *Sonnim-eun wang-ida* (손님은 왕); 서비스 문화 |
| **미안하다** | 미안하다 (mianhada) | 미안 + 감사 + 빚진 (다기능) | *Mianhamnida* = 사과, 감사, 실례 |
| **고맙다** | 고맙다 (gomapda) | 감사 + 노력/친절 인식 | *Gomapseumnida* *gamsahamnida*보다 깊음 |
| **빨리빨리** | 빨리빨리 (ppali-ppali) | 빨리빨리, 속도 문화 | 경제 기적 동력; *ppali-ppali munhwa* |
| **정들다** | 정들다 (jeong-deulda) | 시간 경과 후 정서적 애착 형성 | *Jeong-deureo himdeulda* (떠나기 어려움) |

### 중국어 고유 개념

| 단어 | Pinyin | 설명 | 문화 맥락 |
|------|--------|-------|------------------|
| **关系** | guānxi | 연결, 네트워크, 호혜 의무 | 사회적 자본; *guanxi-xue* (연구); 비즈니스 필수 |
| **面子** | miànzi | 체면, 사회적 지위, 평판 | *Gei mianzi* (체면 주기); *diu mianzi* (체면 잃기); *liu mianzi* |
| **缘分** | yuánfèn | 예정된 친화, 카르마적 연결 | *You yuanfen* (인연 있음); *mei yuanfen* (인연 없음) |
| **孝顺** | xiàoshùn | 효도 + 정서적 돌봄 | *Xiao* (孝) 핵심 유교 미덕; *bai xiao* (백효) |
| **吃苦** | chīkǔ | 고난 인내, 고통 통한 인격 형성 | *Chiku nailao* (吃苦耐劳) = 미덕; 양육 가치 |
| **面子工程** | miànzi gōngchéng | 체면 프로젝트, 과시적 무용 프로젝트 | 정치/관료 비판 |
| **差不多** | chàbùduō | 거의 충분, 괜찮음, 대충 | 실용주의; *chabuduo* 태도 vs 정밀성 |
| **随缘** | suíyuán | 흐름에 따르기, 운명 수용 | 불교 *suí yuán*; 수동 아닌 비집착 |
| **人情** | rénqíng | 인간 정서, 호혜 선물/호의 의무 | *Renqing shehui* (호혜 사회); *huan renqing* (보답) |
| **面子上过得去** | miànzi shàng guòdeqù | 체면 유지, 간신히 수용 | 사회적 윤활 |
| **塞翁失马** | sàiwēng shīmǎ | 역설적 축복 (노인 말 잃음) | *Saiweng shima, yan zhi fei fu* — 고전 성어 |
| **缘木求鱼** | yuánmù qiúyú | 물고기 잡으려 나무에 오르기 — 잘못된 방법 | 헛된 노력; 잘못된 접근 |
| **守着金山讨饭吃** | shǒuzhe jīnshān tǎofàn chī | 금산 위에 앉아 밥 구걸 | 낭비된 잠재력; 미인식 가치 |
| **上有政策，下有对策** | shàng yǒu zhèngcè, xià yǒu duìcè | 위는 정책, 아래는 대응책 | 규제 회피 창의성 |
| **差距** | chājù | 격차, 불평등 (행동 가능 암시) | *Chaju* 소득, 기술, 교육 — 정책 대상 |

### 비교 표: 언어별 상위 3개 번역 불가

| 언어 | #1 | #2 | #3 |
|----------|-----|-----|-----|
| **English** | Serendipity | Awkward | Privacy |
| **Spanish** | Sobremesa | Duende | Estrenar |
| **Japanese** | Wabi-sabi / Mono no aware | Omotenashi | Giri / Ninjo |
| **Korean** | Han | Jeong | Nunchi |
| **Chinese** | Guanxi | Mianzi | Yuanfen |

### 거짓 친구 / 근접 매치

| 단어 | 언어 | 닮은 것 | 실제 의미 |
|------|----------|------------|----------------|
| **Embarazada** | Spanish | Embarrassed | **임신한** |
| **Pretender** | Spanish | Pretend | **의도하다/열망하다** |
| **Realizar** | Spanish | Realize | **달성하다/수행하다** |
| **Sensible** | Spanish | Sensible | **민감한** |
| **Argumento** | Spanish | Argument | **플롯/이유** |
| **KY** | Japanese | Kentucky / KY Jelly | **Kuuki Yomenai** (분위기 못 읽음) |
| **Yabai** | Japanese | Ya-bye | **위험한 / 미친 / 놀라운** (맥락 의존) |
| **Daijoubu** | Japanese | Daijobu (이름?) | **OK / 문제 없음 / 고마워요** |
| **Fighting** | Korean | Fighting (폭력) | **힘내라! / 화이팅!** (화이팅) |
| **Service** | Korean | Service (명사) | **서비스 (무료 제공)** (서비스) |
| **Oppa** | Korean | Older brother | **남자친구/친한 선배 남성** (맥락) |
| **Jiayou** | Chinese | Add oil | **힘내라! / 계속해!** (加油) |
| **Maidan** | Chinese | Maiden | **주문서** (买单 = 계산해 주세요) |
| **Xiaokang** | Chinese | Small Kang | **중산층 사회** (小康) |
| **Chabuduo** | Chinese | Cha bu duo | **거의 충분/대충** (差不多) |

### 학습 우선순위 매트릭스

| 학습자 목표 | 우선순위 개념 |
|--------------|---------------------------|
| **비즈니스** | Guanxi, Mianzi, Omotenashi, Giri, Nunchi, Jeong, Sobremesa |
| **사교/연애** | Jeong, Nunchi, Yuanfen, Duende, Kokuhaku/Gobaek, Jeong-deulda |
| **일상 생활** | Chabuduo, Ppali-ppali, Shi-ga-nai, Chiku, Shinrin-yoku |
| **문화적 유창성** | Han, Wabi-sabi, Mono no aware, Renqing, Chemyeon, Sobremesa |
| **직장** | Ppali-ppali, Karoshi, Ganbaru, Chiiku, Kuuki o yomu, Service |

### 학습자 의사결정 가이드

| 필요한 표현 | EN | ES | JP | KR | CH |
|---------|----|----|----|----|----|
| **"우연한 발견"** | Serendipity | Chiripa / Casualidad | 僥倖 (ぎょうこう) / 偶然の産物 | 우연한 발견 | 机缘巧合 (jīyuán qiǎohé) |
| **"사회적 어색함"** | Awkward | Incómodo / Vergonzoso | 気まずい (kimazui) / KY | 어색하다 / 민망하다 | 尴尬 (gāngà) |
| **"식후 대화"** | — | **Sobremesa** | 食後の歓談 (しょくごのかんだん) | 식후 대화 | 饭后闲聊 (fànhòu xiánliáo) |
| **"깊은 슬픔/비애"** | Grief | Pena / Duelo | 哀しみ (kanashimi) / 無常 | **한 (Han)** / 깊은 슬픔 | 悲愁 (bēichóu) / 憾恨 (hànhèn) |
| **"분위기 읽기"** | Read the room | Leer el ambiente | **空気を読む (kuuki o yomu)** | **눈치 (nunchi)** | 察言观色 (cháyán guānsè) |
| **"체면/평판"** | Reputation | Reputación / Imagen | **面目 (めんぼく) / 体面 (ていめん)** | **체면 (chemyeon)** | **面子 (miànzi)** |
| **"연결/네트워크"** | Networking | Contactos / Enchufe | コネ (kone) / 人脈 | 인맥 / 줄 | **关系 (guānxi)** |
| **"효도"** | Respect parents | Respeto a padres | 親孝行 (おやこうこう) | **효도 (hyodo)** | **孝顺 (xiàoshùn)** |
| **"어쩔 수 없다"** | It is what it is | Qué le vamos a hacer | **しょうがない (shou ga nai)** | 어쩔 수 없다 | 没办法 (méi bànfǎ) / 无奈 |
| **"작은 확실한 행복"** | Simple pleasures | Pequeñas alegrías | 小さな幸せ (chiisana shiawase) | **소확행 (so-hwak-haeng)** | 小确幸 (xiǎoquèxìng) |

---

## 🇰🇷 한국어 학습자 노트 (Korean Learner Notes)

> 본 섹션은 한국어 학습자 대상의 추가 학습 가이드입니다.

### 한국어 화자가 다른 4개 언어 번역 불가 개념을 학습할 때 흔히 마주치는 함정

1. **"한 (Han)" 의 한국어 고유성 — 번역 불가능한 슬픔**:
   - 한국어 "한" = 집단 트라우마 (식민지, 전쟁, 분단)에서 온 **깊은 슬픔/원한/미해결 비애**. *Han-puri* (해소 의식).
   - 영어 "grief" / 스페인어 "pena" / 일본어 "哀しみ" / 중국어 "悲愁" — 모두 "개인 슬픔" 또는 "일반 슬픔". **집단 트라우마 깊이** 부재.
   - **함정**: 한국어 학습자가 영어 "grief" 단순 매핑 → "한" 의 집단 트라우마 차원 손실.
   - **훈련법**: **"한" = 한국 고유**, 다른 4개 언어 동등 없음. *Han-puri* 의식, 한옥, 한국전쟁, 분단 맥락 학습 필수.

2. **"정 (Jeong)" 의 한국어 시간-의존성**:
   - 한국어 "정" = 시간 경과 후 형성되는 **깊은 애정/애착**. *Jeong-deulda* (정들다) = 시간이 지나면서 정 형성.
   - 영어 "love" / 스페인어 "amor" / 일본어 "愛" / 중국어 "爱" — **즉각적/강렬한 사랑** 의미. 시간 의존성 부재.
   - **함정**: 한국어 학습자가 영어 "love" 단순 매핑 → "정" 의 시간-의존성 손실. "I love you" ≠ "정든다".
   - **훈련법**: **"정" = 한국 고유**, 시간 의존성 명시. *정들다*, *정이 생기다*, *정이 들다* 동사 어형 학습.

3. **"눈치 (Nunchi)" vs 일본어 "空気を読む" vs 영어 "Reading the room"**:
   - 한국어 "눈치" + 일본어 "空気を読む (kuuki o yomu)" — 동등한 사회적 tact. 그러나 **한국어 "눈치" = 한국 문화 더 강조**.
   - 영어 "Reading the room" — 상대적으로 약함.
   - **함정**: 한국어 학습자가 영어 "read the room" 단순 매핑 → "눈치" 의 한국 사회 강조도 손실.
   - **훈련법**: **"눈치" vs "空気を読む"** 동등 비교, 영어 "read the room" 약함 인지. **동아시아 3개국 (KR/JP/CN) 의 사회적 tact** 매트릭스.

4. **"체면 (Chemyeon)" vs 중국어 "面子 (miànzi)"**:
   - 한국어 "체면" + 중국어 "面子" — 유사한 체면 개념. 그러나 한국은 유교 + 집단 문화, 중국은 关系(관계) 맥락.
   - 영어 "face" / 스페인어 "reputación" / 일본어 "面目 (めんぼく)" / "体面 (ていめん)" — 유사.
   - **함정**: 한국어 학습자가 "체면" 을 다른 4개 언어 "face/reputation" 단순 매핑 → 한국 "체면" 의 사회적/직업적 뉘앙스 손실.
   - **훈련법**: **"체면" = 한국어 + "面子" = 중국어** 유사 비교, 일본어 面目/体면 별도 학습. **체면 4개 언어 매트릭스**.

5. **"빠리빠리 (Ppali-ppali)" vs 다른 4개 문화의 속도 개념**:
   - 한국어 "빨리빨리" = 한국 **속도 문화**의 상징 (경제 기적 동력).
   - 영어 "hurry" / 스페인어 "rápido" / 일본어 "急いで (isoide)" / 중국어 "快 (kuài)" — 모두 "빨리" 의미이나 문화적 강조도 다름.
   - **함정**: 한국어 학습자가 다른 4개 언어에 "빨리빨리" 단순 매핑 → 문화적 상징 손실.
   - **훈련법**: **"빨리빨리" = 한국 문화 상징**, 다른 4개 언어 단순 "빨리" 와 구별. **속도 문화 매트릭스**.

6. **"소확행 (so-hwak-haeng)" 의 한국-일본 동일성**:
   - 한국어 "소확행" = 일본어 "小確幸 (shōkakukō)" — **2010s 동시 동향** (한국이 일본에서 차용).
   - 영어 "small certain happiness" / 스페인어 "pequeñas alegrías" / 중국어 "小确幸 (xiǎo què xìng)" — 동등.
   - **함정**: 한국어 학습자가 영어 "small certain happiness" 단순 매핑 → "소확행" 의 2010s 트렌드 차용 맥락 손실.
   - **훈련법**: **"소확행" = 한국-일본 동시 트렌드**, 차용어 (일본어) 인지. **5개 언어 매트릭스**.

### 학습 전략

1. **우선순위 1**: 한국어 고유 개념 5개 (한/정/눈치/체면/효도) **명시 학습** — 다른 4개 언어 동등 부재. **집단 트라우마 + 시간 의존성 + 사회 tact + 체면 + 효도** 학습.
2. **우선순위 2**: 한자 한자어 문화 의존 3개국 비교 — 체면/面目/面子, 정/情/情, 효도/孝/孝. **한자 1글자 = 3개국 의미 변형**.
3. **우선순위 3**: 동아시아 3개국 문화 의존 개념 매트릭스 — 한(韓) / 눈치 / 체면 vs 일본 와비사비 / 空気を読む / 面目 vs 중국 关系 / 面子 / 缘分. **동아시아 한자 문화 비교**.
4. **우선순위 4**: 거짓 친구 (false friends) 5개 언어 매트릭스 — Embarazada (스페인 = 임신, 영어 = embarrassed) / Pretender / Realizar / KY / Yabai / Fighting / Service / Oppa / Jiayou. **명시적 학습**.
5. **우선순위 5**: 2010s 동시 트렌드 — 소확행 (KR/JP 동시), 내로남불 (KR), 화이팅 (KR 글로벌), 별별 한자어 차용. **문화적 맥락 의존**.

### 관련 한국어 위키 페이지

- [[cultural-values]] — 가치관 배경
- [[politeness-honorifics]] — 체면, 위계, 의무
- [[dating-romance]] — 정, 인연, 연애
- [[business-email]] — 관계, 눈치, 이메일
- [[gestures-body-language]] — 비언어 표현

---

## 관련 페이지

- `[[cultural-values.md]]` — 가치관 배경
- `[[politeness-honorifics]]` — 체면, 위계, 의무
- `[[dating-romance]]` — 정, 인연, 연애
- `[[business-email]]` — 관계, 눈치, 이메일
- `[[gestures-body-language.md]]` — 비언어 표현

## 출처

- English: `[English/culture/english-dating-culture]`, `[English/vocabulary/emotions-personality-vocabulary]`
- Spanish: `[Spanish/culture/espana-vs-latinoamerica-registro]`, `[Spanish/vocabulary/emotions-personality-vocabulary]`
- Japanese: `[Japanese/culture/japanese-dating-culture]`, `[Japanese/vocabulary/emotions-personality-vocabulary]`
- Korean: `[Korean/culture/korean-dating-culture]`, `[Korean/vocabulary/emotions-personality-vocabulary]`
- Chinese: `[Chinese/sources/greetings-zh]`, `[Chinese/vocabulary/family-zh]`

---

**원본 (영어)**: [[untranslatable-concepts]] | **관련 미러**: [[untranslatable-concepts.es|Spanish]] · [[untranslatable-concepts.ja|Japanese]] · [[untranslatable-concepts.zh|Chinese]] | **정책**: ADR-0006
