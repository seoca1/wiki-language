# 时间与日历 — 跨语言对比 (中文版)

> 原文: [[time-calendar]] (English) | 撰写日期: 2026-08-19 | ADR-0006
> **5种语言时间表达/日历/相对时间对比** — English · Spanish · Japanese · Korean · Chinese

---

## 速查表

### 时间表达

### 报时 (小时 + 分钟)

| 时间 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **1:00** | one o'clock | la una (en punto) | 一時 (いちじ) | 한 시 (han si) | 一点 (yī diǎn) |
| **2:00** | two o'clock | las dos (en punto) | 二時 (にじ) | 두 시 (du si) | 两点 (liǎng diǎn) |
| **3:00** | three o'clock | las tres (en punto) | 三時 (さんじ) | 세 시 (se si) | 三点 (sān diǎn) |
| **12:00** | twelve o'clock / noon | las doce / mediodía | 十二時 (じゅうにじ) / 正午 (しょうご) | 열두 시 (yeoldu si) / 낮 (nat) | 十二点 (shíèr diǎn) / 中午 (zhōngwǔ) |
| **0:00 / 24:00** | midnight | medianoche | 零時 (れいじ) / 深夜 (しんや) | 자정 (jajeong) / 밤 12시 | 零点 (líng diǎn) / 午夜 (wǔyè) |

### 几点几分

| 分钟 | English | Spanish | Japanese | Korean | Chinese |
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

### 12h vs 24h 格式

| 语言 | 默认格式 | 24h 语境 |
|----------|----------------|-------------|
| **英语 (美)** | 12h (am/pm) | 军事, 医疗, 交通 |
| **英语 (英)** | 12h 常见, 24h 增长中 | 交通, 电视时刻表, 军事 |
| **西班牙语** | 12h 口语, 24h 书面/时刻表 | 时刻表, 官方, 军事 |
| **日语** | **24h 标准** (13:00, 23:59) | 12h 仅在口语中用 *gozen/gogo* |
| **韩语** | **24h 标准** (13시, 23시 59분) | 12h 用 *am/pm* 或 *오전/오후* 口语 |
| **中文** | **24h 标准** (13:00, 23:59) | 12h 用 *am/pm* 或 *上午/下午* 口语 |

### AM/PM 对应

| 时段 | English | Spanish | Japanese | Korean | Chinese |
|--------|---------|---------|----------|--------|---------|
| **早晨 (12am-12pm)** | am / a.m. | a.m. / de la mañana | 午前 (ごぜん) / 朝 (あさ) | 오전 (ojeon) / 아침 (achim) | 上午 (shàngwǔ) / 早上 (zǎoshang) |
| **中午** | noon / 12pm | mediodía / 12 del mediodía | 正午 (しょうご) / 昼 (ひる) | 낮 (nat) / 정오 (jeong-o) | 中午 (zhōngwǔ) / 正午 (zhèngwǔ) |
| **下午 (12pm-6pm)** | pm / p.m. | p.m. / de la tarde | 午後 (ごご) / 昼過ぎ (ひるすぎ) | 오후 (ohu) / 오후 (ohu) | 下午 (xiàwǔ) / 午后 (wǔhòu) |
| **傍晚 (6pm-12am)** | evening | tarde / noche | 夕方 (ゆうがた) / 夜 (よる) | 저녁 (jeonyeok) / 밤 (bam) | 晚上 (wǎnshang) / 傍晚 (bàngwǎn) |
| **午夜** | midnight | medianoche | 深夜 (しんや) / 真夜中 (まよなか) | 자정 (jajeong) / 밤중 (bamjung) | 午夜 (wǔyè) / 半夜 (bànyè) |

---

## 一周

