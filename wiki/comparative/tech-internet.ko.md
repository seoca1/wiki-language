# 기술 & 인터넷 — 다국어 비교 (한국어판)

> 원본: [[tech-internet]] (English) | 작성일: 2026-08-20 | ADR-0006
> **5개 언어 디지털 어휘 비교 — 소셜 미디어, 모바일 결제, 인터넷 문화**

---

## 빠른 참조 표

### 모바일 결제 생태계

| 제공자 | English (US/UK) | Spanish | Japan | Korea | China |
|----------|-----------------|---------|-------|-------|--------|
| **네이티브 (현금less)** | Apple Pay, Google Pay, Venmo, Zelle | Bizum (Spain), Yape (Peru) | Suica/Pasmo (transit), **PayPay**, LINE Pay, Rakuten Pay | **Samsung Pay**, **Kakao Pay**, **Naver Pay**, Toss | **WeChat Pay (微信支付)**, **Alipay (支付宝)** — 거의 보편 |
| **채택** | 탭 카드 일반; 모바일 차선 | 증가; 라틴아메리카 현금 우세 | **탭-페이 높음** (NFC 보편) | **거의 보편** 모바일 페이 | **기본** 대부분의 거래 |
| **QR 코드** | 증가 | Plin (Peru), Mercado Pago | PayPay, d-barai | Kakao Pay QR, Naver Pay QR | **보편** (모든 상점) |

**핵심 문화 패턴**:
- 미국: 카드 여전히 1차, 모바일 페이 증가
- 스페인: Bizum (P2P)
- 일본: Suica (교통, 원래), 이제 PayPay (일반)
- 한국: 모바일 우선 (Samsung Pay, Kakao Pay)
- 중국: **2015년부터 모바일 우선**; WeChat/Alipay = 기본; 현금 드물다

### 국가별 소셜 미디어 플랫폼

### 영어권 (US/UK/AU/CA)
| 플랫폼 | 상태 | 용도 |
|----------|--------|-----|
| **Facebook** | **쇠퇴** (고연령) | 가족/그룹/이벤트 |
| **Instagram** | 청년 지배 | 사진/비디오 스토리 |
| **TikTok** | **거대** (Gen Z) | 짧은 비디오 |
| **X (Twitter)** | 틈새 (저널리스트/기술) | 뉴스/담론 |
| **Snapchat** | 틈새 (Gen Z 한정) | 사라지는 메시지 |
| **Reddit** | 틈새 | 포럼/토론 |
| **LinkedIn** | 직업 | 네트워킹 |
| **YouTube** | 보편 | 긴 비디오 |
| **WhatsApp** | UK/AU 보편 | 메시징 |

### 스페인어권 (Spain + LatAm)
| 플랫폼 | 상태 | 지역 |
|----------|--------|--------|
| **WhatsApp** | **보편** | 전체 |
| **Facebook** | 지배 (LatAm) | LatAm 고연령/가족 |
| **Instagram** | 지배 (청년) | 전체 |
| **TikTok** | 증가 | 청년 |
| **Twitter/X** | 정치적 활동 (Spain) | Spain |
| **Telegram** | 틈새 | Spain |

### 일본
| 플랫폼 | 상태 | 용도 |
|----------|--------|-----|
| **LINE** | **보편** (90%+) | 메시징 |
| **X (Twitter)** | **매우 인기** (미국보다) | 실시간, 뉴스 |
| **Instagram** | 증가 | 사진 스토리 |
| **TikTok** | 증가 | 청년 비디오 |
| **Facebook** | 고연령/가족 | 가족 그룹 |
| **Mixi** | 틈새 | 고연령 |
| **Ameblo** | 틈새 | 블로그 |
| **Pixiv** | Otaku 예술 | 예술 커뮤니티 |
| **2channel/5ch** | 익명 포럼 | 토론 |

### 한국
| 플랫폼 | 상태 | 용도 |
|----------|--------|--------|
| **KakaoTalk** | **보편** (95%+) | 메시징 |
| **Instagram** | 지배 (청년) | 사진 |
| **X (Twitter)** | 일반 | 담론 |
| **Naver (Blog/Cafe)** | 지배 (고연령) | 블로그/포럼 |
| **YouTube** | 보편 | 비디오 |
| **Band** | 틈새 | 그룹 채팅 |
| **Tiktok** | 증가 | 짧은 비디오 |
| **Blind** | 틈새 | 직장 익명 |

