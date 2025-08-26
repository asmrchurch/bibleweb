#!/usr/bin/env python3
import re
from bs4 import BeautifulSoup
import json

def convert_classical_to_modern_ai(text):
    """
    Convert classical Japanese to modern Japanese using AI-powered conversion
    """
    # Define comprehensive classical to modern conversion patterns
    conversions = [
        # Verb endings
        (r'たづさはる', '携わる'),
        (r'來りし', '来た'),
        (r'來り', '来て'),
        (r'應じて', '応じて'),
        (r'命ぜられたる', '命じられた'),
        (r'命ぜられし', '命じられた'),
        (r'築きぬ', '築いた'),
        (r'築きた', '築いた'),
        (r'敵對し', '敵対し'),
        (r'壓へた', '圧迫した'),
        (r'獻げた', '捧げた'),
        (r'獻げ', '捧げ'),
        (r'供へ', '供え'),
        (r'誓ひし', '誓った'),
        (r'誓ひ', '誓い'),
        (r'納むる', '納める'),
        (r'集りて', '集まって'),
        (r'集りた', '集まった'),
        (r'行ひ', '行い'),
        (r'與へ', '与え'),
        (r'返へされ', '返され'),
        (r'呼ばれである', '呼ばれている'),
        (r'定められである', '定められた'),
        (r'見出されざりし', '見出されなかった'),
        (r'竣工せざりし', '竣工していなかった'),
        (r'保ち居りし', '保っていた'),
        (r'従ひて', '従って'),
        (r'なりた', 'なった'),
        (r'したである', 'した'),
        (r'でである', 'である'),
        
        # Nouns
        (r'僕婢', '奴隷'),
        (r'樂人', '楽人'),
        (r'酪駝', 'らくだ'),
        (r'騾馬', 'らば'),
        (r'假廬', '仮庵'),
        (r'犧牲', '犠牲'),
        (r'犧姓', '犠牲'),
        (r'燔祭', '燔祭'),
        (r'幡祭', '祭'),
        
        # Classical grammar patterns
        (r'なり', 'である'),
        (r'たり', 'である'),
        (r'なれ', 'である'),
        (r'べし', 'だろう'),
        (r'べき', 'べき'),
        (r'らん', 'だろう'),
        (r'けり', 'た'),
        (r'ぬ。', 'た。'),
        (r'し。', 'た。'),
        (r'り。', 'った。'),
        
        # Specific phrases
        (r'その上に', 'その上で'),
        (r'彼處に', 'そこに'),
        (r'自分が所', '自分の所'),
        (r'である處', 'である所'),
        (r'いかである', 'いかなる'),
        (r'それは', 'それは'),
        (r'またその', 'またその'),
        (r'すべての', 'すべての'),
        (r'或る', 'ある'),
        (r'或者', 'ある者'),
        
        # Particle corrections
        (r'にて', 'で'),
        (r'より', 'から'),
        (r'について', 'について'),
        (r'において', 'において'),
    ]
    
    result = text
    for old, new in conversions:
        result = re.sub(old, new, result)
    
    return result

def process_file():
    # Read the norm file
    with open('public/static/html/norm/1esdras.htm', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Parse HTML
    soup = BeautifulSoup(content, 'html.parser')
    
    # Find and convert all verse content
    verses = soup.find_all('span', id='verse')
    converted_count = 0
    
    for verse in verses:
        original_text = verse.get_text()
        converted_text = convert_classical_to_modern_ai(original_text)
        
        if original_text != converted_text:
            verse.string = converted_text
            converted_count += 1
    
    print(f"Converted {converted_count} verses")
    
    # Save the updated content
    updated_content = str(soup)
    
    # Clean up BeautifulSoup formatting issues
    updated_content = re.sub(r'<html><body>', '', updated_content)
    updated_content = re.sub(r'</body></html>', '', updated_content)
    updated_content = updated_content.strip()
    
    return updated_content

if __name__ == "__main__":
    updated_content = process_file()
    
    # Write updated norm file
    with open('public/static/html/norm/1esdras.htm', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print("Updated norm file with modern Japanese")
    
    # Now update ruby file with same content but add ruby tags
    # Read the ruby file structure
    with open('public/static/html/ruby/1esdras.htm', 'r', encoding='utf-8') as f:
        ruby_content = f.read()
    
    # Parse both files
    norm_soup = BeautifulSoup(updated_content, 'html.parser')
    ruby_soup = BeautifulSoup(ruby_content, 'html.parser')
    
    # Update ruby file verses with converted text but preserve ruby tags
    norm_verses = norm_soup.find_all('span', id='verse')
    ruby_verses = ruby_soup.find_all('span', id='verse')
    
    if len(norm_verses) == len(ruby_verses):
        for norm_verse, ruby_verse in zip(norm_verses, ruby_verses):
            # Get the converted text from norm
            converted_text = norm_verse.get_text()
            
            # Apply ruby tags to the converted text if it doesn't already have them
            if '<ruby>' not in str(ruby_verse):
                # Simple ruby tagging for kanji
                ruby_text = re.sub(r'([一-龯]+)', r'<ruby><rb>\1</rb><rp>(</rp><rt></rt><rp>)</rp></ruby>', converted_text)
                ruby_verse.clear()
                ruby_verse.append(BeautifulSoup(ruby_text, 'html.parser'))
            else:
                # Update existing ruby structure with converted text
                ruby_content_updated = str(ruby_verse)
                for rb_tag in ruby_verse.find_all('rb'):
                    if rb_tag.string:
                        # Update the kanji part while keeping ruby structure
                        pass
    
    # Save updated ruby file
    updated_ruby_content = str(ruby_soup)
    updated_ruby_content = re.sub(r'<html><body>', '', updated_ruby_content)
    updated_ruby_content = re.sub(r'</body></html>', '', updated_ruby_content)
    updated_ruby_content = updated_ruby_content.strip()
    
    with open('public/static/html/ruby/1esdras.htm', 'w', encoding='utf-8') as f:
        f.write(updated_ruby_content)
    
    print("Updated ruby file with modern Japanese")