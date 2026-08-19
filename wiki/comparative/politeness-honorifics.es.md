# Cortesía y honoríficos (Versión en español)

> Original: [[politeness-honorifics]] (English) | Fecha: 2026-08-19 | ADR-0006
> **Comparación de sistemas de cortesía y honoríficos en 5 idiomas** — Español · Inglés · Japonés · Coreano · Chino

---

## Tabla de referencia rápida

| Rasgo | Inglés | Español | Japonés | Coreano | Chino |
|---------|---------|---------|----------|---------|---------|
| **Codificación gramatical** | Solo léxica (elección de vocabulario) | Pronombre (tú/usted) + morfología verbal | Morfología verbal (keigo) + vocabulario | Terminaciones verbales (niveles de habla) + sustantivos/verbos honoríficos | Elección léxica + títulos honoríficos + 您 (nín) |
| **Número de niveles** | 2-3 (formal/neutro/informal) | 2-3 (tú/usted/vosotros) | 3-4 (casual/cortés/honorífico/humilde) | 4-6 (해체/해요체/합쇼체/하소서체 + mixtos) | 2-3 (neutro/您/títulos respetuosos) |
| **Distinción pronominal** | you (universal) | tú / usted / vosotros / ustedes | あなた / 君 / お前 / 貴方 (a menudo omitido) | 너 / 당신 / 선생님 / 님 (evitado) | 你 / 您 / 诸位 / 先生/女士 |
| **Morfología verbal** | No | Sí (2.ª/3.ª persona) | Sí (extensa) | Sí (extensa) | Mínima (algunas formas supletivas) |
| **Vocabulario honorífico** | Limitado (sir/ma'am, títulos) | Don/Doña, formas de usted | 尊敬語 / 謙譲語 / 丁寧語 | 존댓말 / 높임말 (sustantivos/verbos especiales) | 尊称, 敬语 (您, 贵姓, etc.) |
| **Importa estatus relativo** | Depende del contexto | Sí (edad, familiaridad) | Central (uchi/soto) | Central (edad, jerarquía) | Central (edad, jerarquía, guanxi) |
| **Endogrupo vs exogrupo** | Débil | Moderado (usted = exogrupo por defecto) | Fundamental (uchi/soto) | Fundamental (내사람/남) | Fundamental (自己人/外人) |

---

## Por idioma

### Español
- **Términos clave**: tú / usted / vosotros / ustedes, *don/doña*, formas verbales de usted, *tuteo* vs *ustedeo*
- **Patrones**:
  - **Tú**: amigos, familia, niños, pares (por defecto entre jóvenes en España)
  - **Usted**: desconocidos, mayores, contextos formales, autoridad (por defecto en LatAm)
  - **Vosotros** (solo España): plural informal
  - **Ustedes**: plural formal (España) / plural ambos (LatAm)
- **Variantes regionales**:
  - **España**: fuerte distinción tú/usted; vosotros usado
  - **México/Colombia/Perú**: usted por defecto incluso entre jóvenes en algunos contextos
  - **Argentina/Uruguay/Paraguay**: *vos* reemplaza *tú* (voseo) — conjugación distinta
  - **Caribe**: *usted* más frecuente, *tú* reservado para intimidad

### Japonés
- **Términos clave**:
  - **丁寧語 (teineigo)**: です/ます — cortés por defecto
  - **尊敬語 (sonkeigo)**: honorífico — eleva al oyente (*いらっしゃる, 召し上がる, ご存知*)
  - **謙譲語 (kenjōgo)**: humilde — rebaja al hablante (*参る, いただく, 拝見する*)
  - **美化語 (bikago)**: prefijos お/ご (*お茶, ご飯*)
- **Patrones**: Conjugaciones verbales cambian completamente según registro. *Uchi* (endogrupo) vs *soto* (exogrupo) determina qué keigo usar. Con desconocidos = teineigo. Negocios = combinación sonkeigo/kenjougo.

### Coreano
- **Términos clave**:
  - **해체 (haeche)**: simple/formal escrito — amigos cercanos, niños, monólogo interno
  - **해요체 (haeyoche)**: cortés informal — vida diaria, compañeros, conocidos (habla por defecto)
  - **합쇼체 (hapsyoche)**: formal cortés — presentaciones,广播, militar, clientes
  - **하소서체 (hasoseoche)**: extremadamente formal — histórico, religioso, realeza
  - **존댓말 (jondaetmal)**: paraguas para niveles corteses
  - **반말 (banmal)**: casual (mezcla de 해체/해요체)
- **Patrones**:
  - Terminación verbal cambia: 가다 → 가/가요/갑니다/가시옵소서
  - Sustantivos honoríficos: 밥 → 진지, 집 → 댁, 이름 → 성함, 생일 → 생신
  - Verbos honoríficos: 먹다 → 잡수시다, 자다 → 주무시다, 계시다 (있다/계시다)
  - Marcador honorífico de sujeto: ~(으)시 (가시다, 드시다)

### Chino
- **Términos clave**:
  - **您 (nín)**: "tú" respetuoso (vs 你 nǐ)
  - **尊称 (zūnchēng)**: títulos respetuosos — 先生, 女士, 老师, 总经理, 姐/哥
  - **敬语 (jìngyǔ)**: vocabulario honorífico — 贵姓, 请教, 拜访, 敬请, 承蒙
  - **谦辞 (qiāncí)**: autodespreciativo — 拙作, 拙见, 献丑, 不敢当
- **Patrones**:
  - Sin cambio morfológico verbal para cortesía
  - Cortesía = sustitución léxica + títulos + partículas finales (请, 麻烦您, 劳驾)
  - **您 (nín)** para mayores, superiores, desconocidos en contextos formales
  - **Título + 姓**: 王先生, 李老师, 张总 — dirección por defecto en contextos profesionales
  - **Guanxi (关系)** modula el registro: relación cercana → descartar 您, usar nombre/apodo

---

## Contrastes clave (síntesis)

| Contraste | Implicación para estudiantes |
|----------|--------------------------|
| **Gramatical vs léxico** — JP/KR/ES codifican cortesía en gramática; EN/CH en vocabulario | Estudiantes de JP/KR deben dominar paradigmas verbales temprano; los de EN/CH pueden comunicarse con gramática básica + palabras corteses |
| **Registro por defecto con desconocidos** — ES: *usted* (LatAm) / *tú* (jóvenes España); JP: *desu/masu*; KR: *haeyoche*; CH: *nín* + título | Elegir el registro por defecto según la región objetivo |
| **Endogrupo/exogrupo (uchi/soto, 내사람/남)** — Central en JP/KR; débil en EN; moderado en ES/CH | En JP/KR, usar el registro incorrecto con endogrupo = frío/distante; con exogrupo = grosero |
| **Edad vs título como base del tratamiento** — KR/CH requieren título+님/先生; JP usa -san/様; ES usa Don/Doña + usted; EN usa Mr/Ms | En KR/CH, llamar a alguien por el nombre solo = grosero. Memorizar títulos para cada rol |
| **Negociación del registro** — KR explícita ("우리 반말 해요"); JP implícita; ES explícita ("tuteame"); CH implícita | Practicar guiones de transición de registro |

---

## 🇪🇸 Notas para estudiantes de español (Spanish Learner Notes)

> Esta sección es una guía de aprendizaje adicional para hispanohablantes.

### Trampas comunes para hispanohablantes al aprender los otros 4 idiomas

1. **Asumir que *usted* es la opción formal universal**:
   - En chino no existe un pronombre formal paralelo a *usted*; se usa 您 (nín) para mayores/respecto, y títulos contextuales (王老师, 服务员).
   - **Trampa**: traducir *"¿usted es...?"* al chino como *nín shì ma?* sin contexto (puede sonar raro).
   - **Entrenamiento**: usar 您 SOLO con mayores o en contextos claramente formales; preferir nombres + títulos.

2. **No distinguir *tú* (español) de la fonética de *tu* (francés/italiano)**:
   - Aunque no es parte del conjunto, vale notar: hispanohablantes aplican *tú* como informal universal; en algunas regiones asiáticas *tu* no existe.
   - **Entrenamiento**: en CJK, no traducir *"you"* como análogo directo de *tú*; preferir nombres y títulos.

3. **Confundir *vos* y *tú***:
   - En Argentina/Uruguay/Paraguay, *vos* reemplaza *tú* con conjugación propia (*vos tenés, vos sos*).
   - **Trampa**: usar *vosotros* en Argentina (no se usa, es solo España).
   - **Entrenamiento**: dominar el voseo rioplatense si viajas a esa región.

4. **Aplicar la lógica español al keigo japonés**:
   - Español tiene *tú/usted* como pronombres. Japonés tiene conjugaciones completas distintas (sonkeigo/kenjougo).
   - **Trampa**: intentar traducir literalmente *"para usted"* como conjugación japonesa.
   - **Entrenamiento**: memorizar *ご家族 (gokazoku - familia honorífica)*, *いらっしゃる (irassharu - ir honorífico)* en contexto.

5. **Olvidar el 您 (nín) en chino**:
   - *您* es opcional y limitado a contexto formal con mayores; usar en exceso (= condescendencia) o insuficiente (= grosería) son errores.
   - **Entrenamiento**: usar 您 con taxistas, ancianos, desconocidos en negocios; no usar con amigos ni同龄 (misma edad).

### Páginas relacionadas del wiki español

- [[polite-expressions-comparison]] — frases de cortesía cotidianas
- [[greetings]] — saludos formales/informales
- [[pronouns-reference]] — sistemas pronominales
- [[business-email]] — formalidad escrita
- [[dating-romance]] — negociación de registro en intimidad
- [[untranslatable-concepts]] — conceptos culturales de cortesía

### Flujo de aprendizaje recomendado

1. **Familiarizar con el sistema español** (tú/usted/vosotros/vos) y sus variantes regionales
2. **Estudiar las cuatro capas del keigo** japonés (teineigo, sonkeigo, kenjougo, bikago)
3. **Aprender los niveles de habla coreanos** (해체 → 해요체 → 합쇼체) y cuándo usar cada uno
4. **Dominar el 您 (nín) + títulos** en chino, especialmente en contextos profesionales
5. **Practicar la negociación de registro** (de formal a informal tras relación establecida)

---

## Páginas relacionadas

- `[[greetings]]` — fórmulas de saludo según registro
- `[[pronouns-reference]]` — pronombres y registro
- `[[business-email]]` — registro escrito formal
- `[[dating-romance]]` — negociación de registro en relaciones

## Fuentes

- Inglés: `[English/vocabulary/basic-vocabulary]`, `[English/culture/english-dating-culture]`
- Español: `[Spanish/vocabulary/polite-expressions-vocabulary]`, `[Spanish/culture/espana-vs-latinoamerica-registro]`, `[Spanish/sources/notes-in-spanish-listening-log]`
- Japonés: `[Japanese/vocabulary/business-vocabulary]`, `[Japanese/culture/japanese-dating-culture]`, `[Japanese/sources/business-email]`
- Coreano: `[Korean/vocabulary/emotions-personality-vocabulary]`, `[Korean/culture/korean-dating-culture]`, `[Korean/sources/daily-life-basics]`
- Chino: `[Chinese/vocabulary/body-zh]`, `[Chinese/sources/greetings-zh]`, `[Chinese/sources/daily-routine-zh]`

---

**Original (inglés)**: [[politeness-honorifics]] | **Espejos relacionados**: [[politeness-honorifics.ko|Coreano]] · [[politeness-honorifics.ja|Japonés]] · [[politeness-honorifics.zh|Chino]] | **Política**: ADR-0006
