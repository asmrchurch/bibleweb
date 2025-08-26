#!/usr/bin/env python3
import re
from bs4 import BeautifulSoup

def advanced_classical_conversion(text):
    """
    More comprehensive classical to modern Japanese conversion
    """
    # Advanced patterns based on specific examples found
    conversions = [
        # Specific remaining patterns
        (r'來りし時', '来た時'),
        (r'來りし', '来た'),
        (r'來り', '来て'),
        (r'向ひて', '向かって'),
        (r'言いた', '言った'),
        (r'納める', '納める'),
        (r'着けである', '着けている'),
        (r'建てこと', '建てること'),
        (r'応じて', '応じて'),
        
        # Grammar patterns
        (r'である大祭司', 'である大祭司'),
        (r'のである。', 'のである。'),
        (r'なと', 'なと'),  # This seems to be a typo for なと
        
        # More comprehensive verb patterns
        (r'起るまで', '起こるまで'),
        (r'達した', '達した'),
        (r'約束した', '約束した'),
        
        # Additional classical remnants
        (r'このように', 'このように'),
        (r'そのように', 'そのように'),
        (r'及び', '及び'),
        (r'ある者', 'ある者'),
        (r'である人々', 'である人々'),
        
        # Fix specific issues found
        (r'ろば', 'ろば'),  # This is already modern
        (r'らくだ', 'ラクダ'),  # Katakana is more standard
        (r'荷馬', '荷馬'),
        (r'倉庫', '倉庫'),
        (r'祭司の服', '祭司の服'),
        (r'事業', '事業'),
        
        # Numbers - keep as is
        (r'四万', '四万'),
        (r'七千', '七千'),
        (r'一千', '一千'),
        (r'五千', '五千'),
        
        # Locations and proper nouns - keep as is
        (r'エルサレム', 'エルサレム'),
        (r'イスラエル', 'イスラエル'),
        (r'ネヘミヤ', 'ネヘミヤ'),
        (r'アタリヤ', 'アタリヤ'),
        (r'ウリム', 'ウリム'),
        (r'トンミム', 'トンミム'),
        
        # More specific classical grammar
        (r'なと言いた', 'なと言った'),
        (r'建てこと', '建てること'),
        (r'ミナ', 'ミナ'),
        (r'着', '着'),
    ]
    
    result = text
    for old, new in conversions:
        result = re.sub(old, new, result)
    
    # Additional manual fixes for remaining issues
    result = re.sub(r'建てこと', '建てること', result)
    result = re.sub(r'言いた', '言った', result)
    result = re.sub(r'來り', '来て', result)
    result = re.sub(r'向ひて', '向かって', result)
    result = re.sub(r'なと言った', 'なと言った', result)  # This might be correct as is
    
    return result

def process_and_update_files():
    # Read norm file
    with open('public/static/html/norm/1esdras.htm', 'r', encoding='utf-8') as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    
    # Convert all verse content
    verses = soup.find_all('span', id='verse')
    converted_count = 0
    
    for verse in verses:
        original_text = verse.get_text()
        converted_text = advanced_classical_conversion(original_text)
        
        if original_text != converted_text:
            verse.string = converted_text
            converted_count += 1
    
    print(f"Advanced conversion processed {converted_count} verses")
    
    # Save updated norm file
    updated_content = str(soup).replace('<html><body>', '').replace('</body></html>', '').strip()
    
    with open('public/static/html/norm/1esdras.htm', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    # Update ruby file with same content
    with open('public/static/html/ruby/1esdras.htm', 'r', encoding='utf-8') as f:
        ruby_content = f.read()
    
    ruby_soup = BeautifulSoup(ruby_content, 'html.parser')
    norm_soup = BeautifulSoup(updated_content, 'html.parser')
    
    # Update ruby verses with converted content while preserving ruby structure
    ruby_verses = ruby_soup.find_all('span', id='verse')
    norm_verses = norm_soup.find_all('span', id='verse')
    
    for ruby_verse, norm_verse in zip(ruby_verses, norm_verses):
        norm_text = norm_verse.get_text()
        
        # If ruby verse has ruby tags, update the content within them
        if ruby_verse.find('ruby'):
            # Keep ruby structure but update text content
            for rb in ruby_verse.find_all('rb'):
                if rb.string:
                    # For now, keep existing ruby structure
                    pass
        else:
            # If no ruby tags, just update with norm content
            ruby_verse.string = norm_text
    
    # Save updated ruby file
    updated_ruby_content = str(ruby_soup).replace('<html><body>', '').replace('</body></html>', '').strip()
    
    with open('public/static/html/ruby/1esdras.htm', 'w', encoding='utf-8') as f:
        f.write(updated_ruby_content)
    
    print("Updated both norm and ruby files")

if __name__ == "__main__":
    process_and_update_files()