# 技術とインターネット — 言語間比較 (日本語版)

> 原文: [[tech-internet]] (English) | 作成日: 2026-08-20 | ADR-0006
> **5言語のデジタル語彙・SNS・モバイル決済・インターネット文化の比較**

---

## 早見表

### モバイル決済エコシステム

| プロバイダー | English (US/UK) | Spanish | Japan | Korea | China |
|----------|-----------------|---------|-------|-------|--------|
| **Native (cashless)** | Apple Pay, Google Pay, Venmo, Zelle | Bizum (Spain), Yape (Peru) | Suica/Pasmo (transit), **PayPay**, LINE Pay, Rakuten Pay | **Samsung Pay**, **Kakao Pay**, **Naver Pay**, Toss | **WeChat Pay (微信支付)**, **Alipay (支付宝)** — 普遍的 |
| **Adoption** | Tap cards common; mobile secondary | Growing; cash still dominant in LatAm | **Tap-pay high** (NFC ubiquitous) | **Near-universal** mobile pay | **Default** for most transactions |
| **QR Codes** | Growing | Plin (Peru), Mercado Pago | PayPay, d-barai | Kakao Pay QR, Naver Pay QR | **Universal** (every vendor) |

**主な文化パターン**:
- US: カードが依然中心、モバイル決済成長中
- Spain: Bizum for peer-to-peer
- Japan: Suica for transit (originally), now PayPay for general
- Korea: モバイル ファースト (Samsung Pay, Kakao Pay)
- China: **2015 年からモバイル ファースト**; WeChat/Alipay = デフォルト; 現金稀

### SNSプラットフォーム (国別)

#### 🇬🇧 英語圏 West (US/UK/AU/CA)
| プラットフォーム | ステータス | 用途 |
|----------|--------|---------|
| **Facebook** | **衰退中** (年配者) | 家族/グループ/イベント |
| **Instagram** | 若者に支配的 | 写真/動画 ストーリー |
| **TikTok** | **巨大** (Gen Z) | 短編動画 |
| **X (Twitter)** | ニッチ (ジャーナリスト/テック) | ニュース/言論 |
| **Snapchat** | ニッチ (Gen Z のみ) | 消えるメッセージ |
| **Reddit** | ニッチ | フォーラム/議論 |
| **LinkedIn** | プロフェッショナル | ネットワーキング |
| **YouTube** | 普遍的 | 長尺動画 |
| **WhatsApp** | UK/AU で普遍的 | メッセージ |

#### 🇪🇸 スペイン語圏 (Spain + LatAm)
| プラットフォーム | ステータス | 地域 |
|----------|--------|--------|
| **WhatsApp** | **普遍的** | 全て |
| **Facebook** | 支配的 (ラ米) | ラ米年配/家族 |
| **Instagram** | 支配的 (若者) | 全域 |
| **TikTok** | 成長中 | 若者 |
| **Twitter/X** | 政治的にアクティブ (Spain) | スペイン |
| **Telegram** | ニッチ | スペイン |

#### 🇯🇵 日本
| プラットフォーム | ステータス | 用途 |
|----------|--------|---------|
| **LINE** | **普遍的** (90%+) | メッセージ |
| **X (Twitter)** | **とても人気** (vs. 米国) | リアルタイム、ニュース |
| **Instagram** | 成長中 | 写真 ストーリー |
| **TikTok** | 成長中 | 若者動画 |
| **Facebook** | 年配/家族 | 家族グループ |
| **Mixi** | ニッチ | 年配 |
| **Ameblo** | ニッチ | ブログ |
| **Pixiv** | オタクアート | アートコミュニティ |
| **2channel/5ch** | 匿名フォーラム | 議論 |

#### 🇰🇷 韓国
| プラットフォーム | ステータス | 用途 |
|----------|--------|---------|
| **KakaoTalk** | **普遍的** (95%+) | メッセージ |
| **Instagram** | 支配的 (若者) | 写真 |
| **X (Twitter)** | 一般的 | 議論 |
| **Naver (Blog/Cafe)** | 支配的 (年配) | ブログ/フォーラム |
| **YouTube** | 普遍的 | 動画 |
| **Band** | ニッチ | グループチャット |
| **Tiktok** | 成長中 | 短編動画 |
| **Blind** | ニッチ | 職場匿名 |

