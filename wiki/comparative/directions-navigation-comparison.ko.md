# 방향 & 내비게이션 — Cross-Language Comparison (한국어판)

> 원본: [[directions-navigation-comparison]] (English) | 작성일: 2026-08-19 | ADR-0006
> **5개 언어 방향·내비게이션 비교** — English · Spanish · Japanese · Korean · Chinese

---

## 빠른 참조 표

### 사방위 (Cardinal Directions)

| Direction | English | Spanish | Japanese | Korean | Chinese |
|-----------|---------|---------|----------|--------|---------|
| **North** | North | Norte | 北 (kita) | 북 (buk) / 북쪽 | 北 (běi) |
| **South** | South | Sur | 南 (minami) | 남 (nam) / 남쪽 | 南 (nán) |
| **East** | East | Este | 東 (higashi) | 동 (dong) / 동쪽 | 东 (dōng) |
| **West** | West | Oeste | 西 (nishi) | 서 (seo) / 서쪽 | 西 (xī) |

### 복합 방향

| Direction | English | Spanish | Japanese | Korean | Chinese |
|-----------|---------|---------|----------|--------|---------|
| **Northeast** | Northeast | Noreste | 北東 (hokutō) | 북동 (bukdong) | 东北 (dōngběi) |
| **Northwest** | Northwest | Noroeste | 北西 (hokusai) | 북서 (bukseo) | 西北 (xīběi) |
| **Southeast** | Southeast | Sureste | 南東 (nantō) | 남동 (namdong) | 东南 (dōngnán) |
| **Southwest** | Southwest | Suroeste | 南西 (nansai) | 남서 (namseo) | 西南 (xīnán) |

### 기본 방향

| Direction | English | Spanish | Japanese | Korean | Chinese |
|-----------|---------|---------|----------|--------|---------|
| **Left** | Left | Izquierda | 左 (hidari) | 왼쪽 (oenjjok) | 左 (zuǒ) |
| **Right** | Right | Derecha | 右 (migi) | 오른쪽 (oreunjjok) | 右 (yòu) |
| **Forward** | Forward / Ahead | Adelante | 前 (mae) | 앞 (ap) | 前 (qián) |
| **Backward** | Backward / Behind | Atrás | 後ろ (ushiro) | 뒤 (dwi) | 后 (hòu) |
| **Up** | Up | Arriba | 上 (ue) | 위 (wi) | 上 (shàng) |
| **Down** | Down | Abajo | 下 (shita) | 아래 (arae) | 下 (xià) |

### 내비게이션 어휘

| Term | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **Straight** | Straight (ahead) | Recto / Derecho | まっすぐ (massugu) | 일직 (iljjik) / 똑바로 | 直 (zhí) |
| **Turn left** | Turn left | Gire a la izquierda | 左に曲がる (hidari ni magaru) | 왼쪽으로 돌다 | 左转 (zuǒ zhuǎn) |
| **Turn right** | Turn right | Gire a la derecha | 右に曲がる (migi ni magaru) | 오른쪽으로 돌다 | 右转 (yòu zhuǎn) |
| **Stop** | Stop | Para / Pare | 止まる (tomaru) | 멈추다 (meomchuda) | 停 (tíng) |
| **Go** | Go | Vaya / Vamos | 行け (ike) | 가다 (gada) | 走 (zǒu) / 去 (qù) |
| **Cross** | Cross | Cruzar | 渡る (wataru) | 건너다 (geonneom) | 过 (guò) |
| **Around** | Around | Alrededor | 周り (mawari) | 주변 (jubyun) | 周围 (zhōuwéi) |
| **Corner** | Corner | Esquina | 角 (kado) | 모퉁이 (motungi) | 拐角 (guǎijiǎo) |

### 위치 표현

| Phrase | English | Spanish | Japanese | Korean | Chinese |
|--------|---------|---------|----------|--------|---------|
| **X는 어디?** | Where is X? | ¿Dónde está X? | Xはどこですか？ | X는 어디에 있나요? | X在哪里? |
| **이 근처** | Near here | Cerca de aquí | この近く (kono chikaku) | 이 근처 (i geuncheo) | 这附近 (zhè fùjìn) |
| **여기서 멀리** | Far from here | Lejos de aquí | この遠く (kono tōku) | 여기서 멀리 | 这离得远 |
| **옆에** | Next to | Al lado de | 隣 (tonari) | 옆 (yeop) | 旁边 (pángbiān) |
| **앞에** | In front of | Delante de | 前 (mae) | 앞 (ap) | 前面 (qiánmiàn) |
| **뒤에** | Behind | Detrás de | 後ろ (ushiro) | 뒤 (dwi) | 后面 (hòumiàn) |
| **위에** | Above | Encima de | 上 (ue) | 위 (wi) | 上面 (shàngmiàn) |
| **아래에** | Below | Debajo de | 下 (shita) | 아래 (arae) | 下面 (xiàmiàn) |

### 문화적 내비게이션

