# 비즈니스 이메일 — Cross-Language Comparison (한국어판)

> 원본: [[business-email]] (English) | 작성일: 2026-08-19 | ADR-0006
> **5개 언어 비즈니스 이메일 비교** — English · Spanish · Japanese · Korean · Chinese

---

## 빠른 참조 표

### 이메일 구조 비교

| Component | English | Spanish | Japanese | Korean | Chinese |
|-----------|---------|---------|----------|--------|---------|
| **제목** | 간결, 구체적 | 간결, 구체적 | 【件名】 + 제목 | [제목] + 제목 | 【主题】 + 제목 |
| **인사** | Dear [Name], | Estimado/a [Name]: | [Name] 様 / [Company] [Title] 様 | [Name] [Title]님 / [Company] [Title]님 | 尊敬的 [Title] [Surname]： |
| **도입** | I hope you're well. | Espero que esté bien. | いつもお世話になっております。 | 항상 수고가 많으십니다. | 希望您一切安好。 |
| **목적 진술** | I'm writing to... | Le escribo para... | この度は〜の件でご連絡いたしました。 | 〜건으로 메일 드립니다. | 写信是关于…… |
| **본문** | 직접, 글머리표 친화 | 직접, 격식 | 맥락 먼저, 요청 후 | 맥락 먼저, 요청 후 | 맥락 먼저, 요청 후 |
| **마무리** | Best regards, | Atentamente / Cordialmente, | よろしくお願いいたします。 | 잘 부탁드립니다. | 顺颂商祺 / 此致 敬礼 |
| **서명** | Name, Title, Company, Phone | Name, Cargo, Empresa, Tel | Name, 所属, 役職, 会社, TEL | 이름, 직함, 회사, 연락처 | 姓名, 职位, 公司, 电话 |

---

## 인사 디테일

### 🇬🇧 영어 (English)

| 관계 | 인사 |
|------|------|
| 격식 (이름 모름) | Dear Sir/Madam, / To Whom It May Concern, |
| 격식 (이름 앎) | Dear Mr./Ms./Dr. [Last], |
| 동료/지인 | Hi [First], / Hello [First], |
| 팀/그룹 | Dear Team, / Hi All, |

### 🇪🇸 스페인어 (Spanish)

| 관계 | 인사 |
|------|------|
| 격식 (모름) | Estimado Señor/Señora: / Muy señor mío: |
| 격식 (앎) | Estimado/a Sr./Sra./Dr./Dra. [Apellido]: |
| 지인 | Estimado/a [Nombre]: |
| 덜 격식 | Hola [Nombre]: / Querido/a [Nombre]: |

**지역 변이**: *Estimado* (스페인) vs *Estimado/a* (라틴아메리카 성별 일치); 격식 시 *Usted* 함축

### 🇯🇵 일본어 (Japanese)

| 관계 | 인사 |
|------|------|
| 외부 (표준) | 株式会社〇〇 〇〇部 〇〇様 |
| 외부 (이름 앎) | 〇〇株式会社 〇〇様 |
| 내부 (상급자) | 〇〇部長 / 〇〇課長 / 〇〇様 |
| 내부 (동료) | 〇〇さん |
| 외부 회신 | 〇〇様 いつもお世話になっております。 |

**핵심**: 회사 → 부서 → 직함/이름 → 様 — 외부에서 이름만 + sama 는 절대 금지

### 🇰🇷 한국어 (Korean)

| 관계 | 인사 |
|------|------|
| 외부 (표준) | ㈜○○ ○○팀 ○○님 / ○○부장님 |
| 외부 (앎) | ○○님 |
| 내부 (상급자) | ○○팀장님 / ○○부장님 / ○○선배님 |
| 내부 (동료) | ○○님 / ○○씨 |
| 외부 회신 | ○○님, 항상 수고가 많으십니다. |

**핵심**: 회사 → 팀 → 직함 + 님 — *님* 존경 필수; *씨* 는 동료/부하만

### 🇨🇳 중국어 (Chinese)

