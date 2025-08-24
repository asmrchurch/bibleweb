import React from 'react';
import './ComingSoon.css';

function ComingSoon({ bookName }) {
  const bookDisplayNames = {
    '1esdras': 'エズラ第一書 (1 Esdras)',
    '2esdras': 'エズラ第二書 (2 Esdras)',
    'tobit': 'トビト書 (Tobit)',
    'judith': 'ユデト書 (Judith)',
    'esther-additions': 'エステル書殘篇 (Additions to Esther)',
    'wisdom': 'ソロモンの智慧 (Wisdom of Solomon)',
    'sirach': 'ベン・シラの智慧 (Sirach/Ecclesiasticus)',
    'baruch': 'バルク書 (Baruch)',
    'letter-of-jeremiah': 'エレミヤの書翰 (Letter of Jeremiah)',
    'song-of-three': '三童兒の歌 (Song of the Three Young Men)',
    'susanna': 'スザンナ物語 (Susanna)',
    'bel-and-dragon': 'ベルと龍 (Bel and the Dragon)',
    'prayer-of-manasseh': 'マナセの祈禱 (Prayer of Manasseh)',
    '1maccabees': 'マカビー第一書 (1 Maccabees)',
    '2maccabees': 'マカビー第二書 (2 Maccabees)'
  };

  const displayName = bookDisplayNames[bookName] || bookName;

  return (
    <div className="coming-soon-container">
      <div className="coming-soon-content">
        <h2>{displayName}</h2>
        <p className="coming-soon-message">Coming soon...</p>
        <p className="coming-soon-description">
          このコンテンツは現在準備中です。<br />
          近日公開予定ですので、しばらくお待ちください。
        </p>
      </div>
    </div>
  );
}

export default ComingSoon;