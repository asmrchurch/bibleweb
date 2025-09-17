#!/bin/bash

echo "=== PDF Conversion Diagnostic ==="

# Check current directory
echo "Current directory: $(pwd)"

# Check if output directory exists
if [ -d "output" ]; then
    echo "✓ Output directory exists"
    cd output
else
    echo "✗ Output directory not found"
    exit 1
fi

# Check if required HTML files exist
if [ -f "1esdras_ruby_ebook.html" ]; then
    echo "✓ Ruby HTML file exists"
else
    echo "✗ Ruby HTML file missing"
fi

if [ -f "1esdras_norm_ebook.html" ]; then
    echo "✓ Norm HTML file exists"
else
    echo "✗ Norm HTML file missing"
fi

# Check if calibre is installed
if command -v ebook-convert &> /dev/null; then
    echo "✓ Calibre ebook-convert found at: $(which ebook-convert)"
else
    echo "✗ Calibre ebook-convert not found"
    echo "Installing Calibre..."
    /opt/homebrew/bin/brew install --cask calibre
fi

# Test conversion with minimal options
echo ""
echo "Testing PDF conversion..."
if ebook-convert 1esdras_ruby_ebook.html test_output.pdf --language ja --title "Test"; then
    echo "✓ Test conversion successful"
    ls -la test_output.pdf
else
    echo "✗ Test conversion failed"
fi

echo ""
echo "Files in output directory:"
ls -la *.html *.pdf 2>/dev/null || echo "No PDF files found"