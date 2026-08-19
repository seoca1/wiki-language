# 代词与指代 — 跨语言对比 (中文版)

> 原文: [[pronouns-reference]] (English) | 撰写日期: 2026-08-19 | ADR-0006
> **5种语言人称代词/反身/指示代词对比** — English · Spanish · Japanese · Korean · Chinese

---

## 速查表

### 人称代词表

| 人称 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **1 单** | I | yo | 私 / 僕 / 俺 / わし | 나 / 저 | 我 / 咱 |
| **2 单** | you | tú / usted / vos | あなた / 君 / お前 / 貴方 | 너 / 당신 / 선생님 | 你 / 您 |
| **3 单** | he/she/it | él / ella | 彼 / 彼女 / あの人 | 그 / 그녀 / 그분 | 他 / 她 / 它 |
| **1 复** | we | nosotros/as | 私たち / 僕ら / 俺たち | 우리 / 저희 | 我们 / 咱们 |
| **2 复** | you (all) | vosotros/as / ustedes | あなたたち / 君たち | 너희 / 여러분 / 선생님들 | 你们 / 您们 |
| **3 复** | they | ellos / ellas | 彼ら / 彼女ら / あの人たち | 그들 / 그분들 | 他们 / 她们 / 它们 |

### 关键结构差异

| 特征 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **强制?** | 是 (主语必需) | 否 (pro-drop) | 否 (pro-drop, 语境重) | 否 (pro-drop) | 否 (pro-drop) |
| **第三人称单性别** | 是 (he/she/it) | 是 (él/ella) | 否 (kare/kanojo = 男/女 但少用) | 否 (geu/geunyeo = 男/女 但少见) | 是 (tā/tā/tā — 同音, 不同字) |
| **语阶编码** | 否 (仅词汇) | 是 (tú/usted/vos) | 是 (代词选择 = 语阶) | 是 (代词选择 = 语阶) | 是 (nǐ/nín) |
| **包含/排除 we** | 否 | 否 | 否 (wareware = 正式 we) | 否 (uri = 包含默认) | **是** (zánmen = 包含, wǒmen = 排除) |
| **零代词 (pro-drop)** | 否 | **是** (标准) | **是** (标准) | **是** (标准) | **是** (标准) |

---

## 各语言详情

### 🇬🇧 英语 (English)
- **强制主语**: 每个有定式子句需要显性主语
- **格系统**: I/me, he/him, she/her, we/us, they/them
- **通用 "you"**: 单数和复数相同
- **单数 "they"**: 未知/非二元性别的标准
- **反身**: myself, yourself, himself, herself, itself, ourselves, yourselves, themselves
- **所有格**: my/mine, your/yours, his, her/hers, its, our/ours, their/theirs
- **来源**: `[English/vocabulary/basic-vocabulary]`

### 🇪🇸 西班牙语 (Spanish)
- **Pro-drop**: 主语代词常省略 (*hablo* = "我说")
- **Tú/Usted/Vos**: 三元单数随意/正式区分 (地区)
- **Vosotros (仅西班牙)**: 复数随意; *ustedes* = 复数正式 (西班牙) / 复数全部 (LatAm)
- **性别**: 所有代词有性别 (*nosotros/nosotras*, *ellos/ellas*)
- **代词**: me/te/se/nos/os/le/les/lo/la/los/las — 动词前或附着于不定式/动名词
- **反身**: *se* (第三人称所有数/性别)
- **来源**: `[Spanish/vocabulary/basic-vocabulary]`, `[Spanish/culture/espana-vs-latinoamerica-registro]`

### 🇯🇵 日语 (Japanese)
- **代词 = 语阶选择**: 无中性 "I/you" — 每次选择都标记关系
- **第一人称**:
  - *watashi* (私) — 中性礼貌 (默认)
  - *watakushi* (私) — 正式
  - *boku* (僕) — 阳性随意
  - *ore* (俺) — 阳性粗鲁/亲密
  - *atashi* (あたし) — 阴性随意
  - *uchi* (うち) — 阴性关西
- **第二人称**:
  - *anata* (あなた) — 礼貌但疏远 (夫妇使用)
  - *kimi* (君) — 上级→下级, 阳性同辈
  - *omae* (お前) — 阳性粗鲁/亲密
  - *kisama* (貴様) — 敌对
  - *name-san* — **偏好** (用名字 + 敬称)
