#!/bin/bash

echo "1 Esdras Manual Conversion Script"
echo "=================================="

# Change to project directory
cd /Users/suganolab/web/bibleweb

# Create output directory
mkdir -p output

echo "Step 1: Running Python conversion script..."
if command -v python3 &> /dev/null; then
    python3 generate_all_formats.py
    echo "Python script execution completed."
else
    echo "Python3 not found. Please install Python3."
fi

echo ""
echo "Step 2: Installing conversion tools..."

# Check and install wkhtmltopdf
if ! command -v wkhtmltopdf &> /dev/null; then
    echo "Installing wkhtmltopdf..."
    if command -v brew &> /dev/null; then
        brew install --cask wkhtmltopdf
    else
        echo "Homebrew not found. Please install wkhtmltopdf manually."
        echo "Download from: https://wkhtmltopdf.org/downloads.html"
    fi
else
    echo "✓ wkhtmltopdf is already installed"
fi

# Check and install calibre
if ! command -v ebook-convert &> /dev/null; then
    echo "Installing calibre..."
    if command -v brew &> /dev/null; then
        brew install --cask calibre
    else
        echo "Homebrew not found. Please install calibre manually."
        echo "Download from: https://calibre-ebook.com/download"
    fi
else
    echo "✓ calibre is already installed"
fi

echo ""
echo "Step 3: Running conversion tools..."

# Run conversions if tools are available
if command -v wkhtmltopdf &> /dev/null; then
    echo "Creating PDFs with wkhtmltopdf..."
    wkhtmltopdf output/1esdras_ruby_ebook.html output/1esdras_ruby.pdf
    wkhtmltopdf output/1esdras_norm_ebook.html output/1esdras_norm.pdf
fi

if command -v ebook-convert &> /dev/null; then
    echo "Creating EPUB and MOBI files..."
    # EPUB
    ebook-convert output/1esdras_ruby_ebook.html output/1esdras_ruby.epub \
        --title "エズラ第一書（ルビ付き）" \
        --authors "外典" \
        --language ja \
        --input-encoding utf-8

    ebook-convert output/1esdras_norm_ebook.html output/1esdras_norm.epub \
        --title "エズラ第一書" \
        --authors "外典" \
        --language ja \
        --input-encoding utf-8

    # MOBI
    ebook-convert output/1esdras_ruby_ebook.html output/1esdras_ruby.mobi \
        --title "エズラ第一書（ルビ付き）" \
        --authors "外典" \
        --language ja \
        --input-encoding utf-8

    ebook-convert output/1esdras_norm_ebook.html output/1esdras_norm.mobi \
        --title "エズラ第一書" \
        --authors "外典" \
        --language ja \
        --input-encoding utf-8
fi

echo ""
echo "Step 4: Listing output files..."
echo "Files in output directory:"
ls -la output/

echo ""
echo "=================================="
echo "Conversion process complete!"
echo "=================================="
echo ""
echo "Manual steps if tools are not installed:"
echo "1. Install tools:"
echo "   brew install --cask wkhtmltopdf"
echo "   brew install --cask calibre"
echo ""
echo "2. For PDF conversion:"
echo "   Open output/*_ebook.html in browser and print to PDF"
echo ""
echo "3. For Kindle conversion:"
echo "   Email PDF files to your Kindle email address"
echo "   Or use calibre GUI to convert HTML to EPUB/MOBI"