# 교통 — 다국어 비교 (한국어판)

> 원본: [[transportation]] (English) | 작성일: 2026-08-20 | ADR-0006
> **5개 언어 교통 어휘 비교 — 메트로, 기차, 택시, 라이드셰어, 운전**

---

## 빠른 참조 표

### 주요 교통수단

| 교통수단 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **도보** | walking / on foot | a pie / caminando | 歩き (aruki) / 徒歩 (ho-to) | 걷기 (geotgi) / 도보 (dobo) | 走路 (zǒulù) |
| **자전거** | bicycle / bike | bicicleta | 自転車 (jitensha) | 자전거 (jajeongeo) | 自行车 (zìxíngchē) |
| **오토바이** | motorcycle | motocicleta | バイク (baiku) / オートバイ | 오토바이 (otobai) / 모터바이 | 摩托车 (mótuōchē) |
| **자동차** | car | coche / carro / auto | 車 (kuruma) / 自動車 (jidōsha) | 자동차 (jadongcha) | 汽车 (qìchē) / 车 (chē) |
| **버스** | bus | autobús / bus | バス (basu) | 버스 (beoseu) | 公交车 (gōngjiāochē) / 巴士 (bāshì) |
| **트램** | tram / streetcar | tranvía | 路面電車 (romen densha) | 노면전차 (nomyeonjeoncha) / 트램 (teuraem) | 有轨电车 (yǒuguǐ diànchē) / 电车 (diànchē) |
| **지하철** | subway / metro | metro | 地下鉄 (chikatetsu) | 지하철 (jihacheol) | 地铁 (dìtiě) |
| **도시 철도** | commuter rail / local train | cercanías (Spain) | 各停 (kakutei) / 私鉄 (shitetsu) | 전철 (jeoncheol) / 도시철도 | 城市铁路 (chéngshì tiělù) |
| **고속철도** | high-speed rail | tren de alta velocidad (AVE) | 新幹線 (shinkansen) | KTX (Korea Train eXpress) | 高铁 (gāotiě) / CRH (China Railway High-speed) |
| **택시** | taxi / cab | taxi | タクシー (takushii) | 택시 (taeksi) | 出租车 (chūzūchē) / 的士 (díshì) |
| **라읻셰어** | rideshare / Uber | VTC / Uber | ライドシェア (raido shia) / Uber | 카카오택시 / 우버 | 滴滴出行 / 高德打车 |

### 국가별 교통 시스템

### 미국
| 교통수단 | 설명 |
|------|-------------|
| **자동차** | 주요 교통수단 (~85% 여행) |
| **비행기** | 장거리, 광범위 네트워크 |
| **버스** | Greyhound (장거리), 도시 버스 |
| **지하철** | NYC, Chicago, DC, Boston, SF, LA (제한) |
| **기차** | Amtrak (제한 여객 철도) |
| **라읻셰어** | Uber, Lyft (도시 우세) |
| **자전거** | 도시 증가 (Citi Bike, Lyft bikeshare) |

### 스페인
| 교통수단 | 설명 |
|------|-------------|
| **고속철도 (AVE)** | 우수 네트워크 (Madrid, Barcelona, Sevilla) |
| **메트로** | Madrid, Barcelona, Bilbao, Valencia |
| **Cercanías** | 교외 철도 (통근) |
| **버스** | ALSA (장거리), 도시 버스 |
| **자동차** | 일반, 역사 도심 제한 |
| **택시** | 백색 + 녹색 줄 (Madrid), 검정/노랑 (Barcelona) |
| **라읻셰어** | Uber, Cabify, FreeNow |

### 일본
| 교통수단 | 설명 |
|------|-------------|
| **기차 (Japan Railways)** | JR (6 지역 회사), 조밀 네트워크 |
| **지하철 (chikatetsu)** | Tokyo Metro, Toei, Osaka, Nagoya, 등 |
| **신칸센** | 고속 (총알 열차) — 글로벌 골드 스탠다드 |
| **버스** | 고속도로 버스 (기차보다 저렴), 도시 버스 |
| **택시** | 비싸지만 신뢰성 (문 자동 개방) |
| **자동차** | 도시에서는 덜 일반 (비싼 주차, 좁은 거리) |
| **자전거** | 일반 (사이클링 문화), 특히 Kyoto |
| **비행기** | 주요 도시 간 국내선 |
| **페리** | 섬 (Okinawa, Hokkaido) |

