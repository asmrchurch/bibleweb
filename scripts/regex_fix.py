#!/usr/bin/env python3
import re

def regex_fix():
    file_path = "/Users/suganolab/web/bibleweb/public/static/html/ruby/1esdras.htm"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 正規表現で正確に修正
    patterns = [
        # 1:41 憐んで → 憐れんで, 遣された → 遣わされた  
        (r'<ruby><rb>憐</rb><rp>\(</rp><rt>あわれ</rt><rp>\)</rp></ruby>んで、<ruby><rb>使者</rb><rp>\(</rp><rt>ししゃ</rt><rp>\)</rp></ruby>を<ruby><rb>遣</rb><rp>\(</rp><rt>つかわ</rt><rp>\)</rp></ruby>された',
         r'<ruby><rb>憐</rb><rp>(</rp><rt>あわれ</rt><rp>)</rp></ruby>れんで、<ruby><rb>使者</rb><rp>(</rp><rt>ししゃ</rt><rp>)</rp></ruby>を<ruby><rb>遣</rb><rp>(</rp><rt>つかわ</rt><rp>)</rp></ruby>わされた'),
        # 3:14 遣して → 遣わして
        (r'<ruby><rb>使者</rb><rp>\(</rp><rt>ししゃ</rt><rp>\)</rp></ruby>を<ruby><rb>遣</rb><rp>\(</rp><rt>つかわ</rt><rp>\)</rp></ruby>してペルシア',
         r'<ruby><rb>使者</rb><rp>(</rp><rt>ししゃ</rt><rp>)</rp></ruby>を<ruby><rb>遣</rb><rp>(</rp><rt>つかわ</rt><rp>)</rp></ruby>わしてペルシア'),
        # 3:18 惑せる → 惑わせる
        (r'<ruby><rb>人</rb><rp>\(</rp><rt>ひと</rt><rp>\)</rp></ruby>を<ruby><rb>惑</rb><rp>\(</rp><rt>まど</rt><rp>\)</rp></ruby>せる。',
         r'<ruby><rb>人</rb><rp>(</rp><rt>ひと</rt><rp>)</rp></ruby>を<ruby><rb>惑</rb><rp>(</rp><rt>まど</rt><rp>)</rp></ruby>わせる。'),
        # 4:26 惑されて → 惑わされて
        (r'ために<ruby><rb>惑</rb><rp>\(</rp><rt>まど</rt><rp>\)</rp></ruby>されて',
         r'ために<ruby><rb>惑</rb><rp>(</rp><rt>まど</rt><rp>)</rp></ruby>わされて'),
        # 5:1 連て → 連れて
        (r'などを<ruby><rb>連</rb><rp>\(</rp><rt>つれ</rt><rp>\)</rp></ruby>て<ruby><rb>出発</rb>',
         r'などを<ruby><rb>連</rb><rp>(</rp><rt>つれ</rt><rp>)</rp></ruby>れて<ruby><rb>出発</rb>'),
        # 5:2 遣して → 遣わして  
        (r'<ruby><rb>騎兵</rb><rp>\(</rp><rt>きへい</rt><rp>\)</rp></ruby>を<ruby><rb>遣</rb><rp>\(</rp><rt>つかわ</rt><rp>\)</rp></ruby>して',
         r'<ruby><rb>騎兵</rb><rp>(</rp><rt>きへい</rt><rp>)</rp></ruby>を<ruby><rb>遣</rb><rp>(</rp><rt>つかわ</rt><rp>)</rp></ruby>わして'),
        # 5:7 連て → 連れて
        (r'バビロンに<ruby><rb>連</rb><rp>\(</rp><rt>つれ</rt><rp>\)</rp></ruby>て<ruby><rb>来</rb>',
         r'バビロンに<ruby><rb>連</rb><rp>(</rp><rt>つれ</rt><rp>)</rp></ruby>れて<ruby><rb>来</rb>')
    ]
    
    for pattern, replacement in patterns:
        matches = len(re.findall(pattern, content))
        if matches > 0:
            content = re.sub(pattern, replacement, content)
            print(f"✓ {matches} 箇所修正")
        else:
            print(f"❌ パターンが見つからない")
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ 正規表現修正完了")

if __name__ == "__main__":
    regex_fix()