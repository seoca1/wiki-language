# Writing Systems — Cross-Language Comparison

**Languages**: English · Spanish · Japanese · Korean · Chinese
**Last updated**: 2026-07-19

---

## System Classification

| Language | System Type | Direction | Script Name | Unicode Block |
|----------|-------------|-----------|-------------|---------------|
| **English** | Alphabet (Latin) | LTR | Latin | Basic Latin, Latin-1 Supplement |
| **Spanish** | Alphabet (Latin) | LTR | Latin | Basic Latin, Latin-1 Supplement |
| **Japanese** | Mixed: Logographic + Syllabary ×2 | LTR (modern), TTB (traditional) | Kanji + Hiragana + Katakana | CJK Unified Ideographs, Hiragana, Katakana |
| **Korean** | Featural Alphabet (Hangul) | LTR (modern), TTB (traditional) | Hangul | Hangul Syllables, Hangul Jamo |
| **Chinese** | Logographic | LTR (modern), TTB (traditional) | Hanzi (Simplified / Traditional) | CJK Unified Ideographs |

---

## English & Spanish: Latin Alphabet

### English (26 letters)
| Feature | Detail |
|---------|--------|
| **Letters** | 26 (A-Z) |
| **Digraphs** | ch, sh, th, ph, wh, ng, ck, qu, etc. |
| **Diacritics** | Rare (loanwords: *café, naïve, résumé*) |
| **Case** | Upper/lower (bicameral) |
| **Phoneme-grapheme** | **Deep orthography** — 44 phonemes, 250+ spellings |
| **Punctuation** | Standard Latin (. , ? ! : ; " ' ( ) [ ] { } ...) |

### Spanish (27 letters + ñ)
| Feature | Detail |
|---------|--------|
| **Letters** | 27 (A-Z + Ñ) — *ch, ll* deprecated as letters (2010) |
| **Digraphs** | ch, ll, rr, gu, qu |
| **Diacritics** | **Acute accent (´)** — stress, disambiguation (*sí* vs *si*); **Dieresis (¨)** — *pingüino, vergüenza*; **Tilde (˜)** — *ñ* only |
| **Case** | Upper/lower |
| **Phoneme-grapheme** | **Shallow orthography** — near 1:1 (5 vowels, 19 consonants) |
| **Punctuation** | **Inverted ¿ ¡** — unique to Spanish |

### Orthographic Depth Comparison

| Word | English | Spanish |
|------|---------|---------|
| /kæt/ | cat | gato |
| /kɑː/ | car | caro |
| /siː/ | see / sea / si | sí |
| /naɪt/ | night | noche |
| /θɪŋk/ | think | pensar |

**Spanish advantage**: Predictable spelling → easier literacy acquisition
**English advantage**: Etymological transparency (*sign/signature, nation/national*)

---

## Japanese: Three-Script Mixed System

### Script Inventory

| Script | Type | Characters | Primary Use |
|--------|------|------------|-------------|
| **Hiragana** | Syllabary | 46 basic + 25 voiced + 33 combos = ~104 | Native words, grammar (okurigana), furigana, children's text |
| **Katakana** | Syllabary | 46 basic + 25 voiced + 33 combos = ~104 | Loanwords, emphasis, onomatopoeia, scientific names |
| **Kanji** | Logographic | 2,136 Jōyō (daily use) + ~3,000 more | Content words (nouns, verb stems, adj stems) |

### Hiragana (平仮名) — Basic 46

| Vowel | k | s | t | n | h | m | y | r | w |
|-------|---|---|---|---|---|---|---|---|---|
| **a** | あ | か | さ | た | な | は | ま | や | ら | わ |
| **i** | い | き | し | ち | に | ひ | み |  | り |  |
| **u** | う | く | す | つ | ぬ | ふ | む | ゆ | る | を |
| **e** | え | け | せ | て | ね | へ | め |  | れ |  |
| **o** | お | こ | そ | と | の | ほ | も | よ | ろ | ん |

**Diacritics**: Dakuten (゛) = voiced (*ka→ga*); Handakuten (゜) = p-sound (*ha→pa*)

### Katakana (片仮名) — Basic 46

| Vowel | k | s | t | n | h | m | y | r | w |
|-------|---|---|---|---|---|---|---|---|---|
| **a** | ア | カ | サ | タ | ナ | ハ | マ | ヤ | ラ | ワ |
| **i** | イ | キ | シ | チ | ニ | ヒ | ミ |  | リ |  |
| **u** | ウ | ク | ス | ツ | ヌ | フ | ム | ユ | ル | ヲ |
| **e** | エ | ケ | セ | テ | ネ | ヘ | メ |  | レ |  |
| **o** | オ | コ | ソ | ト | ノ | ホ | モ | ヨ | ロ | ン |

### Kanji (漢字) — Key Stats

| Metric | Value |
|--------|-------|
| **Jōyō Kanji** (常用漢字) | 2,136 (official daily use) |
| **Jinmeiyō Kanji** (人名用漢字) | 863 (names only) |
| **Total in use** | ~3,000-4,000 (educated adult) |
| **Readings per kanji** | 2-10+ (On-yomi + Kun-yomi) |
| **Stroke count range** | 1-30+ (mean ~12) |

### Mixed Writing Example

```
昨日は友達と東京駅で待ち合わせをして、ラーメンを食べました。
```

| Segment | Script | Function |
|---------|--------|----------|
| 昨日 | Kanji | "yesterday" (content) |
| は | Hiragana | Topic marker (grammar) |
| 友達 | Kanji | "friend" (content) |
| と | Hiragana | Particle "with" |
| 東京駅 | Kanji | "Tokyo Station" (proper noun) |
| で | Hiragana | Particle "at" |
| 待ち合わせ | Kanji + Hiragana | "meeting" (verb stem + okurigana) |
| を | Hiragana | Object marker |
| し | Hiragana | Verb stem (suru) |
| て | Hiragana | Te-form connector |
| ラーメン | Katakana | "ramen" (loanword) |
| を | Hiragana | Object marker |
| 食べ | Kanji | Verb stem "eat" |
| まし | Hiragana | Polite suffix |
| た | Hiragana | Past tense |
| です | Hiragana | Copula polite |
| 。 | Punctuation | Period |

### Romaji Systems

| System | Example | Use Case |
|--------|---------|----------|
| **Hepburn** (standard) | *Tokyo, shinkansen, ganbaru* | International, passports, signs |
| **Kunrei-shiki** | *Tôkyô, sinsenkansen, ganbaru* | Japanese education (MEXT) |
| **Nihon-shiki** | *Tôkyô, sinsenkansen, ganbaru* | Linguistics, historical |

---

## Korean: Hangul (한글) — Featural Alphabet

### Design Principles (1443, Sejong the Great)

| Principle | Implementation |
|-----------|----------------|
| **Featural** | Letter shapes encode articulation (tongue, lips, throat) |
| **Syllabic blocks** | Letters combine into square syllables (CV, CVC, CVCC) |
| **Systematic** | 19 consonants × 21 vowels = 11,172 possible syllables |
| **Phonemic** | Near 1:1 letter-to-sound |

### Consonants (19: 14 basic + 5 tense)

| Basic | ㄱ | ㄴ | ㄷ | ㄹ | ㅁ | ㅂ | ㅅ | ㅇ | ㅈ | ㅊ | ㅋ | ㅌ | ㅍ | ㅎ |
|-------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sound | g/k | n | d/t | r/l | m | b/p | s | ng/∅ | j/ch | ch' | k' | t' | p' | h |
| Tense | ㄲ | ㄸ | ㅃ | ㅆ | ㅉ | | | | | | | | | |
| Sound | kk | tt | pp | ss | jj | | | | | | | | | |

**Articulatory featural shapes**:
- ㄱ (g/k) — tongue back raised
- ㄴ (n) — tongue tip to alveolar ridge
- ㅁ (m) — lips closed
- ㅅ (s) — tooth shape
- ㅇ (ng/∅) — throat outline

### Vowels (21: 10 basic + 11 diphthongs)

| Basic | ㅏ | ㅑ | ㅓ | ㅕ | ㅗ | ㅛ | ㅜ | ㅠ | ㅡ | ㅣ |
|-------|---|---|---|---|---|---|---|---|---|---|
| Sound | a | ya | eo | yeo | o | yo | u | yu | eu | i |

| Diphthong | ㅐ | ㅒ | ㅔ | ㅖ | ㅘ | ㅙ | ㅚ | ㅝ | ㅞ | ㅟ | ㅢ |
|-----------|---|---|---|---|---|---|---|---|---|---|---|
| Sound | ae | yae | e | ye | wa | wae | oe | wo | we | wi | ui |

### Syllable Block Structure

```
CV:    가 (ga) = ㄱ + ㅏ
CVC:   감 (gam) = ㄱ + ㅏ + ㅁ
CVCC:  값 (gaps) = ㄱ + ㅏ + ㄱ + ㅅ (final cluster)
```

**Batchim (받침)** — Final consonants: 27 possible (single + clusters)

### Orthographic Rules

| Rule | Example |
|------|---------|
| **No initial ㅇ** | *아* (a) not *이아* |
| **Batchim neutralization** | *값* [갑] — ㅅ→ㄷ; *닭* [닥] — ㄹ silent |
| **Tensing** | *꽃이* [꼬치] — ㅊ tensing after batchim |
| **Nasalization** | *깜짝* [깜짝] — ㅁ+ㅈ→ㄴㅉ |
| **Liaison** | *한국어* [한구거] — ㄱ→ㅇ between vowels |

### Romanization Systems

| System | Example | Use |
|--------|---------|-----|
| **Revised Romanization (2000)** | *Hangul, Seoul, Gimpo* | Official (South Korea), road signs |
| **McCune-Reischauer (1937)** | *Han'gŭl, Sŏul, Kimp'o* | Academia, North Korea |
| **Yale** | *Hankul, Sel, Kimpo* | Linguistics |

---

## Chinese: Hanzi (汉字/漢字) — Logographic

### Simplified vs Traditional

| Aspect | Simplified (简体) | Traditional (繁體) |
|--------|------------------|-------------------|
| **Regions** | Mainland, Singapore, Malaysia | Taiwan, Hong Kong, Macau, overseas |
| **Characters** | ~2,500 reduced strokes | ~4,500+ full forms |
| **Reduction methods** | Cursive → standard; merge homophones; reduce radicals | Preserves etymology |
| **Example** | 爱 / 龙 / 书 / 学 | 愛 / 龍 / 書 / 學 |

### Character Structure

| Type | % | Principle | Example |
|------|---|-----------|---------|
| **Pictographic** (象形) | ~4% | Picture of object | 日 (sun), 月 (moon), 山 (mountain), 人 (person) |
| **Ideographic** (指事) | ~2% | Abstract concept | 上 (up), 下 (down), 一 (one), 二 (two) |
| **Compound Ideographic** (会意) | ~10% | Meaning + meaning | 休 (person + tree = rest), 好 (woman + child = good) |
| **Phono-semantic** (形声) | ~80%+ | Radical (meaning) + Phonetic (sound) | 妈 (female + ma), 河 (water + he), 晴 (sun + qing) |

### Radicals (部首 — 214 Kangxi)

| Radical | Name | Meaning | Example Characters |
|---------|------|---------|-------------------|
| 人 (亻) | rén | person | 你, 他, 们, 休, 位 |
| 水 (氵) | shuǐ | water | 河, 洋, 泳, 汗, 汁 |
| 火 (灬) | huǒ | fire | 灯, 烧, 热, 灾, 烟 |
| 木 | mù | wood/tree | 林, 森, 材, 村, 校 |
| 心 (忄) | xīn | heart/mind | 想, 情, 恩, 急, 息 |
| 口 | kǒu | mouth | 吃, 喝, 叫, 哪, 吴 |
| 手 (扌) | shǒu | hand | 拿, 推, 拉, 打, 拜 |
| 言 (讠) | yán | speech | 说, 话, 读, 讯, 论 |

### Phonetic Components (Not Perfect)

| Phonetic | Sound | Characters (same phonetic, diff meaning) |
|----------|-------|------------------------------------------|
| **马** (mǎ) | ma | 妈 (mā mother), 码 (mǎ code), 蚂 (mǎ ant), 骂 (mà scold) |
| **青** (qīng) | qing | 青 (qīng), 请 (qǐng), 情 (qíng), 晴 (qíng), 清 (qīng) |
| **工** (gōng) | gong | 工 (gōng), 功 (gōng), 攻 (gōng), 红 (hóng), 江 (jiāng) |

### Orthographic Stats

| Metric | Value |
|--------|-------|
| **HSK 1-6 vocab** | ~5,000 words / ~2,600 chars |
| **Literacy threshold** | ~3,000 chars (newspaper) |
| **Educated adult** | ~5,000-8,000 chars |
| **Total encoded** | ~98,000 (Unicode) / ~50,000 (Kangxi) |
| **Stroke count range** | 1-64 (mean ~12) |
| **Most complex** | 龘 (zhé, 64 strokes) / 龍 (traditional, 16) |

### Pinyin (拼音) — Romanization

| Feature | Detail |
|---------|--------|
| **Official** | ISO 7098, China standard (1958) |
| **Tone marks** | 4 tones + neutral (ā á ǎ à a) |
| **Initials** | 21 (b p m f d t n l g k h j q x zh ch sh r z c s y w) |
| **Finals** | 36 (a o e i u ü + compounds) |
| **Syllables** | ~400 base × 4 tones = ~1,600 tonal syllables |
| **Spacing** | Word-based (not syllable) — *wǒ ài nǐ* not *wǒ ài nǐ* |

---

## Comparative Learning Burden

| Metric | English | Spanish | Japanese | Korean | Chinese |
|--------|---------|---------|----------|--------|---------|
| **Graphemes to learn** | 26 + digraphs | 27 + diacritics | ~100 kana + 2,136 kanji | 40 jamo (blocks) | ~3,000 hanzi |
| **Phonemic transparency** | Low (deep) | **High (shallow)** | High (kana) / Low (kanji) | **High (featural)** | Low (logographic) |
| **Literacy age** | 7-8 | 5-6 | 12+ (kanji through HS) | 5-6 | 10-12 |
| **Adult functional** | 20,000+ words | 20,000+ words | 2,136 jōyō + vocab | 2,000+ hanja + hangul | 3,000-5,000 hanzi |
| **Input method** | Direct typing | Direct typing | IME (kana→kanji) | IME (jamo→syllable) | IME (pinyin→hanzi) |

---

## Digital Text Processing

| Challenge | EN/ES | JP | KR | CH |
|-----------|-------|-----|-----|-----|
| **Segmentation** | Trivial (spaces) | Hard (no spaces) | Easy (syllable blocks) | Hard (no spaces) |
| **Sorting** | Alphabetical | By reading (kana) | Hangul order (가나다) | By radical / pinyin / stroke |
| **Search** | Substring | Substring + reading | Syllable/word | Substring + pinyin |
| **OCR** | Mature | Complex (3 scripts) | Good (regular blocks) | Complex (dense strokes) |

---

## Related Pages

- `[[pronunciation-challenges.md]]` — sound systems behind orthographies
- `[[grammar-difficulty-map.md]]` — grammar complexity by feature
- `[[cultural-values.md]]` — writing system as cultural artifact
- `[[untranslatable-concepts.md]]` — concepts embedded in scripts

---

## Sources

- `[[wiki/English/vocabulary/basic-vocabulary]]`
- `[[wiki/Spanish/vocabulary/basic-vocabulary]]`
- `[[wiki/Japanese/vocabulary/basic-vocabulary]]`, `[[wiki/Japanese/vocabulary/jp-counters]]`, `[[wiki/Japanese/vocabulary/kanji-n5]]`
- `[[wiki/Korean/vocabulary/basic-vocabulary]]`, `[[wiki/Korean/vocabulary/topik1-starter]]`
- `[[wiki/Chinese/vocabulary/body-zh]]`, `[[wiki/Chinese/sources/pinyin-basics-zh]]`
- Unicode Consortium — *Unicode Standard*
- DeFrancis, J. (1989) *Visible Speech: The Diverse Oneness of Writing Systems*
- Taylor, I. & Olson, D.R. (1995) *Scripts and Literacy*