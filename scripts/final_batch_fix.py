#!/usr/bin/env python3

def final_batch_fix():
    file_path = "/Users/suganolab/web/bibleweb/public/static/html/ruby/1esdras.htm"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 残りの8箇所を一括修正
    fixes = [
        ('憐</ruby>んで、<ruby><rb>使者</rb><rp>(</rp><rt>ししゃ</rt><rp>)</rp></ruby>を<ruby><rb>遣</rb><rp>(</rp><rt>つかわ</rt><rp>)</rp></ruby>された', 
         '憐</ruby>れんで、<ruby><rb>使者</rb><rp>(</rp><rt>ししゃ</rt><rp>)</rp></ruby>を<ruby><rb>遣</rb><rp>(</rp><rt>つかわ</rt><rp>)</rp></ruby>わされた'),
        ('遣</ruby>してペルシア', '遣</ruby>わしてペルシア'),
        ('惑</ruby>せる。', '惑</ruby>わせる。'),
        ('惑</ruby>されて', '惑</ruby>わされて'),
        ('連</ruby>て出発', '連</ruby>れて出発'),
        ('遣</ruby>して、彼らが', '遣</ruby>わして、彼らが'),
        ('連</ruby>て来られ', '連</ruby>れて来られ')
    ]
    
    for old, new in fixes:
        if old in content:
            content = content.replace(old, new)
            print(f"✓ {old} → {new}")
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ 最終修正完了")

if __name__ == "__main__":
    final_batch_fix()