#### 🇨🇳 中国
| プラットフォーム | ステータス | 用途 |
|----------|--------|---------|
| **WeChat (微信)** | **普遍的** (13 億+) | メッセージ、決済、ソーシャル、仕事 |
| **Weibo (微博)** | 支配的 (Twitter-like) | ニュース/議論 |
| **Douyin/TikTok (抖音)** | 支配的 (短編動画) | 動画 (国際 TikTok 別) |
| **Bilibili (B站)** | 若者/ACGN | 動画/アニメ |
| **Xiaohongshu (小红书)** | 成長中 (ライフスタイル) | レビュー |
| **Douban (豆瓣)** | 文化的レビュー | 映画/書籍/音楽 |
| **QQ** | 年配 | メッセージ |
| **Zhihu (知乎)** | Q&A | 知識 |
| **YouTube/FB/X** | **ブロック** | (VPN 必要) |

### デジタル語彙比較

#### デバイス・ハードウェア

| 用語 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **Computer** | Computer | Computadora / Ordenador | コンピュータ / パソコン (pasokon) | 컴퓨터 (keompyuteo) | 电脑 (diànnǎo) / 计算机 (jìsuànjī) |
| **Phone** | Phone / Cell phone | Teléfono / Celular / Móvil | 電話 / スマホ (sumaho) | 전화 (jeonhwa) / 핸드폰 (haendeupon) / 폰 (pon) | 电话 (diànhuà) / 手机 (shǒujī) |
| **Smartphone** | Smartphone | Smartphone / Móvil inteligente | スマートフォン | 스마트폰 (seumateupon) | 智能手机 (zhìnéng shǒujī) |
| **Laptop** | Laptop | Portátil / Laptop | ノートパソコン (nōto pasokon) | 노트북 (noteubuk) | 笔记本电脑 (bǐjìběn diànnǎo) |
| **Tablet** | Tablet | Tablet / Tableta | タブレット | 태블릿 (taebeullit) | 平板电脑 (píngbǎn diànnǎo) |
| **Charger** | Charger | Cargador | 充電器 (juudenki) | 충전기 (chujeongi) | 充电器 (chōngdiànqì) |
| **Headphones** | Headphones / Earbuds | Auriculares / Audífonos | ヘッドホン / イヤホン (iyahon) | 헤드폰 (hedeupon) / 이어폰 (ieopon) | 耳机 (ěrjī) |
| **Wi-Fi** | Wi-Fi | Wi-Fi | Wi-Fi / ワイファイ | 와이파이 (waipai) | Wi-Fi / 无线网 (wúxiànwǎng) |
| **Bluetooth** | Bluetooth | Bluetooth | ブルートゥース | 블루투스 (beullutuseu) | 蓝牙 (lán yá) |
| **Battery** | Battery | Batería | バッテリー | 배터리 (baeteori) | 电池 (diànchí) |
| **Screen** | Screen | Pantalla | 画面 (gamen) | 화면 (hwamyeon) | 屏幕 (píngmù) / 屏 (píng) |

#### ソフトウェア・アプリ

