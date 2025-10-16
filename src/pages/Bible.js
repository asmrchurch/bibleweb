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
import { AdIcons } from '../components/Ad';

// Custom Blogger Share Button
const BloggerShareButton = ({ url, title, text, image, children }) => {
  // Clean text: remove HTML tags and markdown syntax
  let cleanText = text || '';

  // Remove HTML tags
  cleanText = cleanText.replace(/<[^>]*>/g, '');

  // Remove markdown image syntax
  cleanText = cleanText.replace(/!\[.*?\]\(.*?\)/g, '');

  // Remove markdown headers
  cleanText = cleanText.replace(/^#{1,6}\s+/gm, '');

  // Remove markdown bold/italic
  cleanText = cleanText.replace(/[*_]{1,2}([^*_]+)[*_]{1,2}/g, '$1');

  // Remove markdown links but keep text
  cleanText = cleanText.replace(/\[([^\]]+)\]\([^)]+\)/g, '$1');

  // Normalize whitespace
  cleanText = cleanText.replace(/\s+/g, ' ').trim();

  // Truncate to 1000 chars to avoid URL length issues
  const truncatedText = cleanText.length > 1000 ? cleanText.substring(0, 997) + '...' : cleanText;

  // Build HTML content: image + text + link at bottom
  const imageTag = image ? `<img src="${image}" alt="${title}" style="max-width:100%;height:auto;"><br><br>` : '';
  const content = `${imageTag}${truncatedText}<br><br><a href="${url}">${url}</a>`;

  const bloggerUrl = `https://www.blogger.com/blog-this.g?u=${encodeURIComponent(url)}&n=${encodeURIComponent(title)}&t=${encodeURIComponent(content)}`;

  return (
    <a
      href={bloggerUrl}
      target="_blank"
      rel="noopener noreferrer"
      style={{ display: 'inline-block', cursor: 'pointer' }}
    >
      {children}
    </a>
  );
};

// Custom Blogger Icon
const BloggerIcon = ({ size = 32 }) => (
  <svg
    viewBox="0 0 24 24"
    width={size}
    height={size}
    style={{ display: 'block' }}
  >
    <rect width="24" height="24" fill="#FF5722" />
    <path
      d="M10.5 9h3c.28 0 .5.22.5.5s-.22.5-.5.5h-3c-.28 0-.5-.22-.5-.5s.22-.5.5-.5zm0 5h3c.28 0 .5.22.5.5s-.22.5-.5.5h-3c-.28 0-.5-.22-.5-.5s.22-.5.5-.5zm6.5-7h-2.5V5c0-1.1-.9-2-2-2h-4C7.9 3 7 3.9 7 5v4c0 1.1.9 2 2 2v1c0 1.1.9 2 2 2v3c0 1.1.9 2 2 2h4c1.1 0 2-.9 2-2V9c0-1.1-.9-2-2-2z"
      fill="white"
    />
  </svg>
);

