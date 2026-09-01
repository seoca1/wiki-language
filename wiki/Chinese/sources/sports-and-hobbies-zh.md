---
type: "vocabulary-source"
date_added: "2026-09-01"
language_level: "HSK 3-5"
language: "Chinese"
theme: "sports-and-hobbies"
source_url: "raw/Chinese/sports-and-hobbies.md"
license: "Educational use"
access_date: "2026-09-01"
---

# sports-and-hobbies-zh

**Type:** vocabulary-source / 体育运动与爱好  
**Language:** Chinese  
**Theme:** 体育运动 / 爱好 / Sports & Hobbies  
**Level:** HSK 3-5 / A2-B2  
**Date Ingested:** 2026-09-01  

---

## Original (Source)

`raw/Chinese/sports-and-hobbies.md`

---

## Summary

体育运动与休闲爱好主题的中文词汇源文件。涵盖球类运动、水上运动、健身/武术、户外运动、电竞/棋类、收藏/手工等爱好类别。为中文wiki的 `sports-and-hobbies.md` 主题页提供规范 pipeline-form 条目。

---

## Key Takeaways

- **主题**: 体育运动 / 爱好 / 娱乐 / 休闲
- **HSK级别**: 3-5 (中级~高级)
- **分类**: 球类/水上/健身武术/户外/电竞棋类/收藏手工
- **用途**: 为中文wiki `sports-and-hobbies.md` 主题页提供规范 pipeline-form 条目

---

## Vocabulary Extracted (词汇提取)

### Ball Sports / 球类运动

| ID | Display | Input | Meaning | Level | Category |
|---|---|---|---|---|---|
| zh_sport_001 | 篮球 (lánqiú) | lánqiú | basketball | 2 | sports |
| zh_sport_002 | 足球 (zúqiú) | zúqiú | football/soccer | 2 | sports |
| zh_sport_003 | 乒乓球 (pīngpāngqiú) | pīngpāngqiú | table tennis | 2 | sports |
| zh_sport_004 | 羽毛球 (yǔmáoqiú) | yǔmáoqiú | badminton | 2 | sports |

### Fitness & Martial Arts / 健身与武术

| ID | Display | Input | Meaning | Level | Category |
|---|---|---|---|---|---|
| zh_sport_017 | 跑步 (pǎobù) | pǎobù | running/jogging | 2 | sports |
| zh_sport_018 | 健身 (jiànshēn) | jiànshēn | fitness/working out | 2 | sports |
| zh_sport_019 | 瑜伽 (yújiā) | yújiā | yoga | 3 | sports |
| zh_sport_019 | 太极拳 (tàijíquán) | tàijíquán | tai chi | 3 | sports |

---

## Pipeline Form (机器可读格式)

```yaml
- { id: zh_sport_001, display: "篮球 (lánqiú)", input: "lánqiú", meaning: "basketball", level: "2", category: "sports", source: "[[sports-and-hobbies-zh]]" }
```

---

## Game Application

### Vocabulary Categories
- `category: sports`
- `category: hobby`
- `level: 3-5`
- `input: pinyin`

### New Stages (Proposed)
- `zh_sp_1`: Ball Sports Basics (球类基础)
- `zh_sp_2`: Water Sports (水上运动)
- `zh_sp_3`: Fitness & Martial Arts (健身武术)
- `zh_sp_4`: Outdoor Adventure (户外探险)

---

## Sources

- Synthetic vocabulary source for cross-language parity with English `sports-and-hobbies` and Japanese `sports-and-hobbies`
