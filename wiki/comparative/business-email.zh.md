# 商务邮件 — 跨语言对比 (中文版)

> 原文: [[business-email]] (English) | 撰写日期: 2026-08-19 | ADR-0006
> **5语言商务邮件对比** — English · Spanish · Japanese · Korean · Chinese

---

## 速查表: 邮件结构对比

| 组成部分 | English | Spanish | Japanese | Korean | Chinese |
|----------|---------|---------|----------|--------|---------|
| **主题行** | 简洁, 具体 | 简洁, 具体 | 【件名】 + 主题 | [제목] + 主题 | 【主题】 + 主题 |
| **称呼** | Dear [Name], | Estimado/a [Name]: | [Name] 様 / [Company] [Title] 様 | [Name] [Title]님 / [Company] [Title]님 | 尊敬的 [Title] [Surname]： |
| **开场白** | I hope you're well. | Espero que esté bien. | いつもお世話になっております。 | 항상 수고가 많으십니다. | 希望您一切安好。 |
| **目的陈述** | I'm writing to... | Le escribo para... | この度は〜の件でご連絡いたしました。 | 〜건으로 메일 드립니다. | 写信是关于…… |
| **正文** | 直接, 项目符号友好 | 直接, 正式 | 上下文优先, 后请求 | 上下文优先, 后请求 | 上下文优先, 后请求 |
| **结尾** | Best regards, | Atentamente / Cordialmente, | よろしくお願いいたします。 | 잘 부탁드립니다. | 顺颂商祺 / 此致 敬礼 |
| **签名** | Name, Title, Company, Phone | Name, Cargo, Empresa, Tel | Name, 所属, 役職, 会社, TEL | 이름, 직함, 회사, 연락처 | 姓名, 职位, 公司, 电话 |

---

## 称呼详情

### 🇬🇧 英语
| 关系 | 称呼 |
|------|------|
| 正式 (未知姓名) | Dear Sir/Madam, / To Whom It May Concern, |
| 正式 (已知姓名) | Dear Mr./Ms./Dr. [Last], |
| 同事/已知 | Hi [First], / Hello [First], |
| 团队/组 | Dear Team, / Hi All, |

### 🇪🇸 西班牙语
| 关系 | 称呼 |
|------|------|
| 正式 (未知) | Estimado Señor/Señora: / Muy señor mío: |
| 正式 (已知) | Estimado/a Sr./Sra./Dr./Dra. [Apellido]: |
| 已知联系人 | Estimado/a [Nombre]: |
| 较随意 | Hola [Nombre]: / Querido/a [Nombre]: |

**地区**: *Estimado* (西班牙) vs *Estimado/a* (拉美性别一致); *Usted* 隐含于正式

### 🇯🇵 日语 (from `[Japanese/sources/business-email]`)
| 关系 | 称呼 |
|------|------|
| 外部 (标准) | 株式会社〇〇 〇〇部 〇〇様 |
| 外部 (已知姓名) | 〇〇株式会社 〇〇様 |
| 内部 (上级) | 〇〇部長 / 〇〇課長 / 〇〇様 |
| 内部 (同事) | 〇〇さん |
| 回复外部 | 〇〇様 いつもお世話になっております。 |

**关键**: 公司 → 部门 → 职位/姓名 → 様 — 外部永不用"姓名 + sama"

### 🇰🇷 韩语 (from `[Korean/sources/daily-life-basics]`)
| 关系 | 称呼 |
|------|------|
| 外部 (标准) | ㈜○○ ○○팀 ○○님 / ○○부장님 |
| 外部 (已知) | ○○님 |
| 内部 (上级) | ○○팀장님 / ○○부장님 / ○○선배님 |
| 内部 (同事) | ○○님 / ○○씨 |
| 回复外部 | ○○님, 항상 수고가 많으십니다. |

**关键**: 公司 → 团队 → 职位 + 님 — *님* 尊称强制; *씨* 仅同事/下属

