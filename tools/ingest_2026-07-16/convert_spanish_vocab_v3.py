#!/usr/bin/env python3
"""
Comprehensive converter for Spanish vocabulary files.
Handles both table format and ### word section format with inline YAML.
"""

import re
from pathlib import Path
from typing import List, Dict, Any

# POS hints for Spanish
POS_HINTS_ES = {
    # Animals
    'perro': 'sustantivo', 'gato': 'sustantivo', 'pájaro': 'sustantivo', 'pez': 'sustantivo',
    'caballo': 'sustantivo', 'vaca': 'sustantivo', 'cerdo': 'sustantivo', 'oveja': 'sustantivo',
    'pollo': 'sustantivo',
    # Basic
    'hola': 'interjección', 'adiós': 'interjección', 'gracias': 'interjección', 'por_favor': 'adverbio',
    'sí': 'adverbio', 'no': 'adverbio', 'además': 'adverbio',
    'uno': 'numeral', 'dos': 'numeral', 'tres': 'numeral', 'cuatro': 'numeral', 'cinco': 'numeral',
    'rojo': 'adjetivo/sustantivo', 'azul': 'adjetivo/sustantivo', 'verde': 'adjetivo/sustantivo',
    'madre': 'sustantivo', 'padre': 'sustantivo', 'niño': 'sustantivo',
    'rápido': 'adjetivo', 'fácil': 'adjetivo', 'difícil': 'adjetivo', 'importante': 'adjetivo',
    # Business
    'empresa': 'sustantivo', 'oficina': 'sustantivo', 'colega': 'sustantivo', 'jefe': 'sustantivo',
    'empleado': 'sustantivo', 'reunión': 'sustantivo', 'proyecto': 'sustantivo', 'contrato': 'sustantivo',
    'email': 'sustantivo', 'ordenador': 'sustantivo', 'internet': 'sustantivo', 'teléfono': 'sustantivo',
    # Food
    'comida': 'sustantivo', 'agua': 'sustantivo', 'pan': 'sustantivo', 'carne': 'sustantivo',
    'pescado': 'sustantivo', 'pollo': 'sustantivo', 'arroz': 'sustantivo', 'frijoles': 'sustantivo',
    'café': 'sustantivo', 'té': 'sustantivo', 'cerveza': 'sustantivo', 'vino': 'sustantivo',
    'restaurante': 'sustantivo', 'mesero': 'sustantivo', 'menú': 'sustantivo', 'cuenta': 'sustantivo',
    'propina': 'sustantivo',
    # Travel
    'pasaporte': 'sustantivo', 'boleto': 'sustantivo', 'hotel': 'sustantivo', 'habitación': 'sustantivo',
    'reservación': 'sustantivo', 'aeropuerto': 'sustantivo', 'estación': 'sustantivo', 'taxi': 'sustantivo',
    'autobús': 'sustantivo', 'tren': 'sustantivo', 'metro': 'sustantivo', 'mapa': 'sustantivo',
    'guía': 'sustantivo', 'tour': 'sustantivo', 'museo': 'sustantivo', 'playa': 'sustantivo',
    'montaña': 'sustantivo', 'parque': 'sustantivo',
    # Nature/Weather
    'sol': 'sustantivo', 'luna': 'sustantivo', 'estrella': 'sustantivo', 'cielo': 'sustantivo',
    'nube': 'sustantivo', 'lluvia': 'sustantivo', 'nieve': 'sustantivo', 'viento': 'sustantivo',
    'tormenta': 'sustantivo', 'trueno': 'sustantivo', 'mar': 'sustantivo',
    'río': 'sustantivo', 'lago': 'sustantivo', 'isla': 'sustantivo', 'hielo': 'sustantivo',
    'niebla': 'sustantivo', 'arcoíris': 'sustantivo',
    'primavera': 'sustantivo', 'verano': 'sustantivo', 'otoño': 'sustantivo', 'invierno': 'sustantivo',
    'calor': 'sustantivo', 'frío': 'sustantivo', 'templado': 'adjetivo', 'húmedo': 'adjetivo', 'seco': 'adjetivo',
    # Clothing
    'camisa': 'sustantivo', 'pantalones': 'sustantivo', 'zapatos': 'sustantivo', 'calcetines': 'sustantivo',
    'chaqueta': 'sustantivo', 'abrigo': 'sustantivo', 'sombrero': 'sustantivo', 'guantes': 'sustantivo',
    'bufanda': 'sustantivo', 'vestido': 'sustantivo', 'falda': 'sustantivo',
    # Daily life
    'casa': 'sustantivo', 'puerta': 'sustantivo', 'ventana': 'sustantivo', 'cama': 'sustantivo',
    'mesa': 'sustantivo', 'silla': 'sustantivo', 'libro': 'sustantivo', 'teléfono': 'sustantivo',
    'ordenador': 'sustantivo', 'dinero': 'sustantivo', 'tiempo': 'sustantivo', 'reloj': 'sustantivo',
    # Body
    'cabeza': 'sustantivo', 'ojo': 'sustantivo', 'boca': 'sustantivo', 'brazo': 'sustantivo',
    'mano': 'sustantivo', 'espalda': 'sustantivo', 'estómago': 'sustantivo', 'pierna': 'sustantivo',
    'pie': 'sustantivo', 'corazón': 'sustantivo',
    # Family
    'hermano': 'sustantivo', 'hermana': 'sustantivo', 'abuelo': 'sustantivo', 'abuela': 'sustantivo',
    'tío': 'sustantivo', 'tía': 'sustantivo', 'primo': 'sustantivo', 'prima': 'sustantivo',
    # Adjectives/Emotions
    'feliz': 'adjetivo', 'triste': 'adjetivo', 'enojado': 'adjetivo', 'asustado': 'adjetivo',
    'sorprendido': 'adjetivo', 'cansado': 'adjetivo', 'contento': 'adjetivo', 'preocupado': 'adjetivo',
    'nervioso': 'adjetivo', 'tranquilo': 'adjetivo', 'amable': 'adjetivo', 'simpático': 'adjetivo',
    'guapo': 'adjetivo', 'bonito': 'adjetivo', 'feo': 'adjetivo', 'grande': 'adjetivo', 'pequeño': 'adjetivo',
    'nuevo': 'adjetivo', 'viejo': 'adjetivo', 'bueno': 'adjetivo', 'malo': 'adjetivo',
    # Verbs
    'ser': 'verbo', 'estar': 'verbo', 'tener': 'verbo', 'hacer': 'verbo', 'ir': 'verbo',
    'venir': 'verbo', 'ver': 'verbo', 'oír': 'verbo', 'hablar': 'verbo', 'escuchar': 'verbo',
    'comer': 'verbo', 'beber': 'verbo', 'dormir': 'verbo', 'despertar': 'verbo', 'trabajar': 'verbo',
    'estudiar': 'verbo', 'aprender': 'verbo', 'enseñar': 'verbo', 'leer': 'verbo', 'escribir': 'verbo',
    'comprar': 'verbo', 'vender': 'verbo', 'pagar': 'verbo', 'costar': 'verbo', 'gustar': 'verbo',
    'encantar': 'verbo', 'odiar': 'verbo', 'querer': 'verbo', 'amar': 'verbo', 'necesitar': 'verbo',
    'poder': 'verbo', 'saber': 'verbo', 'conocer': 'verbo', 'pensar': 'verbo', 'creer': 'verbo',
    'entender': 'verbo', 'comprender': 'verbo', 'olvidar': 'verbo', 'recordar': 'verbo',
    'levantarse': 'verbo pronominal', 'ducharse': 'verbo pronominal', 'vestirse': 'verbo pronominal',
    'acostarse': 'verbo pronominal', 'irse': 'verbo pronominal',
    'desayunar': 'verbo', 'almorzar': 'verbo', 'cenar': 'verbo', 'trabajar': 'verbo', 'estudiar': 'verbo',
    'pedir': 'verbo', 'probar': 'verbo', 'reservar': 'verbo',
}