### 중국
| 플랫폼 | 상태 | 용도 |
|----------|--------|--------|
| **WeChat (微信)** | **보편** (1.3B+) | 메시징, 페이, 소셜, 직장 |
| **Weibo (微博)** | 지배 (Twitter-같은) | 뉴스/담론 |
| **Douyin/TikTok (抖音)** | 지배 (짧은 비디오) | 비디오 (TikTok 국제 분리) |
| **Bilibili (B站)** | 청년/ACGN | 비디오/애니 |
| **Xiaohongshu (小红书)** | 증가 (라이프스타일) | 리뷰 |
| **Douban (豆瓣)** | 문화 리뷰 | 영화/책/음악 |
| **QQ** | 고연령 | 메시징 |
| **Zhihu (知乎)** | Q&A | 지식 |
| **YouTube/FB/X** | **차단** | (VPN 필요) |

### 디지털 어휘 비교

#### 기기 & 하드웨어

| 단어 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **컴퓨터** | Computer | Computadora / Ordenador | コンピュータ / パソコン (pasokon) | 컴퓨터 (keompyuteo) | 电脑 (diànnǎo) / 计算机 (jìsuànjī) |
| **전화** | Phone / Cell phone | Teléfono / Celular / Móvil | 電話 / スマホ (sumaho) | 전화 (jeonhwa) / 핸드폰 (haendeupon) / 폰 (pon) | 电话 (diànhuà) / 手机 (shǒujī) |
| **스마트폰** | Smartphone | Smartphone / Móvil inteligente | スマートフォン | 스마트폰 (seumateupon) | 智能手机 (zhìnéng shǒujī) |
| **노트북** | Laptop | Portátil / Laptop | ノートパソコン (nōto pasokon) | 노트북 (noteubuk) | 笔记本电脑 (bǐjìběn diànnǎo) |
| **태블릿** | Tablet | Tablet / Tableta | タブレット | 태블릿 (taebeullit) | 平板电脑 (píngbǎn diànnǎo) |
| **충전기** | Charger | Cargador | 充電器 (juudenki) | 충전기 (chujeongi) | 充电器 (chōngdiànqì) |
| **헤드폰** | Headphones / Earbuds | Auriculares / Audífonos | ヘッドホン / イヤホン (iyahon) | 헤드폰 (hedeupon) / 이어폰 (ieopon) | 耳机 (ěrjī) |
| **Wi-Fi** | Wi-Fi | Wi-Fi | Wi-Fi / ワイファイ | 와이파이 (waipai) | Wi-Fi / 无线网 (wúxiànwǎng) |
| **블루투스** | Bluetooth | Bluetooth | ブルートゥース | 블루투스 (beullutuseu) | 蓝牙 (lán yá) |
| **배터리** | Battery | Batería | バッテリー | 배터리 (baeteori) | 电池 (diànchí) |
| **화면** | Screen | Pantalla | 画面 (gamen) | 화면 (hwamyeon) | 屏幕 (píngmù) / 屏 (píng) |

#### 소프트웨어 & 앱

| 단어 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **앱** | App | Aplicación / App | アプリ (apuri) | 앱 (aep) | 应用 (yìngyòng) / App |
| **웹사이트** | Website | Sitio web | ウェブサイト / ホームページ | 웹사이트 (waebsaijeu) | 网站 (wǎngzhàn) |
| **브라우저** | Browser | Navegador | ブラウザ (burausa) | 브라우저 (beulaujeo) | 浏览器 (liúlǎnqì) |
| **검색** | Search | Buscar | 検索 (kensaku) | 검색 (geomsaek) | 搜索 (sōusuǒ) |
| **이메일** | Email | Correo electrónico | メール (meeru) / Eメール | 이메일 (imeil) | 邮件 (yóujiàn) / 邮箱 (yóuxiāng) |
| **비밀번호** | Password | Contraseña | パスワード (pasuwaado) | 비밀번호 (bimilbeonho) | 密码 (mìmǎ) |
| **계정** | Account | Cuenta | アカウント (akaunto) | 계정 (gyejeong) | 账号 (zhànghào) / 账户 (zhànghù) |
| **로그인** | Login | Iniciar sesión | ログイン (roguin) | 로그인 (rogeuin) | 登录 (dēnglù) |
| **로그아웃** | Logout | Cerrar sesión | ログアウト (roguauto) | 로그아웃 (rogeuaut) | 退出 (tuìchū) / 注销 (zhùxiāo) |
| **프로필** | Profile | Perfil | プロフィール (purofiiru) | 프로필 (peuropil) | 个人资料 (gèrén zīliào) / 主页 (zhǔyè) |
| **설정** | Settings | Ajustes / Configuración | 設定 (settei) | 설정 (seoljeong) | 设置 (shèzhì) |
| **업로드** | Upload | Subir / Cargar | アップロード (appu roodo) | 업로드 (eeprodeo) | 上传 (shàngchuán) |
| **다운로드** | Download | Descargar | ダウンロード (daun roodo) | 다운로드 (daunrodeu) | 下载 (xiàzài) |
| **알림** | Notification | Notificación | 通知 (tsuuchi) | 알림 (allim) | 通知 (tōngzhī) |
| **DM** | DM (direct message) | Mensaje directo | DM / ダイレクトメッセージ | DM / 쪽지 (jjokji) | 私信 (sīxìn) / 私聊 (sīliáo) |

