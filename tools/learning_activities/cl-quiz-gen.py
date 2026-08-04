#!/usr/bin/env/python3
"""Cross-language quiz generation.

Generates quizzes across multiple languages.
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
    parser.add_argument("--output", default=str(ROOT / "exports" / "cl-quiz.json"))
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    
    random.seed(args.seed)
    
    vdir = ROOT / "wiki" / args.lang / "vocabulary"
    if not vdir.exists():
        return 1
    
    # Build pool of cross-language concepts
    concepts = []
    for f in vdir.glob("*.md"):
        if "-vocabulary" in f.name or f.stem.startswith("index"):
            continue
        text = f.read_text(encoding="utf-8", errors="ignore")
        if "_TODO_" in text:
            continue
        m = re.match(r"^# (.+)$", text, re.MULTILINE)
        m_def = re.search(r"\*\*Definition:\*\* (.+?)$", text, re.MULTILINE)
        m_xl = re.search(rf"{SECTION}\s*\n([\s\S]*?)(?=\n## |\Z)", text)
        if not (m and m_def and m_xl):
            continue
        
        translations = []
        for line in m_xl.group(1).split("\n"):
            m_l = re.search(r"\*\*(\w+)\*\*:\s*\[\[([^\]]+)\]\]", line)
            if m_l:
                translations.append({"lang": m_l.group(1), "stem": m_l.group(2).strip()})
        
        if len(translations) >= 2:
            concepts.append({
                "word": m.group(1).strip(),
                "definition": m_def.group(1).strip(),
                "translations": translations,
            })
    
    random.shuffle(concepts)
    selected = concepts[:args.count]
    
    # Generate questions
    questions = []
    for i, c in enumerate(selected, 1):
        # Multiple choice: pick the correct answer + 3 wrong
        correct = c["translations"][0] if c["translations"] else None
        if not correct:
            continue
        
        # Get wrong answers from other concepts
        wrong_pool = [t["stem"] for oc in concepts if oc != c for t in oc.get("translations", [])]
        wrong = random.sample(wrong_pool, min(3, len(wrong_pool)))
        choices = [correct["stem"]] + wrong[:3]
        random.shuffle(choices)
        
        questions.append({
            "id": i,
            "word": c["word"],
            "definition": c["definition"],
            "target_lang": correct["lang"],
            "target_stem": correct["stem"],
            "choices": choices,
            "answer": correct["stem"],
        })
    
    output = {
        "lang": args.lang,
        "generated_at": datetime.now().isoformat(),
        "count": len(questions),
        "questions": questions,
    }
    
    target = Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[OK] {target} ({len(questions)} questions)")


if __name__ == "__main__":
    import sys
    sys.exit(main() or 0)
