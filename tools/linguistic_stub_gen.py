#!/usr/bin/env python3
"""Per-language stub generator for Language vault broken wikilinks.

Generates stub pages in correct language directories based on detected language.

Strategy:
- Group broken stems by detected language (KO/EN/ES/JA/ZH/Unknown)
- Drop each group into corresponding wiki/<lang>/vocabulary/ (or expressions/)
- Use frontmatter pattern from existing pages
- Skip non-language-tagged stems
"""
from __future__ import annotations
import re
import sys
from collections import defaultdict
from pathlib import Path
import argparse

ROOT = Path(__file__).resolve().parents[2]
EXCLUDE = {'.git','node_modules','.obsidian','.vite','.cache','.mypy_cache','.pytest_cache','.ruff_cache','.omo','.openclaw'}
WIKILINK = re.compile(r'(?<!`)\[\[([^\]|#]+)')
CODE = re.compile(r'```.*?```', re.DOTALL)


def detect_language_from_path(source_path: str) -> str:
    """Detect target wiki language from file path containing wikilink."""
    sp = source_path.lower()
    if '/wiki/chinese' in sp or '/wiki/zh/' in sp: return 'Chinese'
    if '/wiki/spanish' in sp or '/wiki/es/' in sp: return 'Spanish'
    if '/wiki/english' in sp or '/wiki/en/' in sp: return 'English'
    if '/wiki/korean' in sp or '/wiki/ko/' in sp: return 'Korean'
    if '/wiki/japanese' in sp or '/wiki/jp/' in sp or '/wiki/ja/' in sp: return 'Japanese'
    if '/raw/chinese/' in sp or '/raw/zh/' in sp: return 'Chinese'
    if '/raw/spanish/' in sp or '/raw/es/' in sp: return 'Spanish'
    if '/raw/english/' in sp or '/raw/en/' in sp: return 'English'
    if '/raw/korean/' in sp or '/raw/ko/' in sp: return 'Korean'
    if '/raw/japanese/' in sp or '/raw/jp/' in sp or '/raw/ja/' in sp: return 'Japanese'
    if '/session_summary' in sp: return 'Unknown'
    return 'Unknown'


def classify_subdir(stem: str, lang: str) -> str:
    """Decide vocabulary/ vs expressions/ for stub placement."""
    # Expressions tend to be multi-word with particles (ko: ~해/요 endings, ja: です)
    if lang == 'Korean' and any(c in stem for c in ['요','니다','까','면']): return 'expressions'
    if lang == 'Japanese' and any(c in stem for c in ['です','ます','した']): return 'expressions'
    # Loose heuristic: 1-2 chars → expressions (interjections), else vocabulary
    return 'vocabulary'


def detect_lang_from_stem(stem: str) -> str | None:
    """Heuristic: detect target language from the stem itself (CJK ranges)."""
    if all(0xAC00 <= ord(c) <= 0xD7AF or c in '·' for c in stem): return 'Korean'
    if all(0x3040 <= ord(c) <= 0x309F or 0x30A0 <= ord(c) <= 0x30FF for c in stem): return 'Japanese'
    if all(0x4E00 <= ord(c) <= 0x9FFF or 0x3000 <= ord(c) <= 0x303F for c in stem): return 'Chinese'
    if any(0xC0 <= ord(c) <= 0xFF for c in stem): return 'Spanish'
    return None


def collect():
    files = [p for p in ROOT.rglob('*.md') if not any(e in p.parts for e in EXCLUDE)]
    stem_set = {p.stem: p for p in files}

    referencing = defaultdict(set)
    for f in files:
        txt = CODE.sub('', f.read_text(errors='ignore'))
        for w in WIKILINK.findall(txt):
            w = w.strip()
            if not w or w in {'wikilink','...','…'}: continue
            if '{' in w or w in {'stem','theme','word'}: continue
            try: ok = (f.parent / w).resolve().exists()
            except: ok = False
            if not ok: ok = Path(w).stem in stem_set
            if not ok:
                referencing[w].add(str(f.relative_to(ROOT)))

    return referencing


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--inventory', action='store_true')
    parser.add_argument('--create-stubs', action='store_true', help='Create per-language stub pages')
    parser.add_argument('--limit', type=int, default=0, help='Limit to N stubs')
    args = parser.parse_args()

    referencing = collect()

    if args.inventory:
        lang_count = defaultdict(int)
        for s, paths in referencing.items():
            lang = detect_lang_from_stem(s)
            if not lang:
                # infer from sources
                for p in paths:
                    l = detect_language_from_path(p)
                    if l != 'Unknown':
                        lang = l
                        break
            lang_count[lang or 'Unknown'] += 1
        print(f'## Broken Wikilink Inventory (by detected language)')
        print()
        print(f'총 **{sum(lang_count.values())}개** unique stem')
        print()
        print('| Language | Count |')
        print('|---|---:|')
        for lang in sorted(lang_count.keys()):
            print(f'| {lang} | {lang_count[lang]} |')
        return 0

    if args.create_stubs:
        # Group by detected language → distribute to wiki/<lang>/vocabulary (or expressions/)
        # Skip Unknown stems — those are session-summary artifacts
        buckets = defaultdict(list)
        for stem, paths in sorted(referencing.items()):
            lang = detect_lang_from_stem(stem)
            if not lang:
                for p in paths:
                    l = detect_language_from_path(p)
                    if l != 'Unknown': lang = l; break
            if not lang or lang == 'Unknown':
                # attempt to detect from stem
                lang = detect_lang_from_stem(stem) or 'Unknown'
            if lang == 'Unknown':
                continue
            subdir = classify_subdir(stem, lang)
            buckets[(lang, subdir)].append((stem, paths))

        total = 0
        per_lang_count = defaultdict(int)
        for (lang, subdir), items in sorted(buckets.items()):
            if args.limit and total >= args.limit:
                break
            target_dir = ROOT / 'wiki' / lang / subdir
            target_dir.mkdir(parents=True, exist_ok=True)
            for stem, paths in items:
                if args.limit and total >= args.limit:
                    break
                safe = stem.replace('/', '-')
                target = target_dir / f'{safe}.md'
                if target.exists():
                    continue  # don't overwrite
                target.write_text(render_stub(stem, lang, subdir, paths))
                per_lang_count[lang] += 1
                total += 1
        print(f'Created {total} stubs across {len(per_lang_count)} languages:')
        for lang, c in sorted(per_lang_count.items()):
            print(f'  {lang}: {c}')
        return 0

    return 0


def render_stub(stem: str, lang: str, subdir: str, sources: set) -> str:
    front = f"""---
title: "{stem}"
language: "{lang}"
category: "{subdir}"
status: stub
ingested_from: "auto-stub-gen 2026-07-19 (Phase A & B)"
source_references: {len(sources)}
---

# {stem}

> **Stub page** — auto-generated to resolve broken wikilink. Content
> pending ingestion.
> Sources: {', '.join(sorted(sources)[:3])}{' ...' if len(sources) > 3 else ''}

"""
    return front


if __name__ == '__main__':
    sys.exit(main())
