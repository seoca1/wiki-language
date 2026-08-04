#!/usr/bin/env/python3
"""Native language support.

Generates language preference handling for UI.
"""
import json
import argparse
from pathlib import Path
from datetime import datetime

ROOT = Path("/Usersemelio/projects/Projects/Language") if Path("/Usersemelio").exists() else Path("/Users/emelio/projects/Projects/Language")
OUTPUT = ROOT / "exports" / "html-preview"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default=str(ROOT / "exports" / "native-lang-support.html"))
    args = parser.parse_args()
    
    LANG_OPTIONS = {
        "en": "English",
        "es": "Spanish",
        "ja": "Japanese",
        "ko": "Korean",
    }
    
    html = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Native Language Support</title>
<link rel="stylesheet" href="/assets/style.css">
<style>
body { font-family: system-ui; max-width: 600px; margin: 2em auto; padding: 1em; }
.lang-picker { display: grid; grid-template-columns: repeat(2, 1fr); gap: 1em; margin: 2em 0; }
.lang-btn { 
  padding: 1.5em; border: 2px solid #3498db; border-radius: 8px; 
  background: white; cursor: pointer; text-align: center;
}
.lang-btn:hover { background: #ecf0f1; }
.lang-btn.active { background: #3498db; color: white; }
.native-info { background: #f8f9fa; padding: 1em; border-radius: 8px; margin: 1em 0; }
</style>
</head>
<body>
<h1>Select Your Native Language</h1>
<p>Choose your native language for translations and UI</p>

<div class="lang-picker" id="picker"></div>

<div class="native-info" id="info"></div>

<h2>Benefits</h2>
<ul>
<li>UI in your language</li>
<li>Definitions translated to your language</li>
<li>Examples in your language</li>
</ul>

<script>
const LANGUAGES = {
  "en": { "name": "English", "flag": "🇬🇧" },
  "es": { "name": "Spanish", "flag": "🇪🇸" },
  "ja": { "name": "Japanese", "flag": "🇯🇵" },
  "ko": { "name": "Korean", "flag": "🇰🇷" }
};

function renderPicker() {
  const picker = document.getElementById("picker");
  const saved = localStorage.getItem("native_lang") || "en";
  picker.innerHTML = Object.entries(LANGUAGES).map(([code, data]) =>
    `<button class="lang-btn ${code === saved ? "active" : ""}" data-code="${code}">
      <div style="font-size:2em">${data.flag}</div>
      <div>${data.name}</div>
    </button>`
  ).join("");
  picker.querySelectorAll(".lang-btn").forEach(btn => {
    btn.onclick = () => {
      const code = btn.dataset.code;
      localStorage.setItem("native_lang", code);
      document.querySelectorAll(".lang-btn").forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      updateInfo(code);
    };
  });
  updateInfo(saved);
}

function updateInfo(code) {
  const info = document.getElementById("info");
  info.innerHTML = `<strong>Selected:</strong> ${LANGUAGES[code].name}<br>All UI text, definitions, and examples will be optimized for this language.`;
}

renderPicker();
</script>
</body>
</html>"""
    
    target = Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(html, encoding="utf-8")
    print(f"[OK] {target}")


if __name__ == "__main__":
    import sys
    sys.exit(main() or 0)
