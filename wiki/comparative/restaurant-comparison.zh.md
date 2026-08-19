# 餐厅服务 — 跨语言对比 (中文版)

> 原文: [[restaurant-comparison]] (English) | 撰写日期: 2026-08-19 | ADR-0006
> **5种语言餐厅流程/点餐/付款对比** — English · Spanish · Japanese · Korean · Chinese

---

## 速查表

| 阶段 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **问候** | "Hi, table for two." | "Hola, mesa para dos." | "こんにちは、二人です。" (futari desu) | "안녕하세요, 두 명이요." (du myeong-iyo) | "你好，两位。" (liǎng wèi) |
| **入座** | "Follow me, please." | "Sígame, por favor." | "どうぞ。" (dōzo) | "이쪽으로 오세요." (ijjokeuro oseyo) | "请跟我来。" (qǐng gēn wǒ lái) |
| **请求菜单** | "Menu, please." | "La carta, por favor." | "メニューをください。" (menyū o kudasai) | "메뉴 주세요." (menyu juseyo) | "菜单。" (càidān) |
| **点餐** | "I'll have..." | "Quisiera..." / "Para mí..." | "〜をお願いします。" (~o onegaishimasu) | "〜 주세요." (~ juseyo) | "我要..." (wǒ yào) |
| **饮料** | "Water, please." | "Agua, por favor." | "お水ください。" (omizu kudasai) | "물 주세요." (mul juseyo) | "请来杯水。" (qǐng lái bēi shuǐ) |
| **加菜** | "More, please." | "Más, por favor." | "おかわりください。" (okawari kudasai) | "더 주세요." (deo juseyo) | "再来一份。" (zài lái yí fèn) |
| **账单** | "Check, please." | "La cuenta, por favor." | "お会計お願いします。" (o-kaikei onegaishimasu) | "계산서 주세요." (gyesanseo juseyo) | "买单。" (mǎidān) |
| **支付** | "Card / Cash?" | "¿Tarjeta o efectivo?" | "カードで / 現金で。" (kādo de / genkin de) | "카드 / 현금." (kadeu / hyeongeum) | "刷卡 / 现金。" (shuākǎ / xiànjīn) |
| **小费** | "Keep the change." | "Quédese con el cambio." | (无小费文化) | (无小费) | (无小费大陆) |
| **告别** | "Thanks, bye!" | "Gracias, ¡adiós!" | "ごちそうさまでした。" (gochisousama deshita) | "잘 먹었습니다." (jal meogeosseumnida) | "谢谢，慢走。" (xièxiè, mànzǒu) |

### 预订词汇

| 概念 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **预订** | Reservation / Booking | Reserva / Reservación | 予約 (yoyaku) | 예약 (yeyak) | 预订 (yùdìng) / 订位 (dìngwèi) |
| **预订 (动词)** | "I'd like to reserve..." | "Quisiera reservar..." | "〜を予約したいのですが" (~o yoyaku shitai nodesu ga) | "〜 예약하고 싶어요" (~ yeyakhago sipeoyo) | "我想预订..." (wǒ xiǎng yùdìng) |
| **时间** | "At 7 PM" | "A las 7" | "7時に" (shichiji ni) | "7시에" (ilgop si-e) | "七点" (qī diǎn) |
| **人数** | "Table for 4" | "Mesa para 4" | "4名です" (yonmei desu) | "4명이요" (ne myeong-iyo) | "四位" (sì wèi) |
| **电话** | "Phone reservation" | "Reserva por teléfono" | "電話予約" (denwa yoyaku) | "전화 예약" (jeonhwa yeyak) | "电话预订" (diànhuà yùdìng) |
| **临时** | "Walk-in" | "Sin reserva" | "飛び込み" (tobikomi) / "予約なし" (yoyaku nashi) | "예약 없이" (yeyak eopsi) | "直接去" (zhíjiē qù) |

### 菜单与支付词汇

