# 부정 — 다국어 비교 (한국어판)

> 원본: [[negation]] (English) | 작성일: 2026-08-20 | ADR-0006
> **5개 언어 부정 시스템 비교 — 구조, 형태, 부정의 일치**

---

## 빠른 참조 표

### 부정 구조 개요

| 기능 | English | Spanish | Japanese | Korean | Chinese |
|---------|---------|---------|----------|--------|---------|
| **문장 부정** | 조동사 + not | *no* + 동사 | 동사 접미 *-nai* / *-masen* | 동사 접미 *-ji anta* / *-ji anhseumnida* | *bù* (不) / *méi* (没) + 동사 |
| **구성소 부정** | *not* + 구성소 | *no* + 구성소 | *wa* + *nai* / *dewa nai* | *an(i)* + 동사 / *mot* + 동사 | *bù* + 형용사/동사; *wú* (无) + 명사 |
| **부정 일치 (neg concord)** | **No** (이중 부정 = 긍정) | **Yes** (이중 부정 = 부정) | **No** (단일 부정) | **No** (단일 부정) | **No** (단일 부정) |
| **부정 극성 항목 (NPI)** | any, ever, anymore | *nadie, nada, nunca* | *dare mo...nai, nani mo...nai* | *amudo...an(i), amugeotdo...an(i)* | *shéi dōu...bù, shénme dōu...bù* |

### 문장 부정 패턴

#### English
- **구조**: 조동사 + *not* (*n't*)
- **현재**: I **do not** / **don't** know. She **does not** / **doesn't** go.
- **과거**: I **did not** / **didn't** go.
- **미래**: I **will not** / **won't** go.
- **조동사**: I **cannot** / **can't** / **could not** / **couldn't** go.
- **Be**: I **am not** / **'m not** / **is not** / **isn't** / **are not** / **aren't** ready.
- **Have (조동사)**: I **have not** / **haven't** seen it.
- **Have (본동사, 영국)**: I **haven't** a car. (미국: I **don't have** a car.)

#### Spanish
- **구조**: *no* + 동사 (동사 앞)
- **현재**: *No sé.* / *No voy.*
- **과거**: *No supe.* / *No fui.* / *No he ido.* (완료)
- **미래**: *No iré.* / *No voy a ir.*
- **가정법 트리거**: *No creo que venga.* (가정법), *No es verdad que venga.*
- **이중 부정**: *No vi **nada**.* (나는 아무것도 보지 못했다.) *Nadie **no** vino.* → *Nadie vino.* (아무도 오지 않았다.)

#### Japanese
- **단형 부정**: 동사 어간 + *nai* (ない) — *tabenai* (食べない = 먹지 않는다)
- **정중 부정**: 동사 어간 + *masen* (ません) — *tabemasen* (食べません)
- **과거 부정**: *tabenakatta* (食べなかった) / *tabemasen deshita* (食べませんでした)
- **형용사**:
  - *i-형용사*: *takai* → *takakunai* (高くない) / *takaku arimasen*
  - *na-형용사/명사*: *kirei* → *kirei dewa nai* (綺麗ではない) / *kirei dewa arimasen*
- **존재**: *aru* → *nai* (ない) / *arimasen*; *iru* → *inai* (いない) / *imasen*
- **금지**: *taberu na* (食べるな) — 단형; *tabenaide kudasai* (食べないでください) — 정중 요청

#### Korean
- **단형 (평서)**: 동사 어간 + *ji anta* (지 않다) — *meokji anta* (먹지 않다)
- **장형 (정중)**: 동사 어간 + *ji anhseumnida* (지 않습니다) — *meokji anhseumnida*
- **과거**: *meokji anatda* (먹지 않았다) / *meokji anhasseumnida*
- **형용사**: 같은 패턴 — *yeppeuji anta* (예쁘지 않다)
- **존재**: *itda* (있다) → *eopda* (없다) — **별도 부정 동사!**
- **금지**: *meokji maseyo* (먹지 마세요) / *meokjima* (먹지 마)
- **불능 (능력)**: *mot* (못) + 동사 — *mot meokda* (못 먹다) — *an(i)*와 **구별**

