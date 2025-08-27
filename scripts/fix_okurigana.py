#!/usr/bin/env python3
import re

def fix_okurigana():
    """送り仮名の相違を修正"""
    file_path = "/Users/suganolab/web/bibleweb/public/static/html/ruby/1esdras.htm"
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print(f"修正前のファイルサイズ: {len(content)} 文字")
        
        # 送り仮名の修正（ルビタグの後の部分を修正）
        replacements = [
            # 1:36 連去らせ → 連れ去らせ
            (r'</ruby>去らせ', '</ruby>れ去らせ'),
            # 1:41, 5:2 遣された → 遣わされた, 遣して → 遣わして  
            (r'</ruby>された', '</ruby>わされた'),
            (r'</ruby>して', '</ruby>わして'),
            # 1:46 連去り → 連れ去り
            (r'</ruby>去り', '</ruby>れ去り'),
            # 3:18 惑せる → 惑わせる
            (r'</ruby>せる', '</ruby>わせる'),
            # 4:26 惑されて → 惑わされて
            (r'</ruby>されて', '</ruby>わされて'),
            # 5:7 連て → 連れて
            (r'</ruby>て', '</ruby>れて')
        ]
        
        for i, (pattern, replacement) in enumerate(replacements):
            matches = len(re.findall(pattern, content))
            if matches > 0:
                content = re.sub(pattern, replacement, content)
                print(f"修正 {i+1}: {pattern} → {replacement} ({matches} 箇所)")
            else:
                print(f"修正 {i+1}: {pattern} (対象なし)")
        
        # より具体的な修正（コンテキストを含む）
        specific_fixes = [
            # 1:36節
            ('バビロンに<ruby><rb>連</rb><rp>(</rp><rt>つれ</rt><rp>)</rp></ruby>去らせ', 
             'バビロンに<ruby><rb>連</rb><rp>(</rp><rt>つれ</rt><rp>)</rp></ruby>れ去らせ'),
            # 1:41節  
            ('使者を<ruby><rb>遣</rb><rp>(</rp><rt>つかわ</rt><rp>)</rp></ruby>された', 
             '使者を<ruby><rb>遣</rb><rp>(</rp><rt>つかわ</rt><rp>)</rp></ruby>わされた'),
            # 1:46節
            ('バビロンに<ruby><rb>連</rb><rp>(</rp><rt>つれ</rt><rp>)</rp></ruby>去り', 
             'バビロンに<ruby><rb>連</rb><rp>(</rp><rt>つれ</rt><rp>)</rp></ruby>れ去り'),
            # 3:14節
            ('使者を<ruby><rb>遣</rb><rp>(</rp><rt>つかわ</rt><rp>)</rp></ruby>して', 
             '使者を<ruby><rb>遣</rb><rp>(</rp><rt>つかわ</rt><rp>)</rp></ruby>わして'),
            # 3:18節
            ('人を<ruby><rb>惑</rb><rp>(</rp><rt>まど</rt><rp>)</rp></ruby>せる', 
             '人を<ruby><rb>惑</rb><rp>(</rp><rt>まど</rt><rp>)</rp></ruby>わせる'),
            # 4:26節
            ('ために<ruby><rb>惑</rb><rp>(</rp><rt>まど</rt><rp>)</rp></ruby>されて', 
             'ために<ruby><rb>惑</rb><rp>(</rp><rt>まど</rt><rp>)</rp></ruby>わされて'),
            # 5:2節
            ('騎兵を<ruby><rb>遣</rb><rp>(</rp><rt>つかわ</rt><rp>)</rp></ruby>して', 
             '騎兵を<ruby><rb>遣</rb><rp>(</rp><rt>つかわ</rt><rp>)</rp></ruby>わして'),
            # 5:7節
            ('バビロンに<ruby><rb>連</rb><rp>(</rp><rt>つれ</rt><rp>)</rp></ruby>て来られ', 
             'バビロンに<ruby><rb>連</rb><rp>(</rp><rt>つれ</rt><rp>)</rp></ruby>れて来られ')
        ]
        
        print("\n=== 具体的な修正 ===")
        for i, (old, new) in enumerate(specific_fixes):
            if old in content:
                content = content.replace(old, new)
                print(f"具体的修正 {i+1}: ✅ 修正完了")
            else:
                print(f"具体的修正 {i+1}: ❌ 対象文字列が見つかりません")
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"\n修正後のファイルサイズ: {len(content)} 文字")
        print("✅ 送り仮名修正完了")
        
    except Exception as e:
        print(f"❌ エラー: {e}")

if __name__ == "__main__":
    fix_okurigana()