| 用語 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **App (application)** | App | Aplicación / App | アプリ (apuri) | 앱 (aep) | 应用 (yìngyòng) / App |
| **Website** | Website | Sitio web | ウェブサイト / ホームページ | 웹사이트 (waebsaijeu) | 网站 (wǎngzhàn) |
| **Browser** | Browser | Navegador | ブラウザ (burausa) | 브라우저 (beulaujeo) | 浏览器 (liúlǎnqì) |
| **Search** | Search | Buscar | 検索 (kensaku) | 검색 (geomsaek) | 搜索 (sōusuǒ) |
| **Email** | Email | Correo electrónico | メール (meeru) / Eメール | 이메일 (imeil) | 邮件 (yóujiàn) / 邮箱 (yóuxiāng) |
| **Password** | Password | Contraseña | パスワード (pasuwaado) | 비밀번호 (bimilbeonho) | 密码 (mìmǎ) |
| **Account** | Account | Cuenta | アカウント (akaunto) | 계정 (gyejeong) | 账号 (zhànghào) / 账户 (zhànghù) |
| **Login** | Login | Iniciar sesión | ログイン (roguin) | 로그인 (rogeuin) | 登录 (dēnglù) |
| **Logout** | Logout | Cerrar sesión | ログアウト (roguauto) | 로그아웃 (rogeuaut) | 退出 (tuìchū) / 注销 (zhùxiāo) |
| **Profile** | Profile | Perfil | プロフィール (purofiiru) | 프로필 (peuropil) | 个人资料 (gèrén zīliào) / 主页 (zhǔyè) |
| **Settings** | Settings | Ajustes / Configuración | 設定 (settei) | 설정 (seoljeong) | 设置 (shèzhì) |
| **Upload** | Upload | Subir / Cargar | アップロード (appu roodo) | 업로드 (eeprodeo) | 上传 (shàngchuán) |
| **Download** | Download | Descargar | ダウンロード (daun roodo) | 다운로드 (daunrodeu) | 下载 (xiàzài) |
| **Notification** | Notification | Notificación | 通知 (tsuuchi) | 알림 (allim) | 通知 (tōngzhī) |
| **DM (direct message)** | DM | Mensaje directo | DM / ダイレクトメッセージ | DM / 쪽지 (jjokji) | 私信 (sīxìn) / 私聊 (sīliáo) |

#### インターネット活動

| 活動 | English | Spanish | Japanese | Korean | Chinese |
|----------|---------|---------|----------|--------|---------|
| **Browse** | Browse | Navegar | 閲覧 (etsuran) / ブラウズ | 탐색 (tamseak) / 둘러보다 (deulleoboda) | 浏览 (liúlǎn) |
| **Search** | Search | Buscar | 検索する (kensaku suru) | 검색하다 (geomsaekada) | 搜索 (sōusuǒ) |
| **Click** | Click | Clic / Hacer clic | クリック (kurikku) | 클릭 (keullik) | 点击 (diǎnjī) |
| **Scroll** | Scroll | Desplazar / Scroll | スクロール (sukurooru) | 스크롤 (seukeurol) | 滚动 (gǔndòng) |
| **Stream** | Stream | Transmitir en vivo / Streaming | 配信 (haishin) / ストリーミング | 스트리밍 (seuteuriming) | 流媒体 (liúméitǐ) / 直播 (zhíbō) |
| **Download** | Download | Descargar | ダウンロードする | 다운로드하다 | 下载 (xiàzài) |
| **Share** | Share | Compartir | 共有 (kyouyuu) / シェア (shea) | 공유 (gongyu) / 공유하다 | 分享 (fēnxiǎng) |
| **Tag** | Tag | Etiquetar / Tag | タグ (tagu) | 태그 (taegu) | 标签 (biāoqiān) / @ |
| **Like** | Like | Me gusta | いいね (ii ne) | 좋아요 (johayo) | 赞 (zàn) / 点赞 (diǎnzàn) |
| **Comment** | Comment | Comentar | コメント (komento) | 댓글 (daetgeul) | 评论 (pínglùn) |
| **Follow** | Follow | Seguir | フォロー (foroo) | 팔로우 (pallow) | 关注 (guānzhù) |
| **Block** | Block | Bloquear | ブロック (burokku) | 차단 (chadan) / 블록 (beullok) | 拉黑 (lāhēi) / 屏蔽 (píngbì) |
| **Trending** | Trending | Tendencia | トレンド (torendo) | 트렌드 (teuraendeu) | 热门 (rèmén) / 趋势 (qūshì) |

### 絵文字・シンボル規約

#### 笑い

