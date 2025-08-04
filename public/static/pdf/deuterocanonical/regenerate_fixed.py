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
            
            for i, page in enumerate(reader.pages):
                if i % 100 == 0:
                    print(f"Processing page {i+1}...")
                text = page.extract_text()
                all_text += text + "\n"
            
            return all_text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None

def extract_book_by_lines(lines, start_line, end_line, book_name):
    """Extract book text between specific line numbers"""
    book_lines = []
    
    for i in range(start_line, min(end_line, len(lines))):
        line = lines[i].strip()
        if line:
            book_lines.append(line)
    
    return '\n'.join(book_lines)

def extract_book_by_pattern(text, start_patterns, book_name):
    """Extract book text by finding start patterns"""
    lines = text.split('\n')
    
    for start_pattern in start_patterns:
        for i, line in enumerate(lines):
            if re.search(start_pattern, line, re.IGNORECASE):
                print(f"Found {book_name} starting at line {i}: {line.strip()}")
                
                # Extract text from this point
                book_lines = []
                j = i + 1
                
                # End patterns to stop extraction
                end_patterns = [
                    r'^(Genesis|Exodus|Leviticus|Numbers|Deuteronomy)',
                    r'^(Matthew|Mark|Luke|John|Acts|Romans)',
                    r'^(THE\s+HISTORY\s+OF\s+SUSANNA)',
                    r'^(BEL\s+AND\s+THE\s+DRAGON)',
                    r'^\s*THE\s+NEW\s+TESTAMENT',
                    r'^\s*Appendix'
                ]
                
                while j < len(lines) and len(book_lines) < 3000:
                    line = lines[j].strip()
                    
                    # Check if we've reached another book
                    is_end = False
                    for end_pattern in end_patterns:
                        if re.match(end_pattern, line, re.IGNORECASE) and book_name.lower() not in line.lower():
                            is_end = True
                            break
                    
                    # Also check for next deuterocanonical book
                    next_books = ['Judith', 'Wisdom', 'Sirach', 'Baruch', 'Maccabees']
                    for next_book in next_books:
                        if next_book.lower() not in book_name.lower() and next_book.lower() in line.lower():
                            if 'recognized as deuterocanonical' in line.lower() or f'{next_book} 1:1' in line:
                                is_end = True
                                break
                    
                    if is_end:
                        print(f"Stopping extraction at line {j}: {line}")
                        break
                    
                    if line:
                        book_lines.append(line)
                    
                    j += 1
                
                if book_lines:
                    return '\n'.join(book_lines)
    
    return None

def apply_basic_spacing_fixes(text):
    """Apply basic spacing fixes"""
    if not text:
        return text
    
    # Add spaces between concatenated words
    text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
    text = re.sub(r'([a-z])(\d)', r'\1 \2', text)
    text = re.sub(r'(\d)([a-z])', r'\1 \2', text)
    
    # Fix common concatenations
    fixes = [
        (r'\bofthe\b', 'of the'),
        (r'\binthe\b', 'in the'),
        (r'\btothe\b', 'to the'),
        (r'\bandthe\b', 'and the'),
        (r'\bwiththe\b', 'with the'),
        (r'\boutof\b', 'out of'),
        (r'\ballthe\b', 'all the'),
        (r'\bmylife\b', 'my life'),
        (r'\bmykindred\b', 'my kindred'),
        (r'\bmynation\b', 'my nation'),
        (r'\bmyown\b', 'my own'),
        (r'\btheways\b', 'the ways'),
        (r'\bthedays\b', 'the days'),
        (r'\btheland\b', 'the land'),
        (r'\bthehouse\b', 'the house'),
        (r'\bIwas\b', 'I was'),
        (r'\bIdid\b', 'I did'),
        (r'\bIwent\b', 'I went'),
        (r'\bmeinto\b', 'me into'),
        (r'\byetyoung\b', 'yet young'),
        (r'\bwho went\b', 'who went'),
        (r'\bwho was\b', 'who was'),
        (r'\bsonof\b', 'son of'),
        (r'\bkingof\b', 'king of'),
        (r'\btribeof\b', 'tribe of'),
    ]
    
    for pattern, replacement in fixes:
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    
    return text

