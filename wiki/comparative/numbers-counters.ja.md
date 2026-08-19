# 数字と助数詞 — 言語間比較 (日本語版)

> 原文: [[numbers-counters]] (English) | 作成日: 2026-08-20 | ADR-0006
> **5言語の数字・助数詞 (counters) 比較**

---

## 早見表

### 基数 (1-10, 100, 1000, 10000)

| 数字 | English | Spanish | Japanese | Korean (Sino) | Korean (Native) | Chinese |
|--------|---------|---------|----------|---------------|-----------------|---------|
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

### 構造的差異

| 機能 | English | Spanish | Japanese | Korean | Chinese |
|---------|---------|---------|----------|--------|---------|
| **Base** | 1,000 (thousand) | 1,000 (mil) | 10,000 (万) | 10,000 (만) | 10,000 (万) |
| **Large number grouping** | 3 digits (thousand, million, billion) | 3 digits | 4 digits (万, 億, 兆) | 4 digits (만, 억, 조) | 4 digits (万, 亿, 兆) |
| **Two systems** | No | No | No | **Yes** (Sino-Korean + Native) | No (but 两 vs 二) |
| **Zero in compound** | "one hundred **and** one" | "ciento uno" | "hyaku ichi" | "baek il" / "baek hana" | "yībǎi líng yī" |

### 序数

| 位置 | English | Spanish | Japanese | Korean | Chinese |
|----------|---------|---------|----------|--------|---------|
| 1st | first | primero / 1º | 一番目 (いちばんめ) | 첫째 / 제1 | 第一 (dì yī) |
| 2nd | second | segundo / 2º | 二番目 (にばんめ) | 둘째 / 제2 | 第二 (dì èr) |
| 3rd | third | tercero / 3º | 三番目 (さんばんめ) | 셋째 / 제3 | 第三 (dì sān) |
| nth | -th | -º / -ª | -番目 (-ばんめ) | -째 / 제- | 第- (dì-) |

- **Spanish**: *primero/tercero* drop -o before masculine noun (*primer libro, tercer piso*)
- **Japanese**: *dai-* prefix for formal (*dai-ikkai* = 第1回)
- **Korean**: *je-* (Sino) + *beonchae* for formal; native *cheot-/du-/se-* for informal
- **Chinese**: *dì-* prefix universally

### 助数詞/類別詞 (the big divergence)

> **English/Spanish**: 助数詞なし — "three apples" = *tres manzanas*
> **Japanese/Korean/Chinese**: **必須** — 名詞は助数詞なしで数えられない

### 日本語助数詞 (助数詞)

| 助数詞 | 漢字 | 用途 | 1 | 2 | 3 | 10 |
|---------|-------|---------|---|---|---|---|
| General objects | 個 | Small objects, apples, eggs | ひとつ | ふたつ | みっつ | とお |
| People | 人 | Humans | ひとり | ふたり | さんにん | じゅうにん |
| Long objects | 本 | Pens, bottles, umbrellas | いっぽん | にほん | さんぼん | じゅっぽん |
| Flat objects | 枚 | Paper, tickets, shirts | いちまい | にまい | さんまい | じゅうまい |
| Machines/Cars | 台 | Cars, computers, TVs | いちだい | にだい | さんだい | じゅうだい |
| Floors | 階 | Building floors | いっかい | にかい | さんがい | じゅっかい |
| Times/Occurrences | 回 | Times doing something | いっかい | にかい | さんかい | じゅっかい |
| Minutes | 分 | Minutes | いっぷん | にふん | さんぷん | じゅっぷん |
| Hours (duration) | 時間 | Hours | いちじかん | にじかん | さんじかん | じゅうじかん |
| Age | 歳 | Years old | いっさい | にさい | さんさい | じゅっさい |
| Animals (small) | 匹 | Cats, dogs, fish | いっぴき | にひき | さんびき | じゅっぴき |
| Books | 冊 | Books, magazines | いっさつ | にさつ | さんさつ | じゅっさつ |
| Cups/Bowls | 杯 | Drinks, bowls of rice | いっぱい | にはい | さんばい | じゅっぱい |