- **第三人称**: *kare/kanojo* 存在但听起来像翻译; *ano hito* (那个人) 偏好
- **复数**: *-tachi* (中性), *-ra* (随意/阳性), *-gata* (尊称)
- **零代词**: 标准 — 语境界定指代
- **来源**: `[[index]]`, `[Japanese/culture/japanese-dating-culture]`

### 🇰🇷 韩语 (Korean)
- **代词 = 语阶选择**: 像日语, 无中性形式
- **第一人称**:
  - *na* (나) — 随意 (해체)
  - *jeo* (저) — 谦让 (해요체/합쇼체)
  - *uri* (우리) — "我们" 包含 (默认); *jeohui* (저희) — 谦让我们
- **第二人称**:
  - *neo* (너) — 随意 (亲密朋友, 儿童)
  - *dangsin* (당신) — **避免** (争论或诗意/配偶)
  - *name-ssi/nim* — **偏好** (名字 + 头衔)
  - *seonsaengnim* (선생님) — 通用尊敬
- **第三人称**: *geu/geunyeo* (그/그녀) — 书面/正式; *geu bun* (그분) — 尊称
- **零代词**: 标准 — 主语/宾语常规省略
- **反身**: *jagi* (자기) — 自己; *jagijasin* (자신) — oneself
- **来源**: `[[index]]`, `[Korean/culture/korean-dating-culture]`

### 🇨🇳 中文 (Chinese)
- **Pro-drop**: 主语/宾语自由省略
- **包含/排除 we**:
  - *zánmen* (咱们) — 包含 (你 + 我 + 其他人)
  - *wǒmen* (我们) — 排除 (我 + 其他人, 不含你)
- **礼貌**: *nǐ* (你) vs *nín* (您) — 第二人称尊敬
- **复数**: *-men* (们) 后缀 — *wǒmen, nǐmen, tāmen*
- **书写性别仅**: 他/她/它 都 *tā* 口语
- **指示代词**: *zhè* (这), *nà* (那) — 这/那个人
- **反身**: *zìjǐ* (自己) — 自己
- **来源**: `[Chinese/sources/greetings-zh]`, `[Chinese/vocabulary/family-zh]`

---

## 指示代词

| 距离 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **近 (this)** | this | este/esta/esto | これ (kore) | 이거 / 이것 | 这 / 这个 |
| **中 (that near you)** | that | ese/esa/eso | それ (sore) | 그거 / 그것 | 那 / 那个 |
| **远 (that over there)** | that over there | aquel/aquella/aquello | あれ (are) | 저거 / 저것 | 那个 (far) |
| **地点 (here/there)** | here/there | aquí/allí/allá | ここ/そこ/あそこ | 여기/거기/저기 | 这里/那里/那儿 |

### 用法说明
- **西班牙语**: 三级距离 (*este/ese/aquel*) — *aquel* = 远离说话者和听者
- **日语**: *kore/sore/are* = 物; *koko/soko/asoko* = 地点; *kochira/sochira/achira* = 方向/人 (礼貌)
- **韩语**: *igeo/geugeo/jeogeo* (物) vs *yeogi/geogi/jeogi* (地点); *ireon/geureon/jeoreon* (种)
- **中文**: *zhè/zhège* vs *nà/nàge* — 二级口语; *zhèr/nàr* (北) vs *zhèlǐ/nàlǐ* (南) 表示地点

---

## 疑问代词

| 问题 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **谁** | who | quién | 誰 (だれ) | 누구 (nugu) | 谁 (shéi/shuí) |
| **什么** | what | qué | 何 (なに/なん) | 무엇 / 뭐 (mueot/mwo) | 什么 (shénme) |
| **哪个** | which | cuál | どれ (dore) | 어느 (eoneu) | 哪个 (nǎge) |
| **哪里** | where | dónde | どこ (doko) | 어디 (eodi) | 哪里 / 哪儿 (nǎlǐ/nǎr) |
| **何时** | when | cuándo | いつ (itsu) | 언제 (eonje) | 什么时候 (shénme shíhou) |
| **为何** | why | por qué | なぜ (naze) / どうして (doushite) | 왜 (wae) | 为什么 (wèishénme) |
| **怎么** | how | cómo | どう (dou) | 어떻게 (eotteoke) | 怎么 (zěnme) |
| **谁的** | whose | de quién | 誰の (dare no) | 누구 것 (nugu geot) | 谁的 (shéi de) |

---

## 不定代词