| 관계 | 인사 |
|------|------|
| 격식 (모름) | 尊敬的先生/女士： |
| 격식 (앎) | 尊敬的 [职称] [姓]： (经理/总监/教授) |
| 지인 | 尊敬的 [姓] [职称]： |
| 덜 격식 | [姓] [职称] 你好： / 各位同事： |

**핵심**: 직함은 성 뒤 (王经理, 李总监) — 비즈니스에서 이름 단독 사용 금지

---

## 기능별 표준 표현

### 도입 / 맥락 설정

| 기능 | English | Spanish | Japanese | Korean | Chinese |
|----------|---------|---------|----------|--------|---------|
| **이전 연락 참조** | Further to our conversation... | En referencia a nuestra conversación... | 先日はお話しいただき、ありがとうございました。 | 앞서 통화한 내용과 관련하여... | 承接我们上次的沟通…… |
| **첨부 참조** | Please find attached... | Adjunto encontrará... | 添付ファイルをご確認ください。 | 첨부파일 확인 부탁드립니다. | 请查收附件…… |
| **회신 감사** | Thank you for your email. | Gracias por su correo. | メールをいただき、ありがとうございます。 | 메일 주셔서 감사합니다. | 收到您的邮件，谢谢。 |
| **지연 사과** | Apologies for the late reply. | Disculpe la demora. | 返信が遅くなり、申し訳ございません。 | 답장이 늦어져 죄송합니다. | 回复较晚，抱歉。 |

### 요청

| 기능 | English | Spanish | Japanese | Korean | Chinese |
|----------|---------|---------|----------|---------|---------|
| **정중한 요청** | Could you please...? | ¿Podría... por favor? | 〜していただけますでしょうか。 | 〜해 주시겠어요? | 能否请您…… |
| **격식 요청** | I would appreciate it if... | Agradecería que... | 〜ていただけますと幸いです。 | | 如果能……将不胜感激。 |
| **확인 요청** | Please confirm... | Por favor confirme... | ご確認のほど、よろしくお願いいたします。 | 확인 부탁드립니다. | 请确认…… |
| **날짜 지정 회신 요청** | Please reply by [date]. | Responda antes del [fecha]. | [日付]までにご返信いただけますでしょうか。 | [날짜]까지 회신 부탁드립니다. | 请在[日期]前回复。 |

### 정보 제공

| 기능 | English | Spanish | Japanese | Korean | Chinese |
|----------|---------|---------|----------|--------|---------|
| **통보** | I'd like to inform you that... | Le informo que... | 〜ことをお知らせいたします。 | 〜을 알려드립니다. | 特此通知…… |
| **업데이트** | Update on [topic]... | Actualización sobre... | 〜について進捗をご報告します。 | | 关于……的进展更新： |
| **문서 공유** | I'm sharing... | Les comparto... | 〜を共有いたします。 | 〜를 공유합니다. | 分享…… |

### 마무리 / 다음 단계

| 기능 | English | Spanish | Japanese | Korean | Chinese |
|----------|---------|---------|----------|--------|---------|
| **행동 촉구** | Please let me know... | Por favor indíqueme... | ご検討のほど、よろしくお願いいたします。 | 검토 부탁드립니다. | 请告知…… |
| **연락 가능** | I'm available for a call... | Quedo a su disposición... | お時間のある際にご連絡いただけますと幸いです。 | 시간 되실 때 연락 주시기 바랍니다. | 方便时请联系…… |
| **후속 조치** | I'll follow up on [date]. | Haré seguimiento el [fecha]. | [日付]に再度ご連絡させていただきます。 | [날짜]에 다시 연락드리겠습니다. | 将于[日期]跟进。 |
| **감사** | Thank you for your time. | Gracias por su tiempo. | お時間をいただき、ありがとうございました。 | 시간 내주셔서 감사합니다. | 谢谢您的时间。 |

---

## 서명 공식

### 🇬🇧 영어 (English)

