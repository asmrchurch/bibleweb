import React from 'react';
import MainHeader from '../components/MainHeader';
import Footer from '../components/Footer';
import BibleList from '../components/BibleList';
import Ad from '../components/Ad';
import './styles.css';
import './main.css';

function Home() {
  return (
    <div className="body">
      <MainHeader />
      <div className="container">
        <BibleList
          title="旧約聖書"
          books={[
            ['genesis', '創世記'],
            ['exodus', '出エジプト記'],
            ['leviticus', 'レビ記'],
            ['numbers', '民数記'],
            ['deuteronomy', '申命記'],
            ['joshua', 'ヨシュア記'],
            ['judges', '士師記'],
            ['ruth', 'ルツ記'],
            ['1samuel', 'サムエル記 第一'],
            ['2samuel', 'サムエル記 第二'],
            ['1kings', '列王記 第一'],
            ['2kings', '列王記 第二'],
            ['1chronicles', '歴代誌 第一'],
            ['2chronicles', '歴代誌 第二'],
            ['ezra', 'エズラ記'],
            ['nehemiah', 'ネヘミヤ記'],
            ['esther', 'エステル記'],
            ['job', 'ヨブ記'],
            ['psalms', '詩篇'],
            ['proverbs', '箴言'],
            ['ecclesiastes', '伝道の書'],
            ['songofsongs', '雅歌'],
            ['isaiah', 'イザヤ書'],
            ['jeremiah', 'エレミヤ書'],
            ['lamentations', '哀歌'],
            ['ezekiel', 'エゼキエル書'],
            ['daniel', 'ダニエル書'],
            ['hosea', 'ホセア書'],
            ['joel', 'ヨエル書'],
            ['amos', 'アモス書'],
            ['obadiah', 'オバデヤ書'],
            ['jonah', 'ヨナ書'],
            ['micah', 'ミカ書'],
            ['nahum', 'ナホム書'],
            ['habakkuk', 'ハバクク書'],
            ['zephaniah', 'ゼパニヤ書'],
            ['haggai', 'ハガイ書'],
            ['zecariah', 'ゼカリヤ書'],
            ['malachi', 'マラキ書']
          ]}
        />
        <br/>
        <BibleList
          title="新約聖書"
          books={[
            ['matthew', 'マタイによる福音書'],
            ['mark', 'マルコによる福音書'],
            ['luke', 'ルカによる福音書'],
            ['john', 'ヨハネによる福音書'],
            ['acts', '使徒行伝'],
            ['romans', 'ローマ人への手紙'],
            ['1corinthians', 'コリント人への第一の手紙'],
            ['2corinthians', 'コリント人への第二の手紙'],
            ['galatians', 'ガラテヤ人への手紙'],
            ['ephesians', 'エペソ人への手紙'],
            ['philippians', 'ピリピ人への手紙'],
            ['colossians', 'コロサイ人への手紙'],
            ['1thessalonians', 'テサロニケ人への第一の手紙'],
            ['2thessalonians', 'テサロニケ人への第二の手紙'],
            ['1timothy', 'テモテへの第一の手紙'],
            ['2timothy', 'テモテへの第二の手紙'],
            ['titus', 'テトスへの手紙'],
            ['philemon', 'ピレモンへの手紙'],
            ['hebrews', 'ヘブル人への手紙'],
            ['james', 'ヤコブの手紙'],
            ['1peter', 'ペテロの第一の手紙'],
            ['2peter', 'ペテロの第二の手紙'],
            ['1john', 'ヨハネの第一の手紙'],
            ['2john', 'ヨハネの第二の手紙'],
            ['3john', 'ヨハネの第三の手紙'],
            ['jude', 'ユダの手紙'],
            ['revelation', 'ヨハネの黙示録']
          ]}
        />
        <br/>
        <Ad />
      </div>
      <Footer />
    </div>
  );
}

export default Home;
