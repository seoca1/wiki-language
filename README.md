# Language Learning Wiki

A personal knowledge base for learning English, Spanish, Japanese, and Korean using the LLM Wiki pattern.

## Structure

```
Language/
├── raw/                    # Source materials (immutable)
│   ├── English/           # English learning materials
│   ├── Spanish/           # Spanish learning materials
│   ├── Japanese/          # Japanese learning materials
│   ├── Korean/            # Korean learning materials
│   └── assets/            # Images, audio, diagrams
│
├── wiki/                   # LLM-maintained knowledge base
│   ├── English/           # English learning wiki
│   │   ├── index.md       # Master index
│   │   ├── log.md         # Activity log
│   │   ├── vocabulary/    # Word pages
│   │   ├── expressions/   # Idiom and phrase pages
│   │   ├── culture/       # Cultural context pages
│   │   └── sources/       # Source summaries
│   │
│   ├── Spanish/           # Spanish learning wiki (same structure)
│   ├── Japanese/          # Japanese learning wiki (same structure)
│   └── Korean/            # Korean learning wiki (same structure)
│
└── schema/
    └── AGENTS.md          # Instructions for LLM agents
```

## How It Works

This is not a traditional flashcard or vocabulary app. Instead, it's a **persistent, compounding knowledge base** that grows with every source you add.

### The LLM Wiki Pattern

1. **You add sources** to `raw/{Language}/` (textbooks, articles, novels, blog posts)
2. **The LLM ingests** each source, extracting vocabulary, expressions, and cultural insights
3. **The wiki grows** - new pages are created, existing pages are updated and cross-referenced
4. **You explore** - ask questions, browse connections, discover patterns
5. **Knowledge compounds** - each new source enriches what you've already learned

### Three Key Operations

**Ingest**: Process a new source and integrate it into the wiki
```
"Please ingest the Spanish textbook chapter I added to raw/Spanish/"
```

**Query**: Ask questions and get answers with citations
```
"What's the difference between ser and estar in Spanish?"
"Show me all the expressions related to politeness in Japanese"
```

**Lint**: Health-check the wiki and find gaps
```
"Run a lint check on the English wiki"
```

## Getting Started

1. Add your first source to `raw/{Language}/`
2. Open a session with your LLM agent
3. Tell it to read `schema/AGENTS.md` to understand the system
4. Ask it to ingest your source
5. Browse the resulting wiki pages in Obsidian or your markdown editor

## Recommended Tools

- **Obsidian**: Best way to browse the wiki
  - Graph view shows connections between concepts
  - Backlinks panel shows related pages
  - Live preview makes it easy to follow links
  
- **Obsidian Web Clipper**: Browser extension to capture articles as markdown

- **Git**: Track changes and version history of your wiki

## Philosophy

**The LLM maintains everything.** You never write wiki pages yourself - you read, you curate sources, you ask questions, and you explore. The LLM does all the bookkeeping: summarizing, cross-referencing, updating, maintaining consistency.

**Knowledge compounds.** Unlike RAG systems that re-derive answers from raw sources every time, this wiki is built once and kept current. Cross-references already exist. Contradictions are already noted. The synthesis reflects everything you've learned.

**You own your data.** Everything is local markdown files. No vendor lock-in, no API costs for retrieval, no privacy concerns.

## Learning Focus

Based on your preferences:
- **Materials**: Original books (novels, non-fiction), textbooks, web articles
- **Key elements**: Vocabulary, expressions/idioms, cultural context
- **Languages**: English, Spanish, Japanese, Korean

The system is designed to support your specific learning style and priorities.

## Downstream Consumers

`Language/` 위키는 학습 콘텐츠의 **단일 진실 공급원**이다. 다른 프로젝트가 콘텐츠를 끌어다 쓴다.

| 다운스트림 | 위치 | 소비 형태 |
| --- | --- | --- |
| `typing_language` 게임 | `../Game/typing_language/` | `wiki/{Lang}/vocabulary/` 를 게임 코퍼스(`raw/{lang}_words.md`)의 `source: [[wikilink]]` 인용 형태로 큐레이션 |

게임 측에서 신규 콘텐츠를 요청했을 때 Language 위키에 없으면, **Language에 먼저 출처를 추가하고 인제스트한 후** 게임으로 반영한다. Language 위키는 게임 없이도 독립적으로 성장한다.

자세한 파이프라인: `wiki/pipeline-to-game.md`, 게임 측: `../Game/typing_language/wiki/corpus-pipeline.md`

---

*For detailed instructions on wiki structure, page formats, and workflows, see `schema/AGENTS.md`*
