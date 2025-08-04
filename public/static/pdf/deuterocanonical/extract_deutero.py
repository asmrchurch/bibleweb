#!/usr/bin/env python3
import PyPDF2
import re
import os

def extract_pdf_text(pdf_path):
    """Extract all text from PDF"""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            all_text = ""
            print(f"Processing {len(reader.pages)} pages...")
            
            for i, page in enumerate(reader.pages):
                if i % 100 == 0:
                    print(f"Processing page {i+1}...")
                text = page.extract_text()
                all_text += text + "\n"
            
            return all_text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None

def find_deuterocanonical_books(text):
    """Find and extract deuterocanonical books from the text"""
    
    # Books to extract with their possible variations
    deutero_books = {
        'tobit': ['Tobit', 'TOBIT', 'The Book of Tobit'],
        'judith': ['Judith', 'JUDITH', 'The Book of Judith'],
        'wisdom': ['Wisdom of Solomon', 'Wisdom', 'WISDOM OF SOLOMON', 'WISDOM', 'The Wisdom of Solomon'],
        'sirach': ['Sirach', 'Ecclesiasticus', 'SIRACH', 'ECCLESIASTICUS', 'The Wisdom of Jesus the Son of Sirach'],
        'baruch': ['Baruch', 'BARUCH', 'The Book of Baruch'],
        '1maccabees': ['1 Maccabees', '1Maccabees', 'I Maccabees', 'FIRST MACCABEES', 'The First Book of Maccabees'],
        '2maccabees': ['2 Maccabees', '2Maccabees', 'II Maccabees', 'SECOND MACCABEES', 'The Second Book of Maccabees'],
        'esther_additions': ['Additions to Esther', 'ADDITIONS TO ESTHER', 'The Rest of Esther'],
        'daniel_additions': ['Additions to Daniel', 'ADDITIONS TO DANIEL', 'Prayer of Azariah', 'Song of the Three Young Men', 'Susanna', 'Bel and the Dragon']
    }
    
    found_books = {}
    
    # Split text into lines for easier processing
    lines = text.split('\n')
    
    # Look for book headers
    for book_key, book_names in deutero_books.items():
        print(f"Looking for {book_key}...")
        for book_name in book_names:
            # Look for the book name as a header
            pattern = rf'^{re.escape(book_name)}\s*$'
            for i, line in enumerate(lines):
                if re.match(pattern, line.strip(), re.IGNORECASE):
                    print(f"Found {book_name} at line {i}")
                    # Extract text from this point until next book
                    book_text = extract_book_text(lines, i, book_key)
                    if book_text:
                        found_books[book_key] = book_text
                    break
    
    return found_books

def extract_book_text(lines, start_line, book_key):
    """Extract text for a specific book"""
    book_text = []
    i = start_line + 1
    
    # Common book names that might indicate end of current book
    next_book_indicators = [
        'Genesis', 'Exodus', 'Leviticus', 'Numbers', 'Deuteronomy',
        'Joshua', 'Judges', 'Ruth', '1 Samuel', '2 Samuel',
        'Matthew', 'Mark', 'Luke', 'John', 'Acts',
        'Tobit', 'Judith', 'Wisdom', 'Sirach', 'Baruch',
        '1 Maccabees', '2 Maccabees'
    ]
    
    while i < len(lines):
        line = lines[i].strip()
        
        # Check if we've reached another book
        if any(line.startswith(book) for book in next_book_indicators):
            if not line.startswith(book_key.title()):
                break
        
        # Skip empty lines and page numbers
        if line and not re.match(r'^\d+$', line):
            book_text.append(line)
        
        i += 1
        
        # Safety check - don't extract more than 1000 lines per book
        if len(book_text) > 1000:
            break
    
    return '\n'.join(book_text) if book_text else None