#### Chinese
- **표준 부정**: *bù* (不) + 동사/형용사 — *bù chī* (不吃), *bù hǎo* (不好)
- **완료/경험 부정**: *méi* (没) / *méiyǒu* (没有) + 동사 — *méi chī* (没吃), *méiyǒu qù* (没有去)
- **미래/의지 부정**: *bù* — *bù qù* (不去 = 가지 않을 것이다)
- **명령 부정**: *bié* (别) + 동사 — *bié chī* (别吃 = 먹지 마라)
- **형용사**: *bù* — *bù dà* (不大), *bù cōngming* (不聪明)
- **존재**: *méiyǒu* (没有) — *méiyǒu qián* (没有钱 = 돈이 없다)

### 구성소 부정

#### English
- *Not* + NP: **Not** John but Mary came.
- *Not* + PP: I saw him **not** in Paris but in London.
- *Not* + Adv: He drove **not** carefully but recklessly.
- *No* + N: **No** student passed. (한정사)

#### Spanish
- *No* + 구성소: *No Juan, sino María vino.*
- *Ningún* + N (부정 한정사): *Ningún estudiante aprobó.*
- *Ni*... *ni* (neither...nor): *Ni Juan ni María vinieron.*

#### Japanese
- *Wa* + 부정: *Jon wa konakatta.* (존은, 오지 않았다 — 대조)
- *De wa nai* (서술격 부정): *Jon de wa nai.* (존이 아니다.)
- *Mo* in 부정: *Dare mo konakatta.* (아무도 오지 않았다.)

#### Korean
- *An(i)* / *mot* + 동사: *an(i) meokda* (안/못 먹다)
- *An(i)* = don't/won't; *mot* = can't
- *Ani* as 서술격 부정: *Jon-i aniya.* (존이 아니야 = 존이 아니다.)

#### Chinese
- *Bù* + VP/형용사: *bù shì* (不是 = 아니다), *bù xǐhuan* (不喜欢)
- *Méi* + V (완료): *méi qù* (没去)
- *Wú* (无) + N (격식/문어): *wú rén* (无人 = 아무도 없다), *wú fǎ* (无法 = 방법이 없다)

### 부정 극성 항목 (NPI) & 부정 일치

#### English (No Neg Concord)
- something → **anything** / nothing
- someone → **anyone** / nobody
- somewhere → **anywhere** / nowhere
- already → **any more** / **no longer**
- somewhat → **at all**
- *I didn't see **anything**.* (not *nothing*)
- *I **don't** have **any** money.* (not *no money* — although colloquial *I don't got no money* exists)

#### Spanish (Neg Concord Required)
- algo → **nada**
- alguien → **nadie**
- algún/alguno → **ningún/ninguno**
- también → **tampoco**
- siempre → **nunca / jamás**
- algo de → **nada de**
- *No vi **nada**.* (나는 아무것도 보지 못했다.)
- *Nadie **no** sabe.* → *Nadie sabe.* (아무도 모른다.)

#### Japanese (No Neg Concord — NPI needs negation)
- 何か → 何も...ない (nani mo...nai)
- 誰か → 誰も...ない (dare mo...nai)
- どこか → どこも...ない (doko mo...nai)
- いつも → 決して...ない (kesshite...nai) / 全然...ない (zenzen...nai)
- ちょっと → 全く...ない (mattaku...nai)
- *Nani mo tabenakatta.* (나는 아무것도 먹지 않았다.)
- *Dare mo inai.* (아무도 없다.)

#### Korean (No Neg Concord — NPI needs negation)
- 무언가/뭐 → 아무것도...안/못 (amugeotdo...an/mot)
- 누군가 → 아무도...안/못 (amudo...an/mot)
- 어딘가 → 아무데도...안/못 (amudeo...an/mot)
- 항상 → 결코...안/못 (gyeolko...an/mot) / 전적으로...안/못
- 조금 → 전혀...안/못 (jeonhyeo...an/mot) / 하나도...안/못 (hana do...an/mot)
- *Amugeotdo an meogeosseo.* (나는 아무것도 안 먹었어.)
- *Amudo an wasseo.* (아무도 안 왔어.)

#### Chinese (No Neg Concord — NPI needs negation)
- 什么 → 什么都不/没 (shénme dōu bù/méi)
- 谁 → 谁都不/没 (shéi dōu bù/méi)
- 哪里 → 哪里都不/没 (nǎlǐ dōu bù/méi)
- 总是 → 从不/没 (cóng bù/méi)
- 一点儿 → 根本不/没 (gēnběn bù/méi) / 一点儿都不/没
- *Wǒ shénme dōu méi chī.* (나는 아무것도 안 먹었다.)
- *Shéi yě méi lái.* (아무도 안 왔다.)

