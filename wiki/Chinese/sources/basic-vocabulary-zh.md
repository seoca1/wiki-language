---
type: "vocabulary-source"
date_added: "2026-09-01"
language_level: "HSK 1-2"
language: "Chinese"
theme: "basic-vocabulary"
source_url: "raw/Chinese/basic-vocabulary.md"
license: "Educational use"
access_date: "2026-09-01"
---

# basic-vocabulary-zh

**Type:** vocabulary-source / 基础词汇  
**Language:** Chinese  
**Theme:** 基础词汇 / Basic Vocabulary  
**Level:** HSK 1-2  
**Date Ingested:** 2026-09-01  

---

## Original (Source)

`raw/Chinese/basic-vocabulary.md`

---

## Summary

中文基础词汇源文件。涵盖问候、数字、时间、家庭、食物、方向、颜色、数字等基础日常词汇。为中文wiki的 `basic-vocabulary.md` 主题页提供规范 pipeline-form 条目。

---

## Key Takeaways

- **核心分类**: 问候/数字/时间/家庭/食物/方向/颜色/数字
- **HSK级别**: 1-2 (入门~初级)
- **单词数**: 200-300个目标
- **用途**: 为中文wiki `basic-vocabulary.md` 主题页提供规范 pipeline-form 条目

---

## Vocabulary Extracted (词汇提取)

### Greetings / 问候

| ID | Display | Input | Meaning | Level | Category |
|---|---|---|---|---|---|
| zh_basic_001 | 你好 (nǐ hǎo) | nǐ hǎo | hello | 1 | greetings |
| zh_basic_002 | 再见 (zài jiàn) | zài jiàn | goodbye | 1 | greetings |
| zh_basic_003 | 谢谢 (xiè xie) | xiè xie | thank you | 1 | greetings |

### Numbers / 数字

| ID | Display | Input | Meaning | Level | Category |
|---|---|---|---|---|---|
| zh_basic_006 | 一 (yī) | yī | one | 1 | numbers |
| zh_basic_007 | 二 (èr) | èr | two | 1 | numbers |

---

## Pipeline Form (机器可读格式)

```yaml
- { id: zh_basic_001, display: "你好 (nǐ hǎo)", input: "nǐ hǎo", meaning: "hello", level: "1", category: "basics", source: "[[basic-vocabulary-zh]]" }
```

---

## Game Application

### Vocabulary Categories
- `category: basics`
- `level: 1-2`
- `input: pinyin`

### New Stages (Proposed)
- `zh_basic_1`: Greetings & Politeness (问候/礼貌)
- `zh_basic_2`: Numbers & Counting (数字/计数)
- `zh_basic_3`: Time & Date (时间/日期)
- `zh_basic_4`: Basic Verbs (基础动词)

---

## Sources

- Synthetic vocabulary source for cross-language parity with English `basic-vocabulary` and Japanese `basic-vocabulary`
