# 音乐 — 跨语言对比 (中文版)

> 原文: [[music-comparison]] (English) | 撰写日期: 2026-08-19 | ADR-0006
> **5种语言乐器/流派/音乐术语对比** — English · Spanish · Japanese · Korean · Chinese

---

## 速查表

### 乐器

| 乐器 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **钢琴** | Piano | Piano | ピアノ (piano) | 피아노 (piano) | 钢琴 (gāngqín) |
| **小提琴** | Violin | Violín | バイオリン (baiorin) | 바이올린 (baiollin) | 小提琴 (xiǎotíqín) |
| **吉他** | Guitar | Guitarra | ギター (gitā) | 기타 (gita) | 吉他 (jítā) |
| **鼓** | Drums | Batería / Tambor | ドラム (doramu) | 드럼 (deoreom) | 鼓 (gǔ) / 架子鼓 |
| **长笛** | Flute | Flauta | フルート (furūto) | 플루트 (peulluteu) | 长笛 (chángdí) |
| **萨克斯** | Saxophone | Saxofón | サクソフォーン | 색소폰 (saekseupon) | 萨克斯 (sàkèsī) |
| **小号** | Trumpet | Trompeta | トランペット (toranpetto) | 트럼펫 (teureompæt) | 小号 (xiǎohào) |
| **二胡 (中)** | Erhu / Chinese fiddle | Erhu | 二胡 (niko) | 어호 (eoho) | 二胡 (èrhú) |
| **三味线 (日)** | Shamisen | Shamisen | 三味線 (shamisen) | 샤미센 (syamisen) | 三味线 (sānmèixiàn) |
| **伽倻琴 (韩)** | Gayageum | Gayageum | 伽倻琴 (kayakin) | 가야금 (gayageum) | 伽倻琴 (jiāyēqín) |

### 音乐流派

| 流派 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **流行** | Pop | Pop | ポップス (poppusu) | 팝 (pap) | 流行音乐 (liúxíng yīnyuè) |
| **摇滚** | Rock | Rock | ロック (rokku) | 록 (rok) | 摇滚 (yáogǔn) |
| **爵士** | Jazz | Jazz | ジャズ (jazu) | 재즈 (jaejeu) | 爵士乐 (juéshìyuè) |
| **古典** | Classical | Música clásica | クラシック (kurashikku) | 클래식 (keullaesik) | 古典音乐 (gǔdiǎn yīnyuè) |
| **嘻哈** | Hip-Hop | Hip-Hop | ヒップホップ (hippu hoppu) | 힙합 (hiphap) | 嘻哈 (xīhā) |
| **电子** | Electronic | Electrónica | エレクトロニック | 일렉트로닉 (illekteulonik) | 电子音乐 (diànzǐ yīnyuè) |
| **民谣** | Folk | Folclore / Folclórica | フォーク (fōku) | 포크 (pokeu) | 民谣 (mínyáo) |
| **K-Pop/J-Pop/C-Pop** | K-Pop / J-Pop / C-Pop | K-Pop / J-Pop / C-Pop | J-Pop (ジェーポップ) | K-Pop (케이팝) | C-Pop (华语流行) |

### 音乐理论

| 概念 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **音符** | Note | Nota | 音符 (onpu) | 음표 (eumpyo) | 音符 (yīnfú) |
| **旋律** | Melody | Melodía | 旋律 (senritsu) | 멜로디 (mellodi) | 旋律 (xuánlǜ) |
| **和声** | Harmony | Armonía | 和音 (waon) / ハーモニー | 하모니 (hamoni) | 和声 (héshēng) |
| **节奏** | Rhythm | Ritmo | リズム (rizumu) | 리듬 (rideum) | 节奏 (jiézòu) |
| **速度** | Tempo | Tempo | テンポ (tenpo) | 템포 (taempo) | 速度 (sùdù) |
| **拍子** | Beat | Compás | ビート (bīto) | 비트 (biteu) | 拍子 (pāizi) |
| **音阶** | Scale | Escala | 音階 (onkai) | 음계 (eumgye) | 音阶 (yīnjiē) |
| **和弦** | Chord | Acorde | コード (kōdo) | 코드 (kodeu) | 和弦 (héxián) |

### 音乐产业

