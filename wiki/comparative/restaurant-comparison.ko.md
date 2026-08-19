# 식당 서비스 — 다국어 비교 (한국어판)

> 원본: [[restaurant-comparison]] (English) | 작성일: 2026-08-20 | ADR-0006
> **5개 언어 식당 동선 비교 — 인사, 주문, 메뉴, 결제, 예약**

---

## 빠른 참조 표

| 단계 | English | Spanish | Japanese | Korean | Chinese |
|-------|---------|---------|----------|--------|---------|
| **인사** | "Hi, table for two." | "Hola, mesa para dos." | "こんにちは、二人です。" (futari desu) | "안녕하세요, 두 명이요." (du myeong-iyo) | "你好，两位。" (liǎng wèi) |
| **자리 안내** | "Follow me, please." | "Sígame, por favor." | "どうぞ。" (dōzo) | "이쪽으로 오세요." (ijjokeuro oseyo) | "请跟我来。" (qǐng gēn wǒ lái) |
| **메뉴 요청** | "Menu, please." | "La carta, por favor." | "メニューをください。" (menyū o kudasai) | "메뉴 주세요." (menyu juseyo) | "菜单。" (càidān) |
| **주문** | "I'll have..." | "Quisiera..." / "Para mí..." | "〜をお願いします。" (~o onegaishimasu) | "〜 주세요." (~ juseyo) | "我要..." (wǒ yào) |
| **음료** | "Water, please." | "Agua, por favor." | "お水ください。" (omizu kudasai) | "물 주세요." (mul juseyo) | "请来杯水。" (qǐng lái bēi shuǐ) |
| **추가** | "More, please." | "Más, por favor." | "おかわりください。" (okawari kudasai) | "더 주세요." (deo juseyo) | "再来一份。" (zài lái yí fèn) |
| **계산** | "Check, please." | "La cuenta, por favor." | "お会計お願いします。" (o-kaikei onegaishimasu) | "계산서 주세요." (gyesanseo juseyo) | "买单。" (mǎidān) |
| **결제** | "Card / Cash?" | "¿Tarjeta o efectivo?" | "カードで / 現金で。" (kādo de / genkin de) | "카드 / 현금." (kadeu / hyeongeum) | "刷卡 / 现金。" (shuākǎ / xiànjīn) |
| **팁** | "Keep the change." | "Quédese con el cambio." | (no tipping culture) | (no tipping) | (no tipping Mainland) |
| **작별** | "Thanks, bye!" | "Gracias, ¡adiós!" | "ごちそうさまでした。" (gochisousama deshita) | "잘 먹었습니다." (jal meogeosseumnida) | "谢谢，慢走。" (xièxiè, mànzǒu) |

### 예약 어휘

| 개념 | English | Spanish | Japanese | Korean | Chinese |
|---------|---------|---------|----------|--------|---------|
| **예약** | Reservation / Booking | Reserva / Reservación | 予約 (yoyaku) | 예약 (yeyak) | 预订 (yùdìng) / 订位 (dìngwèi) |
| **예약 (동사)** | "I'd like to reserve..." | "Quisiera reservar..." | "〜を予約したいのですが" (~o yoyaku shitai nodesu ga) | "〜 예약하고 싶어요" (~ yeyakhago sipeoyo) | "我想预订..." (wǒ xiǎng yùdìng) |
| **시간** | "At 7 PM" | "A las 7" | "7時に" (shichiji ni) | "7시에" (ilgop si-e) | "七点" (qī diǎn) |
| **인원** | "Table for 4" | "Mesa para 4" | "4名です" (yonmei desu) | "4명이요" (ne myeong-iyo) | "四位" (sì wèi) |
| **전화** | "Phone reservation" | "Reserva por teléfono" | "電話予約" (denwa yoyaku) | "전화 예약" (jeonhwa yeyak) | "电话预订" (diànhuà yùdìng) |
| **워크인** | "Walk-in" | "Sin reserva" | "飛び込み" (tobikomi) / "予約なし" (yoyaku nashi) | "예약 없이" (yeyak eopsi) | "直接去" (zhíjiē qù) |

### 메뉴 & 결제 어휘

