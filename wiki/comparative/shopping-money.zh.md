# 购物与货币 — 跨语言对比 (中文版)

> 原文: [[shopping-money]] (English) | 撰写日期: 2026-08-19 | ADR-0006
> **5种语言购物/付钱/退货对比** — English · Spanish · Japanese · Korean · Chinese

---

## 速查表

### 货币词汇

| 概念 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **钱** | money | dinero / plata | お金 (okane) / 金 (kane) | 돈 (don) / 금전 (geumjeon) | 钱 (qián) / 金钱 (jīnqián) |
| **现金** | cash | efectivo | 現金 (genkin) | 현금 (hyeongeum) | 现金 (xiànjīn) |
| **信用卡** | credit card | tarjeta de crédito | クレジットカード (kurejitto kaado) | 신용카드 (sinyong kadeu) | 信用卡 (xìnyòngkǎ) |
| **借记卡** | debit card | tarjeta de débito | デビットカード (debito kaado) | 체크카드 (chekeu kadeu) | 借记卡 (jièjìkǎ) / 储蓄卡 (chǔxùkǎ) |
| **移动支付** | Apple Pay / Google Pay | Bizum / Apple Pay / Google Pay | Apple Pay / Google Pay / LINE Pay / PayPay | Samsung Pay / Kakao Pay / Naver Pay / Toss | **WeChat Pay / Alipay** (无处不在) |
| **货币** | currency | moneda | 通貨 (tsuuka) | 통화 (tonghwa) | 货币 (huòbì) |
| **汇率** | exchange rate | tipo de cambio | 為替レート (kawase reeto) | 환율 (hwan-yul) | 汇率 (huìlǜ) |
| **收据** | receipt | recibo / factura / ticket | 領収書 (ryoushuusho) / レシート (reshiito) | 영수증 (yeongsujeung) | 发票 (fāpiào) / 小票 (xiǎopiào) |
| **发票** | invoice | factura | 請求書 (seikyuusho) | 세금계산서 (segwa-gyesanseo) | 发票 (fāpiào) |
| **零钱** | change (coins) | cambio / vuelto | お釣り (otsuri) | 거스름돈 (geoseureumdon) | 零钱 (língqián) / 找零 (zhǎolíng) |
| **账单 (餐厅)** | check / bill | la cuenta | お会計 (okaikei) / 伝票 (denpyou) | 계산서 (gyesanseo) | 买单 (mǎidān) / 账单 (zhàngdān) |
| **小费** | tip | propina | チップ (chippu) — 罕见 | 팁 (tip) — 罕见 | 小费 (xiǎofèi) — 罕见 (大陆) |
| **税** | tax | IVA / impuesto | 消費税 (shouhizei) / 税金 (zeikin) | 세금 (segum) / 부가세 (bugase) | 税 (shuì) / 增值税 (zēngzhíshuì) |

### 购物动词与短语