| 星期 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **周一** | Monday | lunes | 月曜日 (げつようび) | 월요일 (woryoil) | 星期一 (xīngqīyī) / 周一 (zhōuyī) |
| **周二** | Tuesday | martes | 火曜日 (かようび) | 화요일 (hwayoil) | 星期二 (xīngqī'èr) / 周二 (zhōu'èr) |
| **周三** | Wednesday | miércoles | 水曜日 (すいようび) | 수요일 (suyoil) | 星期三 (xīngqīsān) / 周三 (zhōusān) |
| **周四** | Thursday | jueves | 木曜日 (もくようび) | 목요일 (mogyoil) | 星期四 (xīngqīsì) / 周四 (zhōusì) |
| **周五** | Friday | viernes | 金曜日 (きんようび) | 금요일 (geumyoil) | 星期五 (xīngqīwù) / 周五 (zhōuwǔ) |
| **周六** | Saturday | sábado | 土曜日 (どようび) | 토요일 (toyoil) | 星期六 (xīngqīliù) / 周六 (zhōuliù) |
| **周日** | Sunday | domingo | 日曜日 (にちようび) | 일요일 (iryoil) | 星期日 (xīngqīrì) / 周日 (zhōurì) / 星期天 |

### 词源 (行星/元素)

| 语言 | 系统 | 示例 |
|------|--------|---------|
| **英语** | 北欧神 + 日/月 | *Mon*day (月), *Tues*day (Tyr), *Wednes*day (Odin), *Thurs*day (Thor), *Fri*day (Frigg), *Satur*day (Saturn), *Sun*day |
| **西班牙语** | 罗马神 + 日/月 | *Lunes* (Luna), *Martes* (Marte), *Miércoles* (Mercurio), *Jueves* (Júpiter), *Viernes* (Venus), *Sábado* (Sabbat), *Domingo* (Dominus) |
| **日语** | 5 元素 + 日/月 | *Getsu* (月 Moon), *Ka* (火 Fire), *Sui* (水 Water), *Moku* (木 Wood), *Kin* (金 Metal), *Do* (土 Earth), *Nichi* (日 Sun) |
| **韩语** | 与日语相同 (汉字) | *Wol* (月), *Hwa* (火), *Su* (水), *Mok* (木), *Geum* (金), *To* (土), *Il* (日) |
| **中文** | 编号 (周 = 星期/周) | *Xingqi* (星期) = "star period" / *Zhou* (周) = cycle |

### 周末定义

| 语言 | 周末 | 工作周 |
|----------|---------|-----------|
| **英语 (美)** | 周六-周日 | 周一-周五 |
| **英语 (英)** | 周六-周日 | 周一-周五 |
| **西班牙语** | 周六-周日 (周日神圣) | 周一-周五 (有些周六半天) |
| **日语** | 周六-周日 | 周一-周五 (历史上的周六半天) |
| **韩语** | 周六-周日 | 周一-周五 (2004: 5 天工作周 法律) |
| **中文** | 周六-周日 | 周一-周五 (调整假日创造长假) |

---

## 月份

| 月份 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **1月** | January | enero | 一月 (いちがつ) / 睦月 (むつき) | 일월 (ilwol) / 1월 | 一月 (yīyuè) / 1月 |
| **2月** | February | febrero | 二月 (にがつ) / 如月 (きさらぎ) | 이월 (iwol) / 2월 | 二月 (èryuè) / 2月 |
| **3月** | March | marzo | 三月 (さんがつ) / 弥生 (やよい) | 삼월 (samwol) / 3월 | 三月 (sānyuè) / 3月 |
| **4月** | April | abril | 四月 (しがつ) / 卯月 (うづき) | 사월 (sawol) / 4월 | 四月 (sìyuè) / 4月 |
| **5月** | May | mayo | 五月 (ごがつ) / 皐月 (さつき) | 오월 (owol) / 5월 | 五月 (wǔyuè) / 5月 |
| **6月** | June | junio | 六月 (ろくがつ) / 水無月 (みなづき) | 유월 (yuwol) / 6월 | 六月 (liùyuè) / 6月 |
| **7月** | July | julio | 七月 (しちがつ) / 文月 (ふみづき) | 칠월 (chirwol) / 7월 | 七月 (qīyuè) / 7月 |
| **8月** | August | agosto | 八月 (はちがつ) / 葉月 (はづき) | 팔월 (parwol) / 8월 | 八月 (bāyuè) / 8月 |
| **9月** | September | septiembre | 九月 (くがつ) / 長月 (ながつき) | 구월 (guwol) / 9월 | 九月 (jiǔyuè) / 9月 |
| **10月** | October | octubre | 十月 (じゅうがつ) / 神無月 (かんなづき) | 시월 (siwol) / 10월 | 十月 (shíyuè) / 10月 |
| **11月** | November | noviembre | 十一月 (じゅういちがつ) / 霜月 (しもつき) | 십일월 (sibilwol) / 11월 | 十一月 (shíyīyuè) / 11月 |
| **12月** | December | diciembre | 十二月 (じゅうにがつ) / 師走 (しわす) | 십이월 (sibiwol) / 12월 | 十二月 (shíèryuè) / 12月 |