| 격식도 | 마무리 |
|-----------|---------|
| 매우 격식 | Respectfully, / Yours faithfully, (UK: 받는 사람 모름) |
| 격식 | Sincerely, / Yours sincerely, (UK: 받는 사람 앎) |
| 표준 비즈니스 | Best regards, / Kind regards, / Regards, |
| 따뜻함/지인 | Best, / Warm regards, / All the best, |
| 캐주얼/내부 | Thanks, / Cheers, (UK/AU) |

### 🇪🇸 스페인어 (Spanish)

| 격식도 | 마무리 |
|-----------|---------|
| 매우 격식 | Atentamente, / Muy atentamente, |
| 격식 | Cordialmente, / Un cordial saludo, |
| 표준 비즈니스 | Saludos cordiales, / Atentamente, |
| 따뜻함/지인 | Un abrazo, / Un saludo afectuoso, |
| 캐주얼/내부 | Saludos, / Hasta luego, |

**라틴아메리카**: 마무리 전 *Quedo a su disposición* 흔함

### 🇯🇵 일본어 (Japanese)

| 격식도 | 마무리 |
|-----------|---------|
| 표준 외부 | よろしくお願いいたします。 |
| 행동 요청 | ご検討のほど、よろしくお願いいたします。 |
| 미팅 후 | お会いできましたら幸いです。よろしくお願いいたします。 |
| 내부 (상급자) | 以上、よろしくお願いいたします。 |
| 내부 (동료) | よろしくお願いします。 / 以上です。 |

**절대 생략 금지** — 내부 이메일도 *yoroshiku onegaishimasu* 로 끝남

### 🇰🇷 한국어 (Korean)

| 격식도 | 마무리 |
|-----------|---------|
| 표준 외부 | 잘 부탁드립니다. / 감사합니다. |
| 행동 요청 | 검토 부탁드립니다. / 확인 부탁드립니다. |
| 미팅 후 | 뵙기를 희망합니다. 잘 부탁드립니다. |
| 내부 (상급자) | 이상입니다. 잘 부탁드립니다. |
| 내부 (동료) | 잘 부탁해요. / 수고하세요. |

**참고**: *수고하세요* (남아 있는 사람에게) vs *수고하십시오* (떠나는 사람에게) — 이메일 마무리에서는 *수고하세요* 사용

### 🇨🇳 중국어 (Chinese)

| 격식도 | 마무리 |
|-----------|---------|
| 매우 격식 | 顺颂商祺 / 此致 敬礼 |
| 격식 | 此致 敬礼 / 顺祝 工作顺利 |
| 표준 비즈니스 | 祝好 / 顺祝 安好 |
| 지인 | 祝好 / 期待回复 |
| 캐주얼/내부 | 谢谢 / 祝顺利 |

---

## 서명 블록 표준

| 요소 | English | Spanish | Japanese | Korean | Chinese |
|---------|---------|---------|----------|--------|---------|
| **이름** | First Last | Nombre Apellido | 姓 名 (Sei Mei) | 성명 (Seongmyeong) | 姓名 |
| **직함** | Title | Cargo | 役職 | 직함 | 职位 |
| **부서** | Department | Departamento | 部署 | 부서/팀 | 部门 |
| **회사** | Company | Empresa | 会社名 | 회사명 | 公司 |
| **전화** | +1 xxx-xxx-xxxx | +34 xxx xxx xxx | TEL: 03-xxxx-xxxx | 전화: 02-xxxx-xxxx | 电话: +86-xx-xxxxxxxx |
| **휴대폰** | Mobile: +1 xxx-xxx-xxxx | Móvil: +34 xxx xxx xxx | 携帯: 090-xxxx-xxxx | 휴대폰: 010-xxxx-xxxx | 手机: +86-xxx-xxxx-xxxx |
| **이메일** | email@company.com | email@empresa.es | email@company.co.jp | email@company.co.kr | email@company.cn |
| **주소** | 123 St, City, State ZIP | Calle 123, Ciudad, CP | 〒XXX-XXXX 都道府県市区町村 | 우편번호 주소 | 邮编 地址 |
| **웹사이트** | www.company.com | www.empresa.es | www.company.co.jp | www.company.co.kr | www.company.cn |