| 絵文字 | English | Spanish | Japanese | Korean | Chinese |
|-------|---------|---------|----------|--------|---------|
| **😂** (Face with Tears of Joy) | "LOL" / "Haha" | "Jaja" | "笑" (warau) | "ㅋㅋ" (kkk) | "2333" / "哈哈" |
| **🤣** (Rolling on Floor) | "ROFL" / "LMAO" | "JAJAJA" | "爆笑" (bakushou) | "ㅋㅋㅋㅋ" | "笑死" (xiàosǐ) |
| **😊** (Smiling with Halo) | "Aw shucks" / Sweet | "Sonrisa tierna" | "嬉しい" (ureshii) | "행복" (haengbok) | "开心" (kāixīn) |
| **😆** (Grinning Squinting) | "Haha" | "Jajaja" | "www" / "草" | "ㅋㅋㅋ" | "哈哈" |

#### 否定反応

| 絵文字 | English | Spanish | Japanese | Korean | Chinese |
|-------|---------|---------|----------|--------|---------|
| **😭** (Loudly Crying) | "I'm sobbing" | "Llorando" | "号泣" | "흑흑" (heukheuk) | "呜呜" (wūwū) |
| **😩** (Weary) | "I can't" | "No puedo" | "疲れた" (tsukareta) | "힘들어" | "累死" |
| **🙃** (Upside Down) | "Lol ironic" | "Irónico" | "皮肉" (hiniku) | "아이러니" | "反讽" |
| **💀** (Skull) | "I'm dead" / "Lethal" | "Morí" / "Ja ja" | "死んだ" (shinda) | "ㅋㅋㅋ" | "笑死" |

#### 愛情

| 絵文字 | English | Spanish | Japanese | Korean | Chinese |
|-------|---------|---------|----------|--------|---------|
| **❤️** (Red Heart) | "Love" | "Amor" | "好き" (suki) | "사랑해" (saranghae) | "爱" (ài) |
| **🥺** (Pleading) | "Pls?" / "Cute" | "Por favor" / "Tierno" | "お願い" (onegai) | "제발" (jebal) | "拜托" (bàituō) |
| **💕** (Two Hearts) | "Love" | "Amor" | "好き好き" | "짝사랑" | "爱爱" |
| **🥰** (Smiling with Hearts) | "Cutie" | "Precioso" | "好き好き好き" | "귀여워" | "可爱" |

#### 笑い文化ノート
- **English**: 😂 支配
- **Spanish**: 😂 支配
- **Japanese**: www (テキスト) / "w" (横向き顔) / "草" (kusa)
- **Korean**: ㅋㅋㅋ / ㅎㅎㅎ (韓国語特有子音)
- **Chinese**: 2333 / 哈哈 / 「笑死」

### 検索エンジン風景

| 国 | 主要検索 | 二次 | ノート |
|---------|----------------|-----------|-------|
| **US/UK/AU** | **Google** | Bing, DuckDuckGo | Google ~92% |
| **Spain** | **Google** | — | Google 支配 |
| **LatAm** | **Google** | — | Google 支配 |
| **Japan** | **Google** | Yahoo! Japan (legacy) | Yahoo JP まだ ~15% (Yahoo Auctions, mail) |
| **Korea** | **Naver** | Google (~10%) | **Naver 支配 ~60%** |
| **China** | **Baidu** | Bing (CN), Sogou | **Google ブロック**; Baidu ~75% |

### インターネット俗語頭文字比較

| English | Spanish | Japanese | Korean | Chinese |
|---------|---------|----------|--------|---------|
| lol = laughing out loud | jajaja = laughing | www / 草 = LOL | ㅋㅋ = LOL | 2333 = LOL (BBS code) |
| brb = be right back | ya vuelvo | すぐ戻る | 잠만 (jamman) | 马上回 |
| omg = oh my god | Dios mío | まじ / うそ | 헐 (heol) | 我去 / 我的天 |
| nvm = never mind | no importa | 気にしないで | 됐어 (dwaesseo) | 算了 (suànle) |
| idk = I don't know | no sé | わからん | 모르겠어 (moreugesseo) | 不知道 (bù zhīdào) |
| afk = away from keyboard | ausente | 離席中 | 자리비움 | 挂机 (guàjī) |
| ttyl = talk to you later | hablamos luego | またね | 나중에 봐 (najunge bwa) | 回聊 (huí liáo) |
| tbh = to be honest | para ser honesto | 正直に言うと | 솔직히 말하면 (soljighi malhamyeon) | 说实话 (shuō shíhuà) |

