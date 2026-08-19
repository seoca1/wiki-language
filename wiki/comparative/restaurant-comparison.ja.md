# レストランサービス — 言語間比較 (日本語版)

> 原文: [[restaurant-comparison]] (English) | 作成日: 2026-08-20 | ADR-0006
> **5言語のレストランフロー (挨拶・注文・会計) 比較**

---

## 早見表

### クイックリファレンステーブル

| 段階 | English | Spanish | Japanese | Korean | Chinese |
|-------|---------|---------|----------|--------|---------|
| **Greeting** | "Hi, table for two." | "Hola, mesa para dos." | "こんにちは、二人です。" (futari desu) | "안녕하세요, 두 명이요." (du myeong-iyo) | "你好，两位。" (liǎng wèi) |
| **Seated** | "Follow me, please." | "Sígame, por favor." | "どうぞ。" (dōzo) | "이쪽으로 오세요." (ijjokeuro oseyo) | "请跟我来。" (qǐng gēn wǒ lái) |
| **Menu request** | "Menu, please." | "La carta, por favor." | "メニューをください。" (menyū o kudasai) | "메뉴 주세요." (menyu juseyo) | "菜单。" (càidān) |
| **Order** | "I'll have..." | "Quisiera..." / "Para mí..." | "〜をお願いします。" (~o onegaishimasu) | "〜 주세요." (~ juseyo) | "我要..." (wǒ yào) |
| **Drink** | "Water, please." | "Agua, por favor." | "お水ください。" (omizu kudasai) | "물 주세요." (mul juseyo) | "请来杯水。" (qǐng lái bēi shuǐ) |
| **More food** | "More, please." | "Más, por favor." | "おかわりください。" (okawari kudasai) | "더 주세요." (deo juseyo) | "再来一份。" (zài lái yí fèn) |
| **Check** | "Check, please." | "La cuenta, por favor." | "お会計お願いします。" (o-kaikei onegaishimasu) | "계산서 주세요." (gyesanseo juseyo) | "买单。" (mǎidān) |
| **Pay** | "Card / Cash?" | "¿Tarjeta o efectivo?" | "カードで / 現金で。" (kādo de / genkin de) | "카드 / 현금." (kadeu / hyeongeum) | "刷卡 / 现金。" (shuākǎ / xiànjīn) |
| **Tip** | "Keep the change." | "Quédese con el cambio." | (no tipping culture) | (no tipping) | (no tipping Mainland) |
| **Goodbye** | "Thanks, bye!" | "Gracias, ¡adiós!" | "ごちそうさまでした。" (gochisousama deshita) | "잘 먹었습니다." (jal meogeosseumnida) | "谢谢，慢走。" (xièxiè, mànzǒu) |

### 予約語彙

| 概念 | English | Spanish | Japanese | Korean | Chinese |
|---------|---------|---------|----------|--------|---------|
| **Reservation** | Reservation / Booking | Reserva / Reservación | 予約 (yoyaku) | 예약 (yeyak) | 预订 (yùdìng) / 订位 (dìngwèi) |
| **Book (verb)** | "I'd like to reserve..." | "Quisiera reservar..." | "〜を予約したいのですが" (~o yoyaku shitai nodesu ga) | "〜 예약하고 싶어요" (~ yeyakhago sipeoyo) | "我想预订..." (wǒ xiǎng yùdìng) |
| **Time** | "At 7 PM" | "A las 7" | "7時に" (shichiji ni) | "7시에" (ilgop si-e) | "七点" (qī diǎn) |
| **Party size** | "Table for 4" | "Mesa para 4" | "4名です" (yonmei desu) | "4명이요" (ne myeong-iyo) | "四位" (sì wèi) |
| **Phone** | "Phone reservation" | "Reserva por teléfono" | "電話予約" (denwa yoyaku) | "전화 예약" (jeonhwa yeyak) | "电话预订" (diànhuà yùdìng) |
| **Walk-in** | "Walk-in" | "Sin reserva" | "飛び込み" (tobikomi) / "予約なし" (yoyaku nashi) | "예약 없이" (yeyak eopsi) | "直接去" (zhíjiē qù) |

### メニュー・会計語彙

