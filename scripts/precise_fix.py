#!/usr/bin/env python3
import re

def precise_fix():
    """正確な送り仮名の修正のみ実行"""
    file_path = "/Users/suganolab/web/bibleweb/public/static/html/ruby/1esdras.htm"
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print("正確な送り仮名の修正を実行中...")
        
        # 前回修正した「モーセに」の追加
        if 'モーセに<ruby><rb>与</rb><rp>(</rp><rt>あた</rt><rp>)</rp></ruby>えられた主の<ruby><rb>戒</rb><rp>(</rp><rt>いまし</rt><rp>)</rp></ruby>め' in content:
            print("✓ 「モーセに」は既に修正済み")
        else:
            content = content.replace(
                '<ruby><rb>与</rb><rp>(</rp><rt>あた</rt><rp>)</rp></ruby>えられた主の<ruby><rb>戒</rb><rp>(</rp><rt>いまし</rt><rp>)</rp></ruby>め',
                'モーセに<ruby><rb>与</rb><rp>(</rp><rt>あた</rt><rp>)</rp></ruby>えられた主の<ruby><rb>戒</rb><rp>(</rp><rt>いまし</rt><rp>)</rp></ruby>め'
            )
            print("✓ 「モーセに」を追加")
        
        # 正確な8箇所の送り仮名修正
        specific_replacements = [
            # 1:5 基いて → 基づいて
            ('<ruby><rb>基</rb><rp>(</rp><rt>もとづ</rt><rp>)</rp></ruby>いて', 
             '<ruby><rb>基</rb><rp>(</rp><rt>もとづ</rt><rp>)</rp></ruby>づいて'),
            # 1:21 遣して → 遣わして
            ('人を<ruby><rb>遣</rb><rp>(</rp><rt>つかわ</rt><rp>)</rp></ruby>して言わせた',
             '人を<ruby><rb>遣</rb><rp>(</rp><rt>つかわ</rt><rp>)</rp></ruby>わして言わせた'),
            # 1:26 終り → 終わり
            ('<ruby><rb>終</rb><rp>(</rp><rt>おわ</rt><rp>)</rp></ruby>り、見よ',
             '<ruby><rb>終</rb><rp>(</rp><rt>おわ</rt><rp>)</rp></ruby>わり、見よ'),
            # 1:30 連去った → 連れ去った
            ('エジプトに<ruby><rb>連</rb><rp>(</rp><rt>つれ</rt><rp>)</rp></ruby>去った。',
             'エジプトに<ruby><rb>連</rb><rp>(</rp><rt>つれ</rt><rp>)</rp></ruby>れ去った。'),
            # 1:32 連去った → 連れ去った  
            ('バビロンに<ruby><rb>連</rb><rp>(</rp><rt>つれ</rt><rp>)</rp></ruby>去った。',
             'バビロンに<ruby><rb>連</rb><rp>(</rp><rt>つれ</rt><rp>)</rp></ruby>れ去った。'),
            # 1:36 連去らせ → 連れ去らせ
            ('バビロンに<ruby><rb>連</rb><rp>(</rp><rt>つれ</rt><rp>)</rp></ruby>去らせ、',
             'バビロンに<ruby><rb>連</rb><rp>(</rp><rt>つれ</rt><rp>)</rp></ruby>れ去らせ、'),
            # 1:41 憐んで → 憐れんで, 遣された → 遣わされた
            ('を<ruby><rb>憐</rb><rp>(</rp><rt>あわれ</rt><rp>)</rp></ruby>んで、使者を<ruby><rb>遣</rb><rp>(</rp><rt>つかわ</rt><rp>)</rp></ruby>された',
             'を<ruby><rb>憐</rb><rp>(</rp><rt>あわれ</rt><rp>)</rp></ruby>れんで、使者を<ruby><rb>遣</rb><rp>(</rp><rt>つかわ</rt><rp>)</rp></ruby>わされた'),
            # 1:43 憐まなかった → 憐れまなかった
            ('も<ruby><rb>憐</rb><rp>(</rp><rt>あわれ</rt><rp>)</rp></ruby>まなかった',
             'も<ruby><rb>憐</rb><rp>(</rp><rt>あわれ</rt><rp>)</rp></ruby>れまなかった'),
            # 1:46 連去り → 連れ去り
            ('バビロンに<ruby><rb>連</rb><rp>(</rp><rt>つれ</rt><rp>)</rp></ruby>去り、',
             'バビロンに<ruby><rb>連</rb><rp>(</rp><rt>つれ</rt><rp>)</rp></ruby>れ去り、'),
            # 3:14 遣して → 遣わして
            ('使者を<ruby><rb>遣</rb><rp>(</rp><rt>つかわ</rt><rp>)</rp></ruby>してペルシアと',
             '使者を<ruby><rb>遣</rb><rp>(</rp><rt>つかわ</rt><rp>)</rp></ruby>わしてペルシアと'),
            # 3:18 惑せる → 惑わせる
            ('人を<ruby><rb>惑</rb><rp>(</rp><rt>まど</rt><rp>)</rp></ruby>せる。',
             '人を<ruby><rb>惑</rb><rp>(</rp><rt>まど</rt><rp>)</rp></ruby>わせる。'),
            # 4:26 惑されて → 惑わされて
            ('ために<ruby><rb>惑</rb><rp>(</rp><rt>まど</rt><rp>)</rp></ruby>されて',
             'ために<ruby><rb>惑</rb><rp>(</rp><rt>まど</rt><rp>)</rp></ruby>わされて'),
            # 5:2 遣して → 遣わして
            ('騎兵を<ruby><rb>遣</rb><rp>(</rp><rt>つかわ</rt><rp>)</rp></ruby>して、彼らが',
             '騎兵を<ruby><rb>遣</rb><rp>(</rp><rt>つかわ</rt><rp>)</rp></ruby>わして、彼らが'),
            # 5:7 連て → 連れて
            ('バビロンに<ruby><rb>連</rb><rp>(</rp><rt>つれ</rt><rp>)</rp></ruby>て来られ',
             'バビロンに<ruby><rb>連</rb><rp>(</rp><rt>つれ</rt><rp>)</rp></ruby>れて来られ')
        ]
        
        fixed_count = 0
        for old, new in specific_replacements:
            if old in content:
                content = content.replace(old, new)
                fixed_count += 1
                print(f"✓ 修正: {old[:20]}...")
        
        print(f"\n修正完了: {fixed_count} 箇所")
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ 正確な修正完了")
        
    except Exception as e:
        print(f"❌ エラー: {e}")

if __name__ == "__main__":
    precise_fix()