| Concept | English | Spanish | Japanese | Korean | Chinese |
|---------|---------|---------|----------|--------|---------|
| **주소 형식** | Number → Street → City → State → Zip | Street, Number, Floor, City | Prefecture (都道府県), City, District, Block, Number | Province (도), City (시), District (구), Block (동), Number (번지) | Province (省), City, District, Street, Number |
| **Compass** | Standard compass | Brújula | コンパス | 나침반 | 指南针 |
| **GPS** | GPS | GPS | GPS / カーナビ | 내비게이션 | 导航 |
| **Maps** | Map | Mapa | 地図 | 지도 | 地图 |

### 이동 & 여행

| Action | English | Spanish | Japanese | Korean | Chinese |
|--------|---------|---------|----------|--------|---------|
| **Walk** | Walk | Caminar / Andar | 歩く (arukku) | 걷다 (geotta) | 走 (zǒu) |
| **Run** | Run | Correr | 走る (hashiru) | 뛰다 (ttwida) | 跑 (pǎo) |
| **Drive** | Drive | Conducir | 運転する (unten suru) | 운전하다 (unjeonhada) | 开车 (kāichē) |
| **Stop** | Stop | Parar | 止まる (tomaru) | 멈추다 (meomchuda) | 停 (tíng) |
| **Follow** | Follow | Seguir | ついてくる (tsuite kuru) | 따라가다 (ttaragada) | 跟着 (gēnzhe) |
| **Pass** | Pass | Pasar | 通り過ぎる (toorisugiru) | 지나가다 (jinaganda) | 经过 (jīngguò) |
| **Arrive** | Arrive | Llegar | 着く (tsuku) | 도착하다 (dochakada) | 到达 (dàodá) |
| **Depart** | Depart | Salir / Partir | 出発する (shuppatsu suru) | 출발하다 (chulbalhada) | 离开 (líkāi) |

---

## 언어별 상세

### 🇬🇧 영어 (English)
- **핵심 용어**: "Turn left" / "Turn right" / "Go straight"; "North" / "South"
- **패턴**: 전치사: "on" (on the left); "to the" (to the left)
- **출처**: `[[directions-vocabulary]]`

### 🇪🇸 스페인어 (Spanish)
- **핵심 용어**: "Norte/Sur/Este/Oeste" (흔히 대문자); "a la izquierda/derecha"
- **패턴**: 성 일치: "izquierdo" / "izquierda"; "Gire" (격식 명령) vs "gira" (캐주얼)
- **출처**: N/A — 스페인어 방향 테마 미정

### 🇯🇵 일본어 (Japanese)
- **핵심 용어**: 北東 (hokutō) / 北西 (hokusai) / 南東 (nantō) / 南西 (nansai); 交差点 (kōsaten = 교차로)
- **패턴**: 동사: 〜を曲がる (wo magaru); 조사: 〜に (방향); "左に" (hidari ni)
- **출처**: `[[directions-vocabulary]]`

### 🇰🇷 한국어 (Korean)
- **핵심 용어**: 방위 (bangwi = 방향); 동서남북 (dong-seo-nam-buk = 사방위)
- **패턴**: 동사: 〜을/를 돌다 (eul/reul dolida); 조사: 〜으로 (euro = 방향)
- **출처**: `[[directions-vocabulary]]`

### 🇨🇳 중국어 (Chinese)
- **핵심 용어**: 方向 (fāngxiàng), 东南西北 (dōng-nán-xī-běi); 十字路口 (shízì lùkǒu = 교차로)
- **패턴**: 동사: 〜转 (zhuǎn); 조사: 向 (xiàng = 향하여)
- **출처**: N/A — 중국어 방향 테마 미정

---

## 핵심 대조 (종합)

| 대조 | 학습자 시사점 |
|------|----------------|
| **방위 어휘** | JP 는 "kita/minami/higashi/nishi" — 단일 한자 + 다중 독음; CJK 는 단일 한자 |
| **주소 위계** | 동아시아 주소는 계층 (province→city→district→block→number); 서양 주소 평탄 |
| **좌/우** | EN/ES: 형용사; CJK: 명사 또는 또는 형 중; 동사 패턴 다름 |
| **조사 사용** | 한국어는 -(으)로; 일본어는 に; 중국어는 往/向 |

---

## 학습자 의사결정 가이드

- **마스터해야 할 첫 10 표현**:
  - EN: left, right, straight, north, south, east, west, turn, stop, go
  - ES: izquierda, derecha, recto, norte, sur, este, oeste, girar, parar, ir
  - JP: 左(hidari), 右(migi), まっすぐ(massugu), 北(kita), 南(minami), 東(higashi), 西(nishi), 曲がる(magaru), 止まる(tomaru), 行く(iku)
  - KR: 왼쪽, 오른쪽, 똑바로, 북, 남, 동, 서, 돌다, 멈추다, 가다
  - CH: 左(zuǒ), 右(yòu), 直(zhí), 北(běi), 南(nán), 东(dōng), 西(xī), 转(zhuǎn), 停(tíng), 走(zǒu)

---

## 🇰🇷 한국어 학습자 노트 (Korean Learner Notes)

