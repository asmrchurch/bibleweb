#!/usr/bin/env python3
"""
Script to extract and process the English Tobit text from HTML table format
and create a comprehensive Japanese translation.
"""
import re
import html

def read_tobit_html(file_path):
    """Read and parse the Tobit HTML file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract all table rows with verse content
    verse_pattern = r'<tr><td class="vn">([^<]+)</td><td class="vn">&nbsp;&nbsp;</td><td class="v en">([^<]+)</td></tr>'
    verses = re.findall(verse_pattern, content)
    
    # Group verses by chapter:verse and combine text fragments
    verse_dict = {}
    for verse_num, text in verses:
        # Clean up the text
        text = html.unescape(text)
        text = re.sub(r'\s+', ' ', text)  # Normalize whitespace
        text = text.strip()
        
        # Skip empty, very short verses, or metadata lines
        if (len(text) <= 3 or text.isdigit() or 
            'Tobit' in text and ('511' in text or '512' in text or '513' in text) or
            text.startswith('†') or text.startswith('‡') or text.startswith('§')):
            continue
            
        # Parse verse number
        verse_key = verse_num.strip()
        
        # Combine text fragments for same verse
        if verse_key in verse_dict:
            verse_dict[verse_key] += ' ' + text
        else:
            verse_dict[verse_key] = text
    
    # Convert back to list and sort by verse number
    cleaned_verses = []
    for verse_key in sorted(verse_dict.keys(), key=lambda x: parse_verse_key(x)):
        cleaned_verses.append((verse_key, verse_dict[verse_key]))
    
    return cleaned_verses

def parse_verse_key(verse_key):
    """Parse verse key for sorting (e.g., '1:5' -> (1, 5))"""
    try:
        if ':' in verse_key:
            chapter, verse = verse_key.split(':', 1)
            return (int(chapter), int(verse))
        else:
            return (int(verse_key), 0)
    except:
        return (999, 999)  # Put unparseable keys at end

def print_verses(verses, limit=50):
    """Print verses for inspection"""
    for i, (verse_num, text) in enumerate(verses[:limit]):
        print(f"{verse_num}: {text}")

if __name__ == "__main__":
    tobit_path = "/Users/suganolab/web/bibleweb/etc/html/en/tobit.htm"
    verses = read_tobit_html(tobit_path)
    print(f"Found {len(verses)} verses")
    print("\nFirst 50 verses:")
    print_verses(verses, 50)