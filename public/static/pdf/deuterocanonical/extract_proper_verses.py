#!/usr/bin/env python3
import PyPDF2
import re
import os

def clean_and_fix_text(text):
    """Clean and fix spacing issues in extracted text"""
    # Remove extra whitespace and newlines
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Fix common word concatenations
    fixes = [
        (r'ofthe', 'of the'), (r'tothe', 'to the'), (r'inthe', 'in the'),
        (r'onthe', 'on the'), (r'atthe', 'at the'), (r'forthe', 'for the'),
        (r'bythe', 'by the'), (r'withthe', 'with the'), (r'fromthe', 'from the'),
        (r'andthe', 'and the'), (r'allthe', 'all the'), (r'thatthe', 'that the'),
        (r'whenthe', 'when the'), (r'wherethe', 'where the'), (r'whichthe', 'which the'),
        (r'andI', 'and I'), (r'thatI', 'that I'), (r'whenI', 'when I'),
        (r'ifI', 'if I'), (r'asI', 'as I'), (r'soI', 'so I'), (r'butI', 'but I'),
        (r'theson', 'the son'), (r'hisson', 'his son'), (r'herdaughter', 'her daughter'),
        (r'myfather', 'my father'), (r'mymother', 'my mother'), (r'myGod', 'my God'),
        (r'mypeople', 'my people'), (r'mykindred', 'my kindred'), (r'mynation', 'my nation'),
        (r'mylife', 'my life'), (r'myown', 'my own'), (r'myheart', 'my heart'),
        (r'hisfather', 'his father'), (r'hismother', 'his mother'), (r'hisheart', 'his heart'),
        (r'hishands', 'his hands'), (r'hishouse', 'his house'), (r'hisway', 'his way'),
        (r'hisname', 'his name'), (r'theLord', 'the Lord'), (r'ofGod', 'of God'),
        (r'toGod', 'to God'), (r'withGod', 'with God'), (r'beforeGod', 'before God'),
        (r'awife', 'a wife'), (r'ahusband', 'a husband'), (r'achild', 'a child'),
        (r'aman', 'a man'), (r'awoman', 'a woman'), (r'ayoung', 'a young'),
        (r'allages', 'all ages'), (r'thetribes', 'the tribes'), (r'thedays', 'the days'),
        (r'thetime', 'the time'), (r'theland', 'the land'), (r'thehouse', 'the house'),
        (r'theway', 'the way'), (r'theword', 'the word'), (r'thepeople', 'the people'),
        (r'wascarried', 'was carried'), (r'wasleft', 'was left'), (r'washallowed', 'was hallowed'),
        (r'wasbuilt', 'was built'), (r'waschosen', 'was chosen'), (r'hasbeen', 'has been'),
        (r'havebeen', 'have been'), (r'willbe', 'will be'), (r'shallbe', 'shall be')
    ]
    
    for pattern, replacement in fixes:
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    
    # Fix punctuation spacing
    text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)  # Add space between lowercase and uppercase
    text = re.sub(r'(\w),(\w)', r'\1, \2', text)  # Add space after comma
    text = re.sub(r'(\w)\.(\w)', r'\1. \2', text)  # Add space after period
    text = re.sub(r'(\w);(\w)', r'\1; \2', text)  # Add space after semicolon
    text = re.sub(r'(\w):(\w)', r'\1: \2', text)  # Add space after colon
    
    # Fix multiple spaces
    text = re.sub(r'\s+', ' ', text)
    
    return text.strip()

def extract_book_text(pdf_reader, start_page, end_page, book_name):
    """Extract text for a specific book from PDF"""
    book_text = ""
    
    for page_num in range(start_page - 1, min(end_page, len(pdf_reader.pages))):
        page = pdf_reader.pages[page_num]
        text = page.extract_text()
        book_text += text + "\n"
    
    return book_text

