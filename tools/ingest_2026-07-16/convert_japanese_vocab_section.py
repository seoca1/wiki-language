#!/usr/bin/env python3
"""
Convert Japanese vocabulary files with section format (### word + **Reading:** **Meaning:**)
to full AGENTS.md format.
"""

import re
from pathlib import Path
from typing import List, Dict

# POS hints for Japanese
POS_HINTS_JP = {
    # Counters
    '一つ': '助数詞', '二つ': '助数詞', '三つ': '助数詞', '四つ': '助数詞', '五つ': '助数詞',
    '六つ': '助数詞', '七つ': '助数詞', '八つ': '助数詞', '九つ': '助数詞', '十': '助数詞',
    '匹': '助数詞', '頭': '助数詞', '羽': '助数詞', '名': '助数詞', '個': '助数詞',
    '本': '助数詞', '枚': '助数詞', '冊': '助数詞', '台': '助数詞', '杯': '助数詞',
    '着': '助数詞', '足': '助数詞', '軒': '助数詞', '丁': '助数詞', '件': '助数詞',
    '点': '助数詞', '組': '助数詞', '箱': '助数詞', '皿': '助数詞', '束': '助数詞',
    '粒': '助数詞', '錠': '助数詞', '曲': '助数詞', '回': '助数詞', '階': '助数詞',
    '番': '助数詞', '度': '助数詞', '歳': '助数詞', '才': '助数詞', '時': '助数詞',
    '分': '助数詞', '秒': '助数詞', '日': '助数詞', '週間': '助数詞', 'か月': '助数詞',
    '年': '助数詞', '月': '助数詞', '泊': '助数詞',
    # Kanji
    '一': '漢字', '二': '漢字', '三': '漢字', '四': '漢字', '五': '漢字',
    '六': '漢字', '七': '漢字', '八': '漢字', '九': '漢字', '十': '漢字',
    '年': '漢字', '月': '漢字', '日': '漢字', '時': '漢字', '分': '漢字',
    '半': '漢字', '今': '漢字', '毎': '漢字', '火': '漢字', '水': '漢字',
    '木': '漢字', '金': '漢字', '土': '漢字',
    '上': '漢字', '下': '漢字', '中': '漢字', '外': '漢字', '前': '漢字', '後': '漢字',
    '人': '漢字', '私': '漢字', '体': '漢字', '手': '漢字', '目': '漢字', '口': '漢字', '耳': '漢字',
    '父': '漢字', '母': '漢字', '子': '漢字', '友': '漢字',
    '山': '漢字', '川': '漢字', '海': '漢字', '空': '漢字', '天': '漢字', '雨': '漢字', '花': '漢字',
    '行': '漢字', '来': '漢字', '帰': '漢字', '食': '漢字', '飲': '漢字', '見': '漢字', '聞': '漢字', '話': '漢字',
    '読': '漢字', '書': '漢字', '買': '漢字', '売': '漢字', '住': '漢字',
    '大': '漢字', '小': '漢字', '高': '漢字', '安': '漢字', '新': '漢字', '古': '漢字', '良': '漢字', '悪': '漢字',
    '早': '漢字', '寒': '漢字',
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


def extract_words_from_sections(content: str) -> List[Dict]:
    """Extract word entries from section format (### word + **Reading:** **Meaning:** **Usage:**)."""
    words = []
    
    # Pattern for section format used in jp-counters.md and kanji-n5.md
    # Matches: ### Word\n\n**Reading:** ...\n**Meaning:** ...\n**Usage/Note:** ...
    section_pattern = re.compile(
        r'###\s+(.+?)\n\n'
        r'\*\*Reading:\*\*\s*(.+?)\s*\n'
        r'\*\*Meaning:\*\*\s*(.+?)\s*\n'
        r'(?:\*\*Usage:\*\*\s*(.+?)\s*\n|\*\*Note:\*\*\s*(.+?)\s*\n)?'
        r'(?=\n\n### |\n\n---|\Z)',
        re.DOTALL
    )
    
    matches = section_pattern.finditer(content)
    for match in matches:
        word = match.group(1).strip()
        reading = match.group(2).strip()
        meaning = match.group(3).strip()
        usage = match.group(4).strip() if match.group(4) else ''
        note = match.group(5).strip() if match.group(5) else ''
        
        # Determine section from context
        section_match = re.search(r'(^## .+?)$', content[:match.start()], re.MULTILINE)
        section = section_match.group(1) if section_match else 'General'
        
        if word and word not in ['Animals', 'Basic Animals', 'Wild Animals', 'Marine Animals', 'Insects', 'Mythical/Legendary']:
            words.append({
                'word': word,
                'reading': reading,
                'meaning': meaning,
                'usage': usage,
                'note': note,
                'section': section
            })
    
    return words


def infer_pos(word: str, meaning: str) -> str:
    """Infer part of speech."""
    if word in POS_HINTS_JP:
        return POS_HINTS_JP[word]
    meaning_lower = meaning.lower()
    if any(v in meaning_lower for v in ['to ', 'verb', '動詞', 'action', '하다', 'action']):
        return '動詞'
    if any(v in meaning_lower for v in ['adjective', 'adjectival', '形容詞', 'describing', 'quality']):
        return '形容詞'
    if any(v in meaning_lower for v in ['adverb', 'adverbial', '副詞', 'manner', '모양']):
        return '副詞'
    if any(v in meaning_lower for v in ['counter', '助数詞', 'counter', 'counting']):
        return '助数詞'
    if any(v in meaning_lower for v in ['kanji', '漢字', 'character']):
        return '漢字'
    if any(v in meaning_lower for v in ['interjection', '感動詞', 'exclamation']):
        return '感動詞'
    if any(v in meaning_lower for v in ['numeral', '数詞', 'number']):
        return '数詞'
    return '名詞'


def generate_etymology_jp(word: str, meaning: str, reading: str) -> str:
    """Generate basic etymology note."""
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
    elif '助数詞' in pos:
        examples.append(f'{word}一つお願いします。 — 数え方')
    elif '漢字' in pos:
        examples.append(f'{word}（{reading}）— 読み方')
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
    elif '助数詞' in pos:
        related.append(f'[[{word}]] — 助数詞基本形')
    elif '漢字' in pos:
        related.append(f'[[{word}]] — 漢字自体')
    
    # Category-based
    counters = ['一つ', '二つ', '三つ', '四つ', '五つ', '六つ', '七つ', '八つ', '九つ', '十',
                '匹', '頭', '羽', '名', '個', '本', '枚', '冊', '台', '杯', '着', '足', '軒', '丁',
                '件', '点', '組', '箱', '皿', '束', '粒', '錠', '曲', '回', '階', '番', '度', '歳',
                '才', '時', '分', '秒', '日', '週間', 'か月', '年', '月', '泊']
    if word in counters:
        related.append('[[助数詞]] — 日本語の助数詞一覧')
    
    kanji_n5 = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '年', '月', '日', '時', '分', '半', '今', '毎',
                '火', '水', '木', '金', '土', '上', '下', '中', '外', '前', '後', '人', '私', '体', '手', '目', '口', '耳',
                '父', '母', '子', '友', '山', '川', '海', '空', '天', '雨', '花', '行', '来', '帰', '食', '飲', '見', '聞', '話',
                '読', '書', '買', '売', '住', '大', '小', '高', '安', '新', '古', '良', '悪', '早', '寒']
    if word in kanji_n5:
        related.append('[[漢字]] — JLPT N5漢字一覧')
    
    return related


