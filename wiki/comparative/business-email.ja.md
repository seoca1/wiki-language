# ビジネスメール — 言語間比較 (日本語版)

> 原文: [[business-email]] (English) | 作成日: 2026-08-19 | ADR-0006
> **5言語のビジネスメール比較** — English · Spanish · Japanese · Korean · Chinese

---

## 早見表

### メール構造比較

| 構成要素 | English | Spanish | Japanese | Korean | Chinese |
|----------|---------|---------|----------|--------|---------|
| **件名** | Concise, specific | Concise, specific | 【件名】 + topic | [제목] + topic | 【主题】 + topic |
| **宛名** | Dear [Name], | Estimado/a [Name]: | [Name] 様 / [Company] [Title] 様 | [Name] [Title]님 / [Company] [Title]님 | 尊敬的 [Title] [Surname]： |
| **書き出し** | I hope you're well. | Espero que esté bien. | いつもお世話になっております。 | 항상 수고가 많으십니다. | 希望您一切安好。 |
| **用件** | I'm writing to... | Le escribo para... | この度は〜の件でご連絡いたしました。 | 〜건으로 메일 드립니다. | 写信是关于…… |
| **本文** | Direct, bullet-friendly | Direct, formal | Context-first, then request | Context-first, then request | Context-first, then request |
| **結び** | Best regards, | Atentamente / Cordialmente, | よろしくお願いいたします。 | 잘 부탁드립니다. | 顺颂商祺 / 此致 敬礼 |
| **署名** | Name, Title, Company, Phone | Name, Cargo, Empresa, Tel | Name, 所属, 役職, 会社, TEL | 이름, 직함, 회사, 연락처 | 姓名, 职位, 公司, 电话 |

---

## 宛名詳細

### 🇬🇧 英語 (English)
| 関係 | 宛名 |
|------|------|
| フォーマル (名前不明) | Dear Sir/Madam, / To Whom It May Concern, |
| フォーマル (名前既知) | Dear Mr./Ms./Dr. [Last], |
| 同僚・知人 | Hi [First], / Hello [First], |
| チーム・グループ | Dear Team, / Hi All, |

### 🇪🇸 スペイン語 (Spanish)
| 関係 | 宛名 |
|------|------|
| フォーマル (不明) | Estimado Señor/Señora: / Muy señor mío: |
| フォーマル (既知) | Estimado/a Sr./Sra./Dr./Dra. [Apellido]: |
| 知人 | Estimado/a [Nombre]: |
| カジュアル | Hola [Nombre]: / Querido/a [Nombre]: |

**地域差**: *Estimado* (スペイン) vs *Estimado/a* (ラ米 性一致); *Usted*  がフォーマルで暗黙

### 🇯🇵 日本語 (Japanese) — `[Japanese/sources/business-email]` 出典
| 関係 | 宛名 |
|------|------|
| 社外 (標準) | 株式会社〇〇 〇〇部 〇〇様 |
| 社外 (名前既知) | 〇〇株式会社 〇〇様 |
| 社内 (上位) | 〇〇部長 / 〇〇課長 / 〇〇様 |
| 社内 (同僚) | 〇〇さん |
| 社外返信 | 〇〇様 いつもお世話になっております。 |

**重要**: 会社 → 部署 → 役職/名前 → 様 — 社外宛で名前だけの 「name-sama」 は不可

### 🇰🇷 韓国語 (Korean) — `[Korean/sources/daily-life-basics]` 出典
| 関係 | 宛名 |
|------|------|
| 社外 (標準) | ㈜○○ ○○팀 ○○님 / ○○부장님 |
| 社外 (既知) | ○○님 |
| 社内 (上位) | ○○팀장님 / ○○부장님 / ○○선배님 |
| 社内 (同僚) | ○○님 / ○○씨 |
| 社外返信 | ○○님, 항상 수고가 많으십니다. |

**重要**: 会社 → チーム → 役職 + 님 — *님* 尊敬に必須; *씨* は同僚・部下のみ

### 🇨🇳 中国語 (Chinese)
| 関係 | 宛名 |
|------|------|
| フォーマル (不明) | 尊敬的先生/女士： |
| フォーマル (既知) | 尊敬的 [职称] [姓]： (经理/总监/教授) |
| 知人 | 尊敬的 [姓] [职称]： |
| カジュアル | [姓] [职称] 你好： / 各位同事： |

**重要**: 役職は姓の後 (王经理, 李总监) — ビジネスでファーストネームは不可

---

## 機能別標準フレーズ

### 書き出し / 文脈設定