### 🇨🇳 中文
| 关系 | 称呼 |
|------|------|
| 正式 (未知) | 尊敬的先生/女士： |
| 正式 (已知) | 尊敬的 [职称] [姓]： (经理/总监/教授) |
| 已知联系人 | 尊敬的 [姓] [职称]： |
| 较随意 | [姓] [职称] 你好： / 各位同事： |

**关键**: 头衔后跟姓 (王经理, 李总监) — 商务永不用名字

---

## 速查表: 标准化功能短语

### 开场 / 上下文设定

| 功能 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **引用之前联系** | Further to our conversation... | En referencia a nuestra conversación... | 先日はお話しいただき、ありがとうございました。 | 앞서 통화한 내용과 관련하여... | 承接我们上次的沟通…… |
| **引用附件** | Please find attached... | Adjunto encontrará... | 添付ファイルをご確認ください。 | 첨부파일 확인 부탁드립니다. | 请查收附件…… |
| **回执感谢** | Thank you for your email. | Gracias por su correo. | メールをいただき、ありがとうございます。 | 메일 주셔서 감사합니다. | 收到您的邮件，谢谢。 |
| **延迟致歉** | Apologies for the late reply. | Disculpe la demora. | 返信が遅くなり、申し訳ございません。 | 답장이 늦어져 죄송합니다. | 回复较晚，抱歉。 |

### 请求

| 功能 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **礼貌请求** | Could you please...? | ¿Podría... por favor? | 〜していただけますでしょうか。 | 〜해 주시겠어요? | 能否请您…… |
| **正式请求** | I would appreciate it if... | Agradecería que... | 〜ていただけますと幸いです。 | 〜해 주시면 감사하겠습니다. | 如果能……将不胜感激。 |
| **请求确认** | Please confirm... | Por favor confirme... | ご確認のほど、よろしくお願いいたします。 | 확인 부탁드립니다. | 请确认…… |
| **请求回复日期** | Please reply by [date]. | Responda antes del [fecha]. | [日付]までにご返信いただけますでしょうか。 | [날짜]까지 회신 부탁드립니다. | 请在[日期]前回复。 |

### 提供信息

| 功能 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **通知** | I'd like to inform you that... | Le informo que... | 〜ことをお知らせいたします。 | 〜을 알려드립니다. | 特此通知…… |
| **更新** | Update on [topic]... | Actualización sobre... | 〜について進捗をご報告します。 | 〜 관련 진행상황 보고드립니다. | 关于……的进展更新： |
| **分享文档** | I'm sharing... | Les comparto... | 〜を共有いたします。 | 〜를 공유합니다. | 分享…… |

### 结尾 / 下一步

| 功能 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **行动呼吁** | Please let me know... | Por favor indíqueme... | ご検討のほど、よろしくお願いいたします。 | 검토 부탁드립니다. | 请告知…… |
| **可联系** | I'm available for a call... | Quedo a su disposición... | お時間のある際にご連絡いただけますと幸いです。 | 시간 되실 때 연락 주시기 바랍니다. | 方便时请联系…… |
| **跟进** | I'll follow up on [date]. | Haré seguimiento el [fecha]. | [日付]に再度ご連絡させていただきます。 | [날짜]에 다시 연락드리겠습니다. | 将于[日期]跟进。 |
| **感谢** | Thank you for your time. | Gracias por su tiempo. | お時間をいただき、ありがとうございました。 | 시간 내주셔서 감사합니다. | 谢谢您的时间。 |

---

## 速查表: 签名字段

