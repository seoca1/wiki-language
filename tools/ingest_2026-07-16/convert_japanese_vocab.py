#!/usr/bin/env python3
"""
Convert Japanese vocabulary files from table format to full AGENTS.md format with sections per word.
"""

import re
from pathlib import Path
from typing import List, Dict

# POS hints for Japanese
POS_HINTS_JP = {
    '犬': '名詞', '猫': '名詞', '馬': '名詞', '牛': '名詞', '豚': '名詞', '鶏': '名詞', '羊': '名詞',
    '鳥': '名詞', '魚': '名詞', '蛇': '名詞', '熊': '名詞', '鹿': '名詞', '猿': '名詞', '亀': '名詞',
    '鯨': '名詞', '鮫': '名詞', 'イルカ': '名詞',
    '蝶': '名詞', 'アリ': '名詞', 'カエル': '名詞',
    '龍': '名詞', '竜': '名詞', '狼': '名詞', '狐': '名詞',
    # Travel
    'パスポート': '名詞', '切符': '名詞', 'ホテル': '名詞', '部屋': '名詞', '予約': '名詞',
    '空港': '名詞', '駅': '名詞', 'タクシー': '名詞', 'バス': '名詞', '電車': '名詞', '地下鉄': '名詞', '地図': '名詞',
    'ガイド': '名詞', 'ツアー': '名詞', '博物館': '名詞', '海': '名詞', '山': '名詞', '公園': '名詞',
    # Nature
    '太陽': '名詞', '月': '名詞', '星': '名詞', '空': '名詞', '雲': '名詞',
    '雨': '名詞', '雪': '名詞', '風': '名詞', '嵐': '名詞', '雷': '名詞',
    '山': '名詞', '海': '名詞', '川': '名詞', '湖': '名詞', '島': '名詞', '氷': '名詞', '霧': '名詞', '虹': '名詞',
    '春': '名詞', '夏': '名詞', '秋': '名詞', '冬': '名詞',
    # Clothing
    'シャツ': '名詞', 'ズボン': '名詞', '靴': '名詞', '靴下': '名詞', 'ジャケット': '名詞',
    'コート': '名詞', '帽子': '名詞', '手袋': '名詞', 'マフラー': '名詞', 'ワンピース': '名詞', 'スカート': '名詞',
    # Food
    '肉': '名詞', '魚': '名詞', '卵': '名詞', 'チーズ': '名詞', 'パン': '名詞',
    'パスタ': '名詞', '玉ねぎ': '名詞',
    '水': '名詞', 'コーヒー': '名詞', 'お茶': '名詞', 'ワイン': '名詞', 'ビール': '名詞',
    'メニュー': '名詞', '注文': '名詞', 'ウェイター': '名詞', 'ウェイトレス': '名詞', '勘定': '名詞', 'チップ': '名詞',
    '前菜': '名詞', 'メイン': '名詞', 'デザート': '名詞', '飲み物': '名詞',
    'レストラン': '名詞', '美味しい': '形容詞', '甘い': '形容詞', '辛い': '形容詞', 'レシピ': '名詞',
    # Daily life
    '起きる': '動詞', 'シャワーを浴びる': '動詞', '着替える': '動詞', '寝る': '動詞', '出かける': '動詞',
    '朝食を食べる': '動詞', '昼食を食べる': '動詞', '夕食を食べる': '動詞',
    '働く': '動詞', '勉強する': '動詞',
    '注文する': '動詞', '欲しい': '動詞', '味見する': '動詞', '予約する': '動詞',
    # Business
    '会社': '名詞', 'オフィス': '名詞', '同僚': '名詞', '上司': '名詞', '部下': '名詞',
    '社員': '名詞', '社長': '名詞', '課長': '名詞', 'プロジェクト': '名詞', '仕事': '名詞',
    '契約': '名詞', '契約する': '動詞', '売上': '名詞', '目標': '名詞', '達成': '名詞',
    '報告書': '名詞', '提出する': '動詞', '処理する': '動詞', '確認する': '動詞', '承認する': '動詞',
    '拒否する': '動詞', '価格': '名詞', '費用': '名詞', '予算': '名詞', '支出': '名詞',
    '収入': '名詞', '利益': '名詞', '損失': '名詞', '投資': '名詞', '協力': '名詞', 'パートナー': '名詞',
    '手付金': '名詞', '分割払い': '名詞', '利子': '名詞', '為替レート': '名詞', '税金': '名詞',
    '申告': '名詞', '申告する': '動詞',
    '電話': '名詞', '電話する': '動詞', 'メッセージ': '名詞', 'メール': '名詞', '切る': '動詞',
    '通話中': '名詞', '電話番号': '名詞', '案内': '名詞', '繋ぐ': '動詞', '掛け直す': '動詞',
    # Grammar specific
    '助数詞': '名詞', '漢字': '名詞',
}