### モバイルアプリカテゴリ

| カテゴリ | English | Spanish | Japanese | Korean | Chinese |
|----------|---------|---------|----------|--------|---------|
| **Messaging** | Messages | Mensajes | メッセージ | 메시지 | 消息 (xiāoxi) |
| **Camera** | Camera | Cámara | カメラ (kamera) | 카메라 (kamela) | 相机 (xiàngjī) |
| **Maps** | Maps | Mapas | 地図 (chizu) | 지도 (jido) | 地图 (dìtú) |
| **Calculator** | Calculator | Calculadora | 電卓 (dentaku) | 계산기 (gyesangi) | 计算器 (jìsuànqì) |
| **Calendar** | Calendar | Calendario | カレンダー | 캘린더 (kaellinde) | 日历 (rìlì) |
| **Clock** | Clock | Reloj | 時計 (tokei) | 시계 (sigye) | 时钟 (shízhōng) |
| **Notes** | Notes | Notas | メモ (memo) | 메모 (memo) | 备忘录 (bèiwànglù) |
| **Music** | Music | Música | 音楽 (ongaku) | 음악 (eumak) | 音乐 (yīnyuè) |
| **Photos** | Photos | Fotos | 写真 (shashin) | 사진 (sajin) | 照片 (zhàopiàn) |

### オンラインショッピング用語

| 用語 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **Cart** | Cart / Basket | Carrito / Cesta | カート | 장바구니 (jangbaguni) | 购物车 (gòuwùchē) |
| **Checkout** | Checkout | Pago / Finalizar compra | チェックアウト | 결제 (gyeolje) | 结算 (jiésuàn) / 结账 (jiézhàng) |
| **Wishlist** | Wishlist | Lista de deseos | お気に入り (okiniiri) | 위시리스트 (wisiliseu) | 心愿单 (xīnyuàndān) / 收藏 (shōucáng) |
| **Coupon** | Coupon | Cupón | クーポン (kuupon) | 쿠폰 (kupon) | 优惠券 (yōuhuìquàn) |
| **Discount** | Discount / Sale | Descuento / Oferta | 割引 (waribiki) | 할인 (harin) | 折扣 (zhékòu) / 打折 (dǎzhé) |
| **Free shipping** | Free shipping | Envío gratis | 送料無料 (souryoumuryou) | 무료 배송 (mulyo baesong) | 包邮 (bāoyóu) |
| **Subscribe** | Subscribe | Suscribirse | 登録 (touroku) / 購読 | 구독 (gudok) | 订阅 (dìngyuè) |
| **Review** | Review | Reseña | レビュー (rebhyuu) | 리뷰 (ribyu) | 评价 (píngjià) / 点评 (diǎnpíng) |
| **Rating** | Rating | Calificación | 評価 (hyouka) | 평점 (pyeongjeom) | 评分 (píngfēn) / 星级 (xīngjí) |
| **Pre-order** | Pre-order | Reserva | 予約 (yoyaku) | 사전 예약 (sajeon yeyak) | 预订 (yùdìng) |

#### Eコマース プラットフォーム (国別)

| 国 | トッププラットフォーム | 2 番目 | ノート |
|---------|--------------|----|-------|
| **US** | Amazon | eBay, Etsy, Walmart | Amazon ~40% |
| **UK** | Amazon | eBay, Argos, Tesco | Amazon ~30% |
| **Spain** | Amazon.es | eBay, El Corte Inglés | Amazon ~25% |
| **Mexico** | Amazon MX | Mercado Libre, Walmart MX | Mercado Libre ~40% |
| **Argentina** | Mercado Libre | Tiendamia, Amazon | **Mercado Libre ~70%** |
| **Japan** | Amazon JP, **Rakuten** | Yahoo Shopping, Mercari | Rakuten ロイヤリティ 強力 |
| **Korea** | **Coupang**, Naver Smartstore, Gmarket, 11번가 | Auction, SSG | Coupang = ロケット配達 |
| **China** | **Taobao (淘宝)**, **JD.com**, **Pinduoduo** | Tmall, Xiaohongshu, Douyin shop | Taobao = C2C; Tmall = B2C; Pinduoduo = 割引 |

