# 数字与量词 — 跨语言对比 (中文版)

> 原文: [[numbers-counters]] (English) | 撰写日期: 2026-08-19 | ADR-0006
> **5种语言数字/量词/计数系统对比** — English · Spanish · Japanese · Korean · Chinese

---

## 速查表

### 基数 (1-10, 100, 1000, 10000)

| 数字 | English | Spanish | Japanese | Korean (汉数) | Korean (固有) | Chinese |
|------|---------|---------|----------|---------------|---------------|---------|
| 0 | zero | cero | ゼロ / 零 | 영 / 공 | - | 零 / 〇 |
| 1 | one | uno | 一 (いち) | 일 | 하나 (han-) | 一 (yī) |
| 2 | two | dos | 二 (に) | 이 | 둘 (tu-) | 二 (èr) / 两 (liǎng) |
| 3 | three | tres | 三 (さん) | 삼 | 셋 (se-) | 三 (sān) |
| 4 | four | cuatro | 四 (よん/し) | 사 | 넷 (ne-) | 四 (sì) |
| 5 | five | cinco | 五 (ご) | 오 | 다섯 (da-) | 五 (wǔ) |
| 6 | six | seis | 六 (ろく) | 육 | 여섯 (yeo-) | 六 (liù) |
| 7 | seven | siete | 七 (なな/しち) | 칠 | 일곱 (il-) | 七 (qī) |
| 8 | eight | ocho | 八 (はち) | 팔 | 여덟 (yeo-) | 八 (bā) |
| 9 | nine | nueve | 九 (きゅう/く) | 구 | 아홉 (a-) | 九 (jiǔ) |
| 10 | ten | diez | 十 (じゅう) | 십 | 열 (yeol) | 十 (shí) |
| 20 | twenty | veinte | 二十 (にじゅう) | 이십 | 스물 (seumul) | 二十 (èrshí) |
| 100 | one hundred | cien / ciento | 百 (ひゃく) | 백 | 온 (on) | 一百 (yībǎi) |
| 1,000 | one thousand | mil | 千 (せん) | 천 | - | 一千 (yīqiān) |
| 10,000 | ten thousand | diez mil | 万 (まん) | 만 | - | 一万 (yīwàn) |
| 100,000,000 | hundred million | cien millones | 億 (おく) | 억 | - | 一亿 (yīyì) |

### 关键结构差异

| 特征 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **基础** | 1,000 (千) | 1,000 (mil) | 10,000 (万) | 10,000 (만) | 10,000 (万) |
| **大数字分组** | 3 位 (千, 百万, 十亿) | 3 位 | 4 位 (万, 億, 兆) | 4 位 (만, 억, 조) | 4 位 (万, 亿, 兆) |
| **两系统** | 无 | 无 | 无 | **是** (汉数 + 固有) | 无 (但 两 vs 二) |
| **零在合成** | "one hundred **and** one" | "ciento uno" | "hyaku ichi" | "baek il" / "baek hana" | "yībǎi líng yī" |

### 序数

| 位置 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| 1st | first | primero / 1º | 一番目 (いちばんめ) | 첫째 / 제1 | 第一 (dì yī) |
| 2nd | second | segundo / 2º | 二番目 (にばんめ) | 둘째 / 제2 | 第二 (dì èr) |
| 3rd | third | tercero / 3º | 三番目 (さんばんめ) | 셋째 / 제3 | 第三 (dì sān) |
| nth | -th | -º / -ª | -番目 (-ばんめ) | -째 / 제- | 第- (dì-) |

- **西班牙语**: *primero/tercero* 在阳性名词前省略 -o (*primer libro, tercer piso*)
- **日语**: *dai-* 前缀表示正式 (*dai-ikkai* = 第1回)
- **韩语**: *je-* (汉数) + *beonchae* 表示正式; 固有 *cheot-/du-/se-* 表示非正式
- **中文**: *dì-* 前缀通用

---

## 量词 / 类别词 (大差异)

> **英语/西班牙语**: 无强制量词 — "三个苹果" = *tres manzanas*
> **日语/韩语/中文**: **强制** — 名词无法无需量词计数

### 日语量词 (助数詞) — 来自 `[Japanese/vocabulary/jp-counters]`

