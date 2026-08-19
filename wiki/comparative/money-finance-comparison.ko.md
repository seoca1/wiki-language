# 돈 & 금융 — 다국어 비교 (한국어판)

> 원본: [[money-finance-comparison]] (English) | 작성일: 2026-08-20 | ADR-0006
> **5개 언어 화폐, 은행, 금융 어휘 비교**

---

## 빠른 참조 표

### 통화

| 통화 | English | Spanish | Japanese | Korean | Chinese |
|----------|---------|---------|----------|--------|---------|
| **현지 통화** | Dollar / Pound / Euro | Peso / Euro / Sol | 円 (en) | 원 (won) | 人民币 (rénmínbì) / 元 (yuán) |
| **통화 기호** | $ / £ / € | $ / € / S/ | ¥ (yen) | ₩ (won) | ¥ (yuan) / 元 |
| **센트/보조 단위** | Cent | Céntimo / Centavo | 銭 (sen) — 역사적 | 전 (jeon) — 역사적 | 分 (fēn) / 角 (jiǎo) |
| **현금 (지폐)** | Bill / Note | Billete | 紙幣 (shihei) | 지폐 (jipye) | 纸币 (zhǐbì) |
| **동전** | Coin | Moneda | 硬貨 (kōka) | 동전 (dongjeon) | 硬币 (yìngbì) |
| **환전** | Foreign exchange | Cambio de divisas | 為替 (kawase) | 환전 (hwanjeon) | 外汇 (wàihuì) |

### 은행

| 개념 | English | Spanish | Japanese | Korean | Chinese |
|---------|---------|---------|----------|--------|---------|
| **은행** | Bank | Banco | 銀行 (ginkō) | 은행 (eunhaeng) | 银行 (yínháng) |
| **은행 계좌** | Bank account | Cuenta bancaria | 口座 (kōza) | 은행 계좌 (eunhaeng gyezwa) | 银行账户 (yínháng zhànghù) |
| **저축 계좌** | Savings account | Cuenta de ahorros | 普通預金 (futsū yokin) | 보통예금 (boteong yegum) | 储蓄账户 (chǔxù zhànghù) |
| **당좌 계좌** | Checking account | Cuenta corriente | 当座預金 (tōza yokin) | 당좌예금 (dangjwa yegum) | 活期账户 (huóqī zhànghù) |
| **ATM** | ATM / Cash machine | Cajero automático | ATM / 現金自動預け払い機 | ATM / 현금인출기 | ATM / 自动取款机 (zìdòng qǔkuǎnjī) |
| **입금** | Deposit | Depósito / Ingreso | 預け入れ (azukeire) | 예금 (yegum) | 存款 (cúnkuǎn) |
| **출금** | Withdrawal | Retiro | 引き出し (hikidashi) | 인출 (inchul) | 取款 (qǔkuǎn) |
| **이체** | Transfer | Transferencia | 振込 (furikomi) | 송금 (songgeum) | 转账 (zhuǎnzhàng) |
| **대출** | Loan | Préstamo | ローン (rōn) / 融資 | 대출 (daechul) | 贷款 (dàikuǎn) |
| **이자** | Interest | Interés | 利息 (risoku) | 이자 (ija) | 利息 (lìxī) |

### 결제 방법

| 방법 | English | Spanish | Japanese | Korean | Chinese |
|--------|---------|---------|----------|--------|---------|
| **현금** | Cash | Efectivo | 現金 (genkin) | 현금 (hyeongeum) | 现金 (xiànjīn) |
| **신용카드** | Credit card | Tarjeta de crédito | クレジットカード | 신용카드 (sinyongkadeu) | 信用卡 (xìnyòngkǎ) |
| **체크카드** | Debit card | Tarjeta de débito | デビットカード | 체크카드 (chekkukadeu) | 借记卡 (jièjìkǎ) |
| **모바일 결제** | Mobile pay | Pago móvil | モバイル決済 (kesai) | 모바일 결제 (gyeolje) | 移动支付 (yídòng zhīfù) |
| **수표** | Check | Cheque | 小切手 (kogitte) | 수표 (supyo) | 支票 (zhīpiào) |
| **비접촉** | Contactless | Sin contacto | タッチ決済 | 비접촉 결제 | 非接触支付 (fēi jiēchù) |
| **디지털 지갑** | Digital wallet | Monedero digital | 電子マネー (denshi mani) | 전자지갑 (jeonjagigap) | 电子钱包 (diànzǐ qiánbāo) |

### 투자 & 보험