| 动作 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **买** | buy | comprar | 買う (kau) | 사다 (sada) | 买 (mǎi) |
| **卖** | sell | vender | 売る (uru) | 팔다 (paldà) | 卖 (mài) |
| **购物** | shop / go shopping | ir de compras | 買い物する (kaimono suru) | 쇼핑하다 (syopinghada) / 장보다 (jangboda) | 买东西 (mǎi dōngxi) / 逛街 (guàngjiē) |
| **浏览** | browse / look around | curiosear / echar un vistazo | 見る (miru) / ウィンドウショッピング | 구경하다 (gugyeonghada) | 看看 (kàn kan) / 逛逛 (guàng guang) |
| **试穿** | try on | probarse | 試着する (shichaku suru) | 입어보다 (ibeoboda) / 신어보다 (sineoboda) | 试穿 (shìchuān) / 试戴 (shìdài) |
| **合身** | fit (size) | quedar bien / tallar | サイズが合う (saizu ga au) | 맞다 (matda) / 사이즈가 맞다 | 合身 (héshēn) / 合适 (héshì) |
| **支付** | pay | pagar | 支払う (shiharau) / 払う (harau) | 지불하다 (jibulhada) / 계산하다 (gyesanhada) | 付款 (fùkuǎn) / 买单 (mǎidān) |
| **退货** | return / exchange | devolver / cambiar | 返品する (henpin suru) / 交換する (koukan suru) | 반품하다 (banpumhada) / 교환하다 (gyohwanhada) | 退货 (tuìhuò) / 换货 (huànhuò) |
| **退款** | refund | reembolsar / devolver el dinero | 返金する (henkin suru) | 환불하다 (hwanbulhada) | 退款 (tuìkuǎn) |
| **讨价还价** | bargain / haggle | regatear / negociar | 値切る (negiru) — 罕见 | 흥정하다 (heungjeonghada) | 砍价 (kǎnjià) / 讨价还价 (tǎojià huánjià) |
| **获取折扣** | get a discount | conseguir descuento | 割引してもらう (waribiki shitemorau) | 할인받다 (harinbatda) | 打折 (dǎzhé) / 优惠 (yōuhuì) |

### 尺码系统

| 类别 | English (美/英) | Spanish (EU) | Japanese | Korean | Chinese |
|------|-----------------|--------------|----------|--------|---------|
| **女装上衣** | XS-XXL / 0-18 | 34-48 / XS-XXL | S-M-L-LL-3L / 7-15号 | 44-77 / S-M-L-XL-XXL | S-M-L-XL-XXL / 155-175/80A-100A |
| **男装上衣** | XS-XXL / 34-48 | 44-58 / XS-XXL | S-M-L-LL-3L / S-3L | 90-115 / S-M-L-XL-XXL | S-M-L-XL-XXL / 165-185/84A-96A |
| **女鞋** | 美 5-11 / 英 3-9 / EU 35-42 | EU 35-42 | 22.0-25.5cm | 220-255mm | 34-41 / 220-255mm |
| **男鞋** | 美 7-13 / 英 6-12 / EU 39-46 | EU 39-46 | 24.5-28.5cm | 245-290mm | 39-46 / 245-290mm |
| **戒指** | 美 3-13 | EU 44-70 | 日 1-30 (mm 直徑) | 韩 1-30 (mm 周长) | 港/中 8-24 (mm 周长) |

**关键差异**:
- **日/韩/中**: 基于厘米 (脚长 for 鞋, 身体尺寸 for 衣)
- **西**: EU 尺码标准
- **英**: 美/英双系统; 虚荣尺码常见

### 商店类型

| 类型 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **百货店** | department store | grandes almacenes / El Corte Inglés | デパート (depaato) | 백화점 (baekhwajeom) | 百货公司 (bǎihuò gōngsī) / 商场 (shāngchǎng) |
| **超市** | supermarket | supermercado | スーパー (suupaa) | 슈퍼 (syupeo) / 마트 (mateu) | 超市 (chāoshì) |
| **便利店** | convenience store / corner store | tienda de conveniencia / 24h | コンビニ (konbini) | 편의점 (pyeonijeom) | 便利店 (biànlìdiàn) / 7-11 / 全家 (FamilyMart) |
| **药店** | pharmacy / drugstore | farmacia / parafarmacia | 薬局 (yakkyoku) / ドラッグストア | 약국 (yakguk) / 드럭스토어 | 药店 (yàodiàn) / 药房 (yàofáng) |
| **电子** | electronics store | tienda de electrónica | 家電量販店 (kaden ryouhanten) / ヨドバシ/ビックカメラ | 전자상가 (jeonjasangga) / 하이마트/디지털프라자 | 电器店 (diànqìdiàn) / 苏宁/国美 |
| **服装精品** | boutique / clothing store | boutique / tienda de ropa | セレクトショップ (serekuto shoppu) / ブティック | 편집샵 (pyeonjipsyap) / 부티크 | 精品店 (jīngpǐn diàn) / 服装店 (fúzhuāng diàn) |
| **市场** | market / farmers market | mercado / mercadillo | 市場 (ichiba) / 朝市 (asaichi) | 시장 (sijang) / 재래시장 (jaeraesijang) | 市场 (shìchǎng) / 菜市场 (càishìchǎng) |
| **商场** | mall / shopping center | centro comercial | ショッピングモール (shoppingu mooru) | 쇼핑몰 (syopingmol) / 복합쇼핑몰 | 购物中心 (gòuwù zhōngxīn) / 商场 (shāngchǎng) |
| **在线市场** | Amazon / eBay | Amazon / Wallapop / Vinted | Amazon / 楽天 (Rakuten) / メルカリ (Mercari) | 쿠팡 (Coupang) / 11번가 / 당근마켓 | **淘宝 (Taobao) / 京东 (JD) / 拼多多 (Pinduoduo)** / 闲鱼 (Xianyu) |