| 카테고리 | English | Spanish | Japanese | Korean | Chinese |
|----------|---------|---------|----------|--------|---------|
| **전채** | Appetizer / Starter | Aperitivo / Entrante | 前菜 (zensai) | 전채 (jeonchae) | 前菜 (qiáncài) |
| **메인** | Main course | Plato principal | メイン / 主菜 (shusai) | 메인 | 主菜 (zhǔcài) |
| **디저트** | Dessert | Postre | デザート | 디저트 / 후식 | 甜点 (tiándiǎn) |
| **정식** | Set meal / Combo | Menú del día | 定食 (teishoku) | 정식 (jeongsik) | 套餐 (tàocān) |
| **계산서** | Check / Bill | La cuenta | お会計 (o-kaikei) | 계산서 (gyesanseo) | 账单 (zhàngdān) |
| **현금** | Cash | Efectivo | 現金 (genkin) | 현금 (hyeongeum) | 现金 (xiànjīn) |
| **카드** | Credit card | Tarjeta | カード (kādo) | 카드 (kadeu) | 刷卡 (shuākǎ) |
| **더치페이** | Split the bill | Dividir la cuenta | 割り勘 (warikan) | 더치페이 / N빵 | AA制 (AA zhì) |
| **팁** | Tip | Propina | チップ (드물다) | 팁 (드물다) | 小费 (드물다) |

---

## 핵심 대조 (종합)

| 대조 | 학습자 함의 |
|----------|--------------------------|
| **팁 문화** | EN/ES: 팁 기대; JP/KR/Mainland CH: 팁 없음 또는 비정상 |
| **카운터 공손** | JP/KR는 전체 keigo 사용; CH는 请 + 服务员; EN/ES는 por favor / please |
| **계산서 요청** | "Check" (EN) vs "La cuenta" (ES) vs お会計 (JP) vs 계산서 (KR) vs 买单 (CH) |
| **정식 문화** | JP 定食, KR 정식, CH 套餐는 일상 주식; EN/ES 식당에서 덜 일반 |

---

## 학습자 의사결정 가이드

> **주문**: お願いします (onegaishimasu) · 주세요 (juseyo) · 请 (qǐng)
> **계산서**: お会計 (o-kaikei) · 계산서 (gyesanseo) · 买单 (mǎidān) · la cuenta
> **예약**: 予約 (yoyaku) · 예약 (yeyak) · 预订 (yùdìng) · reserva
> **팁**: チップ (드물다) · 팁 (드물다) · 小费 (드물다)

> **식당 동선 매트릭스 (5개 언어)**:
> 1. **인사** — 손님 입장 → "Hi/Hola/こんにちは/안녕하세요/你好" + 인원
> 2. **자리 안내** — "Follow me" / "Sígame" / "どうぞ" / "이쪽으로 오세요" / "请跟我来"
> 3. **메뉴** — "Menu please" / "La carta" / "メニューをください" / "메뉴 주세요" / "菜单"
> 4. **주문** — "I'll have" / "Quisiera" / "〜をお願いします" / "주세요" / "我要"
> 5. **계산** — "Check please" / "La cuenta" / "お会計" / "계산서" / "买单"
> 6. **작별** — "Thanks bye" / "Adiós" / "ごちそうさまでした" / "잘 먹었습니다" / "谢谢，慢走"

---

## 🇰🇷 한국어 학습자 노트 (Korean Learner Notes)

> 본 섹션은 한국어 학습자 대상의 추가 학습 가이드입니다.

### 한국어 화자가 다른 4개 언어 식당 서비스를 학습할 때 흔히 마주치는 함정

1. **팁 문화의 한국어 학습자 매핑**:
   - 한국어는 팁 문화 없음. 한국 식당/카페/호텔 = 팁 불필요. 일본어 チップ, 중국어 小费, 스페인어 propina 모두 드물게 사용.
   - 영어 팁 문화 (15-20%) 한국어 학습자 적응 필요.
   - **함정**: 한국식 "팁 불필요" 패턴을 미국/유럽 식당에 적용 → 무례 인식. 미국 식당에서 15-20% 팁 미지급 시 서버 부끄러움.
   - **훈련법**: 팁 매트릭스 — 미국 15-20%, 유럽 5-10%, 한국/일본/중국 (대륙) 0%. **문화별 팁 매핑 필수**.

2. **식당 인사/주문 한국어 경어**:
   - 한국어 식당: 캐주얼 식당 = 해요체 (-요), 격식 식당 = 합쇼체 (-ㅂ니다). 직원이 손님에게 합쇼체.
   - 일본어 식당: 캐주얼 = です/ます, 격식 = 敬語. 직원이 손님에게 敬語.
   - 영어/스페인어 식당: please + thank you 기본. 캐주얼/격식 구분 약함.
   - **함정**: 한국어 학습자가 영어 식당에서 "I'd like..." 캐주얼 정중 패턴을 캐주얼 식당에 적용 → "Gimme..." 식 너무 캐주얼.
   - **훈련법**: 식당 경어 매트릭스 — KR/JP 4단계 vs EN/ES 2단계. **식당 등급별 (캐주얼/격식) 등록 선택**.