| 개념 | English | Spanish | Japanese | Korean | Chinese |
|---------|---------|---------|----------|--------|---------|
| **주식** | Stock | Acción | 株 (kabu) / 株式 | 주식 (jusik) | 股票 (gǔpiào) |
| **증권 시장** | Stock market | Bolsa de valores | 証券取引所 | 증권거래소 | 证券交易所 |
| **채권** | Bond | Bono | 債券 (saiken) | 채권 (chaekwon) | 债券 (zhàiquàn) |
| **펀드** | Fund | Fondo | ファンド / 投資信託 | 펀드 (peondeu) | 基金 (jījīn) |
| **배당** | Dividend | Dividendo | 配当 (haitō) | 배당 (baedang) | 股息 (gǔxī) |
| **보험** | Insurance | Seguro | 保険 (hoken) | 보험 (boheom) | 保险 (bǎoxiǎn) |
| **생명보험** | Life insurance | Seguro de vida | 生命保険 (seimei hoken) | 생명보험 (saengmyeong boheom) | 人寿保险 (rénshòu bǎoxiǎn) |
| **세금** | Tax | Impuesto | 税金 (zeikin) | 세금 (segeum) | 税 (shuì) |
| **소득세** | Income tax | Impuesto sobre la renta | 所得税 (shotokuzei) | 소득세 (sodeukse) | 所得税 (suǒdéshuì) |
| **연금** | Pension | Pensión | 年金 (nenkin) | 연금 (yeongeum) | 养老金 (yǎnglǎojīn) |

---

## 핵심 대조 (종합)

| 대조 | 통찰 |
|----------|---------|
| **통화 한자 공유** | JP 円 (en), KR 원 (won), CN 元 (yuán) 모두 한자 圓 파생 — 문자 시스템에서 보임 |
| **모바일 결제 채택** | CN/KR은 거의 보편 모바일 결제 (支付宝, 카카오페이); JP는 현금 카드 선두; ES/EN은 여전히 카드/수표 중심 |
| **숫자 표현** | CN/JP/KR는 만(万) = 10,000 사용; EN/ES는 1000 단위 묶음 — 큰 숫자 읽기 영향 |
| **구두점 및 소수** | CN는 만/억 구분자; EN/ES는 쉼표와 마침표; 소수점 표기 차이 (1,000.50 EN vs 1.000,50 ES) |
| **돈 슬랭** | 각 언어 슬랭 보유: EN "bucks/dough", ES "plata/pasta", JP "お札 (osatsu)", KR "돈 (don)", CN "票子/银子" |

---

## 학습자 의사결정 가이드

> **돈 필수 어휘**:
> - Money: dinero / お金(okane) / 돈(don) / 钱(qián)
> - Bank: banco / 銀行(ginkō) / 은행(eunhaeng) / 银行(yínháng)
> - Cash: efectivo / 現金(genkin) / 현금(hyeongeum) / 现金(xiànjīn)
> - Credit card: tarjeta de crédito / クレジットカード / 신용카드 / 信用卡
> - Currency: moneda / 通貨(tsūka) / 화폐(hwapye) / 货币(huòbì)

> **모바일 결제 국가별 우세**:
> - 한국: 카카오페이, 삼성페이, 네이버페이, 토스
> - 중국: 微信支付 (위챗페이), 支付宝 (알리페이) — 보편
> - 일본: PayPay, LINE Pay, Suica
> - 미국: Apple Pay, Venmo, Zelle
> - 스페인: Bizum (P2P)

---

## 🇰🇷 한국어 학습자 노트 (Korean Learner Notes)

> 본 섹션은 한국어 학습자 대상의 추가 학습 가이드입니다.

### 한국어 화자가 다른 4개 언어 금융 어휘를 학습할 때 흔히 마주치는 함정

1. **한자 통화명 발음 차이**:
   - 같은 한자 통화 "元" — 한국 "원 (won)", 일본 "円 (en)", 중국 "元 (yuán)" — 모두 한자 圓/元 계열이지만 발음/문자 다름.
   - **함정**: 한국어 "원" 발음을 다른 언어 통화에 적용 → "원화"는 KRW, "日元 (Japanese yen)" ≠ "원화" 혼동.
   - **훈련법**: 통화명 한자 3개국 변형 매트릭스 — 원(원화, KRW) / 円(엔화, JPY) / 元(위안화, CNY). 한자 한 글자당 3개국 발음.