### 한국
| 교통수단 | 설명 |
|------|-------------|
| **지하철** | 서울 (9개 노선), 부산, 대구, 인천, 광주, 대전 |
| **KTX** | 고속 철도 (서울-부산 2시간) |
| **SRT** | 사설 고속 (최신, KTX와 유사) |
| **버스** | 시외 (고속버스), 도시 버스 |
| **택시** | 색깔 코드: 일반 (regular) / 모범 (premium) / 대형 (large) |
| **T-money / Cashbee** | 교통 카드 (모든 수단 호환) |
| **자동차** | 일반, 서울 교통 혼잡 |
| **Kakao T** | KakaoTaxi 앱 (우세 라읻셰어) |

### 중국
| 교통수단 | 설명 |
|------|-------------|
| **고속철도 (CRH)** | 세계 최대 네트워크 (40,000+ km) |
| **지하철** | 베이징, 상하이, 광저우, 선전, 40+ 도시 |
| **버스** | 광범위 네트워크, 매우 저렴 |
| **택시** | 도시 일반 |
| **Didi (滴滴)** | 라읻셰어 앱 (중국 우버) |
| **자동차** | 증가 중산층 |
| **Alipay/WeChat Pay** | 모든 교통 결제 사용 |
| **고속 자기부상** | 상하이 (푸동 공항, 세계 최고 속) |

### 교통 카드 시스템

| 국가 | 카드 | 호환성 |
|---------|------|-------------|
| **US** | Oyster (NYC), Clipper (SF) | 도시별 제한 |
| **Spain** | Tarjeta Transporte Público (지역) | 지역별 제한 |
| **Japan** | Suica, Pasmo, Icoca, Kitaca, 등 | **보편** (2013부터 10대 주요 IC 카드 호환) |
| **Korea** | T-money, Cashbee, Kmoney, MyB, OnePay, Rail+, KayoCard | **보편** 교통 + 편의점 |
| **China** | Alipay, WeChat Pay (QR 코드) | 보편 (모바일 페이, 카드 불필요) |

### 어휘 — 모드별

#### 지하철역

| English | Spanish | Japanese | Korean | Chinese |
|---------|---------|----------|--------|---------|
| **역** | estación | 駅 (eki) | 역 (yeok) | 站 (zhàn) |
| **플랫폼** | andén / vía | ホーム (hōmu) / 番線 (bansen) | 승강장 (seunggangjang) / 승강장 / 번 (beon) | 站台 (zhàntái) / 月台 (yuètái) |
| **노선** | línea | 線 (sen) | 노선 (noseon) | 线路 (xiànlù) |
| **출구** | salida | 出口 (deguchi) | 출구 (chulgu) | 出口 (chūkǒu) |
| **입구** | entrada | 入口 (iriguchi) | 입구 (ipgu) | 入口 (rùkǒu) |
| **환승** | transbordo / combinación | 乗換 (norikae) | 환승 (hwansung) | 换乘 (huànchéng) |
| **편도** | billete sencillo / de ida | 片道 (katamichi) | 편도 (pyeondo) | 单程票 (dānchéngpiào) |
| **왕복** | billete de ida y vuelta | 往復 (ōfuku) | 왕복 (wangbok) | 往返票 (wǎngfǎnpiào) |
| **정기권** | abono mensual | 定期券 (teikiken) | 정기권 (jeonggigwon) | 月票 (yuèpiào) |
| **유실물센터** | objetos perdidos | 遺失物取扱所 (ishitsubutsu toriatsukaino) | 유실물센터 (yusilmul senteo) | 失物招领 (shīwù zhāolǐng) |

### 문화 여행 규범

### 에티켓

| 행동 | EN | ES | JP | KR | CH |
|----------|----|----|----|----|----|
| **대기 행렬** | 기대 | 기대 | 덜 엄격 | 덜 엄격 | 가변 |
| **탑승** | 탑승 | 사람 내리기 우선 | **엄격한 순서** | 덜 엄격 | 밀침 문화 |
| **전화 통화** | OK (작은 소리) | OK | **금지** | 권장 안함 | 권장 안함 |
| **식사/음료** | 허용 (US) | 허용 | **금지** (일부 노선) | 권장 안함 | 권장 안함 |
| **대화** | 작은 목소리 | OK | **속삭임** | 조용 | 가변 |
| **우선석** | 어르신 | 어르신, 임산부 | **엄격** (자주 양보) | **엄격** (양보 기대) | 기대 |

### 다문화 학습자 학습 팁

- **EN**: 에스컬레이터 오른쪽 (UK), 왼쪽 (US)
- **ES**: 시에스타 여전히 일반 (2pm-5pm) — 가게 닫힘
- **JP**: 러시 아워 여성 전용 차량
- **JP**: 기차 조용함 (전화 통화 없음, 조용한 대화)
- **JP**: 신호등이 없어도 빨간불이면 기다림 (사회 규범)
- **KR**: 노약자석 엄격 — 쉽게 양보
- **KR**: 임산부 우선석 (분홍색 좌석)
- **CH**: 러시 아워 밀침 일반 (특히 베이징/상하이)
- **CH**: 지하철 별도 남녀 차량 (비-러시)
- **CN**: 모바일 결제 = 보편 (IC 카드 불필요)
- **CN**: 운전자가 보행자에게 경적

