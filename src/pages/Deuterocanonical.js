import React from 'react';
import { Link } from 'react-router-dom';
import Header from '../components/Header';
import Footer from '../components/Footer';
import './main.css';

function Deuterocanonical() {
  const deuterocanonicalBooks = [
    { name: 'トビト書 (Tobit)', description: 'トビトと天使ラファエルの物語', slug: 'tobit' },
    { name: 'ユディト書 (Judith)', description: 'ユディトがホロフェルネスを倒す物語', slug: 'judith' },
    { name: '知恵の書 (Wisdom of Solomon)', description: 'ソロモンの知恵についての書', slug: 'wisdom' },
    { name: 'シラ書・集会の書 (Sirach/Ecclesiasticus)', description: '知恵文学の一つ', slug: 'sirach' },
    { name: 'バルク書 (Baruch)', description: 'エレミヤの弟子バルクの預言', slug: 'baruch' },
    { name: 'マカバイ記1 (1 Maccabees)', description: 'マカバイ家の反乱の歴史', slug: '1maccabees' },
    { name: 'マカバイ記2 (2 Maccabees)', description: 'マカバイ家の戦いの記録', slug: '2maccabees' },
    { name: 'スザンナ (Susanna)', description: 'ダニエル書の補遺の一部', slug: 'susanna' },
    { name: 'エステル記（ギリシア語版）(Esther Greek)', description: 'エステル記のギリシア語版（追加部分を含む）', slug: 'esther-greek' }
  ];

  const pdfFiles = [
    { name: 'World English Bible Catholic Edition - Letter Size', file: 'eng-web-c_all.pdf' },
    { name: 'World English Bible Catholic Edition - A4 Size', file: 'eng-web-c_a4.pdf' },
    { name: 'World English Bible Catholic Edition - Book Size', file: 'eng-web-c_book.pdf' },
    { name: 'World English Bible Catholic Edition - New Testament Only', file: 'eng-web-c_nt.pdf' }
  ];

  return (
    <div className="App">
      <Header />
      <main className="content">
        <h1>カトリック外典・第二正典 (Deuterocanonical Books)</h1>
        
        <section className="intro">
          <p>
            カトリック教会と正教会で正典として認められている書物です。
            プロテスタント教会では「外典」と呼ばれますが、カトリック教会では「第二正典」として扱われます。
          </p>
          <p>
            以下は、World English Bible Catholic Edition（著作権フリー）の英語訳です。
          </p>
        </section>

        <section className="books-list">
          <h2>第二正典に含まれる書物</h2>
          <ul>
            {deuterocanonicalBooks.map((book, index) => (
              <li key={index}>
                <strong>
                  <Link to={`/bible/${book.slug}`} className="book-link">
                    {book.name}
                  </Link>
                </strong>
                <p>{book.description}</p>
              </li>
            ))}
          </ul>
        </section>

        <section className="downloads">
          <h2>PDFダウンロード (World English Bible Catholic Edition)</h2>
          <p>完全に著作権フリーで、自由に使用・配布・印刷できます。</p>
          <ul className="pdf-list">
            {pdfFiles.map((pdf, index) => (
              <li key={index}>
                <a 
                  href={`/static/pdf/deuterocanonical/${pdf.file}`} 
                  download
                  className="download-link"
                >
                  📄 {pdf.name}
                </a>
              </li>
            ))}
          </ul>
        </section>

        <section className="copyright-info">
          <h2>著作権について</h2>
          <p>
            World English Bible (WEB) はパブリックドメイン（著作権なし）の現代英語訳聖書です。
            自由にコピー、印刷、配布、引用することができます。商用利用も可能で、使用料は不要です。
          </p>
        </section>
      </main>
      <Footer />
    </div>
  );
}

export default Deuterocanonical;