| 量词 | 汉字 | 用于 | 1 | 2 | 3 | 10 |
|------|------|------|---|---|---|---|
| 通用物件 | 個 | 小物件, 苹果, 蛋 | ひとつ | ふたつ | みっつ | とお |
| 人 | 人 | 人 | ひとり | ふたり | さんにん | じゅうにん |
| 长物件 | 本 | 笔, 瓶, 伞 | いっぽん | にほん | さんぼん | じゅっぽん |
| 扁物件 | 枚 | 纸, 票, 衬衫 | いちまい | にまい | さんまい | じゅうまい |
| 机器/车 | 台 | 车, 电脑, 电视 | いちだい | にだい | さんだい | じゅうだい |
| 楼层 | 階 | 楼层 | いっかい | にかい | さんがい | じゅっかい |
| 次/次数 | 回 | 次数 | いっかい | にかい | さんかい | じゅっかい |
| 分 | 分 | 分钟 | いっぷん | にふん | さんぷん | じゅっぷん |
| 时段 | 時間 | 小时 | いちじかん | にじかん | さんじかん | じゅうじかん |
| 年龄 | 歳 | 岁 | いっさい | にさい | さんさい | じゅっさい |
| 动物 (小) | 匹 | 猫, 狗, 鱼 | いっぴき | にひき | さんびき | じゅっぴき |
| 书籍 | 冊 | 书, 杂志 | いっさつ | にさつ | さんさつ | じゅっさつ |
| 杯/碗 | 杯 | 饮料, 饭碗 | いっぱい | にはい | さんばい | じゅっぱい |

**音韵规则**:
- *h/b/p* 交替 (本: *hon/bon/pon*)
- *s/sh* 交替 (分: *fun/pun*)
- *k/g* 交替 (階: *kai/gai*)

### 韩语量词 (수사 + 단위 명사) — 固有 vs 汉数

| 量词 | 用于 | 固有 (1-99) | 韩汉 (100+) | 备注 |
|------|------|---------------|---------------|------|
| 개 (gae) | 通用物件 | 하나, 둘, 셋... | 일개, 이개... | 默认回退 |
| 명 (myeong) | 人 (礼貌) | 한 명, 두 명 | 일 명, 이 명 | 尊称用 *bun* |
| 분 (bun) | 人 (尊称) | 한 분, 두 분 | - | 长辈, 顾客 |
| 마리 (mari) | 动物 | 한 마리, 두 마리 | - | |
| 권 (gwon) | 书籍 | 한 권, 두 권 | - | |
| 장 (jang) | 扁物 (纸, 票) | 한 장, 두 장 | - | |
| 대 (dae) | 机器, 车 | 한 대, 두 대 | - | |
| 병 (byeong) | 瓶 | 한 병, 두 병 | - | |
| 잔 (jan) | 杯/玻璃 | 한 잔, 두 잔 | - | |
| 그릇 (geureut) | 碗 | 한 그릇, 두 그릇 | - | |
| 번 (beon) | 次 | 한 번, 두 번 | - | |
| 시 (si) | 小时 (整点) | 한 시, 두 시 | - | 时段固有 |
| 분 (bun) | 分 | 한 분(?) → 일 분 | - | 分汉数 |
| 살 (sal) | 年龄 | 한 살, 두 살 | - | 固有 |
| 세 (se) | 年龄 (正式) | - | 일 세, 이 세 | 汉数 |

**关键规则**: 固有韩语数字 (1-99) + 固有量词; 韩汉 + 汉数量词。 *年龄* 使用固有 (*sal*) 或汉数 (*se*)。

### 中文量词 (量词) — 来自 `[Chinese/vocabulary/measure-words-zh]`

| 量词 | 拼音 | 用于 | 示例 |
|------|------|------|------|
| 个 | gè | 通用 (默认) | 三个苹果 (3 apples) |
| 位 | wèi | 人 (礼貌) | 两位客人 (2 guests) |
| 只 | zhǐ | 小动物 | 一只猫 (1 cat) |
| 条 | tiáo | 长条物 (鱼, 河, 裤子) | 一条鱼 (1 fish) |
| 张 | zhāng | 扁物 (纸, 票, 床) | 三张票 (3 tickets) |
| 本 | běn | 书 | 两本书 (2 books) |
| 双 | shuāng | 双 (鞋, 筷子) | 一双筷子 (1 对) |
| 辆 | liàng | 车辆 | 一辆车 (1 car) |
| 台 | tái | 机器, 电子 | 一台电脑 (1 电脑) |
| 杯 | bēi | 杯/玻璃 | 一杯水 (1 杯水) |
| 碗 | wǎn | 碗 | 两碗饭 (2 碗饭) |
| 次 | cì | 次 | 去过三次 (去过 3 次) |
| 遍 | biàn | 次 (完整周期) | 读了两遍 (读了 2 遍) |

