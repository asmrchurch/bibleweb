#!/usr/bin/env python3
"""
Complete Sirach from 2:1 onwards
"""

import sys
import os
import re

# Add the ruby converter to path
sys.path.append('/Users/suganolab/web/bibleweb')
from ruby_converter import add_ruby_markup

def extract_verse_content(line):
    """Extract the verse number and content from a line."""
    # Pattern to match verse lines: <em style="...">X:Y</em>content
    pattern = r'<em style="color:rgb\(255, 51, 0\);[^"]*">(\d+:\d+)</em>(.+)$'
    match = re.match(pattern, line.strip())
    if match:
        verse_num = match.group(1)
        content = match.group(2)
        return verse_num, content
    return None, None

def get_verses_from_source(source_file, start_chapter, start_verse):
    """Get verses from source file starting from specific chapter:verse."""
    verses = []
    
    with open(source_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for line in lines:
        verse_num, content = extract_verse_content(line)
        if verse_num and content:
            chapter, verse = map(int, verse_num.split(':'))
            
            # Check if this verse should be included
            if chapter > start_chapter or (chapter == start_chapter and verse >= start_verse):
                # Apply ruby conversion
                ruby_content = add_ruby_markup(content)
                verses.append((verse_num, ruby_content))
    
    return verses

def append_to_ruby_file(ruby_file, verses):
    """Append verses to ruby file before closing tags."""
    # Read the current ruby file
    with open(ruby_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the position to insert new verses (before final closing divs)
    # Look for the last </div></div> sequence
    insert_pos = content.rfind('</div>\n</div>')
    if insert_pos == -1:
        print("Warning: Could not find insertion point")
        return
    
    # Prepare new verses with proper HTML structure
    new_verses = []
    current_chapter = None
    in_chapter = False
    
    for verse_num, ruby_content in verses:
        chapter, verse = map(int, verse_num.split(':'))
        
        # Check if we're continuing an existing chapter or starting a new one
        if current_chapter != chapter:
            # Close previous chapter if we were in one
            if in_chapter:
                new_verses.append('</div>')
                new_verses.append('</div>')
            
            # Start new chapter
            new_verses.append(f'<div id="{chapter}" style="display:block;margin-left:0px;margin-top:16px;">')
            new_verses.append(f'<h3 style="font-size:18.72px;font-weight:700;display:inline;margin-block-end:18.72px;margin-block-start:18.72px;margin-inline-end:9.36px;margin-inline-start:0px;margin-right:9.36px;"><ruby><rb>第</rb><rp>(</rp><rt>だい</rt><rp>)</rp></ruby>{chapter}<ruby><rb>章</rb><rp>(</rp><rt>しょう</rt><rp>)</rp></ruby></h3>')
            new_verses.append('<div style="display:block;margin-left:0px;text-indent:16px;">')
            
            current_chapter = chapter
            in_chapter = True
        
        # Add the verse
        verse_line = f'<em style="color:rgb(255, 51, 0);font-style:normal;margin-right:1.6px;padding-right:3.2px;">{verse_num}</em>{ruby_content}'
        new_verses.append(verse_line)
    
    # Close the last chapter if we added any verses
    if in_chapter:
        new_verses.append('</div>')
        new_verses.append('</div>')
    
    # Insert the new verses
    new_content = (
        content[:insert_pos] + 
        '\n'.join(new_verses) + '\n' +
        content[insert_pos:]
    )
    
    # Write back to file
    with open(ruby_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Added {len(verses)} verses to {ruby_file}")

if __name__ == "__main__":
    # Process Sirach from 2:1 onwards
    source_file = '/Users/suganolab/web/bibleweb/public/static/html/norm/sirach.htm'
    ruby_file = '/Users/suganolab/web/bibleweb/public/static/html/ruby/sirach.htm'
    
    print("Getting verses from 2:1 onwards...")
    verses = get_verses_from_source(source_file, 2, 1)
    
    print(f"Found {len(verses)} verses to add")
    
    if verses:
        print("Appending to ruby file...")
        append_to_ruby_file(ruby_file, verses)
        
        # Verify final count
        print("Final verse count:")
        os.system(f'grep -c \'style="color:rgb(255, 51, 0)\' {ruby_file}')
        
        print("Sirach conversion completed!")