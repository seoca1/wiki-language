# 음악 — 다국어 비교 (한국어판)

> 원본: [[music-comparison]] (English) | 작성일: 2026-08-20 | ADR-0006
> **5개 언어 음악 어휘 비교 — 악기, 장르, 음악 이론, 음악 산업**

---

## 빠른 참조 표

### 악기

| 악기 | English | Spanish | Japanese | Korean | Chinese |
|------------|---------|---------|----------|--------|---------|
| **피아노** | Piano | Piano | ピアノ (piano) | 피아노 (piano) | 钢琴 (gāngqín) |
| **바이올린** | Violin | Violín | バイオリン (baiorin) | 바이올린 (baiollin) | 小提琴 (xiǎotíqín) |
| **기타** | Guitar | Guitarra | ギター (gitā) | 기타 (gita) | 吉他 (jítā) |
| **드럼** | Drums | Batería / Tambor | ドラム (doramu) | 드럼 (deoreom) | 鼓 (gǔ) / 架子鼓 |
| **플루트** | Flute | Flauta | フルート (furūto) | 플루트 (peulluteu) | 长笛 (chángdí) |
| **색소폰** | Saxophone | Saxofón | サクソフォーン | 색소폰 (saekseupon) | 萨克斯 (sàkèsī) |
| **트럼펫** | Trumpet | Trompeta | トランペット (toranpetto) | 트럼펫 (teureompæt) | 小号 (xiǎohào) |
| **어호 (중국)** | Erhu / Chinese fiddle | Erhu | 二胡 (niko) | 어호 (eoho) | 二胡 (èrhú) |
| **샤미센 (일본)** | Shamisen | Shamisen | 三味線 (shamisen) | 샤미센 (syamisen) | 三味线 (sānmèixiàn) |
| **가야금 (한국)** | Gayageum | Gayageum | 伽倻琴 (kayakin) | 가야금 (gayageum) | 伽倻琴 (jiāyēqín) |

### 음악 장르

| 장르 | English | Spanish | Japanese | Korean | Chinese |
|-------|---------|---------|----------|--------|---------|
| **팝** | Pop | Pop | ポップス (poppusu) | 팝 (pap) | 流行音乐 (liúxíng yīnyuè) |
| **록** | Rock | Rock | ロック (rokku) | 록 (rok) | 摇滚 (yáogǔn) |
| **재즈** | Jazz | Jazz | ジャズ (jazu) | 재즈 (jaejeu) | 爵士乐 (juéshìyuè) |
| **클래식** | Classical | Música clásica | クラシック (kurashikku) | 클래식 (keullaesik) | 古典音乐 (gǔdiǎn yīnyuè) |
| **힙합** | Hip-Hop | Hip-Hop | ヒップホップ (hippu hoppu) | 힙합 (hiphap) | 嘻哈 (xīhā) |
| **일렉트로닉** | Electronic | Electrónica | エレクトロニック | 일렉트로닉 (illekteulonik) | 电子音乐 (diànzǐ yīnyuè) |
| **포크** | Folk | Folclore / Folclórica | フォーク (fōku) | 포크 (pokeu) | 民谣 (mínyáo) |
| **K-Pop/J-Pop/C-Pop** | K-Pop / J-Pop / C-Pop | K-Pop / J-Pop / C-Pop | J-Pop (ジェーポップ) | K-Pop (케이팝) | C-Pop (华语流行) |

### 음악 이론

| 개념 | English | Spanish | Japanese | Korean | Chinese |
|---------|---------|---------|----------|--------|---------|
| **음표** | Note | Nota | 音符 (onpu) | 음표 (eumpyo) | 音符 (yīnfú) |
| **멜로디** | Melody | Melodía | 旋律 (senritsu) | 멜로디 (mellodi) | 旋律 (xuánlǜ) |
| **하모니** | Harmony | Armonía | 和音 (waon) / ハーモニー | 하모니 (hamoni) | 和声 (héshēng) |
| **리듬** | Rhythm | Ritmo | リズム (rizumu) | 리듬 (rideum) | 节奏 (jiézòu) |
| **템포** | Tempo | Tempo | テンポ (tenpo) | 템포 (taempo) | 速度 (sùdù) |
| **비트** | Beat | Compás | ビート (bīto) | 비트 (biteu) | 拍子 (pāizi) |
| **음계** | Scale | Escala | 音階 (onkai) | 음계 (eumgye) | 音阶 (yīnjiē) |
| **코드** | Chord | Acorde | コード (kōdo) | 코드 (kodeu) | 和弦 (héxián) |

### 음악 산업