### 특수 부정 구조

| 구조 | English | Spanish | Japanese | Korean | Chinese |
|--------------|-------------|--------------|-------------|-------------|--------------|
| **부정 의문문** | Don't you like it? / Isn't she coming? | ¿No vienes? / ¿No te gusta? | Tabemasen ka? (食べませんか？= 안 먹을 거예요?) | An meogeoyo? (안 먹어요?) / Meokji anayo? | Bù chī ma? (不吃吗? = 안 먹을 거예요?) / Méi chī ma? (没吃吗?) |
| **태그 의문문** | You're coming, **aren't you**? / You're not coming, **are you**? | Vienes, **¿verdad?** / **¿no?** / **¿verdad que sí?** | Taberu deshou? (食べるでしょう？) / Tabenai deshou? | Meogeoyo, geureochji? (먹어요, 그렇죠?) | Nǐ qù, duì ba? (你去，对吧?) / Nǐ bù qù, shì ba? |
| **부정 명령문** | Don't go. / Let's not go. | No vayas. / No te vayas. (가정법) | Tabenaide kudasai. (食べないでください = 먹지 마세요) | Meokji maseyo. (먹지 마세요) | Bié chī! (别吃! = 먹지 마!) / Bù yào chī! (不要吃!) |
| **부정 부정사** | I told him **not to go**. | Le dije **que no fuera**. (가정법) / Le dije **no ir**. | - | - | - |
| **부정 부정형용사** | **Not knowing** what to do, I waited. | - | - | - | - |
| **Neither/Nor** | I don't like it. **Neither do I**. / **Neither** John **nor** Mary came. | Yo **tampoco** quiero ir. | Watashi mo...nai / Watashi mo dewa nai | Jeodo...an / Jeodo aniya | Wǒ yě bù / Wǒ yě méi |
| **Mo...nai** (not even) | - | - | Ichido mo ikanai. (一度も行かない = 한 번도 가지 않는다.) | - | Yī cì yě méi qù. (一次也没去 = 한 번도 가지 않았다.) |
| **Wa...nai** (대조) | - | - | Kore wa tabenai. (これは食べない = **이것은** 먹지 않을 거예요.) | - | - |
| **Lián... dōu bù/méi** (not even) | - | - | - | - | Lián tā dōu bù zhīdào. (连他都不知道 = 그도 모른다.) |
| **Wú** (无) 격식 | - | - | - | - | Wú fǎ (无法 = 방법이 없다), Wú rén (无人 = 아무도 없다) |

### 부정에서 정중함 / 체면 유지

| 언어 | 부드러운 부정 | 예 |
|----------|-------------------|---------|
| **English** | *I'm afraid not* / *I don't think so* / *Not really* | *Q: "Can you come?" A: "I'm afraid I can't."* |
| **Spanish** | *Creo que no* / *Me temo que no* / *No creo que pueda* | *¿Vienes? — Creo que no puedo.* |
| **Japanese** | *Chotto...* (암묵적 거절) / *Kangaete okimasu* (생각해 볼게요) | *Ashita kimasu ka? — Chotto... / Kangaete okimasu.* |
| **Korean** | *Geureoke hagi jom...* (그렇게 하긴 좀...) / *Jom...* | *Naeil wayo? — Geureoke hagi jom...* |
| **Chinese** | *Bù tài hǎo shuō* (不太好说) / *Kěngpà bù xíng* (恐怕不行) | *Nǐ néng lái ma? — Kěngpà bù xíng.* |

---

## 핵심 대조 (종합)

