# 否定 — 言語間比較 (日本語版)

> 原文: [[negation]] (English) | 作成日: 2026-08-20 | ADR-0006
> **5言語の否定文 (negation) システムの比較**

---

## 早見表

### 否定アーキテクチャ概観

| 機能 | English | Spanish | Japanese | Korean | Chinese |
|---------|---------|---------|----------|--------|---------|
| **文否定** | 助動詞 + not | *no* + 動詞 | 動詞語尾 *-nai* / *-masen* | 動詞語尾 *-ji anta* / *-ji anhseumnida* | *bù* (不) / *méi* (没) + 動詞 |
| **構成要素否定** | *not* + 構成要素 | *no* + 構成要素 | *wa* + *nai* / *dewa nai* | *an(i)* + 動詞 / *mot* + 動詞 | *bù* + 形容詞/動詞; *wú* (无) + 名詞 |
| **二重否定** | **なし** (二重否定 = 肯定) | **あり** (二重否定 = 否定) | **なし** (単一否定) | **なし** (単一否定) | **なし** (単一否定) |
| **否定極性項目** | any, ever, anymore | *nadie, nada, nunca* | *dare mo...nai, nani mo...nai* | *amudo...an(i), amugeotdo...an(i)* | *shéi dōu...bù, shénme dōu...bù* |

---

## 文否定

### 🇬🇧 英語 (English)
- **Structure**: 助動詞 + *not* (*n't*)
- **Present**: I **do not** / **don't** know. She **does not** / **doesn't** go.
- **Past**: I **did not** / **didn't** go.
- **Future**: I **will not** / **won't** go.
- **Modal**: I **cannot** / **can't** / **could not** / **couldn't** go.
- **Be**: I **am not** / **'m not** / **is not** / **isn't** / **are not** / **aren't** ready.
- **Have (aux)**: I **have not** / **haven't** seen it.
- **Have (main, BrE)**: I **haven't** a car. (AmE: I **don't have** a car.)

### 🇪🇸 スペイン語 (Spanish)
- **Structure**: *no* + 動詞 (動詞前)
- **Present**: *No sé.* / *No voy.*
- **Past**: *No supe.* / *No fui.* / *No he ido.* (完了)
- **Future**: *No iré.* / *No voy a ir.*
- **接続法トリガ**: *No creo que venga.* (接続), *No es verdad que venga.*
- **二重否定**: *No vi **nada**.* (私は何も見えなかった。) *Nadie **no** vino.* → *Nadie vino.* (誰も来なかった。)

