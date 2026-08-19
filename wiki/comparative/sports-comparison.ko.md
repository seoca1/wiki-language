# 스포츠 & 레크리에이션 — 다국어 비교 (한국어판)

> 원본: [[sports-comparison]] (English) | 작성일: 2026-08-20 | ADR-0006
> **5개 언어 스포츠 어휘 비교**

---

## 빠른 참조 표

### 지역별 인기 스포츠

| 스포츠 | English | Spanish | Japanese | Korean | Chinese |
|-------|---------|---------|----------|--------|---------|
| **축구** | Soccer (US) / Football | Fútbol | サッカー (sakkā) | 축구 (chukgu) | 足球 (zúqiú) |
| **야구** | Baseball | Béisbol | 野球 (yakyū) | 야구 (yagu) | 棒球 (bàngqiú) |
| **농구** | Basketball | Baloncesto | バスケットボール | 농구 (nonggu) | 篮球 (lánqiú) |
| **테니스** | Tennis | Tenis | テニス (tenisu) | 테니스 (teniseu) | 网球 (wǎngqiú) |
| **골프** | Golf | Golf | ゴルフ (gorufu) | 골프 (golpeu) | 高尔夫球 (gāo'ěrfūqiú) |
| **수영** | Swimming | Natación | 水泳 (suiei) | 수영 (suyeong) | 游泳 (yóuyǒng) |
| **달리기** | Running / Jogging | Correr / Trotar | ランニング (ranningu) | 달리기 (dalligi) | 跑步 (pǎobù) |

### 무술 & 전통 스포츠

| 스포츠 | English | Spanish | Japanese | Korean | Chinese |
|-------|---------|---------|----------|--------|---------|
| **유도** | Judo | Yudo | 柔道 (jūdō) | 유도 (yudo) | 柔道 (róudào) |
| **가라테** | Karate | Kárate | 空手 (karate) | 가라테 (karate) | 空手道 (kōngshǒudào) |
| **태권도** | Taekwondo | Taekwondo | テコンドー (tekondō) | 태권도 (taegwondo) | 跆拳道 (táiquándào) |
| **검도** | Kendo | Kendo | 剣道 (kendō) | 검도 (geomdo) | 剑道 (jiàndào) |
| **스모** | Sumo | Sumo | 相撲 (sumō) | 스모 (seumo) | 相扑 (xiāngpū) |
| **카포에이라** | Capoeira | Capoeira | カポエイラ (kapoera) | 카포에이라 (kapoeira) | 卡波耶拉 (kǎbōyēlā) |
| **배드민턴** | Badminton | Bádminton | バドミントン (badominton) | 배드민턴 (baedeuminteon) | 羽毛球 (yǔmáoqiú) |
| **탁구** | Table Tennis / Ping-Pong | Tenis de mesa / Ping-Pong | 卓球 (takkyū) | 탁구 (takgu) | 乒乓球 (pīngpāngqiú) |

### 문화 스포츠 패턴

| 측면 | English | Spanish | Japanese | Korean | Chinese |
|--------|---------|---------|----------|--------|---------|
| **가장 인기 스포츠** | Football/Basketball/Baseball | Fútbol (Fútbol) | 野球 / サッカー | 야구 / 축구 | 篮球 / 乒乓球 |
| **스포츠 문화** | 관중 + 참여 | 열정 팬 문화 | 部活動 (클럽 활동) 학교 스포츠 | 프로 스포츠 (pro sports) | 학교 체육 + 올림픽 중시 |
| **유명 선수** | LeBron James, Tom Brady | Messi, Rafael Nadal | 大谷翔平, 羽生結弦 | 손흥민, 박지성 | 姚明, 刘翔 |
| **스포츠 이벤트** | Super Bowl | El Clásico | 甲子園 (Kōshien) | 프로야구 (Pro Baseball) | NBA China / CBA |

### 스포츠 어휘 — 핵심

| 카테고리 | English | Spanish | Japanese | Korean | Chinese |
|----------|---------|---------|----------|--------|---------|
| **팀** | Team | Equipo | チーム (chīmu) | 팀 (tim) | 队 (duì) |
| **경기** | Game / Match | Partido | 試合 (shiai) | 경기 (gyeonggi) | 比赛 (bǐsài) |
| **승/패** | Win/Lose | Ganar/Perder | 勝つ (katsu) / 負ける (makeru) | 이기다 (igida) / 지다 (jida) | 赢 (yíng) / 输 (shū) |
| **점수** | Score | Puntuación | スコア (sukoa) | 점수 (jeomsu) | 分数 (fēnshù) |
| **선수** | Player | Jugador | 選手 (senshu) | 선수 (seonsu) | 选手 (xuǎnshǒu) |
| **감독** | Coach | Entrenador | 監督 (kantoku) | 감독 (gamdok) | 教练 (jiàoliàn) |
| **경기장** | Stadium | Estadio | スタジアム (sutajiamu) | 경기장 (gyeonggijang) | 体育场 (tǐyùchǎng) |
| **토너먼트** | Tournament | Torneo | トーナメント / 大会 (taikai) | 토너먼트 / 대회 (hoe) | 锦标赛 (jǐnbiāosài) |

---

## 핵심 대조 (종합)

| 대조 | 통찰 |
|----------|---------|
| **차용 패턴** | 모든 언어 영어 스포츠 차용 (baseball, basketball, golf) — JP/KR는 원어 발음 추가, ZH는 棒球/篮球/golf 음역 |
| **동사 표현** | EN은 경동사 사용 ("play", "do"); ES는 -ar 활용; JP/KR/ZH는 명사+보조동사 (をやる/을 하다/打) |
| **문화적 무게** | 스포츠 강한 문화 정체성 — 라틴아메리카 축구, JP/KR 야구, CN 농구 — 다른 스포츠 = 다른 문화 앵커 |
| **학교 통합** | JP/KR 학교에 의무 部活/체육; EN/CN은 정규 교육 덜 통합 |

---

## 학습자 의사결정 가이드

> **학습 팁**: 국제 스포츠 이벤트 (올림픽, 월드컵) 시청 시 영어 차용어 청취 — 모든 5개 언어 보편 진입점.

> **5개 언어 스포츠 매트릭스 (7개 인기 스포츠)**:
> - 축구: Soccer (US)/Football / Fútbol / サッカー / 축구 / 足球
> - 야구: Baseball / Béisbol / 野球 / 야구 / 棒球
> - 농구: Basketball / Baloncesto / バスケットボール / 농구 / 篮球
> - 테니스: Tennis / Tenis / テニス / 테니스 / 网球
> - 골프: Golf / Golf / ゴルフ / 골프 / 高尔夫球
> - 수영: Swimming / Natación / 水泳 / 수영 / 游泳
> - 달리기: Running / Correr / ランニング / 달리기 / 跑步

---

## 🇰🇷 한국어 학습자 노트 (Korean Learner Notes)

> 본 섹션은 한국어 학습자 대상의 추가 학습 가이드입니다.

### 한국어 화자가 다른 4개 언어 스포츠 어휘를 학습할 때 흔히 마주치는 함정

1. **스포츠 한자 한자어 발음 차이**:
   - 같은 한자 스포츠 어휘가 한국어/일본어/중국어에서 발음 다름. 예: 野球: 한국 한자음 "야구" vs 일본 "やきゅう (yakyū)" vs 중국 "bàngqiú". 한자 一 글자당 3개국 발음.
   - **함정**: 한국어 한자음 "야구" / "축구" 를 일본어/중국어 발음 추정 → "yakyū" / "zúqiú" 와 다름.
   - **훈련법**: 스포츠 한자 한자어 3개국 발음 매트릭스 — 野球/야구/bàngqiú, 足球/축구/zúqiú, 篮球/농구/lánqiú. 한자 1글자 = 3개국 발음.

2. **스포츠 어휘의 영어 차용 패턴**:
   - 한국어: 야구, 축구 (한자어) + 테니스, 골프, 농구 (영어 차용) 혼재.
   - 일본어: 野球, サッカー (한자어) + テニス, ゴルフ, バスケットボール (영어 차용) 혼재.
   - 중국어: 棒球, 足球 (한자어) + 网球, 高尔夫球 (영어 음역) + 篮球 (의역).
   - 영어/스페인어: 대부분 자국어 + 일부 차용.
   - **함정**: 한국어 학습자가 일본어/중국어 스포츠 어휘에 한국어 한자음 적용 → 실패. 또한 영어 차용 발음도 다름 (한국어 테니스 vs 일본어 テニス vs 중국어 网球).
   - **훈련법**: 스포츠 어휘 한자 한자어 vs 영어 차용 분리 매트릭스. 한자 1글자 = 3개국 발음, 영어 차용 = 발음 다름.

3. **한국 스포츠의 학교 통합 (체육 교육)**:
   - 한국어: 학교에 체육(cheyuk) 수업 + 축구/야구/농구 동아리. 체육 시간 = 必修.
   - 일본어: 部活 (bukatsu) 클럽 활동 = 학교 정규 활동. 의무.
   - 영어: 학교 체육 = 선택/2차.
   - 중국어: 학교 체육 = 必修이지만 스포츠 동아리 문화 약함.
   - 스페인어: 학교 체육 = 필수, 축구 우세.
   - **함정**: 한국어 학습자가 영어 학교 스포츠에 "체육 시간" 단순 매핑 → "PE class" 와 한국 "체육 시간" 시간/의무 다름.
   - **훈련법**: 학교 스포츠 매트릭스 — KR/CH 필수, JP 部活 (클럽), EN 선택. **학교 체육 비교**.

4. **동사 패턴 4개 메커니즘 비교**:
   - 한국어: "~을 하다" (을 + 하다). 예: 야구를 해요, 축구를 해요.
   - 일본어: "~をやる" (を + やる) / "~をする" (를 + する).
   - 중국어: 打 (dǎ) + 명사. 예: 打球 (play ball).
   - 영어: "play" + 명사 (light verb). 예: "play basketball".
   - 스페인어: "jugar a" + 명사. 예: "jugar al fútbol".
   - **함정**: 한국어 학습자가 영어 "play basketball"을 한국어 "농구를 해요" 단순 매핑 → OK. 그러나 일본어 "バスケットボールをする" / 중국어 "打篮球" 패턴 다름.
   - **훈련법**: 스포츠 동사 4개 메커니즘 매트릭스 — 한국어 ~을 하다 / 일본어 ~をする/~をやる / 중국어 打 (dǎ) + 명사 / 영어 play + 명사 / 스페인어 jugar a. **5개 언어 동사 패턴 비교**.

5. **스포츠 클럽/팀/리그 명칭 한자 공유**:
   - 한국어: KBO (Korean Baseball Organization), K-League, KBL.
   - 일본어: NPB (日本野球機構), J-League, B.League.
   - 중국어: CBA (Chinese Basketball Association), CSL.
   - 영어/스페인어: MLB, NBA, La Liga, Premier League.
   - **함정**: KBO, NPB, MLB 모두 야구 리그지만 약자 다름 + 한자 어원 다름. 한국어 학습자가 일본 NPB/중국 CBA 단순 매핑 오류.
   - **훈련법**: 각국 주요 스포츠 리그/팀 약자 매트릭스 — KBO/NPB/MLB, K-League/J-League/La Liga 등. **리그 약자 학습**.

### 학습 전략

1. **우선순위 1**: 5개 언어 스포츠 어휘 7개 × 5언어 매트릭스 — 축구/야구/농구/테니스/골프/수영/달리기. **가장 인기 있는 7개 스포츠 동시 학습**.
2. **우선순위 2**: 스포츠 한자 한자어 3개국 발음 매트릭스 — 野球/야구/bàngqiú, 足球/축구/zúqiú, 篮球/농구/lánqiú, 选手/선수/xuǎnshǒu. **한자 1글자 = 3개국 발음**.
3. **우선순위 3**: 스포츠 동사 4개 메커니즘 — 한국어 ~을 하다 / 일본어 ~をする/~をやる / 중국어 打 / 영어 play / 스페인어 jugar a. **5개 언어 동사 패턴 비교**.
4. **우선순위 4**: 학교 스포츠 매트릭스 — KR/CH 필수, JP 部活 (클럽), EN 선택. **학교 체육 비교**.
5. **우선순위 5**: 각국 리그 약자 매트릭스 — KBO/NPB/MLB, K-League/J-League/La Liga. **리그 약자 학습**.

### 관련 한국어 위키 페이지

- [[adventure-outdoor-comparison]] — 야외 활동
- [[clothing-fashion-comparison]] — 운동복 어휘
- [[body-vocabulary]] — 신체 부위 어휘 (스포츠)
- [[numbers-counters]] — 점수/숫자 (스포츠)
-  — K-Sports (e-sports)

---

## 관련 페이지

- `[[adventure-outdoor-comparison]]` — 야외 활동
- `[[clothing-fashion-comparison]]` — 운동복 어휘
- `[[body-vocabulary]]` — 스포츠 신체 부위
- `[[numbers-counters]]` — 스포츠 점수

## 출처

- Per-language theme files: `wiki/{English,Spanish,Japanese,Korean}/vocabulary/sports-vocabulary.md`
- EN sports: `wiki/English/vocabulary/sports-vocabulary.md`
- ES sports: `wiki/Spanish/vocabulary/sports-vocabulary.md` (note: ES source page `sports-and-hobbies.md` exists; theme integration pending)
- JP sports: `wiki/Japanese/vocabulary/sports-vocabulary.md`
- KR sports: `wiki/Korean/vocabulary/sports-vocabulary.md`

---

**원본 (영어)**: [[sports-comparison]] | **관련 미러**: [[sports-comparison.es|Spanish]] · [[sports-comparison.ja|Japanese]] · [[sports-comparison.zh|Chinese]] | **정책**: ADR-0006