#### 인터넷 활동

| 활동 | English | Spanish | Japanese | Korean | Chinese |
|----------|---------|---------|----------|--------|---------|
| **탐색** | Browse | Navegar | 閲覧 (etsuran) / ブラウズ | 탐색 (tamseak) / 둘러보다 (deulleoboda) | 浏览 (liúlǎn) |
| **검색** | Search | Buscar | 検索する (kensaku suru) | 검색하다 (geomsaekada) | 搜索 (sōusuǒ) |
| **클릭** | Click | Clic / Hacer clic | クリック (kurikku) | 클릭 (keullik) | 点击 (diǎnjī) |
| **스크롤** | Scroll | Desplazar / Scroll | スクロール (sukurooru) | 스크롤 (seukeurol) | 滚动 (gǔndòng) |
| **스트리밍** | Stream | Transmitir en vivo / Streaming | 配信 (haishin) / ストリーミング | 스트리밍 (seuteuriming) | 流媒体 (liúméitǐ) / 直播 (zhíbō) |
| **다운로드** | Download | Descargar | ダウンロードする | 다운로드하다 | 下载 (xiàzài) |
| **공유** | Share | Compartir | 共有 (kyouyuu) / シェア (shea) | 공유 (gongyu) / 공유하다 | 分享 (fēnxiǎng) |
| **태그** | Tag | Etiquetar / Tag | タグ (tagu) | 태그 (taegu) | 标签 (biāoqiān) / @ |
| **좋아요** | Like | Me gusta | いいね (ii ne) | 좋아요 (johayo) | 赞 (zàn) / 点赞 (diǎnzàn) |
| **댓글** | Comment | Comentar | コメント (komento) | 댓글 (daetgeul) | 评论 (pínglùn) |
| **팔로우** | Follow | Seguir | フォロー (foroo) | 팔로우 (pallow) | 关注 (guānzhù) |
| **차단** | Block | Bloquear | ブロック (burokku) | 차단 (chadan) / 블록 (beullok) | 拉黑 (lāhēi) / 屏蔽 (píngbì) |
| **트렌드** | Trending | Tendencia | トレンド (torendo) | 트렌드 (teuraendeu) | 热门 (rèmén) / 趋势 (qūshì) |

### 이모지 & 심볼 관행

#### 웃음

| 이모지 | English | Spanish | Japanese | Korean | Chinese |
|-------|---------|---------|----------|--------|---------|
| **😂** (Face with Tears of Joy) | "LOL" / "Haha" | "Jaja" | "笑" (warau) | "ㅋㅋ" (kkk) | "2333" / "哈哈" |
| **🤣** (Rolling on Floor) | "ROFL" / "LMAO" | "JAJAJA" | "爆笑" (bakushou) | "ㅋㅋㅋㅋ" | "笑死" (xiàosǐ) |
| **😊** (Smiling with Halo) | "Aw shucks" / Sweet | "Sonrisa tierna" | "嬉しい" (ureshii) | "행복" (haengbok) | "开心" (kāixīn) |
| **😆** (Grinning Squinting) | "Haha" | "Jajaja" | "www" / "草" | "ㅋㅋㅋ" | "哈哈" |

