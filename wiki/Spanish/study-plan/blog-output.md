# Salida a Blog y Homepage - 블로그/홈페이지 출력 가이드

**대상 플랫폼:** Tistory, Notion, WordPress (한국형 블로그)
**소스:** `wiki/Spanish/study-plan/weekly-plan.md` 및 위키 전반
**최종 갱신:** 2026-06-16

---

## 핵심 원칙

위키(원본)는 **single source of truth**로 두고, 블로그는 **읽기 전용 사본**으로 운영한다.
- 위키만 수정 → 블로그는 발행 시점에만 동기화
- 모든 발행물은 위키 링크로 다시 연결 → 위키가 본거지

이렇게 하면:
- 위키의 LLM 워크플로우(링크 자동화, 백링크, 그래프 뷰)를 깨지 않음
- 블로그는 SEO와 구독자에 최적화된 형태로 가공
- 두 곳에 중복 입력하는 비용이 없음

---

## 플랫폼별 출력 방법

### 1. Tistory (티스토리)

**방법 A · 수동 발행 (가장 단순)**
1. 위키 markdown 파일을 Obsidian/VS Code에서 연다
2. 전체 복사 → Tistory 에디터에 붙여넣기
3. 코드블록·표는 Tistory 마크다운 모드에서 직접 확인
4. 카테고리/태그 지정 후 발행

**방법 B · Pandoc 변환 후 부분 자동화**
```bash
# 위키 → HTML 변환
pandoc wiki/Spanish/study-plan/weekly-plan.md \
  -f markdown -t html \
  --standalone --metadata title="Semana 1" \
  -o _publish/semana-1.html
```
- 변환된 HTML을 Tistory에 붙여넣기 (서식 깨짐 최소)
- Tistory API는 비공식이라 cron 자동화는 권장하지 않음

**방법 C · 깃허브 페이지 미들웨어 (권장)**
1. 위키를 GitHub Pages(Jekyll/Hugo)로 빌드해 1차 발행
2. Tistory에는 GitHub Pages URL을 "원본 링크" 박스로만 노출
3. 실제 콘텐츠는 GitHub Pages에서, 트래픽/구독은 Tistory에서 흡수

**장점:** 무료, 한국 검색 친화, 애드센스 가능
**단점:** 자동화 도구 부족, 모바일 에디터 일부 마크다운 미지원

---

### 2. Notion (노션)

**방법 A · Markdown Import (가장 단순)**
1. Notion 페이지 → `...` 메뉴 → `Import` → `Markdown & CSV`
2. `wiki/Spanish/study-plan/weekly-plan.md` 또는 변환된 HTML 업로드
3. 노션이 자동으로 페이지 구조로 변환 (제목, 리스트, 코드블록 모두 인식)

**방법 B · Notion API 자동 발행 (반자동)**
이 프로젝트에 포함된 스크립트: `_publish/scripts/publish_to_notion.py`

1. **Integration 생성**: https://www.notion.so/my-integrations → "New integration" → Internal Integration → 토큰 복사
2. **대상 페이지에 권한 부여**: Notion 페이지 → `...` → `Connections` → 만든 Integration 추가
3. **Parent page ID 확보**: 페이지 URL `notion.so/<workspace>/<PAGE_TITLE>-<32-hex-id>` 의 32자리 hex
4. **.env 설정**:
   ```bash
   cd _publish/scripts
   cp .env.example .env
   # .env 열어서 NOTION_TOKEN, NOTION_PARENT_PAGE_ID 채우기
   ```
5. **실행**:
   ```bash
   python3 -m venv .venv
   .venv/bin/pip install notion-client python-frontmatter rich
   .venv/bin/python3 publish_to_notion.py ../2026-W25/semana-1-arranque.md --dry-run  # 검증
   .venv/bin/python3 publish_to_notion.py ../2026-W25/semana-1-arranque.md          # 발행
   ```

스크립트 지원 블록: 제목(h1-h3), 단락, 인용(`>`), 글머리표, 구분선(`---`), 표(`|`), 콜아웃(`> [!TIP]`), **bold** / *italic* / `code` / [link](url).

**방법 C · Notion → 공개 페이지 → 외부 embed**
- Notion에서 `Share to web` 활성화
- 노션 페이지 자체를 홈페이지/포트폴리오에 iframe으로 삽입
- 위키는 로컬에서만 작업, Notion은 출력 캐시 역할

**장점:** 마크다운 호환 우수, 모바일/협업 친화, 데이터베이스화 가능
**단단점:** 외부 SEO 약함, 무료 플랜 페이지 수 제한, 한국 검색에는 불리

---

### 3. WordPress (워드프레스)

