#!/usr/bin/env python3
"""
Append markdown content to an existing Notion page.
Used for adding investigation reports to the canonical OpenCode operations page.
"""

import os
import re
import sys
from pathlib import Path
from typing import Any

from notion_client import Client
from notion_client.errors import APIResponseError
from rich.console import Console

console = Console()

# ---------------------------------------------------------------------------
# Markdown → Notion block 변환기 (publish_to_notion.py 에서 복사)
# ---------------------------------------------------------------------------

def rich_text(text: str) -> list[dict]:
    """인라인 텍스트 → Notion rich_text 배열. **bold**, *italic*, `code` 지원."""
    if not text:
        return [{"type": "text", "text": {"content": ""}}]
    parts: list[dict] = []
    pattern = re.compile(r"(\*\*[^*]+\*\*|\*[^*]+\*|`[^`]+`|\[[^\]]+\]\([^)]+\))")
    pos = 0
    for m in pattern.finditer(text):
        if m.start() > pos:
            parts.append(_text_plain(text[pos:m.start()]))
        token = m.group(0)
        if token.startswith("**"):
            parts.append(_text_with_annotations(token[2:-2], bold=True))
        elif token.startswith("`"):
            parts.append(_text_with_annotations(token[1:-1], code=True))
        elif token.startswith("["):
            link_match = re.match(r"\[([^\]]+)\]\(([^)]+)\)", token)
            if link_match:
                label, url = link_match.groups()
                parts.append({"type": "text", "text": {"content": label, "link": {"url": url}}})
        elif token.startswith("*"):
            parts.append(_text_with_annotations(token[1:-1], italic=True))
        pos = m.end()
    if pos < len(text):
        parts.append(_text_plain(text[pos:]))
    return parts or [{"type": "text", "text": {"content": text}}]


def _text_plain(content: str) -> dict:
    return {"type": "text", "text": {"content": content}}


def _text_with_annotations(content: str, bold=False, italic=False, code=False) -> dict:
    ann = {"bold": bold, "italic": italic, "strikethrough": False,
           "underline": False, "code": code, "color": "default"}
    return {"type": "text", "text": {"content": content}, "annotations": ann}


def make_heading(level: int, text: str) -> dict:
    return {
        "object": "block",
        "type": f"heading_{level}",
        f"heading_{level}": {"rich_text": rich_text(text)},
    }


def make_paragraph(text: str) -> dict:
    return {
        "object": "block",
        "type": "paragraph",
        "paragraph": {"rich_text": rich_text(text)},
    }


def make_quote(text: str) -> dict:
    return {
        "object": "block",
        "type": "quote",
        "quote": {"rich_text": rich_text(text)},
    }


def make_bulleted_item(text: str) -> dict:
    return {
        "object": "block",
        "type": "bulleted_list_item",
        "bulleted_list_item": {"rich_text": rich_text(text)},
    }


def make_numbered_item(text: str) -> dict:
    return {
        "object": "block",
        "type": "numbered_list_item",
        "numbered_list_item": {"rich_text": rich_text(text)},
    }


def make_divider() -> dict:
    return {"object": "block", "type": "divider", "divider": {}}


def make_table(headers: list[str], rows: list[list[str]]) -> dict:
    """Notion 테이블 블록 (table은 자식 table_row를 가져야 한다)."""
    children = []
    for row in [headers, *rows]:
        children.append({
            "object": "block",
            "type": "table_row",
            "table_row": {"cells": [rich_text(cell) for cell in row]},
        })
    return {
        "object": "block",
        "type": "table",
        "table": {
            "table_width": len(headers),
            "has_column_header": True,
            "has_row_header": False,
            "children": children,
        },
    }


def make_callout(text: str, emoji: str = "💡") -> dict:
    return {
        "object": "block",
        "type": "callout",
        "callout": {
            "rich_text": rich_text(text),
            "icon": {"type": "emoji", "emoji": emoji},
            "color": "default",
        },
    }


def make_code_block(text: str, language: str = "plain text") -> dict:
    return {
        "object": "block",
        "type": "code",
        "code": {
            "rich_text": [{"type": "text", "text": {"content": text}}],
            "language": language,
        },
    }


# ---------------------------------------------------------------------------
# 마크다운 파서 (확장판: 번호 목록, 코드 블록 지원)
# ---------------------------------------------------------------------------

