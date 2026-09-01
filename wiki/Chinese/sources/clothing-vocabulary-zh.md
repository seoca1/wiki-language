---
type: "vocabulary-source"
date_added: "2026-09-01"
language_level: "HSK 3-5"
language: "Chinese"
theme: "clothing-vocabulary"
source_url: "raw/Chinese/clothing.md"
license: "Educational use"
access_date: "2026-09-01"
---

# clothing-vocabulary-zh

**Type:** vocabulary-source / 服装词汇  
**Language:** Chinese  
**Theme:** 服装 / Clothing  
**Level:** HSK 3-5  
**Date Ingested:** 2026-09-01  

---

## Original (Source)

`raw/Chinese/clothing.md`

---

## Summary

服装及时尚相关核心词汇。服装种类、材质、颜色、尺码、购物表达等服装购买及穿着相关核心词汇。为中文wiki的 `clothing-vocabulary.md` 主题页提供规范 pipeline-form 条目。

---

## Key Takeaways

- **主题**: 服装/时尚/穿搭/购物
- **HSK级别**: 3-5 (中级~高级)
- **分类**: 上衣/下装/鞋类/配饰/材质/颜色/尺码
- **用途**: 为中文wiki `clothing-vocabulary.md` 主题页提供规范 pipeline-form 条目

---

## Vocabulary Extracted (词汇提取)

### Tops / 上衣

| ID | Display | Input | Meaning | Level | Category |
|---|---|---|---|---|---|
| zh_cloth_001 | 衬衫 (chèn shān) | chèn shān | shirt | 2 | clothing |
| zh_cloth_002 | T恤 (T xù) | T xù | T-shirt | 2 | clothing |
| zh_cloth_003 | 卫衣 (wéi yī) | wéi yī | hoodie | 3 | clothing |
| zh_cloth_004 | 外套 (wài tào) | wài tào | coat/jacket | 3 | clothing |

### Bottoms / 下装

| ID | Display | Input | Meaning | Level | Category |
|---|---|---|---|---|---|
| zh_cloth_005 | 裤子 (kù zi) | kù zi | pants/trousers | 2 | clothing |
| zh_cloth_006 | 牛仔裤 (niú zǎi kù) | niú zǎi kù | jeans | 3 | clothing |
| zh_cloth_007 | 裙子 (qún zi) | qún zi | skirt | 2 | clothing |

### Footwear / 鞋类

| ID | Display | Input | Meaning | Level | Category |
|---|---|---|---|---|---|
| zh_cloth_008 | 鞋 (xié) | xié | shoes | 2 | clothing |
| zh_cloth_009 | 运动鞋 (yùn dòng xié) | yùn dòng xié | sneakers | 3 | clothing |

---

## Pipeline Form (机器可读格式)

```yaml
- { id: zh_cloth_001, display: "衬衫 (chèn shān)", input: "chèn shān", meaning: "shirt", level: "2", category: "clothing", source: "[[clothing-vocabulary-zh]]" }
```

---

## Game Application

### Vocabulary Categories
- `category: clothing`
- `level: 3-5`
- `input: pinyin`

### New Stages (Proposed)
- `zh_cl_1`: Tops & Basics (上衣基础)
- `zh_cl_2`: Bottoms & Pants (下装/裤子)
- `zh_cl_3`: Footwear (鞋类)
- `zh_cl_4`: Accessories (配饰)

---

## Sources

- Synthetic vocabulary source for cross-language parity with English `clothing` and Japanese `clothing`