| 대조 | 통찰 |
|----------|---------|
| **이중 부정** | 스페인어만 이중 부정 = 부정 (no vi nada). 나머지 4개 언어는 이중 부정 = 긍정 |
| **부정 위치** | 영어 (조동사 + not), 스페인어 (no + 동사), 일본어/한국어 (동사 접미), 중국어 (bù/méi + 동사/형용사) |
| **존재 부정** | 한국어 별도 동사 eopda (없다), 영어/스페인어/일본어/중국어는 일반 부정 동사 사용 |
| **불능 vs 부정의무** | 한국어 mot (못) vs an (안) 명확히 구분; 다른 4개 언어는 단일 형태 (can't) |
| **부정 부사** | 중국어 가장 명시적 (bù/méi/bié 세 가지); 영어 (not); 다른 언어는 동사 형태 변화 |

---

## 학습자 의사결정 가이드

| 필요한 표현 | EN | ES | JP | KR | CH |
|----------------|----|----|-----|----|----|
| **"No"** | No | No | Iie (いいえ) / Chigau (ちがう) | Aniyo (아니요) / Ani (아니) | Bù (不) / Bú (不) |
| **"Not"** | not | no | -nai / -masen / dewa nai | -ji anta / -ji anhseumnida | bù / méi |
| **"Don't (imperative)"** | Don't go | No vayas | Tabenaide kudasai / Taberu na | Meokji maseyo / Meokjima | Bié qù / Bú yào qù |
| **"Didn't"** | didn't go | no fui | ikanakatta / ikimasen deshita | an gasseoyo / an gasseumnida | méi qù / bù qù (context) |
| **"Won't"** | won't go | no iré | ikanai / ikimasen | an gal geoyeyo / an gajyo | bù qù |
| **"Can't"** | can't eat | no puedo comer | taberarenai / taberaremasen | meokji motaeyo / mot meogeoyo | chī bù liǎo / bù néng chī |
| **"Nothing"** | nothing | nada | nani mo...nai | amugeotdo...an/mot | shénme dōu méi |
| **"Nobody"** | nobody | nadie | dare mo...nai | amudo...an/mot | shéi dōu méi |
| **"Nowhere"** | nowhere | en ningún lado | doko mo...nai | amudeo...an/mot | nǎlǐ dōu méi |
| **"Never"** | never | nunca / jamás | kesshite...nai / zettai ni...nai | gyeolko...an/mot / jeoldae...an/mot | cóng bù / wànwàn bù |
| **"Neither/Not either"** | neither do I | yo tampoco | watashi mo...nai / watashi mo dewa nai | jeodo...an / jeodo aniya | wǒ yě bù / wǒ yě méi |
| **"Not at all"** | not at all | en absoluto | zenzen...nai / mattaku...nai | jeonhyeo...an/mot / hana do...an/mot | gēnběn...bù/méi / yīdiǎn...bù/méi |

---

## 🇰🇷 한국어 학습자 노트 (Korean Learner Notes)

> 본 섹션은 한국어 학습자 대상의 추가 학습 가이드입니다.

### 한국어 화자가 다른 4개 언어 부정 시스템을 학습할 때 흔히 마주치는 함정

1. **한국어 mot (못) vs an (안) 의 명확한 구분**:
   - 한국어는 능력(못) vs 의지(안) 부정을 명시적으로 구분. 예: "못 먹다" (can't eat) vs "안 먹다" (don't eat).
   - 영어/스페인어/중국어는 단일 부정 (can't, no puedo, 不能), 일본어도 단일 (-nai).
   - **함정**: 한국어 학습자가 영어/스페인어 단일 can't/no puedo에 "mot vs an" 구분을 무시 → 영어 "I can't eat" = 한국어 "못 먹어"만, "I don't eat" = "안 먹어"는 별도 표현. 그러나 영어/스페인어는 단일.
   - **훈련법**: 한국어 "mot vs an" **5개 언어 매트릭스** — 한국어 mot/an → 영어 can't/don't, 스페인어 no puedo/no, 일본어 -nai/-nai (동일), 중국어 不能/不. **5개 언어 모두 mot/an 구별이 있는 것은 한국어만**.

2. **존재 부정 한국어 고유 동사 (eopda, 없다)**:
   - 한국어는 별도 존재 부정 동사 "없다 (eopda)" 사용. 다른 언어는 일반 부정 ("not have" / "no hay" / ない / 没有).
   - **함정**: "돈 없다"를 영어 "money doesn't exist" 식 직역 → "money is not exist" (어색). 영어 "I don't have money" 사용.
   - **훈련법**: 한국어 "있다/없다" / 영어 "have/don't have" / 스페인어 "hay/no hay" / 일본어 "ある/ない" / 중국어 "有/没有" 5개 언어 매트릭스. **존재/소유의 5개 언어별 매핑** 학습.

3. **부정 위치의 한국어 동사 접미 vs 영어 조동사**:
   - 한국어: 동사 + 부정 접미 (먹다 → 먹지 않다). 동사 끝에 부정.
   - 영어: 조동사 + not (do not, does not, did not). 동사 앞/도움동사 위치.
   - 스페인어: no + 동사 (no como). 동사 앞.
   - **함정**: 한국어 학습자가 영어 "I don't know"를 "나는 모른다" (한국어 동사 끝 부정) 패턴으로 학습 → "I know not" 어색.
   - **훈련법**: 한국어 동사 끝 부정 vs 영어 조동사 부정 vs 스페인어 동사 앞 부정 — 3개 메커니즘 명시적 구분.

4. **부정 일치 (neg concord) 의 스페인어 특수성**:
   - 스페인어는 이중 부정 = 부정 ("No vi nada" = I didn't see anything). 영어는 이중 부정 = 긍정.
   - **함정**: 한국어 학습자가 스페인어 이중 부정을 영어처럼 사용 → "No vi no nada" (X) vs "No vi nada" (O). **영어식 이중 부정은 스페인어에서 오류**.
   - **훈련법**: 스페인어 neg concord 명시적 학습 — *No* + 부정 단어 (nada/nadie/ninguno) 필수. 한국어/영어/중국어는 단일 부정만.

5. **부정 부사 (NPI) 의 한국어-일본어 유사성**:
   - 한국어 "아무도/아무것도...안" + 일본어 "誰も/何も...ない" 구조 동일. NPI (negative polarity item) 사용.
   - 영어는 "any-/anybody/anything" 사용. 중국어는 "都...不/没" 사용.
   - **함정**: 한국어 학습자가 영어 "any-" 사용 시 한국어 NPI 패턴 무시 → "I saw nobody" 식 직역 (X) vs "I didn't see anybody" (O).
   - **훈련법**: NPI 5개 언어 매트릭스 — 한국어 아무도...안 / 일본어 誰も...ない / 영어 not...anybody / 스페인어 no...nadie / 중국어 都...没.

### 학습 전략

1. **우선순위 1**: 한국어 mot (못) vs an (안) 구분 매트릭스 — 5개 언어 능력/의지 부정 매핑. mot=능력, an=의지. 영어/스페인어/중국어/일본어는 단일 부정이지만 한국어는 구분. **한국어 고유 메커니즘 학습**.
2. **우선순위 2**: 존재/소유 부정 5개 언어 매트릭스 — 한국어 있다/없다 vs 영어 have/don't have vs 스페인어 hay/no hay vs 일본어 ある/ない vs 중국어 有/没有. 한국어 별도 동사 (eopda) 학습.
3. **우선순위 3**: 부정 위치 3가지 메트릭스 — 한국어/일본어 (동사 접미) vs 영어 (조동사 + not) vs 스페인어/중국어 (부정 부사 + 동사). 메커니즘별 문장 구조 학습.
4. **우선순위 4**: NPI 5개 언어 매트릭스 — 한국어 아무도/아무것도 vs 일본어 誰も/何も vs 영어 any-/anybody vs 스페인어 nadie/nada (neg concord) vs 중국어 都...不/没. **부정 일치 (neg concord) 스페인어 특수성 명시 학습**.
5. **우선순위 5**: 부드러운 부정 (soft negation) 5개 언어 — 영어 "I'm afraid not" vs 스페인어 "Creo que no" vs 일본어 "Chotto..." vs 한국어 "그렇게 하긴 좀..." vs 중국어 "Bù tài hǎo shuō". **정중한 거절 표현** 매트릭스.

### 관련 한국어 위키 페이지

- [[politeness-honorifics]] — 부정의 정중함
- [[business-email]] — 이메일 부정 응답
- [[pronouns-reference]] — 부정 대명사 (nobody, nothing)
- [[greetings]] — 초대 부정 응답
- [[shopping-money]] — "no discount, not for sale"

---

## 관련 페이지

- `[[politeness-honorifics]]` — 부정 정중함 전략
- `[[business-email]]` — 이메일 부정 응답
- `[[pronouns-reference]]` — 부정 대명사
- `[[greetings]]` — 초대 부정 응답
- `[[shopping-money]]` — "no discount, not for sale"

## 출처

- English: `[English/vocabulary/basic-vocabulary]`
- Spanish: `[Spanish/vocabulary/basic-vocabulary]`, `[Spanish/culture/espana-vs-latinoamerica-registro]`
- Japanese: `[[index]]`, `[Japanese/vocabulary/jp-counters]`
- Korean: `[[index]]`, `[Korean/vocabulary/topik1-starter]`
- Chinese: `[Chinese/vocabulary/body-zh]`, `[Chinese/sources/pinyin-basics-zh]`

---

**원본 (영어)**: [[negation]] | **관련 미러**: [[negation.es|Spanish]] · [[negation.ja|Japanese]] · [[negation.zh|Chinese]] | **정책**: ADR-0006