### 🇯🇵 日本語 (Japanese)
- **Plain negative**: 動詞語幹 + *nai* (ない) — *tabenai* (食べない = don't eat)
- **Polite negative**: 動詞語幹 + *masen* (ません) — *tabemasen* (食べません)
- **Past negative**: *tabenakatta* (食べなかった) / *tabemasen deshita* (食べませんでした)
- **形容詞**:
  - *i-adj*: *takai* → *takakunai* (高くない) / *takaku arimasen*
  - *na-adj/noun*: *kirei* → *kirei dewa nai* (綺麗ではない) / *kirei dewa arimasen*
- **存在**: *aru* → *nai* (ない) / *arimasen*; *iru* → *inai* (いない) / *imasen*
- **禁止**: *taberu na* (食べるな) — plain; *tabenaide kudasai* (食べないでください) — 丁寧依頼

### 🇰🇷 韓国語 (Korean)
- **Short form (plain)**: 動詞語幹 + *ji anta* (지 않다) — *meokji anta* (먹지 않다)
- **Long form (polite)**: 動詞語幹 + *ji anhseumnida* (지 않습니다) — *meokji anhseumnida*
- **Past**: *meokji anatda* (먹지 않았다) / *meokji anhasseumnida*
- **形容詞**: 同じパターン — *yeppeuji anta* (예쁘지 않다)
- **存在**: *itda* (있다) → *eopda* (없다) — 別個の否定動詞!
- **禁止**: *meokji maseyo* (먹지 마세요) / *meokjima* (먹지 마)
- **Cannot (能力)**: *mot* (못) + 動詞 — *mot meokda* (못 먹다) — 別個に *an(i)*

### 🇨🇳 中国語 (Chinese)
- **Standard negation**: *bù* (不) + 動詞/形容詞 — *bù chī* (不吃), *bù hǎo* (不好)
- **完了/経験 negation**: *méi* (没) / *méiyǒu* (没有) + 動詞 — *méi chī* (没吃), *méiyǒu qù* (没有去)
- **Future/意志 negation**: *bù* — *bù qù* (不去 = 行かない)
- **命令 negation**: *bié* (别) + 動詞 — *bié chī* (别吃 = 食べるな)
- **形容詞**: *bù* — *bù dà* (不大), *bù cōngming* (不聪明)
- **存在**: *méiyǒu* (没有) — *méiyǒu qián* (没有钱 = お金がない)

---

## 構成要素否定

### 🇬🇧 英語 (English)
- *Not* + NP: **Not** John but Mary came.
- *Not* + PP: I saw him **not** in Paris but in London.
- *Not* + Adv: He drove **not** carefully but recklessly.
- *No* + N: **No** student passed. (限定詞)

### 🇪🇸 スペイン語 (Spanish)
- *No* + 構成要素: *No Juan, sino María vino.*
- *Ningún* + N (否定限定詞): *Ningún estudiante aprobó.*
- *Ni*... *ni* (neither...nor): *Ni Juan ni María vinieron.*

### 🇯🇵 日本語 (Japanese)
- *Wa* + 否定: *Jon wa konakatta.* (John は来なかった — 対比)
- *De wa nai* (コピュラ否定): *Jon de wa nai.* (John ではない。)
- *Mo* in negative: *Dare mo konakatta.* (誰も来なかった。)

### 🇰🇷 韓国語 (Korean)
- *An(i)* / *mot* + 動詞: *an(i) meokda* (안/못 먹다)
- *An(i)* = don't/won't; *mot* = can't
- *Ani* as copula negative: *Jon-i aniya.* (존이 아니야 = John ではない。)

### 🇨🇳 中国語 (Chinese)
- *Bù* + VP/Adj: *bù shì* (不是 = ではない), *bù xǐhuan* (不喜欢)
- *Méi* + V (完了): *méi qù* (没去)
- *Wú* (无) + N (formal/written): *wú rén* (无人 = 誰もいない), *wú fǎ* (无法 = no way)

---

## 否定極性項目 (NPI) と二重否定

### 🇬🇧 英語 (二重否定なし)
| 肯定 | 否定 |
|----------|----------|
| something | **anything** / nothing |
| someone | **anyone** / nobody |
| somewhere | **anywhere** / nowhere |
| already | **any more** / **no longer** |
| somewhat | **at all** |

- *I didn't see **anything**.* (not *nothing*)
- *I **don't** have **any** money.* (not *no money* — though colloquial *I don't got no money* exists)

### 🇪🇸 スペイン語 (二重否定必須)
| 肯定 | 否定 (with *no*) | 否定 (前置き) |
|----------|---------------------|-------------------|
| algo (something) | **nada** | **Nada** vi. |
| alguien (someone) | **nadie** | **Nadie** vino. |
| algún/alguno (some) | **ningún/ninguno** | **Ninguno** sirve. |
| también (also) | **tampoco** | **Tampoco** voy. |
| siempre (always) | **nunca / jamás** | **Nunca** voy. |

- *No vi **nada**.* (私には何も見えなかった。)
- *Nadie **no** sabe.* → *Nadie sabe.* (誰も知らない。)