#### 부정 반응

| 이모지 | English | Spanish | Japanese | Korean | Chinese |
|-------|---------|---------|----------|--------|---------|
| **😭** (Loudly Crying) | "I'm sobbing" | "Llorando" | "号泣" | "흑흑" (heukheuk) | "呜呜" (wūwū) |
| **😩** (Weary) | "I can't" | "No puedo" | "疲れた" (tsukareta) | "힘들어" | "累死" |
| **🙃** (Upside Down) | "Lol ironic" | "Irónico" | "皮肉" (hiniku) | "아이러니" | "反讽" |
| **💀** (Skull) | "I'm dead" / "Lethal" | "Morí" / "Ja ja" | "死んだ" (shinda) | "ㅋㅋㅋ" | "笑死" |

#### 애정

| 이모지 | English | Spanish | Japanese | Korean | Chinese |
|-------|---------|---------|----------|--------|---------|
| **❤️** (Red Heart) | "Love" | "Amor" | "好き" (suki) | "사랑해" (saranghae) | "爱" (ài) |
| **🥺** (Pleading) | "Pls?" / "Cute" | "Por favor" / "Tierno" | "お願い" (onegai) | "제발" (jebal) | "拜托" (bàituō) |
| **💕** (Two Hearts) | "Love" | "Amor" | "好き好き" | "짝사랑" | "爱爱" |
| **🥰** (Smiling with Hearts) | "Cutie" | "Precioso" | "好き好き好き" | "귀여워" | "可爱" |

### 검색 엔진 환경

| 국가 | 1차 검색 | 2차 | 비고 |
|---------|----------------|-----------|-------|
| **US/UK/AU** | **Google** | Bing, DuckDuckGo | Google ~92% |
| **Spain** | **Google** | — | Google 지배 |
| **LatAm** | **Google** | — | Google 지배 |
| **Japan** | **Google** | Yahoo! Japan (레거시) | Yahoo JP 아직 ~15% (Yahoo Auctions, 메일) |
| **Korea** | **Naver** | Google (~10%) | **Naver 지배 ~60%** |
| **China** | **Baidu** | Bing (CN), Sogou | **Google 차단**; Baidu ~75% |

### 인터넷 슬랭 약어 비교

| English | Spanish | Japanese | Korean | Chinese |
|---------|---------|----------|--------|---------|
| lol = laughing out loud | jajaja = laughing | www / 草 = LOL | ㅋㅋ = LOL | 2333 = LOL (BBS 코드) |
| brb = be right back | ya vuelvo | すぐ戻る | 잠만 (jamman) | 马上回 |
| omg = oh my god | Dios mío | まじ / うそ | 헐 (heol) | 我去 / 我的天 |
| nvm = never mind | no importa | 気にしないで | 됐어 (dwaesseo) | 算了 (suànle) |
| idk = I don't know | no sé | わからん | 모르겠어 (moreugesseo) | 不知道 (bù zhīdào) |
| afk = away from keyboard | ausente | 離席中 | 자리비움 | 挂机 (guàjī) |
| ttyl = talk to you later | hablamos luego | またね | 나중에 봐 (najunge bwa) | 回聊 (huí liáo) |
| tbh = to be honest | para ser honesto | 正直に言うと | 솔직히 말하면 (soljighi malhamyeon) | 说实话 (shuō shíhuà) |

### 모바일 앱 카테고리

| 카테고리 | English | Spanish | Japanese | Korean | Chinese |
|----------|---------|---------|----------|--------|---------|
| **메시지** | Messages | Mensajes | メッセージ | 메시지 | 消息 (xiāoxi) |
| **카메라** | Camera | Cámara | カメラ (kamera) | 카메라 (kamela) | 相机 (xiàngjī) |
| **지도** | Maps | Mapas | 地図 (chizu) | 지도 (jido) | 地图 (dìtú) |
| **계산기** | Calculator | Calculadora | 電卓 (dentaku) | 계산기 (gyesangi) | 计算器 (jìsuànqì) |
| **달력** | Calendar | Calendario | カレンダー | 캘린더 (kaellinde) | 日历 (rìlì) |
| **시계** | Clock | Reloj | 時計 (tokei) | 시계 (sigye) | 时钟 (shízhōng) |
| **메모** | Notes | Notas | メモ (memo) | 메모 (memo) | 备忘录 (bèiwànglù) |
| **음악** | Music | Música | 音楽 (ongaku) | 음악 (eumak) | 音乐 (yīnyuè) |
| **사진** | Photos | Fotos | 写真 (shashin) | 사진 (sajin) | 照片 (zhàopiàn) |

