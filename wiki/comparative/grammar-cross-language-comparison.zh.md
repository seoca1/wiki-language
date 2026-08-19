# 跨语言语法对比 (中文版)

> 原文: [[grammar-cross-language-comparison]] (English) | 撰写日期: 2026-08-19 | ADR-0006
> **5语言语法架构对比** — English · Spanish · Japanese · Korean · Chinese

---

## 速查表

| 特征 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **语序** | SVO | SVO | SOV | SOV | SVO |
| **时态标记** | 形态 (eat/ate) | 形态 (-é/-ió) | 形态 (た-form) | 形态 (았/었) | 完句助词 (了/过) |
| **完句系统** | 进行 (-ing), 完成 (have+V-ed) | 进行 (-ndo), 完成 (-ado) | -te iru (进行), -te shimau (完成) | -고 있다 (进行), -아/어 있다 (状态) | 着 (进行), 了 (完成), 过 (经历) |
| **冠词** | a / an / the | el / la / un / una | 无 | 无 | 无 |
| **性** | 无 (自然性) | 阳性 / 阴性 | 无 | 无 | 无 |
| **动词礼貌** | 无 | 有限 (usted 动词形式) | 完整系统 (keigo) | 完整系统 (합쇼체/해요체) | 无 |
| **复数标记** | -s (规则) | -s/-es | 复数词 たち (tachi) 可选 | 复数词 들 (deul) 可选 | 无 (上下文) |
| **疑问标记** | 倒装 / 升调 | ¿...? + 倒装 | か (ka) | 까? (kka?) / 니? (ni?) | 吗 (ma) |
| **否定** | don't / not | no / -ar/-er/-ir 变化 | ない (nai) / ません (masen) | 안 (an) / -지 않다 (-ji anhda) | 不 (bù) / 没 (méi) |
| **代词省略** | 必须 | 必须 | 常见 (零代词) | 常见 | 常见 |

---

## 语序详情

| 语序 | 语言 | 例子 |
|------|------|------|
| **SVO (主-谓-宾)** | English, Spanish, Chinese | "I eat apples." / "Como manzanas." / "我吃苹果。" |
| **SOV (主-宾-谓)** | Japanese, Korean | "私はりんごを食べる" (Watashi wa ringo o taberu) / "나는 사과를 먹다" (Naneun sagwa-reul meokda) |

---

## 时态 vs 完句

| 概念 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **简单过去** | ate | comí | 食べた (tabeta) | 먹었다 (meogeotda) | 吃了 (chī le) |
| **现在进行** | is eating | está comiendo | 食べている (tabete iru) | 먹고 있다 (meokgo itda) | 吃着 (chī zhe) |
| **经历** | have eaten | he comido | 食べたことがある (koto ga aru) | 먹어 본 적 있다 (meogeo bon jeok itda) | 吃过 (chī guò) |
| **将来** | will eat | comerá | 食べるだろう (darō) | 먹을 것이다 (meogeul geosida) | 会吃 (huì chī) |

---

## 冠词与限定词

| 类型 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **定冠词** | the | el / la | (无) | (无; 그 "geu") | (无; 这 "zhè") |
| **不定冠词** | a / an | un / una | (无) | (无; 한 "han") | (无) |
| **指示** | this / that | este / ese | これ / それ (kore/sore) | 이 / 그 (i/geu) | 这 / 那 (zhè/nà) |
| **所有** | my, your, his | mi, tu, su | 私の (watashi no) | 나의 (na-ui) | 我的 (wǒ de) |

---

## 各语言详情

### 🇬🇧 英语 (English)
- **核心**: SVO, 冠词 (a/an/the), 时态-完句, do-support
- **模式**: 时态强制; 单数可数名词需冠词
- **来源**: `[[wiki/English/grammar/grammar-overview]]`

### 🇪🇸 西班牙语 (Spanish)
- **核心**: SVO, 性一致, ser vs estar, 虚拟式
- **模式**: 动词变位据人称/数; 虚拟式表怀疑/欲望/情感
- **地区变体**: Voseo (里约拉布拉塔); Vosotros (西班牙) vs Ustedes (拉美)
- **来源**: `[[wiki/Spanish/grammar/grammar-overview]]`

### 🇯🇵 日语 (Japanese)
- **核心**: SOV, 助词 (は/が/を/に/で/へ), 敬语
- **模式**: 主题-评注 (は/が); 动词始终在末尾
- **敬语层级**: 尊敬語 (尊敬), 謙譲語 (谦逊), 丁寧語 (礼貌)
- **来源**: `[[wiki/Japanese/grammar/grammar-overview]]`

### 🇰🇷 韩语 (Korean)
- **核心**: SOV, 助词 (은/는/이/가/를/을), 语体层级
- **模式**: 主题 는/은, 主语 가/이; 动词始终在末尾
- **语体**: 합쇼체 正式 / 해요체 礼貌 / 해체 简略 / 하소서체 文学
- **来源**: `[[wiki/Korean/grammar/grammar-overview]]`

### 🇨🇳 中文 (Chinese)
- **核心**: SVO, 完句助词 (了/过/着), 量词
- **模式**: 动词不变位; 完句助词标记时间流
- **语域/敬语**: 您 (nín) 尊称; 量词强制 (个/本/杯/张)
- **来源**: `[[wiki/Chinese/grammar/grammar-overview-zh]]`