### 운송 접근성

| 기능 | US | ES | JP | KR | CH |
|---------|----|----|----|----|----|
| **휠체어 접근** | 가변 | 좋음 | 우수 | 우수 | 개선 중 |
| **다국어 표지** | EN/Spanish (일부) | ES/EN/Catalan | JP/EN/CH/KR | KR/EN/JP/CH | CH/EN |
| **음성 안내** | EN | ES | JP/EN | KR/EN/JP/CH | CH/EN |
| **시각 디스플레이** | 일반 | 일반 | 우수 | 우수 | 좋음 |
| **엘리베이터** | 제한 | 일반 | 표준 | 표준 | 증가 |
| **점자 포장** | 일부 | 좋음 | 우수 | 우수 | 좋음 |

### 빠른 참조 카드

| 모드 | EN | ES | JP | KR | CH |
|------|----|----|----|----|----|
| Walk | walking | a pie | 歩き | 걷기 | 走路 |
| Bike | bicycle | bicicleta | 自転車 | 자전거 | 自行车 |
| Bus | bus | autobús | バス | 버스 | 公交车 |
| Subway | subway | metro | 地下鉄 | 지하철 | 地铁 |
| Train | train | tren | 電車 | 열차 | 火车 |
| High-speed | high-speed rail | AVE | 新幹線 | KTX | 高铁 |
| Taxi | taxi | taxi | タクシー | 택시 | 出租车 |
| Rideshare | Uber | Uber/VTC | ライドシェア | 카카오택시 | 滴滴 |

---

## 학습자 의사결정 가이드

> **5개 언어 교통수단 매트릭스 (8개)**:
> - 도보: walking / a pie / 歩き / 걷기 / 走路
> - 자전거: bicycle / bicicleta / 自転車 / 자전거 / 自行车
> - 버스: bus / autobús / バス / 버스 / 公交车
> - 지하철: subway / metro / 地下鉄 / 지하철 / 地铁
> - 기차: train / tren / 電車 / 열차 / 火车
> - 고속철: high-speed rail / AVE / 新幹線 / KTX / 高铁
> - 택시: taxi / taxi / タクシー / 택시 / 出租车
> - 라읻셰어: Uber / Uber/VTC / ライドシェア / 카카오택시 / 滴滴

---

## 🇰🇷 한국어 학습자 노트 (Korean Learner Notes)

> 본 섹션은 한국어 학습자 대상의 추가 학습 가이드입니다.

### 한국어 화자가 다른 4개 언어 교통 어휘를 학습할 때 흔히 마주치는 함정

1. **고속철도 한자 한자어 매트릭스**:
   - 한국어: KTX (Korea Train eXpress) + 고속철도.
   - 일본어: 新幹線 (shinkansen). 한자 = 新 (신) + 幹線 (간선).
   - 중국어: 高铁 (gāotiě, 高 = 높을 + 铁 = 철). 영문 "high-speed rail" 의역.
   - 스페인어: AVE (Alta Velocidad Española, 약자).
   - 영어: high-speed rail, bullet train.
   - **함정**: 한국어 학습자가 다른 4개 언어에 "KTX" 단순 매핑 → 일본 신칸센/중국 高铁 다름. **KTX는 한국 고유 약자**.
   - **훈련법**: 고속철도 5개 언어 매트릭스 — 한국 KTX, 일본 신칸센, 중국 高铁 (gāotiě), 스페인 AVE, 미국 Acela. **각국 고유 명칭 학습**.

2. **지하철 어휘의 한자 한자어**:
   - 한국어: 지하철, 역, 출구, 입구, 환승 (한자어).
   - 일본어: 地下鉄, 駅, 出口, 入口, 乗換 (한자어).
   - 중국어: 地铁, 站, 出口, 入口, 换乘 (한자어).
   - 영어: subway, station, exit, entrance, transfer.
   - 스페인어: metro, estación, salida, entrada, transbordo.
   - **함정**: 한국어 학습자가 영어/스페인어 어휘 단순 매핑 → 한자 한자어 매트릭스 별도 학습.
   - **훈련법**: 지하철 어휘 5개 언어 매트릭스 — 한자 한자어 3개국 + 라틴/게르만 2개국. **5개 어원 시스템 비교**.