### 온라인 쇼핑 어휘

| 단어 | English | Spanish | Japanese | Korean | Chinese |
|------|---------|---------|----------|--------|---------|
| **장바구니** | Cart / Basket | Carrito / Cesta | カート | 장바구니 (jangbaguni) | 购物车 (gòuwùchē) |
| **결제** | Checkout | Pago / Finalizar compra | チェックアウト | 결제 (gyeolje) | 结算 (jiésuàn) / 结账 (jiézhàng) |
| **위시리스트** | Wishlist | Lista de deseos | お気に入り (okiniiri) | 위시리스트 (wisiliseu) | 心愿单 (xīnyuàndān) / 收藏 (shōucáng) |
| **쿠폰** | Coupon | Cupón | クーポン (kuupon) | 쿠폰 (kupon) | 优惠券 (yōuhuìquàn) |
| **할인** | Discount / Sale | Descuento / Oferta | 割引 (waribiki) | 할인 (harin) | 折扣 (zhékòu) / 打折 (dǎzhé) |
| **무료 배송** | Free shipping | Envío gratis | 送料無料 (souryoumuryou) | 무료 배송 (mulyo baesong) | 包邮 (bāoyóu) |
| **구독** | Subscribe | Suscribirse | 登録 (touroku) / 購読 | 구독 (gudok) | 订阅 (dìngyuè) |
| **리뷰** | Review | Reseña | レビュー (rebhyuu) | 리뷰 (ribyu) | 评价 (píngjià) / 点评 (diǎnpíng) |
| **평점** | Rating | Calificación | 評価 (hyouka) | 평점 (pyeongjeom) | 评分 (píngfēn) / 星级 (xīngjí) |
| **사전 예약** | Pre-order | Reserva | 予約 (yoyaku) | 사전 예약 (sajeon yeyak) | 预订 (yùdìng) |

### 국가별 E-커머스 플랫폼

| 국가 | 1위 플랫폼 | 2위 | 비고 |
|---------|--------------|----|-------| 
| **US** | Amazon | eBay, Etsy, Walmart | Amazon ~40% |
| **UK** | Amazon | eBay, Argos, Tesco | Amazon ~30% |
| **Spain** | Amazon.es | eBay, El Corte Inglés | Amazon ~25% |
| **Mexico** | Amazon MX | Mercado Libre, Walmart MX | Mercado Libre ~40% |
| **Argentina** | Mercado Libre | Tiendamia, Amazon | **Mercado Libre ~70%** |
| **Japan** | Amazon JP, **Rakuten** | Yahoo Shopping, Mercari | Rakuten loyalty 강력 |
| **Korea** | **Coupang**, Naver Smartstore, Gmarket, 11번가 | Auction, SSG | Coupang = 로켓 배송 |
| **China** | **Taobao (淘宝)**, **JD.com**, **Pinduoduo** | Tmall, Xiaohongshu, Douyin shop | Taobao = C2C; Tmall = B2C; Pinduoduo = 할인 |

### 스트리밍/미디어

| 서비스 | English | Spanish | Japan | Korea | China |
|---------|---------|---------|-------|-------|--------|
| **음악 스트리밍** | Spotify, Apple Music | Spotify, Apple Music | **Apple Music** (Spotify보다 우세), LINE Music | Melon, Genie, FLO, Bugs | NetEase Cloud Music (网易云音乐), QQ Music, KuGou |
| **비디오 스트리밍** | Netflix, Disney+, Amazon Prime | Netflix, HBO Max | Netflix, Amazon Prime, **U-NEXT**, ABEMA, Hulu JP | Netflix, **Wavve**, **Tving**, Watcha | **iQiyi (爱奇艺)**, **Tencent Video (腾讯视频)**, **Youku** |
| **짧은 비디오** | TikTok, YouTube Shorts | TikTok | TikTok | TikTok | **Douyin (抖音)** (TikTok과 분리), Kuaishou (快手) |
| **라이브 스트리밍** | Twitch, YouTube Live | Twitch, YouTube Live | **Niconico Live**, Twitch | AfreecaTV, CHZZK | **Douyin Live**, **Taobao Live**, Bilibili Live |