| 词汇 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **歌** | Song | Canción | 曲 (kyoku) / 歌 (uta) | 노래 (norae) / 곡 (gok) | 歌 (gē) / 歌曲 (gēqǔ) |
| **专辑** | Album | Álbum | アルバム (arubamu) | 앨범 (aelbeom) | 专辑 (zhuānjí) |
| **歌手** | Singer | Cantante | 歌手 (kashu) | 가수 (gasu) | 歌手 (gēshǒu) |
| **作曲家** | Composer | Compositor | 作曲家 (sakkyokuka) | 작곡가 (jakgokga) | 作曲家 (zuòqǔjiā) |
| **音乐会** | Concert | Concierto | コンサート (konsāto) | 콘서트 (konseoteu) | 音乐会 (yīnyuèhuì) |
| **歌词** | Lyrics | Letra | 歌詞 (kashi) | 가사 (gasa) | 歌词 (gēcí) |
| **乐队** | Band | Banda | バンド (bando) | 밴드 (baendeu) | 乐队 (yuèduì) |
| **管弦乐队** | Orchestra | Orquesta | オーケストラ (ōkesutora) | 오케스트라 (okeseuteura) | 管弦乐队 (guǎnxián yuèduì) |

---

## 各语言详情

### 🇬🇧 英语 (English)
- **关键词**: "Pop" (popular), "Classical" (欧洲艺术音乐), "Folk" (传统); "songwriter" vs "composer"
- **模式**: 大量借用流派名称; 英语是音乐术语的通用语
- **来源**: N/A — 任何语言 wiki 暂无音乐主题

### 🇪🇸 西班牙语 (Spanish)
- **关键词**: "Música" (音乐), "Canción" (歌曲), "Banda" (乐队); "Folclore" / "Folclórica" 因国家而异
- **模式**: Flamenco, salsa, tango, reggaetón 是不同地区传统; "música" 是阴性名词
- **来源**: N/A — 西语 wiki 暂无显式音乐主题

### 🇯🇵 日语 (Japanese)
- **关键词**: 音楽 (ongaku = 音乐); J-Pop, J-Rock, Enka (演歌 = 传统日本民谣); Vocaloid (ボカロ)
- **模式**: おんがく 是汉字词; 借词 (片假名) 主导现代流派; 歌 (uta) for song
- **来源**: N/A — 日语 wiki 暂无显式音乐主题

### 🇰🇷 韩语 (Korean)
- **关键词**: 음악 (eumak = 音乐); K-Pop, K-Indie, 트로트 (teuroteu = 韩国传统流行); 아이돌 (aidorul = 偶像)
- **模式**: 음악 是汉字词; 借词 (K-Pop, 댄스) 与固有词 (노래 norae = 歌曲) 共存
- **来源**: N/A — 韩语 wiki 暂无显式音乐主题

### 🇨🇳 中文 (Chinese)
- **关键词**: 音乐 (yīnyuè); C-Pop, Mandopop, Cantopop (粤语流行); 民乐 (mínyuè = 传统中国音乐)
- **模式**: 古风 (gǔfēng) = 古风现代音乐; 地区风格 (粤 Yue, 沪 Hu); 乐 是多音字 (yuè = 音乐, lè = 快乐)
- **来源**: N/A — 中文 wiki 暂无显式音乐主题

---

## 关键对比 (综合)

| 对比 | 洞察 |
|------|------|
| **传统乐器** | 每种文化有自己标志性的弦乐器: 二胡 (中)、三味线 (日)、伽倻琴 (韩); 西班牙有吉他; 英语国家无文化独特 |
| **借词 vs 固有词** | 现代流派 (rock, jazz, pop) 在 5 种语言都是借词; 传统形式使用本土词汇 (演歌, 트로트, 民乐) |
| **音乐与语言的音高** | 中韩语音调/音高更敏感 (声调/音高重音语言); 可能有助于绝对音感感知 |
| **音乐作为文化出口** | K-Pop 和 J-Pop 是有意识的国家出口; "韩流" (한류 / 韩流) 指韩国浪潮; C-Pop 较少全球包装 |
| **合成结构** | CJK 语言用 2 字合成 (音乐, 음악, 音楽) 共享汉字/hanja/kanji 根; 西/英用拉丁/盎格鲁根 |

---

## 速查卡