THEME_CATEGORIES_ES = {
    'animals-vocabulary': 'animals',
    'basic-vocabulary': 'basic',
    'business-vocabulary': 'business',
    'clothing-vocabulary': 'clothing',
    'daily-life-vocabulary': 'daily-life',
    'emotions-personality-vocabulary': 'emotions-personality',
    'family-vocabulary': 'family',
    'food-vocabulary': 'food',
    'body-vocabulary': 'body',
    'nature-vocabulary': 'nature',
    'weather-vocabulary': 'weather',
    'restaurant-vocabulary': 'restaurant',
    'mexican_food-vocabulary': 'mexican-food',
    'transportation-vocabulary': 'transportation',
    'time-prepositions-vocabulary': 'time-prepositions',
    'polite-expressions-vocabulary': 'polite-expressions',
    'adjectives-vocabulary': 'adjectives',
    'viajes': 'travel',
    'tango-vocabulary': 'tango',
    'gustar-verb-grammar': 'grammar',
    'present-tense-grammar': 'grammar',
    'past-tense-grammar': 'grammar',
    'reflexive-verbs-grammar': 'grammar',
}


def parse_section_format(content: str) -> List[Dict]:
    """Parse files with ### word sections and inline YAML."""
    words = []
    
    # Pattern to match ### word sections with their content
    # This handles the format: ### word\n\n**Part of Speech:** ...\n**Meaning:** ...\n```yaml ... ```
    section_pattern = re.compile(
        r'(###\s+(.+?))\n\n'
        r'(?:\*\*Part of Speech:\*\*\s*(.+?)\n)?'
        r'(?:\*\*Meaning:\*\*\s*(.+?)\n|\*\*Definition:\*\*\s*(.+?)\n)?'
        r'(?:\*\*Pronunciation / IPA:\*\*\s*(.+?)\n|\*\*IPA:\*\*\s*(.+?)\n)?'
        r'(?:\*\*Etymology:\*\*\s*(.+?)\n)?'
        r'(?:\*\*Ejemplo:\*\*\s*(.+?)\n|\*\*Examples?\*\*\s*(.+?)\n)?'
        r'(?:\*\*Categoría gramatical:\*\*\s*(.+?)\n)?'
        r'(?:\n```yaml\n(.+?)\n```)?',
        re.DOTALL
    )
    
    # Also try a simpler pattern for sections with YAML
    simple_section = re.compile(
        r'(###\s+(.+?))\n\n'
        r'(?:\*\*Part of Speech:\*\*\s*(.+?)\n\n)?'
        r'(?:\*\*Meaning:\*\*\s*(.+?)\n\n|\*\*Definition:\*\*\s*(.+?)\n\n)?'
        r'(?:.*?\n\n---)',
        re.DOTALL
    )
    
    matches = section_pattern.finditer(content)
    for match in matches:
        full_section = match.group(1)
        word = match.group(2).strip()
        pos = (match.group(3) or '').strip()
        meaning = (match.group(4) or match.group(5) or '').strip()
        ipa1 = (match.group(6) or '').strip()
        ipa2 = (match.group(7) or '').strip()
        ipa = ipa1 or ipa2
        etymology = (match.group(8) or '').strip()
        examples1 = (match.group(9) or '').strip()
        examples2 = (match.group(10) or '').strip()
        examples = examples1 or examples2
        category_gram = (match.group(11) or '').strip()
        yaml_block = (match.group(12) or '').strip()
        
        if word and word not in ['Animales Básicos', 'Saludos y Cortesía', 'Respuestas Básicas', 'Números', 'Colores', 'Familia', 'Adjetivos Comunes', 'Verbos Reflexivos', 'Verbos de Comidas', 'Verbos Generales', 'Verbos de Restaurante', 'Paisajes', 'Fenómenos Naturales', 'Animales Básicos', 'Ropa Básica', 'Alimentos Básicos']:
            words.append({
                'word': word,
                'pos': pos,
                'meaning': meaning,
                'ipa': ipa,
                'etymology': etymology,
                'examples': examples,
                'category_gram': category_gram,
                'yaml_block': yaml_block,
            })
    
    # Fallback: try simpler pattern
    if not words:
        simple_matches = simple_section.finditer(content)
        for match in simple_matches:
            word = match.group(2).strip()
            pos = (match.group(3) or '').strip()
            meaning = (match.group(4) or match.group(5) or '').strip()
            if word and word not in ['Animales Básicos', 'Saludos y Cortesía', 'Respuestas Básicas', 'Números', 'Colores', 'Familia', 'Adjetivos Comunes']:
                words.append({
                    'word': word,
                    'pos': pos,
                    'meaning': meaning,
                    'ipa': '',
                    'etymology': '',
                    'examples': '',
                    'category_gram': '',
                    'yaml_block': '',
                })
    
    return words


