# Sistemas de escritura (Versión en español)

> Original: [[writing-systems]] (English) | Fecha: 2026-08-19 | ADR-0006
> **Comparación de los sistemas de escritura en 5 idiomas** — Español · Inglés · Japonés · Coreano · Chino

---

## Clasificación de los sistemas

| Idioma | Tipo de sistema | Dirección | Nombre del script | Bloque Unicode |
|----------|-------------|-----------|------------|---------------|
| **Inglés** | Alfabeto (latino) | LTR | Latín | Basic Latin, Latin-1 Supplement |
| **Español** | Alfabeto (latino) | LTR | Latín | Basic Latin, Latin-1 Supplement |
| **Japonés** | Mixto: logográfico + silabario ×2 | LTR (moderno), TTB (tradicional) | Kanji + Hiragana + Katakana | CJK Unified Ideographs, Hiragana, Katakana |
| **Coreano** | Alfabeto featural (Hangul) | LTR (moderno), TTB (tradicional) | Hangul | Hangul Syllables, Hangul Jamo |
| **Chino** | Logográfico | LTR (moderno), TTB (tradicional) | Hanzi (simplificado / tradicional) | CJK Unified Ideographs |

---

## Español: alfabeto latino (27 letras + ñ)

| Rasgo | Detalle |
|---------|--------|
| **Letras** | 27 (A-Z + Ñ) — *ch, ll* deprecated as letters (2010) |
| **Diagramas** | ch, ll, rr, gu, qu |
| **Diacríticos** | **Acento agudo (´)** — acento, desambiguación (*sí* vs *si*); **Dieresis (¨)** — *pingüino, vergüenza*; **Tilde (˜)** — *ñ* |
| **Mayúsculas** | Sí (bicameral) |
| **Grafema-fonema** | **Ortografía transparente** — casi 1:1 (5 vocales, 19 consonantes) |
| **Puntuación** | **Inversión ¿ ¡** — único del español |

### Ventaja del español
- **Pronunciación predecible** → adquisición de lectoescritura más rápida.
- **Acento escrito garantiza la sílaba tónica** → menos ambigüedad que inglés.

---

## Japonés: sistema mixto de tres escrituras

### Inventario

| Escritura | Tipo | Caracteres | Uso principal |
|--------|------|------------|-------------|
| **Hiragana** | Silabario | 46 básicos + 25 sonoros + 33 combinados ≈ 104 | palabras nativas, gramática (okurigana), furigana, textos infantiles |
| **Katakana** | Silabario | 46 básicos + 25 sonoros + 33 combinados ≈ 104 | préstamos, énfasis, onomatopeyas, nombres científicos |
| **Kanji** | Logográfico | 2.136 jōyō (uso diario) + ~3.000 más | palabras de contenido (sustantivos, raíces verbales y adjetivas) |

### Kanji: estadísticas clave

| Métrica | Valor |
|--------|-------|
| **Kanji jōyō** (常用漢字) | 2.136 (uso diario oficial) |
| **Kanji jinmeiyō** (人名用漢字) | 863 (solo nombres) |
| **Total en uso** | ~3.000-4.000 (adulto cultivado) |
| **Lecturas por kanji** | 2-10+ (On-yomi + Kun-yomi) |
| **Trazos** | 1-30+ (media ~12) |

---

## Coreano: Hangul (한글) — alfabeto featural

### Principios de diseño (1443, Rey Sejong)

| Principio | Implementación |
|-----------|----------------|
| **Featural** | forma de la letra codifica la articulación (lengua, labios, garganta) |
| **Bloques silábicos** | letras se combinan en sílabas cuadradas (CV, CVC, CVCC) |
| **Sistemático** | 19 consonantes × 21 vocales = 11.172 sílabas posibles |
| **Fonémico** | casi 1:1 letra-sonido |

### Consonantes (19)