2. **모바일 결제 문화 차이**:
   - 한국/중국은 모바일 결제 보편 (카카오페이, 위챗페이/알리페이). 일본/스페인/미국은 카드 또는 현금.
   - **함정**: 한국어 "모바일 결제" 패턴 (QR 스캔 → 결제) 다른 문화에 적용 → 중국 외 국가에서 QR 결제 미지원.
   - **훈련법**: 국가별 모바일 결제 시스템 학습 — 한국 카카오페이/삼성페이/토스, 중국 위챗페이/알리페이, 일본 PayPay/LINE Pay, 미국 Apple Pay, 유럽 Bizum. **해외 여행 시 해당 국가 결제 시스템 사전 학습**.

3. **수표 (Check) 어휘**:
   - 한국은 수표 사용 거의 사라짐. 미국은 수표 여전히 일반, 유럽 일부 국가 사용.
   - **함정**: 한국어 학습자가 해외에서 "수표 (check)" 어휘 사용 → 실생활 빈도 낮음. 미국/유럽 호텔/식당에서만.
   - **훈련법**: 카드/현금/모바일 결제가 보편. 수표 어휘는 미국 비즈니스/호텔 한정 학습.

4. **큰 숫자 단위 차이**:
   - 한국/중국/일본 = 만(万) 단위 (1,0000). 미국/유럽 = 천 (1,000) 단위.
   - **함정**: 한국어 "일억 (1억, 100,000,000)"을 미국식 "100 million"으로 번역 가능하나, 중국어 "一亿"도 같은 의미. 그러나 영어는 billion이 다름 (1B = 10억 = 한국 10억 = 1,000,000,000).
   - **함정 2**: 스페인 "billón" = 10¹² (long scale) vs 미국 "billion" = 10⁹ (short scale) — 금융 번역 함정.
   - **훈련법**: 만 단위 매트릭스 (KR/JP/CN 동일) vs 천 단위 (EN/ES) — 1억 = 100 million, 1조 = 1 trillion. **스페인 long scale 주의**.

5. **금융 어휘의 한자 한자어 vs 고유어**:
   - 한국어 금융 어휘: "돈 (고유어)" + "貨幣 (한자어 화폐)" / "은행 (한자어)" + "돈 (고유어)" 등 혼재.
   - **함정**: 일본어/중국어 한자어 매핑 시 "돈" 같은 고유어 매핑 실패.
   - **훈련법**: 금융 어휘 고유어/한자어 분리 — 돈/고유어 vs 通貨(통화)/한자어 vs 銀行(은행)/한자어.

### 학습 전략

1. **우선순위 1**: 한자 통화명 3개국 매트릭스 — 원(원화, KRW) / 円(엔화, JPY) / 元(위안화, CNY) / Dollar(미국, USD) / Euro(유로, EUR) / Peso(페소, ARS/MXN). 한자/비한자 모두.
2. **우선순위 2**: 모바일 결제 시스템 5개국 매핑 — 한국 카카오페이/삼성페이/토스, 중국 위챗페이/알리페이, 일본 PayPay/LINE Pay, 미국 Apple Pay/Venmo, 유럽 Bizum. **해외 여행 필수**.
3. **우선순위 3**: 큰 숫자 단위 — 한국/중국/일본 = 만/억/조, 미국 = thousand/million/billion, 유럽 = long scale (billion = 10¹²). 단위 차이 인지.
4. **우선순위 4**: 금융 한자어 vs 고유어 — 한자 매핑 가능 어휘 (통화, 은행, 환율, 이자, 주가) vs 고유어 (돈, 잔돈, 잔고, 송금) 분류.
5. **우선순위 5**: 돈 슬랭 5개국 — bucks/dough (EN), plata/pasta (ES), 札 (JP), 돈/현금/오백원 (KR), 票子/银子 (CN). **문화적 돈 개념 비교**.

### 관련 한국어 위키 페이지

- [[shopping-money]] — 쇼핑 문맥 돈 어휘
- [[business-email]] — 금융 서신
- [[career-workplace-comparison]] — 급여/임금 어휘
- [[numbers-counters]] — 숫자 읽기 차이
- [[untranslatable-concepts]] — 한/정/눈치/관계/面子 등 문화 어휘

---

## 관련 페이지

- `[[shopping-money]]` — 쇼핑 문맥 돈
- `[[business-email]]` — 금융 서신
- `[[career-workplace-comparison]]` — 급여/임금
- `[[numbers-counters]]` — 숫자 읽기

## 출처

- ES: `[[shopping-and-money]]`
- EN/JP/KR/ZH: 금융 테마 미인제스트 — 관련 어휘는 per-language wiki 참조

---

**원본 (영어)**: [[money-finance-comparison]] | **관련 미러**: [[money-finance-comparison.es|Spanish]] · [[money-finance-comparison.ja|Japanese]] · [[money-finance-comparison.zh|Chinese]] | **정책**: ADR-0006
