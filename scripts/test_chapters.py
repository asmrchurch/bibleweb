#!/usr/bin/env python3
import re

def extract_chapters_from_html(html_file):
    """Test function to extract chapters"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Updated chapter pattern
    chapter_pattern = r'<h3[^>]*id="c(\d+)"[^>]*>.*?</h3>'

    chapters_found = []
    for chapter_match in re.finditer(chapter_pattern, content):
        chapter_num = chapter_match.group(1)
        chapters_found.append(chapter_num)

    return chapters_found

# Test the extraction
html_file = "/Users/suganolab/web/bibleweb/public/static/html/ruby/1esdras.htm"
chapters = extract_chapters_from_html(html_file)
print(f"Found chapters: {chapters}")
print(f"Total chapters found: {len(chapters)}")

if len(chapters) == 9:
    print("✓ All 9 chapters detected correctly!")
else:
    print(f"✗ Expected 9 chapters, found {len(chapters)}")