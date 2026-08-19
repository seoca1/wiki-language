# 食物与餐饮 — 跨语言对比 (中文版)

> 原文: [[food-dining]] (English) | 撰写日期: 2026-08-19 | ADR-0006
> **5语言食物与餐饮对比** — English · Spanish · Japanese · Korean · Chinese

---

## 速查表: 餐厅流程对比

| 阶段 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **进门** | "Table for two, please." | "Mesa para dos, por favor." | "二人です。" (Futari desu.) | "두 명이요." (Du myeong-iyo.) | "两位。" (Liǎng wèi.) |
| **菜单** | "Can I see the menu?" | "¿La carta, por favor?" | "メニューをください。" (Menyū o kudasai.) | "메뉴 주세요." (Menyu juseyo.) | "菜单给我。" (Càidān gěi wǒ.) |
| **推荐** | "What do you recommend?" | "¿Qué me recomienda?" | "おすすめは何ですか？" (Osusume wa nan desu ka?) | "추천해 주세요." (Chucheonhae juseyo.) | "推荐什么？" (Tuījiàn shénme?) |
| **点单** | "I'll have the..." | "Voy a tomar..." / "Quisiera..." | "〜をお願いします。" (~o onegaishimasu.) | "〜 주세요." (~ juseyo.) | "我要个..." (Wǒ yào gè...) |
| **水** | "Tap water, please." | "Agua del grifo, por favor." | "お水ください。" (Omizu kudasai.) | "물 주세요." (Mul juseyo.) | "来杯水。" (Lái bēi shuǐ.) |
| **结账** | "Check, please." | "La cuenta, por favor." | "お会計お願いします。" (O-kaikei onegaishimasu.) | "계산서 주세요." (Gyesanseo juseyo.) | "买单。" (Mǎidān.) |
| **付款** | "Can I pay by card?" | "¿Puedo pagar con tarjeta?" | "カードで払えますか？" (Kādo de haraemasu ka?) | "카드 돼요?" (Kadeu dwaeyo?) | "能刷卡吗？" (Néng shuākǎ ma?) |

---

## 速查表: 用餐时间

| 用餐 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **早餐** | Breakfast | Desayuno | 朝食 (ちょうしょく) / 朝ごはん | 아침식사 / 아침밥 | 早餐 (zǎocān) |
| **午餐** | Lunch | Almuerzo / Comida | 昼食 (ちゅうしょく) / 昼ごはん | 점심식사 / 점심밥 | 午餐 (wǔcān) / 中饭 |
| **晚餐** | Dinner | Cena | 夕食 (ゆうしょく) / 晩ごはん | 저녁식사 / 저녁밥 | 晚餐 (wǎncān) / 晚饭 |
| **小吃** | Snack | Merienda / Tapas | おやつ / 軽食 (けいしょく) | 간식 / 야식 | 点心 (diǎnxīn) / 夜宵 |

---

## 速查表: 餐厅类型

| 类型 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **餐厅** | Restaurant | Restaurante | レストラン / 食堂 (しょくどう) | 식당 / 레스토랑 | 餐厅 (cāntīng) / 饭店 |
| **咖啡厅** | Café | Cafetería / Café | カフェ / 喫茶店 (きっさてん) | 카페 / 다방 | 咖啡厅 (kāfēitīng) |
| **居酒屋** | Izakaya / Pub | Taberna / Bar | 居酒屋 (いざかや) | 이자카야 / 술집 | 居酒屋 (jūjiǔwū) / 小酒馆 |
| **街头小吃** | Food stall / Truck | Puesto / Food truck | 屋台 (やたい) / 移動販売 | 포장마차 / 푸드트럭 | 路边摊 (lùbiāntān) / 小吃车 |
| **自助餐** | Buffet | Bufé / Libre | バイキング / ビュッフェ | 뷔페 / 무한리필 | 自助餐 (zìzhùcān) |
| **快餐** | Fast food | Comida rápida | ファストフード / 牛丼屋 (ぎゅうどんや) | 패스트푸드 / 분식집 | 快餐 (kuàicān) |

---

## 速查表: 饮食限制

