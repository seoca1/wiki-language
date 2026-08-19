# 礼貌与敬语 — 跨语言对比 (中文版)

> 原文: [[politeness-honorifics]] (English) | 撰写日期: 2026-08-19 | ADR-0006
> **5种语言语阶/敬语系统对比** — English · Spanish · Japanese · Korean · Chinese

---

## 速查表

| 特征 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **语法编码** | 仅词汇 (词汇选择) | 代词 (tú/usted) + 动词形态 | 动词形态 (keigo) + 词汇 | 动词词尾 (语阶) + 尊称名词/动词 | 词汇选择 + 尊称头衔 + 您 (nín) |
| **级别数** | 2-3 (正式/中性/随意) | 2-3 (tú/usted/vosotros) | 3-4 (随意/礼貌/尊敬/谦让) | 4-6 (해체/해요체/합쇼체/하소서체 + 混合) | 2-3 (中性/您/敬称头衔) |
| **代词区分** | you (通用) | tú / usted / vosotros / ustedes | あなた / 君 / お前 / 貴方 (常省略) | 너 / 당신 / 당신들 / 선생님/님 (避免) | 你 / 您 / 诸位 / 先生/女士 |
| **动词形态变化** | 否 | 是 (2/3 人称) | 是 (广泛) | 是 (广泛) | 最小 (一些异干词) |
| **敬语词汇** | 有限 (sir/ma'am, 头衔) | Don/Doña, usted 形式 | 尊敬語 / 謙譲語 / 丁寧語 | 존댓말 / 높임말 (特殊动词/名词) | 尊称, 敬语 (您, 贵姓, etc.) |
| **相对地位重要** | 语境依赖 | 是 (年龄, 熟悉) | 中心 (内/外) | 中心 (年龄, 等级) | 中心 (年龄, 等级, 关系) |
| **圈内 vs 圈外** | 弱 | 中 (usted 默认圈外) | 基础 (内/外) | 基础 (自己人/外人) | 基础 (自己人/外人) |

---

## 各语言详情

### 🇬🇧 英语 (English)
- **关键词**: 正式 vs 随意语阶, "please/thank you," 头衔 (Mr/Ms/Dr/Prof), 缓和 (could/would/might)
- **模式**: 没有语法敬语。 礼貌 = 词汇选择 + 句法距离 (过去时用于现在请求: "I was wondering if...") + 模态动词 + 间接性
- **语阶笔记**:
  - 正式: "Would you be so kind as to...", "I would appreciate it if..."
  - 中性: "Could you please...", "Please..."
  - 随意: "Can you...", "Hey, ..."
- **来源**: `[English/vocabulary/basic-vocabulary]`, `[English/culture/english-dating-culture]`

### 🇪🇸 西班牙语 (Spanish)
- **关键词**: tú / usted / vosotros / ustedes, *don/doña*, *usted* 动词形式 (第三人称), *tuteo* vs *ustedeo*
- **模式**:
  - **Tú**: 朋友, 家人, 儿童, 同辈 (西班牙年轻人默认)
  - **Usted**: 陌生人, 长辈, 正式场合, 权威 (LatAm 默认)
  - **Vosotros** (仅西班牙): 复数随意
  - **Ustedes**: 复数正式 (西班牙) / 复数全部 (LatAm)
- **地区差异**:
  - **西班牙**: tú/usted 区分强; 使用 vosotros
  - **墨西哥/哥伦比亚/秘鲁**: usted 即使在年轻人某些场合下也是默认
  - **阿根廷/乌拉圭/巴拉圭**: *vos* 替代 *tú* (voseo) — 不同变位
  - **加勒比**: *usted* 较频繁, *tú* 保留亲密
- **来源**: `[Spanish/vocabulary/polite-expressions-vocabulary]`, `[Spanish/culture/espana-vs-latinoamerica-registro]`

### 🇯🇵 日语 (Japanese)
- **关键词**:
  - **丁寧語 (teineigo)**: です/ます — 默认礼貌
  - **尊敬語 (sonkeigo)**: 尊敬 — 抬高对方 (いらっしゃる, 召し上がる, ご存知)
  - **謙譲語 (kenjougo)**: 谦让 — 降低自己 (参る, いただく, 拝見する)
  - **美化語 (bikago)**: お/ご 前缀 (お茶, ご飯)
- **模式**: 动词变位完全按语阶变化。 *内* (圈内) vs *外* (圈外) 决定用哪种 keigo。 与陌生人默认交互 = teineigo。 商务 = sonkeigo/kenjougo 混合。
- **敬语 / 礼貌级别**:
  - 随意 (タメ口): 行く, 食べる, 知ってる — 亲密朋友, 家人, 年轻人
  - 礼貌 (丁寧語): 行きます, 食べます, 知っています — 陌生人, 同事, 默认
  - 尊敬 (尊敬語): いらっしゃいます, 召し上がります, ご存知です — 顾客, 上级, 长辈
  - 谦让 (謙譲語): 参ります, いただきます, 拝見します — 与上级谈论自己
- **来源**: `[Japanese/vocabulary/business-vocabulary]`, `[Japanese/culture/japanese-dating-culture]`

### 🇰🇷 韩语 (Korean)
- **关键词**:
  - **해체 (haeche)**: 普通/书面正式 — 亲密朋友, 儿童, 自我对话
  - **해요체 (haeyoche)**: 礼貌随意 — 日常生活, 同事, 熟人 (口头默认)
  - **합쇼체 (hapsyoche)**: 正式礼貌 — 演讲, 广播, 军队, 顾客
  - **하소서체 (hasoseoche)**: 极端正式 — 历史, 宗教, 皇室
  - **존댓말 (jondaetmal)**: 礼貌级别的总称
  - **반말 (banmal)**: 随意 (해체/해요체 混合)
- **模式**:
  - 动词词尾变化: 가다 → 가/가요/갑니다/가시옵소서
  - 尊称名词: 밥 → 진지, 집 → 댁, 이름 → 성함, 생일 → 생신
  - 尊称动词: 먹다 → 잡수시다, 자다 → 주무시다, 계시다 (있다/계시다)
  - 主题尊称标记: ~(으)시 (가시다, 드시다)
- **语阶选择**: 年龄差 1+ 岁 → 期望敬语。 同龄 → 协商 (언제 반말 할까요?). 工作场所: 头衔 + 님 (팀장님, 매니저님)
- **来源**: `[Korean/vocabulary/emotions-personality-vocabulary]`, `[Korean/culture/korean-dating-culture]`

### 🇨🇳 中文 (Chinese)
- **关键词**:
  - **您 (nín)**: 尊敬 "你" (vs 你 nǐ)
  - **尊称 (zūnchēng)**: 尊敬头衔 — 先生, 女士, 老师, 总经理, 姐/哥
  - **敬语 (jìngyǔ)**: 敬语词汇 — 贵姓, 请教, 拜访, 敬请, 承蒙
  - **谦辞 (qiāncí)**: 自谦 — 拙作, 拙见, 献丑, 不敢当
- **模式**:
  - 礼貌无动词形态变化
  - 礼貌 = 词汇替换 + 头衔 + 句尾助词 (请, 麻烦您, 劳驾)
  - **您 (nín)** 用于长辈, 上级, 正式场合的陌生人
  - **头衔 + 姓**: 王先生, 李老师, 张总 — 专业场合默认
  - **关系 (guanxi)** 调节语阶: 关系更近 → 略 您, 用名字/昵称
- **语阶 / 敬语**:
  - 中性: 你, 叫什么名字?, 去
  - 尊敬: 您, 贵姓?, 请去 / 麻烦您去
  - 正式书面: 阁下, 尊驾, 惠顾, 光临 (商务通信)
- **来源**: `[Chinese/vocabulary/body-zh]`, `[Chinese/sources/greetings-zh]`

---

## 关键对比 (综合)

| 对比 | 学习者启示 |
|------|----------|
| **语法 vs 词汇** — 日/韩/西将礼貌编码在语法; 英/中用词汇 | 日/韩学习者必须早期掌握动词范式; 英/中学习者可以用基础语法 + 礼貌词 沟通 |
| **默认陌生人语阶** — 西: *usted* (LatAm) / *tú* (西班牙青年); 日: *desu/masu*; 韩: *haeyoche*; 中: *nín* + 头衔 | 按目标地区选择默认: 墨西哥 → *usted*; 东京 → *desu/masu*; 首尔 → *haeyoche*; 北京 → *nín* + 头衔 |
| **圈内/圈外 (内/外, 自己人/外人)** — 对日/韩至关重要; 英弱; 西/中中等 | 在日/韩, 对圈内用错误语阶 = 冷淡/距离; 对圈外 = 粗鲁。 先学习群体边界。 |
| **年龄 vs 头衔称呼** — 韩/中要求 头衔+님/先生; 日 用 -san/様; 西 用 Don/Doña + usted; 英 用 Mr/Ms | 在韩/中, 直呼名字 = 粗鲁。 记住每个角色的头衔 (팀장님, 王老师, 部長様, Don Juan)。 |
| **语阶协商** — 韩明示 ("우리 반말 해요"); 日隐含 (略 keigo); 西明示 ("tuteame"); 中隐含 (略 您) | 韩学习者: 练习 "언제 반말 할까요?" 脚本。 日学习者: 注意 keigo 略去的信号。 西学习者: "¿Puedo tutearte?" |

---

## 学习者决策指南

> "如果你的目标是 X, 在语言 Y 中优先 Y 因为..."

- **目标: 基础生存/旅行** →
  - EN: "Please/Thank you/Excuse me" + 模态动词
  - ES: *usted* 形式 + *por favor/gracias* (通用)
  - JP: *desu/masu* + *sumimasen/arigatou* (覆盖 90% 互动)
  - KR: *haeyoche* (-요 词尾) + *juseyo/mianhamnida* (安全默认)
  - CH: *nín* + *qing/xiexie/duibuqi* + 头衔 (服务员, 师傅)

- **目标: 商务/专业** →
  - EN: 缓和, 被动语态, "I would appreciate," 头衔
  - ES: *ustedeo* + *usted* 动词形式 + *Don/Doña* + 正式结尾 (*Atentamente, Cordialmente*)
  - JP: 完整 *keigo* (sonkeigo/kenjougo/bikago) + *keigo* 邮件模板 + *meishi* 交换礼仪
  - KR: *hapsyoche* (-ㅂ니다) + 尊称名词/动词 + 头衔+님 + 鞠躬深度
  - CH: *nín* + 贵姓/请教/拜访 + 头衔 (总监, 经理, 老师) + 请/麻烦您

- **目标: 社交/友谊/恋爱** →
  - EN: 名字基础迅速, 短语动词, 俚语
  - ES: *tuteo* 协商 (*¿Puedo tutearte?*) → 地区规范不同
  - JP: *tameguchi* 转换 (通常在第 3 次见面/饮酒后) — 等前辈提议
  - KR: *banmal* 协商 (*우리 반말 해요*) — 通常年轻者请求年长者
  - CH: 略 *nín* → *nǐ*, 用名字/昵称/哥/姐 — 跟随 *guanxi* 加深

- **目标: 学术/正式写作** →
  - EN: 被动, 名词化, 缓和, 引用风格
  - ES: *ustedeo*, 非人 *se*, 正式场合的虚拟式
  - JP: 论文 *dearu/da* (普通); 演讲 *desu/masu*; *kanbun* 遗留形式
  - KR: *hapsyoche* + 敬语 + 汉字词 (한자어)
  - CH: 书面语 (书面语) — 之/其/乃/乎, 4字成语, 被动 被/由

---

## 相关页面

- `[[greetings]]` — 问候仪式编码礼貌
- `[[pronouns-reference]]` — 代词系统反映敬语结构
- `[[business-email]]` — 书面语阶对比
- `[[dating-romance]]` — 亲密度的语阶协商

## 来源

- 英语: `[English/vocabulary/basic-vocabulary]`, `[English/culture/english-dating-culture]`
- 西班牙语: `[Spanish/vocabulary/polite-expressions-vocabulary]`, `[Spanish/culture/espana-vs-latinoamerica-registro]`, `[Spanish/sources/notes-in-spanish-listening-log]`
- 日语: `[Japanese/vocabulary/business-vocabulary]`, `[Japanese/culture/japanese-dating-culture]`, `[Japanese/sources/business-email]`
- 韩语: `[Korean/vocabulary/emotions-personality-vocabulary]`, `[Korean/culture/korean-dating-culture]`, `[Korean/sources/daily-life-basics]`
- 中文: `[Chinese/vocabulary/body-zh]`, `[Chinese/sources/greetings-zh]`, `[Chinese/sources/daily-routine-zh]`

---

## 🇨🇳 中文学习者笔记 (Chinese Learner Notes)

> 本节是面向中文母语学习者的额外学习指南。

### 中文母语者在学习其他4种语言敬语时的常见陷阱

1. **中文敬语相对简化的假设**:
   - 中文敬语 您/你 + 头衔 → 学员假设其他语言也简单。
   - **陷阱**: 日语 5 层敬语 (普通/礼貌/尊敬/谦让/美化); 韩语 7 个语阶 (해체/해요체/합쇼체/하소서체 + 混合); 西语 2 层 tú/usted; 英语 2-3 层 formal/informal。
   - **训练法**: 制作"敬语层级对照表" — 中文 2 层 vs EN 2-3 层 vs KR 7 层 vs JP 5 层 vs ES 2 层。

2. **尊称代词的差异**:
   - 中文 您 (nín) 用于长辈/上级 → 学员假设其他语言也对应。
   - **陷阱**: 日语无尊称代词 (用动词敬语); 韩语无尊称代词 (用 시 后缀); 西语 usted (正式) vs tú (随意); 英语 you 通用。
   - **训练法**: 区分"代词敬语" vs "动词敬语" — 日韩靠动词变形, 西靠代词, 中靠代词。

3. **头衔称呼的差异**:
   - 中文 头衔 + 姓 (王老师, 张经理) → 学员假设其他语言对应。
   - **陷阱**: 韩语 头衔 + 님 (팀장님, 매니저님); 日语 姓 + 様 (田中様) / 名 + san (健太san); 西语 Don/Doña + 名字 (Don Juan); 英语 Mr/Ms + 姓 (Mr. Smith)。
   - **训练法**: 制作"头衔称呼"对照表 — 中文 头衔+姓 / 韩 头衔+님 / 日 姓+様 or 名+san / 西 Don/Doña+名 / 英 Mr/Ms+姓。

4. **礼貌动词的差异**:
   - 中文 词汇替换表达礼貌 (请/谢谢) → 学员假设其他语言也词汇替换。
   - **陷阱**: 日语动词变形 (食べる→召し上がる/いただく); 韩语尊称动词 (먹다→잡수시다, 자다→주무시다); 英语 间接请求 (Could you...?); 西语 虚拟式 (Quisiera...)。
   - **训练法**: 学习每种语言的"礼貌动词矩阵" — 朋友/同事/上级 各自怎么说。

5. **圈内/圈外的关系敏感度**:
   - 中文 关系 (guanxi) 调节语阶 → 学员假设其他语言也类似。
   - **陷阱**: 日语 内/外 (uchi/soto) 严格; 韩语 自己人/外人 + 严格的年龄等级; 西语 usted 在陌生/正式场合默认; 英语 弱。
   - **训练法**: 学习每种语言的"圈内/圈外"标识 — 何时切换语阶, 何时保持一致。

### 相关中文维基页面

- [Chinese/vocabulary/politeness-zh] — 中文礼貌词汇
- [Chinese/culture/chinese-communication-style] — 中文沟通风格
- [Chinese/grammar/basic-particles] — 中文基本助词
- [Chinese/sources/daily-routine-zh] — 中文日常用语
- [Chinese/culture/chinese-business-etiquette-zh] — 中文商务礼仪

### 学习工作流程推荐

1. **背诵对比表** (5种语言代词 + 头衔 + 语阶)
2. **敬语层级对照** (5种语言各自的敬语系统)
3. **场景模拟** (朋友/同事/上级/陌生人 各自怎么礼貌)
4. **头衔称呼** (各语言尊称方式)
5. **关系驱动语阶** (圈内/圈外如何切换)

---

**原文 (英语)**: [[politeness-honorifics]] | **相关镜像**: [[politeness-honorifics.es|西班牙语]] · [[politeness-honorifics.ja|日语]] · [[politeness-honorifics.ko|韩语]] | **政策**: ADR-0006
