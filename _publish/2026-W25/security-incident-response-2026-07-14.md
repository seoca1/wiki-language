---
title: "보안 사고 대응 가이드 — Language vault 2026-07-14"
date: 2026-07-14
type: security-guide
audience: vault-owner
urgency: high
estimated-effort: 30-45 min
---

# 보안 사고 대응 가이드 — Language vault 2026-07-14

> **긴급도: 높음**. 본 가이드는 2026-07-14 Language 프로젝트 상태 점검 세션에서 발견된
> 보안 이슈를 해결하기 위한 단계별 매뉴얼이다. 3개의 즉시 조치와 2개의 후속 조치로
> 구성되어 있다.

## 컨텍스트 (왜 이 작업이 필요한가)

본 세션에서 다음 두 가지 보안 노출이 확인되었다:

1. **Notion API 토큰 평문 노출** — `_publish/scripts/.env` 가 git history 에
   트래킹되어 있었음 (initial commit 부터). Action 6 (7/10) 에서 `.gitignore` 는
   추가되었으나 실제 untrack 은 실패했고, 토큰은 history 에 그대로 남아 있었다.
   **긴급도: 높음** (이미 한 번 노출된 토큰은 본질적으로 compromised).

2. **GitHub Personal Access Token 노출** — `git filter-repo` 실행 시 NOTICE 메시지에
   remote URL (`https://[REDACTED-PAT:github_pat_11A6…ZjZmT]@github.com/...`) 가
   평문으로 출력되었다. **긴급도: 최고** (실시간 노출).

**완화 완료**: 세션 내에서 `git filter-repo` 로 18 commit 재작성, `.env` / `.pyc`
모든 history 제거, 디스크에서도 삭제. 그러나 **토큰 자체는 회전하지 않았음** —
본 가이드로 회전 진행.

---

## 즉시 조치 1: Notion 토큰 회전

> **소요 시간**: 5분
> **선행 조건**: 없음
> **영향**: vault 의 `_publish/` Notion 발행 기능

### 단계

#### 1.1 새 Notion integration 생성

1. https://www.notion.so/profile/integrations 접속
2. **"내 integrations"** 탭 → **"+ 새 integration"** 클릭
3. 설정:
   - **Name**: `language-vault-publisher` (또는 식별 가능한 이름)
   - **Associated workspace**: 본 vault 가 사용하는 workspace 선택
   - **Type**: Internal Integration
   - **Capabilities**: Read content, Update content, Insert content (기본값)
4. **"Submit"** 클릭

#### 1.2 토큰 복사

- 생성된 integration 의 **"Secrets"** 탭에서 **"Internal Integration Secret"** 복사
- 형식: `secret_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx` (50자)
- ⚠️ **이 화면을 닫으면 다시 볼 수 없음** — 안전한 곳에 임시 저장 (메모장 OK, git 절대 X)

#### 1.3 기존 integration 비활성화 (선택이지만 권장)

- 기존 토큰이 노출된 integration 의 **"Settings"** → **"Delete integration"**
- 또는 "Access" 탭에서 해당 workspace 연결 해제

### 검증

- 복사한 토큰이 `secret_` 로 시작하는지 확인
- 길이 50자 확인

---

## 즉시 조치 2: GitHub PAT 회전

> **소요 시간**: 5분
> **선행 조건**: 없음
> **영향**: 2개 repo 의 push 권한 (wiki-language + typing-language)

### 단계

#### 2.1 기존 PAT 폐기

1. https://github.com/settings/tokens 접속
2. **"Personal access tokens"** → **"Fine-grained tokens"** 또는 **"Tokens (classic)"** 탭
3. 노출된 PAT 식별:
   - 노출된 PAT: `[REDACTED-PAT:github_pat_11A6…ZjZmT]`
   - 이름 또는 메모에서 식별
4. **"Delete"** 클릭 → 확인
5. ⚠️ **이 PAT 으로 진행 중인 push 작업이 있다면 모두 중단됨**

#### 2.2 새 PAT 생성

1. 같은 페이지에서 **"Generate new token"** 클릭
2. 설정 (Fine-grained 권장):
   - **Name**: `vault-publish-2026-07` (회전 일자 명시)
   - **Expiration**: 90 days (또는 정책에 맞게)
   - **Repository access**: Only select repositories
     - `seoca1/wiki-language` ✓
     - `seoca1/typing-language` ✓
   - **Permissions**:
     - Contents: Read and write (push 위해)
     - Metadata: Read-only (자동 부여)
     - Pull requests: Read and write (필요 시)
3. **"Generate token"** 클릭
4. ⚠️ **생성 직후 한 번만 표시되는 토큰 복사** — 안전한 곳에 임시 저장

### 검증

- 새 PAT 가 `github_pat_11A` 또는 `ghp_` 로 시작하는지 확인
- 길이 80자 이상 확인

---

## 후속 조치 3: Force-push (양 repo)

> **소요 시간**: 10분
> **선행 조건**: 조치 1, 2 완료 (새 토큰 확보)
> **영향**: 양 repo 의 원격 history 가 18 commit 재작성된 상태로 교체

### 왜 force-push 가 필요한가

