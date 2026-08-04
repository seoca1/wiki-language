#!/usr/bin/env/python3
"""Real-time quiz analytics dashboard.

Provides live updates on quiz performance.
"""
import json
import argparse
from pathlib import Path
from datetime import datetime
from collections import defaultdict

ROOT = Path("/Usersemelio/projects/Projects/Language") if Path("/Usersemelio").exists() else Path("/Users/emilio/projects/Projects/Language")
USERS_DIR = ROOT / "users"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--user", help="Specific user")
    parser.add_argument("--output", default=str(ROOT / "exports" / "quiz-realtime.md"))
    args = parser.parse_args()
    
    if not USERS_DIR.exists():
        return 0
    
    targets = [USERS_DIR / args.user] if args.user else [u for u in USERS_DIR.iterdir() if u.is_dir()]
    
    md = []
    md.append("# Real-Time Quiz Analytics Dashboard")
    md.append(f"**Generated:** {datetime.now().isoformat()}")
    md.append(f"**Time:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    md.append("")
    
    md.append("## User Performance Overview")
    md.append("")
    md.append("| User | SRS | Reviews | Avg Correct | Mastery |")
    md.append("|------|----:|--------:|------------:|--------:|")
    
    grand_total = {"srs": 0, "reviews": 0, "correct": 0, "mastered": 0}
    
    for u in targets:
        if not u.is_dir():
            continue
        s = u / "state.json"
        if not s.exists():
            continue
        try:
            st = json.loads(s.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        
        seen = st.get("concepts_seen", {})
        srs = st.get("srs", {})
        total_correct = sum(c.get("correct", 0) for c in seen.values())
        total_reviews = sum(c.get("reviews", 0) for c in seen.values())
        avg_correct = total_correct / max(total_reviews, 1) * 100
        mastered = sum(1 for c in seen.values() if c.get("correct", 0) >= 3)
        mastery_rate = mastered / max(len(seen), 1) * 100
        
        md.append(f"| {u.name} | {len(srs)} | {total_reviews} | {avg_correct:.1f}% | {mastery_rate:.1f}% |")
        grand_total["srs"] += len(srs)
        grand_total["reviews"] += total_reviews
        grand_total["correct"] += total_correct
        grand_total["mastered"] += mastered
    
    md.append("")
    md.append("## Aggregate")
    md.append(f"- **Total SRS**: {grand_total['srs']}")
    md.append(f"- **Total Reviews**: {grand_total['reviews']}")
    md.append(f"- **Total Correct**: {grand_total['correct']}")
    md.append(f"- **Total Mastered**: {grand_total['mastered']}")
    md.append("")
    
    md.append("## Recommendations")
    md.append("")
    md.append("- **Daily review**: Set specific time for review sessions")
    md.append("- **Mastery focus**: 5+ correct = mastered, lower to 3 for struggling cards")
    md.append("- **Track trends**: Compare week-over-week for progress")
    md.append("")
    
    target = Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n".join(md), encoding="utf-8")
    print(f"[OK] {target}")


if __name__ == "__main__":
    import sys
    sys.exit(main() or 0)
