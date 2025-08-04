#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import re
import time

def scrape_tobit_chapter(chapter_num):
    """Scrape a specific chapter of Tobit from USCCB"""
    url = f"https://bible.usccb.org/bible/tobit/{chapter_num}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the content area with verses
        verses = []
        
        # Look for verse containers (may vary by site structure)
        verse_elements = soup.find_all('span', class_='verse-num') or soup.find_all('sup', class_='verse-num')
        
        if not verse_elements:
            # Try different approach - look for numbered verses
            content_area = soup.find('div', class_='bible-text') or soup.find('div', class_='content')
            if content_area:
                text = content_area.get_text()
                lines = text.split('\n')
                
                for line in lines:
                    line = line.strip()
                    if not line:
                        continue
                    
                    # Look for verse pattern like "1 Text here" or "1:1 Text here"
                    verse_match = re.match(r'^(\d+)\s+(.+)', line)
                    if verse_match:
                        verse_num = verse_match.group(1)
                        verse_text = verse_match.group(2).strip()
                        verses.append({
                            'chapter': chapter_num,
                            'verse': int(verse_num),
                            'text': verse_text
                        })
        
        return verses
        
    except Exception as e:
        print(f"Error scraping chapter {chapter_num}: {e}")
        return []

def scrape_all_tobit():
    """Scrape all chapters of Tobit"""
    all_verses = []
    
    # Tobit has 14 chapters
    for chapter in range(1, 15):
        print(f"Scraping Tobit chapter {chapter}...")
        verses = scrape_tobit_chapter(chapter)
        all_verses.extend(verses)
        
        # Be respectful to the server
        time.sleep(1)
    
    return all_verses

def create_html_from_verses(verses, output_file):
    """Create HTML file from verses"""
    html_content = "<h1 class='et'>Tobit</h1>\n<BR>\n"
    html_content += "<div id=\"contenten\" style=\"position:relative; top:0px; left:0px; overflow:auto\"><table cellpadding=0 cellspacing=0 border=0>\n"
    
    for verse in verses:
        html_content += f"<tr><td class=\"vn\">{verse['chapter']}:{verse['verse']}</td><td class=\"vn\">&nbsp;&nbsp;</td><td class=\"v en\">{verse['text']}</td></tr>\n"
    
    html_content += "</table></div>"
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Created {output_file} with {len(verses)} verses")

if __name__ == "__main__":
    print("Scraping Book of Tobit from USCCB...")
    verses = scrape_all_tobit()
    
    if verses:
        output_file = "/Users/suganolab/web/bibleweb/public/static/html/en/tobit.htm"
        create_html_from_verses(verses, output_file)
        
        # Also copy to server directory if it exists
        server_file = "/Users/suganolab/web/bible/public/static/html/en/tobit.htm"
        try:
            create_html_from_verses(verses, server_file)
            print(f"Also copied to {server_file}")
        except:
            print("Server directory not found, skipping copy")
    else:
        print("No verses found!")