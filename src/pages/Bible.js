import React, { useState, useEffect } from 'react';
import { useParams, useSearchParams } from 'react-router-dom';
import Header from '../components/Header';
import Footer from '../components/Footer';
import PayComponent from '../components/PayComponent';
import ChapterNavigation from '../components/ChapterNavigation';

function Bible() {
  const { section } = useParams();
  const [searchParams, setSearchParams] = useSearchParams();
  const [content, setContent] = useState('');
  const [currentChapter, setCurrentChapter] = useState('');

  const sectionMap = {
    psalms: '3869678226',
    john: "3493586185",
    nahum: "2341997426",
    joel: "1554179965",
    haggai: "2264983860",
    luke: "3571744779",
    philippians: "160214243",
    titus: "4084456418",
    jonah: "3140582404",
    matthew: "3929365192",
    songofsongs: "1335264384",
    ecclesiastes: "3906097047",
    "2samuel": "4072766808",
    lamentations: "1475919099",
    leviticus: "2606473253",
    mark: "2251790182",
    zephaniah: "3193855292",
    numbers: "777940117",
    genesis: '1234567890',
    exodus: '9876543210',
  };

  const album = sectionMap[section] || '3869678226';

  useEffect(() => {
    let type = searchParams.get('type');

    if (!['norm', 'ruby', 'en'].includes(type)) {
      type = 'norm';
      setSearchParams({ type });
    }

    fetch(`${process.env.PUBLIC_URL}/static/html/${type}/${section}.htm`)
      .then(response => response.text())
      .then(data => setContent(data))
      .catch(error => console.error('Error loading the HTML content:', error));
  }, [section, searchParams, setSearchParams]); // Include setSearchParams as a dependency

  return (
    <div className="bibleframe">
      <Header bible={true} subon={true} />
      <ChapterNavigation 
        htmlContent={content} 
        currentChapter={currentChapter}
        onChapterClick={setCurrentChapter}
      />
      <div className="flex-container">
        <div className="left-area">
          <span className="pad">
      <stripe-buy-button
  buy-button-id="buy_btn_1QiEyXJrEFc0aoshZrg6uGA0"
  publishable-key="pk_live_51L77y9JrEFc0aoshDbT8faRDJBWQJjQTGvMb6jngK3GGGpMtIYf8omncPkMd8e0be0ZsfG2yEWaxYdMSlGSS9pgX00RNzmWvfw"
>
</stripe-buy-button>
          </span>
        </div>
    
        <div className="content">
          <section>
            <div dangerouslySetInnerHTML={{ __html: content }} />
          </section>
        </div>
    
        <div className="right-area">
          <span className="pad">
            <iframe
              style={{
                border: 0,
                width: '100%',
                height: '80%',
              }}
              src={`https://bandcamp.com/EmbeddedPlayer/album=${album}/size=large/bgcol=333333/linkcol=e99708/transparent=true/`}
              seamless
            >
              <a href="https://asmrchruch.bandcamp.com/album/asmr-32"></a>
            </iframe>
          </span>
        </div>
      </div>
      <Footer />
    </div>
  );
}

export default Bible;