### 传统月份名 (日本)
- *Mutsuki* (睦月) - 和睦月
- *Kisaragi* (如月) - 换衣月
- *Yayoi* (弥生) - 新生月
- *Uzuki* (卯月) - 卯月
- *Satsuki* (皐月) - 插秧月
- *Minazuki* (水無月) - 无水月
- *Fumizuki* (文月) - 书写月
- *Hazuki* (葉月) - 叶月
- *Nagatsuki* (長月) - 长月
- *Kannazuki* (神無月) - 神无月 (出云)
- *Shimotsuki* (霜月) - 霜月
- *Shiwasu* (師走) - 师走月

---

## 相对时间表达

| 表达 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **现在** | now | ahora | 今 (いま) | 지금 (jigeum) | 现在 (xiànzài) / 如今 (rújīn) |
| **今天** | today | hoy | 今日 (きょう) | 오늘 (oneul) | 今天 (jīntiān) / 今日 (jīnrì) |
| **明天** | tomorrow | mañana | 明日 (あした/あす/みょうにち) | 내일 (naeil) | 明天 (míngtiān) / 明日 (míngrì) |
| **昨天** | yesterday | ayer | 昨日 (きのう/さくじつ) | 어제 (eoje) | 昨天 (zuótiān) / 昨日 (zuórì) |
| **后天** | day after tomorrow | pasado mañana | 明後日 (あさって/みょうごにち) | 모레 (more) | 后天 (hòutiān) / 后日 (hòurì) |
| **前天** | day before yesterday | anteayer | 一昨日 (おととい/いっさくじつ) | 그저께 (geujeokke) | 前天 (qiántiān) / 前日 (qiánrì) |
| **这周** | this week | esta semana | 今週 (こんしゅう) | 이번 주 (ibeon ju) | 这周 (zhè zhōu) / 本周 (běn zhōu) |
| **上周** | last week | la semana pasada | 先週 (せんしゅう) | 지난 주 (jinan ju) | 上周 (shàng zhōu) / 上个周 |
| **下周** | next week | la semana que viene | 来週 (らいしゅう) | 다음 주 (daeum ju) / 내주 (naeju) | 下周 (xià zhōu) / 下个周 |
| **这个月** | this month | este mes | 今月 (こんげつ) | 이번 달 (ibeon dal) | 这个月 (zhège yuè) / 本月 (běn yuè) |
| **上个月** | last month | el mes pasado | 先月 (せんげつ) | 지난 달 (jinan dal) | 上个月 (shàng gè yuè) |
| **下个月** | next month | el mes que viene | 来月 (らいげつ) | 다음 달 (daeum dal) / 내달 (naedal) | 下个月 (xià gè yuè) |
| **今年** | this year | este año | 今年 (ことし) | 올해 (olhae) / 금년 (geumnyeon) | 今年 (jīnnián) / 今年 (jīnnián) |
| **去年** | last year | el año pasado | 去年 (きょねん) | 작년 (jangnyeon) / 지난해 (jinanhae) | 去年 (qùnián) |
| **明年** | next year | el año que viene | 来年 (らいねん) | 내년 (naenyeon) / 내년 (naenyeon) | 明年 (míngnián) |