| 含义 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **每个人** | everyone | todos | 皆 (みな) / みんな | 모두 / 전부 | 大家 / 人人 |
| **某个人** | someone | alguien | 誰か (だれか) | 누군가 (nugunga) | 某人 / 谁 (shéi) |
| **没人** | no one | nadie | 誰も...ない (dare mo...nai) | 아무도...않다 (amudo...anta) | 没人 / 谁都不 (shéi dōu bù) |
| **一切** | everything | todo | 全て (すべて) / みんな | 모든 것 / 전부 | 一切 / 全部 |
| **某事** | something | algo | 何か (なにか) | 무언가 / 뭔가 (mueotnga/mwonga) | 某事 / 什么 (shénme) |
| **没事** | nothing | nada | 何も...ない (nani mo...nai) | 아무것도...않다 (amugeotdo...anta) | 没事 / 什么都没有 (shénme dōu méiyǒu) |
| **任何人** | anyone | cualquiera | 誰でも (だれでも) | 아무나 (amuna) | 谁都可以 (shéi dōu kěyǐ) |

---

## 反身与相互

| 类型 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **反身** | myself/yourself... | me/te/se/nos/os/se | 自分 (じぶん) | 자기 (jagi) / 자신 (jasin) | 自己 (zìjǐ) |
| **相互** | each other | el uno al otro / mutuamente | お互い (おたがい) | 서로 (seoro) | 彼此 / 互相 (bǐcǐ/hùxiāng) |

---

## 零代词 / Pro-drop 行为

| 语言 | 主语省略 | 宾语省略 | 所有格省略 | 备注 |
|------|---------|---------|---------|------|
| **英语** | ❌ | ❌ | ❌ | 强制主语 |
| **西班牙语** | ✅ (标准) | ❌ (代词必需) | ❌ | *Hablo español* = "我说西班牙语" |
| **日语** | ✅ (标准) | ✅ (标准) | ✅ (标准) | 语境补足必需 |
| **韩语** | ✅ (标准) | ✅ (标准) | ✅ (标准) | 主题/评论结构帮助补足 |
| **中文** | ✅ (标准) | ✅ (标准) | ✅ (标准) | 主题突出; 零照应普遍 |

### 补足策略
- **西班牙语**: 动词形态编码人/数 (*hablo/hablas/habla/hablamos/habláis/hablan*)
- **日语/韩语**: 主题标记 (*wa/は* vs *ga/が* vs *eun/은* vs *i/이*) + 敬语 + 语境
- **中文**: 主题-评论结构 + 体标记 + 词汇语境

---

## 跨语言干扰图

| 学习者 L1 → 目标 L2 | 典型错误 | 原因 |
|--------------------|----------|------|
| **英 → 西/日/韩/中** | 到处用显性代词 ("I think that he...") | L1 要求主语; 目标允许零 |
| **西 → 日/韩** | 使用 *tú* 等价 (*anata/neo*) 与陌生人 | *Tú* = 同辈默认; *anata/neo* = 亲密 |
| **日/韩 → 中** | 过度使用 *nín* (您) 像 *anata/nan* | *Nín* = 特定尊敬; 中文更常用头衔 |
| **中 → 西** | 通用使用 *tú* (无 *nín* 等价) | 中文 *nǐ* 默认; 西语要求 *usted* 选择 |
| **英 → 日/韩** | 翻译 "you" → *anata/neo* | 日/韩无中性 "you" |

---

## 速查卡

| 表达... | EN | ES | JP | KR | CH |
|---------|----|----|----|----|----|
| **"我 (礼貌)"** | I | yo | わたし (watashi) | 저 (jeo) | 我 (wǒ) |
| **"我 (随意男)"** | I | yo | ぼく (boku) / おれ (ore) | 나 (na) | 我 (wǒ) |
| **"你 (礼貌)"** | you | usted | (name)-san | (name)-ssi/nim | 您 (nín) |
| **"你 (随意)"** | you | tú / vos | (name)-kun/chan | 너 (neo) | 你 (nǐ) |
| **"我们 (包含)"** | we | nosotros | わたしたち (watashitachi) | 우리 (uri) | 咱们 (zánmen) |
| **"我们 (排除)"** | we | nosotros | わたしたち (watashitachi) | 우리 (uri) / 저희 (jeohui) | 我们 (wǒmen) |
| **"他/她 (尊)"** | he/she | él/ella | あのかた (ano kata) | 그분 (geu bun) | 他/她 (tā) |
| **"这个"** | this one | este | これ (kore) | 이거 (igeo) | 这个 (zhège) |
| **"谁?"** | who? | quién? | だれ (dare)? | 누구 (nugu)? | 谁 (shéi)? |
| **"没人"** | nobody | nadie | だれもいない (dare mo inai) | 아무도 없다 (amudo eopda) | 没人 (méi rén) |

