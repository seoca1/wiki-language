# 時制と相 (tense vs aspect) — 言語間比較 (日本語版)

> 原文: [[tense-aspect-systems]] (English) | 作成日: 2026-08-20 | ADR-0006
> **5言語の時制と相 (tense/aspect) システムの比較**

---

## 早見表

### 時制システム比較

| 言語 | 過去 | 現在 | 未来 | 相区別 |
|---|---|---|---|---|
| Spanish | preterite/imperfect/perfect/pluperfect | present | future/conditional | 豊か (perfective/imperfective) |
| English | simple past/present perfect/pluperfect | present | will + verb | 単純 (perfective のみ) |
| Japanese | た形/ていた/ていた/てしまう | 常体/辞等 | ます形/だろう | 非常に豊か (完了, 経験, 進行) |
| Korean | 았/었/었었/겠 | 다/는다 | 겠/을 것 | 豊か (完了, 経験, 進行, 持続) |
| Chinese | 了/过/曾经 | present | 会/要/将 | 最小 (了=完了, 过=経験) |

### 相システム 言語間比較

| 相 | English | Spanish | Japanese | Korean | Chinese |
|--------|---------|---------|----------|--------|---------|
| **Simple (unmarked)** | I eat | Como | 食べる | 먹다 | 吃 |
| **Progressive** | I am eating | Estoy comiendo | 食べている | 먹고 있다 | 在吃 |
| **Perfect (completed)** | I have eaten | He comido | 食べた | 먹었다 | 吃了 |
| **Habitual** | I used to eat | Comía (imperfect) | 食べていた | 먹었다 | 吃过 |
| **Experiential** | I have eaten before | He comido alguna vez | 食べたことがある | 먹어 봤다 | 吃过 |
| **Inceptive (begin)** | I'm starting to eat | Empiezo a comer | 食べ始める | 먹기 시작하다 | 开始吃 |
| **Resultative (state)** | I have it eaten | Está comido | 食べてある | 먹어 있다 | 吃了 (state) |
| **Prospective** | I'm about to eat | Voy a comer | 食べようとする | 먹으려고 하다 | 快要吃 |

### 時制形マトリクス

| 時制 | English | Spanish | Japanese | Korean | Chinese |
|-------|---------|---------|----------|--------|---------|
| **Present Simple** | I eat | Como | 食べる | 먹다 | 我吃 |
| **Present Progressive** | I am eating | Estoy comiendo | 食べている | 먹고 있다 | 我在吃 |
| **Past Simple** | I ate | Comí (preterite) | 食べた | 먹었다 | 我吃了 |
| **Past Progressive** | I was eating | Comía (imperfect) | 食べていた | 먹고 있었다 | 我那时在吃 |
| **Present Perfect** | I have eaten | He comido | 食べたことがある | 먹어 봤다 | 我吃过了 |
| **Future** | I will eat | Comeré | 食べるだろう | 먹겠다 | 我会吃 |
| **Conditional** | I would eat | Comería | 食べるなら | 먹겠으면 | 我会吃的话 |
| **Conditional Perfect** | I would have eaten | Habría comido | 食べていたなら | 먹었을 것 | 我会吃的话 |

---

## 各言語詳細

### 🇬🇧 英語 (English)
- **Tense morphology**: 2 時制 (過去/現在) + 未来 via modal
- **Aspect morphology**: 限定的; progressive via "be + -ing"; perfect via "have + past participle"
- **Examples**: "I eat" (present), "I ate" (past simple), "I have eaten" (present perfect)
- **Notes**: Tense-light, aspect-light; relies on adverbs and context

### 🇪🇸 スペイン語 (Spanish)
- **Tense morphology**: 3 時制 (preterite/imperfect/future) + conditional + pluperfect + future perfect
- **Aspect morphology**: 時制に組み込まれる (preterite = perfective, imperfect = imperfective)
- **Examples**: "Como" (present), "Comí" (preterite), "Comía" (imperfect), "He comido" (present perfect)
- **Notes**: 5 言語の中で最も複雑な時制システム; 英語話者の preterite vs imperfect エラーが一般的

### 🇯🇵 日本語 (Japanese)
- **Tense morphology**: 2 時制 (過去/現在-未来 unmarked) + だろう for future
- **Aspect morphology**: 非常に豊か — ている (progressive), てしまう (completive), てある (resultative), ことがある (experiential)
- **Examples**: "食べる" (現在/未来), "食べた" (過去), "食べている" (progressive), "食べたことがある" (experiential)
- **Notes**: Tense-poor, aspect-rich — 英語/スペイン語との主要な違い

### 🇰🇷 韓国語 (Korean)
- **Tense morphology**: 2 時制 (過去 았/었/겠 + 現在 다/는다) + 未来 via -(으)ㄹ 것이다
- **Aspect morphology**: 豊か — 고 있다 (progressive), 았/었 (perfect), 어 보다 (experiential)
- **Examples**: "먹다" (現在), "먹었다" (過去), "먹고 있다" (progressive)
- **Notes**: 日本語と同様 — tense-poor, aspect-rich; 敬語体系と組み合わせ

### 🇨🇳 中国語 (Chinese)
- **Tense morphology**: なし — 動詞 inflection for tense なし
- **Aspect morphology**: Aspect particles (了=完了, 过=経験, 在=progressive) + modal verbs
- **Examples**: "我吃" (現在/未来), "我吃了" (過去/完了), "我在吃" (progressive)
- **Notes**: 5 言語の中で最も aspect-light; 助詞と語順に依存

---

## 主要な対比 (総合)