THEME_CATEGORIES_JP = {
    'animals-vocabulary': 'animals',
    'business-vocabulary': 'business',
    'clothing-vocabulary': 'clothing',
    'emotions-personality-vocabulary': 'emotions-personality',
    'food-vocabulary': 'food',
    'jp-counters': 'counters',
    'kanji-n5': 'kanji',
    'nature-vocabulary': 'nature',
    'travel': 'travel',
}


def extract_words_from_tables(content: str) -> List[Dict]:
    """Extract word entries from markdown tables."""
    words = []
    
    # Find all tables
    table_pattern = re.compile(r'\|([^|]+)\|([^|]+)\|([^|]+)\|')
    
    # Split by sections to get context
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
                        reading = match.group(2).strip()
                        meaning = match.group(3).strip()
                        if word and word not in ['Word', 'Kanji', '単語', 'Kana', '読み', 'Romaji', 'Meaning', '意味']:
                            words.append({
                                'word': word,
                                'reading': reading,
                                'meaning': meaning,
                                'section': current_section
                            })
    return words


def extract_words_from_sections(content: str) -> List[Dict]:
    """Extract from section format (### word)."""
    words = []
    
    section_pattern = re.compile(
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
        r'(.+?))?(?=\n\n---\n\n###|\n\n---\n\n## Pipeline Form|\n\n---\n\n## Sources|\Z)',
        re.DOTALL
    )
    
    for match in section_pattern.finditer(content):
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
        
        # Determine section from context
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


def infer_pos(word: str, meaning: str) -> str:
    """Infer part of speech."""
    if word in POS_HINTS_JP:
        return POS_HINTS_JP[word]
    meaning_lower = meaning.lower()
    if any(v in meaning_lower for v in ['to ', 'verb', '動詞', 'action']):
        return '動詞'
    if any(v in meaning_lower for v in ['adjective', 'adjectival', '形容詞', 'describing']):
        return '形容詞'
    if any(v in meaning_lower for v in ['adverb', 'adverbial', '副詞', 'manner']):
        return '副詞'
    if any(v in meaning_lower for v in ['preposition', 'prepositional', '前置詞', 'conjunction', 'conjunctional', '接続詞']):
        return '前置詞/接続詞'
    if any(v in meaning_lower for v in ['interjection', 'interjectional', '感動詞', 'exclamation']):
        return '感動詞'
    if any(v in meaning_lower for v in ['numeral', 'number', '数詞', '数']):
        return '数詞'
    return '名詞'


def generate_etymology_jp(word: str, meaning: str) -> str:
    """Generate basic etymology note."""
    if any(c in word for c in '一二三四五六七八九十百千万億'):
        return f'漢数字: {word}'
    if all('\u3040' <= c <= '\u309F' for c in word):  # Hiragana
        return f'和語: {word} (語源調査必要)'
    if all('\u30A0' <= c <= '\u30FF' for c in word):  # Katakana
        return f'外来語: {word}'
    if any('\u4E00' <= c <= '\u9FFF' for c in word):  # Kanji
        return f'漢字: {word} (音読み/訓読みによる語源)'
    return f'日本語: {word} (語源調査必要)'


def generate_examples_jp(word: str, meaning: str, pos: str, reading: str = '') -> List[str]:
    """Generate basic example sentences."""
    examples = []
    if '動詞' in pos:
        examples.append(f'{word}ます。 — 基本用法')
        examples.append(f'please {word}てください。 — 依頼形')
    elif '名詞' in pos:
        examples.append(f'{word}が必要です。 — 必要表現')
        examples.append(f'{word}はここにあります。 — 位置/存在')
    elif '形容詞' in pos:
        examples.append(f'とても{word}です。 — 描写')
        examples.append(f'{word}日です。 — 修飾')
    elif '感動詞' in pos:
        examples.append(f'¡{word}! — 独立した感嘆')
    elif '数詞' in pos:
        examples.append(f'{word}冊あります。 — 計数')
    else:
        examples.append(f'{word} — 例文作成必要')
    return examples


def generate_related_terms_jp(word: str, meaning: str, pos: str) -> List[str]:
    """Generate related term wikilinks."""
    related = []
    if '名詞' in pos:
        related.append(f'[[{word}]] — 自動参照')
    elif '動詞' in pos:
        related.append(f'[[{word}]] — 基本形')
    
    animals = ['犬', '猫', '鳥', '魚', '馬', '牛', '豚', '羊', '鶏', '蛇', '熊', '鹿', '猿', '亀',
               '鯨', '鮫', 'イルカ', '蝶', 'アリ', 'カエル', '龍', '竜', '狼', '狐']
    if word in animals:
        related.append('[[動物]] — 動物語彙')
    
    food = ['肉', '魚', '卵', 'チーズ', 'パン', 'パスタ', '玉ねぎ', '水', 'コーヒー', 'お茶', 'ワイン', 'ビール']
    if word in food:
        related.append('[[食べ物]] — 食べ物語彙')
    
    clothing = ['シャツ', 'ズボン', '靴', '靴下', 'ジャケット', 'コート', '帽子', '手袋', 'マフラー', 'ワンピース', 'スカート']
    if word in clothing:
        related.append('[[服]] — 服語彙')
    
    return related


