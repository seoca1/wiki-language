#!/usr/bin/env/python3
"""Federated learning session.

Generates coordinated learning sessions across users.
"""
import json
import argparse
from pathlib import Path
from datetime import datetime
from collections import defaultdict

ROOT = Path("/Usersemelio/projects/Projects/Language") if Path("/Usersemelio").exists() else Path("/Users/emelio/projects/Projects/Language")
USERS_DIR = ROOT / "users"
SESSION_DIR = ROOT / "exports" / "sessions"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--users", nargs="+", help="User names")
    parser.add_argument("--date", help="Session date (default: today)")
    parser.add_argument("--output", default=str(ROOT / "exports" / "fed-learning-session.md"))
    args = parser.parse_args()
    
    if not USERS_DIR.exists():
        return 0
    
    if not args.users:
        args.users = [u.name for u in USERS_DIR.iterdir() if u.is_dir()]
    
    date = args.date or datetime.now().date().isoformat()
    SESSION_DIR.mkdir(parents=True, exist_ok=True)
    
    md = []
    md.append(f"# Federated Learning Session: {date}")
    md.append("")
    md.append(f"**Participants:** {', '.join(args.users)}")
    md.append(f"**Generated:** {datetime.now().isoformat()}")
    md.append("")
    
    md.append("## Session Plan")
    md.append("")
    md.append("1. **Warm-up (5 min)**: Daily review")
    md.append("2. **Vocab (10 min)**: 5 new words")
    md.append("3. **Grammar (10 min)**: Topic discussion")
    md.append("4. **Practice (10 min)**: Apply new vocab")
    md.append("5. **Wrap-up (5 min)**: Set goals for next session")
    md.append("")
    
    md.append("## Per-User Focus")
    md.append("")
    md.append("| User | Focus Area | Vocabulary |")
    md.append("|------|------------|-------------|")
    
    for user in args.users:
        s = USERS_DIR / user / "state.json"
        if s.exists():
            try:
                st = json.loads(s.read_text(encoding="utf-8"))
                seen = st.get("concepts_seen", {})
                srs = st.get("srs", {})
                # Get most common tag for focus
                tags = defaultdict(int)
                for cid in seen:
                    lang_code = cid.split("/")[0] if "/" in cid else "unknown"
                    tags[lang_code] += 1
                focus = max(tags, key=tags.get) if tags else "general"
                md.append(f"| {user} | {focus} | {len(seen)} seen, {len(srs)} SRS |")
            except Exception:
                md.append(f"| {user} | - | - |")
        else:
            md.append(f"| {user} | - | - |")
    md.append("")
    
    md.append("## Shared Goals")
    md.append("")
    md.append("- Complete 10 reviews per user per day")
    md.append("- Learn 5 new words per day per user")
    md.append("- Maintain 80% accuracy")
    md.append("")
    
    target = Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n".join(md), encoding="utf-8")
    
    # Save session
    session_file = SESSION_DIR / f"session-{date}.json"
    session_data = {
        "date": date,
        "users": args.users,
        "plan": "warmup,vocab,grammar,practice,wrapup",
        "duration": "40min",
        "created": datetime.now().isoformat(),
    }
    session_file.write_text(json.dumps(session_data, indent=2, ensure_ascii=False), encoding="utf-8")
    
    print(f"[OK] {target}")
    print(f"     Session saved: {session_file.name}")


if __name__ == "__main__":
    import sys
    sys.exit(main() or 0)
