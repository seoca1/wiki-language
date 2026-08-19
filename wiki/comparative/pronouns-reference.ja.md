# 代名詞参照 — 言語間比較 (日本語版)

> 原文: [[pronouns-reference]] (English) | 作成日: 2026-08-20 | ADR-0006
> **5言語の人称代名詞・指示代名詞の比較**

---

## 早見表

### 人称代名詞

| 人称 | English | Spanish | Japanese | Korean | Chinese |
|--------|---------|---------|----------|--------|---------|
| **1st sg** | I | yo | 私 / 僕 / 俺 / わし | 나 / 저 | 我 / 咱 |
| **2nd sg** | you | tú / usted / vos | あなた / 君 / お前 / 貴方 | 너 / 당신 / 선생님 | 你 / 您 |
| **3rd sg** | he/she/it | él / ella | 彼 / 彼女 / あの人 | 그 / 그녀 / 그분 | 他 / 她 / 它 |
| **1st pl** | we | nosotros/as | 私たち / 僕ら / 俺たち | 우리 / 저희 | 我们 / 咱们 |
| **2nd pl** | you (all) | vosotros/as / ustedes | あなたたち / 君たち | 너희 / 여러분 / 선생님들 | 你们 / 您们 |
| **3rd pl** | they | ellos / ellas | 彼ら / 彼女ら / あの人たち | 그들 / 그분들 | 他们 / 她们 / 它们 |

### 構造的差異

| 機能 | English | Spanish | Japanese | Korean | Chinese |
|---------|---------|---------|----------|--------|---------|
| **Obligatory?** | Yes (subject required) | No (pro-drop) | No (pro-drop, context-heavy) | No (pro-drop) | No (pro-drop) |
| **Gender in 3rd sg** | Yes (he/she/it) | Yes (él/ella) | No (kare/kanojo = he/she but rarely used) | No (geu/geunyeo = he/she but rare) | Yes (tā/tā/tā — same sound, diff char) |
| **Politeness encoded** | No (lexical only) | Yes (tú/usted/vos) | Yes (pronoun choice = register) | Yes (pronoun choice = register) | Yes (nǐ/nín) |
| **Inclusive/exclusive we** | No | No | No (wareware = formal we) | No (uri = inclusive default) | **Yes** (zánmen = inclusive, wǒmen = exclusive) |
| **Zero pronoun (pro-drop)** | No | **Yes** (standard) | **Yes** (standard) | **Yes** (standard) | **Yes** (standard) |

---

## 各言語詳細

### 🇬🇧 英語 (English)
- **Mandatory subjects**: すべての finite clause は overt subject が必要
- **Case system**: I/me, he/him, she/her, we/us, they/them
- **Generic "you"**: 単数複数同一
- **Singular "they"**: 不明/ノンバイナリー gender の標準
- **Reflexives**: myself, yourself, himself, herself, itself, ourselves, yourselves, themselves
- **Possessives**: my/mine, your/yours, his, her/hers, its, our/ours, their/theirs

### 🇪🇸 スペイン語 (Spanish)
- **Pro-drop**: 主語代名詞 regularly omitted (*hablo* = "I speak")
- **Tú/Usted/Vos**: 3 つの単数 informal/formal split (地域別)
- **Vosotros (スペインのみ)**: 複数 informal; *ustedes* = 複数 formal (スペイン) / 複数 両方 (ラ米)
- **Gender**: すべての代名詞が gendered (*nosotros/nosotras*, *ellos/ellas*)
- **Clitic pronouns**: me/te/se/nos/os/le/les/lo/la/los/las — 動詞前 or 不定詞/gerund に attach
- **Reflexive**: *se* (3rd person all numbers/genders)

### 🇯🇵 日本語 (Japanese)
- **Pronoun = register choice**: 中立 "I/you" なし — すべての選択が関係性を mark
- **First person**:
  - *watashi* (私) — 中立 polite (デフォルト)
  - *watakushi* (私) — フォーマル
  - *boku* (僕) — masculine casual
  - *ore* (俺) — masculine rough/intimate
  - *atashi* (あたし) — feminine casual
  - *uchi* (うち) — feminine Kansai
- **Second person**:
  - *anata* (あなた) — polite but distant (配偶者は使用)
  - *kimi* (君) — 上→下, male peer
  - *omae* (お前) — masculine rough/intimate
  - *kisama* (貴様) — 敵対的
  - *name-san* — **好まれる** (名前 + 敬称 を使用)