### 价格与折扣表达

| 表达 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **多少钱?** | How much is this? | ¿Cuánto cuesta? / ¿Cuánto es? | いくらですか？ (Ikura desu ka?) | 얼마예요? (Eolmayeyo?) | 多少钱? (Duōshǎo qián?) |
| **太贵了** | It's too expensive. | Es muy caro. / Me parece caro. | 高すぎます。 (Takasugimasu.) | 너무 비싸요. (Neomu bissayo.) | 太贵了。 (Tài guì le.) |
| **能便宜点吗?** | Can you lower the price? | ¿Me puede hacer un descuento? / ¿Me lo deja en...? | 安くできますか？ (Yasuku dekimasu ka?) | 깎아 주세요. (Kkakka juseyo.) | 能便宜点吗? (Néng piányi diǎn ma?) |
| **折扣** | discount / % off | descuento / % de descuento | 割引 (waribiki) / ○%オフ (○% ofu) | 할인 (harin) / ○% 세일 | 打折 (dǎzhé) / ○折 (○ zhé) / 优惠 (yōuhuì) |
| **促销** | on sale / on clearance | en oferta / rebajas / liquidación | セール (seeru) / バーゲン (baagen) | 세일 (seil) / 할인 행사 | 促销 (cùxiāo) / 打折 (dǎzhé) / 清仓 (qīngcāng) |
| **买一送一** | buy one get one free | compra 1 lleva 1 / 2x1 | 1つ買うと1つ無料 (hitotsu kau to hitotsu muryou) | 1+1 / 원플원 (wonpeulwon) | 买一送一 (mǎi yī sòng yī) / 第二件半价 |
| **最终价** | final price / out the door | precio final / total | 税込み (zeikomi) / 合計 (goukei) | 최종가 (choejongga) / 총액 (chong'aek) | 实付 (shífù) / 总价 (zǒngjià) |
| **含税** | tax included | IVA incluido | 税込み (zeikomi) | 세금 포함 (segum poham) | 含税 (hánshuì) / 价格含税 |
| **能开发票吗?** | Can I get a receipt? | ¿Me da el ticket/recibo? | レシート/領収書ください。 (Reshiito/ryoushuusho kudasai.) | 영수증 주세요. (Yeongsujeung juseyo.) | 能开发票吗? (Néng kāi fāpiào ma?) / 要小票。 |

### 支付互动

### 现金支付

| 步骤 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **递现金** | Here you go. | Aquí tiene. | はい、これです。 (Hai, kore desu.) | 여기요. (Yeogiyo.) | 给您。 (Gěi nín.) |
| **找零** | Your change is $X. | Su cambio son $X. | お釣りはX円です。 (Otsuri wa X-en desu.) | 거스름돈 X원입니다. (Geoseureumdon X-won-imnida.) | 找您X元。 (Zhǎo nín X yuán.) |
| **确认** | Thank you. | Gracias. | ありがとうございます。 (Arigatou gozaimasu.) | 감사합니다. (Gamsahamnida.) | 谢谢。 (Xièxiè.) |

### 刷卡支付

| 步骤 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **插入/接触** | Insert/tap your card. | Introduzca/apoye la tarjeta. | カードを挿入/タッチしてください。 (Kaado o sounyuu/tacchi shite kudasai.) | 카드 넣어주세요/대주세요. (Kadeu neo-eojuseyo/daejuseyo.) | 请插卡/刷卡/刷码。 (Qǐng chākā/shuākā/shuāmǎ.) |
| **密码/签名** | Enter PIN / Sign here. | Introduzca PIN / Firme aquí. | 暗証番号を入力/サインをお願いします。 (Anshou bangou o nyuuryoku/sain o onegaishimasu.) | 비밀번호 입력/사인해 주세요. (Bimilbeonho ibnyeok/sainhae juseyo.) | 请输入密码/签名。 (Qǐng shūrù mìmǎ/qiānmíng.) |
| **已批准** | Approved. | Aprobado. | 承認されました。 (Shounin saremashita.) | 승인되었습니다. (Seungin doeeotseumnida.) | 支付成功。 (Zhīfù chénggōng.) |

### 移动支付 (QR Code)

| 步骤 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **显示码** | I'll pay with [app]. | Pago con [app]. | [アプリ]で払います。 ([Apuri] de haraimasu.) | [앱]으로 결제할게요. ([Aep]euro gyeoljehalgeyo.) | 我用[微信/支付宝]付。 (Wǒ yòng [WeChat/Zhīfùbǎo] fù.) |
| **扫描** | Scan my code. | Escanee mi código. | コードを読み取ってください。 (Koodo o yomitorite kudasai.) | QR 코드 찍어주세요. (QR kodeu jjigeojuseyo.) | 扫一下。 (Sǎo yīxià.) |
| **确认** | Payment successful. | Pago exitoso. | 支払い完了しました。 (Shiharai kanryou shimashita.) | 결제 완료되었습니다. (Gyeolje wallyo doeeotseumnida.) | 支付成功。 (Zhīfù chénggōng.) |

### 退货/换货政策

| 方面 | English (美国) | Spanish | Japanese | Korean | Chinese |
|------|--------------|---------|----------|--------|---------|
| **窗口** | 30 天典型 | 14-30 天 (EU 法律: 14) | 7-30 天 (店家政策) | 7-30 天 (法律: 在线 7) | 7 天 (法律: 在线 7 无理由) |
| **条件** | 未穿, 标签在 | 未用, 包装完整 | 未使用・タグ付き (mishiyou tagutsuki) | 미착용, 택 부착 (michak-yong, taek buchak) | 未拆封, 吊牌完好 (wèi chāifēng, diàopái wánhǎo) |
| **收据必需** | 是 (礼物收据 OK) | 是 | 必要 (hitsuyou) / レシート必須 | 필수 (pil-su) / 영수증 지참 | 必须 (bìxū) / 发票/小票 |
| **退款方式** | 原始支付 | 原始支付 | 現金/カード返金 (genkin/kaado henkin) | 원결제수단 환불 (wongyeoljesudan hwanbul) | 原路退款 (yuánlù tuìkuǎn) |
| **特价品** | 通常最终销售 | 通常不退 | セール品返品不可 (seeru hin henpin fuka) | 세일 상품 교환/환불 불가 | 打折商品不退换 (dǎzhé shāngpǐn bù tuìhuàn) |
| **在线退货** | 免费退货标签常见 | 免费退货 (EU) | 送料自己負担 common | 무료 반품 common (Coupang 等) | 运费险 (yùnfei xiǎn) — return shipping insurance |

### 文化购物规范

| 规范 | English (美/英) | Spanish | Japanese | Korean | Chinese |
|------|-----------------|---------|----------|--------|---------|
| **讨价还价** | 仅跳蚤市场 | 市场, 街头小贩 | **罕见** (固定价格) | 市场 (南大门, 东大门) | **市场, 街头小贩** 期望 |
| **试穿** | 衣服期望 | 期望 | 期望 (先询问店员) | 期望 | 期望 |
| **装袋** | 自装 (美) / 店员 (英) | 店员装 | **店员精心装** | 店员装 | 自装或付袋费 |
| **礼品包装** | DIY 或付费 | 免费/付费 (百货店) | **免费, 精美** (百货店) | 免费/付费 | 免费/付费 (百货店) |
| **会员卡** | 常见 (积分) | 常见 (puntos) | **通用** (T-point, Ponta, Rakuten) | **通用** (L.Point, Happy Point) | **微信/支付宝集成** |
| **销售税** | 收银台添加 (美) / 已含 (英) | **已含** (IVA) | **已含** (zeikomi) | **已含** (VAT 10%) | **已含** (VAT 13%) |
| **小费** | 无 (零售) | 无 | **无** (粗鲁) | **无** | **无** (大陆) |

---

## 速查卡

| 需要说... | EN | ES | JP | KR | CH |
|-----------|----|----|----|----|----|
| **"多少钱?"** | How much? | ¿Cuánto cuesta? | いくらですか？ (Ikura desu ka?) | 얼마예요? (Eolmayeyo?) | 多少钱? (Duōshǎo qián?) |
| **"太贵了"** | Too expensive | Muy caro | 高すぎます (Takasugimasu) | 너무 비싸요 (Neomu bissayo) | 太贵了 (Tài guì le) |
| **"有折扣吗?"** | Any discount? | ¿Descuento? | 割引ありますか？ (Waribiki arimasu ka?) | 할인 돼요? (Harin dwaeyo?) | 有优惠吗? (Yǒu yōuhuì ma?) |
| **"可以试穿吗?"** | Can I try this on? | ¿Me lo puedo probar? | 試着できますか？ (Shichaku dekimasu ka?) | 입어봐도 돼요? (Ibeobwado dwaeyo?) | 可以试穿吗? (Kěyǐ shìchuān ma?) |
| **"合身吗?"** | Does it fit? | ¿Me queda bien? | サイズ合いますか？ (Saizu aimasu ka?) | 맞아요? (Majayo?) | 合身吗? (Héshēn ma?) |
| **"我要这个"** | I'll take it | Me lo llevo / Lo compro | これをください (Kore o kudasai) | 이거 살게요 (Igeo salgeyo) | 我要这个 (Wǒ yào zhège) |
| **"刷卡"** | Card, please | Con tarjeta, por favor | カードで (Kaado de) | 카드로요 (Kadeulloyo) | 刷卡 (Shuākǎ) / 扫码 (Sǎomǎ) |
| **"要发票"** | Receipt, please | El ticket, por favor | レシートください (Reshiito kudasai) | 영수증 주세요 (Yeongsujeung juseyo) | 要发票/小票 (Yào fāpiào/xiǎopiào) |
| **"可以退货吗?"** | Return policy? | ¿Política de devoluciones? | 返品できますか？ (Henpin dekimasu ka?) | 반품 돼요? (Banpum dwaeyo?) | 可以退货吗? (Kěyǐ tuìhuò ma?) |
| **"要袋子"** | Bag, please | Una bolsa, por favor | 袋ください (Fukuro kudasai) | 봉투 주세요 (Bongtu juseyo) | 要袋子 (Yào dàizi) |

---

## 相关页面

- `[[travel-essentials]]` — 旅行时购物
- `[[numbers-counters]]` — 价格, 数量, 量词
- `[[food-dining]]` — 市场/食品购物
- `[[politeness-honorifics]]` — 与店员的语阶
- `[[business-email]]` — B2B 采购订单

## 来源

- 英语: `[English/vocabulary/travel]`, `[English/vocabulary/basic-vocabulary]`
- 西班牙语: `[Spanish/vocabulary/basic-vocabulary]`, `[Spanish/vocabulary/viajes]`
- 日语: `[Japanese/vocabulary/travel]`, `[Japanese/vocabulary/business-vocabulary]`
- 韩语: `[[wiki/Korean/vocabulary/여행]]`, `[[index]]`
- 中文: `[Chinese/vocabulary/numbers-zh]`, `[Chinese/vocabulary/measure-words-zh]`

---

## 🇨🇳 中文学习者笔记 (Chinese Learner Notes)

> 本节是面向中文母语学习者的额外学习指南。

### 中文母语者在学习其他4种语言购物时的常见陷阱

1. **移动支付文化的差异**:
   - 中国 微信/支付宝 几乎全民 → 学员假设其他语言也类似。
   - **陷阱**: 日本 PayPay/LINE Pay 兴起中, 但现金仍主导; 韩国 Samsung Pay/Kakao Pay 普及; 西语国家现金仍主导; 英语国家信用卡主导。
   - **训练法**: 确认目的国移动支付普及程度 — 出境前决定带现金/信用卡/还是用本地支付。

2. **讨价还价的文化差异**:
   - 中国市场和街头小贩讨价还价常见 → 学员假设其他语言也类似。
   - **陷阱**: 日本固定价格(讨价还价罕见); 韩国市场 (南大门, 东大门) 可讨价还价; 西语市场可讨价还价; 英语国家跳蚤市场可。
   - **训练法**: 了解目的地讨价还价文化 — 避免无意冒犯或错失机会。

3. **退货政策的差异**:
   - 中国 7 天无理由退货 (法律规定) → 学员假设其他语言也类似。
   - **陷阱**: 日本 7-30 天 (店家政策); 韩国 7-30 天 (法律规定在线 7 天); 西语 14-30 天 (EU 法律 14 天); 英语 30 天典型。
   - **训练法**: 购物前确认退货政策 — 避免"购买后退货难"。

4. **尺码系统的差异**:
   - 中文 衣服尺码 S/M/L/XL + 身高/胸围 → 学员假设其他语言也对应。
   - **陷阱**: 日语 7-15 号; 韩语 44-77; 西语 EU 34-48; 英语美/英双系统。
   - **训练法**: 出国前制作"尺码对照表" — 避免买错尺寸。

5. **小票/发票的差异**:
   - 中文 发票 (fāpiào) 正式 / 小票 (xiǎopiào) 简单 → 学员假设其他语言也对应。
   - **陷阱**: 英语 receipt (通用); 西语 recibo / factura / ticket; 日语 レシート (reshiito) / 領収書 (ryoushuusho); 韩语 영수증 (yeongsujeung) / 세금계산서。
   - **训练法**: 区分"报销发票" vs "购物小票" — 国际旅行者需要保留哪种。

### 相关中文维基页面

- [Chinese/vocabulary/shopping-zh] — 中文购物词汇
- [Chinese/culture/chinese-mobile-pay-zh] — 中文移动支付文化
- [Chinese/vocabulary/money-zh] — 中文货币词汇
- [Chinese/grammar/basic-particles] — 中文基本助词
- [Chinese/sources/daily-routine-zh] — 中文日常用语

### 学习工作流程推荐

1. **背诵对比表** (货币/购物动词/价格)
2. **移动支付文化** (5种语言各自的支付方式)
3. **讨价还价场景** (5种语言各自的规范)
4. **退货政策** (5种语言各自的差异)
5. **旅行购物场景** (预订/购买/退货/小票)

---

**原文 (英语)**: [[shopping-money]] | **相关镜像**: [[shopping-money.es|西班牙语]] · [[shopping-money.ja|日语]] · [[shopping-money.ko|韩语]] | **政策**: ADR-0006
