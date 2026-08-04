#!/usr/bin/env/python3
"""Federated progress v2.

Aggregated progress with trend analysis.
"""
import json
import argparse
from pathlib import Path
from datetime import datetime, timedelta
from collections import defaultdict

ROOT = Path("/Usersemelio/projects/Projects/Language") if Path("/Usersemelio").exists() else Path("/Users/emilio/projects/Projects/Language")
USERS_DIR = ROOT / "users"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default=str(ROOT / "exports" / "fed-progress-v2.md"))
    args = parser.parse_args()
    
    if not USERS_DIR.exists():
        return 0
    
    md = []
    md.append("# Federated Progress v2")
    md.append("")
    md.append(f"**Generated:** {datetime.now().isoformat()}")
    md.append("")
    
    stats = []
    for u in USERS_DIR.iterdir():
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
        last = None
        for cid, data in srs.items():
            lr = data.get("last_reviewed", "")
            if lr and (not last or lr > last):
                last = lr
        
        stats.append({
            "user": u.name,
            "seen": len(seen),
            "srs": len(srs),
            "mastered": sum(1 for c in seen.values() if c.get("correct", 0) >= 3),
            "last": last[:10] if last else "never",
        })
    
    md.append("## Per-User Status")
    md.append("")
    md.append("| User | Seen | SRS | Mastered | Last Activity |")
    md.append("|------|-----:|----:|---------:|---------------|")
    for s in sorted(stats, key=lambda x: -x["srs"]):
        md.append(f"| {s['user']} | {s['seen']} | {s['srs']} | {s['mastered']} | {s['last']} |")
    md.append("")
    
    # Trends
    md.append("## Trends")
    md.append("")
    md.append("### Top performers (by SRS)")
    md.append("")
    for s in sorted(stats, key=lambda x: -x["srs"])[:3]:
        md.append(f"- **{s['user']}**: {s['srs']} SRS items")
    md.append("")
    
    md.append("### Activity")
    today = datetime.now().date()
    week_ago = today - timedelta(days=7)
    active_week = sum(1 for s in stats if s["last"] != "never" and datetime.fromisoformat(s["last"]).date() >= week_ago)
    md.append(f"- **Active in last week**: {active_week}")
    md.append(f"- **Total users**: {len(stats)}")
    md.append("")
    
    target = Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n".join(md), encoding="utf-8")
    print(f"[OK] {target}")


if __name__ == "__main__":
    import sys
    sys.exit(main() or 0)
