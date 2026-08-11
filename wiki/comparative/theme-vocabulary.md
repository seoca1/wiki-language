# Theme Vocabulary
**Last updated**: 2026-08-10 (5-language matrix expansion)

**Category:** meta-vocabulary

## Definition

Theme vocabulary in the Language wiki is the analytical-category of vocabulary-organization tracking thematic-domains across the multilingual corpora: food, family, work, time, body, space, emotions, abstract-concepts, daily-life, etc. In the Language wiki, theme-vocabulary pages are organized by topical-cluster, cross-language-parallel, and usage-context.

## Theme Vocabulary Categories

### Universal Themes (cross-language)
- **Food vocabulary**: 식사 (Korean), 食事 (Japanese), food (English), comida (Spanish), 食物 (Chinese)
- **Family vocabulary**: 가족 (Korean), 家族 (Japanese), family (English), familia (Spanish), 家庭 (Chinese)
- **Work vocabulary**: 일 (Korean), 仕事 (Japanese), work (English), trabajo (Spanish), 工作 (Chinese)
- **Time vocabulary**: 시간 (Korean), 時間 (Japanese), time (English), tiempo (Spanish), 时间 (Chinese)

### Cultural-Specific Themes
- **Korean honorifics**: 형/누나/오빠/언니 — age-relative-respect
- **Japanese keigo**: 敬語 — respect-language (sonkeigo, kenjōgo, teineigo)
- **Spanish usted/tú**: formality-register
- **Chinese measure words**: 个/条/只/张 — classifier-system

## Theme Vocabulary Coverage (per language)

| Theme | EN | ES | JP | KR | CH |
|-------|:-:|:-:|:-:|:-:|:-:|
| Food & Dining | ✓ | ✓ | ✓ | ✓ | ✓ |
| Family | ✓ | ✓ | ✓ | ✓ | ✓ |
| Body | ✓ | ✓ | ✓ | ✓ | ✓ |
| Time | ✓ | ✓ | ✓ | ✓ | ✓ |
| Colors | ✓ | ✓ | ✓ | ✓ | ✓ |
| Numbers | ✓ | ✓ | ✓ | ✓ | ✓ |
| Greetings | ✓ | ✓ | ✓ | ✓ | ✓ |
| Weather | ✓ | ✓ | ✓ | ✓ | ✓ |
| Travel | ✓ | ✓ | ✓ | ✓ | ✓ |
| Work/Career | ✓ | ✓ | ✓ | ✓ | ✓ |
| Sports | ✓ | ✓ | ✓ | ✓ | ✓ |
| Shopping | ✓ | ✓ | ✓ | ✓ | ✓ |
| Holidays | ✓ | ✓ | ✓ | ✓ | ✓ |
| Literature | ✓ | ✓ | ✓ | ✓ | ✓ |
| Adventure | ✓ | ✓ | ✓ | ✓ | ✓ |
| Quotes | ✓ | ✓ | ✓ | ✓ | ✓ |
| Entertainment | ✓ | ✓ | ✓ | ✓ | ✓ |
| Directions | ✓ | ✓ | ✓ | ✓ | ✓ |
| Animals | ✓ | ✓ | ✓ | ✓ | ✓ |
| Clothing | ✓ | ✓ | ✓ | ✓ | ✓ |
| Food (cooking) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Health | ✓ | ✓ | ✓ | ✓ | ✓ |
| Education | ✓ | ✓ | ✓ | ✓ | ✓ |
| Emotions | ✓ | ✓ | ✓ | ✓ | ✓ |
| Nature | ✓ | ✓ | ✓ | ✓ | ✓ |
| Transportation | ✓ | ✓ | ✓ | ✓ | ✓ |
| Technology | ✓ | ✓ | ✓ | ✓ | ✓ |
| Daily life | ✓ | ✓ | ✓ | ✓ | ✓ |

**Total**: 27 canonical themes across 5 languages, all at 100% parity (as of 2026-08-10)

