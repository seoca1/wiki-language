# 货币与金融 — 跨语言对比 (中文版)

> 原文: [[money-finance-comparison]] (English) | 撰写日期: 2026-08-19 | ADR-0006
> **5种语言货币/银行/金融表达对比** — English · Spanish · Japanese · Korean · Chinese

---

## 速查表

### 货币

| 货币 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **本地货币** | Dollar / Pound / Euro | Peso / Euro / Sol | 円 (en) | 원 (won) | 人民币 (rénmínbì) / 元 (yuán) |
| **货币符号** | $ / £ / € | $ / € / S/ | ¥ (yen) | ₩ (won) | ¥ (yuan) / 元 |
| **分/子单位** | Cent | Céntimo / Centavo | 銭 (sen) — 历史 | 전 (jeon) — 历史 | 分 (fēn) / 角 (jiǎo) |
| **现金 (纸币)** | Bill / Note | Billete | 紙幣 (shihei) | 지폐 (jipye) | 纸币 (zhǐbì) |
| **硬币** | Coin | Moneda | 硬貨 (kōka) | 동전 (dongjeon) | 硬币 (yìngbì) |
| **外汇** | Foreign exchange | Cambio de divisas | 為替 (kawase) | 환전 (hwanjeon) | 外汇 (wàihuì) |

### 银行

| 概念 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **银行** | Bank | Banco | 銀行 (ginkō) | 은행 (eunhaeng) | 银行 (yínháng) |
| **银行账户** | Bank account | Cuenta bancaria | 口座 (kōza) | 은행 계좌 (eunhaeng gyezwa) | 银行账户 (yínháng zhànghù) |
| **储蓄账户** | Savings account | Cuenta de ahorros | 普通預金 (futsū yokin) | 보통예금 (boteong yegum) | 储蓄账户 (chǔxù zhànghù) |
| **活期账户** | Checking account | Cuenta corriente | 当座預金 (tōza yokin) | 당좌예금 (dangjwa yegum) | 活期账户 (huóqī zhànghù) |
| **ATM** | ATM / Cash machine | Cajero automático | ATM / 現金自動預け払い機 | ATM / 현금인출기 | ATM / 自动取款机 (zìdòng qǔkuǎnjī) |
| **存款** | Deposit | Depósito / Ingreso | 預け入れ (azukeire) | 예금 (yegum) | 存款 (cúnkuǎn) |
| **取款** | Withdrawal | Retiro | 引き出し (hikidashi) | 인출 (inchul) | 取款 (qǔkuǎn) |
| **转账** | Transfer | Transferencia | 振込 (furikomi) | 송금 (songgeum) | 转账 (zhuǎnzhàng) |
| **贷款** | Loan | Préstamo | ローン (rōn) / 融資 | 대출 (daechul) | 贷款 (dàikuǎn) |
| **利息** | Interest | Interés | 利息 (risoku) | 이자 (ija) | 利息 (lìxī) |

### 支付方式

| 方式 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **现金** | Cash | Efectivo | 現金 (genkin) | 현금 (hyeongeum) | 现金 (xiànjīn) |
| **信用卡** | Credit card | Tarjeta de crédito | クレジットカード | 신용카드 (sinyongkadeu) | 信用卡 (xìnyòngkǎ) |
| **借记卡** | Debit card | Tarjeta de débito | デビットカード | 체크카드 (chekkukadeu) | 借记卡 (jièjìkǎ) |
| **移动支付** | Mobile pay | Pago móvil | モバイル決済 (kesai) | 모바일 결제 (gyeolje) | 移动支付 (yídòng zhīfù) |
| **支票** | Check | Cheque | 小切手 (kogitte) | 수표 (supyo) | 支票 (zhīpiào) |
| **非接触支付** | Contactless | Sin contacto | タッチ決済 | 비접촉 결제 | 非接触支付 (fēi jiēchù) |
| **电子钱包** | Digital wallet | Monedero digital | 電子マネー (denshi mani) | 전자지갑 (jeonjagigap) | 电子钱包 (diànzǐ qiánbāo) |

### 投资与保险

