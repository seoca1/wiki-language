#!/usr/bin/env/python3
"""Multi-language progress tracking.

Tracks learning across all 4 languages.
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
    parser.add_argument("--user", help="All users if not specified")
    parser.add_argument("--output", default=str(ROOT / "exports" / "progress-tracker.md"))
    args = parser.parse_args()
    
    if not USERS_DIR.exists():
        return 0
    
    user_langs = defaultdict(lambda: defaultdict(int))
    grand_total = defaultdict(int)
    
    targets = [USERS_DIR / args.user] if args.user else [u for u in USERS_DIR.iterdir() if u.is_dir()]
    
    for u in targets:
        if not u.is_dir():
            continue
        s = u / "state.json"
        if not s.exists():
            continue
        try:
            state = json.loads(s.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        
        # Count by language
        for cid in state.get("concepts_seen", {}):
            lang = cid.split("/")[0] if "/" in cid else "unknown"
            user_langs[u.name][lang] += 1
            grand_total[lang] += 1
    
    md = []
    md.append("# Multi-Language Progress Tracking")
    md.append("")
    md.append(f"**Generated:** {datetime.now().isoformat()}")
    md.append("")
    
    md.append("## Per-User Language Coverage")
    md.append("")
    for user, langs in sorted(user_langs.items()):
        md.append(f"### {user}")
        md.append("")
        for lang in LANGS:
            count = langs.get(lang, 0)
            md.append(f"- {lang}: {count}")
        md.append("")
    
    md.append("## Aggregate")
    md.append("")
    for lang in LANGS:
        count = grand_total.get(lang, 0)
        md.append(f"- **{lang}**: {count}")
    md.append("")
    md.append(f"- **TOTAL**: {sum(grand_total.values())}")
    md.append("")
    
    target = Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n".join(md), encoding="utf-8")
    print(f"[OK] {target}")


if __name__ == "__main__":
    import sys
    sys.exit(main() or 0)
