---
type: "vocabulary-source"
date_added: "2026-09-01"
language_level: "HSK 3-5"
language: "Chinese"
theme: "travel-adventure"
source_url: "raw/Chinese/travel-adventure.md"
license: "Educational use"
access_date: "2026-09-01"
---

# travel-adventure-zh

**Type:** vocabulary-source / 旅行探险词汇源  
**Language:** Chinese  
**Theme:** 旅行探险 / Travel & Adventure  
**Level:** HSK 2-4 / A1-B1  
**Date Ingested:** 2026-09-01  

---

## Original (Source)

`raw/Chinese/travel-adventure.md`

---

## Summary

旅行探险主题的中文词汇源文件。涵盖交通工具、住宿、景点门票、户外探险等核心旅行词汇。为中文wiki的 `travel-adventure.md` 主题页提供规范 pipeline-form 条目。

---

## Key Takeaways

- **主题**: 旅行探险 / 交通/住宿/景点/户外探险
- **HSK级别**: 2-4 (初级到中级)
- **分类**: 交通/住宿/景点/户外探险/应急/签证
- **用途**: 为中文wiki的 `travel-adventure.md` 主题页提供规范 pipeline-form 条目

---

## Vocabulary Extracted (词汇提取)

### Transportation / 交通工具

| ID | Display | Input | Meaning | Level | Category |
|---|---|---|---|---|---|
| zh_travel_001 | 飞机 (fēijī) | fēijī | airplane | 1 | travel |
| zh_travel_002 | 高铁 (gāotiě) | gāotiě | high-speed rail | 2 | travel |
| zh_travel_003 | 地铁 (dìtiě) | dìtiě | subway | 2 | travel |

### Accommodation / 住宿

| ID | Display | Input | Meaning | Level | Category |
|---|---|---|---|---|---|
| zh_travel_011 | 酒店 (jiǔdiàn) | jiǔdiàn | hotel | 2 | travel |

### Attractions / 景点

| ID | Display | Input | Meaning | Level | Category |
|---|---|---|---|---|---|
| zh_travel_026 | 景点 (jǐngdiǎn) | jǐngdiǎn | attraction | 2 | travel |

### Outdoor Adventure / 户外探险

| ID | Display | Input | Meaning | Level | Category |
|---|---|---|---|---|---|
| zh_travel_035 | 登山 (dēngshān) | dēngshān | mountain climbing | 2 | travel |

---

## Pipeline Form (机器可读格式)

```yaml
- { id: zh_travel_001, display: "飞机 (fēijī)", input: "fēijī", meaning: "airplane", level: "1", category: "travel", source: "[[travel-adventure-zh]]" }
```

---

## Game Application

### Vocabulary Categories
- `category: travel`
- `level: 2-4`
- `input: pinyin`

### New Stages (Proposed)
- `zh_tr_1`: Transportation Basics (交通基础)
- `zh_tr_2`: Accommodation & Booking (住宿预订)
- `zh_tr_3`: Attractions & Sightseeing (景点游览)
- `zh_tr_4`: Outdoor Adventure (户外探险)

---

## Sources

- Synthetic vocabulary source for cross-language parity with English `travel` and Japanese `travel`
