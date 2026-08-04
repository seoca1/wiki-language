#!/usr/bin/env python3
"""
Convert table-format vocabulary files to full AGENTS.md format with sections per word.
Reads the existing theme file, extracts words from tables, and rewrites with full sections.
Preserves Pipeline Form YAML at the end.
"""

import re
import sys
from pathlib import Path
from typing import List, Dict, Tuple, Optional

# Category mapping for POS hints
POS_HINTS = {
    # Nouns (명사)
    '회사': '명사', '사무실': '명사', '동료': '명사', '상사': '명사', '부하': '명사',
    '직원': '명사', '대표': '명사', '팀장': '명사', '프로젝트': '명사', '업무': '명사',
    '계약': '명사', '체결': '명사', '매출': '명사', '목표': '명사', '달성': '명사',
    '보고서': '명사', '제출': '명사', '처리': '명사', '확인': '명사', '승인': '명사',
    '거절': '명사', '가격': '명사', '비용': '명사', '예산': '명사', '지출': '명사',
    '수입': '명사', '이익': '명사', '손실': '명사', '투자': '명사', '협력': '명사',
    '파트너': '명사', '계약금': '명사', '이자': '명사', '환율': '명사', '세금': '명사',
    '신고': '명사', '전화': '명사', '메시지': '명사', '문자': '명사', '전화번호': '명사',
    '안내': '명사', '연결': '명사', '재통화': '명사', '회의': '명사', '일정': '명사',
    '안건': '명사', '참석자': '명사', '발표': '명사', '발언': '명사', '토론': '명사',
    '의견': '명사', '결정': '명사', '찬성': '명사', '반대': '명사', '합의': '명사',
    '기록': '명사', '시간': '명사', '장소': '명사', '연기': '명사', '취소': '명사',
    '발표자': '명사', '슬라이드': '명사', '자료': '명사', '차트': '명사', '그래프': '명사',
    '표': '명사', '설명': '명사', '요약': '명사', '결론': '명사', '질문': '명사',
    '답변': '명사', '리허설': '명사', '이메일': '명사', '주소': '명사', '보낸 사람': '명사',
    '받는 사람': '명사', '제목': '명사', '본문': '명사', '첨부': '명사',
    # Verbs (동사)
    '보내다': '동사', '받다': '동사', '읽다': '동사', '저장': '동사', '삭제': '동사',
    '취소': '동사', '체결하다': '동사', '제출하다': '동사', '처리하다': '동사',
    '확인하다': '동사', '승인하다': '동사', '거절하다': '동사', '신고하다': '동사',
    '전화하다': '동사', '끊다': '동사',
    # Numbers/Time
    '하나': '수사', '둘': '수사', '셋': '수사', '넷': '수사', '다섯': '수사',
    '여섯': '수사', '일곱': '수사', '여덟': '수사', '아홉': '수사', '열': '수사',
    '오늘': '명사/부사', '내일': '명사/부사', '아침': '명사', '저녁': '명사',
    # People
    '사람': '명사', '친구': '명사', '가족': '명사', '선생님': '명사/호칭', '학생': '명사',
    # Objects
    '물': '명사', '밥': '명사', '책': '명사', '시간': '명사', '나라': '명사',
    '한국': '고유명사', '학교': '명사', '공부': '명사/동사',
    # Greetings
    '안녕하세요': '감탄사/인사말', '감사합니다': '감탄사/인사말', '죄송합니다': '감탄사/인사말',
    '네': '감탄사/응답어', '아니요': '감탄사/응답어',
}

# Category mapping for sub-themes
THEME_CATEGORIES = {
    'business-vocabulary': 'business',
    'topik1-starter': 'topik1',
    'food-vocabulary': 'food',
    'emotions-personality-vocabulary': 'emotions-personality',
    '동물 어휘': 'animals',
    '여행': 'travel',
    '의류・패션 어휘': 'clothing',
    '자연・날씨 어휘': 'nature',
}


def extract_words_from_tables(content: str) -> List[Dict]:
    """Extract word entries from markdown tables in the content."""
    words = []
    
    # Find all tables
    table_pattern = re.compile(r'\|([^|]+)\|([^|]+)\|([^|]+)\|')
    
    # Split by sections to get context
    sections = re.split(r'^(##?\s+.+)$', content, flags=re.MULTILINE)
    
    current_section = ""
    for i, part in enumerate(sections):
        part = part.strip()
        if not part:
            continue
        if part.startswith('#'):
            current_section = part
        else:
            # Look for table rows in this section
            lines = part.split('\n')
            for line in lines:
                line = line.strip()
                if line.startswith('|') and line.endswith('|') and '---' not in line:
                    match = table_pattern.match(line)
                    if match:
                        word = match.group(1).strip()
                        romaja = match.group(2).strip()
                        meaning = match.group(3).strip()
                        if word and word not in ['단어', '단어', '---', 'Palabra', 'English', 'Español', 'Pronunciación', 'Significado', 'Categoría gramatical', 'Connotación', 'Ejemplo', 'Kanji', 'Kana', 'Romaji', 'Meaning']:
                            words.append({
                                'word': word,
                                'romaja': romaja,
                                'meaning': meaning,
                                'section': current_section
                            })
    return words