| 機能 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **前回連絡の参照** | Further to our conversation... | En referencia a nuestra conversación... | 先日はお話しいただき、ありがとうございました。 | 앞서 통화한 내용과 관련하여... | 承接我们上次的沟通…… |
| **添付ファイル参照** | Please find attached... | Adjunto encontrará... | 添付ファイルをご確認ください。 | 첨부파일 확인 부탁드립니다. | 请查收附件…… |
| **返信確認** | Thank you for your email. | Gracias por su correo. | メールをいただき、ありがとうございます。 | 메일 주셔서 감사합니다. | 收到您的邮件，谢谢。 |
| **遅延謝罪** | Apologies for the late reply. | Disculpe la demora. | 返信が遅くなり、申し訳ございません。 | 답장이 늦어져 죄송합니다. | 回复较晚，抱歉。 |

### 依頼

| 機能 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **丁寧な依頼** | Could you please...? | ¿Podría... por favor? | 〜していただけますでしょうか。 | 〜해 주시겠어요? | 能否请您…… |
| **フォーマル依頼** | I would appreciate it if... | Agradecería que... | 〜ていただけますと幸いです。 | 〜해 주시면 감사하겠습니다. | 如果能……将不胜感激。 |
| **確認依頼** | Please confirm... | Por favor confirme... | ご確認のほど、よろしくお願いいたします。 | 확인 부탁드립니다. | 请确认…… |
| **期限付き返信依頼** | Please reply by [date]. | Responda antes del [fecha]. | [日付]までにご返信いただけますでしょうか。 | [날짜]까지 회신 부탁드립니다. | 请在[日期]前回复。 |

### 情報提供

| 機能 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **通知** | I'd like to inform you that... | Le informo que... | 〜ことをお知らせいたします。 | 〜을 알려드립니다. | 特此通知…… |
| **進捗報告** | Update on [topic]... | Actualización sobre... | 〜について進捗をご報告します。 | 〜 관련 진행상황 보고드립니다. | 关于……的进展更新： |
| **文書共有** | I'm sharing... | Les comparto... | 〜を共有いたします。 | 〜를 공유합니다. | 分享…… |

### 結び / 次のステップ

| 機能 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **行動喚起** | Please let me know... | Por favor indíqueme... | ご検討のほど、よろしくお願いいたします。 | 검토 부탁드립니다. | 请告知…… |
| **対応可能** | I'm available for a call... | Quedo a su disposición... | お時間のある際にご連絡いただけますと幸いです。 | 시간 되실 때 연락 주시기 바랍니다. | 方便时请联系…… |
| **フォローアップ** | I'll follow up on [date]. | Haré seguimiento el [fecha]. | [日付]に再度ご連絡させていただきます。 | [날짜]에 다시 연락드리겠습니다. | 将于[日期]跟进。 |
| **感謝** | Thank you for your time. | Gracias por su tiempo. | お時間をいただき、ありがとうございました。 | 시간 내주셔서 감사합니다. | 谢谢您的时间。 |

---

## 結びの定型

### 🇬🇧 英語 (English)
| フォーマリティ | 結び |
|-----------|---------|
| 非常にフォーマル | Respectfully, / Yours faithfully, (UK: 受信者不明) |
| フォーマル | Sincerely, / Yours sincerely, (UK: 既知) |
| 標準 | Best regards, / Kind regards, / Regards, |
| 親しい | Best, / Warm regards, / All the best, |
| カジュアル・社内 | Thanks, / Cheers, (UK/AU) |

### 🇪🇸 スペイン語 (Spanish)
| フォーマリティ | 結び |
|-----------|---------|
| 非常にフォーマル | Atentamente, / Muy atentamente, |
| フォーマル | Cordialmente, / Un cordial saludo, |
| 標準 | Saludos cordiales, / Atentamente, |
| 親しい | Un abrazo, / Un saludo afectuoso, |
| カジュアル・社内 | Saludos, / Hasta luego, |

**ラ米**: *Quedo a su disposición* が結びの前に一般的

### 🇯🇵 日本語 (Japanese) — `[Japanese/sources/business-email]` 出典
| フォーマリティ | 結び |
|-----------|---------|
| 社外標準 | よろしくお願いいたします。 |
| 行動依頼 | ご検討のほど、よろしくお願いいたします。 |
| 会食後 | お会いできましたら幸いです。よろしくお願いいたします。 |
| 社内 (上位) | 以上、よろしくお願いいたします。 |
| 社内 (同僚) | よろしくお願いします。 / 以上です。 |

