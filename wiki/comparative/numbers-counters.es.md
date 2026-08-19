# Números y contadores (Versión en español)

> Original: [[numbers-counters]] (English) | Fecha: 2026-08-19 | ADR-0006
> **Comparación de sistemas numéricos y contadores en 5 idiomas** — Español · Inglés · Japonés · Coreano · Chino

---

## Números cardinales (1-10, 100, 1000, 10000)

| Número | Inglés | Español | Japonés | Coreano (Sino) | Coreano (Nativo) | Chino |
|--------|---------|---------|----------|---------------|-----------------|---------|
| 0 | zero | cero | ゼロ / 零 | 영 / 공 | - | 零 / 〇 |
| 1 | one | uno | 一 (いち) | 일 | 하나 (han-) | 一 (yī) |
| 2 | two | dos | 二 (に) | 이 | 둘 (tu-) | 二 (èr) / 两 (liǎng) |
| 3 | three | tres | 三 (さん) | 삼 | 셋 (se-) | 三 (sān) |
| 4 | four | cuatro | 四 (よん/し) | 사 | 넷 (ne-) | 四 (sì) |
| 5 | five | cinco | 五 (ご) | 오 | 다섯 (da-) | 五 (wǔ) |
| 6 | six | seis | 六 (ろく) | 육 | 여섯 (yeo-) | 六 (liù) |
| 7 | seven | siete | 七 (なな/しち) | 칠 | 일곱 (il-) | 七 (qī) |
| 8 | eight | ocho | 八 (はち) | 팔 | 여덟 (yeo-) | 八 (bā) |
| 9 | nine | nueve | 九 (きゅう/く) | 구 | 아홉 (a-) | 九 (jiǔ) |
| 10 | ten | diez | 十 (じゅう) | 십 | 열 (yeol) | 十 (shí) |
| 20 | twenty | veinte | 二十 (にじゅう) | 이십 | 스물 (seumul) | 二十 (èrshí) |
| 100 | one hundred | cien / ciento | 百 (ひゃく) | 백 | 온 (on) | 一百 (yībǎi) |
| 1.000 | one thousand | mil | 千 (せん) | 천 | - | 一千 (yīqiān) |
| 10.000 | ten thousand | diez mil | 万 (まん) | 만 | - | 一万 (yīwàn) |
| 100.000.000 | cien millones | cien millones | 億 (おく) | 억 | - | 一亿 (yīyì) |

### Diferencias estructurales clave

| Rasgo | Inglés | Español | Japonés | Coreano | Chino |
|---------|---------|---------|----------|---------|---------|
| **Base** | 1.000 (mil) | 1.000 (mil) | 10.000 (万) | 10.000 (만) | 10.000 (万) |
| **Agrupación grande** | 3 dígitos (mil, millón, billón) | 3 dígitos | 4 dígitos (万, 億, 兆) | 4 dígitos (만, 억, 조) | 4 dígitos (万, 亿, 兆) |
| **Dos sistemas** | No | No | No | **Sí** (sino + nativo) | No (pero 两 vs 二) |
| **Cero en compuesto** | "one hundred **and** one" | "ciento uno" | "hyaku ichi" | "baek il" / "baek hana" | "yībǎi líng yī" |

## Números ordinales

| Posición | Inglés | Español | Japonés | Coreano | Chino |
|----------|---------|---------|----------|---------|---------|
| 1.º | first | primero / 1º | 一番目 (いちばんめ) | 첫째 / 제1 | 第一 (dì yī) |
| 2.º | second | segundo / 2º | 二番目 (にばんめ) | 둘째 / 제2 | 第二 (dì èr) |
| 3.º | third | tercero / 3º | 三番目 (さんばんめ) | 셋째 / 제3 | 第三 (dì sān) |
| n.º | -th | -º / -ª | -番目 (-ばんめ) | -째 / 제- | 第- (dì-) |

- **Español**: *primero/tercero* pierden la *-o* ante sustantivo masculino (*primer libro, tercer piso*).
- **Japonés**: prefijo *dai-* (第) en contextos formales (*dai-ikkai* = 第1回).
- **Coreano**: *je-* (sino) + *beonchae* formal; nativo *cheot-/du-/se-* informal.
- **Chino**: prefijo *dì-* (第) universal.

## Contadores / Clasificadores (gran divergencia)

> **Inglés/Español**: sin contadores obligatorios — "tres manzanas" = *tres manzanas*.
> **Japonés/Coreano/Chino**: **obligatorios** — no se puede contar un sustantivo sin contador.