---

## 相关页面

- `[[politeness-honorifics]]` — 代词选择编码礼貌
- `[[greetings]]` — 问候中的称呼形式
- `[[business-email]]` — 书面代词惯例
- `[[negation]]` — 否定代词 (*nadie, dare mo...nai, amudo...*)

## 来源

- 英语: `[English/vocabulary/basic-vocabulary]`
- 西班牙语: `[Spanish/vocabulary/basic-vocabulary]`, `[Spanish/culture/espana-vs-latinoamerica-registro]`
- 日语: `[[index]]`, `[Japanese/culture/japanese-dating-culture]`
- 韩语: `[[index]]`, `[Korean/culture/korean-dating-culture]`
- 中文: `[Chinese/sources/greetings-zh]`, `[Chinese/vocabulary/family-zh]`

---

## 🇨🇳 中文学习者笔记 (Chinese Learner Notes)

> 本节是面向中文母语学习者的额外学习指南。

### 中文母语者在学习其他4种语言代词时的常见陷阱

1. **包含/排除 我们 的区分**:
   - 中文 咱们 (包含) vs 我们 (排除) → 学员假设其他语言也对应。
   - **陷阱**: 英语 we 通用; 西语 nosotros 通用; 日语 わたしたち 通用; 韩语 우리 (包含) / 저희 (排除) 区分。
   - **训练法**: 区分"我们"是否包含对方 — 中文独有这一区分, 学习其他语言时需注意。

2. **nǐ vs nín 的语域**:
   - 中文 你/您 区分 → 学员假设其他语言也对应。
   - **陷阱**: 日语无尊称代词 (用动词敬语); 韩语无尊称代词 (用 시 后缀); 西语 usted (正式) vs tú (随意); 英语 you 通用。
   - **训练法**: 区分"代词敬语" vs "动词敬语" — 日韩靠动词变形, 西靠代词, 中靠代词。

3. **零代词 (pro-drop) 的过度省略**:
   - 中文常省略主语 (我走了) → 学员假设其他语言都允许。
   - **陷阱**: 英语要求显性主语 (I went) — 学员在英语也省略 → 错误。
   - **训练法**: 制作"pro-drop vs 强制"对照表 — 中/日/韩/西允许省略; 英强制。

4. **第三人称性别区分**:
   - 中文 他/她/它 同音 (tā) → 学员假设其他语言也有这种"语音无性别"。
   - **陷阱**: 英语 he/she/it 区分; 西语 él/ella 区分; 日语 kare/kanojo 区分 (但少用); 韩语 geu/geunyeo 区分 (但少用)。
   - **训练法**: 写作时区分性别 — 中文靠字, 英文靠词; 写英文时不能省略 he/she/it。

5. **包含/排除 第二人称复数**:
   - 中文 你们 (排除) vs 您们 (包含尊敬) → 学员假设其他语言区分。
   - **陷阱**: 英语 you 通用 (单数和复数都 you); 西语 vosotros/ustedes 区分; 日语 あなたたち 通用; 韩语 너희/여러분 区分。
   - **训练法**: 区分"向多人说话" vs "向单个人说话" — 英语统一, 其他语言区分。

### 相关中文维基页面

- [Chinese/vocabulary/pronouns-zh] — 中文代词
- [Chinese/culture/chinese-communication-style] — 中文沟通风格
- [Chinese/grammar/basic-particles] — 中文基本助词
- [Chinese/vocabulary/family-zh] — 中文家庭词汇
- [Chinese/sources/daily-routine-zh] — 中文日常用语

### 学习工作流程推荐

1. **背诵对比表** (5种语言代词)
2. **零代词 vs 强制** (pro-drop 矩阵)
3. **尊称代词 vs 动词敬语** (各语言敬语方式)
4. **包含/排除 我们** (中文独有区分)
5. **场景练习** (自我介绍/介绍他人/称呼不同关系)

---

**原文 (英语)**: [[pronouns-reference]] | **相关镜像**: [[pronouns-reference.es|西班牙语]] · [[pronouns-reference.ja|日语]] · [[pronouns-reference.ko|韩语]] | **政策**: ADR-0006
