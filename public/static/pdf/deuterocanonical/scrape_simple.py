#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import re

def scrape_tobit_usccb():
    """Try to scrape Tobit from USCCB using direct text extraction"""
    
    all_verses = []
    
    for chapter in range(1, 15):  # Tobit has 14 chapters
        url = f"https://bible.usccb.org/bible/tobit/{chapter}"
        
        try:
            print(f"Fetching chapter {chapter}...")
            response = requests.get(url)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Try to find the main content area
            content_div = soup.find('div', {'class': 'bible-text'})
            if not content_div:
                content_div = soup.find('div', {'class': 'content'})
            if not content_div:
                content_div = soup.find('main')
            if not content_div:
                content_div = soup
            
            # Get all text and look for verse patterns
            text_content = content_div.get_text()
            
            # Split by lines and look for verse patterns
            lines = text_content.split('\n')
            
            verse_num = 1
            current_verse_text = ""
            
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                
                # Skip navigation and header elements
                if any(skip in line.lower() for skip in ['chapter', 'navigation', 'previous', 'next', 'home', 'book of tobit', 'usccb']):
                    continue
                
                # Look for verse number patterns
                # Pattern 1: Line starts with just a number
                if re.match(r'^\d+$', line):
                    if current_verse_text:
                        all_verses.append({
                            'chapter': chapter,
                            'verse': verse_num,
                            'text': current_verse_text.strip()
                        })
                        current_verse_text = ""
                    verse_num = int(line)
                    continue
                
                # Pattern 2: Line starts with number followed by text
                verse_match = re.match(r'^(\d+)\s+(.+)', line)
                if verse_match:
                    if current_verse_text:
                        all_verses.append({
                            'chapter': chapter,
                            'verse': verse_num,
                            'text': current_verse_text.strip()
                        })
                    verse_num = int(verse_match.group(1))
                    current_verse_text = verse_match.group(2)
                    continue
                
                # Otherwise, add to current verse text
                if line and len(line) > 5:  # Only substantial text
                    if current_verse_text:
                        current_verse_text += " " + line
                    else:
                        current_verse_text = line
            
            # Don't forget the last verse
            if current_verse_text:
                all_verses.append({
                    'chapter': chapter,
                    'verse': verse_num,
                    'text': current_verse_text.strip()
                })
            
            print(f"Found {len([v for v in all_verses if v['chapter'] == chapter])} verses in chapter {chapter}")
            
        except Exception as e:
            print(f"Error scraping chapter {chapter}: {e}")
            continue
    
    return all_verses

def create_html_file(verses, filename):
    """Create HTML file from verses"""
    html_content = "<h1 class='et'>Tobit</h1>\n<BR>\n"
    html_content += "<div id=\"contenten\" style=\"position:relative; top:0px; left:0px; overflow:auto\"><table cellpadding=0 cellspacing=0 border=0>\n"
    
    for verse in verses:
        clean_text = verse['text'].replace('"', '&quot;').replace('<', '&lt;').replace('>', '&gt;')
        html_content += f"<tr><td class=\"vn\">{verse['chapter']}:{verse['verse']}</td><td class=\"vn\">&nbsp;&nbsp;</td><td class=\"v en\">{clean_text}</td></tr>\n"
    
    html_content += "</table></div>"
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Created {filename} with {len(verses)} verses")

if __name__ == "__main__":
    verses = scrape_tobit_usccb()
    
    if verses:
        output_file = "/Users/suganolab/web/bibleweb/public/static/html/en/tobit.htm"
        create_html_file(verses, output_file)
        
        # Show first few verses for verification
        print("\nFirst 5 verses:")
        for i, verse in enumerate(verses[:5]):
            print(f"{verse['chapter']}:{verse['verse']} - {verse['text'][:100]}...")
    else:
        print("No verses extracted!")