#!/usr/bin/env python3
"""
Convert English vocabulary files to full AGENTS.md format.
"""

import re
from pathlib import Path
from typing import List, Dict

# POS hints for English
POS_HINTS_EN = {
    # Nouns
    'dog': 'noun', 'cat': 'noun', 'bird': 'noun', 'fish': 'noun', 'horse': 'noun', 'cow': 'noun',
    'hello': 'interjection', 'goodbye': 'interjection', 'thanks': 'interjection', 'please': 'interjection',
    'yes': 'adverb', 'no': 'adverb', 'maybe': 'adverb',
    'one': 'numeral', 'two': 'numeral', 'three': 'numeral', 'four': 'numeral', 'five': 'numeral',
    'six': 'numeral', 'seven': 'numeral', 'eight': 'numeral', 'nine': 'numeral', 'ten': 'numeral',
    'person': 'noun', 'friend': 'noun', 'family': 'noun', 'teacher': 'noun', 'student': 'noun',
    'water': 'noun', 'rice': 'noun', 'book': 'noun', 'time': 'noun', 'country': 'noun',
    'today': 'noun/adverb', 'tomorrow': 'noun/adverb', 'morning': 'noun', 'evening': 'noun',
    'Korea': 'proper noun', 'school': 'noun', 'study': 'noun/verb',
    'email': 'noun', 'address': 'noun', 'sender': 'noun', 'recipient': 'noun', 'subject': 'noun',
    'body': 'noun', 'attachment': 'noun', 'send': 'verb', 'receive': 'verb', 'read': 'verb',
    'save': 'verb', 'delete': 'verb', 'cancel': 'verb',
    'meeting': 'noun', 'schedule': 'noun', 'agenda': 'noun', 'participant': 'noun', 'presentation': 'noun',
    'speech': 'noun', 'discussion': 'noun', 'opinion': 'noun', 'decision': 'noun', 'approval': 'noun',
    'opposition': 'noun', 'agreement': 'noun', 'record': 'noun', 'time': 'noun', 'location': 'noun',
    'postponement': 'noun', 'cancellation': 'noun',
    'presenter': 'noun', 'slide': 'noun', 'materials': 'noun', 'chart': 'noun', 'graph': 'noun',
    'table': 'noun', 'explanation': 'noun', 'summary': 'noun', 'conclusion': 'noun', 'question': 'noun',
    'answer': 'noun', 'rehearsal': 'noun',
    'company': 'noun', 'office': 'noun', 'colleague': 'noun', 'supervisor': 'noun', 'subordinate': 'noun',
    'employee': 'noun', 'representative': 'noun', 'team leader': 'noun', 'project': 'noun', 'work': 'noun',
    'contract': 'noun', 'signing': 'noun', 'sign': 'verb', 'sales': 'noun', 'target': 'noun',
    'achievement': 'noun', 'report': 'noun', 'submission': 'noun', 'submit': 'verb', 'processing': 'noun',
    'process': 'verb', 'confirmation': 'noun', 'confirm': 'verb', 'approval': 'noun', 'approve': 'verb',
    'rejection': 'noun', 'reject': 'verb',
    'price': 'noun', 'cost': 'noun', 'budget': 'noun', 'expenditure': 'noun', 'income': 'noun',
    'profit': 'noun', 'loss': 'noun', 'investment': 'noun', 'cooperation': 'noun', 'partner': 'noun',
    'deposit': 'noun', 'installment': 'noun', 'interest': 'noun', 'exchange rate': 'noun', 'tax': 'noun',
    'filing': 'noun', 'file': 'verb',
    'telephone': 'noun', 'call': 'verb', 'message': 'noun', 'text': 'noun', 'hang up': 'verb',
    'busy': 'adjective', 'phone number': 'noun', 'guidance': 'noun', 'connection': 'noun', 'callback': 'noun',
    # Animals
    'lion': 'noun', 'tiger': 'noun', 'elephant': 'noun', 'monkey': 'noun', 'bear': 'noun',
    'rabbit': 'noun', 'deer': 'noun', 'butterfly': 'noun', 'ant': 'noun',
    # Clothing
    'shirt': 'noun', 'dress': 'noun', 'coat': 'noun', 'skirt': 'noun', 'pants': 'noun',
    'shoes': 'noun', 'sneakers': 'noun', 'hat': 'noun', 'socks': 'noun', 'gloves': 'noun',
    'scarf': 'noun', 'cotton': 'noun', 'silk': 'noun',
    # Nature/Weather
    'sun': 'noun', 'moon': 'noun', 'star': 'noun', 'sky': 'noun', 'cloud': 'noun',
    'rain': 'noun', 'snow': 'noun', 'wind': 'noun', 'storm': 'noun', 'thunder': 'noun',
    'mountain': 'noun', 'sea': 'noun', 'river': 'noun', 'lake': 'noun', 'island': 'noun',
    'ice': 'noun', 'fog': 'noun', 'rainbow': 'noun',
    'spring': 'noun', 'summer': 'noun', 'autumn': 'noun', 'winter': 'noun',
    # Food
    'meat': 'noun', 'chicken': 'noun', 'egg': 'noun', 'cheese': 'noun', 'bread': 'noun',
    'pasta': 'noun', 'onion': 'noun',
    'water': 'noun', 'coffee': 'noun', 'tea': 'noun', 'wine': 'noun', 'beer': 'noun',
    'menu': 'noun', 'order': 'noun/verb', 'waiter': 'noun', 'waitress': 'noun', 'bill': 'noun',
    'tip': 'noun', 'appetizer': 'noun', 'main course': 'noun', 'dessert': 'noun', 'drink': 'noun',
    'restaurant': 'noun', 'delicious': 'adjective', 'sweet': 'adjective', 'spicy': 'adjective', 'recipe': 'noun',
    # Travel
    'passport': 'noun', 'ticket': 'noun', 'boarding pass': 'noun', 'luggage': 'noun', 'suitcase': 'noun',
    'gate': 'noun', 'terminal': 'noun', 'check-in': 'noun', 'flight': 'noun',
    'reservation': 'noun', 'front desk': 'noun', 'room': 'noun', 'single room': 'noun', 'double room': 'noun',
    'suite': 'noun', 'key card': 'noun', 'lobby': 'noun', 'elevator': 'noun',
    'subway': 'noun', 'bus': 'noun', 'taxi': 'noun', 'train': 'noun', 'station': 'noun',
    'stop': 'noun', 'ticket': 'noun', 'platform': 'noun', 'transfer': 'noun', 'airport': 'noun',
    'map': 'noun', 'guide': 'noun', 'tour': 'noun', 'museum': 'noun', 'temple': 'noun',
    'palace': 'noun', 'monument': 'noun', 'beach': 'noun', 'mountain': 'noun', 'park': 'noun',
    # Directions
    'where is': 'phrase', 'how do I get to': 'phrase', 'go straight': 'phrase',
    'turn left': 'phrase', 'turn right': 'phrase', 'left': 'noun', 'right': 'noun',
    'next to': 'preposition', 'across from': 'preposition', 'between': 'preposition',
    'near': 'preposition', 'far': 'adjective',
    # Useful expressions
    'excuse me': 'phrase', 'how much': 'phrase', 'where is the bathroom': 'phrase',
    "I don't understand": 'phrase', 'help me': 'phrase', 'thank you': 'phrase', 'please': 'phrase',
}

