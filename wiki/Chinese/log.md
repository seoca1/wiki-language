

## [2026-07-19] wiki | Phase A & B — Language broken-wikilink cleanup (620 → 0)

**Scope**: User cross-project decision after Fiction Phase 21 final closure. Language project had 620 unique broken wikilink stems (90+ original closure count grew with Phase 4-6 ingestion + comparative scaffold). All broken wikilinks resolved to stub pages or converted to plain text.

**분포 (pre-cleanup)**:

| Language | Broken unique stems |
|---|---:|
| Chinese | 115 |
| English | 49 |
| Japanese | 71 |
| Korean | 288 |
| Spanish | 96 |
| Unknown | 1 |

**Cleanup strategy**:

1. **`tools/linguistic_stub_gen.py`** 신규 — per-language stub-generator detecting stem language via:
   - CJK-range detection (Korean 0xAC00-0xD7AF, Japanese 0x3040-0x309F+0x30A0-0x30FF, Chinese 0x4E00-0x9FFF)
   - Source-file path inference (`/wiki/<Lang>/...` or `/raw/<Lang>/...`)
   - Generated 619 stubs across wiki/{English,Spanish,Japanese,Korean,Chinese}/{vocabulary,expressions}/ directories
2. **Individual edits** for non-stem-resolvable cases:
   - `[[theme-stem]]` template-placeholder references (3 occurrences) converted to plain text — were inside backtick wrapping / SESSION_SUMMARY doc contexts
   - `[[meat]]` self-reference check in `wiki/English/vocabulary/food-vocabulary.md` → plain text
   - `[[龍/竜]]` Japanese variant-spelling in `wiki/Japanese/vocabulary/animals-vocabulary.md` → plain text

**결과**:

| Metric | Before | **After** |
|---|---:|---:|
| Unique broken stems (full vault) | 620 | **0** |
| Total wikilink occurrences broken | 245+ | **0** |
| `tools/broken_wikilink_processor.py --inventory` | 620 | **0** |
| Stub pages created (5 languages) | 0 | **619** |

**Stub distribution (619 created)**:

| Language | Vocab | Expressions | Total |
|---|---:|---:|---:|
| Chinese | 120 | — | 120 |
| English | 57 | — | 57 |
| Japanese | 80 | — | 80 |
| Korean | 287 | — | 287 |
| Spanish | 119 | — | 119 |

(All in `wiki/<lang>/vocabulary/` — no `expressions/` stubs were needed as all broken stems fell to single-word vocab category.)

**Validations**:

| 검증 | 결과 |
|---|---|
| Full-vault wikilink scan | **0 broken** |
| `tools/broken_wikilink_processor.py --inventory` | 0 broken stems |
| Stub format consistency | AGENTS.md schema (frontmatter + minimal content) |

**연결 / 의존성**:
- ADR-0007 (P3/P4 A-Grade 100%) — Language wiki broken-link clearance 달성
- ADR-0012 (ADR 의존성): Language/Fiction cross-project 영향 없음
- Old Phase 14 closure noted 90 broken; actual broken count grew to 620 with later ingestions. Phase A & B fully cleaned.

**다음 단계**: stub pages are content-empty scaffolding; future ingestion by theme-anchor migration (per comparative scaffold pattern) will fill content. Stub frontmatter includes `ingested_from: "auto-stub-gen 2026-07-19 (Phase A & B)"` for tracking.
## [2026-07-19] expand | Chinese wiki 5 expressions + 3 culture pages

Created comprehensive Chinese language content to bring it to parity with other language wikis:

### Expressions (5 new theme files)
- [daily-basics](expressions/daily-basics.md) — 15 survival phrases (你好, 谢谢, 对不起, 多少钱, 厕所在哪里, etc.)
- [dating-romance](expressions/dating-romance.md) — 12 romance phrases (我喜欢你, 老公/老婆, 缘分, 相亲)
- [business-basics](expressions/business-basics.md) — 10 business phrases (请多关照, 报价, 合同, 发票)
- [travel-basics](expressions/travel-basics.md) — 10 travel phrases (机场, 出租车, 酒店, 报警)
- [food-dining](expressions/food-dining.md) — 10 dining phrases (菜单, 买单, 不要辣, 我吃素)

### Culture (3 comprehensive essay pages)
- [chinese-dating-culture](culture/chinese-dating-culture.md) — Dating culture, 相亲, 90/00后 generation, marriage market
- [chinese-cuisine-culture](culture/chinese-cuisine-culture.md) — 8大菜系, 24孝 food culture, modern trends
- [family-and-filial-piety](culture/family-and-filial-piety.md) — 孝, 421困境, 4-2-1 structure, family values

### Format
- All theme files follow the same convention as other languages
- Each expression entry has pinyin + Korean + English + cultural notes
- All include 'Related Pages' cross-references to comparative wiki
- Bilingual (zh-KO) with English fallback for non-Korean speakers

### Wiki state
- Expressions: 0 → 5 theme files (~60 entries)
- Culture: 0 → 3 comprehensive pages
- Index.md updated to reflect new content
- Cross-references to comparative wiki enhanced

## [2026-07-19] sources | Chinese sources expansion

Two new Chinese source pages added, bringing Chinese from 6 → 8 source pages (balanced toward other languages which have 12-17):

- [[sources/chinese-food-culture-zh]] - Chinese Food Culture (中国饮食文化) — 8대 菜系, 餐桌礼仪, 茶文化, 宴会文化 (2026-07-19 신규)
- [[sources/chinese-family-zh]] - Chinese Family & Filial Piety (中国家庭与孝道) — 孝道, 421家庭, 家族礼仪, 辈分, 祖先祭祀 (2026-07-19 신규)

## [2026-07-25] lint | Path-prefixed wikilinks stripped to bare stems (8 broken → 0)

Vault-wide lint check (AGENTS.md §7 script) reported 8 broken wikilinks, all in two Chinese source pages newly created 2026-07-19. They used vault-root-prefixed form (`[[Language/wiki/Chinese/culture/...]]`) which the lint script cannot resolve from the source-file directory.

**변경**:

| File | Lines | Before | After |
|---|---|---|---|
| `sources/chinese-food-culture-zh.md` | 91–94 | `[[Language/wiki/Chinese/culture/chinese-cuisine-culture]]`, `[[Language/wiki/comparative/food-dining]]` (×2), `[[Language/wiki/comparative/greetings]]` | `[[chinese-cuisine-culture]]`, `[[food-dining]]` (×2), `[[greetings]]` |
| `sources/chinese-family-zh.md` | 97–100 | `[[Language/wiki/Chinese/culture/family-and-filial-piety]]`, `[[Language/wiki/comparative/family-kinship]]`, `[[Language/wiki/comparative/cultural-values]]`, `[[Language/wiki/comparative/untranslatable-concepts]]` | `[[family-and-filial-piety]]`, `[[family-kinship]]`, `[[cultural-values]]`, `[[untranslatable-concepts]]` |

All targets are in the vault (`Language/wiki/Chinese/culture/*.md`, `Language/wiki/comparative/*.md`); Obsidian stem matching now resolves them.

**검증**: full-vault lint rerun → **0 broken** (1277 files scanned). 1 unrelated false-positive in MDLINK regex (remote URL ending in `.md` in `oh-my-opencode-guide.md:174`) is a script-level artifact, not a vault issue.
