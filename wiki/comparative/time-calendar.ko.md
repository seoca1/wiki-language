# 시간 & 달력 — 다국어 비교 (한국어판)

> 원본: [[time-calendar]] (English) | 작성일: 2026-08-20 | ADR-0006
> **5개 언어 시간/달력 어휘 비교 — 시계 시간, 요일, 월, 상대 시간, 지속, 달력 시스템**

---

## 빠른 참조 표

### 시계 시간

#### 시간 표현 (시 + 분)

| 시간 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **1:00** | one o'clock | la una (en punto) | 一時 (いちじ) | 한 시 (han si) | 一点 (yī diǎn) |
| **2:00** | two o'clock | las dos (en punto) | 二時 (にじ) | 두 시 (du si) | 两点 (liǎng diǎn) |
| **3:00** | three o'clock | las tres (en punto) | 三時 (さんじ) | 세 시 (se si) | 三点 (sān diǎn) |
| **12:00** | twelve o'clock / noon | las doce / mediodía | 十二時 (じゅうにじ) / 正午 (しょうご) | 열두 시 (yeoldu si) / 낮 (nat) | 十二点 (shíèr diǎn) / 中午 (zhōngwǔ) |
| **0:00 / 24:00** | midnight | medianoche | 零時 (れいじ) / 深夜 (しんや) | 자정 (jajeong) / 밤 12시 | 零点 (líng diǎn) / 午夜 (wǔyè) |

#### 분 (분 단위)

| 분 | English | Spanish | Japanese | Korean | Chinese |
|---------|---------|---------|----------|--------|---------|
| **:05** | five past one | la una y cinco | 一時五分 (いちじごふん) | 한 시 오 분 (han si o bun) | 一点零五 (yī diǎn líng wǔ) / 一点五分 |
| **:10** | ten past one | la una y diez | 一時十分 (いちじじゅっぷん) | 한 시 십 분 (han si sip bun) | 一点十分 (yī diǎn shí fēn) |
| **:15** | quarter past one | la una y cuarto | 一時十五分 (いちじじゅうごふん) | 한 시 십오 분 (han si sibo bun) | 一点一刻 (yī diǎn yī kè) / 一点十五分 |
| **:20** | twenty past one | la una y veinte | 一時二十分 (いちじにじゅっぷん) | 한 시 이십 분 (han si isip bun) | 一点二十分 (yī diǎn èrshí fēn) |
| **:30** | half past one | la una y media | 一時半 (いちじはん) | 한 시 반 (han si ban) | 一点半 (yī diǎn bàn) / 一点三十分 |
| **:40** | twenty to two | las dos menos veinte | 一時四十分 (いちじよんじゅっぷん) / 二時二十分前 | 두 시 이십 분 전 (du si isip bun jeon) | 差二十分两点 (chà èrshí fēn liǎng diǎn) / 一点四十分 |
| **:45** | quarter to two | las dos menos cuarto | 一時四十五分 (いちじよんじゅうごふん) / 二時十五分前 | 두 시 십오 분 전 (du si sibo bun jeon) | 差一刻两点 (chà yī kè liǎng diǎn) / 一点四十五分 |
| **:50** | ten to two | las dos menos diez | 一時五十分 (いちじごじゅっぷん) / 二時十分前 | 두 시 십 분 전 (du si sip bun jeon) | 差十分钟两点 (chà shí fēnzhōng liǎng diǎn) / 一点五十分 |
| **:55** | five to two | las dos menos cinco | 一時五十五分 (いちじごじゅうごふん) / 二時五分前 | 두 시 오 분 전 (du si o bun jeon) | 差五分钟两点 (chà wǔ fēnzhōng liǎng diǎn) / 一点五十五分 |

#### 12시간 vs 24시간 형식

| 언어 | 기본 형식 | 24시간 맥락 |
|----------|----------------|-------------|
| **English (US)** | 12h (am/pm) | 군용, 의료, 교통 |
| **English (UK)** | 12h 일반, 24h 증가 | 교통, TV 스케줄, 군용 |
| **Spanish** | 12h 말하기, 24h 쓰기/스케줄 | 시각표, 공식, 군용 |
| **Japanese** | **24시간 표준** (13:00, 23:59) | 12h 캐주얼 음성 with *gozen/gogo* |
| **Korean** | **24시간 표준** (13시, 23시 59분) | 12h with *am/pm* or *오전/오후* in speech |
| **Chinese** | **24시간 표준** (13:00, 23:59) | 12h with *am/pm* or *上午/下午* in speech |

