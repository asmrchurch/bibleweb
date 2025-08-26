#!/usr/bin/env python3
import re
from bs4 import BeautifulSoup

def comprehensive_classical_to_modern(text):
    """
    Comprehensive classical Japanese to modern Japanese conversion
    Based on extensive classical patterns found in the text
    """
    
    # Comprehensive conversion patterns
    conversions = [
        # Specific examples from user feedback
        (r'されど', 'しかし'),
        (r'させし', 'させた'),
        (r'覺え', '覚え'),
        (r'あらずや', 'ではないか'),
        (r'語りて', '語って'),
        (r'噤みた', '黙った'),
        (r'なさしむる', 'させる'),
        (r'さしむる', 'させる'),
        
        # Additional classical patterns from Chapter 4
        (r'語りしもの', '語った者'),
        (r'言ひ始む', '言い始める'),
        (r'治めるる', '治める'),
        (r'優れずや', '優れているのではないか'),
        (r'強た', '強い'),
        (r'従ふ', '従う'),
        (r'戦へといはば', '戦えと言えば'),
        (r'戦はん', '戦うだろう'),
        (r'遣わさば', '送れば'),
        (r'打ち毀たん', '打ち壊すだろう'),
        (r'背かない', '背かない'),
        (r'携え来だろう', '持って来るだろう'),
        (r'あらない', 'でない'),
        (r'關係なく', '関係なく'),
        (r'蒔きし', '蒔いた'),
        (r'携え来り', '持って来て'),
        (r'納めん', '納めるだろう'),
        (r'げに', '実に'),
        (r'唯の', 'ただの'),
        (r'殺せといはば', '殺せと言えば'),
        (r'赦せといはば', '赦せと言えば'),
        (r'打てといはば', '打てと言えば'),
        (r'荒せといはば', '荒らせと言えば'),
        (r'築けといはば', '築けと言えば'),
        (r'築た', '築く'),
        (r'切れといはば', '切れと言えば'),
        (r'植ゑよといはば', '植えよと言えば'),
        (r'植ゑん', '植えるだろう'),
        
        # General classical verb endings
        (r'([あ-ん])りし', r'\1った'),
        (r'([あ-ん])りて', r'\1って'),
        (r'([あ-ん])しもの', r'\1した者'),
        (r'([あ-ん])はん', r'\1うだろう'),
        (r'([あ-ん])らん', r'\1るだろう'),
        (r'([あ-ん])べし', r'\1べきである'),
        (r'([あ-ん])べき', r'\1べき'),
        (r'([あ-ん])たり', r'\1である'),
        (r'([あ-ん])なり', r'\1である'),
        
        # Classical auxiliary verbs and particles
        (r'といはば', 'と言えば'),
        (r'いはば', '言えば'),
        (r'なれば', 'なので'),
        (r'ゆえに', 'ゆえに'),
        (r'もし', 'もし'),
        (r'たとひ', 'たとえ'),
        
        # Classical adjective endings
        (r'([あ-ん])き', r'\1い'),
        (r'([あ-ん])かり', r'\1く'),
        (r'([あ-ん])から', r'\1いので'),
        
        # Classical copula variations
        (r'である', 'である'),  # Keep modern copula
        (r'なりしか', 'であったか'),
        (r'なりき', 'であった'),
        
        # Specific word replacements
        (r'許に', '所に'),
        (r'許へ', '所へ'),
        (r'毀たん', '壊すだろう'),
        (r'來り', '来て'),
        (r'來る', '来る'),
        (r'來た', '来た'),
        (r'往き', '行き'),
        (r'往く', '行く'),
        (r'往た', '行った'),
        
        # Numbers and counters (keep modern forms)
        (r'一つ', '一つ'),
        (r'二つ', '二つ'),
        (r'三つ', '三つ'),
        
        # Classical sentence endings
        (r'ぬ。', 'た。'),
        (r'り。', 'った。'),
        (r'けり。', 'た。'),
        (r'つ。', 'た。'),
        (r'ん。', 'るだろう。'),
        (r'べし。', 'べきである。'),
        
        # Conditional forms
        (r'ば、', 'ば、'),  # Keep modern conditional
        (r'なば、', 'なら、'),
        (r'らば、', 'なら、'),
        
        # Classical question particles
        (r'や。', 'か。'),
        (r'かな。', 'だろうか。'),
        
        # Honorific and humble forms (simplify)
        (r'給ふ', 'くださる'),
        (r'給へ', 'ください'),
        (r'申す', '言う'),
        (r'申し', '言い'),
        
        # Fix specific remaining issues
        (r'最も強た', '最も強い'),
        (r'かれは', '彼は'),
        (r'彼互に', '彼らが互いに'),
    ]
    
    result = text
    
    # Apply conversions
    for old_pattern, new_pattern in conversions:
        result = re.sub(old_pattern, new_pattern, result)
    
    # Additional cleanup for common patterns missed
    result = re.sub(r'([あ-ん])ずや', r'\1ないか', result)
    result = re.sub(r'([あ-ん])ざる', r'\1ない', result)
    result = re.sub(r'([あ-ん])ざり', r'\1なかった', result)
    
    return result

def process_files():
    # Read norm file
    with open('public/static/html/norm/1esdras.htm', 'r', encoding='utf-8') as f:
        content = f.read()
    
    print('Starting comprehensive classical to modern conversion...')
    
    # Parse HTML
    soup = BeautifulSoup(content, 'html.parser')
    
    # Convert all verse content
    verses = soup.find_all('span', id='verse')
    converted_count = 0
    
    for verse in verses:
        original_text = verse.get_text()
        converted_text = comprehensive_classical_to_modern(original_text)
        
        if original_text != converted_text:
            verse.string = converted_text
            converted_count += 1
    
    print(f'Converted {converted_count} verses with comprehensive patterns')
    
    # Save updated norm file
    updated_content = str(soup)
    updated_content = re.sub(r'<html><body>', '', updated_content)
    updated_content = re.sub(r'</body></html>', '', updated_content)
    updated_content = updated_content.strip()
    
    with open('public/static/html/norm/1esdras.htm', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    # Update ruby file with same content
    with open('public/static/html/ruby/1esdras.htm', 'r', encoding='utf-8') as f:
        ruby_content = f.read()
    
    ruby_soup = BeautifulSoup(ruby_content, 'html.parser')
    ruby_verses = ruby_soup.find_all('span', id='verse')
    norm_soup = BeautifulSoup(updated_content, 'html.parser')
    norm_verses = norm_soup.find_all('span', id='verse')
    
    # Update ruby verses
    for ruby_verse, norm_verse in zip(ruby_verses, norm_verses):
        ruby_verse.string = norm_verse.get_text()
    
    # Save updated ruby file
    updated_ruby_content = str(ruby_soup)
    updated_ruby_content = re.sub(r'<html><body>', '', updated_ruby_content)
    updated_ruby_content = re.sub(r'</body></html>', '', updated_ruby_content)
    updated_ruby_content = updated_ruby_content.strip()
    
    with open('public/static/html/ruby/1esdras.htm', 'w', encoding='utf-8') as f:
        f.write(updated_ruby_content)
    
    print('Updated both norm and ruby files with comprehensive modern Japanese')

if __name__ == "__main__":
    process_files()