def parse_blocks(md_text: str) -> list[dict]:
    """
    마크다운 텍스트를 Notion 블록 리스트로 변환.
    지원: 제목, 단락, 인용, 글머리표, 번호 목록, 구분선, 표, 콜아웃, 코드 블록.
    """
    lines = md_text.split("\n")
    blocks: list[dict] = []
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]
        stripped = line.strip()

        # 빈 줄
        if not stripped:
            i += 1
            continue

        # 구분선
        if re.match(r"^-{3,}$|^\*{3,}$", stripped):
            blocks.append(make_divider())
            i += 1
            continue

        # 코드 블록
        if stripped.startswith("```"):
            lang = stripped[3:].strip() or "plain text"
            i += 1
            code_lines = []
            while i < n and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            if i < n and lines[i].strip().startswith("```"):
                i += 1  # skip closing ```
            blocks.append(make_code_block("\n".join(code_lines), lang))
            continue

        # 표 감지 (다음 줄이 | --- | 형태)
        if stripped.startswith("|") and i + 1 < n and re.match(r"^\|[\s:|-]+\|$", lines[i + 1].strip()):
            header_cells = [c.strip() for c in stripped.strip("|").split("|")]
            i += 2  # skip header and separator
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                row_cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                rows.append(row_cells)
                i += 1
            blocks.append(make_table(header_cells, rows))
            continue

        # 제목 (# ~ ######)
        heading_match = re.match(r"^(#{1,3})\s+(.*)$", stripped)
        if heading_match:
            level = len(heading_match.group(1))
            blocks.append(make_heading(min(level, 3), heading_match.group(2)))
            i += 1
            continue

        # 인용 (>, 다중 라인 가능)
        if stripped.startswith(">") and not re.match(r"^>\s*\[!\w+\]", stripped):
            quote_lines = []
            while i < n and lines[i].strip().startswith(">") and not re.match(r"^>\s*\[!\w+\]", lines[i].strip()):
                quote_lines.append(lines[i].strip().lstrip(">").strip())
                i += 1
            blocks.append(make_quote(" ".join(quote_lines)))
            continue

        # 콜아웃 (> [!TIP] 같은 패턴)
        callout_match = re.match(r"^>\s*\[!(\w+)\]\s*(.*)$", stripped)
        if callout_match:
            kind, text = callout_match.groups()
            emoji = {"TIP": "💡", "NOTE": "📝", "WARN": "⚠️", "INFO": "ℹ️"}.get(kind.upper(), "💡")
            blocks.append(make_callout(text, emoji))
            i += 1
            continue

        # 번호 목록
        if re.match(r"^\d+\.\s+", stripped):
            content = re.sub(r"^\d+\.\s+", "", stripped)
            blocks.append(make_numbered_item(content))
            i += 1
            continue

        # 글머리표
        if re.match(r"^[-*]\s+", stripped):
            content = re.sub(r"^[-*]\s+", "", stripped)
            blocks.append(make_bulleted_item(content))
            i += 1
            continue

        # 기본: 단락 (연속된 비어있지 않은 줄을 하나의 단락으로 결합)
        para_lines = [stripped]
        i += 1
        while i < n and lines[i].strip() and not _is_block_start(lines[i].strip()):
            para_lines.append(lines[i].strip())
            i += 1
        blocks.append(make_paragraph(" ".join(para_lines)))

    return blocks


def _is_block_start(line: str) -> bool:
    return bool(
        re.match(r"^#{1,3}\s+", line)
        or re.match(r"^[-*]\s+", line)
        or re.match(r"^\d+\.\s+", line)
        or re.match(r"^>\s*", line)
        or re.match(r"^-{3,}$|^\*{3,}$", line)
        or line.startswith("|")
        or line.startswith("```")
    )


def chunked(seq: list, size: int = 100):
    for i in range(0, len(seq), size):
        yield seq[i:i + size]


# ---------------------------------------------------------------------------
# 메인
# ---------------------------------------------------------------------------

def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description="마크다운을 기존 Notion 페이지에 추가")
    parser.add_argument("file", type=Path, help="추가할 .md 파일")
    parser.add_argument("--page-id", default=None, help="대상 페이지 ID (환경변수 NOTION_PAGE_ID 대신 사용)")
    parser.add_argument("--dry-run", action="store_true", help="Notion 호출 없이 변환만 출력")
    args = parser.parse_args()

    if not args.file.exists():
        console.print(f"[red]파일을 찾을 수 없습니다: {args.file}[/red]")
        return 1

    md_text = args.file.read_text(encoding="utf-8")
    blocks = parse_blocks(md_text)

    if args.dry_run:
        console.print(f"[bold cyan]드라이런 모드[/bold cyan]")
        console.print(f"블록 수: {len(blocks)}")
        console.print("\n[dim]--- 처음 10개 블록 ---[/dim]")
        for blk in blocks[:10]:
            console.print(blk)
        return 0

    token = os.environ.get("NOTION_TOKEN")
    page_id = args.page_id or os.environ.get("NOTION_PAGE_ID")
    if not token:
        console.print("[red]NOTION_TOKEN 환경변수가 설정되지 않았습니다.[/red]")
        return 1
    if not page_id:
        console.print("[red]NOTION_PAGE_ID (또는 --page-id) 가 필요합니다.[/red]")
        return 1

    notion = Client(auth=token)

    try:
        # 100개씩 chunk해서 append
        for chunk in chunked(blocks, 100):
            notion.blocks.children.append(block_id=page_id, children=chunk)
    except APIResponseError as e:
        console.print(f"[red]Notion API 오류: {e}[/red]")
        return 1

    console.print(f"[bold green]✅ Notion 페이지에 추가 완료[/bold green]")
    console.print(f"   페이지 ID: {page_id}")
    console.print(f"   추가 블록 수: {len(blocks)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())