| カテゴリ | English | Spanish | Japanese | Korean | Chinese |
|----------|---------|---------|----------|--------|---------|
| **Appetizer** | Appetizer / Starter | Aperitivo / Entrante | 前菜 (zensai) | 전채 (jeonchae) | 前菜 (qiáncài) |
| **Main course** | Main course | Plato principal | メイン / 主菜 (shusai) | 메인 | 主菜 (zhǔcài) |
| **Dessert** | Dessert | Postre | デザート | 디저트 / 후식 | 甜点 (tiándiǎn) |
| **Set meal** | Set meal / Combo | Menú del día | 定食 (teishoku) | 정식 (jeongsik) | 套餐 (tàocān) |
| **Bill/Check** | Check / Bill | La cuenta | お会計 (o-kaikei) | 계산서 (gyesanseo) | 账单 (zhàngdān) |
| **Cash** | Cash | Efectivo | 現金 (genkin) | 현금 (hyeongeum) | 现金 (xiànjīn) |
| **Card** | Credit card | Tarjeta | カード (kādo) | 카드 (kadeu) | 刷卡 (shuākǎ) |
| **Split** | Split the bill | Dividir la cuenta | 割り勘 (warikan) | 더치페이 / N빵 | AA制 (AA zhì) |
| **Tip** | Tip | Propina | チップ (rare) | 팁 (rare) | 小费 (rare) |

---

## 各言語詳細

### 🇬🇧 英語 (English)
- **Key terms**: menu, order, check, tip, server, hostess
- **Patterns**: "I'd like..." for polite order; "Can I get..." casual
- **Sources**: `[[wiki/English/vocabulary/food-vocabulary]]`

### 🇪🇸 スペイン語 (Spanish)
- **Key terms**: carta, cuenta, propina, camarero, pedir
- **Patterns**: Quisiera (conditional) = polite; *para llevar* = takeout
- **Regional variations**: Spain uses "carta"; LatAm often "menú" for food menu vs "carta" for drinks
- **Sources**: `[[wiki/Spanish/vocabulary/restaurant-vocabulary]]`