THEME_CATEGORIES_EN = {
    'animals-vocabulary': 'animals',
    'basic-vocabulary': 'basic',
    'business-vocabulary': 'business',
    'clothing-vocabulary': 'clothing',
    'emotions-personality-vocabulary': 'emotions-personality',
    'food-vocabulary': 'food',
    'nature-vocabulary': 'nature',
    'travel': 'travel',
}


def extract_words_from_tables(content: str) -> List[Dict]:
    """Extract word entries from markdown tables."""
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
                        ipa = match.group(2).strip()
                        meaning = match.group(3).strip()
                        if word and word not in ['English', 'Español', 'Palabra', 'Kanji', 'Kana', 'Romaji', '단어', '로마자', 'Meaning', 'Significado', '의미', 'Categoría gramatical', 'Connotación', 'Ejemplo']:
                            words.append({
                                'word': word,
                                'ipa': ipa,
                                'meaning': meaning,
                                'section': current_section
                            })
    return words


def infer_pos_en(word: str, meaning: str) -> str:
    """Infer part of speech for English words."""
    if word in POS_HINTS_EN:
        return POS_HINTS_EN[word]
    meaning_lower = meaning.lower()
    if any(v in meaning_lower for v in ['to ', 'action', 'verb']):
        return 'verb'
    if any(v in meaning_lower for v in ['adjective', 'describing']):
        return 'adjective'
    if any(v in meaning_lower for v in ['adverb', 'manner']):
        return 'adverb'
    if any(v in meaning_lower for v in ['preposition', 'conjunction']):
        return 'preposition/conjunction'
    if any(v in meaning_lower for v in ['interjection', 'exclamation']):
        return 'interjection'
    return 'noun'