### 기술 용어: 일반 차용어/약어

| 개념 | EN | ES | JP | KR | CH |
|---------|----|----|----|----|----|
| **AI** | AI | IA | AI / 人工知能 (jinkou chinou) | AI / 인공지능 (ingongjineung) | AI / 人工智能 (réngōng zhìnéng) |
| **VPN** | VPN | VPN | VPN | VPN | VPN / 翻墙 (fānqiáng) |
| **스트리밍** | Streaming | Streaming | ストリーミング | 스트리밍 | 流媒体 / 直播 |
| **URL** | URL | URL / Enlace | URL | URL | URL / 链接 (liànjiē) |
| **블로그** | Blog | Blog | ブログ (burogu) | 블로그 (beullogeu) | 博客 (bókè) |
| **브이로그** | Vlog | Vlog | Vlog / ブイログ | 브이로그 (beuirogeu) | Vlog / 视频博客 |
| **인플루언서** | Influencer | Influencer | インフルエンサー (infuruensaa) | 인플루언서 (inpeullueonseo) | 网红 (wǎnghóng) |
| **버추얼 유튜버** | VTuber | VTuber | VTuber / バーチャルYouTuber | 버추얼 유튜버 (beochueol yutyubeo) | 虚拟主播 (xūnǐ zhǔbō) |
| **밈** | Meme | Meme | ミーム (miimu) | 밈 (mim) | 梗 (gěng) / 表情包 (biǎoqíngbāo) |

### 기술 회사 로컬 등가물

| 기능 | US | Spain | Japan | Korea | China |
|----------|----|----|----|----|----|
| **검색** | Google | Google | Google | **Naver** | **Baidu** |
| **비디오** | YouTube | YouTube | YouTube, Niconico | YouTube | **Bilibili**, Youku |
| **지도** | Google Maps | Google Maps | Google Maps | **Naver Maps**, Kakao Map | **Baidu Maps**, Amap (高德) |
| **이메일** | Gmail | Gmail | Gmail, Yahoo JP | **Naver Mail**, Daum Mail | **QQ Mail**, NetEase Mail (163) |
| **페이** | PayPal, Venmo | Bizum | PayPay | Kakao Pay | **Alipay**, WeChat Pay |
| **라이드셰어** | Uber, Lyft | Uber, Cabify | **JapanTaxi**, Uber | **Kakao T** | **Didi (滴滴)** |
| **배달** | DoorDash, Uber Eats | Glovo, Deliveroo | **Demae-can (出前館)**, Uber Eats | **Coupang Eats**, Baemin (배달의민족) | **Meituan (美团)**, Ele.me (饿了么) |
| **클라우드** | AWS, Azure, GCP | AWS, Azure | AWS, Azure, **Sakura Cloud** | AWS, Naver Cloud, NHN Cloud | **Aliyun (阿里云)**, Tencent Cloud, Huawei Cloud |

### AI/ML 특정 어휘

| 단어 | EN | ES | JP | KR | CH |
|------|----|----|----|----|----|
| **챗봇** | Chatbot | Chatbot | チャットボット | 챗봇 (chaetbot) | 聊天机器人 (liáotiān jīqìrén) |
| **프롬프트** | Prompt | Prompt / Indicación | プロンプト | 프롬프트 (peurompteu) | 提示词 (tíshìcí) |
| **토큰** | Token | Token | トークン | 토큰 (token) | Token / 标记 (biāojì) |
| **모델** | Model | Modelo | モデル (moderu) | 모델 (model) | 模型 (móxíng) |
| **환각** | Hallucination | Alucinación | ハルシネーション (harushineeshon) | 환각 (hwangak) / 할루시네이션 (hallusineisyeon) | 幻觉 (huànjué) |
| **파인튜닝** | Fine-tune | Ajuste fino | ファインチューン | 파인튜닝 (paineutyuning) | 微调 (wēitiáo) |
| **RAG** | RAG | RAG | RAG | RAG | RAG / 检索增强生成 (jiǎnsuǒ zēngqiáng shēngchéng) |
| **임베딩** | Embedding | Embedding / Incrustación | 埋め込み (umekomi) | 임베딩 (imbeding) | 嵌入 (qiànrù) |
| **RLHF** | RLHF | RLHF | RLHF | RLHF | RLHF / 基于人类反馈的强化学习 |

