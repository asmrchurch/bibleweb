#!/usr/bin/env python3
import os
from pathlib import Path
import re

def html_to_text(html_file, text_file):
    """Convert HTML to plain text"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove HTML tags but keep text
    # First, handle ruby tags specially to preserve both base and ruby text
    content = re.sub(r'<ruby><rb>(.*?)</rb><rp>\(</rp><rt>(.*?)</rt><rp>\)</rp></ruby>',
                     r'\1(\2)', content)

    # Remove remaining HTML tags
    content = re.sub(r'<[^>]+>', '', content)

    # Clean up whitespace
    content = re.sub(r'\n\s*\n', '\n\n', content)
    content = re.sub(r' +', ' ', content)

    # Write to text file
    with open(text_file, 'w', encoding='utf-8') as f:
        f.write(content.strip())

    print(f"Created text file: {text_file}")
    return text_file

def main():
    # Create output directory
    output_dir = Path("/Users/suganolab/web/bibleweb/output")
    output_dir.mkdir(exist_ok=True)

    # Convert both versions to text
    files = [
        ("/Users/suganolab/web/bibleweb/public/static/html/ruby/1esdras.htm", "1esdras_ruby.txt"),
        ("/Users/suganolab/web/bibleweb/public/static/html/norm/1esdras.htm", "1esdras_norm.txt")
    ]

    for html_file, output_name in files:
        output_file = output_dir / output_name
        html_to_text(html_file, output_file)

    print("\nText conversion complete!")
    print(f"Files saved in: {output_dir}")
    print("\nTo convert to PDF, you can:")
    print("1. Install wkhtmltopdf: brew install --cask wkhtmltopdf")
    print("2. Then run: wkhtmltopdf <html_file> <pdf_file>")
    print("\nTo convert to Kindle format:")
    print("1. Install calibre: brew install --cask calibre")
    print("2. Use ebook-convert command from calibre")
    print("   ebook-convert <html_file> <output.mobi>")
    print("   ebook-convert <html_file> <output.epub>")

if __name__ == "__main__":
    main()