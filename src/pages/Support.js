import React from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';
import { Helmet } from 'react-helmet';
import './styles.css';
import './main.css';

function Support() {
  return (
    <div className="body">
      <Helmet>
        <title>サポートページ - ASMRキリスト教会</title>
        <meta name="description" content="口語訳聖書アプリのサポートページ。FAQ、プライバシーポリシー、お問い合わせ情報をご確認いただけます。" />
      </Helmet>
      
      <Header subon={true} />
      
      <div className="container">
        <div style={{ padding: '20px', maxWidth: '800px', margin: '0 auto' }}>
          <h1>口語訳聖書（ASMRキリスト教会）</h1>
          <p style={{ textAlign: 'center', marginBottom: '40px', fontSize: '18px' }}>
            日本語聖書アプリケーション - サポートページ
          </p>
          
          <section style={{ marginBottom: '40px' }}>
            <h2>アプリについて</h2>
            <p>
              「口語訳聖書（ASMRキリスト教会）」は、日本語の口語訳聖書を手軽に読むことができるモバイルアプリケーションです。
              検索機能やブックマーク機能を搭載し、いつでもどこでも聖書を読むことができます。
            </p>
            
            <h3 style={{ marginTop: '20px', marginBottom: '15px' }}>主な機能</h3>
            <ul style={{ listStyleType: 'none', paddingLeft: '0' }}>
              <li style={{ padding: '8px 0', paddingLeft: '25px', position: 'relative' }}>
                <span style={{ position: 'absolute', left: '0', color: '#FFD700', fontWeight: 'bold' }}>✓</span>
                口語訳聖書全文の閲覧
              </li>
              <li style={{ padding: '8px 0', paddingLeft: '25px', position: 'relative' }}>
                <span style={{ position: 'absolute', left: '0', color: '#FFD700', fontWeight: 'bold' }}>✓</span>
                キーワード検索機能
              </li>
              <li style={{ padding: '8px 0', paddingLeft: '25px', position: 'relative' }}>
                <span style={{ position: 'absolute', left: '0', color: '#FFD700', fontWeight: 'bold' }}>✓</span>
                ブックマーク機能
              </li>
              <li style={{ padding: '8px 0', paddingLeft: '25px', position: 'relative' }}>
                <span style={{ position: 'absolute', left: '0', color: '#FFD700', fontWeight: 'bold' }}>✓</span>
                読みやすいインターフェース
              </li>
              <li style={{ padding: '8px 0', paddingLeft: '25px', position: 'relative' }}>
                <span style={{ position: 'absolute', left: '0', color: '#FFD700', fontWeight: 'bold' }}>✓</span>
                オフラインでの使用可能
              </li>
            </ul>
          </section>
          
          <section style={{ marginBottom: '40px' }}>
            <h2>よくある質問（FAQ）</h2>
            
            <div style={{ marginBottom: '20px', padding: '15px', backgroundColor: '#1a1a1a', borderRadius: '5px', border: '1px solid #444' }}>
              <h3 style={{ color: '#FFD700', marginBottom: '10px', fontSize: '1.1em' }}>Q: アプリは無料ですか？</h3>
              <p>A: はい、このアプリは完全無料でご利用いただけます。広告も表示されません。</p>
            </div>
            
            <div style={{ marginBottom: '20px', padding: '15px', backgroundColor: '#1a1a1a', borderRadius: '5px', border: '1px solid #444' }}>
              <h3 style={{ color: '#FFD700', marginBottom: '10px', fontSize: '1.1em' }}>Q: インターネット接続は必要ですか？</h3>
              <p>A: いいえ、一度ダウンロードすれば、インターネット接続なしでも聖書を読むことができます。</p>
            </div>
            
            <div style={{ marginBottom: '20px', padding: '15px', backgroundColor: '#1a1a1a', borderRadius: '5px', border: '1px solid #444' }}>
              <h3 style={{ color: '#FFD700', marginBottom: '10px', fontSize: '1.1em' }}>Q: ブックマークしたものはどこに保存されますか？</h3>
              <p>A: ブックマークはお使いのデバイス内に保存されます。アプリを削除すると、ブックマークも削除されますのでご注意ください。</p>
            </div>
            
            <div style={{ marginBottom: '20px', padding: '15px', backgroundColor: '#1a1a1a', borderRadius: '5px', border: '1px solid #444' }}>
              <h3 style={{ color: '#FFD700', marginBottom: '10px', fontSize: '1.1em' }}>Q: 検索機能の使い方を教えてください。</h3>
              <p>A: アプリ内の検索アイコンをタップし、探したい言葉を入力してください。聖書全体から該当する箇所が表示されます。</p>
            </div>
            
            <div style={{ marginBottom: '20px', padding: '15px', backgroundColor: '#1a1a1a', borderRadius: '5px', border: '1px solid #444' }}>
              <h3 style={{ color: '#FFD700', marginBottom: '10px', fontSize: '1.1em' }}>Q: 文字サイズは変更できますか？</h3>
              <p>A: 現在のバージョンでは、デバイスの設定に従った文字サイズで表示されます。</p>
            </div>
          </section>
          
          <section style={{ marginBottom: '40px' }}>
            <h2>プライバシーポリシー</h2>
            <div style={{ lineHeight: '1.8' }}>
              <p>ASMRキリスト教会（以下、「当会」）は、口語訳聖書アプリ（以下、「本アプリ」）におけるユーザーの個人情報の取り扱いについて、以下のとおりプライバシーポリシーを定めます。</p>
              
              <h3 style={{ marginTop: '20px', marginBottom: '10px', color: '#FFD700' }}>1. 個人情報の収集</h3>
              <p>本アプリは、ユーザーの個人情報を一切収集しません。アプリの使用に際して、氏名、メールアドレス、位置情報などの個人を特定できる情報の入力や送信は不要です。</p>
              
              <h3 style={{ marginTop: '20px', marginBottom: '10px', color: '#FFD700' }}>2. データの保存</h3>
              <p>ブックマーク機能で保存されるデータは、すべてユーザーのデバイス内にのみ保存されます。当会のサーバーには一切送信されません。</p>
              
              <h3 style={{ marginTop: '20px', marginBottom: '10px', color: '#FFD700' }}>3. 第三者への提供</h3>
              <p>本アプリは個人情報を収集しないため、第三者への提供も行いません。</p>
              
              <h3 style={{ marginTop: '20px', marginBottom: '10px', color: '#FFD700' }}>4. データの安全管理</h3>
              <p>本アプリで扱うデータは、すべてユーザーのデバイス内で管理されます。デバイスのセキュリティは、ユーザー自身で適切に管理してください。</p>
              
              <h3 style={{ marginTop: '20px', marginBottom: '10px', color: '#FFD700' }}>5. お問い合わせ</h3>
              <p>プライバシーポリシーに関するお問い合わせは、下記のサポートメールアドレスまでご連絡ください。</p>
              
              <p style={{ marginTop: '20px' }}><small>最終更新日：2025年1月18日</small></p>
            </div>
          </section>
          
          <section style={{ marginBottom: '40px' }}>
            <h2>お問い合わせ</h2>
            <p>アプリに関するご質問、ご要望、不具合の報告などは、下記のメールアドレスまでお気軽にお問い合わせください。</p>
            
            <div style={{ 
              backgroundColor: '#1a1a1a', 
              padding: '20px', 
              borderRadius: '5px', 
              textAlign: 'center', 
              marginTop: '20px',
              border: '2px solid #FFD700'
            }}>
              <p><strong>サポートメール：</strong></p>
              <p>
                <a 
                  href="mailto:kei@sugano.works" 
                  style={{ color: '#FFD700', textDecoration: 'none', fontWeight: 'bold' }}
                  onMouseOver={(e) => e.target.style.color = '#00FFFF'}
                  onMouseOut={(e) => e.target.style.color = '#FFD700'}
                >
                  kei@sugano.works
                </a>
              </p>
            </div>
            
            <p style={{ marginTop: '20px' }}>※ お返事には数日かかる場合がございます。あらかじめご了承ください。</p>
          </section>
        </div>
      </div>
      
      <Footer />
    </div>
  );
}

export default Support;