#!/usr/bin/env/python3
"""Vocabulary review scheduler.

Schedules optimal review sessions using spaced repetition.
"""
import json
import argparse
from pathlib import Path
from datetime import datetime, timedelta
from collections import defaultdict

ROOT = Path("/Usersemelio/projects/Projects/Language") if Path("/Usersemelio").exists() else Path("/Users/emelio/projects/Projects/Language")
USERS_DIR = ROOT / "users"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--user", required=True)
    parser.add_argument("--days", type=int, default=7)
    parser.add_argument("--output", default=str(ROOT / "exports" / "review-schedule.md"))
    args = parser.parse_args()
    
    state_file = USERS_DIR / args.user / "state.json"
    if not state_file.exists():
        return 1
    state = json.loads(state_file.read_text(encoding="utf-8"))
    srs = state.get("srs", {})
    today = datetime.now().date()
    
    # Generate schedule
    md = []
    md.append(f"# Review Schedule: {args.user}")
    md.append("")
    md.append(f"**Generated:** {datetime.now().isoformat()}")
    md.append("")
    
    # Group by date
    by_date = defaultdict(list)
    for concept_id, data in srs.items():
        next_review = data.get("next_review", "")
        if not next_review:
            continue
        try:
            rd = datetime.fromisoformat(next_review).date()
            if rd <= today + timedelta(days=args.days):
                by_date[rd].append({
                    "concept": concept_id,
                    "ease": data.get("ease", 2.5),
                    "interval": data.get("interval", 0),
                    "reps": data.get("reps", 0),
                })
        except (ValueError, TypeError):
            pass
    
    md.append(f"## Schedule for next {args.days} days")
    md.append("")
    for date in sorted(by_date.keys())[:args.days]:
        day_name = date.strftime("%A")
        items = by_date[date]
        md.append(f"### {date} ({day_name}) - {len(items)} cards")
        md.append("")
        for item in items[:5]:
            quality = "hard" if item["ease"] < 2.0 else "medium" if item["ease"] < 2.5 else "easy"
            md.append(f"- {item['concept']} (ease: {item['ease']:.2f}, {quality})")
        if len(items) > 5:
            md.append(f"- ... and {len(items) - 5} more")
        md.append("")
    
    target = Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n".join(md), encoding="utf-8")
    print(f"[OK] {target}")


if __name__ == "__main__":
    import sys
    sys.exit(main() or 0)
