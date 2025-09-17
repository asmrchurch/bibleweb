#!/usr/bin/env python3
import os
import re
from pathlib import Path

def clean_html(html_content):
    """Clean HTML and extract text"""
    # Handle ruby tags
    html_content = re.sub(r'<ruby><rb>(.*?)</rb><rp>\(</rp><rt>(.*?)</rt><rp>\)</rp></ruby>',
                          r'\1(\2)', html_content)

    # Remove HTML tags
    html_content = re.sub(r'<[^>]+>', '\n', html_content)

    # Clean up extra whitespace
    lines = [line.strip() for line in html_content.split('\n') if line.strip()]
    return '\n'.join(lines)

def extract_structured_content(html_file):
    """Extract structured content from HTML"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract title
    title_match = re.search(r'<h2[^>]*>(.*?)</h2>', content, re.DOTALL)
    if title_match:
        title = re.sub(r'<[^>]+>', '', title_match.group(1))
        title = re.sub(r'\s+', ' ', title).strip()
    else:
        title = "エズラ第一書"

    # Extract chapters
    chapters = []
    chapter_pattern = r'<h3[^>]*id="c(\d+)"[^>]*>(.*?)</h3>'

    for match in re.finditer(chapter_pattern, content):
        chapter_num = match.group(1)
        chapter_title = re.sub(r'<[^>]+>', '', match.group(2))
        chapter_title = re.sub(r'\s+', ' ', chapter_title).strip()
        chapters.append({
            'num': chapter_num,
            'title': chapter_title,
            'start': match.end()
        })

    # Extract verses for each chapter
    for i, chapter in enumerate(chapters):
        end_pos = chapters[i+1]['start'] if i+1 < len(chapters) else len(content)
        chapter_content = content[chapter['start']:end_pos]

        verses = []
        verse_pattern = r'<em[^>]*id="(\d+-\d+)"[^>]*>.*?</em>\s*<span[^>]*id="verse"[^>]*>(.*?)</span>'

        for verse_match in re.finditer(verse_pattern, chapter_content, re.DOTALL):
            verse_id = verse_match.group(1)
            verse_text = verse_match.group(2)

            # Clean verse text
            verse_text = re.sub(r'<ruby><rb>(.*?)</rb><rp>\(</rp><rt>(.*?)</rt><rp>\)</rp></ruby>',
                               r'\1(\2)', verse_text)
            verse_text = re.sub(r'<[^>]+>', '', verse_text)
            verse_text = re.sub(r'\s+', ' ', verse_text).strip()

            verses.append(f"{verse_id} {verse_text}")

        chapter['verses'] = verses

    return title, chapters

def create_text_file(title, chapters, output_file):
    """Create plain text file"""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"{title}\n")
        f.write("=" * 60 + "\n\n")

        for chapter in chapters:
            if 'verses' in chapter and chapter['verses']:
                f.write(f"\n{chapter['title']}\n")
                f.write("-" * 40 + "\n\n")

                for verse in chapter['verses']:
                    f.write(f"{verse}\n\n")

    return output_file

def create_markdown_file(title, chapters, output_file):
    """Create Markdown file"""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"# {title}\n\n")

        for chapter in chapters:
            if 'verses' in chapter and chapter['verses']:
                f.write(f"## {chapter['title']}\n\n")

                for verse in chapter['verses']:
                    f.write(f"{verse}\n\n")

                f.write("---\n\n")

    return output_file

def create_ebook_html(title, chapters, output_file):
    """Create HTML optimized for e-book readers"""
    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            font-family: "Hiragino Mincho ProN", "Yu Mincho", serif;
            line-height: 1.8;
            margin: 20px;
            max-width: 800px;
        }}
        h1 {{
            text-align: center;
            border-bottom: 3px solid #333;
            padding-bottom: 10px;
        }}
        h2 {{
            margin-top: 2em;
            color: #444;
            border-bottom: 1px solid #ccc;
            padding-bottom: 5px;
        }}
        .verse {{
            margin: 0.8em 0;
            text-indent: 1em;
        }}
        .verse-num {{
            color: #cc0000;
            font-weight: bold;
            margin-right: 0.5em;
        }}
    </style>
</head>
<body>
    <h1>{title}</h1>
"""

    for chapter in chapters:
        if 'verses' in chapter and chapter['verses']:
            html += f"    <h2>{chapter['title']}</h2>\n"

            for verse in chapter['verses']:
                parts = verse.split(' ', 1)
                if len(parts) == 2:
                    num, text = parts
                    html += f'    <div class="verse"><span class="verse-num">{num}</span>{text}</div>\n'
                else:
                    html += f'    <div class="verse">{verse}</div>\n'

    html += """</body>
</html>"""

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)

    return output_file

