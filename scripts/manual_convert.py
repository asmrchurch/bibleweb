#!/usr/bin/env python3
import re
from pathlib import Path

def clean_html_content(html_content):
    """Clean HTML and extract text with ruby handling"""
    # Handle ruby tags for the ruby version
    html_content = re.sub(r'<ruby><rb>(.*?)</rb><rp>\(</rp><rt>(.*?)</rt><rp>\)</rp></ruby>',
                          r'\1(\2)', html_content)

    # Remove HTML tags
    html_content = re.sub(r'<[^>]+>', '\n', html_content)

    # Clean up extra whitespace
    lines = [line.strip() for line in html_content.split('\n') if line.strip()]
    return '\n'.join(lines)

def extract_verses_from_html(html_file):
    """Extract verses from HTML file"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract title
    title_match = re.search(r'<h2[^>]*>(.*?)</h2>', content, re.DOTALL)
    if title_match:
        title = re.sub(r'<ruby><rb>(.*?)</rb><rp>\(</rp><rt>(.*?)</rt><rp>\)</rp></ruby>',
                       r'\1', title_match.group(1))
        title = re.sub(r'<[^>]+>', '', title)
        title = re.sub(r'\s+', ' ', title).strip()
    else:
        title = "エズラ第一書"

    # Extract all verses
    verse_pattern = r'<em[^>]*id="(\d+-\d+)"[^>]*>.*?</em>\s*<span[^>]*id="verse"[^>]*>(.*?)</span>'
    verses = []

    for verse_match in re.finditer(verse_pattern, content, re.DOTALL):
        verse_id = verse_match.group(1)
        verse_text = verse_match.group(2)

        # Clean verse text
        verse_text = re.sub(r'<ruby><rb>(.*?)</rb><rp>\(</rp><rt>(.*?)</rt><rp>\)</rp></ruby>',
                           r'\1(\2)', verse_text)
        verse_text = re.sub(r'<[^>]+>', '', verse_text)
        verse_text = re.sub(r'\s+', ' ', verse_text).strip()

        verses.append(f"{verse_id} {verse_text}")

    return title, verses

def create_text_output(title, verses, output_file):
    """Create plain text file"""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"{title}\n")
        f.write("=" * 60 + "\n\n")

        current_chapter = None
        for verse in verses:
            chapter = verse.split('-')[0].split(':')[0] if ':' in verse else verse.split('-')[0]
            if chapter != current_chapter:
                f.write(f"\n第{chapter}章\n")
                f.write("-" * 40 + "\n\n")
                current_chapter = chapter

            f.write(f"{verse}\n\n")

def create_markdown_output(title, verses, output_file):
    """Create Markdown file"""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"# {title}\n\n")

        current_chapter = None
        for verse in verses:
            chapter = verse.split('-')[0].split(':')[0] if ':' in verse else verse.split('-')[0]
            if chapter != current_chapter:
                f.write(f"## 第{chapter}章\n\n")
                current_chapter = chapter

            f.write(f"{verse}\n\n")

def create_ebook_html_output(title, verses, output_file):
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

    current_chapter = None
    for verse in verses:
        chapter = verse.split('-')[0].split(':')[0] if ':' in verse else verse.split('-')[0]
        if chapter != current_chapter:
            html += f"    <h2>第{chapter}章</h2>\n"
            current_chapter = chapter

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

def main():
    # Paths
    output_dir = Path("/Users/suganolab/web/bibleweb/output")
    ruby_file = "/Users/suganolab/web/bibleweb/public/static/html/ruby/1esdras.htm"
    norm_file = "/Users/suganolab/web/bibleweb/public/static/html/norm/1esdras.htm"

    # Process ruby version
    print("Processing ruby version...")
    title_ruby, verses_ruby = extract_verses_from_html(ruby_file)
    full_title_ruby = f"{title_ruby}（ルビ付き）"

    # Create ruby files
    create_text_output(full_title_ruby, verses_ruby, output_dir / "1esdras_ruby.txt")
    create_markdown_output(full_title_ruby, verses_ruby, output_dir / "1esdras_ruby.md")
    create_ebook_html_output(full_title_ruby, verses_ruby, output_dir / "1esdras_ruby_ebook.html")

    # Process norm version
    print("Processing norm version...")
    title_norm, verses_norm = extract_verses_from_html(norm_file)
    full_title_norm = f"{title_norm}（ルビなし）"

    # Create norm files
    create_text_output(full_title_norm, verses_norm, output_dir / "1esdras_norm.txt")
    create_markdown_output(full_title_norm, verses_norm, output_dir / "1esdras_norm.md")
    create_ebook_html_output(full_title_norm, verses_norm, output_dir / "1esdras_norm_ebook.html")

    print("Conversion completed!")
    return len(verses_ruby), len(verses_norm)

if __name__ == "__main__":
    ruby_count, norm_count = main()
    print(f"Ruby version: {ruby_count} verses")
    print(f"Norm version: {norm_count} verses")