| 概念 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **股票** | Stock | Acción | 株 (kabu) / 株式 | 주식 (jusik) | 股票 (gǔpiào) |
| **股市** | Stock market | Bolsa de valores | 証券取引所 | 증권거래소 | 证券交易所 |
| **债券** | Bond | Bono | 債券 (saiken) | 채권 (chaekwon) | 债券 (zhàiquàn) |
| **基金** | Fund | Fondo | ファンド / 投資信託 | 펀드 (peondeu) | 基金 (jījīn) |
| **股息** | Dividend | Dividendo | 配当 (haitō) | 배당 (baedang) | 股息 (gǔxī) |
| **保险** | Insurance | Seguro | 保険 (hoken) | 보험 (boheom) | 保险 (bǎoxiǎn) |
| **人寿保险** | Life insurance | Seguro de vida | 生命保険 (seimei hoken) | 생명보험 (saengmyeong boheom) | 人寿保险 (rénshòu bǎoxiǎn) |
| **税** | Tax | Impuesto | 税金 (zeikin) | 세금 (segeum) | 税 (shuì) |
| **所得税** | Income tax | Impuesto sobre la renta | 所得税 (shotokuzei) | 소득세 (sodeukse) | 所得税 (suǒdéshuì) |
| **养老金** | Pension | Pensión | 年金 (nenkin) | 연금 (yeongeum) | 养老金 (yǎnglǎojīn) |

---

## 各语言详情

### 🇬🇧 英语 (English)
- **关键词**: "Money" (通用), "Currency" (正式), "Cash" (物理), "Capital" (金融)
- **模式**: "Cash" 和 "money" 口语中可互换; "bucks" / "dough" 俚语
- **来源**: N/A — 英语 wiki 暂无显式 finance 主题

### 🇪🇸 西班牙语 (Spanish)
- **关键词**: "Dinero" (钱), "Efectivo" (现金), "Plata" (俚语: 银 = 钱 in many LatAm countries)
- **模式**: "Plata" 广泛用于 LatAm (阿根廷, 智利 等); "Pasta" (西班牙) = 钱俚语
- **来源**: `[[shopping-and-money]]`

### 🇯🇵 日语 (Japanese)
- **关键词**: お金 (okane) 是日常词; 貨幣 (kahei = 货币, 正式); 銭 (zeni) 历史
- **模式**: 现金文化 historically; 円 (en) 与韩 원 (won) 和中 元 (yuán) 共享汉字 — 同源于汉字 圓/元
- **来源**: N/A — 日语 wiki 暂无显式 finance 主题

### 🇰🇷 韩语 (Korean)
- **关键词**: 돈 (don = 钱, 固有韩语); 화폐 (hwapye = 货币, 汉字词)
- **模式**: 固有词 돈 (don) 非正式; 재 (jae) = 财富/财产; 원 (won) 与中/日货币名共享汉字
- **来源**: N/A — 韩语 wiki 暂无显式 finance 主题

### 🇨🇳 中文 (Chinese)
- **关键词**: 钱 (qián = 钱, 日常); 货币 (huòbì = 货币, 正式); 钞票 (chāopiào = 纸币)
- **模式**: 钱 (qián) 原意 "硬币" (源于 鉞 yuè, 斧形早期货币); 块 (kuài) = 非正式 "buck"
- **来源**: N/A — 中文 wiki 暂无显式 finance 主题

---

## 关键对比 (综合)

| 对比 | 洞察 |
|------|------|
| **共享货币根** | 日 円 (en), 韩 원 (won), 中 元 (yuán) 都源于汉字 圓 — 书写系统可见 |
| **移动支付普及** | 中/韩几乎全民移动支付 (支付宝, 카카오페이); 日领先于 cashless 卡; 西/英仍以卡/支票为主 |
| **数字表达** | 中/日/韩用 万 (wàn/man/wan) = 10,000; 英/西用千位分组 — 影响大数字读法 |
| **标点和小数** | 中用 万/亿 分隔符; 英/西用逗号和点; 小数标记不同 (1,000.50 英 vs 1.000,50 西) |
| **钱俚语** | 各语言都有俚语: 英 "bucks/dough", 西 "plata/pasta", 日 "お札 (osatsu)", 韩 "돈 (don)", 中 "票子/银子" |

---

## 速查卡