3. **한국어 T-money vs 일본 Suica vs 중국 모바일 페이**:
   - 한국: T-money (교통카드, IC 카드). 일본: Suica, Pasmo, Icoca (IC 카드). 중국: 모바일 페이 (IC 카드 거의 없음, Alipay/위챗페이).
   - 미국: Oyster (NYC), Clipper (SF) (도시별 제한). 스페인: Tarjeta Transporte Público (지역별 제한).
   - **함정**: 한국어 학습자가 중국 여행 시 T-money 사용 시도 → 중국 모바일 페이 필수. **중국은 IC 카드 아닌 모바일 페이**.
   - **훈련법**: 교통 결제 매트릭스 — KR/JP IC 카드 / CH 모바일 페이 / US/ES 도시별. **문화별 교통 결제 학습**.

4. **택시 한자 한자어 매트릭스**:
   - 한국어: 택시 (영어 차용) + 出租车 (한자어 격식) + 喊车.
   - 일본어: タクシー (영어 차용) + 出租车 (한자어 격식).
   - 중국어: 出租车 (chūzūchē) + 的士 (díshì, 광둥).
   - **함정**: 한국어 학습자가 영어 "taxi/cab" 단순 매핑 → 일본어/중국어 동일 어휘이나 발음 다름. **영어 차용의 한국어/일본어/중국어 진입**.
   - **훈련법**: 택시 어원 매트릭스 — 영어 taxi → 한국어 택시/일본어 タクシー/중국어 出租车. **영어 차용어 학습**.

5. **한국어 "지하철/전철" 구분**:
   - 한국어: 지하철 (도시 지하 철도) vs 전철 (도시 통근 철도). 일부 도시에서 혼용.
   - 일본어: 地下鉄 (지하철) vs 各停 (각역정차 도시 철도).
   - **함정**: "지하철" 단순 매핑 → 영어/스페인어 metro/subway. **전철** 별도 매핑 어려움.
   - **훈련법**: 지하철 vs 전철 매트릭스 — KR 지하철 (대도시) vs 전철 (통근/도시) vs JP 地下鉄 vs 各停. **한국어 두 어휘 학습**.

### 학습 전략

1. **우선순위 1**: 5개 언어 교통수단 8개 × 5언어 매트릭스 — 도보/자전거/버스/지하철/기차/고속철/택시/라읻셰어. **가장 빈도 높은 8개 동시 학습**.
2. **우선순위 2**: 고속철도 5개 언어 매트릭스 — KR KTX, JP 신칸센, CH 高铁 (gāotiě), ES AVE, US Acela. **각국 고유 명칭 학습**.
3. **우선순위 3**: 지하철 한자 한자어 3개국 + 라틴/게르만 매트릭스 — 駅/역/zhàn, 出口/출구/chūkǒu, 환승/乗換/换乘. **5개 어원 시스템 비교**.
4. **우선순위 4**: 교통 결제 매트릭스 — KR/JP IC 카드 / CH 모바일 페이 / US/ES 도시별. **문화별 교통 결제 학습**.
5. **우선순위 5**: 한국어 지하철/전철 구분 + 한자 한자어 + 영어 차용어 매트릭스. **한국어 두 어휘 학습**.

### 관련 한국어 위키 페이지

- [[travel-essentials]] — 일반 여행
- [[business-email]] — 비즈니스 교통
- [[time-calendar]] — 스케줄, 출발 시간
- [[numbers-counters]] — 수량, 가격
- [[shopping-money]] — 결제 수단
- [[tech-internet]] — 모바일 결제 앱

---

## 관련 페이지

- `[[travel-essentials]]` — 일반 여행
- `[[business-email]]` — 비즈니스 교통
- `[[time-calendar]]` — 스케줄, 출발 시간
- `[[numbers-counters]]` — 수량, 가격
- `[[shopping-money]]` — 결제 수단
- `[[tech-internet]]` — 모바일 결제 앱

## 출처

- JR (Japan Railways) 통계
- KORAIL (Korea Railroad Corp)
- CRRC (China Railway)
- Renfe (Spain) / ADIF
- Amtrak (US)
- Uber / Lyft / Didi / Kakao T 기업 데이터
- 国土交通省 (Japan MLIT) 통계
- `[Japanese/vocabulary/travel]`
- `[[wiki/Korean/vocabulary/여행]]`
- `[Spanish/vocabulary/transportation-vocabulary]`
- `[Chinese/sources/daily-routine-zh]`

---

**원본 (영어)**: [[transportation]] | **관련 미러**: [[transportation.es|Spanish]] · [[transportation.ja|Japanese]] · [[transportation.zh|Chinese]] | **정책**: ADR-0006
