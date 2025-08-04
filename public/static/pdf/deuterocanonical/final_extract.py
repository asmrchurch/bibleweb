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

def format_as_html(book_name, book_text):
    """Format book text as HTML"""
    if not book_text:
        return ""
    
    html_lines = [f"<h1 class='et'>{book_name}</h1>", "<BR>"]
    html_lines.append('<div id="contenten" style="position:relative; top:0px; left:0px; overflow:auto"><table cellpadding=0 cellspacing=0 border=0>')
    
    # Clean text
    book_text = re.sub(r'(\w)([A-Z])', r'\1 \2', book_text)
    book_text = re.sub(r'([a-z])(\d)', r'\1 \2', book_text)
    book_text = re.sub(r'(\d)([a-z])', r'\1 \2', book_text)
    
    lines = book_text.split('\n')
    current_chapter = 1
    current_verse = 1
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Skip headers and metadata
        if any(x in line.lower() for x in ['maccabees', 'recognized as deuterocanonical', 'scripture by']):
            continue
        if re.match(r'^\d+$', line) and len(line) <= 3:
            continue
        
        # Look for chapter:verse patterns
        cv_match = re.match(r'^(\d+):(\d+)\s+(.+)', line)
        if cv_match:
            current_chapter = int(cv_match.group(1))
            current_verse = int(cv_match.group(2))
            verse_text = cv_match.group(3).strip()
            if verse_text:
                html_lines.append(f'<tr><td class="vn">{current_chapter}:{current_verse}</td><td class="vn">&nbsp;&nbsp;</td><td class="v en">{verse_text}</td></tr>')
            continue
        
        # Look for verse numbers only
        verse_match = re.match(r'^(\d+)\s+(.+)', line)
        if verse_match:
            verse_num = int(verse_match.group(1))
            verse_text = verse_match.group(2).strip()
            if verse_num <= 200:  # Reasonable verse number
                current_verse = verse_num
                if verse_text and len(verse_text) > 3:
                    html_lines.append(f'<tr><td class="vn">{current_chapter}:{current_verse}</td><td class="vn">&nbsp;&nbsp;</td><td class="v en">{verse_text}</td></tr>')
            continue
        
        # Check if it's a chapter number
        if re.match(r'^\d+$', line) and int(line) <= 50:
            current_chapter = int(line)
            current_verse = 1
            continue
        
        # Otherwise treat as continuation text
        if len(line) > 10:
            # Clean up spacing
            line = re.sub(r'\s+', ' ', line)
            line = line.replace(' ,', ',').replace(' .', '.').replace(' ;', ';')
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
    
    # Based on the search results, extract books with approximate line ranges
    books_to_extract = {
        '1maccabees': (54674, 58171),  # From line 54674 to before 2 Maccabees
        '2maccabees': (58172, 65000),  # From line 58172 onwards, estimate end
        'sirach': (78533, 82324),      # From line 78533 to before Wisdom
    }
    
    output_dir = "../html/en/"
    os.makedirs(output_dir, exist_ok=True)
    
    for book_key, (start_line, end_line) in books_to_extract.items():
        print(f"\nExtracting {book_key} from lines {start_line} to {end_line}...")
        
        # Find the actual end line by looking for the next book
        actual_end = end_line
        for i in range(start_line + 100, min(end_line, len(lines))):
            line = lines[i].strip()
            # Look for indicators of next book/section
            if any(indicator in line.lower() for indicator in [
                'wisdom of solomon', 'baruch', 'tobit', 'judith',
                'the new testament', 'appendix'
            ]):
                actual_end = i
                print(f"Found end marker at line {i}: {line}")
                break
        
        book_text = extract_book_by_lines(lines, start_line, actual_end, book_key)
        
        if book_text:
            html_content = format_as_html(book_key.replace('maccabees', ' Maccabees').title(), book_text)
            output_file = os.path.join(output_dir, f"{book_key}.htm")
            
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            print(f"Created {output_file} with {len(book_text.split())} words")
        else:
            print(f"No content extracted for {book_key}")

if __name__ == "__main__":
    main()