| 限制 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **素食** | Vegetarian | Vegetariano | ベジタリアン / 菜食 (さいしょく) | 채식주의자 / 비건 | 素食 (sùshí) / 吃素 (chī sù) |
| **纯素** | Vegan | Vegano | ビーガン / 完全菜食 (かんぜんさいしょく) | 비건 / 완전채식 | 纯素 (chúnsù) |
| **清真** | Halal | Halal | ハラール | 할랄 | 清真 (qīngzhēn) |
| **犹太洁食** | Kosher | Kosher | コーシャ | 코셔 | 犹太洁食 (yóutài jiéshí) |
| **无麸质** | Gluten-free | Sin gluten | グルテンフリー / 小麦不使用 (こむぎふしよう) | 글루텐 프리 / 밀가루 없는 | 无麸质 (wú fūzhì) |
| **过敏** | Allergy | Alergia | アレルギー (arerugī) | 알레르기 | 过敏 (guòmǐn) |
| **不吃猪肉** | No pork | Sin cerdo | 豚肉抜き (ぶたにくぬき) / ポークフリー | 돼지고기 빼주세요 | 不吃猪肉 (bù chī zhūròu) |
| **不吃牛肉** | No beef | Sin res | 牛肉抜き (ぎゅうにくぬき) / ビーフフリー | 소고기 빼주세요 | 不吃牛肉 (bù chī niúròu) |
| **辣度** | Mild / Medium / Hot | Poco / Medio / Muy picante | 辛くない / 普通 / 激辛 (げきから) | 안 맵게 / 보통 / 맵게 | 不辣 / 微辣 / 中辣 / 特辣 |

---

## 速查表: 食物类别

### 蛋白质

| English | Spanish | Japanese | Korean | Chinese |
|---------|---------|----------|--------|---------|
| **牛肉** | Res / Carne de res | 牛肉 (ぎゅうにく) | 소고기 (sogogi) | 牛肉 (niúròu) |
| **猪肉** | Cerdo / Carne de cerdo | 豚肉 (ぶたにく) | 돼지고기 (dwaejigogi) | 猪肉 (zhūròu) |
| **鸡肉** | Pollo | 鶏肉 (とりにく) | 닭고기 (dakgogi) | 鸡肉 (jīròu) |
| **鱼** | Pescado | 魚 (さかな) / 魚介類 (ぎょかいるい) | 생선 (saengseon) / 해산물 (haesanmul) | 鱼 (yú) / 海鲜 (hǎixiān) |
| **虾** | Camarón / Gambas | 海老 (えび) | 새우 (saeu) | 虾 (xiā) |
| **豆腐** | Tofu | 豆腐 (とうふ) | 두부 (dubu) | 豆腐 (dòufu) |
| **鸡蛋** | Huevo | 卵 (たまご) | 계란 (gyeran) / 달걀 (dalgyal) | 鸡蛋 (jīdàn) |

### 主食 / 蔬菜

| English | Spanish | Japanese | Korean | Chinese |
|---------|---------|----------|--------|---------|
| **米** | Arroz | 米 (こめ) / ご飯 (ごはん) | 쌀 (ssal) / 밥 (bap) | 米 (mǐ) / 饭 (fàn) |
| **面** | Fideos / Tallarines | 麺 (めん) / ラーメン / うどん / そば | 국수 (guksu) / 면 (myeon) | 面 (miàn) / 面条 (miàntiáo) |
| **面包** | Pan | パン | 빵 (ppang) | 面包 (miànbāo) |
| **土豆** | Patata / Papa | じゃがいも | 감자 (gamja) | 土豆 (tǔdòu) / 马铃薯 |
| **洋葱** | Cebolla | 玉ねぎ (たまねぎ) | 양파 (yangpa) | 洋葱 (yángcōng) |
| **大蒜** | Ajo | ニンニク | 마늘 (maneul) | 大蒜 (dàsuàn) |
| **姜** | Jengibre | 生姜 (しょうが) | 생강 (saenggang) | 姜 (jiāng) |
| **辣椒** | Chile / Guindilla | 唐辛子 (とうがらし) | 고추 (gochu) | 辣椒 (làjiāo) |
| **酱油** | Salsa de soja | 醤油 (しょうゆ) | 간장 (ganjang) | 酱油 (jiàngyóu) |
| **芝麻油** | Aceite de sésamo | ごま油 (ごまあぶら) | 참기름 (chamgireum) | 芝麻油 (zhīmayóu) |

