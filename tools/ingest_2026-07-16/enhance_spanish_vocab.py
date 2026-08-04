#!/usr/bin/env python3
"""
Convert already-sectioned Spanish vocabulary files to ensure all fields are complete.
These files already have ### word sections but may be missing some fields.
"""

import re
from pathlib import Path
from typing import List, Dict

POS_HINTS_ES = {
    'perro': 'sustantivo', 'gato': 'sustantivo', 'pájaro': 'sustantivo', 'pez': 'sustantivo',
    'caballo': 'sustantivo', 'vaca': 'sustantivo', 'cerdo': 'sustantivo', 'oveja': 'sustantivo',
    'pollo': 'sustantivo',
    'hola': 'interjección', 'adiós': 'interjección', 'gracias': 'interjección', 'por_favor': 'adverbio',
    'sí': 'adverbio', 'no': 'adverbio', 'además': 'adverbio',
    'uno': 'numeral', 'dos': 'numeral', 'tres': 'numeral', 'cuatro': 'numeral', 'cinco': 'numeral',
    'rojo': 'adjetivo/sustantivo', 'azul': 'adjetivo/sustantivo', 'verde': 'adjetivo/sustantivo',
    'madre': 'sustantivo', 'padre': 'sustantivo', 'niño': 'sustantivo',
    'rápido': 'adjetivo', 'fácil': 'adjetivo', 'difícil': 'adjetivo', 'importante': 'adjetivo',
    'empresa': 'sustantivo', 'oficina': 'sustantivo', 'colega': 'sustantivo', 'jefe': 'sustantivo',
    'empleado': 'sustantivo', 'reunión': 'sustantivo', 'proyecto': 'sustantivo', 'contrato': 'sustantivo',
    'email': 'sustantivo', 'ordenador': 'sustantivo', 'internet': 'sustantivo', 'teléfono': 'sustantivo',
    'comida': 'sustantivo', 'agua': 'sustantivo', 'pan': 'sustantivo', 'carne': 'sustantivo',
    'pescado': 'sustantivo', 'pollo': 'sustantivo', 'arroz': 'sustantivo', 'frijoles': 'sustantivo',
    'café': 'sustantivo', 'té': 'sustantivo', 'cerveza': 'sustantivo', 'vino': 'sustantivo',
    'restaurante': 'sustantivo', 'mesero': 'sustantivo', 'menú': 'sustantivo', 'cuenta': 'sustantivo',
    'propina': 'sustantivo',
    'pasaporte': 'sustantivo', 'boleto': 'sustantivo', 'hotel': 'sustantivo', 'habitación': 'sustantivo',
    'reservación': 'sustantivo', 'aeropuerto': 'sustantivo', 'estación': 'sustantivo', 'taxi': 'sustantivo',
    'autobús': 'sustantivo', 'tren': 'sustantivo', 'metro': 'sustantivo', 'mapa': 'sustantivo',
    'guía': 'sustantivo', 'tour': 'sustantivo', 'museo': 'sustantivo', 'playa': 'sustantivo',
    'montaña': 'sustantivo', 'parque': 'sustantivo',
    'sol': 'sustantivo', 'luna': 'sustantivo', 'estrella': 'sustantivo', 'cielo': 'sustantivo',
    'nube': 'sustantivo', 'lluvia': 'sustantivo', 'nieve': 'sustantivo', 'viento': 'sustantivo',
    'tormenta': 'sustantivo', 'trueno': 'sustantivo', 'montaña': 'sustantivo', 'mar': 'sustantivo',
    'río': 'sustantivo', 'lago': 'sustantivo', 'isla': 'sustantivo', 'hielo': 'sustantivo',
    'niebla': 'sustantivo', 'arcoíris': 'sustantivo',
    'primavera': 'sustantivo', 'verano': 'sustantivo', 'otoño': 'sustantivo', 'invierno': 'sustantivo',
    'calor': 'sustantivo', 'frío': 'sustantivo', 'templado': 'adjetivo', 'húmedo': 'adjetivo', 'seco': 'adjetivo',
    'camisa': 'sustantivo', 'pantalones': 'sustantivo', 'zapatos': 'sustantivo', 'calcetines': 'sustantivo',
    'chaqueta': 'sustantivo', 'abrigo': 'sustantivo', 'sombrero': 'sustantivo', 'guantes': 'sustantivo',
    'bufanda': 'sustantivo', 'vestido': 'sustantivo', 'falda': 'sustantivo',
    'casa': 'sustantivo', 'puerta': 'sustantivo', 'ventana': 'sustantivo', 'cama': 'sustantivo',
    'mesa': 'sustantivo', 'silla': 'sustantivo', 'libro': 'sustantivo', 'teléfono': 'sustantivo',
    'ordenador': 'sustantivo', 'dinero': 'sustantivo', 'tiempo': 'sustantivo', 'reloj': 'sustantivo',
    'cabeza': 'sustantivo', 'ojo': 'sustantivo', 'boca': 'sustantivo', 'brazo': 'sustantivo',
    'mano': 'sustantivo', 'espalda': 'sustantivo', 'estómago': 'sustantivo', 'pierna': 'sustantivo',
    'pie': 'sustantivo', 'corazón': 'sustantivo',
    'hermano': 'sustantivo', 'hermana': 'sustantivo', 'abuelo': 'sustantivo', 'abuela': 'sustantivo',
    'tío': 'sustantivo', 'tía': 'sustantivo', 'primo': 'sustantivo', 'prima': 'sustantivo',
    'feliz': 'adjetivo', 'triste': 'adjetivo', 'enojado': 'adjetivo', 'asustado': 'adjetivo',
    'sorprendido': 'adjetivo', 'cansado': 'adjetivo', 'contento': 'adjetivo', 'preocupado': 'adjetivo',
    'nervioso': 'adjetivo', 'tranquilo': 'adjetivo', 'amable': 'adjetivo', 'simpático': 'adjetivo',
    'guapo': 'adjetivo', 'bonito': 'adjetivo', 'feo': 'adjetivo', 'grande': 'adjetivo', 'pequeño': 'adjetivo',
    'nuevo': 'adjetivo', 'viejo': 'adjetivo', 'bueno': 'adjetivo', 'malo': 'adjetivo',
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
    'desayunar': 'verbo', 'almorzar': 'verbo', 'cenar': 'verbo',
    'trabajar': 'verbo', 'estudiar': 'verbo',
    'pedir': 'verbo', 'querer': 'verbo', 'probar': 'verbo', 'reservar': 'verbo',
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


def extract_words_from_sections(content: str) -> List[Dict]:
    """Extract word entries from ### word sections with full field parsing."""
    words = []
    
    # Pattern to match each word section
    section_pattern = re.compile(
        r'(###\s+(.+?))\n\n'
        r'\*\*Part of Speech:\*\*\s*(.+?)\n\n'
        r'\*\*Definition:\*\*\s*(.+?)(?:\n\n'
        r'\*\*Pronunciation / IPA:\*\*\s*(.+?)\n\n'
        r'\*\*Etymology:\*\*\s*(.+?)\n\n'
        r'#### Examples\n\n'
        r'(.+?)\n\n'
        r'#### Related Terms\n\n'
        r'(.+?)\n\n'
        r'#### Cultural Notes\n\n'
        r'(.+?)\n\n'
        r'#### Sources\n\n'
        r'(.+?)\n\n'
        r'---)',
        re.DOTALL
    )
    
    # Also handle sections that might be missing some fields
    simple_pattern = re.compile(
        r'(###\s+(.+?))\n\n'
        r'\*\*Part of Speech:\*\*\s*(.+?)\n\n'
        r'\*\*Definition:\*\*\s*(.+?)(?:\n\n'
        r'\*\*Pronunciation / IPA:\*\*\s*(.+?))?(?:\n\n'
        r'\*\*Etymology:\*\*\s*(.+?))?(?:\n\n'
        r'#### Examples\n\n'
        r'(.+?))?(?:\n\n'
        r'#### Related Terms\n\n'
        r'(.+?))?(?:\n\n'
        r'#### Cultural Notes\n\n'
        r'(.+?))?(?:\n\n'
        r'#### Sources\n\n'
        r'(.+?))?(?=\n\n---|\n\n## Pipeline Form|\Z)',
        re.DOTALL
    )
    
    matches = list(simple_pattern.finditer(content))
    for match in matches:
        full_section = match.group(1)
        word = match.group(2).strip()
        pos = match.group(3).strip()
        definition = match.group(4).strip()
        pronunciation = match.group(5).strip() if match.group(5) else ''
        etymology = match.group(6).strip() if match.group(6) else ''
        examples = match.group(7).strip() if match.group(7) else ''
        related = match.group(8).strip() if match.group(8) else ''
        cultural = match.group(9).strip() if match.group(9) else ''
        sources = match.group(10).strip() if match.group(10) else ''
        
        # Determine section from context (look for ## before this section)
        section_match = re.search(r'(^## .+?)$', content[:match.start()], re.MULTILINE)
        section = section_match.group(1) if section_match else 'General'
        
        words.append({
            'word': word,
            'pos': pos,
            'definition': definition,
            'pronunciation': pronunciation,
            'etymology': etymology,
            'examples': examples,
            'related': related,
            'cultural': cultural,
            'sources': sources,
            'section': section
        })
    
    return words


def generate_etymology_es(word: str, meaning: str) -> str:
    """Generate basic etymology note."""
    if any(c in word for c in 'àáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿ'):
        return f'Palabra española: {word} (origen latino/árabe/germánico según caso)'
    if word in ['karate', 'sushi', 'kimchi', 'taekwondo', 'k-pop', 'hanbok', 'hangul']:
        return f'Préstamo del coreano: {word}'
    return f'Español: {word} (etimología pendiente de investigación)'


def generate_examples_es(word: str, meaning: str, pos: str) -> List[str]:
    """Generate basic example sentences."""
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
    """Generate related term wikilinks."""
    related = []
    if 'sustantivo' in pos.lower():
        related.append(f'[[{word}]] — Autoreferencia')
    elif 'verbo' in pos.lower():
        related.append(f'[[{word}]] — Forma base')
    
    animals = ['perro', 'gato', 'pájaro', 'pez', 'caballo', 'vaca', 'cerdo', 'oveja', 'pollo']
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
    """Generate cultural context notes for Spanish."""
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


def convert_file_es(input_path: Path, output_path: Path):
    """Convert Spanish vocabulary file to ensure all fields are complete."""
    content = input_path.read_text(encoding='utf-8')
    
    # Find header end (before first ### or ## section)
    header_end = content.find('### ')
    if header_end == -1:
        header_end = content.find('## ')
    if header_end == -1:
        print(f"No sections found in {input_path}")
        return
    
    header = content[:header_end].rstrip()
    
    # Extract words from sections
    words = extract_words_from_sections(content)
    
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
            pronunciation = w.get('pronunciation', '')
            meaning = w['definition']
            pos = w['pos']
            etymology = w.get('etymology', generate_etymology_es(word, meaning))
            examples = w.get('examples', '')
            related = w.get('related', '')
            cultural = w.get('cultural', '')
            sources = w.get('sources', '')
            
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
    print(f"Enhanced {input_path.name}: {len(words)} words → {output_path}")


def main():
    vocab_dir = Path('/Users/emilio/projects/Projects/Language/wiki/Spanish/vocabulary')
    
    files_to_enhance = [
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
    
    for fname in files_to_enhance:
        fpath = vocab_dir / fname
        if fpath.exists():
            convert_file_es(fpath, fpath)
        else:
            print(f"File not found: {fpath}")


if __name__ == '__main__':
    import re
    main()