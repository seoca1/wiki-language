#!/usr/bin/env/python3
"""Vocabulary mastery tracker.

Tracks mastery progression with time-series data.
"""
import json
import argparse
import re
from pathlib import Path
from datetime import datetime
from collections import defaultdict

ROOT = Path("/Usersemelio/projects/Projects/Language") if Path("/Usersemelio").exists() else Path("/Users/emelio/projects/Projects/Language")
USERS_DIR = ROOT / "users"
HISTORY_DIR = ROOT / "exports" / "mastery_history"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--user", required=True)
    parser.add_argument("--snapshot", action="store_true", help="Save current as snapshot")
    parser.add_argument("--report", action="store_true", help="Show history report")
    parser.add_argument("--output", default=str(ROOT / "exports" / "mastery-tracker.md"))
    args = parser.use_args = None
    parser = argparse.ArgumentParser()
    parser.add_argument("--user", required=True)
    parser.add_argument("--snapshot", action="store_true")
    parser.add_argument("--report", action="store_true")
    parser.add_argument("--output", default=str(ROOT / "exports" / "mastery-tracker.md"))
    args = parser.parse_args()
    
    state_file = USERS_DIR / args.user / "state.json"
    if not state_file.exists():
        return 1
    state = json.loads(state_file.read_text(encoding="utf-8"))
    seen = state.get("concepts_seen", {})
    srs = state.get("srs", {})
    
    if args.snapshot:
        HISTORY_DIR.mkdir(parents=True, exist_ok=True)
        snap = {
            "timestamp": datetime.now().isoformat(),
            "seen_count": len(seen),
            "srs_count": len(srs),
            "mastered": sum(1 for c in seen.values() if c.get("correct", 0) >= 3),
            "total_reviews": sum(c.get("reviews", 0) for c in seen.values()),
            "total_correct": sum(c.get("correct", 0) for c in seen.values()),
        }
        snap_file = HISTORY_DIR / f"{args.user}-{int(datetime.now().timestamp())}.json"
        snap_file.write_text(json.dumps(snap, indent=2), encoding="utf-8")
        print(f"[OK] Snapshot saved: {snap_file.name}")
        return 0
    
    if args.report:
        # Build history
        user_history = sorted(HISTORY_DIR.glob(f"{args.user}-*.json")) if HISTORY_DIR.exists() else []
        
        md = []
        md.append(f"# Mastery Tracker: {args.user}")
        md.append("")
        md.append(f"**Generated:** {datetime.now().isoformat()}")
        md.append("")
        
        if user_history:
            md.append("## History")
            md.append("")
            md.append("| Date | Seen | SRS | Mastered |")
            md.append("|------|-----:|----:|---------:|")
            for snap in user_history:
                data = json.loads(snap.read_text(encoding="utf-8"))
                md.append(f"| {data['timestamp'][:19]} | {data['seen_count']} | {data['srs_count']} | {data['mastered']} |")
            md.append("")
        else:
            md.append("No history snapshots yet. Use --snapshot to save one.")
        md.append("")
        
        target = Path(args.output)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("\n".join(md), encoding="utf-8")
        print(f"[OK] {target}")
        return 0
    
    # Default: show current state
    md = []
    md.append(f"# Vocabulary Mastery Tracker: {args.user}")
    md.append("")
    md.append(f"**Generated:** {datetime.now().isoformat()}")
    md.append(f"**Seen:** {len(seen)} | **SRS:** {len(srs)} | **Mastered:** {sum(1 for c in seen.values() if c.get('correct', 0) >= 3)}")
    md.append("")
    md.append("Use --snapshot to save current state, --report to show history.")
    print("".join(md))
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main() or 0)