---

## 速查表: 点单模式

### 🇬🇧 英语
- **直接**: "I'll have the salmon." / "Give me the burger."
- **礼貌**: "Could I get the...?" / "I'd like to order the..."
- **修饰语**: "with/without", "on the side", "well-done/medium-rare"

### 🇪🇸 西班牙语
- **Quisiera** + 名词: *Quisiera la paella.* (条件礼貌)
- **Me pone** + 名词: *Me pone un café.* (西班牙常用)
- **Para mí** + 名词: *Para mí, el pescado.* (口语)
- **Sin / Con**: *Sin cebolla, con queso extra.*

### 🇯🇵 日语
- **~をお願いします** (~o onegaishimasu) — 标准礼貌
- **~をください** (~o kudasai) — 稍直接
- **~はありますか** (~wa arimasu ka) — "有...吗？"
- **量词 + つ/個/本/枚** — 数量必需

### 🇰🇷 韩语
- **~ 주세요** (~ juseyo) — 标准礼貌请求
- **~ 하나 주세요** (~ hana juseyo) — 一个请 (口语中常省略)
- **~ 빼주세요** (~ ppaejuseyo) — "去掉..." (不加)
- **~ 더 주세요** (~ deo juseyo) — "再加" (续杯)

### 🇨🇳 中文
- **我要...** (Wǒ yào...) — 直接 "我要..."
- **给我来个...** (Gěi wǒ lái gè...) — 口语 "给我来..."
- **来份...** (Lái fèn...) — "来一份..."
- **不要...** (Bú yào...) / **不放...** (Bú fàng...) — "不要..." / "不放..."

---

## 速查表: 餐饮礼仪对比

| 行为 | English (US/UK) | Spanish | Japanese | Korean | Chinese |
|------|-----------------|---------|----------|--------|---------|
| **开始吃** | "Bon appétit" / "Enjoy" | *Buen provecho* | *Itadakimasu* (合掌) | *Jal meokkesseumnida* (잘 먹겠습니다) | *Man man chi* (慢慢吃) / *Kuai chi* (快吃) |
| **吃完** | "Thank you" | *Gracias* | *Gochisousama deshita* | *Jal meogeosseumnida* (잘 먹었습니다) | *Chi bao le* (吃饱了) |
| **倒酒** | 自倒或为他人倒 | 为他人倒 | 为他人倒 (永不自倒) | 为他人倒 (双手) | 先为长辈/上级倒 |
| **拒绝酒** | "No thanks" | *No, gracias* | *Kekkou desu* (手盖杯) | *Jeongjunghi* (정중히) / 手盖杯 | *Bu yao le* (不要了) / 盖杯 |
| **AA 制** | 常见 (Venmo) | *A escote* / 分开 | 罕见 (长者付) | *N빵* / 长者付 | *AA制* / 主人请客 |
| **小费** | 15-20% (美) | 5-10% (西班牙) / 10% (拉美) | **无** (失礼) | **无** (罕见) | **无** (大陆) / 10% (港台) |
| **吸面条** | 失礼 | 失礼 | **礼貌** (享受) | 可接受 | 可接受 (北方) |
| **端碗** | 罕见 | 罕见 | **是** (饭/味噌汤) | **是** (饭/汤) | **是** (饭) |
| **筷子插饭** | N/A | N/A | **禁忌** (葬礼) | **禁忌** (葬礼) | **禁忌** (葬礼) |
| **传菜** | 手/餐具 | 手/餐具 | 筷子→筷子 = **禁忌** | 勺/筷 | 公筷 | 公筷 (公筷) |

---

## 速查表: 招牌菜

| 菜系 | 菜 | 关键词 |
|------|----|----|
| **English** | Fish & chips, Sunday roast, Full English breakfast | batter, mushy peas, yorkshire pudding, black pudding |
| **Spanish** | Paella, Tortilla española, Gazpacho, Jamón ibérico | arroz, azafrán, patatas, huevo, pimentón |
| **Japanese** | Sushi, Ramen, Tempura, Tonkatsu, Okonomiyaki | shari, neta, dashi, panko, sauce |
| **Korean** | Bibimbap, Bulgogi, Kimchi jjigae, Samgyeopsal, Tteokbokki | gochujang, doenjang, sesame oil, banchan |
| **Chinese** | Mapo tofu, Peking duck, Xiaolongbao, Hot pot, Dim sum | doubanjiang, huajiao, soy sauce, ginger, scallion |