def generate_cultural_notes_jp(word: str, meaning: str, section: str) -> str:
    """Generate cultural context notes for Japanese."""
    notes = []
    
    # Counters
    if '助数詞' in section or word in ['匹', '頭', '羽', '台', '冊', '本', '枚', '個', '人', '名']:
        notes.append('日本語では物を数えるときに助数詞が必要。品物によって適切な助数詞が変わる。')
    
    # Politeness
    if word in ['です', 'ます', 'ください', 'お願いします']:
        notes.append('日本語の丁寧語（ていねいご）。ビジネスや初対面で必須。')
    
    if word in ['ございます', 'いただきます', 'ごちそうさま']:
        notes.append('敬語（けいご）の基本。尊敬語・謙譲語・丁寧語の使い分けが重要。')
    
    # Food culture
    if word in ['いただきます', 'ごちそうさま']:
        notes.append('食事の前後の決まり文句。感謝の気持ちを表す。省略すると無礼。')
    
    if word in ['お箸', '茶碗', '汁椀']:
        notes.append('和食のマナー：箸の持ち方、茶碗を持って食べる、音を立てない。')
    
    # Business
    if word in ['名刺', '挨拶', 'お辞儀']:
        notes.append('ビジネスマナー：名刺交換は両手で、挨拶はお辞儀、目上の人には深く。')
    
    # Seasonal
    if word in ['お正月', 'お盆', 'クリスマス', 'バレンタイン', 'ホワイトデー']:
        notes.append('日本の季節行事：お正月＝家族集合、お盆＝先祖供養、バレンタイン＝女性→男性、ホワイトデー＝お返し。')
    
    # Onomatopoeia
    if any(c in word for c in 'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん'):
        if len(word) <= 4 and word.endswith(('り', 'ら', 'る', 'ん', 'っ', 'ん')):
            notes.append('擬音語・擬態語（ぎおんご・ぎたいご）が豊富。日常会話で頻出。')
    
    if not notes:
        notes.append('文化的背景情報を追加予定')
    
    return ' '.join(notes)


def convert_file_jp(input_path: Path, output_path: Path):
    """Convert Japanese vocabulary file to full format."""
    content = input_path.read_text(encoding='utf-8')
    
    # Find header end
    header_end = content.find('| Word |')
    if header_end == -1:
        header_end = content.find('### ')
    if header_end == -1:
        print(f"No table or section found in {input_path}")
        return
    
    header = content[:header_end].rstrip()
    
    # Extract words from tables
    words = extract_words_from_tables(content)
    
    # Also try section format
    if not words:
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
    category = THEME_CATEGORIES_JP.get(stem, 'vocabulary')
    
    # Level from header
    level_match = re.search(r'> \*\*Level:\*\*\s*(.+)', header)
    level = level_match.group(1).strip() if level_match else 'JLPT N4-N5'
    
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
            reading = w.get('reading', '')
            meaning = w['meaning']
            pos = w.get('pos', infer_pos(word, meaning))
            etymology = w.get('etymology', generate_etymology_jp(word, meaning))
            examples = w.get('examples', [])
            category_gram = w.get('category_gram', '')
            
            new_lines.append(f'### {word}')
            new_lines.append('')
            new_lines.append(f'**Part of Speech:** {pos}')
            new_lines.append('')
            new_lines.append(f'**Definition:** {meaning}')
            new_lines.append('')
            new_lines.append(f'**Reading / Hiragana / Romaji:** {reading}')
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
                for ex in generate_examples_jp(word, meaning, pos, reading):
                    new_lines.append(f'- {ex}')
            
            new_lines.append('')
            new_lines.append('#### Related Terms')
            new_lines.append('')
            for rt in generate_related_terms_jp(word, meaning, pos):
                new_lines.append(f'- {rt}')
            new_lines.append('')
            new_lines.append('#### Cultural Notes')
            new_lines.append('')
            new_lines.append(generate_cultural_notes_jp(word, meaning, section_name))
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
    vocab_dir = Path('/Users/emilio/projects/Projects/Language/wiki/Japanese/vocabulary')
    
    files_to_convert = [
        'animals-vocabulary.md',
        'business-vocabulary.md',
        'clothing-vocabulary.md',
        'emotions-personality-vocabulary.md',
        'food-vocabulary.md',
        'jp-counters.md',
        'kanji-n5.md',
        'nature-vocabulary.md',
        'travel.md',
    ]
    
    for fname in files_to_convert:
        fpath = vocab_dir / fname
        if fpath.exists():
            convert_file_jp(fpath, fpath)
        else:
            print(f"File not found: {fpath}")


if __name__ == '__main__':
    import re
    main()