---

## 关键对比 (综合)

| 对比 | 对学习者的启示 |
|------|----------------|
| **语序家族** | EN/ES/CH = SVO; JP/KR = SOV. SOV 学员可直接映射到 JP/KR |
| **冠词** | EN/ES 要求可数名词冠词; JP/KR/CH 无 |
| **礼貌深度** | JP/KR 有完整基于动词的礼貌; EN/ES/CH 依赖代词/选词 |
| **时态 vs 完句** | EN/ES 形态标记时态; CH 用完句助词; JP/KR 混合两者 |

---

## 速查卡

> **语序**: SVO (EN/ES/CH) vs SOV (JP/KR)
> **礼貌**: Keigo (JP) / 합쇼체 (KR) / usted (ES) / please (EN) / 请 (CH)
> **冠词**: a/the (EN) · el/la (ES) · 无 (JP/KR/CH)
> **完句**: -ing (EN) · 了/过/着 (CH) · -te iru / -고 있다 (JP/KR)

---

## 🇨🇳 中文学习者笔记 (Chinese Learner Notes)

> 本节是面向中文母语学习者的额外学习指南。

### 中文母语者在学习其他4种语言语法时的常见陷阱

1. **SVO/SOV 语序的颠倒**:
   - 中文 *我吃苹果* (SVO) → 学员假设日韩语序相同。
   - **陷阱**: 日韩 SOV → 我 (S) 苹果 (O) 吃 (V)。
   - **训练法**: 用中文整句翻译练习 (SVO) → SOV 重排。
     - 例: *我吃苹果* → 私は りんごを 食べる (JP) → 나는 사과를 먹다 (KR)。

2. **冠词的概念**:
   - 中文 *我看到苹果* 无冠词 → 学员对英语 *the apple* / *an apple* 感到困惑。
   - **陷阱**: 英语/西班牙语区分定指/不定指; 中文/日文/韩文无此区分。
   - **训练法**: 翻译时按上下文判断"特指 vs 泛指"→ 选用 EN/ES 冠词。

3. **动词的"形态爆炸"**:
   - 中文 *吃/吃了* 几乎不变位 → 学员对西班牙语/日语/韩语动词多变形态感到吃力。
   - **陷阱**: 西班牙语 *comer/comí/comeré/comiendo/comido*; 日语 *食べる/食べた/食べている*; 韩语 *먹다/먹었다/먹고 있다*。
   - **训练法**: 每日 5 动词的 5 时态/完句变位; 33 个"动词变化矩阵"。

4. **时态 vs 完句的概念差异**:
   - 中文用 *了/过/着* 完句助词 → 学员对日韩混合系统感到困惑。
   - **陷阱**: 日语 *た-form* (时态) 与 *て-form + いる* (进行) 同时存在; 韩语 *았/었* (过去) 与 *-고 있다* (进行) 共存。
   - **训练法**: 整理 *了/过/着* 对应矩阵 (CN 了 ↔ EN -ed / ES -ó / JP -た / KR -았/었)。

5. **敬语/语体的"必选性"**:
   - 中文 *您* 可选 → 学员对日语/韩语敬语"必选"感到困惑。
   - **陷阱**: 日语对上级必须 *ます/です*; 韩语对上级必须 *합쇼체*; 不可随意选。
   - **训练法**: 商务对话时优先最礼貌形式; 看到对方"放松"后才尝试更随意形式。

### 相关中文维基页面

- [Chinese/grammar/svo-zh] — 中文 SVO 语序
- [Chinese/grammar/aspect-vs-tense-zh] — 中文完句 vs 时态
- [Chinese/grammar/measure-words-zh] — 中文言词
- [Chinese/grammar/honorifics-zh] — 中文敬语
- [Chinese/grammar/null-pronoun-zh] — 中文零代词省略

### 学习工作流程推荐

1. **5 语言语序对照表** (10 句 SVO 转 SOV 练习)
2. **冠词概念对照表** (CN 无 ↔ EN a/the ↔ ES el/la ↔ JP/KR 无)
3. **每日 5 动词变位矩阵** (33 个变化 × 5 语言)
4. **时态 vs 完句映射表** (CN 了/过/着 ↔ 5 语言对应)
5. **敬语/语体必选性** 商务场景练习 (日语/韩语优先最礼貌)

---

## 相关页面

- `[[grammar-difficulty-map]]` — 特征逐项难度排名
- `[[tense-aspect-systems]]` — 时态 vs 完句深度
- `[[politeness-honorifics]]` — 完整 keigo / 语体 系统
- `[[mood-systems]]` — 直陈 vs 虚拟
- `[[pronouns-reference]]` — 代词系统与零代词

## 来源

- EN: `[[wiki/English/grammar/grammar-overview]]`
- ES: `[[wiki/Spanish/grammar/grammar-overview]]`
- JP: `[[wiki/Japanese/grammar/grammar-overview]]`
- KR: `[[wiki/Korean/grammar/grammar-overview]]`
- CN: `[[wiki/Chinese/grammar/grammar-overview-zh]]`

---

**原文 (英语)**: [[grammar-cross-language-comparison]] | **相关镜像**: [[grammar-cross-language-comparison.es|西班牙语]] · [[grammar-cross-language-comparison.ja|日语]] · [[grammar-cross-language-comparison.ko|韩语]] | **政策**: ADR-0006