**省略禁止** — 社内メールでも *yoroshiku onegaishimasu* で終わる

### 🇰🇷 韓国語 (Korean) — `[Korean/sources/daily-life-basics]` 出典
| フォーマリティ | 結び |
|-----------|---------|
| 社外標準 | 잘 부탁드립니다. / 감사합니다. |
| 行動依頼 | 검토 부탁드립니다. / 확인 부탁드립니다. |
| 会食後 | 뵙기를 희망합니다. 잘 부탁드립니다. |
| 社内 (上位) | 이상입니다. 잘 부탁드립니다. |
| 社内 (同僚) | 잘 부탁해요. / 수고하세요. |

**Note**: *수고하세요* (相手が残る場合) vs *수고하십시오* (相手が出る場合) — メール結びは *수고하세요*

### 🇨🇳 中国語 (Chinese)
| フォーマリティ | 結び |
|-----------|---------|
| 非常にフォーマル | 顺颂商祺 / 此致 敬礼 |
| フォーマル | 此致 敬礼 / 顺祝 工作顺利 |
| 標準 | 祝好 / 顺祝 安好 |
| 知人 | 祝好 / 期待回复 |
| カジュアル・社内 | 谢谢 / 祝顺利 |

---

## 署名欄規格

| 要素 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **名前** | First Last | Nombre Apellido | 姓 名 (Sei Mei) | 성명 (Seongmyeong) | 姓名 |
| **役職** | Title | Cargo | 役職 | 직함 | 职位 |
| **部署** | Department | Departamento | 部署 | 부서/팀 | 部门 |
| **会社** | Company | Empresa | 会社名 | 회사명 | 公司 |
| **電話** | +1 xxx-xxx-xxxx | +34 xxx xxx xxx | TEL: 03-xxxx-xxxx | 전화: 02-xxxx-xxxx | 电话: +86-xx-xxxxxxxx |
| **携帯** | Mobile: +1 xxx-xxx-xxxx | Móvil: +34 xxx xxx xxx | 携帯: 090-xxxx-xxxx | 휴대폰: 010-xxxx-xxxx | 手机: +86-xxx-xxxx-xxxx |
| **メール** | email@company.com | email@empresa.es | email@company.co.jp | email@company.co.kr | email@company.cn |
| **住所** | 123 St, City, State ZIP | Calle 123, Ciudad, CP | 〒XXX-XXXX 都道府県市区町村 | 우편번호 주소 | 邮编 地址 |
| **URL** | www.company.com | www.empresa.es | www.company.co.jp | www.company.co.kr | www.company.cn |

### 🇯🇵 日本語署名例
```
────────────────────────
株式会社〇〇 〇〇部
部長 〇〇 〇〇
TEL: 03-xxxx-xxxx / FAX: 03-xxxx-xxxx
Mobile: 090-xxxx-xxxx
Email: xxxx@xxx.co.jp
〒100-0001 東京都千代田区〇〇 1-1-1
URL: https://xxx.co.jp
────────────────────────
```

### 🇰🇷 韓国語署名例
```
────────────────────────
㈜○○  ○○팀
팀장  김철수
전화: 02-xxxx-xxxx / 팩스: 02-xxxx-xxxx
휴대폰: 010-xxxx-xxxx
이메일: kim@xxx.co.kr
우)06000 서울시 강남구 ○○로 123
홈페이지: https://xxx.co.kr
────────────────────────
```

---

## 文化的規範・タブー

| 文化 | 規範 | タブー |
|------|------|-------|
| **英語 (米/英)** | 1-2回のやり取り後にファーストネーム | 同僚に過度に堅い言葉 |
| **スペイン語 (スペイン)** | *Usted* デフォルト; 招待後に *tú* | 見知らぬ人に *Tú*; *Estimado* 省略 |
| **スペイン語 (ラ米)** | *Usted* が長く持続; 役職重要 | 役職なしのファーストネーム |
| **日本語** | *Yoroshiku* 必須; 翌日返信 | *yoroshiku* 省略; 事前通知なしの CC |
| **韓国語** | *님* 必須; CC の階層 | 上司に *씨*; 上司への返信で上 |
| **中国語** | 役職 + 姓; 依頼に *qing* (请) | ファーストネーム; 結び定型省略 |

---

## メールスレッド作法

