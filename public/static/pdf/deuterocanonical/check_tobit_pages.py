#!/usr/bin/env python3
import PyPDF2

def check_tobit_pages():
    """Check pages around 511 to find actual Tobit content"""
    pdf_path = "/Users/suganolab/web/bibleweb/public/static/pdf/deuterocanonical/eng-web-c_all.pdf"
    
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            
            # Check pages around 511 to find Tobit
            for page_num in range(509, 520):  # Check pages 510-519
                if page_num < len(pdf_reader.pages):
                    page = pdf_reader.pages[page_num]
                    text = page.extract_text()
                    
                    print(f"\n--- PAGE {page_num + 1} ---")
                    print(text[:500])  # First 500 characters
                    
                    if 'tobit' in text.lower():
                        print(f"*** FOUND TOBIT ON PAGE {page_num + 1} ***")
                        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_tobit_pages()