def parse_table_format(content: str) -> List[Dict]:
    """Parse markdown tables."""
    words = []
    table_pattern = re.compile(r'\|([^|]+)\|([^|]+)\|([^|]+)\|')
    sections = re.split(r'^(##?\s+.+)$', content, flags=re.MULTILINE)
    current_section = ""
    for part in sections:
        part = part.strip()
        if not part:
            continue
        if part.startswith('#'):
            current_section = part
        else:
            lines = part.split('\n')
            for line in lines:
                line = line.strip()
                if line.startswith('|') and line.endswith('|') and '---' not in line:
                    match = table_pattern.match(line)
                    if match:
                        word = match.group(1).strip()
                        pronunciation = match.group(2).strip()
                        meaning = match.group(3).strip()
                        if word and word not in ['Español', 'English', 'Palabra', 'Pronunciación', 'Significado', 'Categoría gramatical', 'Connotación', 'Ejemplo', 'Kanji', 'Kana', 'Romaji', 'Meaning', '단어', '로마자', 'の意味', '카테고리', '함축']:
                            words.append({
                                'word': word,
                                'pronunciation': pronunciation,
                                'meaning': meaning,
                                'section': current_section
                            })
    return words


def extract_all_words(content: str) -> List[Dict]:
    """Extract words from both formats."""
    words = parse_table_format(content)
    if len(words) < 5:
        section_words = parse_section_format(content)
        words.extend(section_words)
    return words