`git filter-repo` 로 local history 가 재작성되었으나, **원격 repo 는 여전히 이전
history 를 보유**. local 에서 작업한 27개 commit (security scrub 포함) 이 원격에
없다. Force-push 로 원격을 local 상태와 일치시킨다.

### ⚠️ Force-push 위험

- **다른 collaborator 가 clone 한 상태라면 그들의 history 와 불일치** (본 vault 는
  1인 작업이므로 해당 없음)
- **CI/CD 가 있다면 token rotation 후 깨질 수 있음** (해당 없음)
- **되돌리기 어려움** — force-push 로 덮어쓴 history 는 복구 어려움
- 백업: 로컬 `.git` 디렉토리는 그대로 (재 푸시 가능)

### 단계

#### 3.1 Language repo force-push

```bash
cd /Users/emilio/projects/Projects/Language

# 1. 새 PAT 로 remote URL 갱신
git remote set-url origin https://<NEW_PAT>@github.com/seoca1/wiki-language.git

# 2. Backup 확인 (안전망)
ls -d /tmp/Language-git-backup-*

# 3. Force-push (--force-with-lease 가 --force 보다 안전)
git push --force-with-lease origin main
```

#### 3.2 Game repo curation push

```bash
cd /Users/emilio/projects/Projects/Game/typing_language

# 1. 새 PAT 로 remote URL 갱신
git remote set-url origin https://<NEW_PAT>@github.com/seoca1/typing-language.git

# 2. Game curation commit push
git push origin main
```

#### 3.3 Remote URL 에서 PAT 제거

force-push 성공 후 **즉시** remote URL 에서 PAT 제거:

```bash
# Language
cd /Users/emilio/projects/Projects/Language
git remote set-url origin https://github.com/seoca1/wiki-language.git

# Game
cd /Users/emilio/projects/Projects/Game/typing_language
git remote set-url origin https://github.com/seoca1/typing-language.git

# 검증
git remote -v  # 둘 다 https://github.com/... 형태여야 함 (token 없음)
```

### 검증

- GitHub 웹에서 `seoca1/wiki-language` → commits 탭 → 최신 commit 이
  `c6e1c2c docs(Language/Spanish): log entry — basic-vocabulary theme...` 인지 확인
- GitHub 웹에서 `seoca1/typing-language` → 최신 commit 이
  `7d78707 curate(Game/typing_language): raw/ EN+ES basic-vocab...` 인지 확인

---

## 후속 조치 4: Notion publish 인프라 재설정

> **소요 시간**: 10분
> **선행 조건**: 조치 1 완료 (새 Notion 토큰 확보)
> **영향**: Notion 발행 워크플로 복구

### 단계

#### 4.1 Parent page ID 확보

1. Notion 에서 발행할 parent page 열기 (예: "Language Vault" 또는 "Security Log")
2. URL 에서 ID 복사:
   - URL 형식: `https://www.notion.so/workspace/Page-Title-{32자-hex-id}`
   - 예: `https://www.notion.so/My-Notion-Page-12345678123412341234123456789abc`
   - ID 부분: `12345678123412341234123456789abc` (32자 hex, hyphen 제외)

#### 4.2 새 .env 파일 생성

⚠️ `.env` 는 절대 git commit 금지. `.gitignore` 에 `.env` 가 포함되어 있는지
확인 후 작성.

```bash
cd /Users/emilio/projects/Projects/Language/_publish

# .env 파일 작성
cat > scripts/.env <<'EOF'
NOTION_TOKEN=secret_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
NOTION_PARENT_PAGE_ID=12345678123412341234123456789abc
EOF

# 권한 축소 (다른 사용자가 못 읽게)
chmod 600 scripts/.env

# .gitignore 확인
grep -E '^\.env' .gitignore
# .env, .env.local, .env.*.local 이 모두 있어야 함
```

**중요**: `publish-to-notion.sh` 가 찾는 위치는 `_publish/.env` 임 (parent dir).
두 위치 중 어디든 가능하지만, 기존 스크립트 동작을 따르려면 `_publish/scripts/.env`
가 더 안전 (scripts 폴더 내부라 다른 사용자 접근 어려움).

#### 4.3 Publish 테스트

```bash
cd /Users/emilio/projects/Projects/Language

# Dry-run (Notion 호출 없이 변환만 확인)
python3 _publish/scripts/publish_to_notion.py \
  /path/to/test-post.md --dry-run

# 실제 발행
python3 _publish/scripts/publish_to_notion.py \
  /path/to/real-post.md
```

또는 wrapper 사용:

```bash
cd /Users/emilio/projects/Projects/Language/_publish/scripts
./publish-to-notion.sh /path/to/post.md
```

### 검증

- 발행한 post 가 Notion 의 parent page 아래에 새 페이지로 생성됨
- 마크다운 변환 정상 (heading, bullet, code block 등)
- wikilink 가 Notion 링크로 변환되거나 plain text 로 fallback (스크립트 동작에 따름)

---

## 작업 순서 요약

