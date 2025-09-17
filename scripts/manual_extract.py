#!/usr/bin/env python3
"""
Manual extraction to verify the fix works
"""
import re
import os
from pathlib import Path

def extract_text_from_html(html_file):
    """Extract plain text from HTML file"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract title
    title_match = re.search(r'<h2[^>]*>(.*?)</h2>', content)
    title = title_match.group(1) if title_match else "エズラ第一書"

    # Clean up ruby tags - keep both base and reading
    content = re.sub(r'<ruby><rb>(.*?)</rb><rp>\(</rp><rt>(.*?)</rt><rp>\)</rp></ruby>',
                     r'\1(\2)', content)

    # Extract chapters and verses - FIXED pattern
    chapters = []
    chapter_pattern = r'<h3[^>]*id="c(\d+)"[^>]*>.*?</h3>'
    verse_pattern = r'<em[^>]*id="(\d+-\d+)"[^>]*>.*?</em><span[^>]*id="verse"[^>]*>(.*?)</span>'

    print(f"Searching for chapters in {html_file}...")

    for chapter_match in re.finditer(chapter_pattern, content):
        chapter_num = chapter_match.group(1)
        chapter_title = f"第{chapter_num}章"  # FIXED: Use simple title format

        print(f"Found chapter {chapter_num}")

        # Find verses for this chapter
        verses = []
        chapter_content = content[chapter_match.start():]
        next_chapter = re.search(r'<h3[^>]*id="c\d+"', chapter_content[100:])
        if next_chapter:
            chapter_content = chapter_content[:next_chapter.start() + 100]

        verse_count = 0
        for verse_match in re.finditer(verse_pattern, chapter_content):
            verse_num = verse_match.group(1)
            verse_text = re.sub(r'<[^>]+>', '', verse_match.group(2))
            verses.append(f"{verse_num} {verse_text}")
            verse_count += 1

        print(f"  Chapter {chapter_num} has {verse_count} verses")

        if verses:
            chapters.append({
                'num': chapter_num,
                'title': chapter_title,
                'verses': verses
            })

    print(f"\nTotal chapters extracted: {len(chapters)}")
    return title, chapters

def create_markdown_sample(title, chapters, output_file):
    """Create a sample Markdown file to verify structure"""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"# {title}\n\n")

        for chapter in chapters:
            f.write(f"## {chapter['title']}\n\n")

            # Show first 3 verses and last verse of each chapter for verification
            verse_count = len(chapter['verses'])
            sample_verses = chapter['verses'][:3]
            if verse_count > 3:
                sample_verses.append(f"... ({verse_count - 4} more verses) ...")
                sample_verses.append(chapter['verses'][-1])

            for verse in sample_verses:
                f.write(f"{verse}\n\n")

            f.write(f"*Total verses in chapter: {verse_count}*\n\n")
            f.write("---\n\n")

    print(f"Sample created: {output_file}")

# Test the extraction
html_file = "/Users/suganolab/web/bibleweb/public/static/html/ruby/1esdras.htm"
title, chapters = extract_text_from_html(html_file)

print(f"\nExtraction Results:")
print(f"Title: {title}")
print(f"Number of chapters: {len(chapters)}")

if len(chapters) == 9:
    print("✓ SUCCESS: All 9 chapters extracted correctly!")

    # Create a sample file to verify content
    output_dir = Path("/Users/suganolab/web/bibleweb/output")
    create_markdown_sample(f"{title}（ルビ付き）", chapters, output_dir / "1esdras_verification_sample.md")

    print(f"\nChapter summary:")
    for chapter in chapters:
        print(f"  Chapter {chapter['num']}: {len(chapter['verses'])} verses")

else:
    print(f"✗ ERROR: Expected 9 chapters, found {len(chapters)}")
    if chapters:
        print("Chapters found:", [ch['num'] for ch in chapters])