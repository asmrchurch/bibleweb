#!/usr/bin/env python3
"""
Generate PDF and e-book formats for 1 Esdras
"""
import os
import re
import subprocess
from pathlib import Path
import json

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

    # Extract chapters and verses
    chapters = []
    chapter_pattern = r'<h3[^>]*id="c(\d+)"[^>]*>.*?</h3>'
    verse_pattern = r'<em[^>]*id="(\d+-\d+)"[^>]*>.*?</em><span[^>]*id="verse"[^>]*>(.*?)</span>'

    for chapter_match in re.finditer(chapter_pattern, content):
        chapter_num = chapter_match.group(1)
        chapter_title = f"第{chapter_num}章"

        # Find verses for this chapter
        verses = []
        chapter_content = content[chapter_match.start():]
        next_chapter = re.search(r'<h3[^>]*id="c\d+"', chapter_content[100:])
        if next_chapter:
            chapter_content = chapter_content[:next_chapter.start() + 100]

        for verse_match in re.finditer(verse_pattern, chapter_content):
            verse_num = verse_match.group(1)
            verse_text = re.sub(r'<[^>]+>', '', verse_match.group(2))
            verses.append(f"{verse_num} {verse_text}")

        if verses:
            chapters.append({
                'num': chapter_num,
                'title': chapter_title,
                'verses': verses
            })

    return title, chapters

def create_markdown(title, chapters, output_file):
    """Create Markdown file"""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"# {title}\n\n")

        for chapter in chapters:
            f.write(f"## {chapter['title']}\n\n")
            for verse in chapter['verses']:
                f.write(f"{verse}\n\n")
            f.write("\n---\n\n")

    print(f"Created: {output_file}")

def create_plain_text(title, chapters, output_file):
    """Create plain text file"""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"{title}\n")
        f.write("=" * 50 + "\n\n")

        for chapter in chapters:
            f.write(f"\n{chapter['title']}\n")
            f.write("-" * 30 + "\n\n")
            for verse in chapter['verses']:
                f.write(f"{verse}\n\n")

    print(f"Created: {output_file}")

def create_html_ebook(title, chapters, output_file, with_ruby=True):
    """Create HTML optimized for e-book conversion"""
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
        ruby {{
            ruby-align: center;
        }}
        rt {{
            font-size: 0.5em;
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

    print(f"Created: {output_file}")

def try_command(command, description):
    """Try to run a command and report results"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✓ {description}")
            return True
        else:
            print(f"✗ {description} failed")
            if result.stderr:
                print(f"  Error: {result.stderr[:200]}")
            return False
    except Exception as e:
        print(f"✗ {description} failed: {e}")
        return False

def main():
    # Create output directory
    output_dir = Path("/Users/suganolab/web/bibleweb/output")
    output_dir.mkdir(exist_ok=True)

    print("=" * 50)
    print("Generating all formats for エズラ第一書")
    print("=" * 50)

    # Process both versions
    versions = [
        ("ruby", "/Users/suganolab/web/bibleweb/public/static/html/ruby/1esdras.htm", "ルビ付き"),
        ("norm", "/Users/suganolab/web/bibleweb/public/static/html/norm/1esdras.htm", "ルビなし")
    ]

    for version_id, html_file, version_name in versions:
        print(f"\nProcessing {version_name} version...")

        # Extract content
        title, chapters = extract_text_from_html(html_file)
        full_title = f"{title}（{version_name}）"

        # Create various formats
        create_plain_text(full_title, chapters, output_dir / f"1esdras_{version_id}.txt")
        create_markdown(full_title, chapters, output_dir / f"1esdras_{version_id}.md")
        create_html_ebook(full_title, chapters, output_dir / f"1esdras_{version_id}_ebook.html",
                         with_ruby=(version_id == "ruby"))

    print("\n" + "=" * 50)
    print("Attempting conversions with external tools...")
    print("=" * 50)

    # Try to convert with available tools
    for version_id, _, version_name in versions:
        base_file = output_dir / f"1esdras_{version_id}"

        # Try wkhtmltopdf
        if try_command(f"which wkhtmltopdf", "Checking for wkhtmltopdf"):
            try_command(
                f"wkhtmltopdf '{base_file}_ebook.html' '{base_file}.pdf'",
                f"Creating PDF for {version_name}"
            )

        # Try pandoc
        if try_command(f"which pandoc", "Checking for pandoc"):
            try_command(
                f"pandoc '{base_file}.md' -o '{base_file}_pandoc.pdf' --pdf-engine=xelatex -V mainfont='Hiragino Mincho ProN'",
                f"Creating PDF with pandoc for {version_name}"
            )

        # Try ebook-convert (calibre)
        if try_command(f"which ebook-convert", "Checking for ebook-convert"):
            # EPUB
            try_command(
                f"ebook-convert '{base_file}_ebook.html' '{base_file}.epub' --title '{title}（{version_name}）' --language ja",
                f"Creating EPUB for {version_name}"
            )
            # MOBI
            try_command(
                f"ebook-convert '{base_file}_ebook.html' '{base_file}.mobi' --title '{title}（{version_name}）' --language ja",
                f"Creating MOBI for {version_name}"
            )

    # List all created files
    print("\n" + "=" * 50)
    print("Files created in output directory:")
    print("=" * 50)

    for file in sorted(output_dir.iterdir()):
        if file.is_file():
            size = file.stat().st_size
            size_kb = size / 1024
            print(f"  {file.name:40} ({size_kb:8.1f} KB)")

    print("\n" + "=" * 50)
    print("Conversion complete!")
    print("=" * 50)
    print("\nNext steps:")
    print("1. For PDF: Open the *_ebook.html files in Safari/Chrome and print to PDF")
    print("2. For Kindle: Use the .txt or .html files and email to your Kindle address")
    print("3. Or install tools:")
    print("   brew install --cask wkhtmltopdf  # For PDF")
    print("   brew install --cask calibre      # For EPUB/MOBI")

if __name__ == "__main__":
    main()