def parse_verses(text, book_name):
    """Parse verses from extracted text"""
    lines = text.split('\n')
    verses = []
    current_chapter = 1
    current_verse = 1
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Skip metadata and headers
        skip_patterns = [
            r'world english bible', r'public domain', r'copyright',
            r'ebible\.org', r'page \d+', r'generated using',
            book_name.lower() + r'\s+\d+:\d+\s+\d+',  # Skip "Tobit 1:1 511" type lines
            book_name.lower() + r'\s+is\s+recognized',
            r'deuterocanon', r'apocryph', r'translation note',
            r'^\d+$',  # Skip standalone numbers
            r'^[ivx]+$'  # Skip roman numerals
        ]
        
        if any(re.search(pattern, line, re.IGNORECASE) for pattern in skip_patterns):
            continue
        
        # Look for verse numbers
        verse_match = re.match(r'^(\d+):(\d+)\s*(.*)', line)
        if verse_match:
            current_chapter = int(verse_match.group(1))
            current_verse = int(verse_match.group(2))
            verse_text = verse_match.group(3)
            
            if verse_text and len(verse_text.strip()) > 3:
                cleaned_text = clean_and_fix_text(verse_text)
                if cleaned_text:
                    verses.append({
                        'chapter': current_chapter,
                        'verse': current_verse,
                        'text': cleaned_text
                    })
            continue
        
        # Look for chapter headers
        chapter_match = re.match(r'^(?:chapter\s+)?(\d+)$', line, re.IGNORECASE)
        if chapter_match:
            current_chapter = int(chapter_match.group(1))
            current_verse = 1
            continue
        
        # Look for verse text that starts with a number but no colon
        number_start = re.match(r'^(\d+)\s+(.+)', line)
        if number_start and len(number_start.group(2)) > 10:
            current_verse = int(number_start.group(1))
            verse_text = number_start.group(2)
            cleaned_text = clean_and_fix_text(verse_text)
            if cleaned_text:
                verses.append({
                    'chapter': current_chapter,
                    'verse': current_verse,
                    'text': cleaned_text
                })
            continue
        
        # If it's a substantial line that looks like verse content
        if len(line) > 15 and line[0].isupper() and not line.startswith(book_name):
            cleaned_text = clean_and_fix_text(line)
            if cleaned_text and not any(skip in cleaned_text.lower() for skip in ['page', 'world english', 'copyright']):
                verses.append({
                    'chapter': current_chapter,
                    'verse': current_verse,
                    'text': cleaned_text
                })
                current_verse += 1
    
    return verses

def create_html_file(verses, book_name, file_path):
    """Create HTML file from parsed verses"""
    html_content = f"<h1 class='et'>{book_name}</h1>\n<BR>\n"
    html_content += "<div id=\"contenten\" style=\"position:relative; top:0px; left:0px; overflow:auto\"><table cellpadding=0 cellspacing=0 border=0>\n"
    
    for verse in verses:
        html_content += f"<tr><td class=\"vn\">{verse['chapter']}:{verse['verse']}</td><td class=\"vn\">&nbsp;&nbsp;</td><td class=\"v en\">{verse['text']}</td></tr>\n"
    
    html_content += "</table></div>"
    
    # Write to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Created {file_path} with {len(verses)} verses")

def extract_all_deuterocanonical_books():
    """Extract all deuterocanonical books from PDF"""
    pdf_path = "/Users/suganolab/web/bibleweb/public/static/pdf/deuterocanonical/eng-web-c_all.pdf"
    output_dir = "/Users/suganolab/web/bibleweb/public/static/html/en"
    
    # Book page ranges based on table of contents
    books = {
        'tobit': {'start': 511, 'end': 521, 'name': 'Tobit'},
        'judith': {'start': 522, 'end': 538, 'name': 'Judith'},
        'wisdom': {'start': 773, 'end': 794, 'name': 'Wisdom'},
        'sirach': {'start': 795, 'end': 847, 'name': 'Sirach'},
        'baruch': {'start': 984, 'end': 991, 'name': 'Baruch'},
        '1maccabees': {'start': 551, 'end': 586, 'name': '1 Maccabees'},
        '2maccabees': {'start': 587, 'end': 614, 'name': '2 Maccabees'},
        'susanna': {'start': 1049, 'end': 1053, 'name': 'Susanna'}  # Approximate, within Daniel Greek
    }
    
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            
            for book_slug, book_info in books.items():
                print(f"Extracting {book_info['name']}...")
                
                # Extract text for this book
                book_text = extract_book_text(pdf_reader, book_info['start'], book_info['end'], book_info['name'])
                
                # Parse verses
                verses = parse_verses(book_text, book_info['name'])
                
                if verses:
                    # Create HTML file
                    html_file = os.path.join(output_dir, f"{book_slug}.htm")
                    create_html_file(verses, book_info['name'], html_file)
                else:
                    print(f"No verses found for {book_info['name']}")
                
    except Exception as e:
        print(f"Error extracting books: {e}")

if __name__ == "__main__":
    extract_all_deuterocanonical_books()