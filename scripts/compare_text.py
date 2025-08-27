#!/usr/bin/env python3
import re
import sys

def extract_text_content(html_file):
    """HTMLファイルから本文テキストを抽出（ルビタグを除去）"""
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"ファイル読み込みエラー: {e}")
        return None
    
    # rubyタグとその内容を除去（ルビ部分のみ削除、ベーステキストは残す）
    content = re.sub(r'<ruby><rb>([^<]+)</rb><rp>\([^)]*\)</rp><rt>[^<]*</rt><rp>\)[^)]*\)</rp></ruby>', r'\1', content)
    
    # 残ったルビの読み方部分も除去
    content = re.sub(r'\([^)]*\)', '', content)
    
    # HTMLタグを除去してテキストのみ抽出
    content = re.sub(r'<[^>]+>', '', content)
    
    # 空白や改行を正規化
    content = re.sub(r'\s+', ' ', content).strip()
    
    return content

def compare_files(file1, file2):
    """2つのファイルの本文内容を比較"""
    print("ファイル比較中...")
    
    text1 = extract_text_content(file1)
    text2 = extract_text_content(file2)
    
    if text1 is None or text2 is None:
        return
    
    if text1 == text2:
        print("✅ 両ファイルの本文内容は一致しています（ルビ除く）")
    else:
        print("❌ 本文内容に相違があります")
        
        # 詳細比較のために単語単位で分割
        words1 = text1.split()
        words2 = text2.split()
        
        print(f"ルビ版単語数: {len(words1)}")
        print(f"ノーマル版単語数: {len(words2)}")
        
        # 差分を検索
        min_len = min(len(words1), len(words2))
        differences = []
        
        for i in range(min_len):
            if words1[i] != words2[i]:
                differences.append((i, words1[i], words2[i]))
        
        if len(words1) != len(words2):
            differences.append(("length", len(words1), len(words2)))
        
        if differences:
            print("\n相違点:")
            for diff in differences[:10]:  # 最初の10個の相違点を表示
                if diff[0] == "length":
                    print(f"  長さが異なります: ルビ版 {diff[1]} words vs ノーマル版 {diff[2]} words")
                else:
                    print(f"  位置 {diff[0]}: ルビ版 '{diff[1]}' vs ノーマル版 '{diff[2]}'")

if __name__ == "__main__":
    ruby_file = "/Users/suganolab/web/bibleweb/public/static/html/ruby/1esdras.htm"
    norm_file = "/Users/suganolab/web/bibleweb/public/static/html/norm/1esdras.htm"
    
    compare_files(ruby_file, norm_file)