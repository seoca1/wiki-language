#!/usr/bin/env/python3
"""Activity log analytics.

Analyzes user activity patterns from JSONL logs.
"""
import json
import argparse
from pathlib import Path
from datetime import datetime, timedelta
from collections import defaultdict, Counter

ROOT = Path("/Usersemelio/projects/Projects/Language") if Path("/Usersemelio").exists() else Path("/Usersemelio/projects/Projects/Language")
USERS_DIR = ROOT / "users"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default=str(ROOT / "exports" / "activity-analytics.md"))
    parser.add_argument("--days", type=int, default=30)
    args = parser.parse_args()
    
    if not USERS_DIR.exists():
        return 0
    
    cutoff = datetime.now() - timedelta(days=args.days)
    by_user = defaultdict(Counter)
    by_hour = Counter()
    by_action = Counter()
    total = 0
    
    for u in USERS_DIR.iterdir():
        if not u.is_dir():
            continue
        for log_file in u.glob("*.jsonl"):
            try:
                with open(log_file, "r", encoding="utf-8") as f:
                    for line in f:
                        if not line:
                            continue
                        try:
                            e = json.loads(line)
                        except json.JSONDecodeError:
                            continue
                        ts_str = e.get("timestamp", "")
                        try:
                            ts = datetime.fromisoformat(ts_str)
                        except ValueError:
                            continue
                        if ts < cutoff:
                            continue
                        by_user[e.get("user", "?")][e.get("action", "?")] += 1
                        by_hour[ts.hour] += 1
                        by_action[e.get("action", "?")] += 1
                        total += 1
            except OSError:
                pass
    
    md = []
    md.append(f"# Activity Analytics ({args.days}-day window)")
    md.append("")
    md.append(f"**Generated:** {datetime.now().isoformat()}")
    md.append(f"**Total events**: {total}")
    md.append("")
    
    md.append("## By Hour of Day")
    md.append("")
    md.append("| Hour | Events |")
    md.append("|------|-------:|")
    for h in sorted(by_hour.keys()):
        bar = "█" * min(by_hour[h], 30)
        md.append(f"| {h:02d}:00 | {by_hour[h]:3d} {bar} |")
    md.append("")
    
    md.append("## By Action Type")
    md.append("")
    md.append("| Action | Count |")
    md.append("|--------|------:|")
    for action, count in by_action.most_common(15):
        md.append(f"| {action} | {count} |")
    md.append("")
    
    md.append("## By User")
    md.append("")
    md.append("| User | Total | Top Action |")
    md.append("|------|------:|-----------|")
    for user, actions in sorted(by_user.items(), key=lambda x: -sum(x[1].values())):
        top = actions.most_common(1)[0]
        md.append(f"| {user} | {sum(actions.values())} | {top[0]} ({top[1]}) |")
    md.append("")
    
    target = Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n".join(md), encoding="utf-8")
    print(f"[OK] {target}")


if __name__ == "__main__":
    import sys
    sys.exit(main() or 0)