> **货币精华**:
> - 钱: dinero / お金(okane) / 돈(don) / 钱(qián)
> - 银行: banco / 銀行(ginkō) / 은행(eunhaeng) / 银行(yínháng)
> - 现金: efectivo / 現金(genkin) / 현금(hyeongeum) / 现金(xiànjīn)
> - 信用卡: tarjeta de crédito / クレジットカード / 신용카드 / 信用卡
> - 货币: moneda / 通貨(tsūka) / 화폐(hwapye) / 货币(huòbì)

---

## 相关页面

- `[[shopping-money]]` — 购物场景的货币
- `[[business-email]]` — 金融往来
- `[[career-workplace-comparison]]` — 工资
- `[[numbers-counters]]` — 数字读法差异

## 来源

- 西: `[[shopping-and-money]]` (存在于英语词汇)
- 英/日/韩/中: 主题尚未摄取 — 见各语言 wiki 相关词汇

---

## 🇨🇳 中文学习者笔记 (Chinese Learner Notes)

> 本节是面向中文母语学习者的额外学习指南。

### 中文母语者在学习其他4种语言货币金融时的常见陷阱

1. **货币汉字的桥梁与混淆**:
   - 中文 人民币/元/圆 与日韩货币共享汉字 → 学员以为读音相近。
   - **陷阱**: 韩 원 (won) 与中文 "元" (yuán) 完全不同源 (韩语用汉字但发音不同); 日 円 (en) 历史来自 圓 = 圆形铜钱。
   - **训练法**: 利用汉字桥梁理解概念, 严格训练读音, 区分各自历史背景。

2. **大数字进位的差异**:
   - 中文以 万 为基础 (万/亿/兆) → 学员假设其他语言也相同。
   - **陷阱**: 英语/西语以 千 为基础 (thousand/million/billion); 学习英文大数字时需重新调整。
   - **训练法**: 制作 "万 vs 千" 对比表 — 1万 = 10千; 1亿 = 10000万; 1 million = 100万。

3. **现金文化的差异**:
   - 中国移动支付 (微信/支付宝) 几乎全民 → 学员假设其他语言也如此。
   - **陷阱**: 日本 现金仍是主流 (虽然近年 PayPay 兴起); 韩国移动支付普及; 西语国家现金仍主导; 英语国家信用卡主导。
   - **训练法**: 学习每个国家具体支付方式 — 不要把中文经验直接套用。

4. **小数/分隔符的差异**:
   - 中文在数字中用"万/亿"分隔符 → 学员假设其他语言也相同。
   - **陷阱**: 英语 1,000.50 (逗号千分位, 点小数); 西语 1.000,50 (点千分位, 逗号小数); 法语空格的也有。
   - **训练法**: 严格区分 每个数字读法的实际格式 — 跨国交易时必须确认。

5. **俚语/口语的差异**:
   - 中文 钱/票子/银子 → 学员假设其他语言只有 "money" 一词。
   - **陷阱**: 西语 "plata" (银 = 钱, LatAm) / "pasta" (面团 = 钱, 西班牙); 日 "お札" (纸币); 韩 "돈 (don)"; 英 "bucks/dough/bread"。
   - **训练法**: 学习每个国家非正式钱词 — 提升日常对话能力。

### 相关中文维基页面

- [Chinese/vocabulary/money-zh] — 中文货币词汇
- [Chinese/culture/chinese-mobile-pay-zh] — 中文移动支付文化
- [Chinese/grammar/basic-particles] — 中文基本助词
- [Chinese/vocabulary/numbers-zh] — 中文数字词汇
- [Chinese/vocabulary/measure-words-zh] — 中文量词

### 学习工作流程推荐

1. **背诵对比表** (货币/银行/支付方式)
2. **大数字读法对比** (万 vs 千 系统)
3. **移动支付场景** (各国家主流支付方式)
4. **旅行场景** (ATM/信用卡/汇率查询)
5. **使用当地货币的惯用语** (俚语/口语)

---

**原文 (英语)**: [[money-finance-comparison]] | **相关镜像**: [[money-finance-comparison.es|西班牙语]] · [[money-finance-comparison.ja|日语]] · [[money-finance-comparison.ko|韩语]] | **政策**: ADR-0006