### ストリーミング/メディア

| サービス | English | Spanish | Japan | Korea | China |
|---------|---------|---------|-------|-------|--------|
| **Music streaming** | Spotify, Apple Music | Spotify, Apple Music | **Apple Music** (Spotify より支配的), LINE Music | Melon, Genie, FLO, Bugs | NetEase Cloud Music (网易云音乐), QQ Music, KuGou |
| **Video streaming** | Netflix, Disney+, Amazon Prime | Netflix, HBO Max | Netflix, Amazon Prime, **U-NEXT**, ABEMA, Hulu JP | Netflix, **Wavve**, **Tving**, Watcha | **iQiyi (爱奇艺)**, **Tencent Video (腾讯视频)**, **Youku** |
| **Short video** | TikTok, YouTube Shorts | TikTok | TikTok | TikTok | **Douyin (抖音)** (TikTok 国際版 別), Kuaishou (快手) |
| **Live streaming** | Twitch, YouTube Live | Twitch, YouTube Live | **Niconico Live**, Twitch | AfreecaTV, CHZZK | **Douyin Live**, **Taobao Live**, Bilibili Live |

### 技術用語: 一般的な借用語/頭文字

| 概念 | EN | ES | JP | KR | CH |
|---------|----|----|----|----|----|
| **AI** | AI | IA | AI / 人工知能 (jinkou chinou) | AI / 인공지능 (ingongjineung) | AI / 人工智能 (réngōng zhìnéng) |
| **VPN** | VPN | VPN | VPN | VPN | VPN / 翻墙 (fānqiáng) |
| **Streaming** | Streaming | Streaming | ストリーミング | 스트리밍 | 流媒体 / 直播 |
| **URL** | URL | URL / Enlace | URL | URL | URL / 链接 (liànjiē) |
| **Blog** | Blog | Blog | ブログ (burogu) | 블로그 (beullogeu) | 博客 (bókè) |
| **Vlog** | Vlog | Vlog | Vlog / ブイログ | 브이로그 (beuirogeu) | Vlog / 视频博客 |
| **Influencer** | Influencer | Influencer | インフルエンサー (infuruensaa) | 인플루언서 (inpeullueonseo) | 网红 (wǎnghóng) |
| **V-Tuber** | VTuber | VTuber | VTuber / バーチャルYouTuber | 버추얼 유튜버 (beochueol yutyubeo) | 虚拟主播 (xūnǐ zhǔbō) |
| **Meme** | Meme | Meme | ミーム (miimu) | 밈 (mim) | 梗 (gěng) / 表情包 (biǎoqíngbāo) |

### 技術会社のローカル同等品

| 機能 | US | Spain | Japan | Korea | China |
|----------|----|----|----|----|----|
| **Search** | Google | Google | Google | **Naver** | **Baidu** |
| **Video** | YouTube | YouTube | YouTube, Niconico | YouTube | **Bilibili**, Youku |
| **Maps** | Google Maps | Google Maps | Google Maps | **Naver Maps**, Kakao Map | **Baidu Maps**, Amap (高德) |
| **Email** | Gmail | Gmail | Gmail, Yahoo JP | **Naver Mail**, Daum Mail | **QQ Mail**, NetEase Mail (163) |
| **Pay** | PayPal, Venmo | Bizum | PayPay | Kakao Pay | **Alipay**, WeChat Pay |
| **Ride-share** | Uber, Lyft | Uber, Cabify | **JapanTaxi**, Uber | **Kakao T** | **Didi (滴滴)** |
| **Delivery** | DoorDash, Uber Eats | Glovo, Deliveroo | **Demae-can (出前館)**, Uber Eats | **Coupang Eats**, Baemin (배달의민족) | **Meituan (美团)**, Ele.me (饿了么) |
| **Cloud** | AWS, Azure, GCP | AWS, Azure | AWS, Azure, **Sakura Cloud** | AWS, Naver Cloud, NHN Cloud | **Aliyun (阿里云)**, Tencent Cloud, Huawei Cloud |

