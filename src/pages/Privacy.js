import React from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';
import { Helmet } from 'react-helmet';
import './styles.css';
import './main.css';

function Privacy() {
  return (
    <div className="body">
      <Helmet>
        <title>プライバシーポリシー - ASMRキリスト教会</title>
        <meta name="description" content="ASMRキリスト教会のプライバシーポリシーについて" />
      </Helmet>
      
      <Header subon={true} />
      
      <div className="container">
        <div style={{ padding: '20px', maxWidth: '800px', margin: '0 auto' }}>
          <h1>プライバシーポリシー</h1>
          
          <h2>1. 個人情報の取り扱いについて</h2>
          <p>
            ASMRキリスト教会（以下「当サイト」）では、ユーザーの個人情報を適切に保護することを重要な責務と考えております。
            本プライバシーポリシーでは、当サイトがどのような個人情報を取得し、どのように利用・管理するかについて説明いたします。
          </p>
          
          <h2>2. 収集する情報</h2>
          <p>当サイトでは、以下の情報を収集する場合があります：</p>
          <ul>
            <li>アクセスログ（IPアドレス、ブラウザ情報、アクセス日時など）</li>
            <li>Cookie及び類似技術による情報</li>
            <li>お問い合わせ時に提供いただく情報</li>
          </ul>
          
          <h2>3. 情報の利用目的</h2>
          <p>収集した情報は以下の目的で利用いたします：</p>
          <ul>
            <li>サイトの運営・管理</li>
            <li>サービスの改善・向上</li>
            <li>お問い合わせへの対応</li>
            <li>統計データの作成（個人を特定できない形式）</li>
          </ul>
          
          <h2>4. 第三者への提供</h2>
          <p>
            当サイトは、法令に基づく場合を除き、ユーザーの同意なく個人情報を第三者に提供することはありません。
          </p>
          
          <h2>5. 広告について</h2>
          <p>
            当サイトでは、Google AdSenseを利用した広告を表示しています。
            これらの広告配信事業者は、ユーザーの興味に応じた商品やサービスの広告を表示するため、
            Cookieを使用することがあります。
          </p>
          
          <h2>6. アクセス解析ツール</h2>
          <p>
            当サイトでは、Googleによるアクセス解析ツール「Googleアナリティクス」を利用しています。
            このGoogleアナリティクスはトラフィックデータの収集のためにCookieを使用しています。
          </p>
          
          <h2>7. Cookieについて</h2>
          <p>
            Cookieとは、Webサイトがユーザーのコンピュータに送信する小さなテキストファイルです。
            ブラウザの設定でCookieを無効にすることも可能ですが、
            その場合サイトの一部機能が利用できなくなる可能性があります。
          </p>
          
          <h2>8. プライバシーポリシーの変更</h2>
          <p>
            当サイトは、必要に応じて本プライバシーポリシーを変更することがあります。
            変更後のプライバシーポリシーは、当サイトに掲載した時点から効力を生じるものとします。
          </p>
          
          <h2>9. お問い合わせ</h2>
          <p>
            本プライバシーポリシーに関するお問い合わせは、当サイトのお問い合わせフォームよりご連絡ください。
          </p>
          
          <p style={{ marginTop: '40px', fontSize: '14px', color: '#666' }}>
            制定日：2025年6月17日<br />
            ASMRキリスト教会
          </p>
        </div>
      </div>
      
      <Footer />
    </div>
  );
}

export default Privacy;