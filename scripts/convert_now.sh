#!/bin/bash

# 1 Esdras PDF and Kindle Converter
# This script will create PDF and Kindle files

echo "==================================="
echo "1 Esdras Converter Starting..."
echo "==================================="

# Change to output directory
cd /Users/suganolab/web/bibleweb/output

# Check if tools are installed
if ! command -v wkhtmltopdf &> /dev/null; then
    echo "Installing wkhtmltopdf..."
    /opt/homebrew/bin/brew install --cask wkhtmltopdf
fi

if ! command -v ebook-convert &> /dev/null; then
    echo "Installing calibre..."
    /opt/homebrew/bin/brew install --cask calibre
fi

echo "Creating PDF files..."

# Create PDF files
if wkhtmltopdf 1esdras_ruby_ebook.html 1esdras_ruby.pdf; then
    echo "✓ Created: 1esdras_ruby.pdf"
else
    echo "✗ Failed to create ruby PDF"
fi

if wkhtmltopdf 1esdras_norm_ebook.html 1esdras_norm.pdf; then
    echo "✓ Created: 1esdras_norm.pdf"
else
    echo "✗ Failed to create norm PDF"
fi

echo "Creating EPUB files..."

# Create EPUB files
if ebook-convert 1esdras_ruby_ebook.html 1esdras_ruby.epub --language ja --title "エズラ第一書（ルビ付き）"; then
    echo "✓ Created: 1esdras_ruby.epub"
else
    echo "✗ Failed to create ruby EPUB"
fi

if ebook-convert 1esdras_norm_ebook.html 1esdras_norm.epub --language ja --title "エズラ第一書（ルビなし）"; then
    echo "✓ Created: 1esdras_norm.epub"
else
    echo "✗ Failed to create norm EPUB"
fi

echo "Creating MOBI files..."

# Create MOBI files
if ebook-convert 1esdras_ruby_ebook.html 1esdras_ruby.mobi --language ja --title "エズラ第一書（ルビ付き）"; then
    echo "✓ Created: 1esdras_ruby.mobi"
else
    echo "✗ Failed to create ruby MOBI"
fi

if ebook-convert 1esdras_norm_ebook.html 1esdras_norm.mobi --language ja --title "エズラ第一書（ルビなし）"; then
    echo "✓ Created: 1esdras_norm.mobi"
else
    echo "✗ Failed to create norm MOBI"
fi

echo ""
echo "==================================="
echo "Conversion Complete!"
echo "==================================="
echo "Files created:"
ls -la *.pdf *.epub *.mobi 2>/dev/null || echo "No files found"
echo ""
echo "PDF files: Ready for reading"
echo "EPUB files: Send to Kindle via email or copy to device"
echo "MOBI files: Copy directly to older Kindle devices"