---

## 速查表: 常用短语 (按情境)

### "我对...过敏"

- EN: "I'm allergic to [nuts/shellfish/gluten]."
- ES: "Soy alérgico/a a [los frutos secos/mariscos/gluten]."
- JP: "[ナッツ/甲殻類/グルテン]アレルギーがあります。" (*[nattsu/kakakurui/guruten] arerugī ga arimasu.*)
- KR: "[견과류/갑각류/글루텐] 알레르기가 있어요." (*[gyeongwaryu/kapgangryu/geulluten] alleogiga isseoyo.*)
- CH: "我对[坚果/甲壳类/麸质]过敏。" (*Wǒ duì [jiānguó/jiǎqiáolèi/fūzhì] guòmǐn.*)

### "这是素的吗？/ 这是清真的吗？"

- EN: "Is this vegetarian?" / "Is this halal?"
- ES: "¿Es vegetariano?" / "¿Es halal?"
- JP: "これはベジタリアン向けですか？" / "ハラール対応ですか？"
- KR: "이거 채식인가요?" / "할랄인가요?"
- CH: "这是素的吗？" / "这是清真的吗？"

### "能不能不辣？"

- EN: "Can you make it less spicy?"
- ES: "¿Puede hacerlo menos picante?"
- JP: "辛くないようにできますか？" (*Karaku nai yō ni dekimasu ka?*)
- KR: "안 맵게 해주실 수 있어요?" (*An maepge haejusil su isseoyo?*)
- CH: "能不能不放辣椒？" (*Néng bùnéng bù fàng làjiāo?*)

### "我要打包带走"

- EN: "Can I get a to-go box?" / "Box this up, please."
- ES: "¿Me lo pone para llevar?" / "Para llevar, por favor."
- JP: "お持ち帰りできますか？" (*Omochikaeri dekimasu ka?*)
- KR: "포장해 주세요." (*Pojanghae juseyo.*)
- CH: "打包。" (*Dāobāo.*) / "打包带走。" (*Dāobāo dàizǒu.*)

---

## 关键对比 (综合)

| 对比 | 洞察 |
|------|------|
| **用餐前/后礼貌** | 日韩 *itadakimasu/gochisousama* + 中 *man man chi* 最仪式化; 英语/西语最轻 |
| **小费** | 美 15-20% / 西 5-10% / 日韩中无 (但港台 10%) |
| **AA 制** | 英语圈常见; 日韩长者付; 中 AA 制近年兴起 |
| **筷子禁忌** | 日韩中: 不插饭 (葬礼), 不互相传筷; 西无 |
| **过敏表述** | 日语 *アレルギー* 借用英语; 韩语 *알레르기* 同样; 中文 *过敏* 本土 |

---

## 🇨🇳 中文学习者笔记 (Chinese Learner Notes)

> 本节是面向中文母语学习者的额外学习指南。

### 中文母语者在学习其他4种语言食物词汇时的常见陷阱

1. **"rice" 的不同含义**:
   - 中文 *米 / 饭* 区分 → 学员对日语 *米 (こめ) / ご飯 (ごはん)* 感到困惑。
   - **陷阱**: 日语 *米 (kome)* = 未煮的米; *ご飯 (gohan)* = 煮熟的饭; 韩语 *쌀 (ssal)* / *밥 (bap)* 同理。
   - **训练法**: 整理 5 语言"米 vs 饭"对照 (CN 米/饭 / JP 米/ご飯 / KR 쌀/밥 / EN rice [ambiguous] / ES arroz crudo/cocido)。

2. **"noodles" 的丰富类别**:
   - 中文 *面* 通用 → 学员对日语 麺/ラーメン/うどん/そば 感到困惑。
   - **陷阱**: 日语有 4-5 种面 (拉面/乌冬/荞麦); 中文 *面/面条/拉面* 不细分。
   - **训练法**: 学习日本面类型 (ラーメン = 拉面, うどん = 乌冬, そば = 荞麦)。