| Básicas | ㄱ | ㄴ | ㄷ | ㄹ | ㅁ | ㅂ | ㅅ | ㅇ | ㅈ | ㅊ | ㅋ | ㅌ | ㅍ | ㅎ |
|----|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sonido | g/k | n | d/t | r/l | m | b/p | s | ng/∅ | j/ch | ch' | k' | t' | p' | h |
| Tensas | ㄲ | ㄸ | ㅃ | ㅆ | ㅉ | | | | | | | | | |
| Sonido | kk | tt | pp | ss | jj | | | | | | | | | |

### Vocales (21: 10 básicas + 11 diptongos)

| Básicas | ㅏ | ㅑ | ㅓ | ㅕ | ㅗ | ㅛ | ㅜ | ㅠ | ㅡ | ㅣ |
|----|---|---|---|---|---|---|---|---|---|---|
| Sonido | a | ya | eo | yeo | o | yo | u | yu | eu | i |

---

## Chino: Hanzi (汉字/漢字) — logográfico

### Simplificado vs tradicional

| Aspecto | Simplificado (简体) | Tradicional (繁體) |
|--------|------------------|-------------------|
| **Regiones** | China continental, Singapur, Malasia | Taiwán, Hong Kong, Macao, diáspora |
| **Caracteres** | ~2.500 trazos reducidos | ~4.500+ formas completas |
| **Métodos** | cursiva→estándar; fusionar homófonos; reducir radicales | preserva etimología |
| **Ejemplo** | 爱 / 龙 / 书 / 学 | 愛 / 龍 / 書 / 學 |

### Estructura de caracteres

| Tipo | % | Principio | Ejemplo |
|------|---|-----------|---------|
| **Pictográfico** (象形) | ~4 % | dibujo del objeto | 日 (sol), 月 (luna), 山 (monte), 人 (persona) |
| **Ideográfico** (指事) | ~2 % | concepto abstracto | 上 (arriba), 下 (abajo), 一 (uno), 二 (dos) |
| **Ideográfico compuesto** (会意) | ~10 % | significado + significado | 休 (persona + árbol = descanso), 好 (mujer + niño = bueno) |
| **Fonético-semántico** (形声) | ~80 %+ | radical (significado) + fonético (sonido) | 妈 (mujer + ma), 河 (agua + he), 晴 (sol + qing) |

### Pinyin (拼音) — romanización

| Rasgo | Detalle |
|---------|--------|
| **Oficial** | ISO 7098, estándar chino (1958) |
| **Marcas de tono** | 4 tonos + neutro (ā á ǎ à a) |
| **Iniciales** | 21 (b p m f d t n l g k h j q x zh ch sh r z c s y w) |
| **Finales** | 36 (a o e i u ü + compuestos) |
| **Sílabas** | ~400 base × 4 tonos ≈ 1.600 sílabas tonales |
| **Separación** | por palabra (no por sílaba) — *wǒ ài nǐ* no se une |

---

## Carga de aprendizaje comparada

| Métrica | Inglés | Español | Japonés | Coreano | Chino |
|---------|---------|---------|----------|---------|---------|
| **Grafemas a aprender** | 26 + digramas | 27 + diacríticos | ~100 kana + 2.136 kanji | 40 jamo (bloques) | ~3.000 hanzi |
| **Transparencia fonémica** | Baja (profunda) | **Alta (superficial)** | Alta (kana) / Baja (kanji) | **Alta (featural)** | Baja (logográfico) |
| **Edad de alfabetización** | 7-8 | 5-6 | 12+ (kanji hasta secundaria) | 5-6 | 10-12 |
| **Vocabulario adulto funcional** | 20.000+ palabras | 20.000+ palabras | 2.136 jōyō + vocabulario | 2.000+ hanja + hangul | 3.000-5.000 hanzi |
| **Método de entrada** | Escritura directa | Escritura directa | IME (kana→kanji) | IME (jamo→sílaba) | IME (pinyin→hanzi) |

---

## 🇪🇸 Notas para estudiantes de español (Spanish Learner Notes)

> Esta sección es una guía de aprendizaje adicional para hispanohablantes.

### Trampas comunes para hispanohablantes al aprender los otros 4 idiomas