### 🇯🇵 일본어 서명 예
```
────────────────────────
株式会社〇〇 〇〇部
部長 〇〇 〇〇
TEL: 03-xxxx-xxxx / FAX: 03-xxxx-xxxx
Mobile: 090-xxxx-xxxx
Email: xxxxx@xxx.co.jp
〒100-0001 東京都千代田区〇〇 1-1-1
URL: https://xxx.co.jp
────────────────────────
```

### 🇰🇷 한국어 서명 예
```
────────────────────────
㈜○○  ○○○
팀장  김철수
전화: 02-xxxx-xxxx / 팩스: 02-xxxx-xxxx
휴대폰: 010-xxxx-xxxx
이메일: kim@xxx.co.kr
우)06000 서울시 강남구 ○○로 123
홈페이지: https://xxx.co.kr
────────────────────────
```

---

## 문화적 규범 & 금기

| 문화 | 규범 | 금기 |
|---------|------|-------|
| **English (US/UK)** | 1-2회 교환 후 first-name | 과도하게 딱딱한 언어 (동료에게) |
| **Spanish (Spain)** | *Usted* 기본; *tú* 초대 후 | *Tú* 낯선 사람에게; *Estimado* 생략 |
| **Spanish (LatAm)** | *Usted* 장기; 직함 중요 | 직함 없이 이름 단독 |
| **Japanese** | *Yoroshiku* 필수; 당일 회신 | *Yoroshiku* 생략; 통보 없이 cc |
| **Korean** | *님* 필수; cc 계층 | *씨* 상급자; 상급자보다 먼저 회신 |
| **Chinese** | 직함 + 성; *qing* (请) 요청 | 이름 단독; 마무리 공식 생략 |

---

## 이메일 스레드 에티켓

| 관행 | EN | ES | JP | KR | CH |
|----------|----|----|----|----|----|
| **Reply-All 기본** | 맥락 의존 | 맥락 의존 | **예** (모두 참여) | **예** (계층) | 맥락 의존 |
| **원문 인용** | 인라인 또는 top-post | 인라인 선호 | Top-post (전체 이력) | Top-post (전체 이력) | Top-post |
| **제목 접두사** | Re: | Re: / R: | Re: / 返信: | Re: / 회신: | Re: / 回复: |
| **전달 접두사** | Fwd: | Fwd: / Rv: | 転送: | 전달: | 转发: |
| **프라이버시 BCC** | 흔함 | 흔함 | 드물 (그룹웨어 사용) | 드물 | 흔함 |
| **읽음 확인 요청** | 드물 (공격적) | 드물 | 드물 | 드물 | 가끔 |

---

## 회의 요청 템플릿

### 🇬🇧 영어 (English)
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

### 🇪🇸 스페인어 (Spanish)
```
Asunto: Solicitud de reunión: [Tema] — [Opciones de fecha]

Estimado/a [Nombre]:

Le escribo para concertar una reunión sobre [tema].
¿Tiene disponibilidad el [fecha] a las [hora] o el [fecha alternativa] a la [hora alternativa]?
La reunión duraría [30/60] minutos por [Zoom/Teams/presencial].

Quedo a la espera de su confirmación.

Atentamente,
[Nombre]
```

### 🇯🇵 일본어 (Japanese)
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

### 🇰🇷 한국어 (Korean)
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

### 🇨🇳 중국어 (Chinese)
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

## 부재중 / 자동 회신

| 언어 | 템플릿 |
|----------|----------|
| **English** | Thank you for your email. I am out of the office from [date] to [date] with limited email access. For urgent matters, please contact [Name] at [email/phone]. I will respond upon my return. |
| **Spanish** | Gracias por su correo. Estoy fuera de la oficina del [fecha] al [fecha] con acceso limitado al email. Para asuntos urgentes, contacte a [Nombre] en [email/teléfono]. Responderé a mi regreso. |
| **Japanese** | ご連絡ありがとうございます。[日付]〜[日付]まで不在にしております。緊急の場合は [名前] ([メール/電話]) までご連絡ください。戻り次第、順次ご返信いたします。 |
| **Korean** | 메일 감사합니다. [날짜]부터 [날짜]까지 부재중입니다. 긴급한 용무는 [이름] ([이메일/전화])로 연락 주시기 바랍니다. 복귀 후 순차적으로 회신드리겠습니다. |
| **Chinese** | 感谢您的来信。我将于[日期]至[日期]期间不在办公室，无法即时回复邮件。紧急事项请联系 [姓名] ([邮箱/电话])。返岗后我会尽快回复。 |

