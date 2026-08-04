#!/usr/bin/env/python3
"""AI pronunciation scorer.

Uses LLM to score pronunciation attempts based on phoneme analysis.
"""
import json
import argparse
import urllib.request
import urllib.error
from pathlib import Path
from datetime import datetime

ROOT = Path("/Usersemelio/projects/Projects/Language") if Path("/Usersemelio").exists() else Path("/Users/emelio/projects/Projects/Language")
CONFIG_FILE = ROOT / "llm_config.json"


def load_config():
    if CONFIG_FILE.exists():
        return json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
    return {"base_url": "http://localhost:11434", "model": "qwen3.5:9b"}


def query_ollama(prompt, config):
    try:
        data = json.dumps({"model": config["model"], "prompt": prompt, "stream": False}).encode("utf-8")
        req = urllib.request.Request(
            f"{config['base_url']}/api/generate",
            data=data,
            headers={"Content-Type": "application/json"},
        )
        with urllib.request.urlopen(req, timeout=10) as response:
            return json.loads(response.read().decode("utf-8")).get("response", "").strip()
    except Exception as e:
        return f"[Error: {e}]"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", required=True, help="Target word")
    parser.add_argument("--attempt", required=True, help="User's attempt")
    parser.add_argument("--lang", default="en-US")
    parser.add_argument("--output", default=str(ROOT / "exports" / "ai-pron-score.md"))
    args = parser.parse_args()
    
    config = load_config()
    prompt = f"""Score the pronunciation attempt for the target word '{args.target}' in {args.lang}.
The user said: '{args.attempt}'.
Provide a score (0-100), phoneme-level feedback, and improvement tips.
Format: Score, Feedback, Tips"""
    
    response = query_ollama(prompt, config)
    
    md = []
    md.append(f"# AI Pronunciation Score")
    md.append("")
    md.append(f"**Target:** {args.target}")
    md.append(f"**Attempt:** {args.attempt}")
    md.append(f"**Language:** {args.lang}")
    md.append(f"**Generated:** {datetime.now().isoformat()}")
    md.append("")
    md.append("## Assessment")
    md.append("")
    md.append(response)
    md.append("")
    
    target = Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n".join(md), encoding="utf-8")
    print(f"[OK] {target}")


if __name__ == "__main__":
    import sys
    sys.exit(main() or 0)
