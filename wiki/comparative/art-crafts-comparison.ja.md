# 美術・工芸 — 言語間比較 (日本語版)

> 原文: [[art-crafts-comparison]] (English) | 作成日: 2026-08-19 | ADR-0006
> **5言語の美術・工芸比較** — English · Spanish · Japanese · Korean · Chinese

---

## 早見表

### 視覚芸術

| 芸術形式 | English | Spanish | Japanese | Korean | Chinese |
|----------|---------|---------|----------|--------|---------|
| **絵画** | Painting | Pintura | 絵画 (kaiga) | 회화 (hoehwa) | 绘画 (huìhuà) |
| **ドローイング / 素描** | Drawing | Dibujo | ドローイング / 素描 (sobyō) | 드로잉 / 소묘 (somyo) | 素描 (sùmiáo) |
| **彫刻** | Sculpture | Escultura | 彫刻 (chōkoku) | 조각 (jogak) | 雕塑 (diāosù) |
| **スケッチ** | Sketch | Bosquejo | スケッチ (sukecchi) | 스케치 (seukechi) | 速写 (sùxiě) / 草图 (cǎotú) |
| **水彩** | Watercolor | Acuarela | 水彩 (suisai) | 수채화 (suchaehwa) | 水彩画 (shuǐcǎihuà) |
| **油絵** | Oil painting | Óleo | 油絵 (aburae) | 유화 (yuhwa) | 油画 (yóuhuà) |
| **水墨画** | Ink wash | Tinta china / Lavado | 水墨画 (suibokuga) | 수묵화 (sumukhwa) | 水墨画 (shuǐmòhuà) |
| **書道** | Calligraphy | Caligrafía | 書道 (shodō) | 서예 (seoye) | 书法 (shūfǎ) |

### 伝統工芸

| 工芸 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **陶磁器** | Pottery / Ceramics | Cerámica | 陶器 (tōki) | 도예 (doye) | 陶瓷 (táocí) |
| **折り紙** | Origami (JP) | Origami | 折り紙 (origami) | 종이접기 (jongijeopgi) | 折纸 (zhézhǐ) |
| **韓服** | Hanbok (KR dress) | Hanbok | ハンボク | 한복 (hanbok) | 韩服 (hánfú) |
| **着物** | Kimono (JP) | Kimono | 着物 (kimono) | 기모노 (gimono) | 和服 (héfú) |
| **漢服** | Hanfu (CN) | Hanfu | 漢服 (kanfu) | 한푸 (hanpu) | 汉服 (hànfú) |
| **漆器** | Lacquerware | Laca | 漆器 (shikki) | 칠기 (chilgi) | 漆器 (qīqì) |
| ** batik** | Batik | Batik | batik (battikku) | batik (batik) | 蜡染 (làrǎn) |
| **織物** | Weaving | Tejido | 織物 (orimono) | 직물 (jikmul) | 纺织 (fǎngzhī) |
| **刺繍** | Embroidery | Bordado | 刺繍 (shishū) | 자수 (jasu) | 刺绣 (cìxiù) |

### 画材・材料

| 用品 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **筆** | Brush | Pincel / Brocha | 筆 (fude) / ブラシ | 붓 (but) | 画笔 (huàbǐ) / 毛笔 (máobǐ) |
| **キャンバス** | Canvas | Lienzo | キャンバス (kyanbasu) | 캔버스 (kaenbeoseu) | 画布 (huàbù) |
| **絵具** | Paint | Pintura | 絵具 (enogu) / ペンキ | 물감 (mulgam) / 페인트 | 颜料 (yánliào) / 油漆 (yóuqī) |
| **画架** | Easel | Caballete | 画架 (gaká) / イーゼル | 이젤 (ijel) | 画架 (huàjià) |
| **パレット** | Palette | Paleta | パレット (paretto) | 팔레트 (palleteu) | 调色板 (tiáosèbǎn) |
| **墨** | Ink | Tinta | 墨 (sumi) | 먹 (meok) | 墨 (mò) |
| **鉛筆** | Pencil | Lápiz | 鉛筆 (empitsu) | 연필 (yeonpil) | 铅笔 (qiānbǐ) |
| **紙** | Paper | Papel | 紙 (kami) | 종이 (jongi) | 纸 (zhǐ) |

