# 敬語と敬意表現 — 言語間比較 (日本語版)

> 原文: [[politeness-honorifics]] (English) | 作成日: 2026-08-20 | ADR-0006
> **5言語の敬語・敬称体系の比較**

---

## 早見表

### クイックリファレンステーブル

| 機能 | English | Spanish | Japanese | Korean | Chinese |
|---------|---------|---------|----------|--------|---------|
| **Grammatical encoding** | 語彙のみ (語彙選択) | 代名詞 (tú/usted) + 動詞形態論 | 動詞形態論 (敬語) + 語彙 | 動詞語尾 (speech levels) + 敬語名詞/動詞 | 語彙選択 + 敬称 + 您 (nín) |
| **レベルの数** | 2–3 (formal/neutral/informal) | 2–3 (tú/usted/vosotros) | 3–4 (casual/polite/honorific/humble) | 4–6 (해체/해요체/합쇼체/하소서체 + mixed) | 2–3 (neutral/您/respectful titles) |
| **代名詞区別** | you (普遍的) | tú / usted / vosotros / ustedes | あなた / 君 / お前 / 貴方 (often omitted) | 너 / 당신 / 당신들 / 선생님/님 (avoided) | 你 / 您 / 诸位 / 先生/女士 |
| **動詞形態論変化** | なし | あり (2nd/3rd person) | あり (extensive) | あり (extensive) | 最小限 (some suppletive forms) |
| **敬語語彙** | 限定的 (sir/ma'am, titles) | Don/Doña, usted forms | 尊敬語 / 謙譲語 / 丁寧語 | 존댓말 / 높임말 (special verbs/nouns) | 尊称, 敬语 (您, 贵姓, etc.) |
| **相対的地位が問題** | コンテキスト依存 | あり (age, familiarity) | 中心 (uchi/soto) | 中心 (age, hierarchy) | 中心 (age, hierarchy, guanxi) |
| **In-group vs out-group** | 弱い | 中程度 (usted default out-group) | 基礎 (uchi/soto) | 基礎 (내사람/남) | 基礎 (自己人/外人) |

---

## 各言語詳細

### 🇬🇧 英語 (English)
- **Key terms**: formal vs informal register, "please/thank you," titles (Mr/Ms/Dr/Prof), hedging (could/would/might)
- **Patterns**: 文法敬語なし。Politeness = 語彙選択 + 構文的距離 (過去形で現在の依頼: "I was wondering if...") + 助動詞 + 間接性
- **Register notes**:
  - Formal: "Would you be so kind as to...", "I would appreciate it if..."
  - Neutral: "Could you please...", "Please..."
  - Informal: "Can you...", "Hey, ..."
- **Source**: `[English/vocabulary/basic-vocabulary]`, `[English/culture/english-dating-culture]`

### 🇪🇸 スペイン語 (Spanish)
- **Key terms**: tú / usted / vosotros / ustedes, *don/doña*, *usted* verb forms (3rd person), *tuteo* vs *ustedeo*
- **Patterns**:
  - **Tú**: 友人、家族、子供、同輩 (スペインの若者のデフォルト)
  - **Usted**: 見知らぬ人、目上、フォーマル場面、権威者 (ラ米のデフォルト)
  - **Vosotros** (スペインのみ): 複数カジュアル
  - **Ustedes**: 複数フォーマル (スペイン) / 複数両方 (ラ米)
- **Regional variations**:
  - **スペイン**: tú/usted distinction strong; vosotros used
  - **メキシコ/コロンビア/ペルー**: usted default even among young people in some contexts
  - **アルゼンチン/ウルグアイ/パラグアイ**: *vos* replaces *tú* (voseo) — distinct conjugation
  - **Caribbean**: *usted* more frequent, *tú* reserved for close intimacy
- **Source**: `[Spanish/vocabulary/polite-expressions-vocabulary]`, `[Spanish/culture/espana-vs-latinoamerica-registro]`

### 🇯🇵 日本語 (Japanese)
- **Key terms**:
  - **丁寧語 (teineigo)**: です/ます — デフォルトの polite
  - **尊敬語 (sonkeigo)**: 敬語 — 相手を elevate (いらっしゃる, 召し上がる, ご存知)
  - **謙譲語 (kenjougo)**: 謙譲語 — 自分を降格 (参る, いただく, 拝見する)
  - **美化語 (bikago)**: お/ご prefixes (お茶, ご飯)
- **Patterns**: 動詞活用が register で完全変化。*Uchi* (in-group) vs *soto* (out-group) でどの敬語を使うか決定。見知らぬ人とのデフォルト = ていねい語。ビジネス = 尊敬語/謙譲語の混合。
- **Keigo / politeness level**:
  - Casual (タメ口): 行く, 食べる, 知ってる — 親しい友、家族、年下
  - Polite (丁寧語): 行きます, 食べます, 知っています — 見知らぬ人、同僚、デフォルト
  - Honorific (尊敬語): いらっしゃいます, 召し上がります, ご存知です — 顧客、上司、目上
  - Humble (謙譲語): 参ります, いただきます, 拝見します — 上司への自分語り
- **Source**: `[Japanese/vocabulary/business-vocabulary]`, `[Japanese/culture/japanese-dating-culture]`

### 🇰🇷 韓国語 (Korean)
- **Key terms**:
  - **해체 (haeche)**: 平叙/フォーマル書き言葉 — 親しい友、子供、独り言
  - **해요체 (haeyoche)**: 丁寧インフォーマル — 日常生活、同僚、知り合い (口語のデフォルト)
  - **합쇼체 (hapsyoche)**: フォーマル polite — プレゼン、放送、軍隊、顧客
  - **하소서체 (hasoseoche)**: 極めてフォーマル — 歴史的、宗教、王室
  - **존댓말 (jondaetmal)**: polite levels の包括語
  - **반말 (banmal)**: casual (해체/해요체 混合)
- **Patterns**:
  - 動詞語尾変化: 가다 → 가/가요/갑니다/가시옵소서
  - 敬語名詞: 밥 → 진지, 집 → 댁, 이름 → 성함, 생일 → 생신
  - 敬語動詞: 먹다 → 잡수시다, 자다 → 주무시다, 계시다 (있다/계시다)
  - Subject honorific marker: ~(으)시 (가시다, 드시다)
- **Speech level selection**: 1 歳以上の年齢差 → 敬語期待。同年齢 → 交渉 (언제 반말 할까요?). 職場: タイトル + 님 (팀장님, 매니저님)
- **Source**: `[Korean/vocabulary/emotions-personality-vocabulary]`, `[Korean/culture/korean-dating-culture]`

### 🇨🇳 中国語 (Chinese)
- **Key terms**:
  - **您 (nín)**: 尊敬の "you" (vs 你 nǐ)
  - **尊称 (zūnchēng)**: 敬称 — 先生, 女士, 老师, 总经理, 姐/哥
  - **敬语 (jìngyǔ)**: 敬語語彙 — 贵姓, 请教, 拜访, 敬请, 承蒙
  - **谦辞 (qiāncí)**: 謙譲 — 拙作, 拙见, 献丑, 不敢当
- **Patterns**:
  - 動詞形態論変化 for politeness なし
  - Politeness = 語彙置換 + 敬称 + 終助詞 (请, 麻烦您, 劳驾)
  - **您 (nín)** used for elders, superiors, strangers in formal contexts
  - **Title + 姓**: 王先生, 李老师, 张总 — デフォルトの address in professional settings
  - **Guanxi (关系)** modulates register: closer relationship → drop 您, use first name / nickname
- **Register / honorifics**:
  - Neutral: 你, 叫什么名字?, 去
  - Respectful: 您, 贵姓?, 请去 / 麻烦您去
  - Formal written: 阁下, 尊驾, 惠顾, 光临 (business correspondence)
- **Source**: `[Chinese/vocabulary/body-zh]`, `[Chinese/sources/greetings-zh]`

---

## 主要な対比 (総合)

| 対比 | 学習者への示唆 |
|----------|--------------------------|
| **文法 vs 語彙** — JP/KR/ES は politeness を文法 encode; EN/CH は語彙 | JP/KR 学習者は動詞パラダイムを早期習得; EN/CH 学習者は基本文法 + polite 単語でコミュニケーション可 |
| **デフォルトの見知らぬ人 register** — ES: *usted* (ラ米) / *tú* (スペイン youth); JP: *desu/masu*; KR: *haeyoche*; CH: *nín* + title | 目標地域に基づきデフォルト選択: メキシコ → *usted*; 東京 → *desu/masu*; ソウル → *haeyoche*; 北京 → *nín* + title |
| **In-group/out-group (uchi/soto, 내사람/남)** — JP/KR で中心; EN で弱い; ES/CH で中程度 | JP/KR では間違った register 使用 = in-group で cold/distant; out-group で rude. グループ境界を最初に学習。 |
| **年齢 vs タイトル ベースの address** — KR/CH は title+님/先生 を要求; JP は -san/様; ES は Don/Doña + usted; EN は Mr/Ms | KR/CH では bare 名前 = 失礼。全役割のタイトルを暗記 (팀장님, 王老师, 部長様, Don Juan) |
| **Register の交渉** — KR 明示 ("우리 반말 해요"); JP 暗示 (敬語 drop); ES 明示 ("tuteame"); CH 暗示 (drop 您) | KR 学習者: "언제 반말 할까요?" スクリプトを練習。JP 学習者: 敬語 drop シグナルを観察。ES 学習者: "¿Puedo tutearte?" |

---

## 学習者向け決定ガイド

> "If your goal is X, prioritize Y in Language Z because..."

- **目標: 基礎生存 / 旅行** →
  - EN: "Please/Thank you/Excuse me" + 助動詞
  - ES: *usted* forms + *por favor/gracias* (全てで使える)
  - JP: *desu/masu* + *sumimasen/arigatou* (90% の相互作用をカバー)
  - KR: *haeyoche* (-요 語尾) + *juseyo/mianhamnida* (安全なデフォルト)
  - CH: *nín* + *qing/xiexie/duibuqi* + 敬称 (服务员, 师傅)

- **目標: ビジネス / 専門** →
  - EN: Hedging, 受動態, "I would appreciate," 敬称
  - ES: *ustedeo* + *usted* 動詞形式 + *Don/Doña* + フォーマル closings (*Atentamente, Cordialmente*)
  - JP: Full *keigo* (sonkeigo/kenjougo/bikago) + *keigo* メール template + *meishi* 交換 etiquette
  - KR: *hapsyoche* (-ㅂ니다) + 敬語名詞/動詞 + title+님 + お辞儀の深さ
  - CH: *nín* + 贵姓/请教/拜访 + 敬称 (总监, 经理, 老师) + 请/麻烦您

- **目標: 社交 / 友情 / デート** →
  - EN: ファーストネーム basis quickly, 句動詞, 俗語
  - ES: *tuteo* 交渉 (*¿Puedo tutearte?*) → 地域規範は変動
  - JP: *tameguchi* transition (通常 3 回目 / 飲みの後) — 先輩が提案するのを待つ
  - KR: *banmal* 交渉 (*우리 반말 해요*) — 通常 younger asks older after closeness established
  - CH: Drop *nín* → *nǐ*, use given name / nickname / 哥/姐 — follows *guanxi* deepening

- **目標: 学術 / フォーマル 書き言葉** →
  - EN: 受動態, 名詞化, hedging, citation style
  - ES: *ustedeo*, 非人称 *se*, フォーマル場面の subjunctive
  - JP: *dearu/da* (plain) for papers; *desu/masu* for presentations; *kanbun*  legacy forms
  - KR: *hapsyoche* + 敬語 + Sino-Korean 語彙 (한자어)
  - CH: 書き言葉 register (书面语) — 之/其/乃/乎, 4 文字 chengyu, 受動態 被/由

---

## 関連ページ

- `[[greetings]]` — 挨拶儀式 = politeness の encode
- `[[pronouns-reference]]` — 代名詞体系 = 敬語構造
- `[[business-email]]` — 書き言葉 register
- `[[dating-romance]]` — 親密さの register 交渉

## 出典

- 英語: `[English/vocabulary/basic-vocabulary]`, `[English/culture/english-dating-culture]`
- スペイン語: `[Spanish/vocabulary/polite-expressions-vocabulary]`, `[Spanish/culture/espana-vs-latinoamerica-registro]`, `[Spanish/sources/notes-in-spanish-listening-log]`
- 日本語: `[Japanese/vocabulary/business-vocabulary]`, `[Japanese/culture/japanese-dating-culture]`, `[Japanese/sources/business-email]`
- 韓国語: `[Korean/vocabulary/emotions-personality-vocabulary]`, `[Korean/culture/korean-dating-culture]`, `[Korean/sources/daily-life-basics]`
- 中国語: `[Chinese/vocabulary/body-zh]`, `[Chinese/sources/greetings-zh]`, `[Chinese/sources/daily-routine-zh]`

---

## 🇯🇵 日本語学習者ノート (Japanese Learner Notes)

> 本セクションは日本語学習者向けの追加学習ガイドです。

### 日本語話者が他4言語の敬語・敬称体系を学ぶ際の一般的な落とし穴

1. **コードスイッチング resistance**:
   - 日本語は敬語 3-4 階層 (casual/polite/honorific/humble) を動詞活用で encode → 韓国語も 3-4 階層 (해체/해요체/합쇼체/하소서체) を動詞語尾で。
   - **落とし穴**: 日本語話者が韓国語の上司に「먹어」(カジュアル) を使用 → 日本語では「食べます」を使うべき場面。
   - **練習法**: 韓国語の 합쇼체 (フォーマル) と 해요체 (ポライト) を 5言語対応表で各 10フレーズ練習。

2. **代名詞 vs 敬称**:
   - 日本語は代名詞を避けて「名前 + san/kun/chan」を使用 → 韓国語も「名前 + 님/씨」 → 中国語は「姓 + 敬称 (先生/女士/老师/etc.)」 → スペイン語は usted + 動詞活用。
   - **落とし穴**: 日本語話者が中国語で「你」(nǐ) を見知らぬ人に使用 → 失礼 (「您」nín を使うべき)。
   - **練習法**: 中国語の「您」使用ルール (年配者、上司、フォーマル場面) を 5言語対応表で。

3. **敬語の有無が文法化される言語**:
   - 日本語は動詞活用で文法化 (行く/行きます/いらっしゃる/参る) → 韓国語も同様 (먹다/먹어요/먹습니다/잡수시다)。
   - **落とし穴**: 日本語話者が中国語に「动词 don conjugate」と過信 → 単語選択 (您/请/敬语/劳驾) でカバーする必要。
   - **練習法**: 中国語の politeness = 語彙 (敬称、終助詞、副詞) と覚える。

4. **年齢階層の扱い**:
   - 日本語は「先輩」「後輩」関係 → 韓国語も「선배」「후배」関係 → 英語・スペイン語・中国語は年齢階層が薄い。
   - **落とし穴**: 日本語話者が英語の学校で「先輩システム」を期待 → アメリカ文化にない。
   - **練習法**: 英語/スペイン語圏では年齢階層を意識せず、ファーストネーム文化を覚える。

5. **ビジネス敬語の翻訳**:
   - 日本語の「貴社のご繁栄をお祈り申し上げます」を英語に翻訳 → "Wishing your company prosperity" で完結するが、スペイン語・ラ米・韓国語・中国語のビジネス敬語は異なる構造。
   - **落とし穴**: 日本語の hard-keigo を他言語に直訳 → 過度に stiff。
   - **練習法**: 5言語のビジネスメール closing (EN: Sincerely yours, ES: Atentamente, JP: 敬具, KR: 〜敬上, CH: 此致敬礼) の対応表。

### 関連日本語ウィキページ

- `[[greetings]]` — 5言語の挨拶
- `[[pronouns-reference]]` — 代名詞と敬語
- `[[business-email]]` — メール敬語
- `[[dating-romance]]` — 親密さの register
- `[[untranslatable-concepts]]` — 翻訳不能な概念

### 学習ワークフロー推奨

1. **5言語敬語階層対応表** (上記早見表) を暗記
2. **日本語敬語 3-4 階層** + 韓国語 4-6 階層をマスター
3. **中国語「您」/「你」** 使い分けを練習
4. **スペイン語 usted/tú** の地域別デフォルトを覚える
5. **ビジネスメール closing** を 5言語対応表で

---

**原文 (英語)**: [[politeness-honorifics]] | **関連ミラー**: [[politeness-honorifics.es|スペイン語]] · [[politeness-honorifics.ko|韓国語]] · [[politeness-honorifics.zh|中国語]] | **ポリシー**: ADR-0006
