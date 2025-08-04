#!/usr/bin/env python3
import PyPDF2
import re

def check_and_extract_tobit():
    """Extract only Tobit for testing - check page by page"""
    pdf_path = "/Users/suganolab/web/bibleweb/public/static/pdf/deuterocanonical/eng-web-c_all.pdf"
    
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            
            # Check pages 515-525 where we found Tobit
            for page_num in range(514, 525):  # PDF pages 515-525
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                
                print(f"\n=== PAGE {page_num + 1} ===")
                print(text[:800])  # Show more text
                
                # Look for actual verse structure
                lines = text.split('\n')
                for line_num, line in enumerate(lines):
                    if 'Tobit' in line and ('1:1' in line or 'book of' in line.lower()):
                        print(f"\n*** FOUND TOBIT START AT LINE {line_num}: {line} ***")
                        
                        # Show context around this line
                        start_idx = max(0, line_num - 2)
                        end_idx = min(len(lines), line_num + 10)
                        print("\nCONTEXT:")
                        for i in range(start_idx, end_idx):
                            print(f"{i}: {lines[i]}")
                        break
                        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_and_extract_tobit()