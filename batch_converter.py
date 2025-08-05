#!/usr/bin/env python3
"""
Batch Ruby Converter for Bible Verses

This script processes large batches of Japanese Bible text and applies ruby annotations
using the ruby_converter utility.
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

def process_verses_from_file(source_file, start_verse=None):
    """Extract and convert verses from source file."""
    converted_verses = []
    
    with open(source_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for line in lines:
        verse_num, content = extract_verse_content(line)
        if verse_num and content:
            # Apply ruby conversion
            ruby_content = add_ruby_markup(content)
            
            # Reconstruct the line with ruby markup
            converted_line = f'<em style="color:rgb(255, 51, 0);font-style:normal;margin-right:1.6px;padding-right:3.2px;">{verse_num}</em>{ruby_content}'
            
            converted_verses.append((verse_num, converted_line))
    
    return converted_verses

def process_2maccabees():
    """Process 2 Maccabees starting from verse 1:29."""
    source_file = '/Users/suganolab/web/bibleweb/public/static/html/norm/2maccabees.htm'
    converted_verses = process_verses_from_file(source_file)
    
    # Filter verses starting from 1:29
    target_verses = []
    for verse_num, converted_line in converted_verses:
        chapter, verse = map(int, verse_num.split(':'))
        if chapter > 1 or (chapter == 1 and verse >= 29):
            target_verses.append((verse_num, converted_line))
    
    return target_verses

if __name__ == "__main__":
    print("Starting batch conversion for 2 Maccabees...")
    
    # Process 2 Maccabees verses 1:29 onwards
    verses = process_2maccabees()
    
    print(f"Converted {len(verses)} verses")
    
    # Show first few converted verses
    for i, (verse_num, converted_line) in enumerate(verses[:5]):
        print(f"\n{verse_num}: {converted_line[:100]}...")
    
    # Save converted verses to temporary file
    with open('/Users/suganolab/web/bibleweb/converted_2maccabees.txt', 'w', encoding='utf-8') as f:
        for verse_num, converted_line in verses:
            f.write(f"{converted_line}\n")
    
    print(f"\nConverted verses saved to converted_2maccabees.txt")