### 近期过去 / 近期未来

| 表达 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **刚才** | just now | ahora mismo / hace un momento | さっき (sakki) / たった今 (tatta ima) | 방금 (banggeum) / 막 (mak) | 刚才 (gāngcái) / 刚刚 (gānggāng) |
| **一会儿前** | a while ago | hace un rato | 少し前 (すこしまえ) | 조금 전 (jogeum jeon) | 刚才 / 一会儿前 (yīhuìr qián) |
| **很快** | soon | pronto / en breve | すぐ (sugu) / 近いうちに (ちかいうちに) | 곧 (got) / 머지않아 (meoji-ana) | 很快 (hěn kuài) / 马上 (mǎshàng) |
| **稍后** | later | luego / más tarde | 後で (あとで) / 後ほど (のちほど) | 나중에 (najunge) / 이따가 (ittaga) | 后来 (hòulái) / 稍后 (shāohòu) / 待会儿 (dānghuìr) |
| **马上** | in a moment | en un momento / ahora | すぐに (sugu ni) / 間もなく (まもなく) | 금방 (geumbang) / 잠시 후 (jamsi hu) | 马上 (mǎshàng) / 片刻后 (piànkè hòu) |

---

## 时长表达

| 时长 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **秒** | second | segundo | 秒 (びょう) | 초 (cho) | 秒 (miǎo) |
| **分** | minute | minuto | 分 (ふん/ぷん) | 분 (bun) | 分钟 (fēnzhōng) / 分 (fēn) |
| **小时** | hour | hora | 時間 (じかん) | 시간 (sigan) | 小时 (xiǎoshí) / 个钟头 (gè zhōngtóu) |
| **天** | day | día | 日 (にち/ひ/か) / 日間 (にちかん) | 일 (il) / 하루 (haru) | 天 (tiān) / 日 (rì) |
| **周** | week | semana | 週 (しゅう) / 週間 (しゅうかん) | 주 (ju) / 한 주 (han ju) | 周 (zhōu) / 个星期 (gè xīngqī) |
| **月** | month | mes | 月 (つき/げつ) / 月間 (げっかん) | 달 (dal) / 개월 (gaewol) | 月 (yuè) / 个月 (gè yuè) |
| **年** | year | año | 年 (とし/ねん) / 年間 (ねんかん) | 년 (nyeon) / 해 (hae) | 年 (nián) |

### 近似时长

| 表达 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **一会儿** | a moment | un momento / un rato | 少し (すこし) / ひととき (hitotoki) | 잠깐 (jamkkan) / 잠시 (jamsi) | 片刻 (piànkè) / 一会儿 (yīhuìr) |
| **一阵子** | a while | un rato | しばらく (shibaraku) | 잠시 (jamsi) / 한동안 (handongan) | 一阵子 (yī zhènzi) / 一会儿 (yīhuìr) |
| **半小时** | half an hour | media hora | 30分 (さんじゅっぷん) / 半時間 (はんじかん) | 30분 (samsip bun) / 반 시간 (ban sigan) | 半小时 (bàn xiǎoshí) / 半个钟头 |
| **一个半小时** | an hour and a half | hora y media | 1時間半 (いちじかんはん) | 한 시간 반 (han sigan ban) | 一个半小时 (yī gè bàn xiǎoshí) |
| **整天** | all day | todo el día | 終日 (しゅうじつ) / 一日中 (いちにちじゅう) | 종일 (jongil) / 하루 종일 (haru jongil) | 一整天 (yī zhěng tiān) / 整天 (zhěng tiān) |
| **通宵** | all night | toda la noche | 徹夜 (てつや) / 一晩中 (ひとばんじゅう) | 밤새 (bamsae) / 밤새도록 (bamsaedorok) | 通宵 (tōngxiāo) / 整夜 (zhěng yè) |