---

## 학습자 의사결정 가이드

| 개념 | EN | ES | JP | KR | CH |
|---------|----|----|----|----|----|
| **인터넷** | Internet | Internet | インターネット | 인터넷 (inteonet) | 互联网 (hùliánwǎng) / 因特网 |
| **웹사이트** | Website | Sitio web | ウェブサイト | 웹사이트 | 网站 |
| **앱** | App | Aplicación | アプリ | 앱 | 应用 (yìngyòng) |
| **검색엔진** | Google | Google | Google, Yahoo | Naver | Baidu |
| **메신저** | Messenger, WhatsApp | WhatsApp | LINE | KakaoTalk | WeChat |
| **전화** | Smartphone | Smartphone / Móvil | スマホ | 스마트폰 | 手机 |
| **좋아요** | Like | Me gusta | いいね | 좋아요 | 赞 |
| **LOL** | lol | jajaja | 草 / www | ㅋㅋ | 2333 / 哈哈 |
| **스트리밍** | Stream | Streaming | 配信 | 스트리밍 | 流媒体 |
| **이커머스** | Amazon | Amazon | Amazon, Rakuten | Coupang | Taobao, JD |
| **모바일 페이** | Apple Pay, Venmo | Bizum | PayPay | Kakao Pay | 微信支付 / 支付宝 |
| **해시** | # | # | # | # | # |
| **멘션** | @ | @ | @ | @ | @ |

---

## 🇰🇷 한국어 학습자 노트 (Korean Learner Notes)

> 본 섹션은 한국어 학습자 대상의 추가 학습 가이드입니다.

### 한국어 화자가 다른 4개 언어 기술 어휘를 학습할 때 흔히 마주치는 함정

1. **모바일 결제 시스템의 한국어 학습자 적응**:
   - 한국: 카카오페이/삼성페이/네이버페이/토스 — **보편**.
   - 중국: 위챗페이/알리페이 — **보편**.
   - 일본: PayPay/LINE Pay/Suica — **NFC 우세**.
   - 미국/유럽: Apple Pay/Google Pay — **카드/현금 우세**, 모바일 부차.
   - **함정**: 한국어 학습자가 다른 4개 언어에 한국/중국 모바일 결제 보편성 기대 → 미국/유럽 식당/카페에서 QR 결제 미지원 → 현금/카드 필요.
   - **훈련법**: 모바일 결제 매트릭스 — 한국/중국 보편, 일본 NFC, 미국/유럽 카드/현금. **해외 여행 시 현금/카드 위주 준비**.

2. **메신저 시스템의 국가별 지배**:
   - 한국: 카카오톡 (95%+ 보편). 일본: LINE (90%+). 중국: WeChat (1.3B+). 미국/유럽: WhatsApp, Messenger.
   - **함정**: 한국어 학습자가 해외 친구에게 "카톡으로 연락해" 단순 매핑 → 일본 친구는 LINE, 중국 친구는 WeChat 사용.
   - **훈련법**: 메신저 매트릭스 — KR 카카오톡 / JP LINE / CH WeChat / US WhatsApp+Messenger. **국가별 메신저 매핑 필수**.

3. **검색 엔진의 Google 지배 vs 지역 엔진**:
   - 한국: Naver (~60%). 중국: Baidu (~75%, Google 차단). 일본: Google + Yahoo JP (~15%). 미국/유럽: Google (~90%+).
   - **함정**: 한국어 학습자가 영어 콘텐츠 검색 시 Google 사용 → 한국/중국에서 Google 미사용/차단.
   - **훈련법**: 검색 엔진 매트릭스 — KR Naver / CH Baidu / JP Google+Yahoo / EN Google. **현지 검색 시 Naver/Baidu 활용**.

4. **한자 한자어 기술 어휘 발음 차이**:
   - 같은 한자 기술 어휘가 한국어/일본어/중국어에서 발음 다름. 예: 電話: 한국 "전화" vs 일본 "でんわ (denwa)" vs 중국 "diànhuà".
   - **함정**: 한국어 한자음 "전화" / "컴퓨터" / "이메일" 다른 4개 언어 발음 추정 → 실패.
   - **훈련법**: 기술 한자 한자어 3개국 발음 매트릭스 — 電話/전화/diànhuà, 電脑/컴퓨터/diànnǎo, 邮件/이메일/yóujiàn. 한자 1글자 = 3개국 발음.