def infer_pos(word: str, meaning: str, pos_hint: str = '') -> str:
    """Infer part of speech."""
    if pos_hint:
        return pos_hint
    if word in POS_HINTS_ES:
        return POS_HINTS_ES[word]
    meaning_lower = meaning.lower()
    if any(v in meaning_lower for v in ['to ', 'action', 'verb', 'verbo', 'acción']):
        return 'verbo'
    if any(v in meaning_lower for v in ['adjective', 'adjetivo', 'describing', 'calidad']):
        return 'adjetivo'
    if any(v in meaning_lower for v in ['adverb', 'adverbio', 'manner', 'modo']):
        return 'adverbio'
    if any(v in meaning_lower for v in ['preposition', 'preposición', 'conjunction', 'conjunción']):
        return 'preposición/conjunción'
    if any(v in meaning_lower for v in ['interjection', 'interjección', 'exclamation', 'exclamación']):
        return 'interjección'
    if any(v in meaning_lower for v in ['numeral', 'número', 'number']):
        return 'numeral'
    return 'sustantivo'


def generate_etymology_es(word: str, meaning: str) -> str:
    if any(c in word for c in 'àáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿ'):
        return f'Palabra española: {word} (origen latino/árabe/germánico según caso)'
    if word in ['karate', 'sushi', 'kimchi', 'taekwondo', 'k-pop', 'hanbok', 'hangul']:
        return f'Préstamo del coreano: {word}'
    return f'Español: {word} (etimología pendiente de investigación)'


def generate_examples_es(word: str, meaning: str, pos: str) -> List[str]:
    examples = []
    if 'verbo' in pos.lower():
        examples.append(f'Yo {word} todos los días. — Uso básico')
        examples.append(f'Por favor {word} esto. — Forma de petición')
    elif 'sustantivo' in pos.lower():
        examples.append(f'Necesito un {word}. — Expresando necesidad')
        examples.append(f'El {word} está aquí. — Ubicación/presencia')
    elif 'adjetivo' in pos.lower():
        examples.append(f'Es muy {word}. — Descripción')
        examples.append(f'Un día {word}. — Modificando sustantivo')
    elif 'interjección' in pos.lower():
        examples.append(f'¡{word}! — Exclamación independiente')
    elif 'numeral' in pos.lower():
        examples.append(f'Tengo {word} libros. — Contando')
    else:
        examples.append(f'{word} — Oración de ejemplo necesaria')
    return examples