### 요일

| 요일 | English | Spanish | Japanese | Korean | Chinese |
|-----|---------|---------|----------|--------|---------|
| **월요일** | Monday | lunes | 月曜日 (げつようび) | 월요일 (woryoil) | 星期一 (xīngqīyī) / 周一 (zhōuyī) |
| **화요일** | Tuesday | martes | 火曜日 (かようび) | 화요일 (hwayoil) | 星期二 (xīngqī'èr) / 周二 (zhōu'èr) |
| **수요일** | Wednesday | miércoles | 水曜日 (すいようび) | 수요일 (suyoil) | 星期三 (xīngqīsān) / 周三 (zhōusān) |
| **목요일** | Thursday | jueves | 木曜日 (もくようび) | 목요일 (mogyoil) | 星期四 (xīngqīsì) / 周四 (zhōu'èr) |
| **금요일** | Friday | viernes | 金曜日 (きんようび) | 금요일 (geumyoil) | 星期五 (xīngqīwǔ) / 周五 (zhōuwǔ) |
| **토요일** | Saturday | sábado | 土曜日 (どようび) | 토요일 (toyoil) | 星期六 (xīngqīliù) / 周六 (zhōuliù) |
| **일요일** | Sunday | domingo | 日曜日 (にちようび) | 일요일 (iryoil) | 星期日 (xīngqīrì) / 周日 (zhōurì) / 星期天 |

#### 어원 (행성/원소)

| 언어 | 시스템 | 예 |
|----------|--------|---------|
| **English** | 북유럽 신 + 태양/달 | *Mon*day (달), *Tues*day (Tyr), *Wednes*day (Odin), *Thurs*day (Thor), *Fri*day (Frigg), *Satur*day (Saturn), *Sun*day |
| **Spanish** | 로마 신 + 태양/달 | *Lunes* (달), *Martes* (Mars), *Miércoles* (Mercurio), *Jueves* (Júpiter), *Viernes* (Venus), *Sábado* (Sabbat), *Domingo* (Dominus) |
| **Japanese** | 5 원소 + 태양/달 | *Getsu* (달), *Ka* (불), *Sui* (물), *Moku* (나무), *Kin* (금속), *Do* (흙), *Nichi* (태양) |
| **Korean** | 일본어와 동일 (Hanja) | *Wol* (달), *Hwa* (불), *Su* (물), *Mok* (나무), *Geum* (금속), *To* (흙), *Il* (태양) |
| **Chinese** | 번호 매김 (Week = 星期/周) | *Xingqi* (星期) = "별 시기" / *Zhou* (周) = 주기 |

### 월

| 월 | English | Spanish | Japanese | Korean | Chinese |
|-------|---------|---------|----------|--------|---------|
| **1월** | January | enero | 一月 (いちがつ) / 睦月 (むつき) | 일월 (ilwol) / 1월 | 一月 (yīyuè) / 1月 |
| **2월** | February | febrero | 二月 (にがつ) / 如月 (きさらぎ) | 이월 (iwol) / 2월 | 二月 (èryuè) / 2月 |
| **3월** | March | marzo | 三月 (さんがつ) / 弥生 (やよい) | 삼월 (samwol) / 3월 | 三月 (sānyuè) / 3月 |
| **4월** | April | abril | 四月 (しがつ) / 卯月 (うづき) | 사월 (sawol) / 4월 | 四月 (sìyuè) / 4月 |
| **5월** | May | mayo | 五月 (ごがつ) / 皐月 (さつき) | 오월 (owol) / 5월 | 五月 (wǔyuè) / 5月 |
| **6월** | June | junio | 六月 (ろくがつ) / 水無月 (みなづき) | 유월 (yuwol) / 6월 | 六月 (liùyuè) / 6月 |
| **7월** | July | julio | 七月 (しちがつ) / 文月 (ふみづき) | 칠월 (chirwol) / 7월 | 七月 (qīyuè) / 7月 |
| **8월** | August | agosto | 八月 (はちがつ) / 葉月 (はづき) | 팔월 (parwol) / 8월 | 八月 (bāyuè) / 8月 |
| **9월** | September | septiembre | 九月 (くがつ) / 長月 (ながつき) | 구월 (guwol) / 9월 | 九月 (jiǔyuè) / 9月 |
| **10월** | October | octubre | 十月 (じゅうがつ) / 神無月 (かんなづき) | 시월 (siwol) / 10월 | 十月 (shíyuè) / 10月 |
| **11월** | November | noviembre | 十一月 (じゅういちがつ) / 霜月 (しもつき) | 십일월 (sibilwol) / 11월 | 十一月 (shíyīyuè) / 11月 |
| **12월** | December | diciembre | 十二月 (じゅうにがつ) / 師走 (しわす) | 십이월 (sibiwol) / 12월 | 十二月 (shíèryuè) / 12月 |

### 상대 시간 표현

| 표현 | English | Spanish | Japanese | Korean | Chinese |
|------------|---------|---------|----------|--------|---------|
| **지금** | now | ahora | 今 (いま) | 지금 (jigeum) | 现在 (xiànzài) / 如今 (rújīn) |
| **오늘** | today | hoy | 今日 (きょう) | 오늘 (oneul) | 今天 (jīntiān) / 今日 (jīnrì) |
| **내일** | tomorrow | mañana | 明日 (あした/あす/みょうにち) | 내일 (naeil) | 明天 (míngtiān) / 明日 (míngrì) |
| **어제** | yesterday | ayer | 昨日 (きのう/さくじつ) | 어제 (eoje) | 昨天 (zuótiān) / 昨日 (zuórì) |
| **모레** | day after tomorrow | pasado mañana | 明後日 (あさって/みょうごにち) | 모레 (more) | 后天 (hòutiān) / 后日 (hòurì) |
| **그저께** | day before yesterday | anteayer | 一昨日 (おととい/いっさくじつ) | 그저께 (geujeokke) | 前天 (qiántiān) / 前日 (qiánrì) |
| **이번 주** | this week | esta semana | 今週 (こんしゅう) | 이번 주 (ibeon ju) | 这周 (zhè zhōu) / 本周 (běn zhōu) |
| **지난 주** | last week | la semana pasada | 先週 (せんしゅう) | 지난 주 (jinan ju) | 上周 (shàng zhōu) / 上个周 |
| **다음 주** | next week | la semana que viene | 来週 (らいしゅう) | 다음 주 (daeum ju) / 내주 (naeju) | 下周 (xià zhōu) / 下个周 |
| **이번 달** | this month | este mes | 今月 (こんげつ) | 이번 달 (ibeon dal) | 这个月 (zhège yuè) / 本月 (běn yuè) |
| **지난 달** | last month | el mes pasado | 先月 (せんげつ) | 지난 달 (jinan dal) | 上个月 (shàng gè yuè) |
| **다음 달** | next month | el mes que viene | 来月 (らいげつ) | 다음 달 (daeum dal) / 내달 (naedal) | 下个月 (xià gè yuè) |
| **올해** | this year | este año | 今年 (ことし) | 올해 (olhae) / 금년 (geumnyeon) | 今年 (jīnnián) |
| **작년** | last year | el año pasado | 去年 (きょねん) | 작년 (jangnyeon) / 지난해 (jinanhae) | 去年 (qùnián) |
| **내년** | next year | el año que viene | 来年 (らいねん) | 내년 (naenyeon) | 明年 (míngnián) |

### 지속 표현

| 지속 | English | Spanish | Japanese | Korean | Chinese |
|----------|---------|---------|----------|--------|---------|
| **초** | second | segundo | 秒 (びょう) | 초 (cho) | 秒 (miǎo) |
| **분** | minute | minuto | 分 (ふん/ぷん) | 분 (bun) | 分钟 (fēnzhōng) / 分 (fēn) |
| **시간** | hour | hora | 時間 (じかん) | 시간 (sigan) | 小时 (xiǎoshí) / 个钟头 (gè zhōngtóu) |
| **일** | day | día | 日 (にち/ひ/か) / 日間 (にちかん) | 일 (il) / 하루 (haru) | 天 (tiān) / 日 (rì) |
| **주** | week | semana | 週 (しゅう) / 週間 (しゅうかん) | 주 (ju) / 한 주 (han ju) | 周 (zhōu) / 个星期 (gè xīngqī) |
| **달** | month | mes | 月 (つき/げつ) / 月間 (げっかん) | 달 (dal) / 개월 (gaewol) | 月 (yuè) / 个月 (gè yuè) |
| **년** | year | año | 年 (とし/ねん) / 年間 (ねんかん) | 년 (nyeon) / 해 (hae) | 年 (nián) |

### 달력 시스템 & 휴일

| 언어 | 달력 | 비고 |
|----------|----------|-------|
| **English** | 그레고리력 (태양) | 글로벌 표준 |
| **Spanish** | 그레고리력 (태양) | 가톨릭 전례 달력 오버레이 |
| **Japanese** | 그레고리력 (태양) + **와레키** (연호) | 레이와 6 = 2024; 헤이세이, 쇼와, 다이쇼, 메이지 연호 |
| **Korean** | 그레고리력 (태양) + **음력** (음력) | 설날, 추석 음력; 단기 (단기) 연호 드물다 |
| **Chinese** | 그레고리력 (태양) + **음력** (农历) | 춘절, 중추절 음력; 60년 주기 (간지) |

### 날짜 형식

| 언어 | 짧은 형식 | 긴 형식 | 예 (2024-07-19) |
|----------|--------------|-------------|----------------------|
| **English (US)** | MM/DD/YYYY | Month DD, YYYY | 07/19/2024 / July 19, 2024 |
| **English (UK)** | DD/MM/YYYY | DD Month YYYY | 19/07/2024 / 19 July 2024 |
| **Spanish** | DD/MM/YYYY | DD de Month de YYYY | 19/07/2024 / 19 de julio de 2024 |
| **Japanese** | YYYY/MM/DD | YYYY年MM月DD日 | 2024/07/19 / 2024年7月19日 (令和6年7月19日) |
| **Korean** | YYYY.MM.DD | YYYY년 MM월 DD일 | 2024.07.19 / 2024년 7월 19일 |
| **Chinese** | YYYY/MM/DD | YYYY年MM月DD日 | 2024/07/19 / 2024年7月19日 |

### 계절

| 계절 | English | Spanish | Japanese | Korean | Chinese |
|--------|---------|---------|----------|--------|---------|
| **봄** | spring | primavera | 春 (はる) | 봄 (bom) | 春 (chūn) / 春天 (chūntiān) |
| **여름** | summer | verano | 夏 (なつ) | 여름 (yeoreum) | 夏 (xià) / 夏天 (xiàtiān) |
| **가을** | autumn / fall | otoño | 秋 (あき) | 가을 (ga-eul) | 秋 (qiū) / 秋天 (qiūtiān) |
| **겨울** | winter | invierno | 冬 (ふゆ) | 겨울 (gyeoul) | 冬 (dōng) / 冬天 (dōngtiān) |

### 학습자 의사결정 가이드

| 필요한 표현 | EN | ES | JP | KR | CH |
|----------------|----|----|-----|----|----|
| **"지금 몇 시예요?"** | What time is it? | ¿Qué hora es? | 今何時ですか？ (Ima nanji desu ka?) | 지금 몇 시예요? (Jigeum myeot si-yeyo?) | 现在几点? (Xiànzài jǐ diǎn?) |
| **"3시 반이에요"** | It's three thirty. | Son las tres y media. | 三時半です (Sanji han desu) | 세 시 반이에요 (Se si ban-ieyo) | 三点半 (Sān diǎn bàn) |
| **"내일 봐요"** | See you tomorrow. | Nos vemos mañana. | また明日 (Mata ashita) | 내일 봐요 (Naeil bwayo) | 明天见 (Míngtiān jiàn) |
| **"오늘 무슨 요일이에요?"** | What day is it? | ¿Qué día es hoy? | 今日は何曜日？ (Kyou wa nan youbi?) | 오늘 무슨 요일이에요? (Oneul museun yoil-ieyo?) | 今天星期几? (Jīntiān xīngqī jǐ?) |
| **"다음 주"** | next week | la semana que viene | 来週 (Raishuu) | 다음 주 (Daeum ju) | 下周 (Xià zhōu) |
| **"지난 달"** | last month | el mes pasado | 先月 (Sengetsu) | 지난 달 (Jinan dal) | 上个月 (Shàng gè yuè) |
| **"이틀 후"** | in two days | dentro de dos días | 二日後 (Futsuka go) | 이틀 후 (It-eul hu) | 两天后 (Liǎng tiān hòu) |
| **"사흘 전"** | three days ago | hace tres días | 三日前 (Mikka mae) | 사흘 전 (Saheul jeon) | 三天前 (Sān tiān qián) |
| **"하루 종일"** | all day | todo el día | 一日中 (Ichinichijuu) | 종일 (Jongil) / 하루 종일 | 一整天 (Yī zhěng tiān) |
| **"매일"** | every day | todos los días | 毎日 (Mainichi) | 매일 (Maeil) | 每天 (Měitiān) |
| **"일주일에 한 번"** | once a week | una vez a la semana | 週1回 (Shuu ikkai) | 주 1회 (Ju 1-hoe) | 一周一次 (Yī zhōu yī cì) |

---

## 🇰🇷 한국어 학습자 노트 (Korean Learner Notes)

> 본 섹션은 한국어 학습자 대상의 추가 학습 가이드입니다.

### 한국어 화자가 다른 4개 언어 시간/달력을 학습할 때 흔히 마주치는 함정

1. **시간 한자 한자어 발음 차이**:
   - 같은 한자 시간 어휘가 한국어/일본어/중국어에서 발음 다름. 예: 時間: 한국 한자음 "시간" vs 일본 "じかん (jikan)" vs 중국 "shíjiān".
   - **함정**: 한국어 한자음 "시간" / "분" / "초" 다른 4개 언어 발음 추정 → "jikan" / "fēnzhōng" / "miǎo" 와 다름.
   - **훈련법**: 시간 한자 한자어 3개국 발음 매트릭스 — 時間/시간/shíjiān, 分/분/fēnzhōng, 秒/초/miǎo. 한자 1글자 = 3개국 발음.

2. **24시간 vs 12시간 형식**:
   - 한국/일본/중국: 24시간 표준 (13시, 14시, 23시). 한국어 "오후 1시" (12h) 또는 "13시" (24h) 모두 가능.
   - 미국: 12시간 표준 (1:00 PM, 2:00 PM). 영국/스페인: 12h 일반, 24h 증가.
   - **함정**: 한국어 학습자가 미국 비즈니스 미팅 시간 1:00 PM = 정오 또는 오후 1시? = 13:00 (오후 1시) → PM = 오후.
   - **훈련법**: 시간 형식 매트릭스 — KR/JP/CH 24시간 기본, EN 12시간 기본. **12h/24h 변환 표 학습**.

3. **요일 한자 한자어 5개 원소 공유**:
   - 한국어/일본어: 요일 = 5개 원소 (월/화/수/목/금 = 5개 원소) + 토/일 (흙/태양). 한자 한자어.
   - 한국어 한자음: 월요일 (Woryoil) vs 일본 ごようび (Getsuyoubi) vs 중국 星期一 (Xīngqīyī). **한자 일요일 vs 일 vs day** 발음 다름.
   - 스페인어 lunes/martes/.../domingo = 라틴/로마 신. 영어 Monday/Tuesday = 북유럽 신.
   - **함정**: 한국어 학습자가 영어 Monday 단순 매핑 → 스페인어 lunes, 일본어 getsuyoubi. **요일 어원 시스템 다름**.
   - **훈련법**: 요일 5개 언어 매트릭스 — KR/JP 한자 한자어 5원소, ES 로마 신, EN 북유럽 신, CH 数字 (번호). **5개 어원 시스템 비교**.

4. **"내일/모레/그저께" 의 한국어 고유 시간 표현**:
   - 한국어: 오늘/내일/모레/글피 (= 3일 후) / 어제/그저께/그끄저께 (= 3일 전). **순우리말**.
   - 스페인어: hoy/mañana/pasado mañana/anteayer. 일부 라틴.
   - 영어: today/tomorrow/day after tomorrow/yesterday/day before yesterday. 게르만.
   - **함정**: 한국어 학습자가 다른 4개 언어에 "모레/글피" 단순 매핑 → 영어 "day after tomorrow" / "in 3 days" — 매핑 OK이나 한자 매핑 안 됨.
   - **훈련법**: 한국어 시간 어휘 매트릭스 — 고유어 (오늘, 내일, 모레) vs 한자어 (금년, 작년, 내년). **순우리말 vs 한자어 분리**.

5. **음력/양력 통합의 한국어/중국어/일본어**:
   - 한국: 양력 + 음력 (설날, 추석). 일본: 양력 + 연호 (레이와, 헤이세이). 중국: 양력 + 음력 (춘절, 중추절).
   - 미국/유럽: 양력만. 공휴일 달력 단순.
   - **함정**: 한국어 학습자가 미국 공휴일 (추수감사절, 7월 4일) 만 학습 → 한국 공휴일 (설날, 추석, 개천절) 무지.
   - **훈련법**: 한국/중국/일본 명절 매트릭스 — 설날(음력 1월 1일) / 춘절(음력 1월 1일) / Old New Year(일본). **음력/양력 통합 명절 학습**.

6. **날짜 형식의 5개 언어**:
   - 한국/일본/중국: 연-월-일 (YYYY.MM.DD / YYYY/MM/DD / YYYY年MM月DD日).
   - 미국: 월-일-년 (MM/DD/YYYY). 영국/유럽: 일-월-년 (DD/MM/YYYY).
   - **함정**: 한국어 학습자가 미국식 07/19/2024 단순 매핑 → 19/07/2024 (영국/유럽식). **월-일-년 vs 일-월-년 매핑 차이**.
   - **훈련법**: 날짜 형식 매트릭스 — US MM/DD/YYYY / EU DD/MM/YYYY / KR/JP/CH YYYY.MM.DD or YYYY/MM/DD. **5개 언어 날짜 형식 명시 학습**.

### 학습 전략

1. **우선순위 1**: 시간 한자 한자어 3개국 발음 매트릭스 — 時間/시간/shíjiān, 分/분/fēnzhōng, 秒/초/miǎo. **한자 1글자 = 3개국 발음**.
2. **우선순위 2**: 시간 형식 매트릭스 — KR/JP/CH 24시간 기본, EN 12시간 기본. **12h/24h 변환 표 학습**.
3. **우선순위 3**: 요일 5개 어원 시스템 매트릭스 — KR/JP 한자 5원소, ES 로마 신, EN 북유럽 신, CH 数字. **5개 어원 시스템 비교**.
4. **우선순위 4**: 한국어 고유 시간 어휘 — 오늘/내일/모레/글피 vs 어제/그저께/그끄저께 (순우리말). **고유어 vs 한자어 분리**.
5. **우선순위 5**: 음력/양력 통합 명절 매트릭스 — 설날/추석(음력), 크리스마스(양력), 추수감사절(양력). **명절 매트릭스**.

### 관련 한국어 위키 페이지

- [[numbers-counters]] — 시간 단위
- [[travel-essentials]] — 여행 시간
- [[business-email]] — 미팅 시간
- [[greetings]] — 시간 기반 인사
- [[untranslatable-concepts]] — 시간 문화 개념

---

## 관련 페이지

- `[[numbers-counters]]` — 시간 단위, 지속
- `[[travel-essentials]]` — 스케줄, 교통 시간
- `[[business-email]]` — 미팅 시간
- `[[greetings]]` — 시간 기반 인사
- `[[cultural-values]]` — 시간 인식 (단일 vs 다중)

## 출처

- English: `[English/vocabulary/basic-vocabulary]`, `[English/vocabulary/travel]`
- Spanish: `[Spanish/vocabulary/basic-vocabulary]`, `[Spanish/vocabulary/time-prepositions-vocabulary]`
- Japanese: `[[index]]`, `[Japanese/vocabulary/jp-counters]`
- Korean: `[[index]]`, `[Korean/vocabulary/topik1-starter]`
- Chinese: `[Chinese/vocabulary/numbers-zh]`, `[Chinese/sources/pinyin-basics-zh]`

---

**원본 (영어)**: [[time-calendar]] | **관련 미러**: [[time-calendar.es|Spanish]] · [[time-calendar.ja|Japanese]] · [[time-calendar.zh|Chinese]] | **정책**: ADR-0006