**特殊**: *两 (liǎng)* 不是 *二 (èr)* 在量词前表示 "二" — *两个人*, *两本书*。

---

## 数字文化特殊说明

### 日语
- **4 (shi/yon)** & **9 (ku/kyuu)** — 医院, 酒店, 礼品避免 (*shini* = 死, *ku* = 苦)
- **礼金**: 偏好奇数 (3, 5, 7); 避免 4, 9, 偶数
- **计数手势**: 食指 = 1, 食指+中指 = 2... 拇指收 = 5

### 韩语
- **4 (sa)** — *四音恐惧*, 4 楼电梯常标 "F"
- **秋夕/春节**: 白包, 奇数金额
- **年龄**: 韩年龄 = (当前年 - 出生年) + 1 (所有人 1/1 增 1 岁)

### 中文
- **4 (sì)** — 避免 (音似 死 *sǐ* = 死); 8 (bā) = 吉利 (发 *fā* = 发财); 6 (liù) = 顺利 (流 *liú*)
- **电话号码/车牌**: 8 付溢价, 避免 4
- **红包 (hongbao)**: 偶数 (除 4); 666, 888, 999 吉利

### 西班牙语
- **10亿**: *billón* = 10¹² (长尺度) vs 美 *billion* = 10⁹ — 金融翻译陷阱
- **小数分隔符**: 逗号 (1,5 = 一点五); 千分位: 点或空格 (1.000 或 1 000)

### 英语
- **And**: "one hundred **and** one" (英式) vs "one hundred one" (美式)
- **大数字**: 短尺度 (million=10⁶, billion=10⁹, trillion=10¹²)

---

## 学习者实用决策指南

| 学习... | 优先掌握 | 原因 |
|---------|---------|------|
| **日语** | *hon, mai, hiki, kai, fun, sai* + 1-10 不规则形 | 覆盖 80% 日常计数 |
| **韩语** | 固有 1-10 + *gae, myeong, mari, jang, beon, si, sal* | 固有数字 + 前 7 量词 = 生存 |
| **中文** | *ge, wei, zhang, ben, tiao, liang, bei, ci* + 两 vs 二 规则 | *ge* 是通用回退; 两 在量词前强制 |
| **西班牙语** | 基数 1-100 + *millón/millones* 一致 (*un millón DE*) | *Millón* 需要 *de*; *cien* vs *ciento* |
| **英语** | 序数后缀 (-st, -nd, -rd, -th) + "a/an" 在数字前 | "a hundred" vs "one hundred" |

---

## 跨语言练习场景

### 场景: 点 3 瓶啤酒

- EN: "Three beers, please."
- ES: "Tres cervezas, por favor."
- JP: "ビールを三本ください。" (*biiru o san-bon kudasai*)
- KR: "맥주 세 병 주세요." (*maekju se byeong juseyo*)
- CH: "来三瓶啤酒。" (*lái sān píng píjiǔ*)

### 场景: "我有 2 个弟弟"

- EN: "I have two younger brothers."
- ES: "Tengo dos hermanos menores."
- JP: "弟が二人います。" (*otouto ga futari imasu*) — *futari* (2 人)
- KR: "남동생이 둘 있어요." (*namdongsaeng-i dul isseoyo*) — 固有 *dul*
- CH: "我有两个弟弟。" (*wǒ yǒu liǎng gè dìdi*) — *liǎng* + *ge*

### 场景: "这是我第 5 次去日本"

- EN: "This is my fifth time in Japan."
- ES: "Es la quinta vez que voy a Japón."
- JP: "日本に来るのは五回目です。" (*nihon ni kuru no wa go-kaime desu*)
- KR: "일본에 온 게 다섯 번째예요." (*ilbon-e on ge daseot beonjjae-yeyo*)
- CH: "这是我第五次来日本。" (*zhè shì wǒ dì wǔ cì lái Rìběn*)

---

## 相关页面

