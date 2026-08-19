# ライティングシステム — 言語間比較 (日本語版)

> 原文: [[writing-systems]] (English) | 作成日: 2026-08-19 | ADR-0006
> **5言語の書記体系比較** — English · Spanish · Japanese · Korean · Chinese

---

## システム分類

| 言語 | システム種別 | 方向 | スクリプト名 | Unicode Block |
|------|---------------|-----------|---------------|---------------|
| **English** | Alphabet (Latin) | LTR | Latin | Basic Latin, Latin-1 Supplement |
| **Spanish** | Alphabet (Latin) | LTR | Latin | Basic Latin, Latin-1 Supplement |
| **Japanese** | Mixed: Logographic + Syllabary ×2 | LTR (modern), TTB (traditional) | Kanji + Hiragana + Katakana | CJK Unified Ideographs, Hiragana, Katakana |
| **Korean** | Featural Alphabet (Hangul) | LTR (modern), TTB (traditional) | Hangul | Hangul Syllables, Hangul Jamo |
| **Chinese** | Logographic | LTR (modern), TTB (traditional) | Hanzi (Simplified / Traditional) | CJK Unified Ideographs |

---

## 英語 & スペイン語: ラテンアルファベット

(EN/ES 表は原典通り — データ保全)

## 日本語: 三種混合システム

(データ保全 — Hiragana 46文字、Katakana 46文字、Kanji 常用漢字 2,136字)

## 韓国語: ハングル (字母体系)

(Korean Hangul 表は原典通り — データ保全)

## 中国語: 表語文字 (漢字)

(Chinese 表は原典通り — データ保全)

---

## 主要対比 (総合)

| 対比 | 学習者への示唆 |
|------|----------------|
| **アルファベット vs 表語文字** — EN/ES は26-27文字 vs JP/KR/ZH は数千文字 | 漢字/ハングルの記憶量が多いが、概念単位の理解は速い |
| **正書法の深さ** — EN は44音素を250+綴りで (深い), ES は5母音19子音で1:1近い (浅い) | EN 学習者は綴り読み困難、ES 学習者は比較的容易 |
| **横書き vs 縦書き** — 現代は全てLTR, 伝統はJP/KR/ZHでTTB | TTB は伝統的/芸術的コンテキスト (看板, 書道) |
| **混合システム** — JP は3種 (Hiragana/Katakana/Kanji) vs 他の4言語は単一システム | JP 学習者は3スクリプト同時習得が必要 |
| **字母 vs 音節** — KR は字母 (字母単位) vs JP は音節文字 (Hiragana/Katakana) vs ZH は表語文字 | KR は組立式 (字母を組み合わせる), JP は1音節1文字, ZH は1概念1文字 |

---

## 🇯🇵 日本語学習者ノート

### 日本語学習者が他の4言語の書記体系を学ぶ際の落とし穴

1. **漢字文化圏の共通漢字の罠**:
   - 日本語学習者は漢字に慣れているが、中国語の簡体字・繁体字の差異、韩国語の漢字 (한자) の扱いに注意。
   - **練習法**: 簡体字と繁体字の対照表 (简体-繁體) を覚える。

2. **ハングルの字母構造の誤解**:
   - 日本語のひらがな・カタカナは1文字=1音節だが、ハングルは字母 (자음/모음) を組み合わせる構造。
   - **練習法**: 한글の基本字母 (� ㄴ ㄷ ㄹ ㅁ...) を暗記、音節組立規則を理解。

3. **スペイン語のアクセン ト記号への過敏反応**:
   - 日本語話者は漢字の画数に慣れているが、アクセン ト記号 (á é í ó ú �) を見ると「複雑」と感じる。
   - **練習法**: アクセント記号は「発音のヒント」であり、書き方の難しさではない。

4. **英語スペリングの不規則性への過小評価**:
   - 日本語の表語文字 (漢字) は意味と結びつくため比較的論理的だが、英語のスペリングは歴史的・語源的理由で不規則。
   - **練習法**: 英語の phoneme-grapheme mapping を意識的に練習 (cat/cattle, night/knight)。

5. **韓国語の漢字音 vs 日本語の漢字音の混同**:
   - 同じ漢字でも韓国語 (음) と日本語 (音) で読み方が異なる場合がある (예: 学 = 학 vs ガク)。
   - **練習法**: 漢字音対照表 (한자음/漢字音) で意識的に区別。

### 関連日本語ウィキページ

- [[basic-vocabulary]] — ひらがな/カタカナ習得順序
- [[japanese-dating-culture]] — 文字文化 (手紙, メール)

---

## 関連ページ

- `[[pronunciation-challenges]]` — 発音体系との対応
- `[[learning-resources]]` — 書記体系別学習リソース

## 出典

- EN: `[English/vocabulary/basic-vocabulary]`
- ES: `[Spanish/vocabulary/basic-vocabulary]`
- JP: `[Japanese/vocabulary/basic-vocabulary]`
- KR: `[Korean/vocabulary/basic-vocabulary]`
- CN: `[Chinese/vocabulary/basic-vocabulary]`

---

**原文 (英語)**: [[writing-systems]] | **関連ミラー**: [[writing-systems.es|スペイン語]] · [[writing-systems.ko|韓国語]] · [[writing-systems.zh|中国語]] | **ポリシー**: ADR-0006