### 展示・ギャラリー

| 用語 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **美術館** | Art gallery | Galería de arte | 美術館 (bijutsukan) | 미술관 (misulgwan) | 美术馆 (měishùguǎn) |
| **博物館** | Museum | Museo | 博物館 (hakubutsukan) | 박물관 (bangmulgwan) | 博物馆 (bówùguǎn) |
| **展覧会** | Exhibition | Exposición | 展覧会 (tenrankai) | 전시회 (jeonsihoe) | 展览 (zhǎnlǎn) |
| **芸術家** | Artist | Artista | 芸術家 (geijutsuka) | 예술가 (yesulga) | 艺术家 (yìshùjiā) |
| **キュレーター** | Curator | Curador | キュレーター (kyurētā) | 큐레이터 (kyureiteo) | 策展人 (cèzhǎnrén) |
| **彫刻家** | Sculptor | Escultor | 彫刻家 (chōkokuka) | 조각가 (jogakka) | 雕塑家 (diāosùjiā) |
| **画家** | Painter | Pintor | 画家 (gaka) | 화가 (hwaga) | 画家 (huàj) |
| **美術品** | Artwork | Obra de arte | 美術品 (bijutsuhin) | 예술품 (yesulpun) | 艺术品 (yìshùpǐn) |

---

## 各言語詳細

### 🇬🇧 英語 (English)
- **主要用語**: "Art" (general), "Fine arts" vs "Crafts" 区別; "Canvas" (ラテン語借用)
- **パターン**: "Arts and crafts" は単一複合概念; "visual arts" 包括用語
- **出典**: 英語 wiki にはまだ art テーマ未投入

### 🇪🇸 スペイン語 (Spanish)
- **主要用語**: "Arte" (art, 性が移動: el arte / las artes); "Artesanía" = 工芸; "Obra" (work)
- **パターン**: "bellas artes" (fine arts) と "artesanía" (crafts) の強い区別; muralismo (壁画運動) の豊かな伝統
- **出典**: スペイン語 wiki にはまだ art テーマ未投入

### 🇯🇵 日本語 (Japanese)
- **主要用語**: 美術 (bijutsu = fine art); 工芸 (kōgei = crafts); 芸術 (geijutsu = art broadly)
- **パターン**: 強い工芸伝統: 茶道 (sadō = 茶道), 華道 (kadō = 華道) を芸術形式として扱う; ukiyo-e (浮世絵) = 木版画
- **出典**: 日本語 wiki にはまだ art テーマ未投入

### 🇰🇷 韓国語 (Korean)
- **主要用語**: 미술 (misul = fine art); 공예 (gongye = crafts); 예술 (yesul = art broadly)
- **パターン**: 強い工芸伝統: 瓷器 (青磁), 韩纸 (hanji paper); 분청사기 (bunchaengsagi) 陶磁器
- **出典**: 韓国語 wiki にはまだ art テーマ未投入

### 🇨🇳 中国語 (Chinese)
- **主要用語**: 艺术 (yìshù = art); 工艺 (gōngyì = craft); 美术 (měishù = fine art)
- **パターン**: 文房四宝 (wénfáng sìbǎo = 文房四宝: 筆、墨、紙、硯); 国画 (guóhuà = 中国伝統絵画)
- **出典**: 中国語 wiki にはまだ art テーマ未投入

---

## 主要な対比 (総合)

| 対比 | 学習者への示唆 |
|------|----------------|
| **共有文字基盤** | JP/KR/ZH は「藝/艺」の文字を文化圏で共有; ES "arte" と EN "art" はラテン語源を共有 |
| **美術と工芸の境界** | EN は厳密に区別; CJK 文化は工芸 (茶道, 書道) を高等芸術として扱う |
| **書道の地位** | CN/JP/KR は書道を主要芸術形式として扱う; ES/EN は装飾的または趣味と見る |
| **伝統衣装復活** | 漢服 (CN), 韓服 (KR), 着物 (JP) は現代復活運動; ES/EN は同等の現代民族衣装なし |
| **墨絵伝統** | CJK は筆・墨の伝統を共有; ES は "tinta china" あり; EN は同等の文化的実践なし |