def extract_words_from_bullet_lists(content: str) -> List[Dict]:
    """Extract word entries from bullet list format (like 여행.md)."""
    words = []
    
    # Split by sections
    sections = re.split(r'^(##?\s+.+)$', content, flags=re.MULTILINE)
    
    current_section = ""
    current_pos = ""  # 명사, 동사, etc.
    
    for i, part in enumerate(sections):
        part = part.strip()
        if not part:
            continue
        if part.startswith('#'):
            current_section = part
            # Check if it's a part-of-speech header
            if '명사' in part or '동사' in part or '형용사' in part or '표현' in part:
                current_pos = part.replace('#', '').strip()
        else:
            # Look for bullet list items: **- word** — meaning
            bullet_pattern = re.compile(r'[-*]\s+\*\*(.+?)\*\s*[—-]\s*(.+)')
            lines = part.split('\n')
            for line in lines:
                line = line.strip()
                match = bullet_pattern.match(line)
                if match:
                    word = match.group(1).strip()
                    meaning = match.group(2).strip()
                    if word and meaning:
                        words.append({
                            'word': word,
                            'romaja': '',  # Not in this format
                            'meaning': meaning,
                            'section': f"{current_section} > {current_pos}" if current_pos else current_section,
                            'pos_hint': '명사' if '명사' in current_pos else ('동사' if '동사' in current_pos else '표현')
                        })
    return words


def infer_pos(word: str, meaning: str) -> str:
    """Infer part of speech from word and meaning."""
    # Check hints first
    if word in POS_HINTS:
        return POS_HINTS[word]
    
    # Check meaning for verb indicators
    meaning_lower = meaning.lower()
    if any(v in meaning_lower for v in ['to ', 'to be ', 'to have ']):
        return '동사'
    if any(v in meaning_lower for v in ['이다', '하다', '되다', '있다', '없다']):
        return '동사'
    if '수사' in meaning or word in ['하나', '둘', '셋', '넷', '다섯', '여섯', '일곱', '여덟', '아홉', '열']:
        return '수사'
    if word in ['안녕하세요', '감사합니다', '죄송합니다', '네', '아니요']:
        return '감탄사/인사말'
    
    return '명사'


