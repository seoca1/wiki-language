#!/usr/bin/env/python3
"""Federated search history.

Tracks search queries across users for analysis.
"""
import json
import argparse
from pathlib import Path
from datetime import datetime
from collections import defaultdict, Counter

ROOT = Path("/Usersemelio/projects/Projects/Language") if Path("/Usersemelio").exists() else Path("/Users/emilio/projects/Projects/Language")
HISTORY = ROOT / "exports" / "search_history.jsonl"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--add", nargs=2, help="Log search: user query")
    parser.add_argument("--user", required=True)
    parser.add_argument("--report", action="store_true", help="Show report")
    parser.add_argument("--output", default=str(ROOT / "exports" / "search-history.md"))
    args = parser.parse_args()
    
    HISTORY.parent.mkdir(parents=True, exist_ok=True)
    
    if args.add:
        user, query = args.add
        entry = {
            "timestamp": datetime.now().isoformat(),
            "user": user,
            "query": query,
        }
        with open(HISTORY, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")
        print(f"[OK] Logged: {user} - {query}")
        return 0
    
    if args.report:
        queries_by_user = defaultdict(list)
        query_counts = Counter()
        if HISTORY.exists():
            for line in HISTORY.read_text(encoding="utf-8").split("\n"):
                if line:
                    try:
                        e = json.loads(line)
                        queries_by_user[e["user"]].append(e["query"])
                        query_counts[e["query"]] += 1
                    except json.JSONDecodeError:
                        pass
        
        md = []
        md.append("# Federated Search History Report")
        md.append("")
        md.append(f"**Generated:** {datetime.now().isoformat()}")
        md.append(f"**Total searches:** {sum(query_counts.values())}")
        md.append("")
        
        md.append("## Top Queries")
        md.append("")
        md.append("| Query | Count |")
        md.append("|------|------:|")
        for q, c in query_counts.most_common(20):
            md.append(f"| {q} | {c} |")
        md.append("")
        
        md.append("## Per-User")
        md.append("")
        for user, queries in sorted(queries_by_user.items()):
            md.append(f"### {user} ({len(queries)} searches)")
            md.append("")
            for q in queries[:10]:
                md.append(f"- {q}")
            md.append("")
        
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