| 元素 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **姓名** | First Last | Nombre Apellido | 姓 名 (Sei Mei) | 성명 (Seongmyeong) | 姓名 |
| **职位** | Title | Cargo | 役職 | 직함 | 职位 |
| **部门** | Department | Departamento | 部署 | 부서/팀 | 部门 |
| **公司** | Company | Empresa | 会社名 | 회사명 | 公司 |
| **电话** | +1 xxx-xxx-xxxx | +34 xxx xxx xxx | TEL: 03-xxxx-xxxx | 전화: 02-xxxx-xxxx | 电话: +86-xx-xxxxxxxx |
| **手机** | Mobile: +1 xxx-xxx-xxxx | Móvil: +34 xxx xxx xxx | 携帯: 090-xxxx-xxxx | 휴대폰: 010-xxxx-xxxx | 手机: +86-xxx-xxxx-xxxx |
| **邮箱** | email@company.com | email@empresa.es | email@company.co.jp | email@company.co.kr | email@company.cn |
| **地址** | 123 St, City, State ZIP | Calle 123, Ciudad, CP | 〒XXX-XXXX 都道府県市区町村 | 우편번호 주소 | 邮编 地址 |
| **网址** | www.company.com | www.empresa.es | www.company.co.jp | www.company.co.kr | www.company.cn |

### 中文签名模板
```
────────────────────────
姓名
职位
部门
公司
电话：+86-xx-xxxxxxxx
手机：+86-xxx-xxxx-xxxx
邮箱：xxx@xxx.com
邮编  地址
网址：https://xxx.com
────────────────────────
```

---

## 速查表: 文化规范与禁忌

| 文化 | 规范 | 禁忌 |
|------|------|------|
| **English (US/UK)** | 1-2 次交流后名字直呼 | 同事之间过于僵硬 |
| **Spanish (Spain)** | *Usted* 默认; 被邀请后才用 *tú* | 对陌生人用 *tú*; 漏 *Estimado* |
| **Spanish (LatAm)** | *Usted* 用更久; 头衔重要 | 无头衔用名字 |
| **Japanese** | *Yoroshiku* 强制; 当天回复 | 漏 *yoroshiku*; 抄送无通知 |
| **Korean** | *님* 强制; 抄送顺序体现层级 | 对上级用 *씨*; 回复上级 |
| **Chinese** | 头衔 + 姓; *qing (请)* 用于请求 | 仅用名字; 漏结尾语 |

---

## 速查表: 邮件礼仪

| 实践 | EN | ES | JP | KR | CH |
|------|----|----|----|----|----|
| **默认回复所有** | 因情境 | 因情境 | **是** (保留所有人循环) | **是** (层级) | 因情境 |
| **引用原文** | 内联或顶部回复 | 偏好内联 | 顶部回复 (完整历史) | 顶部回复 (完整历史) | 顶部回复 |
| **主题前缀** | Re: | Re: / R: | Re: / 返信: | Re: / 회신: | Re: / 回复: |
| **转发前缀** | Fwd: | Fwd: / Rv: | 転送: | 전달: | 转发: |
| **BCC 隐私** | 常见 | 常见 | 罕见 (用群件) | 罕见 | 常见 |
| **已读回执请求** | 罕见 (强迫) | 罕见 | 罕见 | 罕见 | 有时 |

---

## 速查表: 自动回复 / 不在办公室

| 语言 | 模板 |
|------|------|
| **English** | Thank you for your email. I am out of the office from [date] to [date] with limited email access. For urgent matters, please contact [Name] at [email/phone]. I will respond upon my return. |
| **Spanish** | Gracias por su correo. Estoy fuera de la oficina del [fecha] al [fecha] con acceso limitado al email. Para asuntos urgentes, contacte a [Nombre] en [email/teléfono]. Responderé a mi regreso. |
| **Japanese** | ご連絡ありがとうございます。[日付]〜[日付]まで不在にしております。緊急の場合は [名前] ([メール/電話]) までご連絡ください。戻り次第、順次ご返信いたします。 |
| **Korean** | 메일 감사합니다. [날짜]부터 [날짜]까지 부재중입니다. 긴급한 용무는 [이름] ([이메일/전화])로 연락 주시기 바랍니다. 복귀 후 순차적으로 회신드리겠습니다. |
| **Chinese** | 感谢您的来信。我将于[日期]至[日期]期间不在办公室，无法即时回复邮件。紧急事项请联系 [姓名] ([邮箱/电话])。返岗后我会尽快回复。 |

---

## 速查表: 做 / 不做

