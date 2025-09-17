#!/usr/bin/env python3
import os
import sys
from pathlib import Path

# Try different libraries based on what's available
try:
    import pdfkit
    PDFKIT_AVAILABLE = True
except ImportError:
    PDFKIT_AVAILABLE = False

try:
    from weasyprint import HTML
    WEASYPRINT_AVAILABLE = True
except ImportError:
    WEASYPRINT_AVAILABLE = False

try:
    from reportlab.lib.pagesizes import A4
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.lib.enums import TA_JUSTIFY
    from bs4 import BeautifulSoup
    REPORTLAB_AVAILABLE = True
except ImportError:
    REPORTLAB_AVAILABLE = False

def convert_with_reportlab(html_file, pdf_file):
    """Convert HTML to PDF using ReportLab"""
    print(f"Converting with ReportLab: {html_file} -> {pdf_file}")

    # Read HTML content
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Parse HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Create PDF
    doc = SimpleDocTemplate(pdf_file, pagesize=A4,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=18)

    # Container for the 'Flowable' objects
    story = []

    # Define styles
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Japanese',
                               fontName='Helvetica',
                               fontSize=10,
                               leading=14))

    # Extract title
    title = soup.find('h2')
    if title:
        story.append(Paragraph(title.get_text(), styles['Title']))
        story.append(Spacer(1, 12))

    # Process content
    for elem in soup.find_all(['h3', 'div', 'em', 'span']):
        if elem.name == 'h3':
            story.append(Spacer(1, 12))
            story.append(Paragraph(elem.get_text(), styles['Heading2']))
            story.append(Spacer(1, 6))
        elif elem.name == 'em' and elem.get('id'):
            # Verse number
            text = elem.get_text()
            if text:
                story.append(Paragraph(f"<b>{text}</b>", styles['Japanese']))
        elif elem.name == 'span' and elem.get('id') == 'verse':
            # Verse content
            text = elem.get_text()
            if text:
                story.append(Paragraph(text, styles['Japanese']))
                story.append(Spacer(1, 6))

    # Build PDF
    doc.build(story)
    print(f"PDF created: {pdf_file}")

def convert_html_to_pdf_simple(html_file, pdf_file):
    """Simple HTML to PDF conversion using basic Python"""
    print(f"Converting with simple method: {html_file} -> {pdf_file}")

    # Read HTML content
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # For now, create a simple text version
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract text content
    text_content = []

    # Get title
    title = soup.find('h2')
    if title:
        text_content.append(title.get_text())
        text_content.append("=" * 50)
        text_content.append("")

    # Get chapters and verses
    for chapter in soup.find_all('h3'):
        text_content.append("")
        text_content.append(chapter.get_text())
        text_content.append("-" * 30)

        # Get verses in this chapter
        parent = chapter.parent
        if parent:
            verses = parent.find_all('em')
            for verse in verses:
                verse_num = verse.get_text()
                # Find the corresponding verse text
                verse_span = verse.find_next_sibling('span')
                if verse_span and verse_span.get('id') == 'verse':
                    verse_text = verse_span.get_text()
                    text_content.append(f"{verse_num} {verse_text}")
                    text_content.append("")

    # Save as text file first
    txt_file = pdf_file.replace('.pdf', '.txt')
    with open(txt_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(text_content))
    print(f"Text file created: {txt_file}")

    return txt_file

def main():
    # Input files
    ruby_html = "/Users/suganolab/web/bibleweb/public/static/html/ruby/1esdras.htm"
    norm_html = "/Users/suganolab/web/bibleweb/public/static/html/norm/1esdras.htm"

    # Output directory
    output_dir = Path("/Users/suganolab/web/bibleweb/output")
    output_dir.mkdir(exist_ok=True)

    # Check which libraries are available
    print("Checking available libraries...")
    print(f"pdfkit: {PDFKIT_AVAILABLE}")
    print(f"weasyprint: {WEASYPRINT_AVAILABLE}")
    print(f"reportlab: {REPORTLAB_AVAILABLE}")

    # Convert Ruby version
    print("\nConverting Ruby version (with furigana)...")
    if REPORTLAB_AVAILABLE:
        try:
            convert_with_reportlab(ruby_html, output_dir / "1esdras_ruby.pdf")
        except Exception as e:
            print(f"ReportLab conversion failed: {e}")
            convert_html_to_pdf_simple(ruby_html, output_dir / "1esdras_ruby.pdf")
    else:
        convert_html_to_pdf_simple(ruby_html, output_dir / "1esdras_ruby.pdf")

    # Convert Normal version
    print("\nConverting Normal version (without furigana)...")
    if REPORTLAB_AVAILABLE:
        try:
            convert_with_reportlab(norm_html, output_dir / "1esdras_norm.pdf")
        except Exception as e:
            print(f"ReportLab conversion failed: {e}")
            convert_html_to_pdf_simple(norm_html, output_dir / "1esdras_norm.pdf")
    else:
        convert_html_to_pdf_simple(norm_html, output_dir / "1esdras_norm.pdf")

    print("\nConversion complete!")
    print(f"Output files are in: {output_dir}")

if __name__ == "__main__":
    main()