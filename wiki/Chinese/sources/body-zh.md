---
type: "vocabulary-source"
date_added: "2026-09-01"
language_level: "HSK 1-2"
language: "Chinese"
theme: "body"
source_url: "raw/Chinese/body.md"
license: "Educational use"
access_date: "2026-09-01"
---

# body-zh

**Type:** vocabulary-source / 신체 부위  
**Language:** Chinese  
**Theme:** 身体部位 / Body Parts  
**Level:** HSK 1-2  
**Date Ingested:** 2026-09-01  

---

## Original (Source)

`raw/Chinese/body.md`

---

## Summary

신체 부위 핵심 어휘. 머리부터 발끝까지 신체 부위 명칭을 HSK 1-2 수준에 맞춰 정리. 한국어/영어/중국어 3개 언어 병기.

---

## Key Takeaways

- **주제**: 신체 부위 / Head/Body/Limbs/Organs
- **HSK급수**: 1-2 (입문~초급)
- **분류**: 머리/상체/하체/내장기관/감각기관
- **용도**: `wiki/Chinese/vocabulary/body.md` 주제 페이지 파이프라인-form 조건 제공

---

## Vocabulary Extracted (词汇提取)

### Head / 머리

| ID | Display | Input | Meaning | Level | Category |
|---|---|---|---|---|---|
| zh_body_001 | 头 (tóu) | tóu | head | 1 | body |
| zh_body_002 | 头发 (tóu fa) | tóu fa | hair | 1 | body |
| zh_body_003 | 脸 (liǎn) | liǎn | face | 1 | body |
| zh_body_004 | 眼睛 (yǎn jing) | yǎn jing | eyes | 1 | body |
| zh_body_005 | 耳朵 (ěr duo) | ěr duo | ears | 1 | body |
| zh_body_006 | 鼻子 (bí zi) | bǐ zi | nose | 1 | body |
| zh_body_007 | 嘴 (zuǐ) | zuǐ | mouth | 1 | body |

### Upper Body / 상체

| ID | Display | Input | Meaning | Level | Category |
|---|---|---|---|---|---|
| zh_body_008 | 脖子 (bó zi) | bó zi | neck | 1 | body |
| zh_body_009 | 肩膀 (jiān bǎng) | jiān bǎng | shoulder | 2 | body |
| zh_body_010 | 手臂 (shǒu bì) | shǒu bì | arm | 1 | body |
| zh_body_011 | 手 (shǒu) | shǒu | hand | 1 | body |
| zh_body_012 | 手指 (shǒu zhǐ) | shǒu zhǐ | finger | 1 | body |

### Lower Body / 하체

| ID | Display | Input | Meaning | Level | Category |
|---|---|---|---|---|---|
| zh_body_013 | 腿 (tuǐ) | tuǐ | leg | 1 | body |
| zh_body_014 | 脚 (jiǎo) | jiǎo | foot | 1 | body |
| zh_body_015 | 脚趾 (jiǎo zhǐ) | jiǎo zhǐ | toe | 1 | body |

---

## Pipeline Form (机器可读格式)

```yaml
- { id: zh_body_001, display: "头 (tóu)", input: "tóu", meaning: "head", level: "1", category: "body", source: "[[body-zh]]" }
- { id: zh_body_002, display: "头发 (tóu fǎ)", input: "tóu fǎ", meaning: "hair", level: "1", category: "body", source: "[[body-zh]]" }
```

---

## Game Application

### Vocabulary Categories
- `category: body`
- `level: 1-2`
- `input: pinyin`

### New Stages (Proposed)
- `zh_body_1`: Head & Face (머리/얼굴)
- `zh_body_2`: Torso & Arms (상체/팔)
- `zh_body_3`: Legs & Feet (하체/다리)
- `zh_body_4`: Internal Organs (내장 기관)

---

## Sources

- Synthetic vocabulary source for cross-language parity with English `body` and Japanese `body`