| 対比 | インサイト |
|----------|---------|
| **Spanish** has both past perfective (pretérito) and past imperfective (imperfecto) — uniquely detailed past tense system |
| **Japanese and Korean** are tense-light but aspect-rich — they use verb conjugations to encode completed (完了) vs ongoing (進行) vs experienced (経験) states |
| **Chinese** is the most minimal — relies on aspect particles (了, 过) and modal verbs (会, 要) rather than verb inflection |
| Romance vs CJK | Romance languages (Spanish) have tense morphology; CJK languages (JP/KR) have aspect morphology; Chinese is most minimal |
| East Asian aspect | JP and KR share similar aspect systems (完了/経験/進行); they often use similar forms for these concepts |

---

## 一般的な学習者エラー

| エラー | 言語ペア | 理由 |
|-------|-----------|---------|
| Forgetting preterite vs imperfect | EN→ES | English only has simple past |
| Overusing progressive | All→JP/KR | East Asian aspect is aspect-rich, not tense-based |
| Using 了 for everything | All→CH | 了 is aspect, not tense — overuse confuses time vs completion |
| Mixing tense markers | JP→KR | Both have past markers but different usages |
| Confusing past simple and present perfect | All→EN | "I ate" vs "I have eaten" — Chinese/Japanese have simpler systems |

---

## 関連ページ

- `[[mood-systems]]` — 法 (mood) システム
- `[[negation]]` — 否定システム
- `[[tense-aspect-systems]]` — 同ページ
- `[[verbs-jp]]` — 日本語動詞
- `[[particles-ko]]` — 韓国語助詞

## 出典

- `[[subjuntivo-conversacional]]` — スペイン語接続法
- `[[mood-systems]]` — 法 (mood) 比較
- `[[verb-conjugation-patterns]]` — スペイン語動詞パターン
- `[[particles-jp]]` — 日本語相助詞
- `[[particles-ko]]` — 韓国語相助詞
- `[[basic-particles]]` — 中国語相助詞 (了, 过, 在)

---

## 🇯🇵 日本語学習者ノート (Japanese Learner Notes)

> 本セクションは日本語学習者向けの追加学習ガイドです。

### 日本語話者が他4言語の tense/aspect を学ぶ際の一般的な落とし穴

1. **スペイン語 preterite vs imperfect**:
   - 日本語は過去形 1 形式 (た形) → スペイン語は preterite (完了) vs imperfect (未完了) を区別。
   - **落とし穴**: 日本語話者が「昨日、友達が公園で遊んだ」と「私が子供の頃、公園で遊んだ」の差を スペイン語「Jugó en el parque」/「Jugaba en el parque」として表現できない。
   - **練習法**: スペイン語の preterite vs imperfect を 5言語対訳表で (完了動作 vs 継続/繰り返し動作)。

2. **英語「現在完了」(have + past participle)**:
   - 日本語は「〜したことがある」「〜した」の 2 形式 → 英語は完了形 (have + p.p.) で動作の relevance を current に伝える。
   - **落とし穴**: 日本語話者が英語 "I have eaten" を「私は食べた」と直訳 → ニュアンス (現在の relevance) が伝わらない。
   - **練習法**: 英語現在完了 (I have eaten = 現在 relevance) と 過去形 (I ate = 過去完了) を 5言語対訳表で。

3. **中国語「了」vs「过」 vs「在」**:
   - 日本語は「ている」「た」「たことがある」 → 中国語は「了」(完了), 「过」(経験), 「在」(進行) を使い分け。
   - **落とし穴**: 日本語話者が中国語「了」をすべて「た」と翻訳 → 完了 (了) vs 経験 (过) vs 進行 (在) の混同。
   - **練習法**: 中国語「了/过/在」を 5言語対訳表で (例: 食べた=吃了, 食べたことがある=吃过, 食べている=在吃)。

4. **英語未来形 (will + verb)**:
   - 日本語は「食べるだろう」「〜つもり」「〜予定」 → 英語は "will + verb" で一形式。
   - **落とし穴**: 日本語話者が英語 "I will go" を「私は行くつもり」/「私は行くだろう」と翻訳 → ネイティブは直接未来 (will) を期待。
   - **練習法**: 英語の「will」「be going to」「present continuous for future」を 5言語対訳表で。

5. **仮定法 (subjunctive) の時制**:
   - 日本語は「〜だったら」 → 英語 "if I were" (subjunctive past) は 仮定法過去 = 現在 wish の意味。
   - **落とし穴**: 日本語話者が "If I were you" を「もし私があなただったら」と翻訳 → ネイティブは英語 "were" の特殊機能を理解。
   - **練習法**: 英語仮定法過去 (were) を 5言語対訳表で (wish + 過去形)。

### 関連日本語ウィキページ

- `[[mood-systems]]` — 法 (mood) システム
- `[[negation]]` — 否定システム
- `[[tense-aspect-systems]]` — 同ページ
- `[[verbs-jp]]` — 日本語動詞
- `[[particles-ko]]` — 韓国語助詞

### 学習ワークフロー推奨

1. **5言語時制・相対比表** (上記早見表) を暗記
2. **スペイン語 preterite vs imperfect** を 5言語対訳表で
3. **英語現在完了** (現在 relevance) を 5言語対訳で
4. **中国語「了/过/在」** 区別を 5言語対訳で
5. **英語未来形** (will / be going to) を 5言語対訳で

---

**原文 (英語)**: [[tense-aspect-systems]] | **関連ミラー**: [[tense-aspect-systems.es|スペイン語]] · [[tense-aspect-systems.ko|韓国語]] · [[tense-aspect-systems.zh|中国語]] | **ポリシー**: ADR-0006