- **Third person**: *kare/kanojo* 存在するが翻訳っぽい; *ano hito* (that person) が好まれる
- **Plural**: *-tachi* (neutral), *-ra* (casual/masculine), *-gata* (honorific)
- **Zero pronoun**: 標準 — 文脈が指示対象を決定

### 🇰🇷 韓国語 (Korean)
- **Pronoun = register choice**: 日本語と同様、中立形なし
- **First person**:
  - *na* (나) — casual (해체)
  - *jeo* (저) — humble (해요체/합쇼체)
  - *uri* (우리) — "we" inclusive (デフォルト); *jeohui* (저희) — humble we
- **Second person**:
  - *neo* (너) — casual (親しい友、子供)
  - *dangsin* (당신) — **回避** (議論的 or 詩的/夫婦)
  - *name-ssi/nim* — **好まれる** (名前 + 敬称)
  - *seonsaengnim* (선생님) — 一般的 敬称
- **Third person**: *geu/geunyeo* (그/그녀) — 書き言葉/フォーマル; *geu bun* (그분) — honorific
- **Zero pronoun**: 標準 — 主語/目的語 routinely dropped
- **Reflexive**: *jagi* (자기) — self; *jagijasin* (자신) — oneself

### 🇨🇳 中国語 (Chinese)
- **Pro-drop**: 主語/目的語 freely omitted
- **Inclusive/Exclusive we**:
  - *zánmen* (咱们) — inclusive (you + me + others)
  - *wǒmen* (我们) — exclusive (me + others, not you)
- **Politeness**: *nǐ* (你) vs *nín* (您) — 2nd sg 尊敬
- **Plural**: *-men* (们) 接尾辞 — *wǒmen, nǐmen, tāmen*
- **Gender in writing only**: 他/她/它 すべて *tā* 発音
- **Demonstratives as pronouns**: *zhè* (这), *nà* (那) — this/that person
- **Reflexive**: *zìjǐ* (自己) — self

---

## 指示代名詞

| 距離 | English | Spanish | Japanese | Korean | Chinese |
|----------|---------|---------|----------|--------|---------|
| **Proximal (this)** | this | este/esta/esto | これ (kore) | 이거 / 이것 | 这 / 这个 |
| **Medial (that near you)** | that | ese/esa/eso | それ (sore) | 그거 / 그것 | 那 / 那个 |
| **Distal (that over there)** | that over there | aquel/aquella/aquello | あれ (are) | 저거 / 저것 | 那个 (far) |
| **Place (here/there)** | here/there | aquí/allí/allá | ここ/そこ/あそこ | 여기/거기/저기 | 这里/那里/那儿 |

### 使用上の注意
- **Spanish**: 3 距離 (*este/ese/aquel*) — *aquel* = 話者と聞き手の両方から遠い
- **Japanese**: *kore/sore/are* = 物体; *koko/soko/asoko* = 場所; *kochira/sochira/achira* = 方向/人 (polite)
- **Korean**: *igeo/geugeo/jeogeo* (物体) vs *yeogi/geogi/jeogi* (場所); *ireon/geureon/jeoreon* (種類)
- **Chinese**: *zhè/zhège* vs *nà/nàge* — 2 距離 話し言葉; *zhèr/nàr* (北) vs *zhèlǐ/nàlǐ* (南) for 場所

---

## 疑問代名詞

| 質問 | English | Spanish | Japanese | Korean | Chinese |
|----------|---------|---------|----------|--------|---------|
| **Who** | who | quién | 誰 (だれ) | 누구 (nugu) | 谁 (shéi/shuí) |
| **What** | what | qué | 何 (なに/なん) | 무엇 / 뭐 (mueot/mwo) | 什么 (shénme) |
| **Which** | which | cuál | どれ (dore) | 어느 (eoneu) | 哪个 (nǎge) |
| **Where** | where | dónde | どこ (doko) | 어디 (eodi) | 哪里 / 哪儿 (nǎlǐ/nǎr) |
| **When** | when | cuándo | いつ (itsu) | 언제 (eonje) | 什么时候 (shénme shíhou) |
| **Why** | why | por qué | なぜ (naze) / どうして (doushite) | 왜 (wae) | 为什么 (wèishénme) |
| **How** | how | cómo | どう (dou) | 어떻게 (eotteoke) | 怎么 (zěnme) |
| **Whose** | whose | de quién | 誰の (dare no) | 누구 것 (nugu geot) | 谁的 (shéi de) |

---

## 不定代名詞

