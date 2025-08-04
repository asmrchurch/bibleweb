#!/usr/bin/env python3
import PyPDF2
import re

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

def search_books(text):
    """Search for deuterocanonical books"""
    lines = text.split('\n')
    
    search_terms = [
        'Maccabees', 'First Book of the Maccabees', 'Second Book of the Maccabees',
        'Bel and the Dragon', 'Prayer of Azariah', 'Song of the Three Young Men',
        'Additions to Esther', 'Additions to Daniel'
    ]
    
    for term in search_terms:
        print(f"\nSearching for '{term}':")
        matches = []
        
        for i, line in enumerate(lines):
            if term.lower() in line.lower():
                matches.append((i, line.strip()))
        
        if matches:
            print(f"Found {len(matches)} matches:")
            for line_num, line_text in matches[:10]:  # Show first 10 matches
                print(f"  Line {line_num}: {line_text}")
        else:
            print("Not found")

def main():
    pdf_path = "eng-web-c_all.pdf"
    
    print("Extracting text from PDF...")
    full_text = extract_pdf_text(pdf_path)
    
    if full_text:
        search_books(full_text)
    else:
        print("Failed to extract text from PDF")

if __name__ == "__main__":
    main()