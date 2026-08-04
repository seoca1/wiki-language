#!/usr/bin/env/python3
"""Vocabulary quiz review system.

Coordinates spaced repetition review sessions.
"""
import json
import argparse
import re
import random
from pathlib import Path
from datetime import datetime, timedelta
from collections import defaultdict

ROOT = Path("/Usersemelio/projects/Projects/Language") if Path("/Usersemelio").exists() else Path("/Users/emelio/projects/Projects/Language")
USERS_DIR = ROOT / "users"
LANGS = ["English", "Spanish", "Japanese", "Korean"]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--user", required=True)
    parser.add_argument("--lang", default="English")
    parser.add_argument("--count", type=int, default=10)
    parser.add_argument("--output", default=str(ROOT / "exports" / "vocab-quiz-system.md"))
    args = parser.parse_args()
    
    state_file = USERS_DIR / args.user / "state.json"
    if not state_file.exists():
        return 1
    
    state = json.loads(state_file.read_text(encoding="utf-8"))
    srs = state.get("srs", {})
    seen = state.get("concepts_seen", {})
    
    today = datetime.now().date()
    week_from_now = today + timedelta(days=7)
    
    due = []
    for concept_id, data in srs.items():
        next_review = data.get("next_review", "")
        if not next_review:
            continue
        try:
            rd = datetime.fromisoformat(next_review).date()
            if rd <= week_from_now:
                due.append((concept_id, data, rd))
        except (ValueError, TypeError):
            pass
    
    due.sort(key=lambda x: x[2])
    
    md = []
    md.append(f"# Vocabulary Quiz Review System: {args.user} ({args.lang})")
    md.append("")
    md.append(f"**Generated:** {datetime.now().isoformat()}")
    md.append(f"**Total SRS items**: {len(srs)}")
    md.append(f"**Due in next 7 days**: {len(due)}")
    md.append("")
    
    if due:
        md.append("## Review Schedule")
        md.append("")
        md.append("| # | Concept | Date | Quality |")
        md.append("|---|---------|------|---------|")
        for i, (cid, data, rd) in enumerate(due[:args.count], 1):
            ease = data.get("ease", 2.5)
            quality = "hard" if ease < 2.0 else "medium" if ease < 2.5 else "easy"
            md.append(f"| {i} | {cid} | {rd} | {quality} |")
    else:
        md.append("No reviews due in next 7 days. 🎉")
    md.append("")
    
    md.append("## Study Tips")
    md.append("")
    md.append("1. **Daily session**: 15-20 min")
    md.append("2. **Hard items first**: Mark with quality < 2.5 ease")
    md.append("3. **Audio + Visual**: Use TTS for pronunciation")
    md.append("4. **Context**: Use XL mesh for cross-language practice")
    md.append("")
    
    target = Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n".join(md), encoding="utf-8")
    print(f"[OK] {target}")


if __name__ == "__main__":
    import sys
    sys.exit(main() or 0)