def main():
    # Create output directory
    output_dir = Path("/Users/suganolab/web/bibleweb/output")
    output_dir.mkdir(exist_ok=True)

    print("=" * 60)
    print("1 Esdras Conversion - Direct Python Method")
    print("=" * 60)

    # Process both versions
    versions = [
        ("ruby", "/Users/suganolab/web/bibleweb/public/static/html/ruby/1esdras.htm", "ルビ付き"),
        ("norm", "/Users/suganolab/web/bibleweb/public/static/html/norm/1esdras.htm", "ルビなし")
    ]

    created_files = []

    for version_id, html_file, version_name in versions:
        print(f"\nProcessing {version_name} version...")

        try:
            # Extract content
            title, chapters = extract_structured_content(html_file)
            full_title = f"{title}（{version_name}）"

            # Create text file
            txt_file = output_dir / f"1esdras_{version_id}.txt"
            create_text_file(full_title, chapters, txt_file)
            created_files.append(txt_file)
            print(f"  ✓ Created: {txt_file.name}")

            # Create markdown file
            md_file = output_dir / f"1esdras_{version_id}.md"
            create_markdown_file(full_title, chapters, md_file)
            created_files.append(md_file)
            print(f"  ✓ Created: {md_file.name}")

            # Create e-book HTML
            ebook_file = output_dir / f"1esdras_{version_id}_ebook.html"
            create_ebook_html(full_title, chapters, ebook_file)
            created_files.append(ebook_file)
            print(f"  ✓ Created: {ebook_file.name}")

        except Exception as e:
            print(f"  ✗ Error processing {version_name}: {e}")

    # Create a combined instructions file
    instructions_file = output_dir / "CONVERSION_INSTRUCTIONS.txt"
    with open(instructions_file, 'w', encoding='utf-8') as f:
        f.write("1 ESDRAS CONVERSION INSTRUCTIONS\n")
        f.write("=" * 60 + "\n\n")
        f.write("FILES CREATED:\n")
        f.write("-" * 40 + "\n")
        for file in created_files:
            if file.exists():
                size = file.stat().st_size / 1024
                f.write(f"  {file.name:30} ({size:.1f} KB)\n")

        f.write("\n\nTO CREATE PDF:\n")
        f.write("-" * 40 + "\n")
        f.write("1. Open any *_ebook.html file in Safari or Chrome\n")
        f.write("2. Press Cmd+P (Mac) or Ctrl+P (Windows)\n")
        f.write("3. Select 'Save as PDF' in the destination dropdown\n")
        f.write("4. Click 'Save'\n\n")

        f.write("TO CREATE KINDLE FILES:\n")
        f.write("-" * 40 + "\n")
        f.write("Option 1: Email to Kindle\n")
        f.write("  - Email the HTML or PDF files to your Kindle email address\n")
        f.write("  - Amazon will convert them automatically\n\n")

        f.write("Option 2: Install Calibre\n")
        f.write("  1. Install: brew install --cask calibre\n")
        f.write("  2. Run: ebook-convert 1esdras_ruby_ebook.html 1esdras_ruby.epub\n")
        f.write("  3. Run: ebook-convert 1esdras_ruby_ebook.html 1esdras_ruby.mobi\n\n")

        f.write("Option 3: Use Kindle Previewer\n")
        f.write("  - Download from Amazon's website\n")
        f.write("  - Open the HTML files directly\n")
        f.write("  - Export as MOBI or KPF\n")

    print("\n" + "=" * 60)
    print("CONVERSION COMPLETE!")
    print("=" * 60)
    print(f"\nFiles created in: {output_dir}")
    print("\nFile list:")
    for file in sorted(output_dir.glob("1esdras_*")):
        if file.is_file():
            size = file.stat().st_size / 1024
            print(f"  {file.name:30} ({size:6.1f} KB)")

    print("\nSee CONVERSION_INSTRUCTIONS.txt for next steps")

    return str(output_dir)

if __name__ == "__main__":
    output_path = main()
    print(f"\nOutput directory: {output_path}")