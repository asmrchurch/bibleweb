#!/usr/bin/env python3
import re

def fix_ruby_file():
    """ルビ版ファイルの相違点を修正"""
    file_path = "/Users/suganolab/web/bibleweb/public/static/html/ruby/1esdras.htm"
    
    # 修正対象のパターンと置換文字列
    replacements = [
        (r'<ruby><rb>基</rb><rp>\(</rp><rt>もとづ</rt><rp>\)</rp></ruby>いて', r'<ruby><rb>基</rb><rp>(</rp><rt>もとづ</rt><rp>)</rp></ruby>づいて'),
        (r'人を<ruby><rb>遣</rb><rp>\(</rp><rt>つかわ</rt><rp>\)</rp></ruby>して', r'人を<ruby><rb>遣</rb><rp>(</rp><rt>つかわ</rt><rp>)</rp></ruby>わして'),
        (r'使者を<ruby><rb>遣</rb><rp>\(</rp><rt>つかわ</rt><rp>\)</rp></ruby>して', r'使者を<ruby><rb>遣</rb><rp>(</rp><rt>つかわ</rt><rp>)</rp></ruby>わして'),
        (r'その<ruby><rb>初</rb><rp>\(</rp><rt>はじ</rt><rp>\)</rp></ruby>めと<ruby><rb>終</rb><rp>\(</rp><rt>おわ</rt><rp>\)</rp></ruby>り', r'その<ruby><rb>初</rb><rp>(</rp><rt>はじ</rt><rp>)</rp></ruby>めと<ruby><rb>終</rb><rp>(</rp><rt>おわ</rt><rp>)</rp></ruby>わり'),
        (r'に<ruby><rb>連</rb><rp>\(</rp><rt>つれ</rt><rp>\)</rp></ruby>去った', r'に<ruby><rb>連</rb><rp>(</rp><rt>つれ</rt><rp>)</rp></ruby>れ去った'),
        (r'を<ruby><rb>連</rb><rp>\(</rp><rt>つれ</rt><rp>\)</rp></ruby>去らせ', r'を<ruby><rb>連</rb><rp>(</rp><rt>つれ</rt><rp>)</rp></ruby>れ去らせ'),
        (r'は<ruby><rb>連</rb><rp>\(</rp><rt>つれ</rt><rp>\)</rp></ruby>去り', r'は<ruby><rb>連</rb><rp>(</rp><rt>つれ</rt><rp>)</rp></ruby>れ去り'),
        (r'を<ruby><rb>憐</rb><rp>\(</rp><rt>あわれ</rt><rp>\)</rp></ruby>んで', r'を<ruby><rb>憐</rb><rp>(</rp><rt>あわれ</rt><rp>)</rp></ruby>れんで'),
        (r'使者を<ruby><rb>遣</rb><rp>\(</rp><rt>つかわ</rt><rp>\)</rp></ruby>された', r'使者を<ruby><rb>遣</rb><rp>(</rp><rt>つかわ</rt><rp>)</rp></ruby>わされた'),
        (r'も<ruby><rb>憐</rb><rp>\(</rp><rt>あわれ</rt><rp>\)</rp></ruby>まなかった', r'も<ruby><rb>憐</rb><rp>(</rp><rt>あわれ</rt><rp>)</rp></ruby>れまなかった'),
        # 追加の修正
        (r'彼を<ruby><rb>連</rb><rp>\(</rp><rt>つれ</rt><rp>\)</rp></ruby>去らせ', r'彼を<ruby><rb>連</rb><rp>(</rp><rt>つれ</rt><rp>)</rp></ruby>れ去らせ'),
        (r'使者を<ruby><rb>遣</rb><rp>\(</rp><rt>つかわ</rt><rp>\)</rp></ruby>された', r'使者を<ruby><rb>遣</rb><rp>(</rp><rt>つかわ</rt><rp>)</rp></ruby>わされた'),
        (r'を<ruby><rb>連</rb><rp>\(</rp><rt>つれ</rt><rp>\)</rp></ruby>去り', r'を<ruby><rb>連</rb><rp>(</rp><rt>つれ</rt><rp>)</rp></ruby>れ去り'),
        (r'彼は<ruby><rb>使者</rb><rp>\(</rp><rt>ししゃ</rt><rp>\)</rp></ruby>を<ruby><rb>遣</rb><rp>\(</rp><rt>つかわ</rt><rp>\)</rp></ruby>して', r'彼は<ruby><rb>使者</rb><rp>(</rp><rt>ししゃ</rt><rp>)</rp></ruby>を<ruby><rb>遣</rb><rp>(</rp><rt>つかわ</rt><rp>)</rp></ruby>わして'),
        (r'人を<ruby><rb>惑</rb><rp>\(</rp><rt>まど</rt><rp>\)</rp></ruby>せる', r'人を<ruby><rb>惑</rb><rp>(</rp><rt>まど</rt><rp>)</rp></ruby>わせる'),
        (r'ために<ruby><rb>惑</rb><rp>\(</rp><rt>まど</rt><rp>\)</rp></ruby>されて', r'ために<ruby><rb>惑</rb><rp>(</rp><rt>まど</rt><rp>)</rp></ruby>わされて'),
        (r'などを<ruby><rb>連</rb><rp>\(</rp><rt>つれ</rt><rp>\)</rp></ruby>て', r'などを<ruby><rb>連</rb><rp>(</rp><rt>つれ</rt><rp>)</rp></ruby>れて'),
        (r'騎兵を<ruby><rb>遣</rb><rp>\(</rp><rt>つかわ</rt><rp>\)</rp></ruby>して', r'騎兵を<ruby><rb>遣</rb><rp>(</rp><rt>つかわ</rt><rp>)</rp></ruby>わして'),
        (r'に<ruby><rb>連</rb><rp>\(</rp><rt>つれ</rt><rp>\)</rp></ruby>て来られ', r'に<ruby><rb>連</rb><rp>(</rp><rt>つれ</rt><rp>)</rp></ruby>れて来られ')
    ]
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print(f"元のファイルサイズ: {len(content)} 文字")
        
        # 各置換を実行
        for i, (pattern, replacement) in enumerate(replacements):
            matches = len(re.findall(pattern, content))
            content = re.sub(pattern, replacement, content)
            print(f"置換 {i+1}: {matches} 箇所修正")
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ 修正完了")
        
    except Exception as e:
        print(f"❌ エラー: {e}")

if __name__ == "__main__":
    fix_ruby_file()