5. **이모지/심볼 문화 차이**:
   - 한국어: ㅋㅋㅋ = LOL, ㅎㅎ = ha-ha, ㅇㅋ = OK. 한글 자음 단독.
   - 일본어: www = LOL, 草 = lol, (笑) = old. 로마자/한자 혼합.
   - 중국어: 2333 = LOL (BBS 코드), 哈哈. 숫자 코드.
   - 영어: lol, lmao. 영어 약어.
   - 스페인어: jajaja, xd. 로마자/특수문자.
   - **함정**: 한국어 학습자가 다른 4개 언어 문자 약어 (2333, xd, www) 무지 → 채팅 문화 적응 어려움.
   - **훈련법**: 문자 약어 5개 언어 매트릭스 — KR 한글 자음, JP www+草, CH 2333, EN lol/lmao, ES jajaja/xd. **5개 메커니즘 비교**.

6. **K-드라마/한류의 글로벌 기술 영향**:
   - K-드라마 (한드), 케이팝 (K-Pop), 웹툰, 만화 — 한국 문화 글로벌 수출의 큰 부분.
   - **함정**: 한국어 학습자가 "케이팝 = K-Pop" 단순 매핑 → 다른 4개 언어에서 같은 약어 사용 (대부분).
   - **훈련법**: 한류 어휘 — K-드라마 (K-Drama) / 케이팝 (K-Pop) / 웹툰 (Webtoon) / 만화 (만화). **한류 차용어 매트릭스**.

### 학습 전략

1. **우선순위 1**: 모바일 결제 5개국 매트릭스 — KR 카카오페이/삼성페이/토스, CH 위챗페이/알리페이, JP PayPay/LINE Pay, US Apple Pay/Venmo, EU Bizum. **해외 여행 시 현지 결제 시스템 사전 학습**.
2. **우선순위 2**: 메신저 매트릭스 — KR 카카오톡 / JP LINE / CH WeChat / US WhatsApp+Messenger. **국가별 메신저 매핑 필수**.
3. **우선순위 3**: 검색 엔진 매트릭스 — KR Naver / CH Baidu / JP Google+Yahoo / EN Google. **현지 검색 엔진 활용**.
4. **우선순위 4**: 기술 한자 한자어 3개국 발음 매트릭스 — 電話/전화/diànhuà, 電脑/컴퓨터/diànnǎo, 邮件/이메일/yóujiàn.
5. **우선순위 5**: 문자 약어 5개 언어 매트릭스 — KR 한글 자음 (ㅋㅋ, ㅎㅎ, ㅇㅋ), JP www+草, CH 2333, EN lol/lmao, ES jajaja/xd. **5개 메커니즘 비교**.

### 관련 한국어 위키 페이지

- [[slang-colloquial]] — 디지털 슬랭
- [[dating-romance]] — 데이팅 앱
- [[shopping-money]] — 모바일 결제
- [[business-email]] — 이메일/Slack/Teams
- [[untranslatable-concepts]] — 관계/네트워킹

---

## 관련 페이지

- `[[slang-colloquial]]` — 디지털 슬랭 중첩
- `[[dating-romance]]` — 데이팅 앱
- `[[shopping-money]]` — 모바일 결제 시스템
- `[[business-email]]` — 이메일/Slack/Teams 관행
- `[[untranslatable-concepts]]` — *netatmo, nettle* 은유

## 출처

- StatCounter Global Stats (2024) — 검색 엔진 시장 점유율
- DataReportal — Digital 2024 국가 보고서
- Sensor Tower — 앱 순위
- `[[index]]`
- `[Spanish/vocabulary/basic-vocabulary]`, `[[index]]`
- `[Japanese/vocabulary/business-vocabulary]`, `[Japanese/sources/technology-and-internet]`
- `[[index]]`, `[Korean/sources/technology-and-internet]`
- `[[index]]`, `[Chinese/sources/pinyin-basics-zh]`

---

**원본 (영어)**: [[tech-internet]] | **관련 미러**: [[tech-internet.es|Spanish]] · [[tech-internet.ja|Japanese]] · [[tech-internet.zh|Chinese]] | **정책**: ADR-0006
