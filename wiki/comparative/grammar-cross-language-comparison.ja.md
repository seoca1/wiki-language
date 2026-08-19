# 文法言語間比較 (日本語版)

> 原文: [[grammar-cross-language-comparison]] (English) | 作成日: 2026-08-19 | ADR-0006
> **5言語の文法アーキテクチャ比較** — English · Spanish · Japanese · Korean · Chinese

---

## 早見表

| 特徴 | English | Spanish | Japanese | Korean | Chinese |
|---------|---------|---------|----------|--------|---------|
| **語順** | SVO | SVO | SOV | SOV | SVO |
| **時制マーキング** | 形態的 (eat/ate) | 形態的 (-é/-ió) | 形態的 (ta-form) | 形態的 (았/었) | アスペクト助詞 (了/过) |
| **アスペクト システム** | 進行 (-ing), 完了 (have+V-ed) | 進行 (-ndo), 完了 (-ado) | -te iru (進行), -te shimau (完了) | -고 있다 (進行), -아/어 있다 (状態) | 着 (進行), 了 (完了), 过 (経験) |
| **冠詞** | a / an / the | el / la / un / una | なし | なし | なし |
| **性** | なし (自然性別) | 男性 / 女性 | なし | なし | なし |
| **動詞のポライトネス** | なし | 限定的 (usted 動詞形) | 完全システム (keigo) | 完全システム (합쇼체/해요체) | なし |
| **複数マーキング** | -s (規則) | -s/-es | 複数化 たち (tachi) オプション | 複数化 들 (deul) オプション | なし (文脈) |
| **疑問マーカー** | 倒置 / 上昇イントネーション | ¿...? + 倒置 | か (ka) | 까? (kka?) / 니? (ni?) | 吗 (ma) |
| **否定** | don't / not | no / -ar/-er/-ir changes | ない (nai) / ません (masen) | 안 (an) / -지 않다 (-ji anhda) | 不 (bù) / 没 (méi) |
| **代名詞省略** | 必須 | 必須 | 一般的 (ゼロ代名詞) | 一般的 | 一般的 |

---

## 語順詳細

| 順序 | 言語 | 例 |
|-------|-----------|---------|
| **SVO (主語-動詞-目的語)** | English, Spanish, Chinese | "I eat apples." / "Como manzanas." / "我吃苹果。" |
| **SOV (主語-目的語-動詞)** | Japanese, Korean | "私はりんごを食べる" (Watashi wa ringo o taberu) / "나는 사과를 먹다" (Naneun sagwa-reul meokda) |

---

## 時制 vs アスペクト

| 概念 | English | Spanish | Japanese | Korean | Chinese |
|---------|---------|---------|----------|--------|---------|
| **単純過去** | ate | comí | 食べた (tabeta) | 먹었다 (meogeotda) | 吃了 (chī le) |
| **現在進行** | is eating | está comiendo | 食べている (tabete iru) | 먹고 있다 (meokgo itda) | 吃着 (chī zhe) |
| **経験** | have eaten | he comido | 食べたことがある (koto ga aru) | 먹어 본 적 있다 (meogeo bon jeok itda) | 吃过 (chī guò) |
| **未来** | will eat | comerá | 食べるだろう (darō) | 먹을 것이다 (meogeul geosida) | 会吃 (huì chī) |

---

## 冠詞 & 限定詞

| タイプ | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **定** | the | el / la | (なし) | (なし; 그 "geu") | (なし; 这 "zhè") |
| **不定** | a / an | un / una | (なし) | (なし; 한 "han") | (なし) |
| **指示** | this / that | este / ese | これ / それ (kore/sore) | 이 / 그 (i/geu) | 这 / 那 (zhè/nà) |
| **所有** | my, your, his | mi, tu, su | 私の (watashi no) | 나의 (na-ui) | 我的 (wǒ de) |

---

## 各言語詳細

### 🇬🇧 英語 (English)
- **主要用語**: SVO, 冠詞 (a/an/the), 時制-アスペクト, do-support
- **パターン**: 時制必須; 単数可算名詞に冠詞必須
- **出典**: `[[wiki/English/grammar/grammar-overview]]`

### 🇪🇸 スペイン語 (Spanish)
- **主要用語**: SVO, 性一致, ser vs estar, 接続法
- **パターン**: 動詞が人/数で活用; 接続法は疑い/願望/感情
- **地域変種**: Voseo (Rioplatense); vosotros (スペイン) vs ustedes (ラ米)
- **出典**: `[[wiki/Spanish/grammar/grammar-overview]]`

### 🇯🇵 日本語 (Japanese)
- **主要用語**: SOV, 助詞 (は/が/を/に/で/へ), keigo
- **パターン**: トピック-コメント (は/が); 動詞は常に最後
- **敬語 / ポライトネスレベル**: 尊敬語 (respect), 謙譲語 (humble), 丁寧語 (polite)
- **出典**: `[[wiki/Japanese/grammar/grammar-overview]]`

### 🇰🇷 韓国語 (Korean)
- **主要用語**: SOV, 助詞 (은/는/이/가/를/을), speech levels
- **パターン**: トピック 는/은, 主語 가/이; 動詞は常に最後
- **Speech level**: 합쇼체 formal / 해요체 polite / 해체 plain / 하소서체 literary
- **出典**: `[[wiki/Korean/grammar/grammar-overview]]`