### 韓国語助数詞 (수사 + 단위 명사)

| 助数詞 | 用途 | 固有 (1-99) | Sino-Korean (100+) | ノート |
|---------|---------|---------------|-------------------|-------|
| 개 (gae) | 一般物体 | 하나, 둘, 셋... | 일개, 이개... | デフォルトフォールバック |
| 명 (myeong) | 人 (丁寧) | 한 명, 두 명 | 일 명, 이 명 | *bun* (敬語) を使う |
| 분 (bun) | 人 (敬語) | 한 분, 두 분 | - | 目上、顧客 |
| 마리 (mari) | 動物 | 한 마리, 두 마리 | - | |
| 권 (gwon) | 書籍 | 한 권, 두 권 | - | |
| 장 (jang) | 薄いもの (紙、切符) | 한 장, 두 장 | - | |
| 대 (dae) | 機械、車 | 한 대, 두 대 | - | |
| 병 (byeong) | ボトル | 한 병, 두 병 | - | |
| 잔 (jan) | カップ/グラス | 한 잔, 두 잔 | - | |
| 그릇 (geureut) | 碗 | 한 그릇, 두 그릇 | - | |
| 번 (beon) | 回 | 한 번, 두 번 | - | |
| 시 (si) | 時 (o'clock) | 한 시, 두 시 | - | 時の固有 |
| 살 (sal) | 年齢 | 한 살, 두 살 | - | 固有 |
| 세 (se) | 年齢 (フォーマル) | - | 일 세, 이 세 | Sino |

### 中国語助数詞 (量词)

| 量詞 | 拼音 | 用途 | 例 |
|--------------|--------|--------|---------|
| 个 | gè | 一般 (デフォルト) | 三个苹果 (3 apples) |
| 位 | wèi | 人 (丁寧) | 两位客人 (2 guests) |
| 只 | zhǐ | 動物 (小) | 一只猫 (1 cat) |
| 条 | tiáo | 細長いもの (魚、川、ズボン) | 一条鱼 (1 fish) |
| 张 | zhāng | 薄いもの (紙、切符、ベッド) | 三张票 (3 tickets) |
| 本 | běn | 書籍 | 两本书 (2 books) |
| 双 | shuāng | ペア (靴、箸) | 一双筷子 (1 pair chopsticks) |
| 辆 | liàng | 車両 | 一辆车 (1 car) |
| 台 | tái | 機械、エレクトロニクス | 一台电脑 (1 computer) |
| 杯 | bēi | カップ/グラス | 一杯水 (1 glass water) |
| 碗 | wǎn | 碗 | 两碗饭 (2 bowls rice) |
| 次 | cì | 回 | 去过三次 (went 3 times) |
| 遍 | biàn | 回 (完全サイクル) | 读了两遍 (read twice) |

**特殊**: *两 (liǎng)* not *二 (èr)* before classifiers for "two" — *两个人*, *两本书*.

---

## 数字に関する文化ノート

### 🇯🇵 日本
- **4 (shi/yon)** & **9 (ku/kyuu)** — 病院、ホテル、贈り物で回避 (*shini* = 死, *ku* = 苦)
- **ご祝儀**: 奇数優先 (3, 5, 7); 4, 9, 偶数回避
- **数え指**: 人差し指=1, 人差し+中=2...親指を折り=5

### 🇰🇷 韓国
- **4 (sa)** — *tetraphobia*, 4階がエレベーターで「F」表示
- **Chuseok/Seollal**: 白い封筒に奇数金額
- **年齢**: 韓国年齢 = (現在の年 - 誕生年) + 1 (皆 1月 1 日に年を取る)

### 🇨🇳 中国
- **4 (sì)** — 回避 (音が 死 *sǐ* に類似); 8 (bā) = 幸運 (發 *fā* = 富); 6 (liù) = スムーズ (流 *liú*)
- **電話番号/ナンバープレート**: 8 は優先、4 は回避
- **紅包 (hongbao)**: 偶数 (4を除く); 666, 888, 999 幸運

### 🇪🇸 スペイン
- **Billions**: *billón* = 10¹² (long scale) vs 米国 *billion* = 10⁹ — 金融翻訳トラップ
- **小数 separators**: コンマ (1,5 = 1.5); 千 separator: ドット or スペース (1.000 or 1 000)

### 🇬🇧 英語
- **And**: "one hundred **and** one" (UK) vs "one hundred one" (US)
- **大数**: 短スケール (million=10⁶, billion=10⁹, trillion=10¹²)

---

## 学習者向け実践ガイド

| 学習言語 | 最初にマスター | 理由 |
|-----------------|--------------|-------------|
| **Japanese** | *hon, mai, hiki, kai, fun, sai* + 1-10 不規則形 | 日常のカウントの 80% をカバー |
| **Korean** | 固有 1-10 + *gae, myeong, mari, jang, beon, si, sal* | 固有数字 + トップ 7 助数詞 = 生存 |
| **Chinese** | *ge, wei, zhang, ben, tiao, liang, bei, ci* + 两 vs 二 rule | *ge* 万能フォールバック; 两 は助数詞前必須 |
| **Spanish** | 基数 1-100 + *millón/millones* agreement (*un millón DE*) | *Millón* に *de* 必要; *cien* vs *ciento* |
| **English** | 序数接尾辞 (-st, -nd, -rd, -th) + "a/an" before numbers | "a hundred" vs "one hundred" |

---

## クロスランゲージ練習シナリオ

### シナリオ: ビールを 3 本注文
- EN: "Three beers, please."
- ES: "Tres cervezas, por favor."
- JP: "ビールを三本ください。" (*biiru o san-bon kudasai*)
- KR: "맥주 세 병 주세요." (*maekju se byeong juseyo*)
- CH: "来三瓶啤酒。" (*lái sān píng píjiǔ*)

### シナリオ: 「私は弟が 2 人います」
- EN: "I have two younger brothers."
- ES: "Tengo dos hermanos menores."
- JP: "弟が二人います。" (*otouto ga futari imasu*) — *futari* (2 人)
- KR: "남동생이 둘 있어요." (*namdongsaeng-i dul isseoyo*) — 固有 *dul*
- CH: "我有两个弟弟。" (*wǒ yǒu liǎng gè dìdi*) — *liǎng* + *ge*

### シナリオ: 「日本に行くのは 5 回目です」
- EN: "This is my fifth time in Japan."
- ES: "Es la quinta vez que voy a Japón."
- JP: "日本に来るのは五回目です。" (*nihon ni kuru no wa go-kaime desu*)
- KR: "일본에 온 게 다섯 번째예요." (*ilbon-e on ge daseot beonjjae-yeyo*)
- CH: "这是我第五次来日本。" (*zhè shì wǒ dì wǔ cì lái Rìběn*)

---

## 🇯🇵 日本語学習者ノート (Japanese Learner Notes)

> 本セクションは日本語学習者向けの追加学習ガイドです。

### 日本語話者が他4言語の数字・助数詞を学ぶ際の一般的な落とし穴

1. **中国語「两」vs「二」の区別**:
   - 日本語は「二」一形式 → 中国語は *二* (èr) vs *两* (liǎng) を助数詞前で必須。
   - **落とし穴**: 日本語話者が「两个苹果」(liǎng gè píngguǒ) を「二个苹果」と書く → ネイティブには不自然。
   - **練習法**: 「两」使用ルール (助数詞前、年齢、量、非公式) を意識的に練習。

2. **韓国語固有数字 vs Sino 数字**:
   - 日本語は数字一形式 → 韓国語は固有 (1-99) vs Sino (100+) の 2 体系。
   - **落とし穴**: 日本語話者が「一つ」(一つ) と「일」(Sino 1) を場面別に使い分けできない。
   - **練習法**: 韓国語固有数字 (하나, 둘, 셋) は年齢・時間・助数詞前、Sino (일, 이, 삼) は数学・金額・日付、と機能別練習。

3. **韓国語年数の固有形**:
   - 日本語の年齢は「〜歳」(sai) → 韓国語「살」(sal, 固有) vs「세」(se, Sino) を使い分け。
   - **落とし穴**: 日本語話者が「10살」を「10歳」と翻訳 → 「열 살」と固有形で言うべき。
   - **練習法**: 韓国語年齢の固有形 (열 살, 스무 살, 서른 살) と Sino (열 세, 스무 세) を 5言語対応表で。

4. **4 と 9 の禁忌**:
   - 日本語の 4 (shi) と 9 (ku) は病院・ホテルで回避される → 中国語の 4 (sì) も同様に禁忌 (sounds like 死 sǐ)。
   - **落とし穴**: 日本語話者が中国のホテルで 4階 を希望 → 「4」が避けられて 3A 表記のことがある。
   - **練習法**: 中国語・日本語の 4 (死) 禁忌 + 8 (発 = prosperity) 幸運数字を覚える。

5. **韓国・日本語の数字「万」vs 英語「千」単位**:
   - 日本語は 1万 (いちまん) 単位 → 韓国語も「만」(man) → 中国語も「万」(wàn) → 英語は「thousand (1,000)」と「million (1,000,000)」。
   - **落とし穴**: 日本語話者が英語の「billion」を「10億」と翻訳 → 短尺度 (10⁹) なら正解だが、スペイン語の「billón」は 10¹²。
   - **練習法**: 短尺度 (EN) vs 長尺度 (ES) の billion 差を覚える。1万/10万/100万/1億 を 5言語換算表で。

### 関連日本語ウィキページ

- `[[greetings]]` — 時刻表現
- `[[travel-essentials]]` — 価格、日付、スケジュール
- `[[food-dining]]` — 食品助数詞
- `[[politeness-honorifics]]` — 敬語助数詞 (*bun, wei, mei, sama*)
- `[[time-calendar]]` — 時間、月の助数詞

### 学習ワークフロー推奨

1. **5言語数字対応表** (上記早見表) を暗記
2. **中国語「两」vs「二」** ルールを 5言語対応で
3. **韓国語固有/Sino 数字** の使い分け表
4. **助数詞 (counter)** 主要 10個を 5言語対応で
5. **1万 vs 1,000** 単位換算表を作成

---

## 関連ページ

- `[[greetings]]` — 時刻表現
- `[[travel-essentials]]` — 価格、日付、スケジュール
- `[[food-dining]]` — 食品助数詞
- `[[politeness-honorifics]]` — 敬語助数詞

## 出典

- 英語: `[English/vocabulary/basic-vocabulary]`
- スペイン語: `[Spanish/vocabulary/basic-vocabulary]`, `[Spanish/vocabulary/time-prepositions-vocabulary]`
- 日本語: `[Japanese/vocabulary/jp-counters]`, `[Japanese/vocabulary/kanji-n5]`, `[Japanese/sources/2026-07-13_Kanji_N5_100]`
- 韓国語: `[[index]]`, `[Korean/vocabulary/topik1-starter]`, `[Korean/sources/daily-life-basics]`
- 中国語: `[Chinese/vocabulary/numbers-zh]`, `[Chinese/vocabulary/measure-words-zh]`, `[Chinese/sources/pinyin-basics-zh]`

---

**原文 (英語)**: [[numbers-counters]] | **関連ミラー**: [[numbers-counters.es|スペイン語]] · [[numbers-counters.ko|韓国語]] · [[numbers-counters.zh|中国語]] | **ポリシー**: ADR-0006