---

## 学習者決定ガイド

> **美術 essentials**:
> - 美術: arte / 美術(bijutsu) / 미술(misul) / 美术(měishù)
> - 絵画: pintura / 絵画(kaiga) / 회화(hoehwa) / 绘画(huìhuà)
> - 彫刻: escultura / 彫刻(chōkoku) / 조각(jogak) / 雕塑(diāosù)
> - 書道: caligrafía / 書道(shodō) / 서예(seoye) / 书法(shūfǎ)
> - 美術館: galería / 美術館(bijutsukan) / 미술관(misulgwan) / 美术馆(měishùguǎn)

---

## 🇯🇵 日本語学習者ノート (Japanese Learner Notes)

> 本セクションは日本語學習者向けの追加学習ガイドです。

### 日本語話者が他の4言語の美術用語を学ぶ際の一般的な落とし穴

1. **「書道」の他言語訳の難しさ**:
   - 日本語の「書道」は単なる "calligraphy" ではなく、精神的修養を含む芸術形式。
   - **落とし穴**: 英語 "calligraphy" = 装飾筆記術 vs 日本語の「書道」= 芸術。
   - **練習法**: 英語で説明時は "Japanese calligraphy as a meditative art form" と補足。

2. **「美術」と「工芸」の境界**:
   - 日本語は「美術 (fine art)」と「工芸 (crafts)」を区別するが、茶道・華道など工芸を芸術として扱う。
   - **落とし穴**: 英語では "craft" はやや低く見られるが、日本語では工芸品は美術品と同格。
   - **練習法**: 英語話者に日本の伝統工芸を紹介する際 "fine craft" や "artisan craft" を使用。

3. **画材名の発音**:
   - 日本語は外来語 (キャンバス, パレット, ブラシ) と和製語 (筆, 絵具) が混在。
   - **練習法**: 外来語は英語発音に近く、和製語は漢字音読み。

4. **文化衣装の漢字**:
   - 日本語「着物」、中国語「和服」、韓国語「기모노」 → 言語により呼び名が異なる。
   - **練習法**: 各言語の呼び方を暗記; 観光案内では相手の言語の名称を使用。

5. **美術館・博物館の区別**:
   - 日本語「美術館 (art museum)」 vs 「博物館 (general museum)」 → 英語圏でも "art gallery" (展示・販売) と "museum" の区別あり。
   - **練習法**: 訪問前に施設のタイプを確認。

### 関連日本語ウィキページ

- [Japanese/vocabulary/art-vocabulary] — 日本語美術語彙
- [Japanese/culture/japanese-traditional-arts] — 日本の伝統芸術
- [Japanese/culture/japanese-craft-traditions] — 日本の工芸伝統
- [Japanese/vocabulary/kanji-vocabulary] — 書道関連漢字
- [Japanese/expressions/art-expressions] — 美術関連表現

### 学習ワークフロー推奨

1. **基本美術用語50語彙** (5言語対訳表)
2. **伝統工芸テーマ別学習** (陶磁器、漆器、織物、書道)
3. **美術館訪問ロールプレイ** (展示案内、チケット購入)
4. **自国の伝統工芸紹介** (5言語で自国の伝統工芸を紹介)
5. **芸術家名鑑** (有名な画家・彫刻家を5言語で)

---

## 関連ページ

- `[[clothing-fashion-comparison]]` — 伝統衣装
- `[[entertainment-pop-culture-comparison]]` — ポピュラーカルチャーの中の芸術
- `[[literature-genres-comparison]]` — 視覚 + 文学芸術
- `[[colors-comparison]]` — 美術における色

## 出典

- Per-language art vocabulary drawn from standard art history references
- All five language wikis: art theme not yet ingested — see per-language wiki for related vocabulary

---

**原文 (英語)**: [[art-crafts-comparison]] | **関連ミラー**: [[art-crafts-comparison.es|スペイン語]] · [[art-crafts-comparison.ko|韓国語]] · [[art-crafts-comparison.zh|中国語]] | **ポリシー**: ADR-0006