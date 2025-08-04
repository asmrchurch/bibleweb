#!/usr/bin/env python3
import time

# I'll use this script to generate fetch commands for all 14 chapters
# Since I can't make web requests directly from Python, I'll prepare the structure

def generate_chapter_structure():
    """Generate the structure for fetching all 14 chapters of Tobit"""
    
    print("# Commands to fetch all 14 chapters of Tobit")
    print("# Each chapter needs to be fetched using WebFetch")
    
    for chapter in range(1, 15):
        print(f"\n# Chapter {chapter}")
        print(f"URL: https://bible.usccb.org/bible/tobit/{chapter}")
        print(f"Prompt: Extract ONLY the biblical verse text from Tobit Chapter {chapter}. For each verse, provide just the verse number and the text content, formatted as 'Verse X: [text]'. Ignore all navigation, headers, footnotes, and commentary.")
        
    print("\n\n# Template for creating the complete HTML file:")
    print("""
html_content = '<h1 class="et">Tobit</h1>\\n<BR>\\n'
html_content += '<div id="contenten" style="position:relative; top:0px; left:0px; overflow:auto"><table cellpadding=0 cellspacing=0 border=0>\\n'

# Add all verses here
for chapter, verse, text in all_verses:
    clean_text = text.replace('"', '&quot;').replace('<', '&lt;').replace('>', '&gt;')
    html_content += f'<tr><td class="vn">{chapter}:{verse}</td><td class="vn">&nbsp;&nbsp;</td><td class="v en">{clean_text}</td></tr>\\n'

html_content += '</table></div>'
""")

if __name__ == "__main__":
    generate_chapter_structure()