def format_as_html(book_name, book_text):
    """Format book text as HTML"""
    if not book_text:
        return ""
    
    html_lines = [f"<h1 class='et'>{book_name}</h1>", "<BR>"]
    html_lines.append('<div id="contenten" style="position:relative; top:0px; left:0px; overflow:auto"><table cellpadding=0 cellspacing=0 border=0>')
    
    # Apply spacing fixes
    book_text = apply_basic_spacing_fixes(book_text)
    
    lines = book_text.split('\n')
    current_chapter = 1
    current_verse = 1
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Skip headers and metadata
        skip_patterns = [
            r'recognized as deuterocanonical',
            r'scripture by',
            r'roman catholic',
            r'greek orthodox',
            r'the book of',
            r'first book of',
            r'second book of',
            r'maccabees',
            r'page \d+',
            r'^\d+$'
        ]
        
        should_skip = False
        for pattern in skip_patterns:
            if re.search(pattern, line, re.IGNORECASE) and len(line) < 50:
                should_skip = True
                break
        
        if should_skip:
            continue
        
        # Look for chapter:verse patterns
        cv_match = re.match(r'^(\d+):(\d+)\s+(.+)', line)
        if cv_match:
            current_chapter = int(cv_match.group(1))
            current_verse = int(cv_match.group(2))
            verse_text = cv_match.group(3).strip()
            if verse_text and len(verse_text) > 3:
                html_lines.append(f'<tr><td class="vn">{current_chapter}:{current_verse}</td><td class="vn">&nbsp;&nbsp;</td><td class="v en">{verse_text}</td></tr>')
            continue
        
        # Look for verse numbers only
        verse_match = re.match(r'^(\d+)\s+(.+)', line)
        if verse_match:
            verse_num = int(verse_match.group(1))
            verse_text = verse_match.group(2).strip()
            if verse_num <= 200 and len(verse_text) > 3:  # Reasonable verse number
                current_verse = verse_num
                # Clean up spacing in verse text
                verse_text = re.sub(r'\s+', ' ', verse_text)
                html_lines.append(f'<tr><td class="vn">{current_chapter}:{current_verse}</td><td class="vn">&nbsp;&nbsp;</td><td class="v en">{verse_text}</td></tr>')
            continue
        
        # Check if it's a chapter number
        if re.match(r'^\d+$', line) and int(line) <= 50:
            current_chapter = int(line)
            current_verse = 1
            continue
        
        # Otherwise treat as continuation text
        if len(line) > 15:  # Only substantial text
            # Clean up spacing
            line = re.sub(r'\s+', ' ', line)
            html_lines.append(f'<tr><td class="vn">{current_chapter}:{current_verse}</td><td class="vn">&nbsp;&nbsp;</td><td class="v en">{line}</td></tr>')
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
    
    lines = full_text.split('\n')
    print(f"Total lines in PDF: {len(lines)}")
    
    # Extract books using known patterns and line ranges
    books_to_extract = {
        'tobit': {
            'patterns': [r'The book ofthewords ofTobit'],
            'range': (50900, 51925)
        },
        'judith': {
            'patterns': [r'Inthedays ofArphaxad'],
            'range': (51925, 54674)
        },
        'wisdom': {
            'patterns': [r'Love righteousness', r'judges oftheearth'],
            'range': (82324, 84000)
        },
        'sirach': {
            'patterns': [r'The Wisdom ofJesus theSonofSirach'],
            'range': (78533, 82324)
        },
        'baruch': {
            'patterns': [r'These arethewords ofthebook'],
            'range': (97186, 98500)
        },
        '1maccabees': {
            'patterns': [r'After Alexander theMacedonian'],
            'range': (54674, 58171)
        },
        '2maccabees': {
            'patterns': [r'Brothers living inJerusalem'],
            'range': (58172, 65000)
        },
        'susanna': {
            'patterns': [r'noon, Susanna went into'],
            'range': (105500, 107000)
        }
    }
    
    output_dir = "../html/en/"
    os.makedirs(output_dir, exist_ok=True)
    
    for book_key, book_info in books_to_extract.items():
        print(f"\nExtracting {book_key}...")
        
        # Try pattern-based extraction first
        book_text = extract_book_by_pattern(full_text, book_info['patterns'], book_key)
        
        # If pattern fails, try line range
        if not book_text:
            print(f"Pattern failed, trying line range {book_info['range']}")
            start_line, end_line = book_info['range']
            book_text = extract_book_by_lines(lines, start_line, end_line, book_key)
        
        if book_text:
            html_content = format_as_html(book_key.replace('maccabees', ' Maccabees').title(), book_text)
            output_file = os.path.join(output_dir, f"{book_key}.htm")
            
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            print(f"Created {output_file}")
        else:
            print(f"Could not extract {book_key}")

if __name__ == "__main__":
    main()