---

## 日历系统与节日

### 日历类型

| 语言 | 日历 | 备注 |
|------|----------|------|
| **英语** | 格里高利 (阳历) | 全球标准 |
| **西班牙语** | 格里高利 (阳历) | 天主教礼仪日历覆盖 |
| **日语** | 格里高利 (阳历) + **和历 (年代)** | 令和 6 = 2024; 平成, 昭和, 大正, 明治 年代 |
| **韩语** | 格里高利 (阳历) + **农历 (음력)** | 春节, 秋夕按农历; 檀纪 (단기) 年代罕见 |
| **中文** | 格里高利 (阳历) + **农历 (农历)** | 春节, 中秋按农历; 60 年周期 (干支) |

### 主要节日对比

| 节日 | English (美/英) | Spanish | Japanese | Korean | Chinese |
|------|-----------------|---------|----------|--------|---------|
| **新年** | Jan 1 | Año Nuevo (Jan 1) | 元日 (がんじつ) Jan 1 | 신정 (sinjeong) Jan 1 | 元旦 (yuándàn) Jan 1 |
| **农历新年** | — | — | 旧正月 (きゅうしょうがつ) — minor | **설날 (Seollal)** — **3 天** | **春节 (Chūnjié)** — **7-15 天** |
| **独立/国家** | Jul 4 (美) / — | Fiesta Nacional (Oct 12) | 建国記念の日 (けんこくきねんのひ) Feb 11 | 광복절 (Gwangbokjeol) Aug 15 | 国庆节 (Guóqìngjié) Oct 1 |
| **劳动节** | September (第一个周一) | Día del Trabajo (May 1) | 勤労感謝の日 (きんろうかんしゃのひ) Nov 23 | 근로자의 날 (Geulloja-ui nal) May 1 | 劳动节 (Láodòngjié) May 1 (5 天) |
| **感恩节** | 11月 (第4周四) | — | 勤労感謝の日 (Nov 23) — 类似 | 추석 (Chuseok) — **3 天** (农历 8月15日) | 中秋节 (Zhōngqiūjié) — 3 天 (农历 8月15日) |
| **圣诞节** | Dec 25 | Navidad (Dec 25) | クリスマス (Dec 24-25) — couples | 성탄절 (Seongtanjeol) Dec 25 | 圣诞节 (Shèngdànjié) — commercial |
| **黄金周** | — | — | **ゴールデンウィーク** (Apr 29-May 5) | — | — |
| **银周** | — | — | シルバーウィーク (Sep, when aligned) | — | — |
| **中元** | — | — | **お盆** (Aug 13-16) — 祖先 | — | 中元节 (Zhōngyuánjié) — 鬼节 |
| **儿童节** | — | Día del Niño (Apr 30 墨西哥) | **こどもの日** (May 5) | 어린이날 (Eorininal) May 5 | 六一儿童节 (Liùyī értóngjié) Jun 1 |

---

## 日期格式

| 语言 | 短格式 | 长格式 | 示例 (2024-07-19) |
|------|--------------|-------------|----------------------|
| **英语 (美)** | MM/DD/YYYY | Month DD, YYYY | 07/19/2024 / July 19, 2024 |
| **英语 (英)** | DD/MM/YYYY | DD Month YYYY | 19/07/2024 / 19 July 2024 |
| **西班牙语** | DD/MM/YYYY | DD de Month de YYYY | 19/07/2024 / 19 de julio de 2024 |
| **日语** | YYYY/MM/DD | YYYY年MM月DD日 | 2024/07/19 / 2024年7月19日 (令和6年7月19日) |
| **韩语** | YYYY.MM.DD | YYYY년 MM월 DD일 | 2024.07.19 / 2024년 7월 19일 |
| **中文** | YYYY/MM/DD | YYYY年MM月DD日 | 2024/07/19 / 2024年7月19日 |

