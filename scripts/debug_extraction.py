#!/usr/bin/env python3
"""
Debug script to check what chapters are being extracted
"""
import re

def debug_extract_text_from_html(html_file):
    """Debug version of extract_text_from_html"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    print(f"File size: {len(content)} characters")

    # Extract title
    title_match = re.search(r'<h2[^>]*>(.*?)</h2>', content)
    title = title_match.group(1) if title_match else "エズラ第一書"
    print(f"Title: {title}")

    # Extract chapters and verses
    chapters = []
    chapter_pattern = r'<h3[^>]*id="c(\d+)"[^>]*>(.*?)</h3>'
    verse_pattern = r'<em[^>]*id="(\d+-\d+)"[^>]*>.*?</em><span[^>]*id="verse"[^>]*>(.*?)</span>'

    print("\nFinding chapters...")
    chapter_matches = list(re.finditer(chapter_pattern, content))
    print(f"Found {len(chapter_matches)} chapters")

    for i, chapter_match in enumerate(chapter_matches):
        chapter_num = chapter_match.group(1)
        chapter_title = re.sub(r'<[^>]+>', '', chapter_match.group(2))
        print(f"\nChapter {chapter_num}: {chapter_title}")
        print(f"  Chapter starts at position: {chapter_match.start()}")

        # Find verses for this chapter
        verses = []
        chapter_content = content[chapter_match.start():]

        # Find next chapter boundary
        next_chapter = re.search(r'<h3[^>]*id="c\d+"', chapter_content[100:])
        if next_chapter:
            chapter_content = chapter_content[:next_chapter.start() + 100]
            print(f"  Chapter ends at relative position: {next_chapter.start() + 100}")
        else:
            print(f"  Chapter extends to end of document")

        print(f"  Chapter content length: {len(chapter_content)}")

        verse_matches = list(re.finditer(verse_pattern, chapter_content))
        print(f"  Found {len(verse_matches)} verses")

        for verse_match in verse_matches[:3]:  # Show first 3 verses
            verse_num = verse_match.group(1)
            verse_text = re.sub(r'<[^>]+>', '', verse_match.group(2))
            verses.append(f"{verse_num} {verse_text}")
            print(f"    {verse_num}: {verse_text[:50]}...")

        if verses:
            chapters.append({
                'num': chapter_num,
                'title': chapter_title,
                'verses': verses
            })

    print(f"\nTotal chapters extracted: {len(chapters)}")
    for ch in chapters:
        print(f"  Chapter {ch['num']}: {len(ch['verses'])} verses")

    return title, chapters

if __name__ == "__main__":
    html_file = "/Users/suganolab/web/bibleweb/public/static/html/ruby/1esdras.htm"
    title, chapters = debug_extract_text_from_html(html_file)