#!/usr/bin/env/python3
"""Vocabulary quiz generator v3.

Generates multiple question types: MCQ, fill-in-blank, matching.
"""
import json
import argparse
import random
import re
from pathlib import Path
from datetime import datetime
from collections import defaultdict

ROOT = Path("/Usersemelio/projects/Projects/Language") if Path("/Usersemelio").exists() else Path("/Users/emelio/projects/Projects/Language")
LANGS = ["English", "Spanish", "Japanese", "Korean"]
SECTION = "## Cross-Language Equivalents"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--lang", default="English")
    parser.add_argument("--count", type=int, default=20)
    parser.add_argument("--types", nargs="+", default=["mcq", "fill", "match"], choices=["mcq", "fill", "match"])
    parser.add_argument("--output", default=str(ROOT / "exports" / "quiz-v3.json"))
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    
    random.seed(args.seed)
    vdir = ROOT / "wiki" / args.lang / "vocabulary"
    if not vdir.exists():
        return 1
    
    entries = []
    for f in vdir.glob("*.md"):
        if "-vocabulary" in f.name or f.stem.startswith("index"):
            continue
        text = f.read_text(encoding="utf-8", errors="ignore")
        if "_TODO_" in text:
            continue
        m = re.match(r"^# (.+)$", text, re.MULTILINE)
        m_def = re.search(r"\*\*Definition:\*\* (.+?)$", text, re.MULTILINE)
        if m and m_def:
            entries.append({
                "word": m.group(1).strip(),
                "definition": m_def.group(1).strip(),
            })
    
    random.shuffle(entries)
    selected = entries[:args.count]
    
    questions = []
    for i, e in enumerate(selected, 1):
        qtype = random.choice(args.types)
        
        if qtype == "mcq":
            correct = e["definition"]
            wrong_pool = [x["definition"] for x in entries if x != e]
            wrong = random.sample(wrong_pool, min(3, len(wrong_pool)))
            choices = [correct] + wrong[:3]
            random.shuffle(choices)
            questions.append({
                "id": i,
                "type": "mcq",
                "word": e["word"],
                "prompt": f"What is the meaning of '{e['word']}'?",
                "choices": choices,
                "answer": correct,
            })
        
        elif qtype == "fill":
            questions.append({
                "id": i,
                "type": "fill",
                "prompt": f"Translate: {e['word']}",
                "answer": e["definition"],
            })
        
        elif qtype == "match":
            # Match pairs
            pair = selected[i-1:i+2] if i + 1 < len(selected) else selected[-2:]
            if len(pair) >= 2:
                questions.append({
                    "id": i,
                    "type": "match",
                    "prompt": "Match words with definitions:",
                    "pairs": [{"word": p["word"], "def": p["definition"]} for p in pair],
                })
    
    output = {
        "lang": args.lang,
        "generated_at": datetime.now().isoformat(),
        "count": len(questions),
        "types": args.types,
        "questions": questions,
    }
    
    target = Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[OK] {target} ({len(questions)} questions)")


if __name__ == "__main__":
    import sys
    sys.exit(main() or 0)