function Bible() {
  const { section, chapter, verse } = useParams();
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
    y: 0,
    preview: '' // For showing selected verses
  });
  const [hasScrolledToVerse, setHasScrolledToVerse] = useState(false);

  // Reset scroll flag when URL changes
  useEffect(() => {
    setHasScrolledToVerse(false);
  }, [section, chapter, verse]);

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

  // Update metadata based on URL parameters (for specific verse)
  useEffect(() => {
    if (!content) return;

    // Remove previous highlights
    const previousHighlights = document.querySelectorAll('.verse-highlight');
    previousHighlights.forEach(el => el.classList.remove('verse-highlight'));

    if (chapter && verse) {
      // URL has chapter and verse like /bible/genesis/1/1 or /bible/genesis/1/1?end=3
      const endVerse = searchParams.get('end');
      const startVerseNum = parseInt(verse);
      const endVerseNum = endVerse ? parseInt(endVerse) : startVerseNum;

      // Collect all verse texts for metadata
      let allVerseTexts = [];

      // Highlight all verses in range
      for (let v = startVerseNum; v <= endVerseNum; v++) {
        const verseId = `${chapter}-${v}`;
        const verseElement = document.getElementById(verseId);

        if (verseElement) {
          const nextElement = verseElement.nextElementSibling;

          // Highlight the verse
          verseElement.classList.add('verse-highlight');
          if (nextElement) {
            nextElement.classList.add('verse-highlight');

            // Collect verse text
            const verseSpans = nextElement.querySelectorAll('span[id="verse"]');
            const verseText = verseSpans.length > 0
              ? verseSpans[verseSpans.length - 1].textContent.trim()
              : nextElement.textContent.trim();
            allVerseTexts.push(verseText);
          }

          // Scroll to the first verse only once when first loaded
          if (v === startVerseNum && !hasScrolledToVerse) {
            setTimeout(() => {
              const yOffset = -150; // Offset to center verse better
              const y = verseElement.getBoundingClientRect().top + window.pageYOffset + yOffset;
              window.scrollTo({ top: y, behavior: 'smooth' });
            }, 100);
            setHasScrolledToVerse(true);
          }
        }
      }

      // Set metadata
      const bookNameJa = bookNamesJa[section] || section;
      const verseRef = endVerse
        ? `${bookNameJa} ${chapter}:${verse}-${endVerse}`
        : `${bookNameJa} ${chapter}:${verse}`;
      const combinedText = allVerseTexts.join(' ');

      setMetaData({
        title: verseRef,
        description: combinedText || '口語訳聖書 旧約：1955年版・新約：1954年版',
        url: `https://www.asmrchurch.com/bible/${section}/${chapter}/${verse}${endVerse ? `?end=${endVerse}` : ''}`,
        image: 'https://www.asmrchurch.com/static/images/card1.jpg'
      });

      return;
    }

    // Default metadata for the book
    const bookNameJa = bookNamesJa[section] || section;
    setMetaData({
      title: `${bookNameJa} - ASMRキリスト教会`,
      description: '口語訳聖書 旧約：1955年版・新約：1954年版',
      url: `https://www.asmrchurch.com/bible/${section}`,
      image: 'https://www.asmrchurch.com/static/images/card1.jpg'
    });
  }, [content, section, chapter, verse, searchParams, bookNamesJa, hasScrolledToVerse]);

  // Add click handlers for verse sharing
  useEffect(() => {
    if (!content) return;

    const handleVerseClick = (e) => {
      // Check if clicked element is a verse link
      const link = e.target.closest('em[id] a[href^="#"]');
      if (!link) return;

      e.preventDefault();
      const verseId = link.parentElement.id; // e.g., "1-1"
      const [chapterNum, verseNum] = verseId.split('-');

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

      // Construct share text with new URL format
      const shareTitle = `${bookNameJa} ${chapterNum}:${verseNum}`;
      const shareText = `${verseText} - ${shareTitle}`;
      const shareUrl = `${window.location.origin}/bible/${section}/${chapterNum}/${verseNum}`;

      // Get click position for popup
      const rect = link.getBoundingClientRect();

      // Show share popup with X and Facebook buttons
      setSharePopup({
        show: true,
        title: shareTitle,
        text: shareText,
        url: shareUrl,
        x: rect.left + window.scrollX,
        y: rect.bottom + window.scrollY + 5,
        preview: '' // No preview for single verse click
      });
    };

    // Handle right-click on selected verses
    const handleContextMenu = (e) => {
      const selection = window.getSelection();
      if (!selection || selection.isCollapsed) return;

      const selectedText = selection.toString().trim();
      if (!selectedText) return;

      // Find all verse elements within the selection
      const range = selection.getRangeAt(0);
      const container = range.commonAncestorContainer;

      // Get the parent element that contains the selection
      const parentElement = container.nodeType === Node.TEXT_NODE
        ? container.parentElement
        : container;

      // Find all verse number elements (em tags with id) in the selected area
      const allEmElements = document.querySelectorAll('em[id]');
      const selectedVerses = [];

      allEmElements.forEach(emElement => {
        if (selection.containsNode(emElement, true) ||
            selection.containsNode(emElement.nextElementSibling, true)) {
          const verseId = emElement.id;
          const [chap, ver] = verseId.split('-');
          const verseTextElement = emElement.nextElementSibling;

          if (verseTextElement) {
            const verseSpans = verseTextElement.querySelectorAll('span[id="verse"]');
            const verseText = verseSpans.length > 0
              ? verseSpans[verseSpans.length - 1].textContent.trim()
              : verseTextElement.textContent.trim();

            selectedVerses.push({
              chapter: chap,
              verse: ver,
              text: verseText
            });
          }
        }
      });

      if (selectedVerses.length > 0) {
        e.preventDefault();

        // Get book name in Japanese
        const bookNameJa = bookNamesJa[section] || section;

        // Construct combined text
        const firstVerse = selectedVerses[0];
        const lastVerse = selectedVerses[selectedVerses.length - 1];

        let shareTitle, shareUrl;
        if (selectedVerses.length === 1) {
          shareTitle = `${bookNameJa} ${firstVerse.chapter}:${firstVerse.verse}`;
          shareUrl = `${window.location.origin}/bible/${section}/${firstVerse.chapter}/${firstVerse.verse}`;
        } else {
          shareTitle = `${bookNameJa} ${firstVerse.chapter}:${firstVerse.verse}-${lastVerse.verse}`;
          shareUrl = `${window.location.origin}/bible/${section}/${firstVerse.chapter}/${firstVerse.verse}?end=${lastVerse.verse}`;
        }

        // Combine all verse texts
        const combinedText = selectedVerses.map((v, i) =>
          `${v.text}${i < selectedVerses.length - 1 ? ' ' : ''}`
        ).join('');

        const shareText = `${combinedText} - ${shareTitle}`;

        // Show share popup at right-click position with preview
        setSharePopup({
          show: true,
          title: shareTitle,
          text: shareText,
          url: shareUrl,
          x: e.pageX,
          y: e.pageY,
          preview: combinedText // Show preview of selected verses
        });
      }
    };

    // Add event listener to content div
    const contentDiv = document.querySelector('.content section');
    if (contentDiv) {
      contentDiv.addEventListener('click', handleVerseClick);
      contentDiv.addEventListener('contextmenu', handleContextMenu);
    }

    // Cleanup
    return () => {
      if (contentDiv) {
        contentDiv.removeEventListener('click', handleVerseClick);
        contentDiv.removeEventListener('contextmenu', handleContextMenu);
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
          <AdIcons />
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
              maxWidth: '500px'
            }}
          >
            {sharePopup.preview && (
              <div
                style={{
                  backgroundColor: '#f9f9f9',
                  padding: '10px',
                  borderRadius: '4px',
                  marginBottom: '12px',
                  fontSize: '14px',
                  lineHeight: '1.5',
                  maxHeight: '150px',
                  overflowY: 'auto',
                  borderLeft: '3px solid #e99708'
                }}
              >
                <div style={{ fontWeight: 'bold', marginBottom: '6px', color: '#333' }}>
                  {sharePopup.title}
                </div>
                <div style={{ color: '#555' }}>
                  {sharePopup.preview}
                </div>
              </div>
            )}
            <div
              style={{
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
              <BloggerShareButton
                url={sharePopup.url}
                title={sharePopup.title}
                text={sharePopup.preview || sharePopup.text}
                image="https://www.asmrchurch.com/static/images/c4.jpg"
              >
                <BloggerIcon size={32} />
              </BloggerShareButton>
            </div>
          </div>
        </>
      )}

      <Footer />

      {/* Verse highlight styles */}
      <style>{`
        .verse-highlight {
          background-color: rgba(255, 255, 0, 0.3);
          padding: 2px 4px;
          border-radius: 3px;
          transition: background-color 0.3s ease;
        }
      `}</style>
    </div>
  );
}

export default Bible;
