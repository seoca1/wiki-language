#!/usr/bin/env bash
# publish-to-notion.sh
# Notion API 토큰을 안전하게 사용하기 위한 helper.
# 사용법:
#   1) .env 파일에 토큰과 parent page id 저장 (절대 git commit 하지 말 것)
#   2) source .env && ./publish-to-notion.sh ../2026-W25/semana-1-arranque.md

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
ENV_FILE="$ROOT_DIR/.env"

if [[ -f "$ENV_FILE" ]]; then
  set -a
  # shellcheck disable=SC1090
  source "$ENV_FILE"
  set +a
else
  echo "⚠️  $ENV_FILE 이 없습니다. .env.example을 참고해 만드세요."
  exit 1
fi

if [[ -z "${NOTION_TOKEN:-}" || -z "${NOTION_PARENT_PAGE_ID:-}" ]]; then
  echo "❌ NOTION_TOKEN 또는 NOTION_PARENT_PAGE_ID 가 비어 있습니다."
  exit 1
fi

POST_FILE="${1:-}"
if [[ -z "$POST_FILE" ]]; then
  echo "Usage: $0 <path-to-post.md>"
  exit 1
fi

if [[ ! -f "$POST_FILE" ]]; then
  POST_FILE="$SCRIPT_DIR/$POST_FILE"
fi
if [[ ! -f "$POST_FILE" ]]; then
  echo "❌ 파일을 찾을 수 없습니다: $POST_FILE"
  exit 1
fi

python3 "$SCRIPT_DIR/publish_to_notion.py" "$POST_FILE"