| 実践 | EN | ES | JP | KR | CH |
|------|----|----|----|----|----|
| **全員に返信デフォルト** | 状況次第 | 状況次第 | **Yes** (全員を含める) | **Yes** (階層) | 状況次第 |
| **原文引用** | インラインまたはトップポスト | インライン推奨 | トップポスト (全履歴) | トップポスト (全履歴) | トップポスト |
| **件名プレフィックス** | Re: | Re: / R: | Re: / 返信: | Re: / 회신: | Re: / 回复: |
| **転送プレフィックス** | Fwd: | Fwd: / Rv: | 転送: | 전달: | 转发: |
| **BCC (プライバシー)** | 一般的 | 一般的 | 稀 (グループウェア使用) | 稀 | 一般的 |
| **開封確認要求** | 稀 (押しが強い) | 稀 | 稀 | 稀 | 時々 |

---

## 会議依頼テンプレート

### 🇬🇧 英語
```
Subject: Meeting Request: [Topic] — [Date Options]

Dear [Name],

I'd like to schedule a meeting to discuss [topic]. 
Are you available on [date] at [time] or [alt date] at [alt time]? 
The meeting would be [30/60] minutes via [Zoom/Teams/in-person].

Please let me know what works best.

Best regards,
[Name]
```

### 🇪🇸 スペイン語
```
Asunto: Solicitud de reunión: [Tema] — [Opciones de fecha]

Estimado/a [Nombre]:

Le escribo para concertar una reunión sobre [tema].
¿Tiene disponibilidad el [fecha] a las [hora] o el [fecha alternativa] a las [hora alternativa]?
La reunión duraría [30/60] minutos por [Zoom/Teams/presencial].

Quedo a la espera de su confirmación.

Atentamente,
[Nombre]
```

### 🇯🇵 日本語 (`[Japanese/sources/business-email]` 出典)
```
件名：【ご相談】〇〇の件について（日程調整のお願い）

〇〇株式会社
〇〇部 〇〇様

いつもお世話になっております。
株式会社△△の〇〇でございます。

表題の件につきまして、ご相談させていただきたく、
ご多忙のところ恐縮ですが、お時間をいただけますでしょうか。

候補日時：
① [日付] [時間]〜
② [日付] [時間]〜
③ [日付] [時間]〜

所要時間：[30/60]分程度
形式：[Web会議/御社訪問/電話]

ご都合のよい日時をご教示いただけますと幸いです。
よろしくお願いいたします。

────────────────────────
株式会社△△ 〇〇部
部長 〇〇 〇〇
...
```

### 🇰🇷 韓国語
```
제목: [요청] 〇〇 건 관련 미팅 일정 조율 요청

㈜○○  〇〇팀  〇〇님

항상 수고가 많으십니다.
㈜△△  〇〇팀  〇〇입니다.

다름이 아니라 〇〇 건과 관련하여 미팅을 요청드리고자 합니다.
바쁘시겠지만 아래 일정 중 가능한 시간을 알려주시면 감사하겠습니다.

후보 일시:
1) [날짜] [시간]〜
2) [날짜] [시간]〜
3) [날짜] [시간]〜

소요 시간: 약 [30/60]분
방식: [화상회의/방문/유선]

검토 부탁드립니다.

잘 부탁드립니다.

────────────────────────
㈜△△  〇〇팀
팀장  〇〇  〇〇
...
```

### 🇨🇳 中国語
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

## 不在時自動返信

| 言語 | テンプレート |
|----------|----------|
| **English** | Thank you for your email. I am out of the office from [date] to [date] with limited email access. For urgent matters, please contact [Name] at [email/phone]. I will respond upon my return. |
| **Spanish** | Gracias por su correo. Estoy fuera de la oficina del [fecha] al [fecha] con acceso limitado al email. Para asuntos urgentes, contacte a [Nombre] en [email/teléfono]. Responderé a mi regreso. |
| **Japanese** | ご連絡ありがとうございます。[日付]〜[日付]まで不在にしております。緊急の場合は [名前] ([メール/電話]) までご連絡ください。戻り次第、順次ご返信いたします。 |
| **Korean** | 메일 감사합니다. [날짜]부터 [날짜]까지 부재중입니다. 긴급한 용무는 [이름] ([이메일/전화])로 연락 주시기 바랍니다. 복귀 후 순차적으로 회신드리겠습니다. |
| **Chinese** | 感谢您的来信。我将于[日期]至[日期]期间不在办公室，无法即时回复邮件。紧急事项请联系 [姓名] ([邮箱/电话])。返岗后我会尽快回复。 |

---

## 学習者決定ガイド

