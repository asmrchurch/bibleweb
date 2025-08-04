#!/usr/bin/env python3
import PyPDF2
import re
import os

def clean_text(text):
    """Clean and fix spacing issues in extracted text"""
    # Remove extra whitespace and newlines
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Fix common spacing issues around punctuation
    text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)  # Add space between lowercase and uppercase
    text = re.sub(r'(\w),(\w)', r'\1, \2', text)  # Add space after comma
    text = re.sub(r'(\w)\.(\w)', r'\1. \2', text)  # Add space after period
    text = re.sub(r'(\w);(\w)', r'\1; \2', text)  # Add space after semicolon
    text = re.sub(r'(\w):(\w)', r'\1: \2', text)  # Add space after colon
    text = re.sub(r'(\w)\?(\w)', r'\1? \2', text)  # Add space after question mark
    text = re.sub(r'(\w)!(\w)', r'\1! \2', text)  # Add space after exclamation
    
    # Fix specific word concatenations
    text = re.sub(r'ofthe', 'of the', text)
    text = re.sub(r'tothe', 'to the', text)
    text = re.sub(r'inthe', 'in the', text)
    text = re.sub(r'onthe', 'on the', text)
    text = re.sub(r'atthe', 'at the', text)
    text = re.sub(r'forthe', 'for the', text)
    text = re.sub(r'bythe', 'by the', text)
    text = re.sub(r'withthe', 'with the', text)
    text = re.sub(r'fromthe', 'from the', text)
    text = re.sub(r'andthe', 'and the', text)
    text = re.sub(r'allthe', 'all the', text)
    text = re.sub(r'andI', 'and I', text)
    text = re.sub(r'thatI', 'that I', text)
    text = re.sub(r'whenI', 'when I', text)
    text = re.sub(r'ifI', 'if I', text)
    text = re.sub(r'asI', 'as I', text)
    text = re.sub(r'soI', 'so I', text)
    text = re.sub(r'butI', 'but I', text)
    text = re.sub(r'theson', 'the son', text)
    text = re.sub(r'myfather', 'my father', text)
    text = re.sub(r'mymother', 'my mother', text)
    text = re.sub(r'myGod', 'my God', text)
    text = re.sub(r'mypeople', 'my people', text)
    text = re.sub(r'mykindred', 'my kindred', text)
    text = re.sub(r'mynation', 'my nation', text)
    text = re.sub(r'mylife', 'my life', text)
    text = re.sub(r'myown', 'my own', text)
    text = re.sub(r'myheart', 'my heart', text)
    text = re.sub(r'myhands', 'my hands', text)
    text = re.sub(r'myfeet', 'my feet', text)
    text = re.sub(r'myeyes', 'my eyes', text)
    text = re.sub(r'hisson', 'his son', text)
    text = re.sub(r'hisfather', 'his father', text)
    text = re.sub(r'hismother', 'his mother', text)
    text = re.sub(r'hisheart', 'his heart', text)
    text = re.sub(r'hishands', 'his hands', text)
    text = re.sub(r'hishouse', 'his house', text)
    text = re.sub(r'hisway', 'his way', text)
    text = re.sub(r'hisname', 'his name', text)
    
    # Fix double spaces
    text = re.sub(r'\s+', ' ', text)
    
    return text

def extract_verses_from_text(text, book_name):
    """Extract verses from text and identify actual scripture content"""
    lines = text.split('\n')
    verses = []
    current_chapter = 1
    current_verse = 1
    
    # Look for patterns that indicate verse numbers
    verse_pattern = r'^(\d+):(\d+)'
    chapter_pattern = r'^Chapter\s+(\d+)'
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Skip headers, page numbers, and metadata
        if any(skip in line.lower() for skip in [
            'world english bible', 'public domain', 'copyright', 
            'ebible.org', 'page', book_name.lower() + ' is recognized',
            'deuterocanon', 'apocryph', 'translation note'
        ]):
            continue
            
        # Check for chapter headers
        chapter_match = re.match(chapter_pattern, line)
        if chapter_match:
            current_chapter = int(chapter_match.group(1))
            current_verse = 1
            continue
            
        # Check for verse numbers at start of line
        verse_match = re.match(verse_pattern, line)
        if verse_match:
            current_chapter = int(verse_match.group(1))
            current_verse = int(verse_match.group(2))
            # Remove the verse number from the beginning
            verse_text = re.sub(verse_pattern, '', line).strip()
            if verse_text:
                verses.append({
                    'chapter': current_chapter,
                    'verse': current_verse,
                    'text': clean_text(verse_text)
                })
            continue
        
        # If line contains scripture-like content (not metadata)
        if len(line) > 10 and not line.isdigit() and ':' not in line[:5]:
            # This might be continuation of a verse or a verse without number prefix
            if line[0].isupper() or any(c.isalpha() for c in line[:5]):
                verses.append({
                    'chapter': current_chapter,
                    'verse': current_verse,
                    'text': clean_text(line)
                })
                current_verse += 1
    
    return verses

def extract_deuterocanonical_books():
    """Extract text from deuterocanonical books PDF"""
    pdf_path = "/Users/suganolab/web/bibleweb/public/static/pdf/deuterocanonical/eng-web-c_all.pdf"
    
    # Book information with approximate page ranges (need to be determined by examining PDF)
    books = {
        'tobit': {'start_page': 0, 'name': 'Tobit'},
        'judith': {'start_page': 20, 'name': 'Judith'}, 
        'wisdom': {'start_page': 40, 'name': 'Wisdom'},
        'sirach': {'start_page': 60, 'name': 'Sirach'},
        'baruch': {'start_page': 120, 'name': 'Baruch'},
        '1maccabees': {'start_page': 130, 'name': '1 Maccabees'},
        '2maccabees': {'start_page': 180, 'name': '2 Maccabees'},
        'susanna': {'start_page': 220, 'name': 'Susanna'}
    }
    
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            total_pages = len(pdf_reader.pages)
            print(f"Total pages in PDF: {total_pages}")
            
            # First, let's extract all text and find where each book starts
            all_text = ""
            for page_num in range(min(50, total_pages)):  # Check first 50 pages to identify structure
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                all_text += f"\n--- PAGE {page_num + 1} ---\n" + text
            
            # Save the raw text for analysis
            with open('/Users/suganolab/web/bibleweb/public/static/pdf/deuterocanonical/raw_text_sample.txt', 'w', encoding='utf-8') as f:
                f.write(all_text)
                
            print("Raw text sample saved. Please check the structure to identify book boundaries.")
            
    except Exception as e:
        print(f"Error extracting text: {e}")

if __name__ == "__main__":
    extract_deuterocanonical_books()