### 🇯🇵 日本語 (二重否定なし — NPI は否定必要)
| 肯定 | NPI (否定必要) | 否定前置き |
|----------|------------------------|------------------|
| 何か (nanika) | 何も...ない (nani mo...nai) | 何もない (nanika mo nai) |
| 誰か (dareka) | 誰も...ない (dare mo...nai) | 誰もいない (dare mo inai) |
| どこか (dokoka) | どこも...ない (doko mo...nai) | どこにもない (doko ni mo nai) |
| いつも (itsumo) | 決して...ない (kesshite...nai) / 全然...ない (zenzen...nai) | — |
| ちょっと (chotto) | 全く...ない (mattaku...nai) | — |

- *Nani mo tabenakatta.* (何も食べなかった = 何も食べなかった。)
- *Dare mo inai.* (誰もいない = 誰もいない。)

### 🇰🇷 韓国語 (二重否定なし — NPI は否定必要)
| 肯定 | NPI (否定必要) | 否定前置き |
|----------|------------------------|------------------|
| 무언가 (mueonga) / 뭐 (mwo) | 아무것도...안/못 (amugeotdo...an/mot) | 아무것도 없다 (amugeotdo eopda) |
| 누군가 (nugunga) | 아무도...안/못 (amudo...an/mot) | 아무도 없다 (amudo eopda) |
| 어딘가 (eodinga) | 아무데도...안/못 (amudeo...an/mot) | 아무데도 없다 (amudeo...eopda) |
| 항상 (hangsang) | 결코...안/못 (gyeolko...an/mot) / 전적으로...안/못 | — |
| 조금 (jogeum) | 전혀...안/못 (jeonhyeo...an/mot) / 하나도...안/못 (hana do...an/mot) | — |

- *Amugeotdo an meogeosseo.* (아무것도 안 먹었어 = 何も食べなかった。)
- *Amudo an wasseo.* (아무도 안 왔어 = 誰も来なかった。)

### 🇨🇳 中国語 (二重否定なし — NPI は否定必要)
| 肯定 | NPI (否定必要) | 否定前置き |
|----------|------------------------|------------------|
| 什么 (shénme) | 什么都不/没 (shénme dōu bù/méi) | 什么都没有 (shénme dōu méiyǒu) |
| 谁 (shéi) | 谁都不/没 (shéi dōu bù/méi) | 谁也没有 (shéi yě méiyǒu) |
| 哪里 (nǎlǐ) | 哪里都不/没 (nǎlǐ dōu bù/méi) | 哪里都没有 (nǎlǐ dōu méiyǒu) |
| 总是 (zǒngshì) | 从不/没 (cóng bù/méi) | — |
| 一点儿 (yīdiǎnr) | 根本不/没 (gēnběn bù/méi) / 一点儿都不/没 | — |

- *Wǒ shénme dōu méi chī.* (我什么都没吃 = 何も食べなかった。)
- *Shéi yě méi lái.* (谁也没来 = 誰も来なかった。)

---

## 特殊な否定構文

### 各国語別の特殊否定構文

