# 家族の役割・親族 — 言語間比較 (日本語版)

> 原文: [[family-roles-comparison]] (English) | 作成日: 2026-08-19 | ADR-0006
> **5言語の家族役割・親族比較** — English · Spanish · Japanese · Korean · Chinese

---

## 早見表

### 直属の家族

| 関係 | English | Spanish | Japanese | Korean | Chinese |
|----------|---------|---------|----------|--------|---------|
| **父** | Father | Padre | 父 (chichi casual) / 父親 (chichioya formal) | 아버지 (abeoji) / 부 (bu, formal written) | 父亲 (fùqin) / 爸爸 (bàba) |
| **母** | Mother | Madre | 母 (haha casual) / 母親 (hahaoya formal) | 어머니 (eomeoni) / 모 (mo, formal written) | 母亲 (mǔqin) / 妈妈 (māma) |
| **息子** | Son | Hijo | 息子 (musuko) | 아들 (adeul) | 儿子 (érzi) |
| **娘** | Daughter | Hija | 娘 (musume) | 딸 (ttal) | 女儿 (nǚ'ér) |
| **兄** | Older brother | Hermano mayor | 兄 (ani) | 형 (hyeong, of male) / 오빠 (oppa, female speaker) | 哥哥 (gēge) |
| **弟** | Younger brother | Hermano menor | 弟 (otōto) | 남동생 (namdongsaeng) | 弟弟 (dìdi) |
| **姉** | Older sister | Hermana mayor | 姉 (ane) | 누나 (nuna, of male) / 언니 (eonni, female speaker) | 姐姐 (jiějie) |
| **妹** | Younger sister | Hermana menor | 妹 (imōto) | 여동생 (yeodongsaeng) | 妹妹 (mèimei) |

### 祖父母

| 関係 | English | Spanish | Japanese | Korean | Chinese |
|----------|---------|---------|----------|--------|---------|
| **祖父 (父方)** | Grandfather | Abuelo | 祖父 (sofu) | 할아버지 (harabeoji) | 爷爷 (yéye) |
| **祖母 (父方)** | Grandmother | Abuela | 祖母 (sobo) | 할머니 (halmeoni) | 奶奶 (nǎinai) |
| **祖父 (母方)** | Grandfather | Abuelo materno | 外祖父 (gaisofu) | 외할아버지 (oe-harabeoji) | 外公 (wàigōng) |
| **祖母 (母方)** | Grandmother | Abuela materna | 外祖母 (gaisobo) | 외할머니 (oe-halmeoni) | 外婆 (wàipó) |

### 拡大家族

| 関係 | English | Spanish | Japanese | Korean | Chinese |
|----------|---------|---------|----------|--------|---------|
| **叔父 (父方)** | Uncle | Tío | 伯父 (oji) / 叔父 (oji) | 삼촌 (samchon) | 伯父 / 叔叔 |
| **叔父 (母方)** | Uncle | Tío materno | 舅父 (oji) | 외삼촌 (oe-samchon) | 舅父 / 舅舅 |
| **叔母 (父方)** | Aunt | Tía | 伯母 (oba) / 叔母 (oba) | 이모 (imo, maternal) / 큰어머니 (keun-eomeoni) | 伯母 / 姑姑 |
| **いとこ (男性)** | Cousin | Primo | いとこ (itoko) | 사촌 (sachon) | 表兄弟 / 堂兄弟 |
| **甥** | Nephew | Sobrino | 甥 (oi) | 조카 (joka, nephew/niece) | 侄子 (zhízi) |
| **姪** | Niece | Sobrina | 姪 (mei) | 조카 (joka) | 侄女 (zhínǚ) |

### 義理の家族 (東アジア特有の複雑さ)

| 関係 | English | Spanish | Japanese | Korean | Chinese |
|----------|---------|---------|----------|--------|---------|
| **義父** | Father-in-law | Suegro | 舅 (shūto, husband of daughter) / 姑 (shūto, father of spouse — opposite!) | 시아버지 (siabeoji, husband's father) | 公公 (gōnggōng) |
| **義母** | Mother-in-law | Suegra | 姑 (shūtobo) / 舅 (shūtobo — varies) | 시어머니 (sieomeoni) | 婆婆 (pópo) |
| **義兄 (姉妹の夫)** | Brother-in-law | Cuñado | 義兄 (gikei) / 義弟 (gitei) | 자형 (jahyeong, older sister's husband) / 매형 (maehyeong) | 姐夫 (jiěfu) |
| **義姉 (兄の妻)** | Sister-in-law | Cuñada | 義姉 (gishi) / 義妹 (gimai) | 형수 (hyeongsu, older brother's wife) | 嫂子 (sǎozi) |

### 配偶者・パートナー

| 用語 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **夫** | Husband | Esposo / Marido | 夫 (otto) / ご主人 (goshujin — polite) | 남편 (nampyeon) | 丈夫 (zhàngfu) |
| **妻** | Wife | Esposa / Mujer | 妻 (tsuma) / 奥さん (okusan — polite) | 아내 (anae) | 妻子 (qīzi) |
| **彼氏/彼女** | Boyfriend/Girlfriend | Novio / Novia | 彼氏 (kareshi) / 彼女 (kanojo) | 남자친구 / 여자친구 | 男朋友 / 女朋友 |
| **婚約者** | Fiancé / Fiancée | Novio / Novia (compromise) | 婚約者 (kon'yakusha) | 약혼자 (yakhonja) | 未婚夫 / 未婚妻 |

### 文化的概念

| 概念 | English | Spanish | Japanese | Korean | Chinese |
|---------|---------|---------|----------|--------|---------|
| **親族の複雑さ** | シンプル (uncle = uncle) | 中 (tío/tía) | 高 (舅/姑 区別) | 最高 (시/외 家族 分離) | 高 (舅父/姑父 区別) |
| **年功序列** | あまり強調されない | Tío mayor vs menor | 非常に重要 (兄/弟, 姉/妹) | 重要 (형/동생, 누나/동생) | 重要 (哥哥/弟弟) |
| **敬語家族呼称** | カジュアル | カジュアル | 多数 (お父さん/お母さん) | 多数 (아버지/어머니) | カジュアル (爸爸/妈妈) |
| **家族レジスタ** | 限定的 | Tío vs tía | 広範 | 最も広範 | 中程度 |

---

## 各言語詳細

### 🇬🇧 英語 (English)
- **主要用語**: "Relative" (general); "Immediate family" vs "Extended family"
- **パターン**: シンプルな呼びかけ; 家族間でファーストネームが一般的に使用される
- **出典**: `[[family-vocabulary]]`

### 🇪🇸 スペイン語 (Spanish)
- **主要用語**: "Familia" (family), "Pariente" (relative), "Primo" (cousin)
- **パターン**: 性一致: tío/tía, primo/prima; "Sobrino" vs "sobrino" by gender
- **出典**: `[[family-vocabulary]]`

### 🇯🇵 日本語 (Japanese)
- **主要用語**: 家族 (kazoku = family), 親戚 (shinseki = relatives); 義理 (giri = in-law)
- **パターン**: 同じ関係の複数の語 (兄/兄さん); 厳格な年功序列マーキング (兄/弟, 姉/妹)
- **出典**: `[[family-vocabulary]]`

### 🇰🇷 韓国語 (Korean)
- **主要用語**: 가족 (gajok), 친척 (chincheok); 시 (妻の親戚) vs 외 (husband's relatives)
- **パターン**: 話者の性が兄弟姉妹用語に関係 (형/오빠); 厳格な年功序列
- **出典**: `[[family-vocabulary]]`

### 🇨🇳 中国語 (Chinese)
- **主要用語**: 家庭 (jiātíng = family), 亲戚 (qīnqi = relatives); 长辈 (zhǎngbèi = elder generation)
- **パターン**: 舅/姑 区別 (maternal vs paternal in-laws); 地域変種
- **出典**: 中国語には family テーマ未投入

---

## 主要な対比 (総合)

| 対比 | 学習者への示唆 |
|----------|---------|
| **親族の複雑さ** | KR > JP > ZH > ES > EN — 韓国語が最も分化した親族語彙 |
| **年功言語** | すべての東アジア言語が兄弟姉妹の年功をマーク; 西洋言語はマークしない |
| **義理の精度** | 東アジア言語は母方 vs 父方の義理を区別; 英語はマージ |
| **家族の価値** | 東アジア文化 (特に CN/KR) は階層を強調; 西洋文化はより平等主義的 |

---

## 学習者決定ガイド

> **言語別家族 reference**:
> - 父: 父 (chichi) / 아버지 (abeoji) / 爸爸 (bàba)
> - 母: 母 (haha) / 어머니 (eomeoni) / 妈妈 (māma)
> - 兄弟/姉妹: 兄/弟/姉/妹 (JP) / 형/동생/누나/여동생 (KR)
> - 義理: 시댁 (wife's family) vs 친정 (husband's family) — 韓国語特有

---

## 🇯🇵 日本語学習者ノート (Japanese Learner Notes)

> 本セクションは日本語学習者向けの追加学習ガイドです。

### 日本語話者が他の4言語の家族呼称を学ぶ際の一般的な落とし穴

1. **敬語家族の二層 (英語/中国語への適用失敗)**:
   - 日本語の父/母 (humble) とお父さん/お母さん (respectful) の二層 → 韓国語も類似だが、中国語は 「爸爸/父亲」 (casual/formal) の二層、英語は単一 ("father/dad")。
   - **練習法**: 言語別の敬語レベルを理解; 英語では "dad" / "father" / "sir" の使い分け; 中国語では 「爸爸」 (casual) / 「父亲」 (formal)。

2. **兄弟姉妹の性差 (韓国語)**:
   - 日本語の「お兄さん」「お姉さん」= 単一語彙 → 韓国語は話者の性別で 4 種類を使い分け。
   - **練習法**: 韓国語会話で自分の性別を先に確認; 適切な語を選択。

3. **義理家族の区別 (中国語)**:
   - 中国語は 舅父 (母方叔父) / 姑父 (父方叔父) を明確に区別 → 英語 "uncle" は単一。
   - **練習法**: 中国語の 6 種類の親戚呼称 (伯父/叔父/舅父 父方叔父 + 伯母/姑母/舅母 母方叔母) を系統的に覚える。

4. **「家」概念の文化差**:
   - 日本語の「家」= family, household, 屋号 → 韓国語은 "집" (家) / "가문" (家系) / "가족" (家族); 中国語 「家」/「家族」/「家庭」。
   - **練習法**: 言語別の "家" の概念的範囲を理解; 家族との会話で適切な単語を使用。

5. **敬称 (さん/様/님) の使用**:
   - 日本語の「さん」/韓国語の「님」/中国語の「先生/女士」 → 英語の "Mr./Ms." とは使用範囲が異なる。
   - **練習法**: 英語では家族に "Mr." をつけない; 中国語では家族にも 「先生」 を使用することがある。

### 関連日本語ウィキページ

- [Japanese/vocabulary/family-vocabulary] — 日本語家族語彙
- [Japanese/grammar/japanese-honorifics-family] — 家族の敬語
- [Japanese/culture/japanese-family-structure] — 日本の家族構造
- [Japanese/expressions/family-greetings] — 家族の挨拶
- [Japanese/culture/japanese-miai] — 日本の見合い

### 学習ワークフロー推奨

1. **基本家族呼称マトリクス** (5言語 × 10 関係)
2. **敬語ペア暗記** (日本語/韓国語/中国語の二層構造)
3. **自分の家系図を5言語で作成** (拡大家族まで)
4. **家族紹介ロールプレイ** (5言語で自己紹介)
5. **文化的家族行事の理解** (お盆、제사、清明節)

---

## 関連ページ

- `[[greetings]]` — 家族の挨拶
- `[[dating-romance]]` — ロマンチックな関係
- `[[politeness-honorifics]]` — 言語と家族の階層

## 出典

- `wiki/English/vocabulary/family-vocabulary.md`
- `wiki/Spanish/vocabulary/family-vocabulary.md`
- `wiki/Japanese/vocabulary/family-vocabulary.md`
- `wiki/Korean/vocabulary/family-vocabulary.md`
- Korean kinship terminology (anthropology references)

---

**原文 (英語)**: [[family-roles-comparison]] | **関連ミラー**: [[family-roles-comparison.es|スペイン語]] · [[family-roles-comparison.ko|韓国語]] · [[family-roles-comparison.zh|中国語]] | **ポリシー**: ADR-0006