def generate_etymology_en(word: str, meaning: str) -> str:
    """Generate basic etymology note."""
    # Simple check for likely loanwords
    if any(c in word for c in 'àáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿ'):
        return f'Loanword: {word} (origin varies)'
    if word in ['karaoke', 'sushi', 'kimchi', 'taekwondo', 'k-pop', 'hanbok', 'hangul', 'kimchi', 'bibimbap', 'bulgogi', 'soju', 'makgeolli', 'hanok', 'jeju', 'seoul', 'busan', 'daegu', 'incheon', 'gwangju', 'daejeon', 'ulsan']:
        return f'Korean loanword: {word}'
    return f'English: {word} (etymology research needed)'


def generate_examples_en(word: str, meaning: str, pos: str) -> List[str]:
    """Generate basic example sentences."""
    examples = []
    if pos == 'verb' or pos.startswith('verb'):
        examples.append(f'I {word} every day. — Basic usage')
        examples.append(f'Please {word} this. — Request form')
    elif pos == 'noun' or pos.startswith('noun'):
        examples.append(f'I need a {word}. — Expressing need')
        examples.append(f'The {word} is here. — Location/presence')
    elif pos == 'adjective':
        examples.append(f'It is {word}. — Description')
        examples.append(f'A very {word} day. — Modifying noun')
    elif pos == 'interjection':
        examples.append(f'{word}! — Standalone exclamation')
    elif pos in ['phrase', 'idiom']:
        examples.append(f'{word} — Common expression')
    else:
        examples.append(f'{word} — Example sentence needed')
    return examples


def generate_related_terms_en(word: str, meaning: str, pos: str) -> List[str]:
    """Generate related term wikilinks."""
    related = []
    if pos == 'noun':
        related.append(f'[[{word}]] — Self-reference check')
    elif pos == 'verb':
        related.append(f'[[{word}]] — Base form')
    
    # Category-based
    animals = ['dog', 'cat', 'bird', 'fish', 'horse', 'cow', 'lion', 'tiger', 'elephant', 'monkey', 'bear', 'rabbit', 'deer', 'butterfly', 'ant']
    if word in animals:
        related.append('[[animals]] — Animal vocabulary')
    
    clothing = ['shirt', 'dress', 'coat', 'skirt', 'pants', 'shoes', 'sneakers', 'hat', 'socks', 'gloves', 'scarf', 'cotton', 'silk']
    if word in clothing:
        related.append('[[clothing]] — Clothing vocabulary')
    
    food = ['meat', 'chicken', 'egg', 'cheese', 'bread', 'pasta', 'onion', 'water', 'coffee', 'tea', 'wine', 'beer']
    if word in food:
        related.append('[[food]] — Food vocabulary')
    
    return related


