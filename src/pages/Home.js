import React, { useState, useEffect } from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';
import BibleList from '../components/BibleList';
import PayComponent from '../components/PayComponent';
import Ad from '../components/Ad';
import './styles.css';
import './main.css';
import { Helmet } from 'react-helmet';
import { useSearchParams } from 'react-router-dom';

function Home() {
  const [searchParams, setSearchParams] = useSearchParams();
  const [type, setType] = useState('ja');
  const [oldTitle, setOldTitle] = useState('旧約聖書');
  const [newTitle, setNewTitle] = useState('新約聖書');
  const [deuteroTitle, setDeuteroTitle] = useState('外典');

  useEffect(() => {
    let urlType = searchParams.get('type') || 'norm';
    if (!['norm', 'en'].includes(urlType)) {
      urlType = 'norm';
      setSearchParams({ type: 'norm' });
    }

    setType(urlType);

    // Update titles based on type
    setOldTitle(urlType === 'en' ? 'The Old Testament' : '旧約聖書');
    setNewTitle(urlType === 'en' ? 'The New Testament' : '新約聖書');
    setDeuteroTitle(urlType === 'en' ? 'Deuterocanonical Books' : '外典');
  }, [searchParams, setSearchParams]);

  return (
    <div className="body">
      <Header subon={true} />
      <div className="container">
        <BibleList
          title={oldTitle}
          type={type}
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
          title={newTitle}
          type={type}
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
        <BibleList
          title={deuteroTitle}
          type={type}
          books={[
            ['tobit', 'トビト書'],
            ['judith', 'ユディト書'],
            ['wisdom', '知恵の書'], 
            ['sirach', 'シラ書'],
            ['baruch', 'バルク書'],
            ['1maccabees', 'マカバイ記第一'],
            ['2maccabees', 'マカバイ記第二'],
            ['susanna', 'スザンナ']
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