def generate_related_terms_es(word: str, meaning: str, pos: str) -> List[str]:
    related = []
    if 'sustantivo' in pos.lower():
        related.append(f'[[{word}]] — Autoreferencia')
    elif 'verbo' in pos.lower():
        related.append(f'[[{word}]] — Forma base')
    
    animals = ['perro', 'gato', 'pájaro', 'pez', 'caballo', 'vaca', 'cerdo', 'oveja', 'pollo',
               'león', 'tigre', 'elefante', 'mono', 'oso', 'conejo', 'ciervo', 'mariposa', 'hormiga']
    if word in animals:
        related.append('[[animales]] — Vocabulario de animales')
    
    food = ['comida', 'agua', 'pan', 'carne', 'pescado', 'pollo', 'arroz', 'frijoles', 'café', 'té', 'cerveza', 'vino']
    if word in food:
        related.append('[[comida]] — Vocabulario de comida')
    
    clothing = ['camisa', 'pantalones', 'zapatos', 'calcetines', 'chaqueta', 'abrigo', 'sombrero', 'guantes', 'bufanda', 'vestido', 'falda']
    if word in clothing:
        related.append('[[ropa]] — Vocabulario de ropa')
    
    return related


def generate_cultural_notes_es(word: str, meaning: str, section: str) -> str:
    notes = []
    
    greetings = ['hola', 'adiós', 'gracias', 'por_favor']
    if word in greetings:
        notes.append('Marcadores esenciales de cortesía en culturas hispanohablantes. Se usan con mucha frecuencia.')
    
    if word in ['gracias', 'por_favor']:
        notes.append('Considerados obligatorios en peticiones y respuestas. Su omisión puede parecer grosera.')
    
    if word in ['usted', 'ustedes']:
        notes.append('Forma de cortesía (ustedeo) estándar en la mayoría de países. En Argentina/Uruguay/Paraguay se usa "vos".')
    
    if word in ['taco', 'tortilla', 'salsa', 'guacamole']:
        notes.append('Comida mexicana icónica. En España "tortilla" = tortilla de patatas (omelette).')
    
    if word in ['mate', 'yerba', 'bombilla']:
        notes.append('Bebida tradicional del Cono Sur (Argentina, Uruguay, Paraguay, sur de Brasil). Ritual social.')
    
    if word in ['siesta', 'fiesta', 'tapas']:
        notes.append('Costumbres sociales españolas. La siesta es menos común en zonas urbanas modernas.')
    
    if word in ['chevere', 'chévere', 'bacano', 'chido', 'padre', 'copado']:
        notes.append('Jerga regional para "genial/bueno": México=chido/padre, Colombia=bacano, Chile=chévere, Argentina=copado.')
    
    if not notes:
        notes.append('Contexto cultural por añadir')
    
    return ' '.join(notes)