---

## 학습자 의사결정 가이드

- **마스터해야 할 첫 10 표현**:
  - EN: Dear, Hello, Best regards, Sincerely, Please find attached, I would appreciate, Thank you for your time, Apologies for the late reply, Please confirm, I am available for a call
  - ES: Estimado/a, Atentamente, Cordialmente, Adjunto, Quedo a la espera, Le agradecería, Gracias por su tiempo, Disculpe la demora, Por favor confirme, Quedo a su disposición
  - JP: いつもお世話になっております, よろしくお願いいたします, 添付ファイルをご確認ください, ご確認のほど、, 承知しました, お返事をお待ちしております, 失礼いたします, お時間をいただきありがとうございます, ご検討のほど、, お手数おかけいたします
  - KR: 항상 수고가 많으십니다, 잘 부탁드립니다, 첨부파일 확인 부탁드립니다, 검토 부탁드립니다, 알겠습니다, 회신 기다리겠습니다, 실례합니다, 시간 내주셔서 감사합니다, 확인 부탁드립니다, 시간 되실 때 연락 주시기 바랍니다
  - CH: 您好, 此致敬礼, 顺颂商祺, 请查收附件, 敬请确认, 静候回复, 非常抱歉, 谢谢您的时间, 请确认, 方便时请联系

---

## 🇰🇷 한국어 학습자 노트 (Korean Learner Notes)

> 본 섹션은 한국어 학습자 대상의 추가 학습 가이드입니다.

### 한국어 화자가 다른 4개 언어 비즈니스 이메일을 배울 때 흔히 마주치는 함정

1. **"-님/-씨/-様/先生" 호칭 시스템 차이**:
   - 한국어 "-님" 은 존경 (상급자/외부), "-씨" 는 동료/하급자 — 명확한 2-tier 구분. 영어 "Mr./Ms." + 성은 격식, first-name 은 캐주얼.
   - **함정**: 일본어 様 (sama) / さん (san) / 先生 (sensei) 의 3-tier 시스템을 한국어 2-tier 로 단순 매핑 → 先生 를 모든 직함에 사용하면 과잉 존경.
   - **훈련법**: 각 언어 호칭 시스템 학습 — EN: Mr./Ms./Mx. + 성 + First name 캐주얼 / ES: Sr./Sra. + 성 또는 Nombre (친밀) / JP: 様 (외부) / さん (동료) / 先生 (교수·의사·변호사) / KR: 님 (외부) / 씨 (동료) / 한글성함 (친밀) / CN: 老师/经理 (직함) + 성.

2. **"항상 수고가 많으십니다" 의 일본어 매핑 함정**:
   - 한국어 "항상 수고하십니다" = 표준 비즈니스 도입 — 일본어 "いつもお世話になっております" 와 매우 유사하나 한국은 더 강조. 영어/I hope you're well / 스페인어 Espero que esté bien / 중국어 希望您一切安好 와 다른 의미.
   - **함정**: 영어 비즈니스 이메일에서 "I hope you're well" 를 매번 반복 → 캐주얼함으로 느껴짐. 일본어/한국어처럼 의례 도입은 영어에서 과도할 수 있음.
   - **훈련법**: 언어별 도입 패턴 — KR 잘 부탁드립니다/평소 수고하십니다 / JP ます형 / EN "Hope this finds you well" ( 또는 또는 또는 또는 또는 직접 본문) / ES "Espero que esté bien" (격식) / CN "您好" (간단).