3. **"tofu" 的汉字假朋友**:
   - 中文 *豆腐 (dòufu)* → 学员对日语 *豆腐 (tōfu)* 感到熟悉但发音不同。
   - **陷阱**: 日语 *豆腐 (とうふ, tōfu)* 读音完全不同; 韩语 *두부 (dubu)* 不同; 英语 tofu 来自日语。
   - **训练法**: 整理 5 语言"豆腐"发音 (CN dòufu / JP tōfu / KR dubu / EN tofu / ES tofu)。

4. **"spicy" 的等级**:
   - 中文 *不辣/微辣/中辣/特辣* 4 档 → 学员对日语 *辛くない/普通/激辛* 感到简洁。
   - **陷阱**: 日语 *激辛 (gekikara)* 仅 1 个等级; 韩语 *안 맵게/보통/맵게* 3 档。
   - **训练法**: 整理 5 语言辣度等级 (CN 4 档 / JP 3 档 / KR 3 档 / EN mild/med/hot 3 档 / ES poco/medio/muy 3 档)。

5. **"chopsticks in rice" 禁忌**:
   - 中文 *筷子插饭* 禁忌 → 学员对日韩同样禁忌感到熟悉。
   - **陷阱**: 日韩中共有禁忌 (象征葬礼的香); 西/英语圈无此概念。
   - **训练法**: 学习东亚筷子禁忌 (不插饭/不互相传筷/不指人/不敲碗)。

6. **"small eat" 的文化差异**:
   - 中文 *点心 (diǎnxīn)* 已知 → 学员对粤语 *dim sum* 感到困惑。
   - **陷阱**: *dim sum* 是粤语 (点心) 借入英语; 日语 *点心 (tenshin)* 也有但含义略异 (小食/糕点)。
   - **训练法**: 整理 *点心/dim sum/tenshin* 跨语言含义 (粤语源, 含义: 广式早茶小食)。

7. **"allergy" 的表达**:
   - 中文 *过敏* 本土 → 学员对日语 *アレルギー (arerugī)* 感到熟悉。
   - **陷阱**: 日韩 *アレルギー/알레르기* 借自英语, 含义与中文 *过敏* 相同。
   - **训练法**: 整理 5 语言过敏表达 (CN 过敏 / JP アレルギー / KR 알레르기 / EN allergy / ES alergia)。

### 相关中文维基页面

- [Chinese/vocabulary/food-zh] — 中文食物词汇
- [Chinese/culture/chinese-cuisine-zh] — 中国菜
- [Chinese/vocabulary/restaurant-zh] — 中文餐厅词汇
- [Chinese/culture/chinese-dining-etiquette-zh] — 中文餐桌礼仪
- [Chinese/culture/teahouse-culture] — 茶馆文化

### 学习工作流程推荐

1. **5 语言核心食物词表** (米/面/肉/鱼 — 5 语言对照)
2. **5 语言餐厅流程词** (进门/点单/买单 — 5 语言对照)
3. **5 语言饮食限制词** (素食/清真/过敏 — 5 语言对照)
4. **5 语言辣度等级** (3-4 档 — 5 语言对照)
5. **5 语言招牌菜** (5 国名菜 — 配图记忆)

---

## 相关页面

- `[[travel-essentials]]` — 旅行场景餐厅流程
- `[[politeness-honorifics]]` — 点单语域
- `[[numbers-counters]]` — 数量, 价格
- `[[shopping-money]]` — 市场/食物购物
- `[[health-body]]` — 饮食限制词汇

## 来源

- EN: `[English/vocabulary/food-vocabulary]`, `[English/vocabulary/travel]`
- ES: `[Spanish/vocabulary/food-vocabulary]`, `[Spanish/vocabulary/restaurant-vocabulary]`, `[Spanish/vocabulary/mexican_food-vocabulary]`
- JP: `[Japanese/vocabulary/food-vocabulary]`, `[Japanese/sources/food-and-dining]`
- KR: `[Korean/vocabulary/food-vocabulary]`, `[Korean/sources/food-and-dining]`
- CN: `[Chinese/vocabulary/measure-words-zh]`, `[Chinese/sources/daily-routine-zh]`

---

**原文 (英语)**: [[food-dining]] | **相关镜像**: [[food-dining.es|西班牙语]] · [[food-dining.ja|日语]] · [[food-dining.ko|韩语]] | **政策**: ADR-0006