| 类别 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **前菜** | Appetizer / Starter | Aperitivo / Entrante | 前菜 (zensai) | 전채 (jeonchae) | 前菜 (qiáncài) |
| **主菜** | Main course | Plato principal | メイン / 主菜 (shusai) | 메인 | 主菜 (zhǔcài) |
| **甜点** | Dessert | Postre | デザート | 디저트 / 후식 | 甜点 (tiándiǎn) |
| **套餐** | Set meal / Combo | Menú del día | 定食 (teishoku) | 정식 (jeongsik) | 套餐 (tàocān) |
| **账单** | Check / Bill | La cuenta | お会計 (o-kaikei) | 계산서 (gyesanseo) | 账单 (zhàngdān) |
| **现金** | Cash | Efectivo | 現金 (genkin) | 현금 (hyeongeum) | 现金 (xiànjīn) |
| **卡** | Credit card | Tarjeta | カード (kādo) | 카드 (kadeu) | 刷卡 (shuākǎ) |
| **AA** | Split the bill | Dividir la cuenta | 割り勘 (warikan) | 더치페이 / N빵 | AA制 (AA zhì) |
| **小费** | Tip | Propina | チップ (rare) | 팁 (rare) | 小费 (rare) |

---

## 各语言详情

### 🇬🇧 英语 (English)
- **关键词**: menu, order, check, tip, server, hostess
- **模式**: "I'd like..." 礼貌点餐; "Can I get..." 随意
- **来源**: `[[wiki/English/vocabulary/food-vocabulary]]`

### 🇪🇸 西班牙语 (Spanish)
- **关键词**: carta, cuenta, propina, camarero, pedir
- **模式**: Quisiera (条件式) = 礼貌; *para llevar* = 外卖
- **地区差异**: 西班牙使用 "carta"; LatAm 通常 "menú" 用于食物菜单 vs "carta" 用于饮料菜单
- **来源**: `[[wiki/Spanish/vocabulary/restaurant-vocabulary]]`