def generate_cultural_notes_jp(word: str, meaning: str, section: str) -> str:
    """Generate cultural context notes for Japanese."""
    notes = []
    
    # Counters
    if '助数詞' in section or word in ['一つ', '二つ', '三つ', '四つ', '五つ', '六つ', '七つ', '八つ', '九つ', '十']:
        notes.append('日本語では物を数えるときに助数詞が必要。品物によって適切な助数詞が変わる。')
    
    if word in ['匹', '頭', '羽', '台', '冊', '本', '枚', '個', '人', '名']:
        notes.append(f'助数詞「{word}」は特定の種類のものを数えるときに使う。')
    
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
    
    # Kanji readings
    if '漢字' in word or '漢字' in section:
        notes.append('漢字には音読み（おんよみ）と訓読み（くんよみ）がある。熟語では音読み、単独では訓読みが多い。')
    
    if not notes:
        notes.append('文化的背景情報を追加予定')
    
    return ' '.join(notes)


def convert_file_jp_section(input_path: Path, output_path: Path):
    """Convert Japanese vocabulary file with section format to full format."""
    content = input_path.read_text(encoding='utf-8')
    
    # Find header end
    header_end = content.find('### ')
    if header_end == -1:
        header_end = content.find('## ')
    if header_end == -1:
        print(f"No sections found in {input_path}")
        return
    
    header = content[:header_end].rstrip()
    
    # Extract words
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
    level = level_match.group(1).strip() if level_match else 'JLPT N5'
    
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
            reading = w['reading']
            meaning = w['meaning']
            note = w.get('note', '')
            pos = infer_pos(word, meaning)
            etymology = generate_etymology_jp(word, meaning, w['reading'])
            
            new_lines.append(f'### {word}')
            new_lines.append('')
            new_lines.append(f'**Part of Speech:** {pos}')
            new_lines.append('')
            new_lines.append(f'**Definition:** {meaning}')
            new_lines.append('')
            new_lines.append(f'**Reading / Hiragana / Romaji:** {w["reading"]}')
            new_lines.append('')
            new_lines.append(f'**Etymology:** {etymology}')
            new_lines.append('')
            new_lines.append('#### Examples')
            new_lines.append('')
            
            for ex in generate_examples_jp(word, meaning, pos, w['reading']):
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
            new_lines.append(f'- [[{input_path.stem}]]')
            new_lines.append('')
            new_lines.append('---')
            new_lines.append('')
    
    if sources_match:
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
    
    # Files with section format that need conversion
    files_to_convert = [
        'jp-counters.md',
        'kanji-n5.md',
    ]
    
    for fname in files_to_convert:
        fpath = vocab_dir / fname
        if fpath.exists():
            convert_file_jp_section(fpath, fpath)
        else:
            print(f"File not found: {fpath}")


if __name__ == '__main__':
    import re
    main()