def convert_file(input_path: Path, output_path: Path):
    """Convert a Spanish vocabulary file to full format."""
    content = input_path.read_text(encoding='utf-8')
    
    # Find header end
    header_end = content.find('| Español |')
    if header_end == -1:
        header_end = content.find('### ')
    if header_end == -1:
        print(f"No table or section found in {input_path}")
        return
    
    header = content[:header_end].rstrip()
    
    # Extract words
    words = extract_all_words(content)
    
    if not words:
        print(f"No words extracted from {input_path}")
        return
    
    # Extract Pipeline Form
    pipeline_match = re.search(r'(## Pipeline Form.*?```)', content, re.DOTALL)
    pipeline_form = pipeline_match.group(1) if pipeline_match else ''
    
    # Extract Sources
    sources_match = re.search(r'(## Sources\s*\n.*?)(?=\n##|\n---|\Z)', content, re.DOTALL)
    sources_section = sources_match.group(1).strip() if sources_match else ''
    
    # Theme category
    stem = input_path.stem
    category = THEME_CATEGORIES_ES.get(stem, 'vocabulary')
    
    # Level from header
    level_match = re.search(r'> \*\*Level:\*\*\s*(.+)', header)
    level = level_match.group(1).strip() if level_match else 'A1-B1'
    
    # Build new content
    new_lines = [header.rstrip(), '']
    
    # Group by section
    sections_dict = {}
    for w in words:
        sec = w.get('section', 'General')
        if sec not in sections_dict:
            sections_dict[sec] = []
        sections_dict[sec].append(w)
    
    for section_name, section_words in sections_dict.items():
        if section_name:
            new_lines.append(f'{section_name}')
            new_lines.append('')
        
        for w in section_words:
            word = w['word']
            pronunciation = w.get('pronunciation', w.get('ipa', ''))
            meaning = w.get('meaning', '')
            pos = w.get('pos', infer_pos(word, meaning))
            etymology = w.get('etymology', generate_etymology_es(word, meaning))
            examples = w.get('examples', [])
            category_gram = w.get('category_gram', '')
            
            new_lines.append(f'### {word}')
            new_lines.append('')
            new_lines.append(f'**Part of Speech:** {pos}')
            new_lines.append('')
            new_lines.append(f'**Definition:** {meaning}')
            new_lines.append('')
            new_lines.append(f'**Pronunciation / IPA:** {pronunciation}')
            new_lines.append('')
            new_lines.append(f'**Etymology:** {etymology}')
            new_lines.append('')
            new_lines.append('#### Examples')
            new_lines.append('')
            
            if examples and isinstance(examples, str):
                for ex in examples.split('\n'):
                    ex = ex.strip()
                    if ex and not ex.startswith('-'):
                        new_lines.append(f'- {ex}')
                    elif ex.startswith('-'):
                        new_lines.append(ex)
            else:
                for ex in generate_examples_es(word, meaning, pos):
                    new_lines.append(f'- {ex}')
            
            new_lines.append('')
            new_lines.append('#### Related Terms')
            new_lines.append('')
            for rt in generate_related_terms_es(word, meaning, pos):
                new_lines.append(f'- {rt}')
            new_lines.append('')
            new_lines.append('#### Cultural Notes')
            new_lines.append('')
            new_lines.append(generate_cultural_notes_es(word, meaning, section_name))
            new_lines.append('')
            new_lines.append('#### Sources')
            new_lines.append('')
            new_lines.append(f'- [[{stem}]]')
            new_lines.append('')
            new_lines.append('---')
            new_lines.append('')
    
    if sources_section:
        new_lines.append(sources_section)
        new_lines.append('')
    
    new_lines.append('---')
    new_lines.append('')
    
    if pipeline_form:
        new_lines.append(pipeline_form)
    
    output_content = '\n'.join(new_lines)
    output_path.write_text(output_content, encoding='utf-8')
    print(f"Converted {input_path.name}: {len(words)} words → {output_path}")


def main():
    vocab_dir = Path('/Users/emilio/projects/Projects/Language/wiki/Spanish/vocabulary')
    
    files_to_convert = [
        'animals-vocabulary.md',
        'basic-vocabulary.md',
        'business-vocabulary.md',
        'clothing-vocabulary.md',
        'daily-life-vocabulary.md',
        'emotions-personality-vocabulary.md',
        'family-vocabulary.md',
        'food-vocabulary.md',
        'body-vocabulary.md',
        'nature-vocabulary.md',
        'weather-vocabulary.md',
        'restaurant-vocabulary.md',
        'mexican_food-vocabulary.md',
        'transportation-vocabulary.md',
        'time-prepositions-vocabulary.md',
        'polite-expressions-vocabulary.md',
        'adjectives-vocabulary.md',
        'viajes.md',
        'tango-vocabulary.md',
    ]
    
    for fname in files_to_convert:
        fpath = vocab_dir / fname
        if fpath.exists():
            convert_file(fpath, fpath)
        else:
            print(f"File not found: {fpath}")


if __name__ == '__main__':
    main()