| 단어 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **노래** | Song | Canción | 曲 (kyoku) / 歌 (uta) | 노래 (norae) / 곡 (gok) | 歌 (gē) / 歌曲 (gēqǔ) |
| **앨범** | Album | Álbum | アルバム (arubamu) | 앨범 (aelbeom) | 专辑 (zhuānjí) |
| **가수** | Singer | Cantante | 歌手 (kashu) | 가수 (gasu) | 歌手 (gēshǒu) |
| **작곡가** | Composer | Compositor | 作曲家 (sakkyokuka) | 작곡가 (jakgokga) | 作曲家 (zuòqǔjiā) |
| **콘서트** | Concert | Concierto | コンサート (konsāto) | 콘서트 (konseoteu) | 音乐会 (yīnyuèhuì) |
| **가사** | Lyrics | Letra | 歌詞 (kashi) | 가사 (gasa) | 歌词 (gēcí) |
| **밴드** | Band | Banda | バンド (bando) | 밴드 (baendeu) | 乐队 (yuèduì) |
| **오케스트라** | Orchestra | Orquesta | オーケストラ (ōkesutora) | 오케스트라 (okeseuteura) | 管弦乐队 (guǎnxián yuèduì) |

---

## 핵심 대조 (종합)

| 대조 | 통찰 |
|----------|---------|
| **전통 악기** | 각 문화는 고유 현악기 보유: erhu (CN), shamisen (JP), gayageum (KR); 스페인 기타, 영어는 문화적 고유 없음 |
| **차용어 vs 고유어** | 현대 장르 (rock, jazz, pop)는 5개 언어 모두 차용어; 전통 장르는 고유 어휘 (演歌, 트로트, 民乐) |
| **음악과 언어의 피치** | ZH/KR 화자는 피치 미묘함에 더 민감 (성조/피치 액센트 언어); 절대음 인식에 유리 |
| **문화 수출로서 음악** | K-Pop과 J-Pop은 의도적 국가 수출; "한류 (한류 / 韩流)" = Korean Wave; C-Pop 덜 글로벌 패키지 |
| **복합어 구조** | CJK는 2자 한자 복합어 (音乐, 음악, 音楽) — 한자/한자/간지 어원 공유; ES/EN는 라틴/앵글로 어원 |

---

## 학습자 의사결정 가이드

> **음악 필수 어휘**:
> - Music: música / 音楽(ongaku) / 음악(eumak) / 音乐(yīnyuè)
> - Song: canción / 歌(uta) / 노래(norae) / 歌(gē)
> - Singer: cantante / 歌手(kashu) / 가수(gasu) / 歌手(gēshǒu)
> - Piano: piano / ピアノ / 피아노 / 钢琴(gāngqín)

> **전통 악기 매핑**:
> - 한국: 가야금, 거문고, 아쟁, 해금
> - 일본: 샤미센, 고토, 시타코토
> - 중국: 어호, 고쟁, 비파, 루
> - 스페인: 기타, 카ホン, 깜파나, 플라멩코 기타
> - 영어권: 없음 (모두 차용)

---

## 🇰🇷 한국어 학습자 노트 (Korean Learner Notes)

> 본 섹션은 한국어 학습자 대상의 추가 학습 가이드입니다.

### 한국어 화자가 다른 4개 언어 음악 어휘를 학습할 때 흔히 마주치는 함정

1. **한자 음악 어휘 발음 차이**:
   - 같은 한자 음악 어휘가 한국어/일본어/중국어에서 발음 다름. 예: 音楽: 한국 "음악 (eumak)" vs 일본 "おんがく (ongaku)" vs 중국 "yīnyuè".
   - **함정**: 한국 한자음으로 일본어/중국어 음악 어휘 발음 추정 → 의사소통 실패. 예: 가수(singer) 한국 "가수" vs 일본 "かしゅ (kashu)" vs 중국 "gēshǒu" — 완전히 다름.
   - **훈련법**: 음악 한자 30자 한자어 — 한국 한자음 + 일본 음(음독) + 중국 병음 별도 매트릭스. 한자 1글자 = 3개국 발음.

2. **한국어 음악 어휘의 한자어 vs 고유어 혼재**:
   - 한국어: "음악 (한자어)" + "노래 (고유어)" / "가수 (한자어)" + "성악가 (한자어)" 등 혼재.
   - **함정**: 일본어/중국어 학습자가 모든 어휘를 한자로 매핑 → 고유어 "노래" 한자 매핑 실패. "노래"는 한자 歌, 중국어 "gē"와 일본어 "うた (uta)"는 같은 한자 歌지만 한국어 "노래"는 고유어.
   - **훈련법**: 음악 어휘 고유어/한자어 분리 — 노래(고유어) vs 歌(가, 한자어) vs 음악(음악, 한자어) vs 音(음, 한자어). 한자 매핑 가능 여부 사전 확인.