| 言語 | 構文 | 例 |
|----------|--------------|---------|
| **English** | 否定疑問 | *Don't you like it?* / *Isn't she coming?* |
| **English** | タグ疑問 | *You're coming, **aren't you**?* |
| **English** | 否定不定詞 | *I told him **not to go**.* |
| **Spanish** | 否定疑問 | *¿No vienes?* / *¿No te gusta?* |
| **Spanish** | タグ疑問 | *Vienes, **¿verdad?** / **¿no?*** |
| **Spanish** | 否定不定詞 | *Le dije **que no fuera**.* (接続) |
| **Japanese** | 否定疑問 | *Tabemasen ka?* (食べませんか？= Won't you eat?) |
| **Japanese** | 否定依頼 | *Tabenaide kudasai.* (食べないでください = 食べないでください。) |
| **Japanese** | 否定条件 | *Tabenakereba* (食べなければ = 食べないなら) |
| **Japanese** | *Mo...nai* (not even) | *Ichido mo ikanai.* (一度も行かない = 一度も行かない。) |
| **Japanese** | *Wa...nai* (対比) | *Kore wa tabenai.* (これは食べない = これは食べない。) |
| **Korean** | 否定疑問 | *An meogeoyo?* (안 먹어요? = 食べないの?) / *Meokji anayo?* |
| **Korean** | 否定依頼 | *Meokji maseyo.* (먹지 마세요 = 食べないでください。) |
| **Korean** | 否定条件 | *Meokji aneumyeon* (먹지 않으면 = 食べないなら) |
| **Korean** | *Mot* (cannot) vs **An** (don't) | *Mot meokda* (못 먹다 = 食べられない) vs *An meokda* (안 먹다 = 食べない) |
| **Chinese** | 否定疑問 | *Bù chī ma?* (不吃吗? = 食べない?) / *Méi chī ma?* (没吃吗?) |
| **Chinese** | 否定命令 | *Bié chī!* (别吃! = 食べるな!) / *Bù yào chī!* (不要吃!) |
| **Chinese** | 否定条件 | *Bù chī de huà* (不吃的话 = 食べないなら) / *Yào bù chī* (要不食べ) |
| **Chinese** | *Bù... yě* (not even) | *Yī cì yě méi qù.* (一次也没去 = 一度も行かなかった。) |
| **Chinese** | *Lián... dōu bù/méi* (not even) | *Lián tā dōu bù zhīdào.* (连他都不知道 = 彼さえ知らない。) |
| **Chinese** | *Wú* (无) formal | *Wú fǎ* (无法 = 方法がない), *wú rén* (无人 = 誰もいない) |

---

## 否定スコープと曖昧性

### 各国語別の曖昧性

| 言語 | 曖昧性例 |
|----------|------------------|
| **English** | *I didn't go because he called.* → 曖昧: (1) 行かなかった理由 = 彼が電話した。(2) 行った、ただし電話したからではない。 |
| **Spanish** | *No fui porque me llamó.* → 同じ曖昧性。区別: *No fui **porque** me llamó* (理由) vs *Fui, **pero no** porque me llamó.* |
| **Japanese** | *Kare ga yonda kara ikanakatta.* (彼が呼んだから行かなかった) — スコープ曖昧。 |
| **Korean** | *Geu-ga bulleoseo an gasseo.* (그가 불러서 안 갔어) — 曖昧。 |
| **Chinese** | *Wǒ bù qù shì yīnwèi tā jiào wǒ.* (我不去是因为他叫我 = 私が行かない理由は彼が電話したから) — スコープは *shì...de* 焦点構文で明確化。 |

---

## 否定慣用句

| English | Spanish | Japanese | Korean | Chinese |
|---------|---------|----------|--------|---------|
| **Not at all** | *En absoluto* | *Zenzen* (全然) + neg / *Mattaku* (全く) + neg | *Jeonhyeo* (전혀) + neg / *Hana do* (하나도) + neg | *Gēnběn* (根本) + neg / *Yīdiǎn* (一点) + neg |
| **No way** | *De ninguna manera* | *Zettai ni...nai* (絶対に...ない) | *Jeoldae* (절대) + neg | *Wànwàn bù* (万万不) / *Juéduì bù* (绝对不) |
| **Not really** | *No mucho* | *Amari...nai* (あまり...ない) | *Geureoke...an* (그렇게...안) / *Byeollo* (별로) | *Bú tài* (不太) / *Méi shénme* (没什么) |
| **Nothing special** | *Nada especial* | *Betsuni* (別に) + neg | *Byeollo* (별로) + neg / *Teukbyeolhan ge eopda* | *Méi shénme tèbié* (没什么特别) |
| **Never mind** | *No importa* | *Ki ni shinaide* (気にしないで) / *Iie, ii desu* | *Gwaenchana* (괜찮아) / *Ije geuman* | *Méi guānxi* (没关系) / *Bú yòng le* (不用了) |
| **No problem** | *No hay problema* | *Mondai nai* (問題ない) / *Daijoubu* (大丈夫) | *Munje eopda* (문제 없다) / *Gwaenchana* | *Méi wèntí* (没问题) |
| **Can't help it** | *No se puede hacer nada* | *Shou ga nai* (仕方がない) / *Shikata nai* | *Eotteoke hal su eopda* (어쩔 수 없다) | *Méi bànfǎ* (没办法) / *Wú kě nài hé* |

---

## 丁寧・フェースセービングの否定

| 言語 | 否定のソフト化 | 例 |
|----------|-------------------|---------|
| **English** | *I'm afraid not* / *I don't think so* / *Not really* | *Q: "Can you come?" A: "I'm afraid I can't."* |
| **Spanish** | *Creo que no* / *Me temo que no* / *No creo que pueda* | *¿Vienes? — Creo que no puedo.* |
| **Japanese** | *Chotto...* (暗示 no) / *Kangaete okimasu* (I'll consider it) | *Ashita kimasu ka? — Chotto... / Kangaete okimasu.* |
| **Korean** | *Geureoke hagi jom...* (그렇게 하긴 좀...) / *Jom...* | *Naeil wayo? — Geureoke hagi jom...* |
| **Chinese** | *Bù tài hǎo shuō* (不太好说) / *Kěngpà bù xíng* (恐怕不行) | *Nǐ néng lái ma? — Kěngpà bù xíng.* |

---

## クイックリファレンスカード

| 必要性 | EN | ES | JP | KR | CH |
|----------------|----|----|-----|----|----|
| **"No"** | No | No | Iie (いいえ) / Chigau (ちがう) | Aniyo (아니요) / Ani (아니) | Bù (不) / Bú (不) |
| **"Not"** | not | no | -nai / -masen / dewa nai | -ji anta / -ji anhseumnida | bù / méi |
| **"Don't (命令)"** | Don't go | No vayas | Tabenaide kudasai / Taberu na | Meokji maseyo / Meokjima | Bié qù / Bú yào qù |
| **"Didn't"** | didn't go | no fui | ikanakatta / ikimasen deshita | an gasseoyo / an gasseumnida | méi qù / bù qù (context) |
| **"Won't"** | won't go | no iré | ikanai / ikimasen | an gal geoyeyo / an gajyo | bù qù |
| **"Can't"** | can't eat | no puedo comer | taberarenai / taberaremasen | meokji motaeyo / mot meogeoyo | chī bù liǎo / bù néng chī |
| **"Nothing"** | nothing | nada | nani mo...nai | amugeotdo...an/mot | shénme dōu méi |
| **"Nobody"** | nobody | nadie | dare mo...nai | amudo...an/mot | shéi dōu méi |
| **"Nowhere"** | nowhere | en ningún lado | doko mo...nai | amudeo...an/mot | nǎlǐ dōu méi |
| **"Never"** | never | nunca / jamás | kesshite...nai / zettai ni...nai | gyeolko...an/mot / jeoldae...an/mot | cóng bù / wànwàn bù |
| **"Not at all"** | not at all | en absoluto | zenzen...nai / mattaku...nai | jeonhyeo...an/mot / hana do...an/mot | gēnběn...bù/méi / yīdiǎn...bù/méi |

---

## 🇯🇵 日本語学習者ノート (Japanese Learner Notes)

> 本セクションは日本語学習者向けの追加学習ガイドです。

### 日本語話者が他4言語の否定形を学ぶ際の一般的な落とし穴

1. **スペイン語二重否定の習得**:
   - 日本語は単一否定 (一回の否定 = 否定) → スペイン語は二重否定 (no + nada = 否定) が必須。
   - **落とし穴**: 日本語話者が「No vi nada」を「私は何も見えなかった」と直訳的発想 → 自然なスペイン語に到達。
   - **練習法**: スペイン語の二重否定表現 (algo → nada, alguien → nadie, siempre → nunca) を 5言語対訳表で暗記。

2. **中国語 *bù* vs *méi* の区別**:
   - 日本語の「〜ない」「〜なかった」は時制で区別 → 中国語は *bù* (习惯/現在/未来) vs *méi* (過去/完了/経験) で区別。
   - **落とし穴**: 日本語話者が中国語「我不要」(wǒ bú yào = 私は欲しくない) と「我没有」(wǒ méiyǒu = 私は持っていない) を混同。
   - **練習法**: *bù* (未来/習慣) vs *méi* (過去/完了) の区別を毎日 5文ずつ練習。

3. **韓国語 *an* vs *mot* の差**:
   - 日本語の「〜ない」「〜できない」は1形式 → 韓国語は *안 (an, 〜しない)* vs *못 (mot, 〜できない)* を明示的に区別。
   - **落とし穴**: 日本語話者が韓国語「안 먹어요」を「食べられない」と誤訳 (正: 食べない)。
   - **練習法**: 韓国語の 못 (能力不可能) と 안 (意志的拒否) を 5言語対訳表で。

4. **日本語の NPI「誰も...ない」「何も...ない」**:
   - 日本語の「誰も...ない」/「何も...ない」 は韓国語/中国語と類似構造 (NPI + 否定)。
   - **落とし穴**: 韓国語 アモド (아무도) / アムゴットド (아무것도) と中国語 誰も (shéi dōu) / 什么も (shénme dōu) を混同。
   - **練習法**: アモド/何も/誰も何も 系 NPI を 5言語対応表で。

5. **否定疑問 (negative question) の politico-pragmatics**:
   - 日本語の「行きませんか?」は機能的に「行きましょう」 (invitation) → 英語 "Won't you go?" も類似、スペイン語 "¿No vienes?" も同様。
   - **落とし穴**: 日本語話者が中国語「不去吗?」(bù qù ma?) を文字通り「行かないの?」と翻訳 → 実際には「行きませんか?」の invitation 機能。
   - **練習法**: 否定疑問の invitation 機能 (한국: 안 가세요? 中国: 不去吗? 英語: Don't go?) を 5言語対応表で。

### 関連日本語ウィキページ

- `[[politeness-honorifics]]` — 否定 politeness 戦略
- `[[business-email]]` — メールでの否定返答
- `[[pronouns-reference]]` — 否定代名詞 (nadie, dare mo...nai, amudo...)
- `[[greetings]]` — 招待への否定返答
- `[[shopping-money]]` — 「割引なし」「非売品」

### 学習ワークフロー推奨

1. **5言語否定形対応表** (上記早見表) を暗記
2. **スペイン語二重否定** 表現を 5言語対訳表で
3. **中国語 *bù*/*méi*** の使い分けを練習
4. **韓国語 *an*/*mot*** の文法差を 5言語対応で
5. **否定疑問 invitation** 機能を 5言語対応で

---

## 関連ページ

- `[[politeness-honorifics]]` — 否定 politeness 戦略
- `[[business-email]]` — メールでの否定返答
- `[[pronouns-reference]]` — 否定代名詞
- `[[greetings]]` — 招待への否定返答
- `[[shopping-money]]` — 「割引なし」「非売品」

## 出典

- 英語: `[English/vocabulary/basic-vocabulary]`
- スペイン語: `[Spanish/vocabulary/basic-vocabulary]`, `[Spanish/culture/espana-vs-latinoamerica-registro]`
- 日本語: `[[index]]`, `[Japanese/vocabulary/jp-counters]`
- 韓国語: `[[index]]`, `[Korean/vocabulary/topik1-starter]`
- 中国語: `[Chinese/vocabulary/body-zh]`, `[Chinese/sources/pinyin-basics-zh]`

---

**原文 (英語)**: [[negation]] | **関連ミラー**: [[negation.es|スペイン語]] · [[negation.ko|韓国語]] · [[negation.zh|中国語]] | **ポリシー**: ADR-0006
