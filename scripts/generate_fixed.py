#!/usr/bin/env python3
"""
Fixed version of generate_all_formats.py that correctly extracts all 9 chapters
"""
import re
from pathlib import Path

def extract_all_chapters(html_file):
    """Extract all chapters from the HTML file"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Clean up ruby tags first
    content = re.sub(r'<ruby><rb>(.*?)</rb><rp>\(</rp><rt>(.*?)</rt><rp>\)</rp></ruby>', r'\1(\2)', content)

    # Find all chapters
    chapters = []
    chapter_pattern = r'<h3[^>]*id="c(\d+)"[^>]*>.*?</h3>'

    # Get all chapter matches first
    chapter_matches = list(re.finditer(chapter_pattern, content))
    print(f"Found {len(chapter_matches)} chapters")

    for i, chapter_match in enumerate(chapter_matches):
        chapter_num = chapter_match.group(1)
        chapter_title = f"第{chapter_num}章"

        # Determine chapter content boundaries
        start_pos = chapter_match.end()
        if i + 1 < len(chapter_matches):
            end_pos = chapter_matches[i + 1].start()
        else:
            end_pos = len(content)

        chapter_content = content[start_pos:end_pos]

        # Extract verses from this chapter
        verse_pattern = r'<em[^>]*id="(\d+-\d+)"[^>]*>.*?</em><span[^>]*id="verse"[^>]*>(.*?)</span>'
        verses = []

        for verse_match in re.finditer(verse_pattern, chapter_content):
            verse_num = verse_match.group(1)
            verse_text = re.sub(r'<[^>]+>', '', verse_match.group(2))
            verses.append(f"{verse_num} {verse_text}")

        print(f"Chapter {chapter_num}: {len(verses)} verses")

        chapters.append({
            'num': chapter_num,
            'title': chapter_title,
            'verses': verses
        })

    return chapters

def create_complete_markdown(title, chapters, output_file):
    """Create complete markdown with all chapters"""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"# {title}\n\n")

        for chapter in chapters:
            f.write(f"## {chapter['title']}\n\n")
            for verse in chapter['verses']:
                f.write(f"{verse}\n\n")
            f.write("\n---\n\n")

    print(f"Created complete markdown: {output_file} ({len(chapters)} chapters)")

def create_complete_text(title, chapters, output_file):
    """Create complete plain text with all chapters"""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"{title}\n")
        f.write("=" * 50 + "\n\n")

        for chapter in chapters:
            f.write(f"\n{chapter['title']}\n")
            f.write("-" * 30 + "\n\n")
            for verse in chapter['verses']:
                f.write(f"{verse}\n\n")

    print(f"Created complete text: {output_file} ({len(chapters)} chapters)")

def create_complete_html(title, chapters, output_file):
    """Create complete HTML with all chapters"""
    html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <style>
        body {{
            font-family: "Hiragino Mincho ProN", "Yu Mincho", "Noto Serif JP", serif;
            line-height: 1.8;
            margin: 20px;
        }}
        h1 {{
            text-align: center;
            margin-bottom: 2em;
        }}
        h2 {{
            margin-top: 2em;
            margin-bottom: 1em;
            border-bottom: 1px solid #ccc;
            padding-bottom: 0.5em;
        }}
        .verse-num {{
            color: #cc0000;
            font-weight: bold;
            margin-right: 0.5em;
        }}
        .verse {{
            margin-bottom: 0.5em;
            text-indent: 1em;
        }}
    </style>
</head>
<body>
    <h1>{title}</h1>
"""

    for chapter in chapters:
        html_content += f"    <h2>{chapter['title']}</h2>\n"
        for verse in chapter['verses']:
            # Split verse number and text
            parts = verse.split(' ', 1)
            if len(parts) == 2:
                verse_num, verse_text = parts
                html_content += f'    <div class="verse"><span class="verse-num">{verse_num}</span>{verse_text}</div>\n'
            else:
                html_content += f'    <div class="verse">{verse}</div>\n'

    html_content += """</body>
</html>"""

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"Created complete HTML: {output_file} ({len(chapters)} chapters)")

def main():
    """Generate corrected files with all 9 chapters"""
    print("=" * 50)
    print("Regenerating 1 Esdras with ALL chapters")
    print("=" * 50)

    output_dir = Path("/Users/suganolab/web/bibleweb/output")

    # Process both versions
    versions = [
        ("ruby", "/Users/suganolab/web/bibleweb/public/static/html/ruby/1esdras.htm", "ルビ付き"),
        ("norm", "/Users/suganolab/web/bibleweb/public/static/html/norm/1esdras.htm", "ルビなし")
    ]

    for version_id, html_file, version_name in versions:
        print(f"\nProcessing {version_name} version from {html_file}...")

        # Extract all chapters
        chapters = extract_all_chapters(html_file)
        title = f"エズラ第一書（{version_name}）"

        if len(chapters) == 9:
            print(f"✓ Successfully extracted all {len(chapters)} chapters")

            # Generate all formats
            create_complete_text(title, chapters, output_dir / f"1esdras_{version_id}.txt")
            create_complete_markdown(title, chapters, output_dir / f"1esdras_{version_id}.md")
            create_complete_html(title, chapters, output_dir / f"1esdras_{version_id}_ebook.html")

            # Verify by showing chapter summary
            print(f"Chapter summary for {version_name}:")
            total_verses = 0
            for chapter in chapters:
                verse_count = len(chapter['verses'])
                total_verses += verse_count
                print(f"  {chapter['title']}: {verse_count} verses")
            print(f"  Total: {total_verses} verses across {len(chapters)} chapters")

        else:
            print(f"✗ ERROR: Expected 9 chapters, found {len(chapters)}")

    print("\n" + "=" * 50)
    print("Fixed generation complete!")
    print("=" * 50)

if __name__ == "__main__":
    main()