---
type: "vocabulary-source"
date_added: "2026-08-13"
language_level: "HSK 3-5"
language: "Chinese"
theme: "adventure-vocabulary"
source_url: "raw/Chinese/adventure-vocabulary-zh.md"
license: "Educational use"
access_date: "2026-08-13"
---

# adventure-vocabulary-zh

**Type:** vocabulary-source / 户外探险词汇源  
**Language:** Chinese  
**Theme:** 户外探险 / 登山 / 露营 / 攀岩  
**Level:** HSK 3-5  
**Date Ingested:** 2026-08-13  

---

## Original (Source)

`raw/Chinese/adventure-vocabulary-zh.md`

---

## Summary

户外探险主题的中文词汇源文件。为中文wiki的 `adventure-vocabulary.md` 主题页提供上游锚点，提供规范的 pipeline-form 条目。

---

## Key Takeaways

- **主题**: 户外探险 / 登山 / 露营 / 攀岩 / 徒步
- **HSK级别**: 3-5 (中级到中高级)
- **重点**: 登山/徒步/露营/攀岩核心装备、动作、地形词汇
- **用途**: 为中文wiki `adventure-vocabulary.md` 主题页提供规范 pipeline-form 条目

---

## Vocabulary Extracted (词汇提取)

| ID | Display | Input | Meaning | Level | Category |
|---|---|---|---|---|---|
| zh_adventure_001 | 登山 (dēngshān) | dēngshān | mountain climbing | 2 | adventure |
| zh_adventure_002 | 徒步 (túbù) | túbù | hiking | 3 | adventure |
| zh_adventure_003 | 露营 (lùyíng) | lùyíng | camping | 3 | adventure |
| zh_adventure_004 | 帐篷 (zhàngpéng) | zhàngpéng | tent | 3 | adventure |
| zh_adventure_005 | 攀岩 (pānyán) | pānyán | rock climbing | 4 | adventure |

---

## Pipeline Form (机器可读格式)

```yaml
- { id: zh_adventure_001, display: "登山 (dēngshān)", input: "dēngshān", meaning: "mountain climbing", level: "2", category: "adventure", source: "[[adventure-vocabulary-zh]]" }
- { id: zh_adventure_002, display: "徒步 (túbù)", input: "túbù", meaning: "hiking", level: "3", category: "adventure", source: "[[adventure-vocabulary-zh]]" }
- { id: zh_adventure_003, display: "露营 (lùyíng)", input: "lùyíng", meaning: "camping", level: "3", category: "adventure", source: "[[adventure-vocabulary-zh]]" }
- { id: zh_adventure_004, display: "帐篷 (zhàngpéng)", input: "zhàngpéng", meaning: "tent", level: "3", category: "adventure", source: "[[adventure-vocabulary-zh]]" }
- { id: zh_adventure_005, display: "攀岩 (pānyán)", input: "pānyán", meaning: "rock climbing", level: "4", category: "adventure", source: "[[adventure-vocabulary-zh]]" }
```

---

## Game Application

### Vocabulary Categories
- `category: adventure`
- `level: 2-5`
- `input: pinyin`

### New Stages (Proposed)
- `zh_adv_1`: Mountaineering Basics (登山基础)
- `zh_adv_2`: Camping Essentials (露营装备)
- `zh_adv_2`: Rock Climbing Terms (攀岩术语)

---

## Sources

- Synthetic vocabulary source for cross-language parity with English `adventure-vocabulary` and Japanese `adventure-vocabulary`