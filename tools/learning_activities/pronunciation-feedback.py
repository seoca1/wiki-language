#!/usr/bin/env/python3
"""Audio pronunciation feedback.

Compares user recording to target pronunciation.
Uses Web Speech API for reference and canvas for visualization.
"""
import json
import argparse
from pathlib import Path
from datetime import datetime

ROOT = Path("/Usersemelio/projects/Projects/Language") if Path("/Usersemelio").exists() else Path("/Users/emelio/projects/Projects/Language")
OUTPUT = ROOT / "exports" / "html-preview"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", help="Output HTML file")
    args = parser.parse_args()
    
    html = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Pronunciation Feedback</title>
<link rel="stylesheet" href="/assets/style.css">
<style>
body { font-family: system-ui; max-width: 700px; margin: 2em auto; padding: 1em; }
.target { padding: 1em; background: #ecf0f1; border-radius: 8px; font-size: 1.2em; text-align: center; margin: 1em 0; }
.controls { display: flex; gap: 0.5em; justify-content: center; margin: 1em 0; }
button { padding: 0.8em 1.5em; border: none; border-radius: 6px; background: #3498db; color: white; cursor: pointer; font-size: 1em; }
button.record { background: #e74c3c; }
button.match { background: #2ecc71; }
.feedback { padding: 1em; background: white; border-radius: 8px; margin: 1em 0; min-height: 100px; }
.score-big { font-size: 3em; font-weight: bold; text-align: center; }
.score-good { color: #2ecc71; }
.score-ok { color: #f39c12; }
.score-bad { color: #e74c3c; }
.waveform-overlay { 
  position: relative; height: 80px; background: #f8f9fa; border-radius: 8px;
  margin: 1em 0; overflow: hidden;
}
.target-wave, .user-wave { position: absolute; left: 0; right: 0; height: 40px; }
.target-wave { top: 0; background: rgba(52, 152, 219, 0.3); }
.user-wave { bottom: 0; background: rgba(231, 76, 60, 0.3); }
</style>
</head>
<body>
<h1>Pronunciation Feedback</h1>
<input type="text" id="word" value="hello" style="width:60%; padding:0.5em; font-size:1em;">
<select id="lang" style="padding:0.5em;">
  <option value="en-US">English</option>
  <option value="es-ES">Spanish</option>
  <option value="ja-JP">Japanese</option>
  <option value="ko-KR">Korean</option>
</select>
<button onclick="setTarget()" style="padding:0.5em 1em;">Set Target</button>

<div class="target" id="target">hello</div>

<div class="waveform-overlay">
  <div class="target-wave" id="targetWave"></div>
  <div class="user-wave" id="userWave"></div>
</div>

<div class="controls">
  <button class="record" id="recBtn" onclick="toggleRec()">🎤 Record</button>
  <button onclick="playTarget()">🔊 Target</button>
  <button onclick="playUser()">▶️ User</button>
</div>

<div class="feedback" id="feedback">
  <div class="score-big" id="score">-</div>
  <div id="feedbackText">Press Record to start</div>
</div>

<script>
let recognition = null;
let lastTranscript = '';
let userAudio = null;

const word = document.getElementById('word');
const lang = document.getElementById('lang');
const target = document.getElementById('target');
const recBtn = document.getElementById('recBtn');
const score = document.getElementById('score');
const feedbackText = document.getElementById('feedbackText');

function setTarget() {
  target.textContent = word.value;
  speakTarget();
}

function speakTarget() {
  if ('speechSynthesis' in window) {
    window.speechSynthesis.cancel();
    const u = new SpeechSynthesisUtterance(word.value);
    u.lang = lang.value;
    window.speechSynthesis.speak(u);
  }
}

function toggleRec() {
  const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!SR) { alert('Not supported'); return; }
  recognition = new SR();
  recognition.lang = lang.value;
  recognition.onresult = (e) => {
    lastTranscript = e.results[0][0].transcript;
    evaluate(lastTranscript);
  };
  recognition.onend = () => { recBtn.textContent = '🎤 Record'; };
  recognition.start();
  recBtn.textContent = '⏹ Stop';
}

function playUser() {
  if (lastTranscript && 'speechSynthesis' in window) {
    const u = new SpeechSynthesisUtterance(lastTranscript);
    u.lang = lang.value;
    window.speechSynthesis.speak(u);
  }
}

function evaluate(spoken) {
  const target_word = word.value.toLowerCase();
  const spoken_word = spoken.toLowerCase();
  const match = spoken_word === target_word;
  const similarity = calculateSimilarity(target_word, spoken_word);
  
  score.textContent = Math.round(similarity * 100) + '%';
  score.className = 'score-big ' + (similarity > 0.8 ? 'score-good' : similarity > 0.5 ? 'score-ok' : 'score-bad');
  
  if (match) {
    feedbackText.innerHTML = '<span style="color:#2ecc71">✓ Perfect match! Great pronunciation!</span>';
  } else {
    feedbackText.innerHTML = `Expected: <strong>${target_word}</strong><br>You said: <strong>${spoken_word}</strong><br>Similarity: ${Math.round(similarity * 100)}%`;
  }
}

function calculateSimilarity(a, b) {
  if (a === b) return 1.0;
  if (b.includes(a) || a.includes(b)) return 0.7;
  
  const setA = new Set(a.split(''));
  const setB = new Set(b.split(''));
  const inter = [...setA].filter(c => setB.has(c)).length;
  return inter / Math.max(setA.size, setB.size);
}

setTarget();
</script>
</body>
</html>"""
    
    target = Path(args.output) if args.output else OUTPUT / "pronunciation-feedback.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(html, encoding="utf-8")
    print(f"[OK] {target}")


if __name__ == "__main__":
    import sys
    sys.exit(main() or 0)
