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
                    r'^(Tobit|Judith|Wisdom|Sirach|Baruch|Maccabees)',
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
                    
                    if is_end:
                        print(f"Stopping extraction at line {j}: {line}")
                        break
                    
                    if line:
                        book_lines.append(line)
                    
                    j += 1
                
                if book_lines:
                    return '\n'.join(book_lines)
    
    return None

def clean_and_format_text(text, book_name):
    """Clean and format the extracted text"""
    if not text:
        return None
    
    # Clean up common PDF extraction issues
    text = re.sub(r'(\w)([A-Z])', r'\1 \2', text)  # Space before capitals
    text = re.sub(r'([a-z])(\d)', r'\1 \2', text)   # Space before numbers
    text = re.sub(r'(\d)([a-z])', r'\1 \2', text)   # Space after numbers
    
    lines = text.split('\n')
    cleaned_lines = []
    
    for line in lines:
        line = line.strip()
        
        # Skip empty lines, headers, and page numbers
        if not line:
            continue
        if re.match(rf'^({book_name}|Sirach|Ecclesiasticus|Maccabees)', line, re.IGNORECASE):
            continue
        if re.match(r'^\d+$', line) and len(line) <= 4:
            continue
        if 'recognized as Deuterocanonical Scripture' in line:
            continue
        
        # Clean up spacing
        line = re.sub(r'\s+', ' ', line)
        line = line.replace(' ,', ',').replace(' .', '.').replace(' ;', ';')
        
        if len(line) > 3:
            cleaned_lines.append(line)
    
    return '\n'.join(cleaned_lines)

def format_as_html(book_name, book_text):
    """Format book text as HTML"""
    if not book_text:
        return ""
    
    html_lines = [f"<h1 class='et'>{book_name}</h1>", "<BR>"]
    html_lines.append('<div id="contenten" style="position:relative; top:0px; left:0px; overflow:auto"><table cellpadding=0 cellspacing=0 border=0>')
    
    lines = book_text.split('\n')
    current_chapter = 1
    current_verse = 1
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Look for chapter indicators
        chapter_match = re.match(r'^(\d+)$', line)
        if chapter_match and int(chapter_match.group(1)) <= 100:  # Reasonable chapter number
            current_chapter = int(chapter_match.group(1))
            current_verse = 1
            continue
        
        # Look for verse numbers
        verse_match = re.match(r'^(\d+)\s+(.+)', line)
        if verse_match:
            verse_num = int(verse_match.group(1))
            verse_text = verse_match.group(2).strip()
            if verse_num <= 200:  # Reasonable verse number
                current_verse = verse_num
                if verse_text and len(verse_text) > 3:
                    html_lines.append(f'<tr><td class="vn">{current_chapter}:{current_verse}</td><td class="vn">&nbsp;&nbsp;</td><td class="v en">{verse_text}</td></tr>')
        else:
            # Treat as continuation or new verse
            if len(line) > 10:
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
    
    # Define books to extract with their search patterns
    books_to_extract = {
        'sirach': [
            r'The\s+Wisdom\s+of\s+Jesus\s+the\s+Son\s+of\s+Sirach',
            r'Sirach\s+1:\d+',
            r'also\s+called\s+Ecclesiasticus'
        ],
        '1maccabees': [
            r'1\s*Maccabees\s+1:\d+',
            r'First\s+Book\s+of\s+Maccabees'
        ],
        '2maccabees': [
            r'2\s*Maccabees\s+1:\d+',
            r'Second\s+Book\s+of\s+Maccabees'
        ],
        'susanna': [
            r'THE\s+HISTORY\s+OF\s+SUSANNA',
            r'Susanna\s+went\s+into'
        ],
        'bel': [
            r'BEL\s+AND\s+THE\s+DRAGON',
            r'Daniel\s+and\s+Bel'
        ],
        'prayer_azariah': [
            r'THE\s+PRAYER\s+OF\s+AZARIAH',
            r'Prayer\s+of\s+Azariah'
        ],
        'song_three': [
            r'THE\s+SONG\s+OF\s+THE\s+THREE\s+YOUNG\s+MEN',
            r'Song\s+of\s+the\s+Three'
        ]
    }
    
    output_dir = "../html/en/"
    os.makedirs(output_dir, exist_ok=True)
    
    for book_key, patterns in books_to_extract.items():
        print(f"\nExtracting {book_key}...")
        book_text = extract_book_by_pattern(full_text, patterns, book_key)
        
        if book_text:
            cleaned_text = clean_and_format_text(book_text, book_key)
            if cleaned_text:
                html_content = format_as_html(book_key.replace('_', ' ').title(), cleaned_text)
                output_file = os.path.join(output_dir, f"{book_key}.htm")
                
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(html_content)
                
                print(f"Created {output_file}")
            else:
                print(f"No content extracted for {book_key}")
        else:
            print(f"Could not find {book_key}")

if __name__ == "__main__":
    main()