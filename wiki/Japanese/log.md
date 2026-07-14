# Japanese Learning - Activity Log

## [2026-06-23] ingest | emotion-nature-animals-clothing | New vocabulary topics for typing game

- Added emotion corpus: 59 entries (嬉しい, 悲しい, 怒った, etc.)
- Added nature corpus: 60 entries (太陽, 月, 星, etc.)
- Added animals corpus: 59 entries (犬, 猫, ライオン, etc.)
- Added clothing corpus: 42 entries (シャツ, ズボン, ドレス, etc.)
- Added Tier 2-5 stages for each topic in typing_language
- Updated index.md with all new topic sections + hiragana annotations
- Total corpus expansion: 222 entries → 384 entries

### Raw Sources Added
- `raw/Japanese/food-vocabulary-jp.md` (30+ entries)
- `raw/Japanese/business-vocabulary-jp.md` (43 entries)
- `raw/Japanese/emotions-personality-vocabulary-jp.md` (43 entries)
- `raw/Japanese/nature-vocabulary-jp.md` (40 entries)
- `raw/Japanese/animals-vocabulary-jp.md` (37 entries)
- `raw/Japanese/clothing-vocabulary-jp.md` (30 entries)

### Wiki Vocabulary Pages Created
- Food: 肉, 野菜, 果物, 魚, 鶏肉, 牛肉, 豚肉, 卵, 牛乳, チーズ, 塩, 砂糖, 油, ご飯, 麺, コーヒー, お茶, ジュース, ビール, ワイン, 寿司, ラーメン, そば, うどん, 天ぷら, とんかつ, カレー, 和牛, 美味しい, 辛い, 甘い, 酸っぱい, 苦い, メニュー, 注文, 勘定, 空腹, 満腹, 朝食, 昼食, 夕食, 弁当, 持帰り (40+ pages)
- Business: メール, 住所, 送信者, 受信者, 件名, 添付, 送る, 受け取る, 返信, 保存, 削除, 会議, スケジュール, 議題, 発表, 意見, 決定, 合意, 記録, 場所, 延期, 会社, 事務所, 同僚, 上司, 部下, 社員, 代表, チームリーダー, プロジェクト, 仕事, 契約, 報告, 提出, 確認, 承認, 電話, メッセージ, 電話番号, 接続, 検討, 協力 (43 pages)
- Emotions: 嬉しい, 悲しい, 怒った, 怖い, 驚いた, 嫌, 後悔, 不安, 恥ずかしい, 感動, 寂しい, 優しい, 可愛い, 立派, 親切, 温かい, 勤勉, 明るい, 元気, 沉着, 悪い, 怠け者, 無礼, 欲張り, 嫉妬, 幸せだ, 会いたい, ごめんなさい, 機嫌が悪い, 羨ましい, 感謝する, 普通だ, ときめく, 緊張する, 快適だ, 心配する (37 pages)
- Nature: 太陽, 山, 月, 星, 空, 雲, 雨, 雪, 風, 嵐, 雷, 虹, 川, 海, 湖, 森, 砂漠, 島, 丘, 谷, 花, 木, 草, 葉, 庭, 咲く, 落ちる, 成長する, 凍る, 溶ける, 輝く, 暗い, 暑い, 寒い (35 pages)
- Animals: 犬, 猫, 鳥, 魚, 馬, 牛, 豚, 鶏, 羊, ライオン, トラ, ゾウ, サル, 熊, オオカミ, キツネ, 鹿, 蛇, 亀, カエル, 蝶, 蜂, アリ, クジラ, イルカ, サメ, 走る, 飛ぶ, 泳ぐ, 狩る, 野生, 大きい, 小さい, 速い, 遅い (35 pages)
- Clothing: シャツ, ズボン, 靴, 帽子, コート, スカート, 靴下, 手袋, マフラー, 赤いドレス, 青いシャツ, 白いズボン, 黒い靴, 綿, 絹, 羊毛, 着る, 脱ぐ, 洗う, 新しい, 古い, 高い, 安い, きつい, 緩い, 長袖, 半袖 (27 pages)

## [2026-06-18] ingest | first-travel-korea | Japanese traveler's perspective on Korea

## [2026-06-12] init | Wiki initialized

- Created directory structure
- Set up index.md
- Ready for first source ingest

## [2026-07-10] lint | Language 위키 일괄 점검 + 8 액션 + Game 측 contract sync

8개 액션 완료 (자세한 기록은 `Language/SESSION_SUMMARY_2026-07-10.md` 참조):

- Action 1: 모든 vocabulary 페이지 (25 파일 / 654 entry) 에 `Pipeline Form` YAML 부록 추가
- Action 2: Korean vocabulary 3 페이지 신규 인제스트
- Action 3: study-plan/ 표준 적용 (EN/JP/KR stub README)
- Action 4 (1차): 안전 범위 65건 wikilink strip
- Action 4 (후속): Wiki Page 컬럼 654행 drop + 범위 한정 strip 733건 + パスポート→pasupooto 86건 매핑
- Action 5: jp-travel-vocab/ 카탈로그 (orphan 86 → 0)
- Action 6: .gitignore + .env / __pycache__ 추적 해제 (**🚨 Notion 토큰 평문 노출 — 사용자 무시 결정**)
- Action 7: pipeline-to-game.md ↔ corpus-pipeline.md 양방향 검증
- Action 8: Wiki Page col drop 후속 + corruption 35건 수정
- Action 9: jp-travel-vocab/ 88 per-word → 2 theme 통합 + 스키마 갱신
- Action 10: expressions/ 59 per-expression → 9 theme 통합 + 스키마 갱신
- Action 11: Game 측 contract docs (corpus-pipeline.md, AGENTS.md, languages/korean.md) cross-project 정합

**원칙 정착**: "단어나 문장 하나를 .md 로 만들지 않는다" — vocabulary/expressions 모두 theme-file 컨벤션.

**최종**: broken wikilink 1302 → 86 (touch 가능 범위 0, 모두 immutable).

## [2026-07-14] sync | index.md 갱신 — 7/13 batch 누락분 반영

- **Trigger**: 본 세션 Language 상태 점검에서 발견 — EN/JP/KR index.md 가 "Last updated: 2026-07-08" 그대로 stale. 7/13 batch 의 vocab theme 신규분이 index 에 미반영.
- **Action**: index.md 전면 갱신 (각 언어 vocab/expressions/culture/sources 카운트 + 신규 theme link + 마지막 갱신일)
- **변경**:
  - EN: Last updated → 2026-07-14, sources 15개 명시 + first-travel-japan source 추가, Pipeline Notes 섹션
  - JP: Last updated → 2026-07-14, vocab 7 → 9 (+ jp-counters + kanji-n5), sources 15개 + 2026-07-13_Kanji_N5_100
  - KR: Last updated → 2026-07-14, vocab 7 → 8 (+ topik1-starter), 의류・패션 어휘 23 entries 명시, raw OCR cleanup 노트
- **wikilink 검증**: 모든 [[wikilink]] 가 실제 파일 가리킴 확인 (placeholder 제외)

## [2026-07-14] session-end | 본 세션 종합 summary 참조

- **세션 종합**: [[SESSION_SUMMARY_2026-07-14]] (전체 15 액션 + 보안 scrub + force-push 요약)
- **보안 가이드**: [[security-incident-response-2026-07-14]] (_publish/2026-W25/, 360 lines)
- **상태**: Language HEAD `8aae316` (force-pushed) / Game HEAD `7d78707` (curation push)
- **세션 종료**: 본 엔트리까지