---

## 季节

| 季节 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **春** | spring | primavera | 春 (はる) | 봄 (bom) | 春 (chūn) / 春天 (chūntiān) |
| **夏** | summer | verano | 夏 (なつ) | 여름 (yeoreum) | 夏 (xià) / 夏天 (xiàtiān) |
| **秋** | autumn / fall | otoño | 秋 (あき) | 가을 (ga-eul) | 秋 (qiū) / 秋天 (qiūtiān) |
| **冬** | winter | invierno | 冬 (ふゆ) | 겨울 (gyeoul) | 冬 (dōng) / 冬天 (dōngtiān) |

### 季节月份 (北半球)

| 语言 | 春 | 夏 | 秋 | 冬 |
|------|--------|--------|--------|--------|
| **英语** | 3-5月 | 6-8月 | 9-11月 | 12-2月 |
| **西班牙语** | 3-5月 | 6-8月 | 9-11月 | 12-2月 |
| **日语** | 3-5月 | 6-8月 | 9-11月 | 12-2月 |
| **韩语** | 3-5月 | 6-8月 | 9-11月 | 12-2月 |
| **中文** | 3-5月 | 6-8月 | 9-11月 | 12-2月 |

**注**: 南半球 (阿根廷, 智利 等) 反转。

---

## 速查卡

| 需要说... | EN | ES | JP | KR | CH |
|------|----|----|----|----|----|
| **"现在几点?"** | What time is it? | ¿Qué hora es? | 今何時ですか？ (Ima nanji desu ka?) | 지금 몇 시예요? (Jigeum myeot si-yeyo?) | 现在几点? (Xiànzài jǐ diǎn?) |
| **"3:30"** | It's three thirty. | Son las tres y media. | 三時半です (Sanji han desu) | 세 시 반이에요 (Se si ban-ieyo) | 三点半 (Sān diǎn bàn) |
| **"明天见"** | See you tomorrow. | Nos vemos mañana. | また明日 (Mata ashita) | 내일 봐요 (Naeil bwayo) | 明天见 (Míngtiān jiàn) |
| **"今天星期几?"** | What day is it? | ¿Qué día es hoy? | 今日は何曜日？ (Kyou wa nan youbi?) | 오늘 무슨 요일이에요? (Oneul museun yoil-ieyo?) | 今天星期几? (Jīntiān xīngqī jǐ?) |
| **"下周"** | next week | la semana que viene | 来週 (Raishuu) | 다음 주 (Daeum ju) | 下周 (Xià zhōu) |
| **"上个月"** | last month | el mes pasado | 先月 (Sengetsu) | 지난 달 (Jinan dal) | 上个月 (Shàng gè yuè) |
| **"两天后"** | in two days | dentro de dos días | 二日後 (Futsuka go) | 이틀 후 (It-eul hu) | 两天后 (Liǎng tiān hòu) |
| **"三天前"** | three days ago | hace tres días | 三日前 (Mikka mae) | 사흘 전 (Saheul jeon) | 三天前 (Sān tiān qián) |
| **"整天"** | all day | todo el día | 一日中 (Ichinichijuu) | 종일 (Jongil) / 하루 종일 | 一整天 (Yī zhěng tiān) |
| **"每天"** | every day | todos los días | 毎日 (Mainichi) | 매일 (Maeil) | 每天 (Měitiān) |
| **"一周一次"** | once a week | una vez a la semana | 週1回 (Shuu ikkai) | 주 1회 (Ju 1-hoe) | 一周一次 (Yī zhōu yī cì) |

---

## 相关页面

- `[[numbers-counters]]` — 时间量词, 时长
- `[[travel-essentials]]` — 时刻表, 交通时间
- `[[business-email]]` — 会议安排
- `[[greetings]]` — 基于时间的问候
- `[[cultural-values]]` — 时间感知 (单一时间 vs 多重时间)

