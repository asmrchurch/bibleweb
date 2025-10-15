import React, { useState, useEffect } from 'react';
import { useParams, useSearchParams } from 'react-router-dom';
import {
  TwitterShareButton,
  FacebookShareButton,
  EmailShareButton,
  RedditShareButton,
  LinkedinShareButton,
  XIcon,
  FacebookIcon,
  EmailIcon,
  RedditIcon,
  LinkedinIcon
} from 'react-share';
import Header from '../components/Header';
import Footer from '../components/Footer';
import PayComponent from '../components/PayComponent';
import ChapterNavigation from '../components/ChapterNavigation';
import ComingSoon from '../components/ComingSoon';

function Bible() {
  const { section } = useParams();
  const [searchParams, setSearchParams] = useSearchParams();
  const [content, setContent] = useState('');
  const [currentChapter, setCurrentChapter] = useState('');
  const [showComingSoon, setShowComingSoon] = useState(false);
  const [metaData, setMetaData] = useState({
    title: '',
    description: '',
    url: '',
    image: ''
  });
  const [sharePopup, setSharePopup] = useState({
    show: false,
    title: '',
    text: '',
    url: '',
    x: 0,
    y: 0
  });

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
    // Deuterocanonical books
    tobit: '3869678226',
    judith: '3869678226',
    wisdom: '3869678226',
    sirach: '3869678226',
    baruch: '3869678226',
    '1maccabees': '3869678226',
    '2maccabees': '3869678226',
    susanna: '3869678226',
  };

  // Japanese book names mapping
  const bookNamesJa = {
    genesis: '創世記',
    exodus: '出エジプト記',
    leviticus: 'レビ記',
    numbers: '民数記',
    deuteronomy: '申命記',
    joshua: 'ヨシュア記',
    judges: '士師記',
    ruth: 'ルツ記',
    '1samuel': 'サムエル記上',
    '2samuel': 'サムエル記下',
    '1kings': '列王記上',
    '2kings': '列王記下',
    '1chronicles': '歴代志上',
    '2chronicles': '歴代志下',
    ezra: 'エズラ記',
    nehemiah: 'ネヘミヤ記',
    esther: 'エステル記',
    job: 'ヨブ記',
    psalms: '詩篇',
    proverbs: '箴言',
    ecclesiastes: '伝道の書',
    songofsongs: '雅歌',
    isaiah: 'イザヤ書',
    jeremiah: 'エレミヤ書',
    lamentations: '哀歌',
    ezekiel: 'エゼキエル書',
    daniel: 'ダニエル書',
    hosea: 'ホセア書',
    joel: 'ヨエル書',
    amos: 'アモス書',
    obadiah: 'オバデヤ書',
    jonah: 'ヨナ書',
    micah: 'ミカ書',
    nahum: 'ナホム書',
    habakkuk: 'ハバクク書',
    zephaniah: 'ゼパニヤ書',
    haggai: 'ハガイ書',
    zechariah: 'ゼカリヤ書',
    malachi: 'マラキ書',
    matthew: 'マタイによる福音書',
    mark: 'マルコによる福音書',
    luke: 'ルカによる福音書',
    john: 'ヨハネによる福音書',
    acts: '使徒行伝',
    romans: 'ローマ人への手紙',
    '1corinthians': 'コリント人への第一の手紙',
    '2corinthians': 'コリント人への第二の手紙',
    galatians: 'ガラテヤ人への手紙',
    ephesians: 'エペソ人への手紙',
    philippians: 'ピリピ人への手紙',
    colossians: 'コロサイ人への手紙',
    '1thessalonians': 'テサロニケ人への第一の手紙',
    '2thessalonians': 'テサロニケ人への第二の手紙',
    '1timothy': 'テモテへの第一の手紙',
    '2timothy': 'テモテへの第二の手紙',
    titus: 'テトスへの手紙',
    philemon: 'ピレモンへの手紙',
    hebrews: 'ヘブル人への手紙',
    james: 'ヤコブの手紙',
    '1peter': 'ペテロの第一の手紙',
    '2peter': 'ペテロの第二の手紙',
    '1john': 'ヨハネの第一の手紙',
    '2john': 'ヨハネの第二の手紙',
    '3john': 'ヨハネの第三の手紙',
    jude: 'ユダの手紙',
    revelation: 'ヨハネの黙示録',
    // Deuterocanonical books
    tobit: 'トビト記',
    judith: 'ユディト記',
    wisdom: '知恵の書',
    sirach: 'シラ書',
    baruch: 'バルク書',
    '1maccabees': 'マカバイ記一',
    '2maccabees': 'マカバイ記二',
    susanna: 'スザンナ',
  };

  const album = sectionMap[section] || '3869678226';

  useEffect(() => {
    let type = searchParams.get('type');

    // List of deuterocanonical books that are currently missing
    const missingDeuterocanonicalBooks = [
      '2esdras', 'tobit', 'judith', 'esther-additions', 'wisdom', 'sirach', 'baruch',
      'letter-of-jeremiah', 'song-of-three', 'susanna', 'bel-and-dragon',
      'prayer-of-manasseh', '1maccabees', '2maccabees'
    ];

    // For all books, use existing logic to validate type
    if (!['norm', 'ruby', 'en'].includes(type)) {
      type = 'norm';
      setSearchParams({ type });
    }

    // Check if this is a missing deuterocanonical book
    if (missingDeuterocanonicalBooks.includes(section)) {
      setShowComingSoon(true);
      setContent('');
      return;
    }

    setShowComingSoon(false);
    fetch(`${process.env.PUBLIC_URL}/static/html/${type}/${section}.htm`)
      .then(response => response.text())
      .then(data => setContent(data))
      .catch(error => {
        console.error('Error loading the HTML content:', error);
        setShowComingSoon(true);
        setContent('');
      });
  }, [section, searchParams, setSearchParams]);

  // Update metadata based on URL hash (for specific verse)
  useEffect(() => {
    if (!content) return;

    const hash = window.location.hash.substring(1); // Remove '#'
    if (hash && hash.match(/^\d+-\d+$/)) {
      // Hash is a verse reference like "1-1"
      const verseElement = document.getElementById(hash);
      if (verseElement) {
        const nextElement = verseElement.nextElementSibling;
        if (nextElement) {
          const verseSpans = nextElement.querySelectorAll('span[id="verse"]');
          const verseText = verseSpans.length > 0
            ? verseSpans[verseSpans.length - 1].textContent.trim()
            : nextElement.textContent.trim();

          const bookNameJa = bookNamesJa[section] || section;
          const verseRef = `${bookNameJa} ${hash.replace('-', ':')}`;

          setMetaData({
            title: verseRef,
            description: verseText,
            url: `https://www.asmrchurch.com/bible/${section}#${hash}`,
            image: 'https://www.asmrchurch.com/static/images/card1.jpg'
          });

          return;
        }
      }
    }

    // Default metadata for the book
    const bookNameJa = bookNamesJa[section] || section;
    setMetaData({
      title: `${bookNameJa} - ASMRキリスト教会`,
      description: '口語訳聖書 旧約：1955年版・新約：1954年版',
      url: `https://www.asmrchurch.com/bible/${section}`,
      image: 'https://www.asmrchurch.com/static/images/card1.jpg'
    });
  }, [content, section, bookNamesJa]);

  // Add click handlers for verse sharing
  useEffect(() => {
    if (!content) return;

    const handleVerseClick = (e) => {
      // Check if clicked element is a verse link
      const link = e.target.closest('em[id] a[href^="#"]');
      if (!link) return;

      e.preventDefault();
      const verseId = link.parentElement.id; // e.g., "1-1"

      // Get the verse text
      const verseElement = link.parentElement.nextElementSibling;
      if (!verseElement) return;

      // Get the innermost span text (nested spans with id='verse')
      const verseSpans = verseElement.querySelectorAll('span[id="verse"]');
      const verseText = verseSpans.length > 0
        ? verseSpans[verseSpans.length - 1].textContent.trim()
        : verseElement.textContent.trim();

      // Get book name in Japanese
      const bookNameJa = bookNamesJa[section] || section;

      // Construct share text
      const shareTitle = `${bookNameJa} ${verseId.replace('-', ':')}`;
      const shareText = `${verseText} - ${shareTitle}`;
      const shareUrl = `${window.location.origin}/bible/${section}#${verseId}`;

      // Get click position for popup
      const rect = link.getBoundingClientRect();

      // Show share popup with X and Facebook buttons
      setSharePopup({
        show: true,
        title: shareTitle,
        text: shareText,
        url: shareUrl,
        x: rect.left + window.scrollX,
        y: rect.bottom + window.scrollY + 5
      });
    };

    // Add event listener to content div
    const contentDiv = document.querySelector('.content section');
    if (contentDiv) {
      contentDiv.addEventListener('click', handleVerseClick);
    }

    // Cleanup
    return () => {
      if (contentDiv) {
        contentDiv.removeEventListener('click', handleVerseClick);
      }
    };
  }, [content, section, bookNamesJa]);

  return (
    <div className="bibleframe">
      <Header
        bible={true}
        subon={true}
        title={metaData.title}
        description={metaData.description}
        url={metaData.url}
        image={metaData.image}
      />
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
            {showComingSoon ? (
              <ComingSoon bookName={section} />
            ) : (
              <div dangerouslySetInnerHTML={{ __html: content }} />
            )}
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

      {/* Share Popup */}
      {sharePopup.show && (
        <>
          <div
            style={{
              position: 'fixed',
              top: 0,
              left: 0,
              right: 0,
              bottom: 0,
              zIndex: 999
            }}
            onClick={() => setSharePopup({ ...sharePopup, show: false })}
          />
          <div
            style={{
              position: 'absolute',
              left: sharePopup.x,
              top: sharePopup.y,
              backgroundColor: 'white',
              border: '1px solid #ccc',
              borderRadius: '8px',
              padding: '12px',
              boxShadow: '0 2px 8px rgba(0,0,0,0.15)',
              zIndex: 1000,
              display: 'flex',
              gap: '8px',
              alignItems: 'center'
            }}
          >
            <span style={{ fontSize: '14px', marginRight: '8px' }}>布教する:</span>
            <TwitterShareButton url={sharePopup.url} title={sharePopup.text}>
              <XIcon size={32} round={false} />
            </TwitterShareButton>
            <FacebookShareButton url={sharePopup.url} quote={sharePopup.text}>
              <FacebookIcon size={32} round={false} />
            </FacebookShareButton>
            <EmailShareButton url={sharePopup.url} subject={sharePopup.title} body={sharePopup.text}>
              <EmailIcon size={32} round={false} />
            </EmailShareButton>
            <RedditShareButton url={sharePopup.url} title={sharePopup.text}>
              <RedditIcon size={32} round={false} />
            </RedditShareButton>
            <LinkedinShareButton url={sharePopup.url} title={sharePopup.title} summary={sharePopup.text}>
              <LinkedinIcon size={32} round={false} />
            </LinkedinShareButton>
          </div>
        </>
      )}

      <Footer />
    </div>
  );
}

export default Bible;