def generate_etymology(word: str, meaning: str) -> str:
    """Generate basic etymology note."""
    # Hanja words
    hanja_pattern = re.compile(r'[가-힣]+')
    if hanja_pattern.match(word) and len(word) <= 3:
        return f'한자어: {word} (확인 필요)'
    # Loanwords
    if any(c in word for c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        return f'외래어: {word}'
    # Native Korean
    return f'고유어: {word} (어원 추적 필요)'


def generate_examples(word: str, meaning: str, romaja: str, pos: str) -> List[str]:
    """Generate basic example sentences."""
    examples = []
    
    if pos == '동사' or '하다' in word:
        examples.append(f'{word} — 기본 활용 예문 필요')
        examples.append(f'{word}요/합니다 — 정중/평어 변형 예문 필요')
    elif pos == '명사':
        examples.append(f'{word}이/가 필요해요. — {meaning} 필요 표현')
        examples.append(f'{word} 주세요. — {meaning} 요청 표현')
    elif pos == '수사':
        examples.append(f'{word} 개 주세요. — 개수 요청')
        examples.append(f'{word} 명이에요. — 인원 수 표현')
    else:
        examples.append(f'{word} — 예문 작성 필요')
    
    return examples


def generate_related_terms(word: str, meaning: str, pos: str) -> List[str]:
    """Generate related term wikilinks."""
    related = []
    
    # Add common semantic relations
    if pos == '명사':
        related.append(f'[[{word}]] — 동일어 반복 확인')
    elif pos == '동사':
        related.append(f'[[{word.replace("하다", "")}]] — 어간 확인')
    
    # Category-based
    if '회사' in word or '사무실' in word or '업무' in word:
        related.append('[[직장]] — 직장 관련 어휘')
    if '회의' in word or '발표' in word:
        related.append('[[회의]] — 회의 관련 어휘')
    if '이메일' in word or '메시지' in word:
        related.append('[[커뮤니케이션]] — 소통 관련 어휘')
    
    return related


def generate_cultural_notes(word: str, meaning: str, section: str) -> str:
    """Generate cultural context notes."""
    notes = []
    
    if '수고하세요' in word:
        notes.append('직장/상점에서 일하는 사람께 인사할 때 씀. 윗사람께는 "수고하십시오" 권장.')
    elif '열공하세요' in word:
        notes.append('젊은 층/온라인에서 격려로 씀. "열심히 공부하세요" 줄임말.')
    elif '사장님' in word or '대표' in word:
        notes.append('한국 직장 문화에서 직함+님 필수. 이름+씨는 동료 간.')
    elif '팀장' in word or '상사' in word:
        notes.append('호칭 문화: 팀장님, 부장님, 차장님 등 직함+님 표준.')
    elif '식사' in meaning or '밥' in word:
        notes.append('"밥 먹었어요?"는 안부 인사 겸용. 실제 식사 여부보다 관계 유지 목적 강함.')
    elif '친구' in word:
        notes.append('한국에서 "친구"는 동갑 전제. 나이 차이면 형/누나, 동생으로 호칭.')
    elif '감사' in word or '죄송' in word:
        notes.append('한국어 감사/사과 표현 빈도 매우 높음. 생략 시 무례하게 여겨짐.')
    
    if not notes:
        notes.append('문화적 맥락 추가 필요')
    
    return ' '.join(notes)


def convert_file(input_path: Path, output_path: Path):
    """Convert a vocabulary file to full format."""
    content = input_path.read_text(encoding='utf-8')
    
    # Extract header (before first table)
    header_end = content.find('| 단어 |')
    if header_end == -1:
        header_end = content.find('| Palabra |')
    if header_end == -1:
        header_end = content.find('| English |')
    
    if header_end == -1:
        print(f"No table found in {input_path}")
        return
    
    header = content[:header_end].rstrip()
    
    # Extract words from tables
    words = extract_words_from_tables(content)
    
    # Also extract from bullet lists (for files like 여행.md)
    bullet_words = extract_words_from_bullet_lists(content)
    words.extend(bullet_words)
    
    if not words:
        print(f"No words extracted from {input_path}")
        return
    
    # Extract Pipeline Form YAML
    pipeline_match = re.search(r'(## Pipeline Form.*?```)', content, re.DOTALL)
    pipeline_form = pipeline_match.group(1) if pipeline_match else ''
    
    # Extract Sources section
    sources_match = re.search(r'(## Sources\s*\n.*?)(?=\n##|\n---|\Z)', content, re.DOTALL)
    sources_section = sources_match.group(1).strip() if sources_match else ''
    
    # Determine theme category
    stem = input_path.stem
    category = THEME_CATEGORIES.get(stem, 'vocabulary')
    
    # Build new content
    new_lines = [header.rstrip(), '']
    
    # Group words by section
    sections_dict = {}
    for w in words:
        sec = w['section'] or '기타'
        if sec not in sections_dict:
            sections_dict[sec] = []
        sections_dict[sec].append(w)
    
    # Write sections
    for section_name, section_words in sections_dict.items():
        new_lines.append(f'{section_name}')
        new_lines.append('')
        
        for w in section_words:
            word = w['word']
            romaja = w['romaja']
            meaning = w['meaning']
            pos = infer_pos(word, meaning)
            
            new_lines.append(f'### {word}')
            new_lines.append('')
            new_lines.append(f'**Part of Speech:** {pos}')
            new_lines.append('')
            new_lines.append(f'**Definition:** {meaning}')
            new_lines.append('')
            new_lines.append(f'**Romaja / IPA / Pronunciación:** {romaja}')
            new_lines.append('')
            new_lines.append(f'**Etymology:** {generate_etymology(word, meaning)}')
            new_lines.append('')
            new_lines.append('#### Examples')
            new_lines.append('')
            for ex in generate_examples(word, meaning, romaja, pos):
                new_lines.append(f'- {ex}')
            new_lines.append('')
            new_lines.append('#### Related Terms')
            new_lines.append('')
            for rt in generate_related_terms(word, meaning, pos):
                new_lines.append(f'- {rt}')
            new_lines.append('')
            new_lines.append('#### Cultural Notes')
            new_lines.append('')
            new_lines.append(generate_cultural_notes(word, meaning, section_name))
            new_lines.append('')
            new_lines.append('#### Sources')
            new_lines.append('')
            new_lines.append(f'- [[{stem}]]')
            new_lines.append('')
            new_lines.append('---')
            new_lines.append('')
    
    # Add Sources section
    if sources_section:
        new_lines.append(sources_section)
        new_lines.append('')
    
    # Add Related section if exists
    related_match = re.search(r'(## Related\s*\n.*?)(?=\n##|\n---|\Z)', content, re.DOTALL)
    if related_match:
        new_lines.append(related_match.group(1).strip())
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
    vocab_dir = Path('/Users/emilio/projects/Projects/Language/wiki/Korean/vocabulary')
    
    # Files to convert (table format → full format)
    files_to_convert = [
        'business-vocabulary.md',
        'emotions-personality-vocabulary.md',
        'food-vocabulary.md',
        '동물 어휘.md',
        '여행.md',
        '의류・패션 어휘.md',
        '자연・날씨 어휘.md',
    ]
    
    for fname in files_to_convert:
        fpath = vocab_dir / fname
        if fpath.exists():
            convert_file(fpath, fpath)
        else:
            print(f"File not found: {fpath}")


if __name__ == '__main__':
    main()