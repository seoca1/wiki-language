#!/usr/bin/env/python3
"""Multi-language content stats v2.

Detailed statistics per language with coverage analysis.
"""
import json
import argparse
import re
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime

ROOT = Path("/Usersemelio/projects/Projects/Language") if Path("/Usersemelio").exists() else Path("/Users/emelio/projects/Projects/Language")
LANGS = ["English", "Spanish", "Japanese", "Korean"]
SECTION = "## Cross-Language Equivalents"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default=str(ROOT / "exports" / "content-stats-v2.md"))
    args = parser.parse_args()
    
    md = []
    md.append("# Multi-Language Content Stats v2")
    md.append("")
    md.append(f"**Generated:** {datetime.now().isoformat()}")
    md.append("")
    
    for lang in LANGS:
        vdir = ROOT / "wiki" / lang / "vocabulary"
        if not vdir.exists():
            continue
        
        total = 0
        with_xl = 0
        with_stub = 0
        with_tags = 0
        with_ipa = 0
        tags_counter = Counter()
        levels = Counter()
        
        for f in vdir.glob("*.md"):
            if "-vocabulary" in f.name or f.stem.startswith("index"):
                continue
            text = f.read_text(encoding="utf-8", errors="ignore")
            total += 1
            if "_TODO_" in text:
                with_stub += 1
            if "## Cross-Language Equivalents" in text:
                with_xl += 1
            if "<!-- tags:" in text:
                with_tags += 1
                m_tag = re.search(r"<!-- tags: ([^>]+) -->", text)
                if m_tag:
                    for t in m_tag.group(1).split(","):
                        tags_counter[t.strip()] += 1
            if "## Pronunciation" in text or "**IPA:**" in text:
                with_ipa += 1
            m_level = re.search(r"\*\*Level:\*\* ([A-Z0-9\-]+)", text)
            if m_level:
                levels[m_level.group(1)] += 1
        
        if total > 0:
            md.append(f"## {lang}")
            md.append("")
            md.append(f"- **Total entries**: {total}")
            md.append(f"- **With XL mesh**: {with_xl} ({100*with_xl/total:.0f}%)")
            md.append(f"- **With tags**: {with_tags} ({100*with_tags/total:.0f}%)")
            md.append(f"- **With IPA**: {with_ipa} ({100*with_ipa/total:.0f}%)")
            md.append(f"- **Stub (TODO)**: {with_stub}")
            md.append("")
            
            if levels:
                md.append("### By Level")
                md.append("")
                for lvl, count in sorted(levels.items(), key=lambda x: x[1], reverse=True)[:5]:
                    md.append(f"- {lvl}: {count}")
                md.append("")
            
            if tags_counter:
                md.append("### Top Tags")
                md.append("")
                for tag, count in tags_counter.most_common(10):
                    md.append(f"- {tag}: {count}")
                md.append("")
    
    target = Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n".join(md), encoding="utf-8")
    print(f"[OK] {target}")


if __name__ == "__main__":
    import sys
    sys.exit(main() or 0)
