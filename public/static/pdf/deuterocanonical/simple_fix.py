#!/usr/bin/env python3
import re
import os

def fix_spacing_in_html(content):
    """Fix common spacing issues in HTML content"""
    
    # Define common word concatenations to fix
    fixes = [
        (r'\bofthe\b', 'of the'),
        (r'\binthe\b', 'in the'),
        (r'\btothe\b', 'to the'),
        (r'\bandthe\b', 'and the'),
        (r'\bwiththe\b', 'with the'),
        (r'\boutof\b', 'out of'),
        (r'\bintotheland\b', 'into the land'),
        (r'\ballthedays\b', 'all the days'),
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
        (r'\bIam\b', 'I am'),
        (r'\bIdid\b', 'I did'),
        (r'\bIdo\b', 'I do'),
        (r'\bIwill\b', 'I will'),
        (r'\bIhave\b', 'I have'),
        (r'\bIhad\b', 'I had'),
        (r'\bIcan\b', 'I can'),
        (r'\bIwent\b', 'I went'),
        (r'\bIcame\b', 'I came'),
        (r'\bIsaw\b', 'I saw'),
        (r'\bIsaid\b', 'I said'),
        (r'\bItold\b', 'I told'),
        (r'\bIheard\b', 'I heard'),
        (r'\bIfound\b', 'I found'),
        (r'\bItook\b', 'I took'),
        (r'\bIgave\b', 'I gave'),
        (r'\bImade\b', 'I made'),
        (r'\bIknow\b', 'I know'),
        (r'\bIknew\b', 'I knew'),
        (r'\bIlook\b', 'I look'),
        (r'\bIlooked\b', 'I looked'),
        (r'\bIsee\b', 'I see'),
        (r'\bwhen I\b', 'when I'),
        (r'\bthat I\b', 'that I'),
        (r'\bif I\b', 'if I'),
        (r'\bas I\b', 'as I'),
        (r'\bwhile I\b', 'while I'),
        (r'\bwhen he\b', 'when he'),
        (r'\bthat he\b', 'that he'),
        (r'\bif he\b', 'if he'),
        (r'\bas he\b', 'as he'),
        (r'\bwhile he\b', 'while he'),
        (r'\btome\b', 'to me'),
        (r'\bfrom me\b', 'from me'),
        (r'\bwith me\b', 'with me'),
        (r'\bmeinto\b', 'me into'),
        (r'\bhiminto\b', 'him into'),
        (r'\bthatit\b', 'that it'),
        (r'\bwhichit\b', 'which it'),
        (r'\bwhereit\b', 'where it'),
        (r'\bwhen it\b', 'when it'),
        (r'\bhow it\b', 'how it'),
        (r'\bwhat it\b', 'what it'),
        (r'\byetyoung\b', 'yet young'),
        (r'\bwho went\b', 'who went'),
        (r'\bwho came\b', 'who came'),
        (r'\bwho was\b', 'who was'),
        (r'\bwho were\b', 'who were'),
        (r'\bwho had\b', 'who had'),
        (r'\bwho have\b', 'who have'),
        (r'\bwho will\b', 'who will'),
        (r'\bwho would\b', 'who would'),
        (r'\bwho could\b', 'who could'),
        (r'\bwho should\b', 'who should'),
        (r'\bwho might\b', 'who might'),
        (r'\bwho must\b', 'who must'),
        (r'\bsonofa\b', 'son of a'),
        (r'\bsonof\b', 'son of'),
        (r'\bdaughterof\b', 'daughter of'),
        (r'\bkingof\b', 'king of'),
        (r'\blordof\b', 'lord of'),
        (r'\bgodof\b', 'god of'),
        (r'\blandof\b', 'land of'),
        (r'\bcityof\b', 'city of'),
        (r'\bhouseof\b', 'house of'),
        (r'\btribeof\b', 'tribe of'),
        (r'\bpeopleof\b', 'people of'),
        (r'\bchildrenof\b', 'children of'),
        (r'\bsonsof\b', 'sons of'),
        (r'\bdaughtersof\b', 'daughters of'),
        (r'\bmena\b', 'men a'),
        (r'\bwomena\b', 'women a'),
        (r'\bchilda\b', 'child a'),
        (r'\bmana\b', 'man a'),
        (r'\bwomana\b', 'woman a'),
        (r'\bkinga\b', 'king a'),
        (r'\bqueena\b', 'queen a'),
        (r'\bprincaa\b', 'prince a'),
        (r'\bprincess\b', 'princess a'),
        (r'\bpriest\b', 'priest a'),
        (r'\bpropheta\b', 'prophet a'),
        (r'\bangela\b', 'angel a'),
        (r'\bservanta\b', 'servant a'),
        (r'\bslavel\b', 'slave a'),
        (r'\bsoldi\b', 'soldier a'),
        (r'\bwarri\b', 'warrior a'),
        (r'\bthat\b', 'that a'),
        (r'\bthis\b', 'this a'),
        (r'\bthese\b', 'these a'),
        (r'\bthose\b', 'those a'),
        (r'\banother\b', 'another a'),
        (r'\bother\b', 'other a'),
        (r'\beveryo\b', 'every o'),
        (r'\beacha\b', 'each a'),
        (r'\bsomea\b', 'some a'),
        (r'\bmanya\b', 'many a'),
        (r'\bfewa\b', 'few a'),
        (r'\bseverala\b', 'several a'),
        (r'\bavarious\b', 'a various'),
        (r'\banumber\b', 'a number'),
        (r'\bamajority\b', 'a majority'),
        (r'\baminority\b', 'a minority'),
        (r'\bagroup\b', 'a group'),
        (r'\banassembly\b', 'an assembly'),
        (r'\bacrowd\b', 'a crowd'),
        (r'\bamultitude\b', 'a multitude'),
        (r'\banarray\b', 'an array'),
        (r'\bavariey\b', 'a variety'),
        (r'\baselection\b', 'a selection'),
        (r'\bacollection\b', 'a collection'),
        (r'\banassortment\b', 'an assortment'),
        (r'\bamixture\b', 'a mixture'),
        (r'\bacombination\b', 'a combination'),
        (r'\bablend\b', 'a blend'),
        (r'\bamix\b', 'a mix'),
    ]
    
    # Apply fixes
    for pattern, replacement in fixes:
        content = re.sub(pattern, replacement, content)
    
    return content

def process_file(file_path):
    """Process a single HTML file to fix spacing"""
    print(f"Processing {file_path}...")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Apply spacing fixes
        fixed_content = fix_spacing_in_html(content)
        
        # Write back the fixed content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(fixed_content)
        
        print(f"Fixed spacing in {file_path}")
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def main():
    # List of deuterocanonical files to fix
    deutero_files = [
        '../html/en/tobit.htm',
        '../html/en/judith.htm', 
        '../html/en/wisdom.htm',
        '../html/en/sirach.htm',
        '../html/en/baruch.htm',
        '../html/en/1maccabees.htm',
        '../html/en/2maccabees.htm',
        '../html/en/susanna.htm'
    ]
    
    for file_path in deutero_files:
        if os.path.exists(file_path):
            process_file(file_path)
        else:
            print(f"File not found: {file_path}")

if __name__ == "__main__":
    main()