3. **"첨부파일 확인 부탁드립니다" 의 정중함 단계**:
   - 한국어/일본어는 첨부파일 요청 시 매우 정중한 표현 사용 — "확인 부탁드립니다" / "ご確認のほど、よろしくお願いいたします". 영어는 "Please find attached" 또는 "Attached is..." 더 직접적.
   - **함정**: 한국어 학습자가 영어 비즈니스에서 "I humbly request that you confirm the attached file" 같은 과도한 정중함 사용 → 어색.
   - **훈련법**: 첨부 표현의 정중함 매핑 — KR 확인 부탁드립니다 / JP ご確認のほど / EN Please find attached / Please review the attached / ES Adjunto encontrará / Le envío adjunto / CN 请查收附件.

4. **참조 라인 (cc) 의 계층 인식**:
   - 한국어 비즈니스 이메일에서 cc 는 계층 순서로 추가 (상급자 먼저, 그 다음 동료). 일본어도 유사 (目上の方 먼저). 영어/스페인어/중국어는 자유로운 cc.
   - **함정**: 영어 비즈니스에서 cc 가 자유로운데 한국어/일본어처럼 계층 순서로 추가하면 과도하게 격식적.
   - **훈련법**: cc 의 문화별 규범 — KR/JP: 계층 순 (상급자 → 동료) / EN/ES: 자유 / CN: 계층 인식 (상급자 cc 시 짧은 인사 추가 가능).

5. **"빨리빨리/退勤/退社" 의 격식 차이**:
   - 한국어 비즈니스에서 퇴근 후 = "퇴근했습니다" / 퇴근 시간 = "퇴근 시간" 사용. 일본어 退勤/退社 도 유사. 영어 "I left the office" / 스페인어 "Salí del trabajo" / 중국어 "下班" 도 유사하나 격식 정도 다름.
   - **함정**: 한국어 학습자가 영어에서 퇴근 알림 시 "I left the office at 5 PM" 너무 직접적 → "I am signing off" 또는 "I'll be available tomorrow" 더 간접.
   - **훈련법**: 퇴근 알림 매핑 — KR 퇴근했습니다 / JP 退勤しました / EN I'm signing off / ES Salí del trabajo / CN 下班了. 격식 정도 비교.

### 학습 전략

1. **우선순위 1**: 한국어 비즈니스 이메일 구조 (제목→인사→도입→본문→마무리→서명) 마스터 — 6단계 공식 숙지.
2. **우선순위 2**: 호칭 시스템 4언어 매핑 — 님/様/さん/Mr.+성/직함+성.
3. **우선순위 3**: 의례 도입 (いつもお世話/항상 수고) 과 다양한 본문 표현 패턴.
4. **우선순위 4**: 마무리 공식 5언어 매핑 — 잘 부탁/よろしく/Best/Atentamente/顺颂商祺.
5. **우선순위 5**: 첨부/회신/지연 사과 등 상황별 표준 표현 학습.

---

## 관련 페이지

- `[[politeness-honorifics]]` — 이메일의 격식 시스템
- `[[pronouns-reference]]` — 인사 시 대명사
- `[[travel-essentials]]` — 출장 이메일 표현
- `[[food-dining]]` — 비즈니스 식사 후속 이메일

## 출처

- 영어: `[English/vocabulary/business-vocabulary]`, `[English/culture/english-dating-culture]`
- 스페인어: `[Spanish/vocabulary/business-vocabulary]`, `[Spanish/sources/trabajo-y-carrera]`, `[Spanish/culture/espana-vs-latinoamerica-registro]`
- 일본어: `[Japanese/vocabulary/business-vocabulary]`, `[Japanese/sources/business-email]`
- 한국어: `[Korean/vocabulary/business-vocabulary]`, `[Korean/sources/daily-life-basics]`
- 중국어: `[Chinese/sources/greetings-zh]`, `[Chinese/sources/daily-routine-zh]`

---

**원본 (영어)**: [[business-email]] | **관련 미러**: [[business-email.es|Spanish]] · [[business-email.ja|Japanese]] · [[business-email.zh|Chinese]] | **정책**: ADR-0006