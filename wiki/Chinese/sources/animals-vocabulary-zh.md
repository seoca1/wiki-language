---
type: "vocabulary-source"
date_added: "2026-09-01"
language_level: "HSK 3-5"
language: "Chinese"
theme: "animals-vocabulary"
source_url: "raw/Chinese/animals-vocabulary.md"
license: "Educational use"
access_date: "2026-09-01"
---

# animals-vocabulary-zh

**Type:** vocabulary-source / 动物词汇  
**Language:** Chinese  
**Theme:** 动物 / Animals  
**Level:** HSK 3-5  
**Date Ingested:** 2026-09-01  

---

## Original (Source)

`raw/Chinese/animals-vocabulary.md`

---

## Summary

动物相关核心词汇源文件。涵盖哺乳类、鸟类、爬行类、鱼类、昆虫等主要动物分类的核心词汇。为中文wiki的 `animals.md` 主题页提供规范 pipeline-form 条目。

---

## Key Takeaways

- **主题**: 动物 / 哺乳类/鸟类/爬行类/鱼类/昆虫
- **HSK级别**: 3-5 (中级~高级)
- **分类**: 哺乳/鸟类/爬行/鱼类/昆虫
- **用途**: 为中文wiki的 `animals.md` 主题页提供规范 pipeline-form 条目

---

## Vocabulary Extracted (词汇提取)

### Mammals / 哺乳类

| ID | Display | Input | Meaning | Level | Category |
|---|---|---|---|---|---|
| zh_anim_001 | 狮子 (shīzi) | shīzi | lion | 3 | animals |
| zh_anim_002 | 老虎 (lǎohǔ) | lǎohǔ | tiger | 3 | animals |
| zh_anim_003 | 熊 (xióng) | xióng | bear | 3 | animals |

### Birds / 鸟类

| ID | Display | Input | Meaning | Level | Category |
|---|---|---|---|---|---|
| zh_anim_006 | 鹰 (yīng) | yīng | eagle | 3 | animals |
| zh_anim_007 | 猫头鹰 (māotóuyīng) | māotóuyīng | owl | 4 | animals |

---

## Pipeline Form (机器可读格式)

```yaml
- { id: zh_anim_001, display: "狮子 (shīzi)", input: "shīzi", meaning: "lion", level: "3", category: "animals", source: "[[animals-vocabulary-zh]]" }
```

---

## Game Application

### Vocabulary Categories
- `category: animals`
- `level: 3-5`
- `input: pinyin`

### New Stages (Proposed)
- `zh_an_1`: Mammals Basics (哺乳类基础)
- `zh_an_2`: Birds & Flight (鸟类与飞行)
- `zh_an_3`: Reptiles & Amphibians (爬行类/两栖类)
- `zh_an_4`: Insects & Arachnids (昆虫/蜘蛛)

---

## Sources

- Synthetic vocabulary source for cross-language parity with English `animals` and Japanese `animals`
