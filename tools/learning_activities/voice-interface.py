#!/usr/bin/env/python3
"""Voice-based learning interface.

Generates voice-controlled learning UI with TTS + speech recognition.
"""
import json
import argparse
from pathlib import Path
from datetime import datetime

ROOT = Path("/Usersemelio/projects/Projects/Language") if Path("/Usersemelio").exists() else Path("/Users/emelio/projects/Projects/Language")
OUTPUT = ROOT / "exports" / "html-preview"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default=str(ROOT / "exports" / "voice-interface.html"))
    args = parser.parse_args()
    
    html = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Voice Learning Interface</title>
<link rel="stylesheet" href="/assets/style.css">
<style>
body { font-family: system-ui; max-width: 700px; margin: 2em auto; padding: 1em; text-align: center; }
.card { 
  background: white; padding: 2em; border-radius: 16px; 
  margin: 1em 0; box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}
.word { font-size: 3em; font-weight: bold; margin: 1em 0; }
.controls { display: flex; gap: 0.5em; justify-content: center; margin: 1em 0; flex-wrap: wrap; }
button {
  padding: 1em 1.5em; border: none; border-radius: 8px; 
  background: #3498db; color: white; cursor: pointer; font-size: 1em;
}
button.mic { background: #e74c3c; }
button.mic.listening { animation: pulse 1s infinite; }
.status { padding: 1em; margin: 1em 0; background: #f8f9fa; border-radius: 8px; min-height: 50px; }
.vocab-list { text-align: left; }
.vocab-item { 
  padding: 0.5em; border-bottom: 1px solid #ecf0f1; cursor: pointer;
  display: flex; justify-content: space-between; align-items: center;
}
.vocab-item:hover { background: #f8f9fa; }
</style>
</head>
<body>
<h1>🎤 Voice Learning</h1>
<p>Say "next" for next card, "repeat" to hear again, "translate" for translation</p>

<div class="vocab-list" id="vocabList"></div>

<div class="card" id="cardDisplay" style="display:none;">
  <div class="word" id="word">-</div>
  <div id="definition">-</div>
</div>

<div class="controls">
  <button class="mic" id="micBtn" onclick="toggleMic()">🎤 Voice</button>
  <button onclick="nextCard()">Next Card</button>
  <button onclick="speakWord()">🔊 Speak</button>
</div>

<div class="status" id="status">Say a command to begin</div>

<script>
const VOCAB = [
  { word: "hello", def: "a greeting" },
  { word: "water", def: "a clear liquid" },
  { word: "food", def: "what you eat" },
  { word: "family", def: "related people" },
  { word: "friend", def: "person you trust" },
];

let currentIdx = 0;
let recognition = null;
let isListening = false;
let currentWord = null;

function renderVocab() {
  const list = document.getElementById("vocabList");
  list.innerHTML = VOCAB.map((v, i) => 
    `<div class="vocab-item" onclick="showCard(${i})">
      <span>${v.word}</span>
      <span style="color:#666">${v.def}</span>
    </div>`
  ).join("");
  document.getElementById("cardDisplay").style.display = "block";
}

function showCard(i) {
  currentIdx = i || 0;
  currentWord = VOCAB[currentIdx];
  document.getElementById("word").textContent = currentWord.word;
  document.getElementById("definition").textContent = currentWord.def;
  speakWord();
}

function nextCard() {
  currentIdx = (currentIdx + 1) % VOCAB.length;
  showCard(currentIdx);
}

function speakWord() {
  if (currentWord && 'speechSynthesis' in window) {
    const u = new SpeechSynthesisUtterance(currentWord.word);
    u.lang = 'en-US';
    u.rate = 0.7;
    window.speechSynthesis.speak(u);
  }
}

function toggleMic() {
  if (isListening) {
    recognition?.stop();
    isListening = false;
    document.getElementById("micBtn").classList.remove("listening");
    return;
  }
  const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!SR) { alert('Not supported'); return; }
  recognition = new SR();
  recognition.continuous = true;
  recognition.interimResults = false;
  recognition.onresult = (e) => {
    const transcript = e.results[e.results.length-1][0].transcript.toLowerCase().trim();
    processCommand(transcript);
  };
  recognition.onend = () => {
    if (isListening) recognition.start();
  };
  recognition.start();
  isListening = true;
  document.getElementById("micBtn").classList.add("listening");
}

function processCommand(cmd) {
  const status = document.getElementById("status");
  if (cmd.includes("next") || cmd.includes("skip")) {
    nextCard();
    status.textContent = "🎤 → next card";
  } else if (cmd.includes("repeat") || cmd.includes("again")) {
    speakWord();
    status.textContent = "🎤 → repeating";
  } else if (cmd.includes("translate") || cmd.includes("meaning")) {
    status.textContent = `🎤 → ${currentWord.word} means "${currentWord.def}"`;
    speakWord();
  } else {
    status.textContent = `🎤 Heard: "${cmd}" (try "next", "repeat", "translate")`;
  }
}

renderVocab();
showCard(0);
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