**방법 A · Jetpack Markdown 플러그인 (가장 단순)**
1. WordPress.com 또는 자체 호스팅 + Jetpack 설치
2. 새 글 작성 화면을 `Markdown` 모드로 전환
3. 위키 markdown 붙여넣기 → 발행

**방법 B · WP REST API + 자동화 (고급)**
```bash
# 예시: curl로 draft 포스트 생성
curl -X POST "https://example.com/wp-json/wp/v2/posts" \
  -u "user:app_password" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Semana 1 - Subjuntivo",
    "content": "'"$(cat semana-1.html)"'",
    "status": "draft",
    "categories": [101],
    "tags": [10, 11]
  }'
```
- GitHub Actions로 주 1회 cron 발행 가능
- `gh workflow run publish-spanish.yml`

**방법 C · Jekyll/Hugo → WordPress 마이그레이션**
- 위키를 Jekyll로 빌드 → 정적 사이트의 글을 WP XML로 변환 → 일괄 임포트
- 주기적으로 새 글만 동기화하려면 별도 스크립트 필요

**장점:** SEO 최강, 플러그인 생태계, 자체 호스팅 시 통제권
**단점:** 셋업 비용, 보안/유지보수, 한국형 UI는 Tistory가 더 편함

---

## 통합 권장 아키텍처

세 플랫폼 모두를 운영한다면 아래 3-tier 구조를 추천한다.

```
┌─────────────────────────────────────────────────┐
│ Tier 1 · 원본 (Wiki)                            │
│  ~/Language/wiki/Spanish/                       │
│  - LLM이 자동 유지                               │
│  - 링크·백링크·그래프의 진실 공급원              │
└──────────────────┬──────────────────────────────┘
                   │ ① 발행 시점 export (수동/스크립트)
                   ▼
┌─────────────────────────────────────────────────┐
│ Tier 2 · 발행 캐시 (Markdown/HTML)              │
│  ~/Language/_publish/{YYYY-WW}/post.md         │
│  - 위키 일부를 가공 (Front-matter, 태그, 요약)   │
│  - SEO/카테고리 메타 추가                        │
└──────────────────┬──────────────────────────────┘
                   │ ② 플랫폼별 변환
        ┌──────────┼──────────┐
        ▼          ▼          ▼
   ┌────────┐ ┌────────┐ ┌─────────┐
   │Tistory │ │ Notion │ │WP/Hexo  │
   │ (한국SEO)│ │(협업)  │ │(기술블로그)│
   └────────┘ └────────┘ └─────────┘
                   │ ③ 모든 글에 원본 위키 링크 포함
                   ▼
            "원본·갱신 이력 보기 → wiki/Spanish/..."
```

**홈페이지(개인 사이트)에는:**
- Hexo/Hugo로 GitHub Pages에 통합 발행 (마크다운 100% 호환)
- 위키의 `study-plan/`, `sources/`를 카테고리화
- Tistory/Notion은 외부 채널로 링크만 노출

---

## 주간 발행 워크플로우

```
[일요일 15분]
  1. 위키에 그 주 학습 내용 기록 (LLM과 함께)
  2. [[weekly-plan#blog-template]] 형식으로 _publish/ 폴더에 사본 작성
  3. Tistory: 사본 markdown → HTML 변환 → 붙여넣기 → 발행
  4. Notion: markdown 파일 import → 페이지 발행
  5. WordPress: Jetpack markdown 모드 → 발행
  6. log.md에 발행 기록 추가
     ## [YYYY-MM-DD] publish | semana N → tistory/notion/wordpress
```

발행 후 위키의 `sources/` 페이지에 블로그 URL을 `## Enlaces externos` 섹션으로 추가.

---

## 자동화 도구 후보

- **markdown-to-notion**: GitHub 오픈소스, 노션 API 래퍼
- **pandoc**: 마크다운 → HTML/DOCX/PDF 만능 변환기
- **Hugo + GitHub Actions**: 위키 일부를 정적 사이트로 자동 빌드
- **Obsidian Publish**: 유료지만 마크다운 노트를 그대로 웹 게시 (1-tier만 쓸 때)

자동화는 **월 발행 4건 이상 + 꾸준한 운영 3개월 이후**에 도입을 권장. 그 전엔 수동 발행이 안정적이다.

---

## 체크리스트 (플랫폼 선택용)

- 한국 독자 위주, 수익화(애드센스) → **Tistory**
- 협업/모바일 중심, 학습 일지 형태 → **Notion**
- 기술 블로그 통합, SEO 최우선 → **WordPress (Hexo 백업)**
- 위키를 그대로 외부 공개 → **Obsidian Publish 또는 GitHub Pages**

혼합 운영 시 Tier 구조를 따라 원본-사본-플랫폼 분리를 유지할 것.

---

## Fuentes

- [[weekly-plan]] - 학습 계획 본체
- [[../index]] - 스페인어 위키 인덱스
