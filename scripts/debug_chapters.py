#!/usr/bin/env python3
import re

def test_chapter_extraction():
    """Test the fixed chapter extraction"""

    # Read the HTML file
    html_file = "/Users/suganolab/web/bibleweb/public/static/html/ruby/1esdras.htm"
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Test the fixed pattern
    chapter_pattern = r'<h3[^>]*id="c(\d+)"[^>]*>.*?</h3>'

    chapters = []
    for chapter_match in re.finditer(chapter_pattern, content):
        chapter_num = chapter_match.group(1)
        chapters.append(chapter_num)
        print(f"Found chapter {chapter_num}")

    print(f"\nTotal chapters found: {len(chapters)}")
    print(f"Chapters: {', '.join(chapters)}")

    if len(chapters) == 9:
        print("✓ SUCCESS: All 9 chapters detected!")
        return True
    else:
        print(f"✗ ERROR: Expected 9 chapters, found {len(chapters)}")
        return False

if __name__ == "__main__":
    test_chapter_extraction()