## 来源

- 英语: `[English/vocabulary/basic-vocabulary]`, `[English/vocabulary/travel]`
- 西班牙语: `[Spanish/vocabulary/basic-vocabulary]`, `[Spanish/vocabulary/time-prepositions-vocabulary]`
- 日语: `[[index]]`, `[Japanese/vocabulary/jp-counters]`
- 韩语: `[[index]]`, `[Korean/vocabulary/topik1-starter]`
- 中文: `[Chinese/vocabulary/numbers-zh]`, `[Chinese/sources/pinyin-basics-zh]`

---

## 🇨🇳 中文学习者笔记 (Chinese Learner Notes)

> 本节是面向中文母语学习者的额外学习指南。

### 中文母语者在学习其他4种语言时间与日历时的常见陷阱

1. **24h vs 12h 时制的差异**:
   - 中文 24h 标准 (13:00, 23:59) → 学员假设其他语言也类似。
   - **陷阱**: 英语 12h 通用 (am/pm); 西语 12h 口语 / 24h 书面; 日韩 24h 标准 + 12h 口语。
   - **训练法**: 制作"时制对照表" — 中/日/韩 24h 标准 vs 英/西 12h 标准 (但在正式场合用 24h)。

2. **一周起始日的差异**:
   - 中文 周一为周首 → 学员假设其他语言也类似。
   - **陷阱**: 英语/西语 周日为周首 (Western convention); 阿拉伯/伊斯兰 周六为周首; 国际标准 ISO 8601 周一为周首。
   - **训练法**: 区分"周首" vs 周日 — 跨国交流时确认习惯。

3. **农历 vs 阳历节日的差异**:
   - 中文 春节 (农历) / 中秋 (农历) → 学员假设其他语言也有农历节日。
   - **陷阱**: 韩语 설날 (农历) / 추석 (农历) 类似; 日语 旧正月 (旧历) 较少; 英语/西语 仅阳历节日。
   - **训练法**: 区分"阳历节日" (圣诞/新年) vs "农历节日" (春节/中秋) — 东亚文化有, 西方较少。

4. **日期格式的差异**:
   - 中文 YYYY/MM/DD → 学员假设其他语言也对应。
   - **陷阱**: 英语 美 MM/DD/YYYY vs 英 DD/MM/YYYY; 日语 YYYY/MM/DD; 韩语 YYYY.MM.DD; 西语 DD/MM/YYYY。
   - **训练法**: 制作"日期格式"对照表 — 跨国交流时避免混淆 (7/8/2024 美式 vs 8/7/2024 英式)。

5. **时代 (era) 的差异**:
   - 中文 公元 2024 → 学员假设其他语言也对应。
   - **陷阱**: 日语 令和 6 = 2024; 韩语 檀纪 (단기) 罕见; 英语 BC/AD; 西语 a.C./d.C.
   - **训练法**: 了解目的地时代系统 — 日本时代必须用令和 6 = 2024。

### 相关中文维基页面

- [Chinese/vocabulary/time-zh] — 中文时间词汇
- [Chinese/culture/chinese-lunar-calendar-zh] — 中文农历
- [Chinese/vocabulary/numbers-zh] — 中文数字词汇
- [Chinese/grammar/basic-particles] — 中文基本助词
- [Chinese/culture/chinese-holidays-zh] — 中文节日

### 学习工作流程推荐

1. **背诵对比表** (时间/星期/月份/日期)
2. **时制对照** (24h vs 12h)
3. **日期格式** (跨国交流避免混淆)
4. **农历 vs 阳历节日** (东亚文化 vs 西方)
5. **时代系统** (日本令和 vs 公元)

---

**原文 (英语)**: [[time-calendar]] | **相关镜像**: [[time-calendar.es|西班牙语]] · [[time-calendar.ja|日语]] · [[time-calendar.ko|韩语]] | **政策**: ADR-0006
