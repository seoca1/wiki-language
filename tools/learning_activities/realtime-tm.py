#!/usr/bin/env/python3
"""Real-time translation memory.

Manages live translation pairs with TTL and usage tracking.
"""
import json
import argparse
from pathlib import Path
from datetime import datetime, timedelta
from collections import defaultdict

ROOT = Path("/Usersemelio/projects/Projects/Language") if Path("/Usersemelio").exists() else Path("/Users/emilio/projects/Projects/Language")
TM_DIR = ROOT / "exports" / "realtime_tm"
TM_DIR.mkdir(parents=True, exist_ok=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--add", nargs=2, help="Add translation (source target)")
    parser.add_argument("--query", help="Query source text")
    parser.add_argument("--output", default=str(ROOT / "exports" / "realtime-tm.md"))
    args = parser.parse_args()
    
    if args.add:
        source, target = args.add
        pair = {
            "source": source,
            "target": target,
            "added": datetime.now().isoformat(),
            "uses": 1,
        }
        ts = datetime.now().timestamp()
        file = TM_DIR / f"{int(ts)}.json"
        file.write_text(json.dumps(pair, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"[OK] Added: {source} -> {target}")
        return 0
    
    if args.query:
        # Find matches
        matches = []
        for f in TM_DIR.glob("*.json"):
            try:
                pair = json.loads(f.read_text(encoding="utf-8"))
                if args.query.lower() in pair["source"].lower():
                    matches.append(pair)
            except (json.JSONDecodeError, OSError):
                pass
        
        md = [f"# TM Matches for: {args.query}", ""]
        for m in matches:
            md.append(f"- **{m['source']}** → **{m['target']}** (uses: {m['uses']})")
        if not matches:
            md.append("No matches found.")
        target = Path(args.output)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("\n".join(md), encoding="utf-8")
        print(f"[OK] {target}")
        return 0
    
    parser.print_help()
    return 1


if __name__ == "__main__":
    import sys
    sys.exit(main() or 0)