def generate_cultural_notes_en(word: str, meaning: str, section: str) -> str:
    """Generate cultural context notes for English."""
    notes = []
    
    greetings = ['hello', 'goodbye', 'thanks', 'please', 'excuse me']
    if word in greetings:
        notes.append('Essential politeness markers in English-speaking cultures. Used frequently in all social interactions.')
    
    if word in ['please', 'thank you', 'thanks']:
        notes.append('Considered mandatory in requests and responses. Omission can seem rude.')
    
    if word in ['water', 'coffee', 'tea']:
        notes.append('Common beverage offerings in social/business settings.')
    
    if word in ['meeting', 'schedule', 'agenda']:
        notes.append('Business culture emphasizes punctuality and prepared agendas.')
    
    if word in ['tip', 'waiter', 'waitress']:
        notes.append('Tipping 15-20% is standard in US restaurants. Not optional culturally.')
    
    if not notes:
        notes.append('Cultural context to be added')
    
    return ' '.join(notes)


def convert_file_en(input_path: Path, output_path: Path):
    """Convert English vocabulary file to full format."""
    content = input_path.read_text(encoding='utf-8')
    
    # Find header end (before first table)
    header_end = content.find('| English |')
    if header_end == -1:
        header_end = content.find('| Palabra |')
    if header_end == -1:
        print(f"No table found in {input_path}")
        return
    
    header = content[:header_end].rstrip()
    
    # Extract words
    words = extract_words_from_tables(content)
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
    category = THEME_CATEGORIES_EN.get(stem, 'vocabulary')
    
    # Level from header
    level_match = re.search(r'> \*\*Level:\*\*\s*(.+)', header)
    level = level_match.group(1).strip() if level_match else 'A1-B1'
    
    # Build new content
    new_lines = [header.rstrip(), '']
    
    # Group by section
    sections_dict = {}
    for w in words:
        sec = w['section'] or '기타'
        if sec not in sections_dict:
            sections_dict[sec] = []
        sections_dict[sec].append(w)
    
    for section_name, section_words in sections_dict.items():
        new_lines.append(f'{section_name}')
        new_lines.append('')
        
        for w in section_words:
            word = w['word']
            ipa = w.get('ipa', '')
            meaning = w['meaning']
            pos = infer_pos_en(word, meaning)
            
            new_lines.append(f'### {word}')
            new_lines.append('')
            new_lines.append(f'**Part of Speech:** {pos}')
            new_lines.append('')
            new_lines.append(f'**Definition:** {meaning}')
            new_lines.append('')
            new_lines.append(f'**IPA / Pronunciation:** {ipa}')
            new_lines.append('')
            new_lines.append(f'**Etymology:** {generate_etymology_en(word, meaning)}')
            new_lines.append('')
            new_lines.append('#### Examples')
            new_lines.append('')
            for ex in generate_examples_en(word, meaning, pos):
                new_lines.append(f'- {ex}')
            new_lines.append('')
            new_lines.append('#### Related Terms')
            new_lines.append('')
            for rt in generate_related_terms_en(word, meaning, pos):
                new_lines.append(f'- {rt}')
            new_lines.append('')
            new_lines.append('#### Cultural Notes')
            new_lines.append('')
            new_lines.append(generate_cultural_notes_en(word, meaning, section_name))
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
    
    # Add Pipeline Form
    if pipeline_form:
        new_lines.append(pipeline_form)
    
    output_content = '\n'.join(new_lines)
    output_path.write_text(output_content, encoding='utf-8')
    print(f"Converted {input_path.name}: {len(words)} words → {output_path}")


def main():
    vocab_dir = Path('/Users/emilio/projects/Projects/Language/wiki/English/vocabulary')
    
    files_to_convert = [
        'animals-vocabulary.md',
        'basic-vocabulary.md',
        'business-vocabulary.md',
        'clothing-vocabulary.md',
        'emotions-personality-vocabulary.md',
        'food-vocabulary.md',
        'nature-vocabulary.md',
        'travel.md',
    ]
    
    for fname in files_to_convert:
        fpath = vocab_dir / fname
        if fpath.exists():
            convert_file_en(fpath, fpath)
        else:
            print(f"File not found: {fpath}")


if __name__ == '__main__':
    main()