3. **K-Pop 산업 어휘의 한국 고유성**:
   - K-Pop 관련 어휘 (아이돌, 팬, 최애, 원픽, 덕질, 컴백, 팬미팅)는 한국 고유어 또는 한국에서 만들어진 차용어.
   - **함정**: "최애 (choeae, bias)"를 다른 4개 언어에서 동일 어휘로 사용 — 한국어 고유어이므로 다른 언어에서 다른 표현 (일본 お気に入り/推し, 중국 本命, 영어 favorite/bias).
   - **훈련법**: K-Pop 산업 어휘의 한국 고유성 인지 — 영어 "idol", "fan", "comeback"이 차용어로 들어왔지만 "최애/원픽"은 한국어 고유. K-Pop/J-Pop 어휘 비교 학습.

4. **트로트 (Trot) 한국 고유 장르**:
   - 트로트 (teuroteu)는 한국에서 발전한 대중가요 장르. 일본 엔카(演歌)와 비슷하지만 다른 발전.
   - **함정**: 트로트를 일본 엔카와 동일시 → 문화적 차이 손실. 트로트는 한국 전쟁 후 등장, 엔카는 메이지 시대부터.
   - **훈련법**: 트로트 vs 엔카 vs 중국 民族音乐(민족 음악) — 동아시아 전통 대중가요 비교. 트로트의 한국어 가사 vs 엔카의 일본어 가사 비교.

5. **음악 어휘의 한자 + 외래어 혼재**:
   - 한국어: "클래식 (한자어 차용)" + "팝 (영어 차용)" + "가요 (한자어)" / "노래 (고유어)" / "댄스 (영어 차용)" 등.
   - **함정**: 음악 장르 어휘의 어원 추적 어려움. 예: "팝"은 영어 "pop" 차용, "클래식"은 한자어, "트로트"는 한국 고유, "아이돌"은 영어 차용 + 한국 한자어 "偶像" 매핑 시도.
   - **훈련법**: 음악 어휘 어원 분류 — 영어 차용 (팝, 록, 재즈, 힙합, 일렉트로닉, 포크, 콘서트, 밴드, 앨범, 싱글, EP, 코드, 비트, 멜로디, 하모니, 리듬, 템포) vs 한자어 (음악, 노래曲, 가수, 작곡가, 악기, 음표) vs 고유어 (노래, 가락, 소리, 흥얼거리다) vs 한국 고유 (트로트, 아이돌, 팬미팅, 덕질).

### 학습 전략

1. **우선순위 1**: 음악 한자 한자어 30자 한자 동시 학습 — 音楽/音楽/yīnyuè, 歌/가/gē, 歌手/가수/gēshǒu, 曲/곡/qǔ, 音符/음표/yīnfú, 旋律/선율/xuánlǜ, 和音/하음/héyīn. 한자 1글자 = 3개국 발음 학습.
2. **우선순위 2**: 한국어 음악 어휘의 고유어/한자어/외래어 분류 — 노래(고유어) vs 歌(가, 한자어) vs 음악(음악, 한자어) vs pop(팝, 영어). 한자 매핑 가능 어휘 vs 불가 어휘 분리.
3. **우선순위 3**: K-Pop/J-Pop/C-Pop 산업 어휘 비교 — 한국 "아이돌/팬/최애/원픽" vs 일본 "アイドル/推し/ファン" vs 중국 "偶像/粉丝/本命" vs 영어 "idol/fan/bias". K-Pop 산업 용어의 한국 고유성 학습.
4. **우선순위 4**: 동아시아 전통 악기 비교 — 한국 가야금 vs 일본 샤미센 vs 중국 어호. 문화적 배경과 음색 차이 학습.
5. **우선순위 5**: 전통 대중가요 비교 — 한국 트로트 vs 일본 엔카 vs 중국 민요. 문화적 맥락 + 발원 시기 + 가사 언어 비교.

### 관련 한국어 위키 페이지

-  — K-Pop 산업 용어
- [[literature-media]] — 미디어 + 음악
- [[literature-genres-comparison]] — 장르 어휘
- [[tech-internet]] — 스트리밍/디지털 음악
- [[untranslatable-concepts]] — 매너리즘/감성 어휘

---

## 관련 페이지

- `[[entertainment-pop-culture-comparison]]` — 대중문화 속 음악
- `[[literature-media]]` — 음악 + 미디어
- `[[literature-genres-comparison]]` — 음악 인접 창작 장르
- `[[tech-internet]]` — 스트리밍/디지털 음악

## 출처

- 5개 언어 음악 어휘 일반 음악 용어 참조
- 모든 5개 언어 wiki: 음악 테마 미인제스트 — 관련 어휘는 per-language wiki 참조

---

**원본 (영어)**: [[music-comparison]] | **관련 미러**: [[music-comparison.es|Spanish]] · [[music-comparison.ja|Japanese]] · [[music-comparison.zh|Chinese]] | **정책**: ADR-0006
