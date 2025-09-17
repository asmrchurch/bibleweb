#!/bin/bash

# Create output directory
mkdir -p output

echo "==================================="
echo "1 Esdras (エズラ第一書) Conversion"
echo "==================================="

# Check for required tools
echo "Checking for conversion tools..."

# Method 1: Using wkhtmltopdf (if available)
if command -v wkhtmltopdf &> /dev/null; then
    echo "✓ wkhtmltopdf found - creating PDFs..."
    wkhtmltopdf public/static/html/ruby/1esdras.htm output/1esdras_ruby.pdf
    wkhtmltopdf public/static/html/norm/1esdras.htm output/1esdras_norm.pdf
    echo "PDFs created in output/ directory"
else
    echo "✗ wkhtmltopdf not found"
    echo "  To install: brew install --cask wkhtmltopdf"
fi

# Method 2: Using calibre's ebook-convert (if available)
if command -v ebook-convert &> /dev/null; then
    echo "✓ ebook-convert found - creating EPUB and MOBI..."

    # Convert to EPUB (better for most e-readers)
    ebook-convert public/static/html/ruby/1esdras.htm output/1esdras_ruby.epub \
        --title "エズラ第一書（ルビ付き）" \
        --authors "外典" \
        --language ja \
        --input-encoding utf-8

    ebook-convert public/static/html/norm/1esdras.htm output/1esdras_norm.epub \
        --title "エズラ第一書" \
        --authors "外典" \
        --language ja \
        --input-encoding utf-8

    # Convert to MOBI (for older Kindles)
    ebook-convert public/static/html/ruby/1esdras.htm output/1esdras_ruby.mobi \
        --title "エズラ第一書（ルビ付き）" \
        --authors "外典" \
        --language ja \
        --input-encoding utf-8

    ebook-convert public/static/html/norm/1esdras.htm output/1esdras_norm.mobi \
        --title "エズラ第一書" \
        --authors "外典" \
        --language ja \
        --input-encoding utf-8

    echo "EPUB and MOBI files created in output/ directory"
else
    echo "✗ ebook-convert not found"
    echo "  To install: brew install --cask calibre"
fi

# Method 3: Using pandoc (if available)
if command -v pandoc &> /dev/null; then
    echo "✓ pandoc found - creating alternative formats..."

    # Convert to markdown first, then to PDF
    pandoc public/static/html/ruby/1esdras.htm -o output/1esdras_ruby.md
    pandoc public/static/html/norm/1esdras.htm -o output/1esdras_norm.md

    # If pdflatex is available, create PDF
    if command -v pdflatex &> /dev/null; then
        pandoc output/1esdras_ruby.md -o output/1esdras_ruby_pandoc.pdf --pdf-engine=pdflatex
        pandoc output/1esdras_norm.md -o output/1esdras_norm_pandoc.pdf --pdf-engine=pdflatex
    fi

    echo "Markdown files created in output/ directory"
else
    echo "✗ pandoc not found"
    echo "  To install: brew install pandoc"
fi

echo ""
echo "==================================="
echo "Conversion Summary:"
echo "==================================="
echo "HTML files processed:"
echo "  - public/static/html/ruby/1esdras.htm (with ruby/furigana)"
echo "  - public/static/html/norm/1esdras.htm (without ruby)"
echo ""
echo "Output directory: ./output/"
echo ""
echo "To view the files:"
echo "  ls -la output/"
echo ""
echo "Manual conversion options:"
echo "1. Open output/1esdras_printable.html in browser"
echo "2. Press Cmd+P (Mac) or Ctrl+P (Windows/Linux)"
echo "3. Select 'Save as PDF'"
echo ""
echo "For Kindle:"
echo "- Use the .mobi files for older Kindle devices"
echo "- Use the .epub files for newer Kindle devices"
echo "- Or email the PDF to your Kindle email address"
echo "==================================="