| 语言 | ✅ 做 | � 不做 |
|------|------|---------|
| **English** | 用 "please" 和 "thank you"; 简洁 | 过度致歉; 用 "kindly" (过时) |
| **Spanish** | 用 *usted* 直到被邀请到 *tú*; 含 *Estimado* | 漏称呼; 对客户用 *tú* |
| **Japanese** | 永远用 *yoroshiku onegaishimasu*; 完整签名 | 漏 *yoroshiku*; 无上下文回复 |
| **Korean** | 用 *님*; 层级感知的抄送; *수고하세요* 结尾 | 对上级用 *씨*; 不思考回复所有 |
| **Chinese** | 头衔 + 姓; *qing* 用于请求; 结尾格式 | 仅用名字; 漏结尾; 直接请求 |

---

## 中文邮件模板

### 会议请求模板 (中文)
```
主题：【会议申请】关于〇〇事宜 —— 日期协调

尊敬的 [职称] [姓]：

您好！

我是 〇〇公司 〇〇部 〇〇。

因〇〇事宜，想约请安排一次会议沟通。
不知您下周是否有空？初步建议时间如下：

1) [日期] [时间]〜
2) [日期] [时间]〜
3) [日期] [时间]〜

会议时长约 [30/60] 分钟，形式为 [视频会议/贵司拜访/电话]。

烦请告知方便时间，不胜感激。

顺颂商祺

〇〇
〇〇公司 〇〇部
电话：+86-xx-xxxxxxxx
邮箱：xxx@xxx.com
```

---

## 各语言详情

### 🇬🇧 英语
- **来源**: `[English/vocabulary/business-vocabulary]`, `[English/culture/english-dating-culture]`

### 🇪🇸 西班牙语
- **来源**: `[Spanish/vocabulary/business-vocabulary]`, `[Spanish/sources/trabajo-y-carrera]`, `[Spanish/culture/espana-vs-latinoamerica-registro]`

### 🇯🇵 日语
- **来源**: `[Japanese/vocabulary/business-vocabulary]`, `[Japanese/sources/business-email]`

### 🇰🇷 韩语
- **来源**: `[Korean/vocabulary/business-vocabulary]`, `[Korean/sources/daily-life-basics]`

### 🇨🇳 中文
- **来源**: `[Chinese/sources/greetings-zh]`, `[Chinese/sources/daily-routine-zh]`

---

## 关键对比 (综合)

| 对比 | 洞察 |
|------|------|
| **称呼层级** | 日韩最复杂 (様/님 + 公司层级); 西班牙 + 拉美正式 (Estimado + 头衔); 中文 (头衔 + 姓); 英语最随意 |
| **结尾公式** | 日韩 *yoroshiku / 잘 부탁드립니다* 强制; 西 *Atentamente*; 中 *此致敬礼 / 顺颂商祺*; 英 *Best regards* 最随意 |
| **回复所有** | 日韩几乎强制; 其他语言因情境 |
| **敬语系统** | 日韩融入动词 (です/ます / 합쇼체); 西语 usted; 中文您 + 头衔; 英语通过词汇选择 |

---

## 🇨🇳 中文学习者笔记 (Chinese Learner Notes)

> 本节是面向中文母语学习者的额外学习指南。

### 中文母语者在学习其他4种语言商务邮件时的常见陷阱

1. **结尾格式的强制 vs 可选**:
   - 中文 *此致敬礼 / 顺颂商祺* 常用 → 学员对日韩 *yoroshiku / 잘 부탁드립니다* 的强制感到困惑。
   - **陷阱**: 日韩漏 *yoroshiku / 잘 부탁드립니다* = 不完整邮件, 类似中文漏称呼。
   - **训练法**: 把日韩 *yoroshiku / 잘 부탁드립니다* 当作 *此致敬礼* 的强制版; 不要漏。

2. **称呼的"层级"**:
   - 中文 *尊敬的 [职称] [姓]* 二元 → 学员对日韩公司层级称呼感到困惑。
   - **陷阱**: 日语 *株式会社〇〇 〇〇部 〇〇様* 是 3-4 层; 韩语 *㈜○○ ○○팀 ○○님* 同样。
   - **训练法**: 学习日韩公司层级称呼模板 (公司→部门→职位→姓名)。