```
┌─────────────────────────────────────────────────┐
│ 1. Notion 토큰 회전 (조치 1)                     │  5분
│    - 새 integration 생성                          │
│    - 토큰 복사                                    │
└────────────────┬────────────────────────────────┘
                 ↓
┌─────────────────────────────────────────────────┐
│ 2. GitHub PAT 회전 (조치 2)                       │  5분
│    - 기존 PAT 폐기                                │
│    - 새 PAT 생성 + 복사                           │
└────────────────┬────────────────────────────────┘
                 ↓
┌─────────────────────────────────────────────────┐
│ 3. Force-push (조치 3)                           │  10분
│    - 양 repo remote URL 에 새 PAT 설정             │
│    - force-push 실행                              │
│    - 원격 URL 에서 PAT 즉시 제거                   │
└────────────────┬────────────────────────────────┘
                 ↓
┌─────────────────────────────────────────────────┐
│ 4. Notion publish 인프라 재설정 (조치 4)           │  10분
│    - Parent page ID 확보                          │
│    - .env 파일 생성 + 권한 600                    │
│    - Dry-run + 실제 발행 테스트                    │
└─────────────────────────────────────────────────┘
```

---

## 롤백 계획

각 조치별 실패 시 복구:

### 조치 1 실패 (Notion 회전)
- 새 integration 이 생성되지 않으면 → Notion 콘솔에서 수동 확인
- 토큰을 분실하면 → 새 integration 다시 생성

### 조치 2 실패 (GitHub PAT 회전)
- 기존 PAT 가 이미 폐기되었는데 새 PAT 생성이 안 되면 → 작업 중단, GitHub 지원팀 연락
- 기존 PAT 폐기 전에 새 PAT 생성 권장 (병행 가능)

### 조치 3 실패 (Force-push)
- Push 거절 (403) → 새 PAT 가 권한 부족. PAT 설정에서 "Contents: Read and write" 확인
- Network error → 재시도. 이미 push 된 부분은 멱등 (idempotent)
- `--force-with-lease` 사용 시 remote 가 local 보다 앞서면 거절 (안전)

### 조치 4 실패 (Notion publish)
- "Unauthorized" → NOTION_TOKEN 이 잘못됨. 토큰 재생성
- "Page not found" → NOTION_PARENT_PAGE_ID 가 잘못됨. URL 재확인
- integration 이 해당 page 에 접근 권한 없음 → Notion 에서 page 공유 설정에 integration 추가

---

## 체크리스트

본 가이드를 진행하면서 다음을 확인:

- [ ] Notion workspace 에서 새 integration 생성 완료
- [ ] 새 Notion 토큰 안전한 곳에 저장 (메모장, password manager)
- [ ] 기존 (노출된) Notion integration 비활성화/삭제
- [ ] GitHub 에서 기존 PAT 폐기 완료
- [ ] GitHub 에서 새 PAT 생성 + 저장
- [ ] 새 PAT 에서 wiki-language + typing-language 두 repo 권한 부여
- [ ] Language repo force-push 성공
- [ ] Game repo curation push 성공
- [ ] 양 repo remote URL 에서 PAT 제거 확인 (`git remote -v`)
- [ ] GitHub 웹에서 양 repo 의 최신 commit hash 가 local 과 일치 확인
- [ ] `_publish/scripts/.env` 파일 생성 + 권한 600
- [ ] `.gitignore` 에 `.env` 규칙 확인
- [ ] Notion publish dry-run 성공
- [ ] Notion publish 실제 발행 성공

---

## 참고: 발견된 모든 이슈와 그 처리

| # | 발견 | 상태 |
|---|---|---|
| 1 | Notion 토큰이 git history 에 노출 | ✅ filter-repo 로 history 에서 제거 + 디스크 삭제 |
| 2 | GitHub PAT 가 filter-repo NOTICE 출력에 노출 | ✅ local remote URL 에서 PAT 제거 (placeholder 복원). 회전은 본 가이드 |
| 3 | `_publish/scripts/__pycache__/` 에 compiled bytecode | ✅ filter-repo + 디스크 삭제 |
| 4 | `.env` 가 `.gitignore` 에 등록되어 있었지만 initial commit 부터 트래킹됨 | ✅ `.gitignore` 는 신규 추적 차단용으로 유지 |
| 5 | Game corpus curation (raw/) 가 per-word source 잔존 | ✅ EN/ES basic 47 entries 정리, 나머지 deferred |

---

## 후속 권고사항 (본 가이드 범위 외)

1. **PAT 만료 정책 강화** — 90일 rotation cycle 설정 (GitHub Settings → PAT → "Configure expiration policy")
2. **CI/CD 통합 시** — GitHub Actions secrets 사용 (PAT 을 workflow env 에 저장)
3. **Vault-remote URL 자동 검증** — `git remote -v` 출력에 PAT 패턴 없는지 CI check
4. **History scrub 자동화** — pre-commit hook 에서 `.env` / `.pyc` 추가 시 즉시 알림
5. **Notion API 키 권한 최소화** — 새 integration 생성 시 "Read content" 만 부여하고 발행 시에만 일시적 write 권한 부여

---

## 변경 이력

- **2026-07-14**: 본 가이드 초안 작성 (Language 세션 상태 점검)
