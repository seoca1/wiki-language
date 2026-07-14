# Chinese Study Plan

## Status

Placeholder / schema-stub. The Chinese wiki needs `study-plan/` to satisfy `Language/schema/AGENTS.md` (each language's seven required subdirectories), so this stub exists for structural completeness. No actual Chinese learning plan has been authored yet.

## Why this stub

Chinese is the 5th language in the vault (added 2026-07-13), scaffolded with empty vocabulary / expressions / culture / sources. Once a real study plan is in scope, this stub gets replaced with the actual files.

## Inherited convention (from `wiki/Spanish/study-plan/weekly-plan.md`)

When the Chinese plan is eventually authored, follow the same shape as the other languages:

- **Weekly cycle** with microlearning (weekday, ~30 min) + deep work (weekend, ~60 min)
- **4-week rotation**: one grammar axis + one vocabulary theme + one output deliverable per cycle
- **Output obligation**: weekly Chinese 5-sentence summary shipped to a public blog draft
- **Level bracket**: HSK 1 → HSK 6 documented at the file head
- **Date started** + commit interval explicit

## Open decisions (Chinese-specific)

- **Input method**: pinyin input (병음) / zhuyin (注音符號, 대만) / direct hanzi (한자 직입력) — affects how the typing game `Game/typing_language/` should treat Chinese keystrokes
- **Script focus**: Simplified (大陆) vs Traditional (繁體, 台灣/홍콩) — these diverge significantly in vocabulary, characters, and grammar
- **Tone pedagogy**: tone-pair drills (声调组合) are a Chinese-specific axis that no other language in the vault needs
- **Measure words (量词)**: a Chinese-specific grammar axis that the 4-week rotation should reserve a slot for

## Templates

Two files referenced by `schema/AGENTS.md`:

- `weekly-plan.md` — perpetual rolling 4-week cycle
- `blog-output.md` — collected weekly blog draft outputs

Both will be added once the user kicks off a Chinese study plan session.

## See also

- `Language/schema/AGENTS.md` (structural spec)
- `Language/wiki/Spanish/study-plan/weekly-plan.md` (precedent)
- `Language/wiki/English/study-plan/README.md` (English stub, same shape)