| 意味 | English | Spanish | Japanese | Korean | Chinese |
|---------|---------|---------|----------|--------|---------|
| **Everyone** | everyone | todos | 皆 (みな) / みんな | 모두 / 전부 | 大家 / 人人 |
| **Someone** | someone | alguien | 誰か (だれか) | 누군가 (nugunga) | 某人 / 谁 (shéi) |
| **No one** | no one | nadie | 誰も...ない (dare mo...nai) | 아무도...않다 (amudo...anta) | 没人 / 谁都不 |
| **Everything** | everything | todo | 全て (すべて) / みんな | 모든 것 / 전부 | 一切 / 全部 |
| **Something** | something | algo | 何か (なにか) | 무언가 / 뭔가 (mueotnga/mwonga) | 某事 / 什么 |
| **Nothing** | nothing | nada | 何も...ない (nani mo...nai) | 아무것도...않다 (amugeotdo...anta) | 没事 / 什么都没有 |
| **Anyone** | anyone | cualquiera | 誰でも (だれでも) | 아무나 (amuna) | 谁都可以 |

---

## 再帰・相互代名詞

| タイプ | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **Reflexive** | myself/yourself... | me/te/se/nos/os/se | 自分 (じぶん) | 자기 (jagi) / 자신 (jasin) | 自己 (zìjǐ) |
| **Reciprocal** | each other | el uno al otro / mutuamente | お互い (おたがい) | 서로 (seoro) | 彼此 / 互相 (bǐcǐ/hùxiāng) |

---

## ゼロ代名詞 / Pro-Drop 行動

| 言語 | 主語 drop | 目的語 drop | 所有格 drop | ノート |
|----------|--------------|-------------|----------------|-------|
| **English** | ❌ | ❌ | ❌ | Mandatory subjects |
| **Spanish** | ✅ (standard) | ❌ (clitics required) | ❌ | *Hablo español* = "I speak Spanish" |
| **Japanese** | ✅ (standard) | ✅ (standard) | ✅ (standard) | Context-recovery mandatory |
| **Korean** | ✅ (standard) | ✅ (standard) | ✅ (standard) | Topic/comment structure aids recovery |
| **Chinese** | ✅ (standard) | ✅ (standard) | ✅ (standard) | Topic-prominent; null anaphora pervasive |

### Recovery 戦略
- **Spanish**: 動詞形態論が person/number を encode (*hablo/hablas/habla/hablamos/habláis/hablan*)
- **Japanese/Korean**: Topic marker (*wa/は* vs *ga/が* vs *eun/은* vs *i/이*) + 敬語 + 文脈
- **Chinese**: Topic-comment structure + aspect markers + lexical context

---

## 言語間干渉マップ

| 学習者 L1 → 目標 L2 | 典型エラー | 理由 |
|------------------------|---------------|-----|
| **EN → ES/JP/KR/CH** | Overt pronouns everywhere ("I think that he...") | L1 主語要求; 目標 zero 許可 |
| **ES → JP/KR** | Using *tú* equivalent (*anata/neo*) with strangers | *Tú* = 同輩デフォルト; *anata/neo* = 親密 |
| **JP/KR → CH** | Overusing *nín* (您) like *anata/nan* | *Nín* = 特定尊敬; 中国語は 敬称 中心 |
| **CH → ES** | Using *tú* universally (no *nín* equivalent) | 中国語 *nǐ* デフォルト; スペイン語は *usted* 選択必須 |
| **EN → JP/KR** | Translating "you" → *anata/neo* | JP/KR に中立 "you" なし |

---

## クイックリファレンスカード

| 必要性 | EN | ES | JP | KR | CH |
|----------------|----|----|-----|----|----|
| **"I (polite)"** | I | yo | わたし (watashi) | 저 (jeo) | 我 (wǒ) |
| **"I (casual male)"** | I | yo | ぼく (boku) / おれ (ore) | 나 (na) | 我 (wǒ) |
| **"You (polite)"** | you | usted | (name)-san | (name)-ssi/nim | 您 (nín) |
| **"You (casual)"** | you | tú / vos | (name)-kun/chan | 너 (neo) | 你 (nǐ) |
| **"We (inclusive)"** | we | nosotros | わたしたち (watashitachi) | 우리 (uri) | 咱们 (zánmen) |
| **"We (exclusive)"** | we | nosotros | わたしたち (watashitachi) | 우리 (uri) / 저희 (jeohui) | 我们 (wǒmen) |
| **"He/She (respectful)"** | he/she | él/ella | あのかた (ano kata) | 그분 (geu bun) | 他/她 (tā) |
| **"This one"** | this one | este | これ (kore) | 이거 (igeo) | 这个 (zhège) |
| **"Who?"** | who? | quién? | だれ (dare)? | 누구 (nugu)? | 谁 (shéi)? |
| **"Nobody"** | nobody | nadie | だれもいない (dare mo inai) | 아무도 없다 (amudo eopda) | 没人 (méi rén) |