| 言語 | ✅ Do | ❌ Don't |
|----------|------|------|
| **English** | "please" と "thank you" を使用; 簡潔に | 過剰に謝罪; "kindly" (dated) |
| **Spanish** | 招待されるまで *usted*; *Estimado* を含める | 宛名省略; クライアントに *tú* |
| **Japanese** | 常に *yoroshiku onegaishimasu*; 完全な署名 | *yoroshiku* 省略; 文脈なしの返信 |
| **Korean** | *님* 使用; 階層を意識した cc; *수고하세요* 結び | 上司に *씨*; 熟考なしの reply-all |
| **Chinese** | 役職 + 姓; 依頼に *qing*; 結び定型 | ファーストネームのみ; 結び省略; ぶっきらぼうな依頼 |

---

## 🇯🇵 日本語学習者ノート (Japanese Learner Notes)

> 本セクションは日本語学習者向けの追加学習ガイドです。

### 日本語話者が他の4言語のビジネスメールを書く際の一般的な落とし穴

1. **過剰敬語の英語への転移**:
   - 日本語の「いつもお世話になっております」「よろしくお願いいたします」を英語に直訳すると不自然。
   - **落とし穴**: 英語で "I always appreciate your kindness" のような過剰表現。
   - **練習法**: 英語は "I hope you're well" → 用件 → "Best regards" のシンプル構造。

2. **敬称省略の失敗 (英語・中国語)**:
   - 日本語は社内では「○○さん」「○○部長」で十分 → 英語/中国語では役職+姓が必要。
   - **落とし穴**: 英語メールで "Hi John" のようなファーストネーム呼び; 中国語で役職なしの宛名。
   - **練習法**: 初対は "Dear Mr./Ms. [Last]" / "尊敬的 [职称] [姓]" を徹底。

3. **件名の簡潔さ**:
   - 日本語の件名は「【ご相談】〇〇の件」程度 → 英語/中国語では件名にもっと具体的に。
   - **落とし穴**: 英語メールで "Subject: Question" のような曖昧件名。
   - **練習法**: 件名 = "Meeting Request: [Topic] — [Date Options]" 形式を定型化。

4. **結びの文化差**:
   - 日本語の「よろしくお願いいたします」は英語では不要 → 英語では "Best regards" のみ。
   - **落とし穴**: 英語メールで "I humbly request" のような翻訳直訳。
   - **練習法**: 各言語の標準結び定型を暗記。

5. **添付ファイル参照の表現**:
   - 日本語「添付ファイルをご確認ください」 → 英語 "Please find attached..." は定型だが、現在ではカジュアルに "I've attached..." も可。
   - **練習法**: 英語は状況に応じて "Please find attached" (formal) / "Attaching..." (modern) を使い分け。

### 関連日本語ウィキページ

- [Japanese/sources/business-email] — 日本語ビジネスメール出典
- [Japanese/vocabulary/business-vocabulary] — ビジネス語彙
- [Japanese/expressions/polite-expressions] — 敬語表現
- [Japanese/grammar/japanese-keigo] — 敬語システム
- [Japanese/culture/japanese-workplace-culture] — 日本の職場文化

### 学習ワークフロー推奨

1. **5言語の定型句暗記表作成** (宛名、書き出し、結び)
2. **社内・社外テンプレ作成** (5言語 × 2 = 10パターン)
3. **ロールプレイ** (ビジネスメールを5言語で書く練習)
4. **実例分析** (受信したビジネスメールを5言語で分析)
5. **文化規範チェックリスト** (各言語のタブーを確認)

---

## 関連ページ

- `[[politeness-honorifics]]` — メールスタイルを支える register システム
- `[[pronouns-reference]]` — 宛名の pronouns
- `[[travel-essentials]]` — 出張メールフレーズ
- `[[food-dining]]` — ビジネス会食後のフォローアップメール

## 出典

- English: `[English/vocabulary/business-vocabulary]`, `[English/culture/english-dating-culture]`
- Spanish: `[Spanish/vocabulary/business-vocabulary]`, `[Spanish/sources/trabajo-y-carrera]`, `[Spanish/culture/espana-vs-latinoamerica-registro]`
- Japanese: `[Japanese/vocabulary/business-vocabulary]`, `[Japanese/sources/business-email]`
- Korean: `[Korean/vocabulary/business-vocabulary]`, `[Korean/sources/daily-life-basics]`
- Chinese: `[Chinese/sources/greetings-zh]`, `[Chinese/sources/daily-routine-zh]`

---

**原文 (英語)**: [[business-email]] | **関連ミラー**: [[business-email.es|スペイン語]] · [[business-email.ko|韓国語]] · [[business-email.zh|中国語]] | **ポリシー**: ADR-0006