1. **Subestimar el sistema de kanji japonés**:
   - Hispanohablantes saben leer español con alfabeto; asumir que japonés es similar.
   - **Trampa**: creer que leer japonés es aprender otro alfabeto (¡son 2.000+ caracteres logográficos!).
   - **Entrenamiento**: aceptar 1-2 años para dominio funcional; usar mnemotecnia con radicales.

2. **Confundir el pinyin chino con la ortografía final**:
   - El pinyin (zǎo shang) NO es la escritura china; es solo romanización.
   - **Trampa**: escribir *zaoshang* en lugar de 早上 en contexto formal.
   - **Entrenamiento**: al aprender chino, escribir siempre hanzi desde el inicio, pinyin solo como apoyo fonético.

3. **Asumir que Hangul coreano es "fácil porque tiene pocas letras"**:
   - Hangul tiene 40 jamo, pero se combinan en bloques silábicos con reglas de batchim y ortografía fonológica.
   - **Trampa**: pensar que después de 1 semana ya se lee coreano.
   - **Entrenamiento**: dominar las reglas de sandhi (ligadura, nasalización) antes de leer fluido.

4. **Olvidar la ñ y los acentos en español**:
   - Hispanohablantes suelen olvidar marcar tildes al escribir rápido, generando ambigüedad (*si* vs *sí*, *el* vs *él*).
   - **Entrenamiento**: al escribir correos profesionales, revisar acentos uno por uno.

5. **Creer que el español y el inglés son "iguales" porque comparten alfabeto**:
   - Aunque ambos usan el alfabeto latino, las reglas ortográficas y el lexicon difieren enormemente.
   - **Trampa**: asumir pronuncias desde el inglés (*pizza* se dice /ˈpi.tsa/ en español, no /ˈpɪzə/).
   - **Entrenamiento**: estudiar la fonética española explícitamente; no confiar en la ortografía.

### Páginas relacionadas del wiki español

- [[basic-vocabulary]] — vocabulario básico
- [[espana-vs-latinoamerica-registro]] — variantes regionales
- [[pronunciation-challenges]] — sistemas fonológicos
- [[grammar-difficulty-map]] — gramática por rasgo
- [[untranslatable-concepts]] — conceptos culturales

### Flujo de aprendizaje recomendado

1. **Dominar el alfabeto latino ampliado del español** (27 letras, acentos, diéresis)
2. **Para cada idioma adicional**: entender primero si es alfabético (coreano), logográfico (chino) o mixto (japonés)
3. **Practicar la dirección y segmentación** (CJK sin espacios, coreano por bloques)
4. **Vigilar las reglas de sandhi y ortografía fonológica** (lenguas CJK tienen reglas no obvias)

---

## Páginas relacionadas

- `[[pronunciation-challenges]]` — sistemas fonológicos detrás de las ortografías
- `[[grammar-difficulty-map]]` — complejidad gramatical por rasgo
- `[[cultural-values]]` — el sistema de escritura como artefacto cultural
- `[[untranslatable-concepts]]` — conceptos inscritos en los sistemas de escritura

## Fuentes

- `[English/vocabulary/basic-vocabulary]`
- `[Spanish/vocabulary/basic-vocabulary]`
- `[[index]]`, `[Japanese/vocabulary/jp-counters]`, `[Japanese/vocabulary/kanji-n5]`
- `[[index]]`, `[Korean/vocabulary/topik1-starter]`
- `[Chinese/vocabulary/body-zh]`, `[Chinese/sources/pinyin-basics-zh]`
- Unicode Consortium — *Unicode Standard*
- DeFrancis, J. (1989) *Visible Speech: The Diverse Oneness of Writing Systems*
- Taylor, I. & Olson, D.R. (1995) *Scripts and Literacy*

---

**Original (inglés)**: [[writing-systems]] | **Espejos relacionados**: [[writing-systems.ko|Coreano]] · [[writing-systems.ja|Japonés]] · [[writing-systems.zh|Chino]] | **Política**: ADR-0006