def format_as_html(book_name, book_text):
    """Format book text as HTML similar to existing structure"""
    html_lines = [f"<h1 class='et'>{book_name}</h1>", "<BR>"]
    html_lines.append('<div id="contenten" style="position:relative; top:0px; left:0px; overflow:auto"><table cellpadding=0 cellspacing=0 border=0>')
    
    # Clean up text spacing issues
    book_text = re.sub(r'(\w)([A-Z])', r'\1 \2', book_text)  # Add space before capital letters
    book_text = re.sub(r'([a-z])([0-9])', r'\1 \2', book_text)  # Add space before numbers
    book_text = re.sub(r'([0-9])([a-z])', r'\1 \2', book_text)  # Add space after numbers
    
    # Try to parse verse structure
    lines = book_text.split('\n')
    current_chapter = 1
    current_verse = 1
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Skip headers and page numbers
        if re.match(r'^(Tobit|Judith|Wisdom|Sirach|Baruch|Maccabees|Ecclesiasticus)', line, re.IGNORECASE):
            continue
        if re.match(r'^\d+$', line) and len(line) <= 3:
            continue
            
        # Look for chapter indicators
        chapter_match = re.match(r'^(?:Chapter\s+)?(\d+)$', line, re.IGNORECASE)
        if chapter_match:
            current_chapter = int(chapter_match.group(1))
            current_verse = 1
            continue
        
        # Look for verse numbers at start of line
        verse_match = re.match(r'^(\d+)\s*(.+)', line)
        if verse_match:
            verse_num = int(verse_match.group(1))
            verse_text = verse_match.group(2).strip()
            current_verse = verse_num
            
            # Clean up text formatting
            verse_text = re.sub(r'\s+', ' ', verse_text)  # Normalize whitespace
            verse_text = verse_text.replace(' ,', ',').replace(' .', '.').replace(' ;', ';')
            
            if verse_text and len(verse_text) > 2:
                html_lines.append(f'<tr><td class="vn">{current_chapter}:{current_verse}</td><td class="vn">&nbsp;&nbsp;</td><td class="v en">{verse_text}</td></tr>')
        else:
            # This might be a continuation of the previous verse
            verse_text = line.strip()
            verse_text = re.sub(r'\s+', ' ', verse_text)
            verse_text = verse_text.replace(' ,', ',').replace(' .', '.').replace(' ;', ';')
            
            if verse_text and len(verse_text) > 10:  # Only add substantial text
                html_lines.append(f'<tr><td class="vn">{current_chapter}:{current_verse}</td><td class="vn">&nbsp;&nbsp;</td><td class="v en">{verse_text}</td></tr>')
                current_verse += 1
    
    html_lines.append('</table></div>')
    return '\n'.join(html_lines)

def main():
    pdf_path = "eng-web-c_all.pdf"
    
    if not os.path.exists(pdf_path):
        print(f"PDF file {pdf_path} not found!")
        return
    
    print("Extracting text from PDF...")
    full_text = extract_pdf_text(pdf_path)
    
    if not full_text:
        print("Failed to extract text from PDF")
        return
    
    print("Searching for deuterocanonical books...")
    books = find_deuterocanonical_books(full_text)
    
    if books:
        print(f"Found {len(books)} deuterocanonical books:")
        for book_name in books.keys():
            print(f"- {book_name}")
        
        # Create HTML files
        output_dir = "../html/en/"
        os.makedirs(output_dir, exist_ok=True)
        
        for book_key, book_text in books.items():
            html_content = format_as_html(book_key.title(), book_text)
            output_file = os.path.join(output_dir, f"{book_key}.htm")
            
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            print(f"Created {output_file}")
    else:
        print("No deuterocanonical books found in the PDF")
        # Let's try to find what books are actually in the PDF
        print("\nFirst 2000 characters of PDF text:")
        print(full_text[:2000])
    
    # Search for missing books by looking for common patterns
    print("\nSearching for missing books...")
    missing_patterns = [
        'Sirach', 'Ecclesiasticus', 'Maccabees', 'First Book of Maccabees', 
        'Second Book of Maccabees', 'Additions to Esther', 'Additions to Daniel',
        'Prayer of Azariah', 'Song of the Three', 'Susanna', 'Bel and the Dragon'
    ]
    
    for pattern in missing_patterns:
        matches = []
        lines = full_text.split('\n')
        for i, line in enumerate(lines):
            if pattern.lower() in line.lower():
                matches.append((i, line.strip()))
        
        if matches:
            print(f"\nFound '{pattern}' at {len(matches)} locations:")
            for line_num, line_text in matches[:5]:  # Show first 5 matches
                print(f"  Line {line_num}: {line_text}")
        else:
            print(f"'{pattern}' not found")

if __name__ == "__main__":
    main()