---

## 🇪🇸 Notas para estudiantes de español (Spanish Learner Notes)

> Esta sección es una guía de aprendizaje adicional para hispanohablantes.

### Trampas comunes para hispanohablantes al aprender los otros 4 idiomas

1. **Asumir que no hay contadores en inglés/especialmente en español**:
   - El español usa algunos clasificadores livianos (*un trozo de pan, una hoja de papel, dos cabezas de ganado*) pero con poco rigor gramatical.
   - **Trampa**: ignorar los contadores en chino/japonés/coreano.
   - **Entrenamiento**: aprender el contador principal de cada categoría (个/個 en chino, 本/枚 en japonés, 개/명 en coreano).

2. **Confundir dos escalas de conteo en coreano**:
   - El coreano distingue números sino-coreanos (일, 이, 삼) para 100+ y meses, y nativos (하나, 둘, 셋) para edad y horas.
   - **Trampa**: decir *일 시* (1 hora) en vez de *한 시*; decir *스무 살* con sustantivos que requieren sino (*20 años = 스무 살* ✓, pero *20 personas = 이십 명*).
   - **Entrenamiento**: practicar pares mínimos (*한 시* vs *일 시*, *둘째* vs *제2*).

3. **Aplicar las reglas del español a los grandes números**:
   - El español usa base mil (*mil, millón, billón*). Chino/japonés/coreano usan base 10.000 (*万/만/만*, *億/억/억*).
   - **Trampa**: traducir *un millón* como *一亿* (100 millones) en chino.
   - **Entrenamiento**: aprender primero la base numérica antes de convertir cifras grandes.

4. **Olvidar *dos* = *两* en chino**:
   - Antes de un clasificador, *两 (liǎng)* y no *二 (èr)* es obligatorio: *两个人*, *两本书*.
   - **Trampa**: usar *二* universalmente como en español (*dos*).
   - **Entrenamiento**: practicar *两 vs 二* en contraste antes de cada clasificador.

5. **Tetraphobia (4) en Asia oriental**:
   - El 4 se evita en Japón, Corea y China (suena a *muerte/shi/sa/sì*). Hospitales omiten piso 4.
   - **Trampa**: hispanohablantes no perciben el tabú cultural.
   - **Entrenamiento**: al regalar o numerar, evitar el 4 si es posible, o al menos reconocer el tabú.

### Páginas relacionadas del wiki español

- [[basic-vocabulary]] — vocabulario numérico básico
- [[time-prepositions-vocabulary]] — números en contexto temporal
- [[espana-vs-latinoamerica-registro]] — variantes regionales (billón corto/largo)
- [[food-dining]] — contadores para comida
- [[travel-essentials]] — precios, fechas, horarios

### Flujo de aprendizaje recomendado

1. **Cardinales del 1 al 100** + lectura de números grandes (millón, billón, diferencia escala corta vs larga)
2. **Números ordinales** + reglas de acortamiento (*primer/tercer*)
3. **Top 5-7 contadores** en cada idioma (个/位/张/本 en chino; 개/명/마리/장 en coreano; 個/人/本/枚 en japonés)
4. **Particularidades culturales** (4, 8, 9, 13 según cultura)

---

## Páginas relacionadas

- `[[greetings]]` — la hora usa números
- `[[travel-essentials]]` — precios, fechas, horarios
- `[[food-dining]]` — contadores de comida
- `[[politeness-honorifics]]` — contadores honoríficos (*bun, wei, mei, sama*)

## Fuentes

- Inglés: `[English/vocabulary/basic-vocabulary]`
- Español: `[Spanish/vocabulary/basic-vocabulary]`, `[Spanish/vocabulary/time-prepositions-vocabulary]`
- Japonés: `[Japanese/vocabulary/jp-counters]`, `[Japanese/vocabulary/kanji-n5]`, `[Japanese/sources/2026-07-13_Kanji_N5_100]`
- Coreano: `[[index]]`, `[Korean/vocabulary/topik1-starter]`, `[Korean/sources/daily-life-basics]`
- Chino: `[Chinese/vocabulary/numbers-zh]`, `[Chinese/vocabulary/measure-words-zh]`, `[Chinese/sources/pinyin-basics-zh]`

---

**Original (inglés)**: [[numbers-counters]] | **Espejos relacionados**: [[numbers-counters.ko|Coreano]] · [[numbers-counters.ja|Japonés]] · [[numbers-counters.zh|Chino]] | **Política**: ADR-0006