### 🇯🇵 日语 (Japanese)
- **关键词**: 注文 (chūmon), 会計 (kaikei), 予約 (yoyaku), 店員 (ten'in)
- **模式**: お願いします / ください 礼貌; 无小费 (失礼 = 粗鲁)
- **敬语 / 礼貌级别**: 店员使用 敬語 (keigo); いらっしゃいませ (irasshaimase) = 欢迎
- **来源**: `[[wiki/Japanese/vocabulary/food-vocabulary]]`

### 🇰🇷 韩语 (Korean)
- **关键词**: 주문 (jumun), 계산 (gyesan), 예약 (yeyak), 종업원 (jongeopwon)
- **模式**: 주세요 (juseyo) 标准礼貌; 합쇼체 用于餐厅
- **语阶**: 해요체 在随意餐厅最常见; 합쇼체 在高档餐厅
- **来源**: `[[wiki/Korean/vocabulary/food-vocabulary]]`

### 🇨🇳 中文 (Chinese)
- **关键词**: 点菜 (diǎncài), 买单 (mǎidān), 预订 (yùdìng), 服务员 (fúwùyuán)
- **模式**: 请 + 动词 (请结账); 服务费 在大餐厅常见
- **语阶 / 敬语**: 您 (nín) 用于长辈; 无动词变位
- **来源**: `[[wiki/Chinese/vocabulary/restaurant-zh]]`

---

## 关键对比 (综合)

| 对比 | 学习者启示 |
|------|----------|
| **小费文化** | 英/西: 期望小费; 日/韩/大陆中: 无小费或不寻常 |
| **柜台礼貌** | 日/韩使用完整 keigo; 中使用 请 + 服务员; 英/西 使用 por favor / please |
| **账单请求** | "Check" (英) vs "La cuenta" (西) vs お会計 (日) vs 계산서 (韩) vs 买单 (中) |
| **套餐文化** | 日 定食, 韩 정식, 中 套餐 是日常主食; 英/西餐厅较少 |

---

## 速查卡

> **点餐**: お願いします (onegaishimasu) · 주세요 (juseyo) · 请 (qǐng)
> **账单**: お会計 (o-kaikei) · 계산서 (gyesanseo) · 买单 (mǎidān) · la cuenta
> **预订**: 予約 (yoyaku) · 예약 (yeyak) · 预订 (yùdìng) · reserva
> **小费**: チップ (rare) · 팁 (rare) · 小费 (rare)

---

## 相关页面

- `[[food-dining]]` — 完整食物+用餐词汇
- `[[polite-expressions-comparison]]` — 餐厅语阶
- `[[numbers-counters]]` — 数量与价格
- `[[travel-essentials]]` — 旅行中的餐厅

## 来源

- 英语: `[[wiki/English/vocabulary/food-vocabulary]]`
- 西班牙语: `[[wiki/Spanish/vocabulary/restaurant-vocabulary]]`
- 日语: `[[wiki/Japanese/vocabulary/food-vocabulary]]`
- 韩语: `[[wiki/Korean/vocabulary/food-vocabulary]]`
- 中文: `[[wiki/Chinese/vocabulary/restaurant-zh]]`

## 变更记录

- `2026-08-11`: 创建 — 餐厅服务流程 (问候 → 点餐 → 付款) 跨 5 种语言

---

## 🇨🇳 中文学习者笔记 (Chinese Learner Notes)

> 本节是面向中文母语学习者的额外学习指南。

### 中文母语者在学习其他4种语言餐厅时的常见陷阱

1. **小费文化的差异**:
   - 中国内陆无小费文化 → 学员假设其他语言也类似。
   - **陷阱**: 美国 15-20% 小费常态; 西班牙 5-10% 小费; 日本/韩国小费罕见甚至失礼。
   - **训练法**: 出境前确认目的国小费文化 — 避免失礼或花费不足。

2. **套餐文化的差异**:
   - 中文 套餐 (固定搭配) 餐厅常见 → 学员假设其他语言也对应。
   - **陷阱**: 日语 定食 (teishoku) = 套餐; 韩语 정식 (jeongsik) = 套餐; 英语 "set meal" 或 "combo" 不常见。
   - **训练法**: 区分"点菜" vs "套餐" — 每个语言的不同单词。

3. **结账方式的差异**:
   - 中文 买单 (mǎidān) 通用 → 学员假设其他语言也对应。
   - **陷阱**: 英语 "the check" / "the bill" (美/英); 日语 お会計 (o-kaikei); 韩语 계산서 (gyesanseo); 西语 la cuenta。
   - **训练法**: 准备 5种语言"我要结账"独立表达 — 出国旅行必备。

4. **菜品分类的差异**:
   - 中文 前菜/主菜/甜点 分类 → 学员假设其他语言也对应。
   - **陷阱**: 日语 前菜 (zensai) / 主菜 (shusai) / デザート (dessert); 韩语 전채 (jeonchae) / 메인 / 후식; 西语 Aperitivo / Plato principal / Postre。
   - **训练法**: 制作"菜品分类"对照表 — 5种语言各自的菜单分类。

5. **服务的礼貌语差异**:
   - 中文 请 (qǐng) + 动词 (请结账) → 学员假设其他语言也对应。
   - **陷阱**: 日语动词变形 (お会計お願いします); 韩语 주세요 (juseyo); 西语 Quisiera (条件式); 英语 "Could I have...?" 间接。
   - **训练法**: 学习每种语言的"礼貌请求"句式 — 5种语言各自不同。

### 相关中文维基页面

- [Chinese/vocabulary/restaurant-zh] — 中文餐厅词汇
- [Chinese/culture/chinese-food-culture-zh] — 中文饮食文化
- [Chinese/grammar/basic-particles] — 中文基本助词
- [Chinese/sources/daily-routine-zh] — 中文日常用语
- [Chinese/vocabulary/food-zh] — 中文饮食词汇

### 学习工作流程推荐

1. **背诵对比表** (餐厅流程/预订/菜单/支付)
2. **小费文化对比** (5种语言各自的文化)
3. **套餐/点菜区分** (每个语言的不同单词)
4. **结账方式** (5种语言各自表达)
5. **场景练习** (预订/点餐/AA/抱怨/结账)

---

**原文 (英语)**: [[restaurant-comparison]] | **相关镜像**: [[restaurant-comparison.es|西班牙语]] · [[restaurant-comparison.ja|日语]] · [[restaurant-comparison.ko|韩语]] | **政策**: ADR-0006