### ハッシュタグ・シンボル規約

| 概念 | English | Spanish | Japanese | Korean | Chinese |
|---------|---------|---------|----------|--------|---------|
| **Hashtag** | # | # | # / 全タグ (zen tagu) | # / 해시태그 | # |
| **Mention** | @username | @usuario | @ / ID | @ / 아이디 | @ |
| **Link** | URL | URL/enlace | URL/リンク | URL/링크 | URL/链接 (liànjiē) |
| **Bookmark** | 🔖 / Save | 🔖 / Guardar | 🔖 / 保存 (hozon) | 🔖 / 저장 (jeojang) | 🔖 / 收藏 (shōucáng) |
| **Trending (Twitter)** | Trending | Tendencia | トレンド (torendo) | 실시간 트렌드 (silsigan teuraendeu) | 热搜 (rèsōu) |

### AI/ML 特定語彙

| 用語 | EN | ES | JP | KR | CH |
|------|----|----|----|----|----|
| **ChatGPT/AI chatbot** | Chatbot | Chatbot | チャットボット | 챗봇 (chaetbot) | 聊天机器人 (liáotiān jīqìrén) |
| **Prompt** | Prompt | Prompt / Indicación | プロンプト | 프롬프트 (peurompteu) | 提示词 (tíshìcí) |
| **Token** | Token | Token | トークン | 토큰 (token) | Token / 标记 (biāojì) |
| **Model** | Model | Modelo | モデル (moderu) | 모델 (model) | 模型 (móxíng) |
| **Hallucination** | Hallucination | Alucinación | ハルシネーション (harushineeshon) | 환각 (hwangak) / 할루시네이션 (hallusineisyeon) | 幻觉 (huànjué) |
| **Fine-tune** | Fine-tune | Ajuste fino | ファインチューン | 파인튜닝 (paineutyuning) | 微调 (wēitiáo) |
| **RAG** | RAG | RAG | RAG | RAG | RAG / 检索增强生成 (jiǎnsuǒ zēngqiáng shēngchéng) |
| **Embedding** | Embedding | Embedding / Incrustación | 埋め込み (umekomi) | 임베딩 (imbeding) | 嵌入 (qiànrù) |
| **RLHF** | RLHF | RLHF | RLHF | RLHF | RLHF / 基于人类反馈的强化学习 |

---

## クイックリファレンスカード

| 概念 | EN | ES | JP | KR | CH |
|---------|----|----|----|----|----|
| **Internet** | Internet | Internet | インターネット | 인터넷 (inteonet) | 互联网 (hùliánwǎng) / 因特网 |
| **Website** | Website | Sitio web | ウェブサイト | 웹사이트 | 网站 |
| **App** | App | Aplicación | アプリ | 앱 | 应用 (yìngyòng) |
| **Search engine** | Google | Google | Google, Yahoo | Naver | Baidu |
| **Messenger** | Messenger, WhatsApp | WhatsApp | LINE | KakaoTalk | WeChat |
| **Phone** | Smartphone | Smartphone / Móvil | スマホ | 스마트폰 | 手机 |
| **Like** | Like | Me gusta | いいね | 좋아요 | 赞 |
| **LOL** | lol | jajaja | 草 / www | ㅋㅋ | 2333 / 哈哈 |
| **Streaming** | Stream | Streaming | 配信 | 스트리밍 | 流媒体 |
| **E-commerce** | Amazon | Amazon | Amazon, Rakuten | Coupang | Taobao, JD |
| **Mobile pay** | Apple Pay, Venmo | Bizum | PayPay | Kakao Pay | 微信支付 / 支付宝 |
| **Hash** | # | # | # | # | # |
| **Mention** | @ | @ | @ | @ | @ |

---

## 関連ページ

- `[[slang-colloquial]]` — デジタル俗語
- `[[dating-romance]]` — デートアプリ
- `[[shopping-money]]` — モバイル決済システム
- `[[business-email]]` — メール/Slack/Teams 規約
- `[[untranslatable-concepts]]` — *netatmo, nettle* メタファー

## 出典