### 🇯🇵 日本語 (Japanese)
- **Key terms**: 注文 (chūmon), 会計 (kaikei), 予約 (yoyaku), 店員 (ten'in)
- **Patterns**: お願いします / ください polite; tipping absent (失礼 = rude)
- **Keigo / politeness level**: 店員 use 敬語 (keigo); いらっしゃいませ (irasshaimase) = welcome
- **Sources**: `[[wiki/Japanese/vocabulary/food-vocabulary]]`

### 🇰🇷 韓国語 (Korean)
- **Key terms**: 주문 (jumun), 계산 (gyesan), 예약 (yeyak), 종업원 (jongeopwon)
- **Patterns**: 주세요 (juseyo) standard polite; 합쇼체 for restaurants
- **Speech level**: 해요체 most common in casual restaurants; 합쇼체 in upscale
- **Sources**: `[[wiki/Korean/vocabulary/food-vocabulary]]`

### 🇨🇳 中国語 (Chinese)
- **Key terms**: 点菜 (diǎncài), 买单 (mǎidān), 预订 (yùdìng), 服务员 (fúwùyuán)
- **Patterns**: 请 + verb (请结账); 服务费 common in larger restaurants
- **Register / honorifics**: 您 (nín) for elders; no verb conjugation
- **Sources**: `[[wiki/Chinese/vocabulary/restaurant-zh]]`

---

## 主要な対比 (総合)

| 対比 | 学習者への示唆 |
|----------|--------------------------|
| **Tipping culture** | EN/ES: tipping expected; JP/KR/Mainland CH: tipping absent or unusual |
| **Politeness at counter** | JP/KR use full keigo; CH uses 请 + 服务员; EN/ES use por favor / please |
| **Bill request** | "Check" (EN) vs "La cuenta" (ES) vs お会計 (JP) vs 계산서 (KR) vs 买单 (CH) |
| **Set meal culture** | JP 定食, KR 정식, CH 套餐 are daily staples; less common in EN/ES restaurants |

---

## クイックリファレンスカード

> **Order**: お願いします (onegaishimasu) · 주세요 (juseyo) · 请 (qǐng)
> **Bill**: お会計 (o-kaikei) · 계산서 (gyesanseo) · 买单 (mǎidān) · la cuenta
> **Reservation**: 予約 (yoyaku) · 예약 (yeyak) · 预订 (yùdìng) · reserva
> **Tip**: チップ (rare) · 팁 (rare) · 小费 (rare)

---

## 🇯🇵 日本語学習者ノート (Japanese Learner Notes)

> 本セクションは日本語学習者向けの追加学習ガイドです。

### 日本語話者が他4言語のレストランサービスを学ぶ際の一般的な落とし穴

1. **チップ不要文化の適用**:
   - 日本語はチップ不要文化 (失礼) → 英語圏 (米国) では 15-20% チップ必須。
   - **落とし穴**: 米国レストランで「カードで」とだけ言ってテーブルを去る → チップ未払いでサーバーが困惑。
   - **練習法**: 米国/英国では「カードで + 20% チップ」/ スペイン/イタリアでは 5-10% チップをデフォルトに。

2. **「お会計」(Okaikei) vs 各国語表現**:
   - 日本語の「お会計お願いします」(o-kaikei onegaishimasu) → 英語 "Check, please"、韓国語 "계산서 주세요" (gyesanseo juseyo)、中国語 "买单" (mǎidān)。
   - **落とし穴**: 各言語の「check」「cuenta」「お会計」「계산서」「买单」が同じ機能だが、英語 "check" のみは和食レストランでは不自然。
   - **練習法**: 各言語の「請求」表現 (check / la cuenta / お会計 / 계산서 / 买单) を 5言語対応表で。

3. **料理注文時の politeness 階層**:
   - 日本語: 「〜をください」/「〜をお願いします」 → 韓国語: 「〜 주세요」 → 中国語: 「请 + 動詞」 → 英語: "I'll have..." / "Can I get..." → スペイン語: "Quisiera..." / "Para mí..."。
   - **落とし穴**: 韓国語「주세요」を「〜をください」の翻訳と思いがち → 韓国語ではより casual な場合あり。
   - **練習法**: 5言語の「注文」表現 politeness 階層を対訳表で。

4. **「ごちそうさまでした」(gochisousama deshita)**:
   - 日本語の「ごちそうさま」 = 食後の感謝 → 韓国語「잘 먹었습니다」(jal meogeosseumnida) → 中国語「谢谢」(xièxiè) → 英語 "Thanks" / スペイン語 "Gracias"。
   - **落とし穴**: 日本語話者が中国語で「ごちそうさま」をそのままに「好吃」と表現 → ネイティブは「ありがとう、美味しかった」の意味と理解。
   - **練習法**: 5言語の「食後感謝」表現 (ごちそうさま / 잘 먹었습니다 / 谢谢 / Thanks / Gracias) を 5言語対応表で。

5. **アレルギー・苦手食材の伝達**:
   - 日本語は「アレルギーがあります」「〜は食べられません」 → 韓国語、中国語、英語、スペイン語にも類似表現。
   - **落とし穴**: 日本語話者が英語圏で「I have an allergy」(深刻) と言って、軽い「苦手」(dislike) と同じニュアンス → ネイティブは shock。
   - **練習法**: 5言語の「アレルギー」 vs 「苦手」表現 (life-threatening vs dislike) を区別表で。

### 関連日本語ウィキページ

- `[[food-dining]]` — 食事語彙フル
- `[[polite-expressions-comparison]]` — レストランの register
- `[[numbers-counters]]` — 数量と価格
- `[[travel-essentials]]` — 旅行時のレストラン
- `[[untranslatable-concepts]]` — 翻訳不能な概念

### 学習ワークフロー推奨

1. **5言語レストラン表現対応表** (上記早見表) を暗記
2. **チップ慣行** を 5言語圏でマスター (EN/ES 必要、JP/KR/CH 不要)
3. **注文 politeness 階層** を 5言語対応で
4. **アレルギー伝達** (life-threatening vs dislike) を 5言語で
5. **食後感謝表現** (ごちそうさま / 잘 먹었습니다) を 5言語対応で

---

## 関連ページ

- `[[food-dining]]` — 食事語彙フル
- `[[polite-expressions-comparison]]` — レストランの register
- `[[numbers-counters]]` — 数量と価格
- `[[travel-essentials]]` — 旅行時のレストラン

## 出典

- 英語: `[[wiki/English/vocabulary/food-vocabulary]]`
- スペイン語: `[[wiki/Spanish/vocabulary/restaurant-vocabulary]]`
- 日本語: `[[wiki/Japanese/vocabulary/food-vocabulary]]`
- 韓国語: `[[wiki/Korean/vocabulary/food-vocabulary]]`
- 中国語: `[[wiki/Chinese/vocabulary/restaurant-zh]]`

---

**原文 (英語)**: [[restaurant-comparison]] | **関連ミラー**: [[restaurant-comparison.es|スペイン語]] · [[restaurant-comparison.ko|韓国語]] · [[restaurant-comparison.zh|中国語]] | **ポリシー**: ADR-0006