3. **"안녕히 가세요/계세요" 의 한국어 작별 특수성**:
   - 한국어 작별: "안녕히 가세요" (to leaving person) vs "안녕히 계세요" (to staying person). 일본어/중국어/영어/스페인어는 단일 작별.
   - **함정**: 한국어 학습자가 영어 "Goodbye" 단순 매핑 → "안녕히 가세요/계세요" 구분 무시.
   - **훈련법**: 한국어 작별 **2-way 구분** 매트릭스 — 떠나는/머무는 별도. **한국어 특수성**.

4. **"잘 먹겠습니다/먹었습니다" 의 한국어 식사 인사**:
   - 한국어: 식사 시작 "잘 먹겠습니다" / 식사 끝 "잘 먹었습니다" — **매우 한국적**.
   - 일본어: "いただきます" (식사 시작) / "ごちそうさまでした" (식사 끝). 동등한 일본 문화.
   - 영어: "Bon appétit" (격식, 덜 일반) / "Enjoy" (캐주얼).
   - 스페인어: "Buen provecho".
   - 중국어: 식사 인사 적음.
   - **함정**: 한국어 학습자가 "잘 먹겠습니다" 다른 4개 언어에 단순 매핑 → 영어 "Bon appétit" 어색.
   - **훈련법**: 식사 인사 5개 언어 — 한국어/일본어 가장 명시적. **한국어 식사 인사 문화 보존**.

5. **메뉴 어휘의 한자 vs 고유어**:
   - 한국어 메뉴: "전채/메인/디저트/정식" (한자어 차용) / "안주/반찬/국/밥" (고유어).
   - 일본어 메뉴: "前菜/メイン/デザート" (한자 + 외래어) / "お通し/お米/味噌汁" (일본 고유).
   - **함정**: 한자어 메뉴 = 같은 의미 가정 → 한국어 한자음 vs 일본 음 다른 발음.
   - **훈련법**: 한자 메뉴 한자어 3개국 발음 매트릭스. 한자 동일 ≠ 발음/의미 동일.

### 학습 전략

1. **우선순위 1**: 5개 언어 식당 동선 6단계 × 5언어 매트릭스 — 인사/자리/메뉴/주문/계산/작별. **동시 암기**.
2. **우선순위 2**: 팁 문화 매트릭스 — 미국 15-20%, 유럽 5-10%, 한국/일본/중국 0%. **문화별 팁 매핑 필수**.
3. **우선순위 3**: 식당 경어 매트릭스 — KR/JP 4단계 vs EN/ES 2단계. **식당 등급별 등록 선택**.
4. **우선순위 4**: 한국어 작별 "안녕히 가세요/계세요" 2-way 구분 + "잘 먹겠습니다/먹었습니다" 식사 인사. **한국어 특수성 명시 학습**.
5. **우선순위 5**: 한자 메뉴 어휘 3개국 발음 매트릭스 — 한자 동일, 발음 다름. 일본어 メイン/메인 (한자) vs 한국어 メイン (차용) vs 중국어 主菜 (zhǔcài) — 한자 1글자 = 3개국 발음.

### 관련 한국어 위키 페이지

- [[food-dining]] — 음식 + 식사 어휘
- [[polite-expressions-comparison]] — 식당 등록
- [[numbers-counters]] — 수량/가격
- [[travel-essentials]] — 여행 시 식당
- [[shopping-money]] — 결제 어휘

---

## 관련 페이지

- `[[food-dining]]` — 전체 음식 + 식사 어휘
- `[[polite-expressions-comparison]]` — 식당 등록
- `[[numbers-counters]]` — 수량과 가격
- `[[travel-essentials]]` — 여행 맥락 식당

## 출처

- English: `[[wiki/English/vocabulary/food-vocabulary]]`
- Spanish: `[[wiki/Spanish/vocabulary/restaurant-vocabulary]]`
- Japanese: `[[wiki/Japanese/vocabulary/food-vocabulary]]`
- Korean: `[[wiki/Korean/vocabulary/food-vocabulary]]`
- Chinese: `[[wiki/Chinese/vocabulary/restaurant-zh]]`

---

**원본 (영어)**: [[restaurant-comparison]] | **관련 미러**: [[restaurant-comparison.es|Spanish]] · [[restaurant-comparison.ja|Japanese]] · [[restaurant-comparison.zh|Chinese]] | **정책**: ADR-0006