### 🇨🇳 中国語 (Chinese)
- **主要用語**: SVO, アスペクト助詞 (了/过/着), 量詞
- **パターン**: 動詞は活用しない; アスペクト助詞が time-flow をマーク
- **レジスタ / 敬語**: 您 (nín) 敬語; 量詞必須 (个/本/杯/张)
- **出典**: `[[wiki/Chinese/grammar/grammar-overview-zh]]`

---

## 主要な対比 (総合)

| 対比 | 学習者への示唆 |
|----------|--------------------------|
| **語順の系統** | EN/ES/CH = SVO; JP/KR = SOV. SOV 話者は JP/KR に直接マッピング可能 |
| **冠詞** | EN/ES は可算名詞に冠詞必須; JP/KR/CH には冠詞なし |
| **ポライトネスの深さ** | JP/KR は完全な動詞ベース ポライトネス; EN/ES/CH は代名詞/語選択に依存 |
| **時制 vs アスペクト** | EN/ES は形態的に時制をマーク; CH はアスペクト助詞; JP/KR は両方混合 |

---

## 学習者決定ガイド

> **語順**: SVO (EN/ES/CH) vs SOV (JP/KR)
> **ポライトネス**: Keigo (JP) / 합쇼체 (KR) / usted (ES) / please (EN) / 请 (CH)
> **冠詞**: a/the (EN) · el/la (ES) · none (JP/KR/CH)
> **アスペクト**: -ing (EN) · 了/过/着 (CH) · -te iru / -고 있다 (JP/KR)

---

## 🇯🇵 日本語学習者ノート (Japanese Learner Notes)

> 本セクションは日本語学習者向けの追加学習ガイドです。

### 日本語話者が他の4言語の文法を学ぶ際の一般的な落とし穴

1. **SOV → SVO への語順転換失敗**:
   - 日本語は SOV (「私はりんごを食べる」) → 英語・スペイン語・中国語は SVO ("I eat apples")。
   - **落とし穴**: 日本語話者が英語「SOV」を作ろうとする ("I apples eat")。
   - **練習法**: 英語 SVO 構文を機械的に練習; 主語 + 動詞 + 目的語の順序をマスター。

2. **冠詞の欠如 (英語/スペイン語)**:
   - 日本語は冠詞なし → 英語 "a book" / スペイン語 "un libro" の冠詞を忘れる。
   - **練習法**: 冠詞練習を反復; 不定冠詞 (a/an) と定冠詞 (the) の使い分けをマスター。

3. **動詞活用の単純化 (中国語)**:
   - 中国語は動詞活用なし → 日本語話者にとって中国語は「易しい」が、過去/未来/アスペクト (了/过/着) を区別する必要あり。
   - **練習法**: 中国語の 了/过/着 を日本語の「た」「たことがある」「ている」に対応させて理解。

4. **敬語システムの違い**:
   - 日本語の敬語 (尊敬語/謙譲語/丁寧語) → 韓国語も 존댓말 があるが、中国語・英語・スペイン語は限定的。
   - **練習法**: 英語では "Please" + "Thank you" のみ; 中国語は 您 + 役職; スペイン語は usted/tú。

5. **性・数一致 (スペイン語)**:
   - 日本語は性・数変化なし → スペイン語の性一致 (tío/tía) と複数形 (libros) を忘れがち。
   - **練習法**: ペア暗記; 名詞の性と数を意識した文を作成。

### 関連日本語ウィキページ

- [Japanese/grammar/grammar-overview] — 日本語文法概要
- [Japanese/grammar/japanese-sos-construction] — 日本語 SOV 構文
- [Japanese/vocabulary/japanese-particles] — 日本語助詞
- [Japanese/grammar/japanese-keigo] — 敬語システム
- [Japanese/vocabulary/measure-words-jp] — 日本語量詞

### 学習ワークフロー推奨

1. **5言語の語順対照表作成** (SVO vs SOV)
2. **冠詞ペア暗記** (EN/ES の冠詞 20 パターン)
3. **時制・アスペクト マトリクス** (5言語 × 4 アスペクト)
4. **敬語レベル比較** (EN 2 層 vs ES 2 層 vs JP 5 層 vs KR 3 層 vs CH 2 層)
5. **5言語で同じ内容を表現** (自己紹介を5言語で書いて比較)

---

## 関連ページ

- `[[grammar-difficulty-map]]` — 特徴別難易度ランキング
- `[[tense-aspect-systems]]` — 時制 vs アスペクト 深堀り
- `[[politeness-honorifics]]` — 完全な keigo / speech-level システム
- `[[mood-systems]]` — 直説法 vs 接続法
- `[[pronouns-reference]]` — 代名詞システムとゼロ代名詞

## 出典

- English: `[[wiki/English/grammar/grammar-overview]]`
- Spanish: `[[wiki/Spanish/grammar/grammar-overview]]`
- Japanese: `[[wiki/Japanese/grammar/grammar-overview]]`
- Korean: `[[wiki/Korean/grammar/grammar-overview]]`
- Chinese: `[[wiki/Chinese/grammar/grammar-overview-zh]]`

## Changelog

- `2026-08-11`: Created — 言語間文法アーキテクチャ概要 (語順、時制/アスペクト、冠詞、ポライトネス)

---

**原文 (英語)**: [[grammar-cross-language-comparison]] | **関連ミラー**: [[grammar-cross-language-comparison.es|スペイン語]] · [[grammar-cross-language-comparison.ko|韓国語]] · [[grammar-cross-language-comparison.zh|中国語]] | **ポリシー**: ADR-0006