> **音乐精华**:
> - 音乐: música / 音楽(ongaku) / 음악(eumak) / 音乐(yīnyuè)
> - 歌: canción / 歌(uta) / 노래(norae) / 歌(gē)
> - 歌手: cantante / 歌手(kashu) / 가수(gasu) / 歌手(gēshǒu)
> - 钢琴: piano / ピアノ / 피아노 / 钢琴(gāngqín)

---

## 相关页面

- `[[entertainment-pop-culture-comparison]]` — 流行文化中的音乐
- `[[literature-media]]` — 音乐 + 媒体
- `[[literature-genres-comparison]]` — 音乐相关创意流派
- `[[tech-internet]]` — 流媒体与数字音乐

## 来源

- 各语言音乐词汇来自通用音乐术语参考
- 5个语言 wiki: 音乐主题尚未摄取 — 见各语言 wiki 相关词汇

---

## 🇨🇳 中文学习者笔记 (Chinese Learner Notes)

> 本节是面向中文母语学习者的额外学习指南。

### 中文母语者在学习其他4种语言音乐时的常见陷阱

1. **汉字桥梁导致乐器名称混淆**:
   - 中文音乐词汇与日韩大量共享汉字 (例: 音乐/音楽/음악, 歌/歌/노래) → 学员以为读音相近。
   - **陷阱**: 韩语 음악 (eumak) 与中文 "音乐" (yīnyuè) 同字不同音; 日语 音楽 (ongaku) 与中文发音差异巨大。
   - **训练法**: 利用汉字桥梁先理解概念, 然后严格训练读音 — 不要假设同汉字 = 同读音。

2. **乐器借词的标准化**:
   - 中文 钢琴/小提琴/吉他 都是规范译名 → 学员假设其他语言也用规范译名。
   - **陷阱**: 日语 ピアノ/ヴァイオリン/ギター 直接音译; 韩语 피아노/바이올린/기타 直接音译; 西语 piano/violín/guitarra 来自拉丁。
   - **训练法**: 记忆每种语言乐器的"原产+译名" — 中文是意译, 日韩多音译, 西语来自拉丁。

3. **传统乐器的"单字+单字"误读**:
   - 中文 二胡/三味线/伽倻琴 → 学员假设其他语言也有对应单字。
   - **陷阱**: 二胡 在日语 = 二胡 (niko, 音译); 日语 三味线 在中文 = 三味线 (音译); 韩语 가야금 在中文 = 伽倻琴 (意译)。
   - **训练法**: 记忆每种传统乐器的"原产+译名" — 跨文化可能使用音译或意译。

4. **流行文化输出词汇**:
   - 中国 K-Pop/J-Pop 表达普及 → 学员假设其他语言也有相同语言。
   - **陷阱**: 韩语 케이팝/韩剧/한드; 日语 韓ドラ/アニメ; 英语 K-Pop/J-Pop/C-Pop (国际通用)。
   - **训练法**: 记忆每种语言流行文化的"本地化"表达 — 不要直接将中文术语翻译。

5. **音乐理论术语的差异**:
   - 中文音乐理论术语 (音阶/和弦/节奏) → 学员假设其他语言对应。
   - **陷阱**: 日语 コード (kōdo) = chord (音译); 韩语 코드 (kodeu) (音译); 西语 acorde (意译); 英语 chord (本土)。
   - **训练法**: 区分 "音乐理论" vs "音乐表演" — 理论术语多来自西方, 表演术语多本土化。

### 相关中文维基页面

- [Chinese/vocabulary/music-zh] — 中文音乐词汇
- [Chinese/culture/chinese-music-zh] — 中文音乐文化
- [Chinese/sources/pinyin-basics-zh] — 中文拼音基础
- [Chinese/vocabulary/basic-vocabulary-zh] — 中文基础词汇
- [Chinese/grammar/basic-particles] — 中文基本助词

### 学习工作流程推荐

1. **背诵对比表** (乐器/流派/理论)
2. **乐器类型区分** (键盘/弦乐/打击乐/吹奏乐)
3. **传统乐器学习** (各文化标志性乐器 + 跨文化名称)
4. **流行音乐流派** (K-Pop/J-Pop/C-Pop 当地表达)
5. **实用音乐场景** (点歌/听音乐会/讨论喜欢的歌手)

---

**原文 (英语)**: [[music-comparison]] | **相关镜像**: [[music-comparison.es|西班牙语]] · [[music-comparison.ja|日语]] · [[music-comparison.ko|韩语]] | **政策**: ADR-0006
