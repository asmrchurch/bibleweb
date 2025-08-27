#!/usr/bin/env python3
import re

def final_fix():
    file_path = "/Users/suganolab/web/bibleweb/public/static/html/ruby/1esdras.htm"
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 送り仮名の修正
        fixes = [
            ('連去らせ', '連れ去らせ'),
            ('連去り', '連れ去り'),
            ('連て', '連れて'),
            ('遣して', '遣わして'),
            ('遣された', '遣わされた'),
            ('惑せる', '惑わせる'),
            ('惑されて', '惑わされて')
        ]
        
        for old, new in fixes:
            count = content.count(old)
            content = content.replace(old, new)
            print(f"'{old}' → '{new}': {count} 箇所")
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ 最終修正完了")
    except Exception as e:
        print(f"エラー: {e}")

if __name__ == "__main__":
    final_fix()