---

## 🇯🇵 日本語学習者ノート (Japanese Learner Notes)

> 本セクションは日本語学習者向けの追加学習ガイドです。

### 日本語話者が他4言語の代名詞を学ぶ際の一般的な落とし穴

1. **ゼロ代名詞 (pro-drop) の頻度**:
   - 日本語は pro-drop 標準 → スペイン語/韓国語/中国語も同様だが、英語は主語必須。
   - **落とし穴**: 日本語話者が英語 "I think that he..." のように overt pronoun を使いすぎる → ネイティブは stiff と感じる。
   - **練習法**: 英語 "Think he'll come?" (主語省略) や "It's raining" (it 仮主語) のような省略構文に慣れる。

2. **代名詞の敬語一体性**:
   - 日本語は 代名詞 + 敬語 (例: 「田中様」(name + 様)) → 中国語は 「姓 + 敬称 (先生/女士)」、韓国語は 「名前 + 님/씨」、英語は「Mr./Ms./Dr. + 姓」。
   - **落とし穴**: 日本語話者が中国語「姓 + 先生」を使用 → 教師以外に使用すると違和感 (「老师」の方が汎用的)。
   - **練習法**: 中国語の敬称 (老师/先生/女士/经理/总监) の使用場面を 5言語対応表で。

3. **包括的「我們」vs 排他的「我們」**:
   - 日本語は「私たち」1形式 → 中国語は包括的「咱们」vs 排他的「我们」を区別。
   - **落とし穴**: 日本語話者が中国語「咱们」 (zánmen) を使い慣れていない。
   - **練習法**: 中国語「咱们」(you + me) vs 「我们」(me + others) を意識的に練習。

4. **英語 it / they / "one" の多用**:
   - 日本語は「それ」「彼」を行為者 with 状況依存 → 英語は gender 明確な he/she/it + 状況依存 + they (nonbinary)。
   - **落とし穴**: 日本語話者が英語 "they" (singular) を使用しない → ジェンダー中立表現の幅が狭い。
   - **練習法**: 英語の singular "they" (someone who has no gender) 表現を 5言語対応で。

5. **韓国語 2 人称回避**:
   - 日本語は代名詞回避 (「名前 + san」) → 韓国語も同様 (「이름 + 님」) → 当該回避文化は 東アジア共通。
   - **落とし穴**: 韓国語 "당신" (dangsin) を「あなた」と思って使用 → ネイティブは「夫婦」または「敵対的」使用と誤解。
   - **練習法**: 韓国語の "당신" (dangsin) 使用場面 (夫婦/詩/敵対) を 5言語対応表で。

### 関連日本語ウィキページ

- `[[politeness-honorifics]]` — 代名詞選択 = politeness
- `[[greetings]]` — 挨拶の呼び方
- `[[business-email]]` — 書き言葉の代名詞規約
- `[[negation]]` — 否定代名詞 (*nadie, dare mo...nai, amudo...*)
- `[[numbers-counters]]` — 助数詞と代名詞の組み合わせ

### 学習ワークフロー推奨

1. **5言語人称代名詞対応表** (上記早見表) を暗記
2. **英語 pro-drop 回避** (ゼロ代名詞) を意識的に練習
3. **中国語「咱们」vs「我们」** 区別を覚える
4. **韓国語 2 人称回避** (당신) の特殊用法を覚える
5. **代名詞敬語体系** (日本語/韓国語/中国語) を 5言語対応で

---

## 関連ページ

- `[[politeness-honorifics]]` — 代名詞選択 = politeness
- `[[greetings]]` — 挨拶の呼び方
- `[[business-email]]` — 書き言葉の代名詞規約
- `[[negation]]` — 否定代名詞

## 出典

- 英語: `[English/vocabulary/basic-vocabulary]`
- スペイン語: `[Spanish/vocabulary/basic-vocabulary]`, `[Spanish/culture/espana-vs-latinoamerica-registro]`
- 日本語: `[[index]]`, `[Japanese/culture/japanese-dating-culture]`
- 韓国語: `[[index]]`, `[Korean/culture/korean-dating-culture]`
- 中国語: `[Chinese/sources/greetings-zh]`, `[Chinese/vocabulary/family-zh]`

---

**原文 (英語)**: [[pronouns-reference]] | **関連ミラー**: [[pronouns-reference.es|スペイン語]] · [[pronouns-reference.ko|韓国語]] · [[pronouns-reference.zh|中国語]] | **ポリシー**: ADR-0006