> 본 섹션은 한국어 학습자 대상의 추가 학습 가이드입니다.

### 한국어 화자가 다른 4개 언어 방향 어휘를 배울 때 흔히 마주치는 함정

1. **일본어 단일 한자 다중 독음 (北 = kita/chinook/hoku)**:
   - 한국어 학습자는 "북" = "buk" 으로 단순 매핑 → 일본어 北 의 다중 독음 (kita 単独, hoku 結合) 에 혼란.
   - **함정**: 北東 = hokutou (kitau 아님), 北海道 = Hokkaido (Kita + 도가 아니라 hoku + kai + dou). 한국어 학습자가 kita + 東 어순 기대 → 잘못된 발음.
   - **훈련법**: 일본어 한자 독음 매트릭스 — 단독 (音読/훈독) vs 결합 (音読만). 京都 = "Kyouto" (경 + 도), 東京 = "Toukyou" (동 + 경, ん 발음), 大阪 = "Oosaka" (大 + 오사카). 결합 시 한국어 어순 무관.

2. **중국어 走 (zǒu) 의 "걷다" 의미**:
   - 한국어 학습자가 중국어 走 를 "달리다 (run)" 으로 가정 → 사실 走 = "걷다 (walk)" 의미. "달리다" = 跑 (pǎo).
   - **함정**: "我走 10 分钟" = "10분 걸어요" (달리기 아님). 한국어 학습자가 "10분 뛰어" 로 오역.
   - **훈련법**: 중국어 이동 동사 매핑 — 走 = walk (zǒu) / 跑 = run (pǎo) / 去 = go (qù) / 来 = come (lái) / 到 = arrive (dào). 한국어 학습자는 走 가 "walk" 임을 명시.

3. **스페인어 성 일치 (izquierdo/izquierda)**:
   - 한국어 학습자에게 "izquierdo" (남성형) vs "izquierda" (여성형) 의 성별 일치는 매우 낯설 — 한국어 "왼쪽" 은 성별 무관.
   - **함정**: "el lado izquierdo" (남성 명사) vs "la mano izquierda" (여성 명사) — 명사 성별에 따라 형용사 어미 변경.
   - **훈련법**: 스페인어 위치/방향 형용사의 성별 4형태 — izquierdo/izquierda/izquierdos/izquierdas + derecho/derecha/derechos/derechas. 좌/우 + 명사 성별 일치.

4. **한국어 "-으로" 방향 조사 vs 일본어 "에"**:
   - 한국어 "왼쪽으로 가세요" 의 -으로 조사 — 일본어 "左に行ってください" (hidari ni itte kudasai) 의 에 조사와 유사한 기능.
   - **함정**: 한국어 학습자가 일본어 에서 -을/를 → を (o) 로 단순 매핑 → 사실 은/는 vs は/가 의 미묘한 차이 있음.
   - **훈련법**: 방향 조사 비교 — KR -(으)로 / JP 에 / CH 向·往 / EN to/toward / ES a/hacia. 5개 조사 매핑.

5. **한국 주소 체계 (도-시-구-동-번지)**:
   - 한국어 주소 = province(도) → city(시) → district(구) → block(동) → number(번지) — 동아시아 계층적 형식. 영어 주소 = number → street → city → state → zip (역순).
   - **함정**: 한국어 학습자가 영어 주소 형식 (1234 Main St)을 한국어 어순으로 → 매우 어색.
   - **훈련법**: 5개 언어 주소 형식 비교 — EN: 123 Main St, City / ES: Calle Mayor 123, Ciudad / JP: 東京都千代田区千代田1-1 / KR: 서울특별시 종로구 세종대로 1 / CH: 北京市东城区东长安街1号. 어순 차이 명시.

### 학습 전략

1. **우선순위 1**: 한국어 기본 방향 어휘 마스터 (왼쪽/오른쪽/위/아래/앞/뒤 + -으로/에서 조사 결합).
2. **우선순위 2**: 한자 사방위 (東/西/南/北) 의 JP/KR/CN 발음 매핑.
3. **우선순위 3**: 중국어 走 (걷다) vs 跑 (달리다) 의 한국어 의미 매핑.
4. **우선순위 4**: 스페인어 위치 형용사 성별 4형태 (izquierdo/izquierda + s 복수).
5. **우선순위 5**: 5개 언어 주소 형식 비교 + 어순 차이 학습.

---

## 관련 페이지

- `[[transportation]]` — 이동
- `[[travel-essentials]]` — 여행 어휘
- `[[time-calendar]]` — 시간 + 방향 개념

## 출처

- `wiki/English/vocabulary/directions-vocabulary.md`
- `wiki/Japanese/vocabulary/directions-vocabulary.md`
- `wiki/Korean/vocabulary/directions-vocabulary.md`
- 문화 횡단 길찾기 연구

---

**원본 (영어)**: [[directions-navigation-comparison]] | **관련 미러**: [[directions-navigation-comparison.es|Spanish]] · [[directions-navigation-comparison.ja|Japanese]] · [[directions-navigation-comparison.zh|Chinese]] | **정책**: ADR-0006