- StatCounter Global Stats (2024) — 検索エンジン市場シェア
- DataReportal — Digital 2024 country reports
- Sensor Tower — アプリランキング
- `[[index]]`
- `[Spanish/vocabulary/basic-vocabulary]`, `[[index]]`
- `[Japanese/vocabulary/business-vocabulary]`, `[Japanese/sources/technology-and-internet]`
- `[[index]]`, `[Korean/sources/technology-and-internet]`
- `[[index]]`, `[Chinese/sources/pinyin-basics-zh]`

---

## 🇯🇵 日本語学習者ノート (Japanese Learner Notes)

> 本セクションは日本語学習者向けの追加学習ガイドです。

### 日本語話者が他4言語の技術・インターネット用語を学ぶ際の一般的な落とし穴

1. **モバイル決済の国別支配**:
   - 日本は PayPay / Suica / LINE Pay → 中国は WeChat Pay / Alipay (絶対的) → 韓国は Samsung Pay / Kakao Pay → 英語圏は Apple Pay / Google Pay。
   - **落とし穴**: 日本語話者が中国/韓国旅行で現金やカード中心 → QR コード決済のみ受付店で詰む。
   - **練習法**: 中国/韓国の WeChat Pay / Kakao Pay を旅行前にインストール・登録。

2. **SMS 頭文字の文化差**:
   - 日本語の「草」/「www」 → 韓国語「ㅋㅋㅋ」 → 中国語「2333」 → 英語「lol」 → スペイン語「jajaja」。
   - **落とし穴**: 日本語話者が英語「lol」を「笑」と翻訳 → ネイティブは「lol」自体の使用。
   - **練習法**: 5言語の「laugh テキスト」 (www / ㅋㅋ / 2333 / lol / jajaja) を比較表で。

3. **漢字文化 vs 借用語 (technology)**:
   - 日本語の技術を漢字で書く (音読み) vs 韓国語 (漢字音) vs 中国語 (簡体字) vs 英語 (loanword)。
   - **落とし穴**: 日本語の「検索」(kensaku) と中国語の「搜索」(sōusuǒ)、「電話」(denwa) と韓国語の「전화」(jeonhwa) と中国語の「电话」(diànhuà)。
   - **練習法**: 漢字技術語彙 (電話/电话/전화, 検索/搜索/검색) を 5言語対応表で。

4. **SNS プラットフォームの国別差**:
   - 日本は LINE/X (Twitter) → 韓国は KakaoTalk/Naver → 中国は WeChat/Weibo → 英語圏は WhatsApp/Meta。
   - **落とし穴**: 日本語話者が中国で WhatsApp を使用 → block されている。
   - **練習法**: 5言語圏の主要 SNS プラットフォームと利用率を 5言語対応表で。

5. **検索エンジンの国別支配**:
   - 英語圏と日本/スペインは Google 支配 → 韓国は Naver 支配 → 中国は Baidu (Google 不可)。
   - **落とし穴**: 日本語話者が韓国/中国で Google 検索 → 韓国では Google 比率 10%、中国では block。
   - **練習法**: 韓国の Naver、中国の Baidu をそれぞれ旅行前に試用。

### 関連日本語ウィキページ

- `[[slang-colloquial]]` — デジタル俗語
- `[[dating-romance]]` — デートアプリ
- `[[shopping-money]]` — モバイル決済システム
- `[[business-email]]` — メール規約
- `[[untranslatable-concepts]]` — 翻訳不能な概念

### 学習ワークフロー推奨

1. **5言語技術語彙対応表** (上記早見表) を暗記
2. **モバイル決済** (PayPay / WeChat Pay / Kakao Pay) の比較表
3. **SMS 頭文字** (www / ㅋㅋ / 2333) の比較表
4. **漢字技術語彙** (電話/电话/전화) の 5言語対応
5. **国別主要 SNS** を 5言語対応表で

---

**原文 (英語)**: [[tech-internet]] | **関連ミラー**: [[tech-internet.es|スペイン語]] · [[tech-internet.ko|韓国語]] · [[tech-internet.zh|中国語]] | **ポリシー**: ADR-0006
