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
        (r'havebeen', 'have been'), (r'willbe', 'will be'), (r'shallbe', 'shall be'),
        (r'don\'t', 'don\'t'), (r'didn\'t', 'didn\'t'), (r'won\'t', 'won\'t'),
        (r'can\'t', 'can\'t'), (r'haven\'t', 'haven\'t'), (r'isn\'t', 'isn\'t')
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

def parse_verses_from_pages(pdf_reader, start_page, end_page, book_name):
    """Extract and parse verses from specific PDF pages"""
    verses = []
    current_chapter = 1
    current_verse = 1
    
    for page_num in range(start_page - 1, min(end_page, len(pdf_reader.pages))):
        page = pdf_reader.pages[page_num]
        text = page.extract_text()
        lines = text.split('\n')
        
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
                r'^[ivx]+$',  # Skip roman numerals
                r'catholic', r'orthodox', r'churches'
            ]
            
            if any(re.search(pattern, line, re.IGNORECASE) for pattern in skip_patterns):
                continue
            
            # Look for verse numbers
            verse_match = re.match(r'^(\d+):(\d+)\s*(.*)', line)
            if verse_match:
                current_chapter = int(verse_match.group(1))
                current_verse = int(verse_match.group(2))
                verse_text = verse_match.group(3).strip()
                
                if verse_text and len(verse_text) > 3:
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
            
            # Look for numbered verse text (number at start)
            number_start = re.match(r'^(\d+)\s+(.+)', line)
            if number_start and len(number_start.group(2)) > 10:
                verse_num = int(number_start.group(1))
                if verse_num < 100:  # Reasonable verse number
                    current_verse = verse_num
                    verse_text = number_start.group(2)
                    cleaned_text = clean_and_fix_text(verse_text)
                    if cleaned_text and not any(skip in cleaned_text.lower() for skip in ['page', 'world english', 'copyright']):
                        verses.append({
                            'chapter': current_chapter,
                            'verse': current_verse,
                            'text': cleaned_text
                        })
                continue
            
            # If it's substantial verse-like content (starts with capital, reasonable length)
            if (len(line) > 15 and line[0].isupper() and 
                not line.startswith(book_name) and
                not any(skip in line.lower() for skip in ['page', 'world english', 'copyright', 'deuterocanon'])):
                
                cleaned_text = clean_and_fix_text(line)
                if cleaned_text:
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

def extract_all_books():
    """Extract all deuterocanonical books with correct PDF page numbers"""
    pdf_path = "/Users/suganolab/web/bibleweb/public/static/pdf/deuterocanonical/eng-web-c_all.pdf"
    output_dir = "/Users/suganolab/web/bibleweb/public/static/html/en"
    
    # Correct PDF page ranges (PDF pages, not book page numbers)
    books = {
        'tobit': {'start': 515, 'end': 525, 'name': 'Tobit'},
        'judith': {'start': 526, 'end': 545, 'name': 'Judith'},
        'wisdom': {'start': 778, 'end': 800, 'name': 'Wisdom'},
        'sirach': {'start': 800, 'end': 855, 'name': 'Sirach'},
        'baruch': {'start': 990, 'end': 998, 'name': 'Baruch'},
        '1maccabees': {'start': 555, 'end': 592, 'name': '1 Maccabees'},
        '2maccabees': {'start': 592, 'end': 620, 'name': '2 Maccabees'},
        'susanna': {'start': 1055, 'end': 1058, 'name': 'Susanna'}
    }
    
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            
            for book_slug, book_info in books.items():
                print(f"Extracting {book_info['name']} from pages {book_info['start']}-{book_info['end']}...")
                
                # Extract and parse verses
                verses = parse_verses_from_pages(pdf_reader, book_info['start'], book_info['end'], book_info['name'])
                
                if verses:
                    # Create HTML file
                    html_file = os.path.join(output_dir, f"{book_slug}.htm")
                    create_html_file(verses, book_info['name'], html_file)
                    
                    # Also copy to server directory if it exists
                    server_dir = "/Users/suganolab/web/bible/public/static/html/en"
                    if os.path.exists(os.path.dirname(server_dir)):
                        server_file = os.path.join(server_dir, f"{book_slug}.htm")
                        create_html_file(verses, book_info['name'], server_file)
                        print(f"Also copied to {server_file}")
                else:
                    print(f"No verses found for {book_info['name']}")
                
    except Exception as e:
        print(f"Error extracting books: {e}")

if __name__ == "__main__":
    extract_all_books()