- `[[greetings]]` — 报时用数字
- `[[travel-essentials]]` — 价格, 日期, 时刻表
- `[[food-dining]]` — 食物量词
- `[[politeness-honorifics]]` — 尊称量词 (*bun, wei, mei, sama*)

## 来源

- 英语: `[English/vocabulary/basic-vocabulary]`
- 西班牙语: `[Spanish/vocabulary/basic-vocabulary]`, `[Spanish/vocabulary/time-prepositions-vocabulary]`
- 日语: `[Japanese/vocabulary/jp-counters]`, `[Japanese/vocabulary/kanji-n5]`, `[Japanese/sources/2026-07-13_Kanji_N5_100]`
- 韩语: `[[index]]`, `[Korean/vocabulary/topik1-starter]`, `[Korean/sources/daily-life-basics]`
- 中文: `[Chinese/vocabulary/numbers-zh]`, `[Chinese/vocabulary/measure-words-zh]`, `[Chinese/sources/pinyin-basics-zh]`

---

## 🇨🇳 中文学习者笔记 (Chinese Learner Notes)

> 本节是面向中文母语学习者的额外学习指南。

### 中文母语者在学习其他4种语言数字量词时的常见陷阱

1. **两 vs 二 的差异**:
   - 中文 "两" 在量词前 / "二" 在数字中 → 学员假设其他语言也对应。
   - **陷阱**: 日语 ふたり (2 人) vs ににん (2 人); 韩语 둘 (2) vs 이 (2); 西语 dos (2) no diferencia; 英语 two 通用。
   - **训练法**: 制作"两 vs 二"对照表 — 中: 两个人 (两) / 第二 (二); 日: 2人 读作 ふたり; 韩: 2人 读作 두 명。

2. **量词的必要性**:
   - 中文量词必须 (一本书/一个苹果) → 学员假设其他语言都强制。
   - **陷阱**: 英语/西语不需要量词 (a book / un libro) — 直数名词。
   - **训练法**: 学习新量词时, 配合三个常用名词 (例: 一本书/一张纸/一支笔)。

3. **韩语固有 vs 汉数数字**:
   - 中文数字单一 (一二三四) → 学员假设韩语日语也单一。
   - **陷阱**: 韩语有固有 (하나/둘/셋) 和汉数 (일/이/삼) 两套; 日语有训读 (ひと/ふた) 和音读 (いち/に); 西班牙语 uno 数字与 un 冠词区分。
   - **训练法**: 学习韩语时, 区分 "固有数" 用于计数 + "汉数" 用于日期/金额 — 实际使用混乱点。

4. **大数字进位的差异**:
   - 中文以 万 为基础 (万/亿/兆) → 学员假设其他语言也相同。
   - **陷阱**: 英语/西语以 千 为基础 (thousand/million/billion); 学习英文大数字时需重新调整。
   - **训练法**: 制作 "万 vs 千" 对比表 — 1万 = 10千; 1亿 = 10000万; 1 million = 100万; 1 billion = 10亿 (英文) = 100亿 (中文短尺度差异)。

5. **日语 4/9 的禁忌**:
   - 中文 4 (sì) 避免 (音似 死) → 学员假设日语 4 (shi/よん) 也回避。
   - **陷阱**: 日语 4 读 shi (同 死) 或 よん (yon); 9 读 く (同 苦) 或 きゅう (kyuu); 韩国 4 楼标 "F"; 西方 13 禁忌。
   - **训练法**: 跨文化数字禁忌对比 — 学习每个语言的"数字迷信"。

### 相关中文维基页面

- [Chinese/vocabulary/numbers-zh] — 中文数字词汇
- [Chinese/vocabulary/measure-words-zh] — 中文量词
- [Chinese/culture/chinese-numbers-zh] — 中文数字文化
- [Chinese/sources/pinyin-basics-zh] — 中文拼音基础
- [Chinese/grammar/basic-particles] — 中文基本助词

### 学习工作流程推荐

1. **背诵对比表** (基数/序数/量词)
2. **量词分类学习** (人/物/书/车 等)
3. **两 vs 二 区分** (中文学习其他语言时的核心难点)
4. **大数字进位对比** (万 vs 千 系统)
5. **场景练习** (购物/点餐/报时间/算账)

---

**原文 (英语)**: [[numbers-counters]] | **相关镜像**: [[numbers-counters.es|西班牙语]] · [[numbers-counters.ja|日语]] · [[numbers-counters.ko|韩语]] | **政策**: ADR-0006
