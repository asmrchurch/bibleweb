#!/usr/bin/env python3

def fix_remaining():
    """残りの相違点を修正"""
    file_path = "/Users/suganolab/web/bibleweb/public/static/html/ruby/1esdras.htm"
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 残りの修正
        remaining_fixes = [
            # 1:26 終り → 終わり
            ('その<ruby><rb>初</rb><rp>(</rp><rt>はじ</rt><rp>)</rp></ruby>めと<ruby><rb>終</rb><rp>(</rp><rt>おわ</rt><rp>)</rp></ruby>り、見よ',
             'その<ruby><rb>初</rb><rp>(</rp><rt>はじ</rt><rp>)</rp></ruby>めと<ruby><rb>終</rb><rp>(</rp><rt>おわ</rt><rp>)</rp></ruby>わり、見よ'),
            # 1:36 遣して → 遣わして
            ('人を<ruby><rb>遣</rb><rp>(</rp><rt>つかわ</rt><rp>)</rp></ruby>して彼を',
             '人を<ruby><rb>遣</rb><rp>(</rp><rt>つかわ</rt><rp>)</rp></ruby>わして彼を'),
            # 1:41 憐んで → 憐れんで, 遣された → 遣わされた
            ('を<ruby><rb>憐</rb><rp>(</rp><rt>あわれ</rt><rp>)</rp></ruby>んで、使者を<ruby><rb>遣</rb><rp>(</rp><rt>つかわ</rt><rp>)</rp></ruby>された',
             'を<ruby><rb>憐</rb><rp>(</rp><rt>あわれ</rt><rp>)</rp></ruby>れんで、使者を<ruby><rb>遣</rb><rp>(</rp><rt>つかわ</rt><rp>)</rp></ruby>わされた'),
            # 3:14 遣して → 遣わして
            ('使者を<ruby><rb>遣</rb><rp>(</rp><rt>つかわ</rt><rp>)</rp></ruby>してペルシア',
             '使者を<ruby><rb>遣</rb><rp>(</rp><rt>つかわ</rt><rp>)</rp></ruby>わしてペルシア'),
            # 3:18 惑せる → 惑わせる
            ('人を<ruby><rb>惑</rb><rp>(</rp><rt>まど</rt><rp>)</rp></ruby>せる。',
             '人を<ruby><rb>惑</rb><rp>(</rp><rt>まど</rt><rp>)</rp></ruby>わせる。'),
            # 4:26 惑されて → 惑わされて
            ('ために<ruby><rb>惑</rb><rp>(</rp><rt>まど</rt><rp>)</rp></ruby>されて',
             'ために<ruby><rb>惑</rb><rp>(</rp><rt>まど</rt><rp>)</rp></ruby>わされて'),
            # 5:1 連て → 連れて
            ('などを<ruby><rb>連</rb><rp>(</rp><rt>つれ</rt><rp>)</rp></ruby>て出発',
             'などを<ruby><rb>連</rb><rp>(</rp><rt>つれ</rt><rp>)</rp></ruby>れて出発'),
            # 5:2 遣して → 遣わして
            ('騎兵を<ruby><rb>遣</rb><rp>(</rp><rt>つかわ</rt><rp>)</rp></ruby>して、',
             '騎兵を<ruby><rb>遣</rb><rp>(</rp><rt>つかわ</rt><rp>)</rp></ruby>わして、'),
            # 5:7 連て → 連れて
            ('バビロンに<ruby><rb>連</rb><rp>(</rp><rt>つれ</rt><rp>)</rp></ruby>て来られ',
             'バビロンに<ruby><rb>連</rb><rp>(</rp><rt>つれ</rt><rp>)</rp></ruby>れて来られ')
        ]
        
        fixed_count = 0
        for old, new in remaining_fixes:
            if old in content:
                content = content.replace(old, new)
                fixed_count += 1
                print(f"✓ {old[:30]}... → ...{new[-30:]}")
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"\n残り修正完了: {fixed_count} 箇所")
        
    except Exception as e:
        print(f"エラー: {e}")

if __name__ == "__main__":
    fix_remaining()