## Theme File Structure (per language)

Each theme file follows the established pattern:
- **YAML frontmatter** (source/category/level/theme)
- **Korean-language title** + Spanish/English/etc. equivalents
- **Per-word sections**: 품사/Part of Speech, 정의/Definition, 로마자/IPA, 한자/Etymology, 예문/Examples, 관련어/Related Terms, 문화적 배경/Cultural Notes, 출처/Sources
- **Quick Reference Card** (15 essential words)
- **Cross-language comparison table** (한중/한일/etc.)

## Per-Language Detail

### English Theme Files
- **Naming convention**: `{theme}-vocabulary.md` (e.g., `food-vocabulary.md`)
- **Source references**: `raw/English/{theme}-{subcategory}.md` (e.g., `food-and-dining.md`)
- **Count**: 22 -vocabulary files (most extensive coverage)

### Spanish Theme Files
- **Naming convention**: `{theme}-vocabulary.md`
- **Source references**: `raw/Spanish/{theme}-{subcategory}-es.md`
- **Count**: 32 -vocabulary files (most themes with Spanish-specific sources)
- **Special**: ES culture is most extensive (43 culture pages, ES-specific regional content)

### Japanese Theme Files
- **Naming convention**: `{theme}-vocabulary.md` AND `{theme}.ko.md` (Korean perspective)
- **Source references**: `raw/Japanese/{theme}.md` + openclaw lang integration
- **Count**: 29 -vocabulary files + 29 .ko.md files (bilingual parallel)

### Korean Theme Files
- **Naming convention**: `{theme}-vocabulary.md`
- **Source references**: `raw/Korean/{theme}.md`
- **Count**: 28 -vocabulary files (cross-language parity with EN/ES/JP/CH)

### Chinese Theme Files
- **Naming convention**: Both `{theme}-vocabulary.md` AND `{theme}-zh.md`
- **Source references**: `raw/Chinese/{theme}-zh.md`
- **Count**: 21 -vocabulary files (13 from openclaw + 8 new 2026-08-10)
- **Special**: Chinese uses Korean-perspective format similar to JP .ko.md

## Theme Naming Conventions

| Pattern | Example | Used By |
|---------|---------|---------|
| `{theme}-vocabulary.md` | `food-vocabulary.md` | All 5 langs (primary convention) |
| `{theme}.ko.md` | `travel.ko.md` | JP (Korean perspective on JP content) |
| `{theme}-zh.md` | `directions-zh.md` | CH (Korean perspective on Chinese content) |
| `{theme}.md` | `theme.md` (this file) | Meta pages |

## Cross-Language Theme Equivalents

| English | Spanish | Japanese | Korean | Chinese |
|---------|---------|----------|--------|---------|
| Food & Dining | Comida y Restaurante | 食事 (食事) | 음식 | 食物 |
| Family | Familia | 家族 | 가족 | 家庭 |
| Work | Trabajo | 仕事 | 일 | 工作 |
| Time | Tiempo | 時間 | 시간 | 时间 |
| Sports | Deportes | スポーツ | 스포츠 | 体育 |
| Shopping | Compras | ショッピング | 쇼핑 | 购物 |
| Holidays | Fiestas y Celebraciones | 祝日 | 명절 | 节日 |
| Literature | Literatura | 文学 | 문학 | 文学 |
| Adventure | Aventura | 冒険 | 모험 | 冒险 |
| Entertainment | Entretenimiento | エンターテイメント | 엔터테인먼트 | 娱乐 |

## Related Concepts

- [[theme-vocabulary]]
- [[culture]]
- [[expression]]
- [[index]]
- [[vocabulary]]

## Sources

- Related: `Language/wiki/comparative/` (multiple theme-vocabulary pages)
- Related: `Language/wiki/{Korean,Japanese,English,Spanish,Chinese}/vocabulary/` (language-specific vocabulary)
