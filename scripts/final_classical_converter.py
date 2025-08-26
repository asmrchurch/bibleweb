#!/usr/bin/env python3
import re
from bs4 import BeautifulSoup

def final_classical_cleanup(text):
    """
    Final cleanup of remaining classical Japanese patterns
    """
    
    # Remaining patterns found in the examples
    final_conversions = [
        # Specific remaining issues
        (r'飲み食ひて', '飲み食いして'),
        (r'まはり', '周り'),
        (r'盡し', '尽くし'),
        (r'従はるれば', '従われれば'),
        (r'言いて', '言って'),
        (r'默した', '黙った'),
        (r'語り初む', '語り始める'),
        (r'強からずや', '強いのではないか'),
        (r'にあらずして', 'ではなくて'),
        (r'何者ぞ', '何者であろうか'),
        (r'出づ', '出る'),
        (r'培ふ', '培う'),
        (r'養ひ育た', '養い育てた'),
        (r'加ふ', '加える'),
        (r'在り得ない', 'ありえない'),
        (r'淑かにして', '美しくて'),
        (r'見とれ', '見とれて'),
        (r'開来るまま', '開けたまま'),
        (r'著く', '着く'),
        (r'忘る', '忘れる'),
        
        # Classical verb forms
        (r'([あ-ん])ひて', r'\1いて'),
        (r'([あ-ん])ふ', r'\1う'),
        (r'([あ-ん])づ', r'\1る'),
        (r'([あ-ん])り初む', r'\1り始める'),
        (r'([あ-ん])からず', r'\1くない'),
        (r'([あ-ん])ざる', r'\1ない'),
        (r'([あ-ん])る。', r'\1る。'),
        
        # Classical particles and auxiliaries
        (r'にあらず', 'ではない'),
        (r'にあらずして', 'ではなくて'),
        (r'何者ぞ', '何者だろうか'),
        (r'ことように', 'このように'),
        (r'わがもの', '自分のもの'),
        
        # Classical adjectives
        (r'強き', '強い'),
        (r'善き', '良い'),
        (r'美しき', '美しい'),
        (r'大なる', '大きな'),
        
        # Fix specific grammar issues
        (r'させるを見れば', 'させることを見れば'),
        (r'治めるる', '治める'),
        (r'従はる', '従われる'),
        (r'從ふ', '従う'),
        
        # Classical endings
        (r'なり。', 'である。'),
        (r'たり。', 'である。'),
        (r'けり。', 'た。'),
        (r'つ。', 'た。'),
        
        # More specific patterns
        (r'彼口を', '彼は口を'),
        (r'且彼', 'そして彼は'),
        (r'事毎に', '事ごとに'),
    ]
    
    result = text
    
    # Apply final conversions
    for old_pattern, new_pattern in final_conversions:
        result = re.sub(old_pattern, new_pattern, result)
    
    return result

def apply_final_conversion():
    # Read norm file
    with open('public/static/html/norm/1esdras.htm', 'r', encoding='utf-8') as f:
        content = f.read()
    
    print('Applying final classical Japanese cleanup...')
    
    # Parse HTML
    soup = BeautifulSoup(content, 'html.parser')
    
    # Convert all verse content
    verses = soup.find_all('span', id='verse')
    converted_count = 0
    
    for verse in verses:
        original_text = verse.get_text()
        converted_text = final_classical_cleanup(original_text)
        
        if original_text != converted_text:
            verse.string = converted_text
            converted_count += 1
    
    print(f'Final cleanup converted {converted_count} verses')
    
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
    
    print('Final conversion complete - both files updated')

if __name__ == "__main__":
    apply_final_conversion()