# Language Learning Wiki - Agent Instructions

This wiki uses the LLM Wiki pattern to build a persistent, compounding knowledge base for language learning across English, Spanish, Japanese, and Korean.

## Architecture

### Three-layer structure

1. **raw/** - Immutable source materials organized by language
   - `English/` - English learning materials (textbooks, articles, novels)
   - `Spanish/` - Spanish learning materials
   - `Japanese/` - Japanese learning materials
   - `Korean/` - Korean learning materials
   - `Chinese/` - Chinese learning materials (added 2026-07 scaffolded as 5th language)
   - `assets/` - Images, audio clips, diagrams referenced in source materials

2. **wiki/** - LLM-maintained knowledge base, organized by language
   - `English/` - English learning wiki pages
   - `Spanish/` - Spanish learning wiki pages
   - `Japanese/` - Japanese learning wiki pages
   - `Korean/` - Korean learning wiki pages
   - `Chinese/` - Chinese learning wiki pages (zh, 5th language)
   - Each language wiki contains:
     - `index.md` - Master index of all pages in this language
     - `log.md` - Chronological record of ingests and updates
     - `vocabulary/` - Word and phrase pages
     - `expressions/` - Idioms and common expressions
     - `culture/` - Cultural context and usage notes
     - `sources/` - Summaries of processed materials
     - `study-plan/` - Personal study plans, weekly rotations, output workflows

3. **schema/** - This file and other configuration documents

## Core Operations

### Ingest

When a new source is added to `raw/{Language}/`:

1. Read the source material thoroughly
2. Discuss key learning points with the user
3. Create a summary page in `wiki/{Language}/sources/`
4. Extract and create/update pages for:
   - New vocabulary words (with definitions, examples, etymology)
   - Expressions and idioms (with usage context)
   - Cultural notes (customs, social conventions, historical context)
5. Update `index.md` with new entries
6. Append an entry to `log.md` with format: `## [YYYY-MM-DD] ingest | Source Title`

### Query

When the user asks questions:

1. Check `index.md` to find relevant pages
2. Read those pages and synthesize an answer
3. Provide citations to specific wiki pages
4. If the answer represents valuable synthesis, offer to save it as a new wiki page
5. Suggest related vocabulary or expressions the user might want to explore

### Lint

Periodically review wiki health:

- Check for contradictions between pages
- Identify orphan pages (no inbound links)
- Find vocabulary mentioned but lacking dedicated pages
- Suggest missing connections between related concepts
- Recommend new sources to fill knowledge gaps

## Page Format Standards

### Vocabulary Pages

> **Convention (effective 2026-07-10)**: 단어나 문장 하나를 별도 `.md`로 만들지 않는다.
> 모든 어휘는 `wiki/{Language}/vocabulary/{theme}.md` 같은 **테마 파일** 단위로 통합하며,
> 개별 단어는 그 안 `### {word}` 섹션이 된다. (게임 측 파이프라인은 `pipeline-to-game.md` 참조.)
> 보조 schema(`schema/vocabulary.md`)는 tier-2/3 필드를 다룰 때 참조.

Location: `wiki/{Language}/vocabulary/{theme}.md` (theme-file convention)

```markdown
# {Theme} — {한 줄 설명}

**Source:** [[{source-slug}]]
**Theme:** {Travel & Tourism, Food, ...}
**Level:** A1-A2 | JLPT N5 | TOPIK 2-3 | ...

{theme에 대한 간결한 설명 — 학습자가 어떤 단어들을 여기서 만나는지}

---

## {subgroup 1 (optional)}

### {word 1}

**Part of Speech:** 명사 (noun) / 동사 (verb) / ...

**Definition:** [뜻 또는 짧은 정의]

**Romaja / IPA / Pronunciación:** [...]

**Etymology:** [Origin and historical development if relevant]

#### Examples

- [Example sentence 1 — context: casual, with translation]
- [Example sentence 2 — context: formal, with translation]

#### Related Terms

- [[synonym]]
- [[antonym]]
- [[related-expression]]

#### Cultural Notes

[Any cultural context]

#### Sources

- [[source-title]]

---

### {word 2}

(같은 형식 반복)

---

## Pipeline Form (machine-readable)

> Generated for downstream consumers (`Game/lingotype/raw/{lang}_words.md`).
> Schema reference: `wiki/pipeline-to-game.md` L33-39, L92.
> The body above remains the human-readable form and is the source of truth.

```yaml
- { id: 001, display: "pasaporte", input: "pasaporte", meaning: "여권", level: "A1-A2", category: "viajes", source: "[[viajes]]" }
- { id: 002, display: "billete", input: "billete", meaning: "티켓", level: "A1-A2", category: "viajes", source: "[[viajes]]" }
# ...
```
```

게임 측 컨슈머(`Game/lingotype/`)는 위 YAML 부록의 각 entry를 그대로 가져가면 된다. `source: [[{theme-filename}]]` 한 줄이 5필드(display/input/meaning/level/category)와 함께 그 entry가 어느 page에서 왔는지 식별한다.

### Expression Pages

> **Convention (effective 2026-07-10, extending vocabulary principle)**:
> "단어나 문장 하나를 별도 `.md`로 만들지 않는다". 관용구도 다중 단어 expression 한 개당
> 페이지 한 개를 권장하지 않고, **테마 파일**로 통합:
> `wiki/{Language}/expressions/{theme}.md` 안에 `## {expression}` 섹션으로 들어간다.
> (관용구 예/메타는 단어보다 풍부할 수 있어 보조 schema `schema/expression.md` 의 tier-2/3 필드 활용)
> 예외: 게임 측 미션 대사(NPC 라인) 같이 다중 문장 + 강한 문맥 의존이면 별도 페이지가 자연스러움.

Location: `wiki/{Language}/expressions/{theme}.md` (theme-file convention)

```markdown
# {Theme — Expresiones / 表現 / 표현}

> **Theme:** {Daily Life / Romance & Relationships / ...}
> **Level:** A1-B2 (idioms)

{theme-intro}

---

## {expression 1}

**Literal Translation:** [Word-for-word translation if cross-language]

**Meaning:** [What it actually means in natural usage]

**Usage Context:** [When/how/where it's used]

**Pattern:** [Grammatical structure]

### Examples

- [Example 1 with context]
- [Example 2 with context]

### Cultural Background

[Historical or cultural origin if applicable]

### Similar Expressions

- [[related-expression-1]]
- [[related-expression-2]]

### Sources

- [[source-title]]

---

## {expression 2}

(같은 형식 반복)
```

### Culture Pages

Location: `wiki/{Language}/culture/{topic}.md`

```markdown
# {Cultural Topic}

**Overview:** [Brief description]

## Key Points

- [Important aspect 1]
- [Important aspect 2]

## Language Connections

- [[vocabulary-term-1]] - used in this context
- [[expression-1]] - related to this cultural practice

## Sources

- [[source-title-1]]
- [[source-title-2]]
```

### Source Summary Pages

Location: `wiki/{Language}/sources/{source-title}.md`

```markdown
# {Source Title}

**Type:** textbook/novel/article/blog  
**Date Added:** YYYY-MM-DD  
**Language Level:** beginner/intermediate/advanced

## Summary

[3-5 sentence overview of the source]

## Key Takeaways

- [Learning point 1]
- [Learning point 2]
- [Learning point 3]

## Vocabulary Extracted

- [[word1]]
- [[word2]]
- [[word3]]

## Expressions Extracted

- [[expression1]]
- [[expression2]]

## Cultural Insights

- [[culture-topic-1]]
- [[culture-topic-2]]

## Notes

[Any additional observations or context]
```

## Index Format

Location: `wiki/{Language}/index.md`

```markdown
# {Language} Learning Wiki - Index

Last updated: YYYY-MM-DD

## Vocabulary ({N} theme files)

- [[{theme-filename}]] - theme description + entry count
- [[{theme-filename-2}]] - ...

## Expressions ({N} theme files / {M} entries)

- [[{expressions-theme-filename}]] - brief meaning + entry count

## Culture ({count} entries)

- [[culture-topic1]] - one-line summary
- [[culture-topic2]] - one-line summary

## Sources ({count} processed)

- [[source1]] - type, date added
- [[source2]] - type, date added
```

## Log Format

Location: `wiki/{Language}/log.md`

Each entry starts with `## [YYYY-MM-DD]` for easy parsing.

```markdown
# {Language} Learning - Activity Log

## [2026-06-12] ingest | Spanish Grammar Textbook Chapter 3

- Added 15 vocabulary entries
- Created 3 expression pages
- Updated subjunctive mood culture page
- Summary: [[spanish-grammar-ch3]]

## [2026-06-11] query | Difference between ser and estar

- Created comparison page: [[ser-vs-estar]]
- Cross-referenced 8 existing vocabulary pages

## [2026-06-10] lint | Spanish wiki health check

- Found 3 orphan pages, added links
- Identified 5 mentioned terms lacking pages
- Added to ingest queue: preposition usage guide
```

## Multi-language Workflow

Since this wiki covers five languages (English, Spanish, Japanese, Korean, Chinese):

- Keep each language's wiki completely separate (no mixing)
- Use consistent page structures across all five languages for easy comparison
- When a user asks cross-language questions (e.g., "How do Spanish and Japanese express politeness?"), create a synthesis document and save it in the most relevant language wiki, or create a comparative analysis in `wiki/comparative/` (the cross-language comparative wiki holds 28+ pages spanning all 5 languages)
- The agent should be prepared to work in any of the five languages at any time

## Special Considerations

### For Japanese

- Include furigana (ruby text) for kanji when appropriate
- Track kanji separately with readings, meanings, and compounds
- Note politeness levels (casual, polite, honorific)
- Consider creating separate pages for different writing systems

### For Spanish

- Track regional variations (Spain vs. Latin America)
- Note gender and plural forms for nouns
- Include conjugation patterns for verbs
- Mark formal vs. informal usage (tú vs. usted)

### For English

- Note common learner mistakes and false cognates
- Track phrasal verbs separately (highly idiomatic)
- Include pronunciation guides for difficult words
- Mark register (formal, informal, slang)

### For Chinese (zh)

- **Tones**: Mandarin has 4 tones + neutral; tone pairs and tone sandhi are critical. Always include tone marks (mā/má/mǎ/mà/ma) in vocabulary entries.
- **Simplified vs Traditional**: Note which character set is used in raw sources; wiki pages may mix but should default to Simplified unless source is Traditional.
- **Measure words (量词)**: Always pair a noun with its classifier (个/条/只/张/本). Single-noun entries without their measure word are incomplete.
- **HSK level**: Use HSK 1-6 scale (not JLPT/TOPIK). Beginner is HSK 1-2, intermediate 3-4, advanced 5-6.
- **Characters ≠ words**: Chinese is logographic; one character may map to a multi-character word. Track both the character and the word-level unit.
- **Pinyin notation**: Use tone-marked pinyin (nǐ hǎo) for readability; numbered pinyin (ni3 hao3) only in YAML `input` fields for the game pipeline.
- **Bilingual cross-references**: Chinese vocabulary pages often benefit from `zh ↔ KO` parallel display (user is a Korean speaker).

### For Korean

- Include hanja (한자) for Sino-Korean words when useful for etymology
- Track speech levels / politeness styles (해체, 해요체, 합쇼체, 하소서체)
- Note honorific (존댓말) vs. casual (반말) usage
- Distinguish word origin: pure Korean (순 우리말), Sino-Korean (한자어), loanword (외래어)
- Mark irregular conjugations (불규칙 활용, e.g., ㄷ/ㅂ/ㅅ/ㅎ/르)
- Note particle usage (조사) and how it shifts with formality

## Tools and Integration

- **Obsidian**: Primary interface for browsing the wiki
  - Use graph view to visualize connections
  - Enable backlinks panel to see cross-references
  - Consider Dataview plugin for dynamic queries

- **Search**: At small scale, use index.md navigation. As the wiki grows, consider adding a dedicated search tool like qmd for hybrid search.

## Downstream Consumers (콘텐츠 파이프라인)

`Language/` 위키는 학습 콘텐츠의 **단일 진실 공급원**이다. 다른 프로젝트가 이 콘텐츠를 끌어다 쓸 수 있다. 현재 알려진 다운스트림:

| 다운스트림 | 위치 | 소비 형태 |
| --- | --- | --- |
| `lingotype` 게임 | `Game/lingotype/` | `wiki/{Language}/vocabulary/` 를 게임 코퍼스(`raw/{lang}_words.md`)의 `source` 인용 형태로 큐레이션 |

### 규칙

1. **게임이 필요로 하는 콘텐츠가 Language에 없으면 Language에 먼저 추가**한다. `raw/{Language}/` 에 출처를 추가하고 인제스트하여 `wiki/{Language}/vocabulary/` 페이지를 만든 다음 게임으로 반영한다.
2. **모든 vocabulary 페이지는 게임 인용이 가능하도록** `display`, `input`(언어별 변환이 필요할 경우), `meaning`, `level`/`category` 메타를 명시한다.
3. **Language 위키는 다운스트림 없이도 독립적으로 동작**한다. 게임은 Language에 의존하지만, Language는 게임에 의존하지 않는다.
4. 자세한 파이프라인: `wiki/pipeline-to-game.md`

## Principles

1. **Incremental growth**: Add sources one at a time, integrate thoroughly
2. **Cross-referencing**: Every page should link to related pages
3. **Consistent structure**: Follow the page format standards strictly
4. **User-driven curation**: The user chooses what to learn; the agent maintains the structure
5. **Compounding knowledge**: Each new source enriches existing pages and creates new ones
6. **Never redundant**: If information exists on a page, link to it rather than repeating it

## User's Learning Focus

Based on user preferences:
- **Materials**: Original books (novels, non-fiction), textbooks, web articles/blogs
- **Key elements to track**: Vocabulary, expressions/idioms, cultural context
- **Languages**: English, Spanish, Japanese, Korean, Chinese (equal priority; Chinese added 2026-07 as 5th language)

The agent should prioritize these elements when processing sources and suggest related materials that align with these preferences.
