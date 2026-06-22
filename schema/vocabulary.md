# Vocabulary Page Schema (Extended)

**Base spec**: see `AGENTS.md` §"Vocabulary Pages"
**This document**: 학습 친화 필드 추가 (pronunciation, memory aid, common mistakes, dialogue, register, frequency)

## Full Template

```markdown
# {word}

**Part of Speech:** noun / verb / adjective / adverb / particle / counter / etc.
**Level:** A1/A2/B1/B2/C1/C2 (CEFR for EN/ES) | N5/N4/N3/N2/N1 (JLPT for JP) | TOPIK I/II 1-6 (KR)

**Definition:** [Clear, concise English/meaning]

**Etymology:** [Origin and historical development if relevant — Latin roots, 한자, etc.]

**Pronunciation:**
- IPA: /.../
- Syllables: word-by-syllable
- Stress: 1st / 2nd / 3rd (강세 위치)
- For JP: 読み方 (hiragana)
- For ES: tilde/stress mark location
- For KR: romanization (Revised Romanization)
- Audio: 🔊 [optional link to TTS / audio file]

**Memory Tip:** [Mnemonic, story, image association, or learning trick]
- EN example: "Beautiful" → French "beau" (handsome) + "ful"
- JP example: 学校 (がっこう) → "学" (study) + "校" (school)
- KR example: 한국 (han-gug) → "han" (one, great) + "gug" (country)

**Common Mistakes:**
- ❌ [What learners often get wrong]
- ✅ [Correct form]
- Note: [Why this matters — register, context, grammar rule]

**Register:** formal | semi-formal | casual | slang | literary
**Frequency:** ⭐ / ⭐⭐ / ⭐⭐⭐ / ⭐⭐⭐⭐ / ⭐⭐⭐⭐⭐ (in everyday speech)

**Visual:** [Optional: image of 한자 decomposition, or ASCII art, or table]

## Examples

- [Example sentence 1 — context: casual, with translation]
- [Example sentence 2 — context: formal, with translation]
- [Example sentence 3 — context: business, with translation]

## Mini-Dialogue

```
A: [Contextual line 1]   ← [translation]
B: [Response 1]          ← [translation]
A: [Follow-up]           ← [translation]
B: [Reaction]            ← [translation]
```

## Related Terms

- [[synonym1]] — different register or nuance
- [[antonym1]]
- [[related-expression]]
- [[cognate-language]] — e.g., Latin root shared with another word

## Cultural Notes

[Any cultural context, body language, social norms — what native speakers know that learners don't]

## Sources

- [[source-title]] (page X)
- [[grammar-reference]]
```

## Language-Specific Notes

### English (EN)
- Always include IPA + stress + syllables
- Phrasal verbs: separate `vocabulary/{verb}.md` from `expressions/{verb-particle}.md`
- Register highly important (formal/informal/slang vary widely)
- False friends with other languages: flag in Common Mistakes

### Spanish (ES)
- Gender + plural forms in Definition: "el libro (m, libros)"
- Conjugation patterns for verbs: "hablar → hablo, hablas, habla..."
- Tú vs usted vs vosotros: mark in Register
- Regional variations: "vosotros" (Spain) vs "ustedes" (LatAm)
- IPA: /θ/ for Spain, /s/ for LatAm — note in Pronunciation

### Japanese (JP)
- 読み方: hiragana reading
- Kanji breakdown under Visual
- Verb groups (Group 1 / 2 / irregular) for verbs
- Politeness level:  casual (タメ口) / polite (です・ます) / honorific (敬語) / humble (謙譲語)
- Counter words (助数詞) for nouns: 一人 (ひとり), 一個 (いっこ)
- Pitch accent where useful

### Korean (KR)
- Revised Romanization: e.g., "한국" → "hangug" (NOT "han-guk")
- Speech level: 해요체 (casual polite) / 합쇼체 (formal) / 해체 (intimate)
- Word origin tag: 순 우리말 (pure Korean) / 한자어 (Sino-Korean) / 외래어 (loanword)
- Irregular conjugations: ㄷ/ㅂ/ㅅ/ㅎ/르 불규칙
- Particle shifts: 이/가, 을/를, 은/는 depend on final consonant

## Field Optionality

| Field | Tier 1 (essential) | Tier 2 (recommended) | Tier 3 (deep) |
| --- | :---: | :---: | :---: |
| Part of Speech | ✅ | | |
| Level | ✅ | | |
| Definition | ✅ | | |
| Pronunciation | ✅ | | |
| Examples | ✅ (3+ each) | | |
| Related Terms | ✅ (2+) | | |
| Sources | ✅ (1+) | | |
| Memory Tip | | ✅ | |
| Common Mistakes | | ✅ | |
| Register | | ✅ | |
| Mini-Dialogue | | | ✅ |
| Etymology | | | ✅ |
| Visual | | | ✅ |
| Cultural Notes | | | ✅ |

**Tier 1** is enough for game-level usage (typing the word correctly).
**Tier 2** unlocks daily lessons at 🟡 Standard level.
**Tier 3** unlocks 🔴 Deep lessons with dialogues + culture.
