#!/usr/bin/env/python3
"""Personal vocabulary collector.

Tracks personal vocabulary lists with multiple collections.
"""
import json
import argparse
import re
from pathlib import Path
from datetime import datetime
from collections import defaultdict

ROOT = Path("/Usersemelio/projects/Projects/Language") if Path("/Usersemelio").exists() else Path("/Users/emelio/projects/Projects/Language")
USERS_DIR = ROOT / "users"
LANGS = ["English", "Spanish", "Japanese", "Korean"]
SECTION = "## Cross-Language Equivalents"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--user", required=True)
    parser.add_argument("--add", help="Add concept to collection")
    parser.add_argument("--collection", default="default", help="Collection name")
    parser.add_argument("--list", action="store_true", help="List collections")
    parser.add_argument("--output", default=str(ROOT / "exports" / "personal-collections.md"))
    args = parser.parse_args()
    
    if not USERS_DIR.exists():
        return 0
    
    user_dir = USERS_DIR / args.user
    user_dir.mkdir(parents=True, exist_ok=True)
    collections_file = user_dir / "collections.json"
    
    if collections_file.exists():
        collections = json.loads(collections_file.read_text(encoding="utf-8"))
    else:
        collections = {"collections": {}}
    
    if args.list:
        md = [f"# Personal Collections: {args.user}", ""]
        if not collections["collections"]:
            md.append("No collections yet.")
        else:
            for name, items in collections["collections"].items():
                md.append(f"## {name} ({len(items)} items)")
                md.append("")
                for item in items:
                    md.append(f"- {item}")
                md.append("")
        target = Path(args.output)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("\n".join(md), encoding="utf-8")
        print(f"[OK] {target}")
        return 0
    
    if args.add:
        collections["collections"].setdefault(args.collection, [])
        if args.add not in collections["collections"][args.collection]:
            collections["collections"][args.collection].append(args.add)
            collections_file.write_text(json.dumps(collections, indent=2, ensure_ascii=False), encoding="utf-8")
            print(f"[OK] Added '{args.add}' to collection '{args.collection}'")
        else:
            print(f"Already in collection '{args.collection}'")
        return 0
    
    parser.print_help()
    return 1


if __name__ == "__main__":
    import sys
    sys.exit(main() or 0)
