#!/bin/bash

# 1 Esdras PDF and Kindle Converter - Updated Version
# Using calibre for all conversions (wkhtmltopdf is discontinued)

echo "==================================="
echo "1 Esdras Converter - Updated Version"
echo "==================================="

# Change to output directory
cd /Users/suganolab/web/bibleweb/output

# Check if calibre is installed
if ! command -v ebook-convert &> /dev/null; then
    echo "Calibre not found. Installing..."
    /opt/homebrew/bin/brew install --cask calibre
    # Add calibre to PATH
    export PATH="/Applications/calibre.app/Contents/MacOS:$PATH"
else
    echo "✓ Calibre is available"
fi

echo ""
echo "Creating PDF files using calibre..."

# Create PDF files using calibre (better than discontinued wkhtmltopdf)
if ebook-convert 1esdras_ruby_ebook.html 1esdras_ruby.pdf \
    --language ja \
    --title "エズラ第一書（ルビ付き）" \
    --authors "外典" \
    --margin-top 20 \
    --margin-bottom 20 \
    --margin-left 15 \
    --margin-right 15 \
    --pdf-page-numbers \
    --pdf-serif-family "Hiragino Mincho ProN" \
    --base-font-size 11; then
    echo "✓ Created: 1esdras_ruby.pdf"
else
    echo "✗ Failed to create ruby PDF"
fi

if ebook-convert 1esdras_norm_ebook.html 1esdras_norm.pdf \
    --language ja \
    --title "エズラ第一書（ルビなし）" \
    --authors "外典" \
    --margin-top 20 \
    --margin-bottom 20 \
    --margin-left 15 \
    --margin-right 15 \
    --pdf-page-numbers \
    --pdf-serif-family "Hiragino Mincho ProN" \
    --base-font-size 11; then
    echo "✓ Created: 1esdras_norm.pdf"
else
    echo "✗ Failed to create norm PDF"
fi

echo ""
echo "Creating EPUB files for Kindle..."

# Create EPUB files
if ebook-convert 1esdras_ruby_ebook.html 1esdras_ruby.epub \
    --language ja \
    --title "エズラ第一書（ルビ付き）" \
    --authors "外典" \
    --series "外典" \
    --tags "聖書,外典,エズラ" \
    --book-producer "Claude Conversion" \
    --publisher "suganolab" \
    --cover-title "エズラ第一書（ルビ付き）"; then
    echo "✓ Created: 1esdras_ruby.epub"
else
    echo "✗ Failed to create ruby EPUB"
fi

if ebook-convert 1esdras_norm_ebook.html 1esdras_norm.epub \
    --language ja \
    --title "エズラ第一書（ルビなし）" \
    --authors "外典" \
    --series "外典" \
    --tags "聖書,外典,エズラ" \
    --book-producer "Claude Conversion" \
    --publisher "suganolab" \
    --cover-title "エズラ第一書（ルビなし）"; then
    echo "✓ Created: 1esdras_norm.epub"
else
    echo "✗ Failed to create norm EPUB"
fi

echo ""
echo "Creating MOBI files for older Kindles..."

# Create MOBI files
if ebook-convert 1esdras_ruby_ebook.html 1esdras_ruby.mobi \
    --language ja \
    --title "エズラ第一書（ルビ付き）" \
    --authors "外典" \
    --series "外典" \
    --tags "聖書,外典,エズラ" \
    --book-producer "Claude Conversion" \
    --publisher "suganolab"; then
    echo "✓ Created: 1esdras_ruby.mobi"
else
    echo "✗ Failed to create ruby MOBI"
fi

if ebook-convert 1esdras_norm_ebook.html 1esdras_norm.mobi \
    --language ja \
    --title "エズラ第一書（ルビなし）" \
    --authors "外典" \
    --series "外典" \
    --tags "聖書,外典,エズラ" \
    --book-producer "Claude Conversion" \
    --publisher "suganolab"; then
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
echo "✓ PDF files: Ready for reading and printing"
echo "✓ EPUB files: Send to Kindle via email or copy to device"
echo "✓ MOBI files: Copy directly to older Kindle devices"
echo ""
echo "To send to Kindle:"
echo "1. Email the EPUB files to your @kindle.com address"
echo "2. Or copy MOBI files to Kindle via USB"
echo "3. Or use Kindle app to open EPUB files directly"