3. **"请" (qǐng) 的位置与功能**:
   - 中文 *请* 用于礼貌请求 → 学员对日韩 *〜ていただけますでしょうか* 感到困惑。
   - **陷阱**: 日语 *〜ていただけますでしょうか* 是动词变形; 韩语 *〜해 주시겠어요?* 同样; 中文 *请* 位置灵活。
   - **训练法**: 整理 5 语言请求模板 (EN Could you / ES ¿Podría / JP 〜いただけますでしょうか / KR 〜해 주시겠어요 / CH 能否请您)。

4. **"回复所有" 的文化差异**:
   - 中文回复所有因情境 → 学员对日韩 *必须回复所有* 感到困惑。
   - **陷阱**: 日韩邮件系统 *全員に返信* 默认; 中文邮件默认仅回复发件人。
   - **训练法**: 学习日韩邮件系统习惯; 不要漏抄送人。

5. **"对不起" 的功能差异**:
   - 中文 *对不起/抱歉* 通用 → 学员对日语 *申し訳ございません* 的重量感到困惑。
   - **陷阱**: 日语 *申し訳ございません* 极重; 韩语 *죄송합니다* 同样; 中 *抱歉* 较轻。
   - **训练法**: 整理 5 语言致歉强度 (EN Sorry / ES Disculpe / JP 申し訳ございません / KR 죄송합니다 / CH 抱歉)。

6. **敬语动词的负担**:
   - 中文 *您辛苦了* 简单 → 学员对日韩敬语动词变形感到困惑。
   - **陷阱**: 日语商务 *お疲れ様です* vs 随意 *お疲れ*; 韩语 *수고하십니까* vs 随意 *수고*.
   - **训练法**: 学习日韩敬语动词模板; 商务场景用最礼貌形式。

### 相关中文维基页面

- [Chinese/culture/chinese-business-etiquette-zh] — 中国商务礼仪
- [Chinese/vocabulary/business-titles-zh] — 中文商业职衔
- [Chinese/culture/chinese-email-style-zh] — 中文邮件风格
- [Chinese/expressions/business-greetings-zh] — 中文商务问候
- [Chinese/culture/chinese-relationships-zh] — 中国职场关系

### 学习工作流程推荐

1. **5 语言称呼对比表** (正式/同事/上级 — 5 语言)
2. **5 语言结尾公式** (yoroshiku/잘 부탁드립니다/Atentamente/此致敬礼/Best regards)
3. **5 语言请求模板** (Could you/¿Podría/〜いただけますか/〜해 주시겠어요/能否请您)
4. **5 语言自动回复模板** (不在办公室 — 5 语言)
5. **5 语言邮件礼仪** (回复所有/引用原文/主题前缀)

---

## 相关页面

- `[[politeness-honorifics]]` — 邮件风格的语域
- `[[pronouns-reference]]` — 称呼中的代词
- `[[travel-essentials]]` — 商务旅行邮件短语
- `[[food-dining]]` — 商务餐跟进邮件

## 来源

- EN: `[English/vocabulary/business-vocabulary]`, `[English/culture/english-dating-culture]`
- ES: `[Spanish/vocabulary/business-vocabulary]`, `[Spanish/sources/trabajo-y-carrera]`, `[Spanish/culture/espana-vs-latinoamerica-registro]`
- JP: `[Japanese/vocabulary/business-vocabulary]`, `[Japanese/sources/business-email]`
- KR: `[Korean/vocabulary/business-vocabulary]`, `[Korean/sources/daily-life-basics]`
- CN: `[Chinese/sources/greetings-zh]`, `[Chinese/sources/daily-routine-zh]`

---

**原文 (英语)**: [[business-email]] | **相关镜像**: [[business-email.es|西班牙语]] · [[business-email.ja|日语]] · [[business-email.ko|韩语]] | **政策**: ADR-0006
