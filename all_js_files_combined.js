// File: server.js
const express = require('express');
const path = require('path');
const app = express();

// Serve the static files from the React app
app.use(express.static(path.join(__dirname, 'build')));

// Handles any requests that don't match the ones above
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'build', 'index.html'));
});

const port = process.env.PORT || 80;
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

-e 


// File: src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './pages/Home';
import Bible from './pages/Bible';
import Blog from './pages/Blog';
import Sermon from './pages/Sermon';
import Caption from './pages/Caption';
import Manga from './pages/Manga';
import Pay from './pages/Pay';
import ListComponent from './components/ListComponent';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/bible/:section" element={<Bible />} />
        <Route path="/blog" element={<ListComponent type="blog" title={`ブログ`}/>} />
        <Route path="/blog/:id" element={<Blog />} />
        <Route path="/sermon/:id" element={<Sermon />} />
        <Route path="/manga/:id" element={<Manga />} />
        <Route path="/manga" element={<ListComponent type="manga" title={`漫画`}/>} />
        <Route path="/sermon" element={<ListComponent type="sermon" title={`説教`}/>} />
        <Route path="/caption" element={<Caption />} />
        <Route path="/pay" element={<Pay />} />
      </Routes>
    </Router>
  );
}

export default App;

-e 


// File: src/App.test.js
import { render, screen } from '@testing-library/react';
import App from './App';

test('renders learn react link', () => {
  render(<App />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});
-e 


// File: src/Genesis.js
import React, { useEffect, useState } from 'react';

function Genesis() {
  const [content, setContent] = useState(null);

  useEffect(() => {
    // Fetch the XML file
    fetch('/genesis.xml')
      .then((response) => response.text())
      .then((data) => {
        // Parse the XML
        const parser = new DOMParser();
        const xml = parser.parseFromString(data, 'application/xml');
        setContent(xml);
      })
      .catch((error) => {
        console.error('Error fetching or parsing the XML:', error);
      });
  }, []);

  return (
    <div>
      <h1>創世記 (Genesis)</h1>
      {content ? (
        // Function to render the parsed XML content
        renderXMLContent(content)
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
}

// Function to render the parsed XML content
function renderXMLContent(xml) {
  const book = xml.querySelector('book');
  const title = book.querySelector('title');
  const chapters = book.querySelectorAll('chapter');

  return (
    <div>
      <h2>
        {renderTitle(title)}
      </h2>
      {Array.from(chapters).map((chapter, i) => (
        <div key={i}>
          <h3>Chapter {chapter.getAttribute('id')}</h3>
          {renderChapter(chapter)}
        </div>
      ))}
    </div>
  );
}

function renderTitle(title) {
  return Array.from(title.children).map((word, i) => (
    <ruby key={i}>
      {word.textContent}
      <rt>{word.getAttribute('s')}</rt>
    </ruby>
  ));
}

function renderChapter(chapter) {
  const paragraphs = chapter.querySelectorAll('p');
  return Array.from(paragraphs).map((paragraph, i) => (
    <div key={i}>
      {renderParagraph(paragraph)}
    </div>
  ));
}

function renderParagraph(paragraph) {
  const verses = paragraph.querySelectorAll('verse');
  return (
    <div>
      {Array.from(verses).map((verse, i) => (
        <p key={i}>
          <strong>{verse.getAttribute('id')}: </strong>
          {Array.from(verse.children).map((word, j) => (
            <ruby key={j}>
              {word.textContent}
              <rt>{word.getAttribute('s')}</rt>
            </ruby>
          ))}
        </p>
      ))}
    </div>
  );
}

export default Genesis;

-e 


// File: src/components/Ad.js
import React from 'react';
import './styles.css';

function Ad() {
  return (
    <div className="section ad">
      <h1></h1>

     <div>
        <div>
          <div>
            <a target="_blank" rel="noopener noreferrer" href="https://www.kirishin.com/2024/05/19/66663/">
              メディア掲載: キリスト新聞様
            </a>
          </div>
          <div>
            <a target="_blank" rel="noopener noreferrer" href="/caption">
              コスパ名言集
            </a>
          </div>
        </div>
      </div>

      <div className="">
        <a target="_blank" rel="noopener noreferrer" href="https://www.dlsite.com/home/work/=/product_id/RJ433352.html">
          <img 
            src={`${process.env.PUBLIC_URL}/static/images/dlsite.png`}
            alt="x" 
            style={{ height: '35px' }}
          />
        </a>
      </div>

      <div className="kirikan">
        <a target="_blank" rel="noopener noreferrer" href="https://www.youtube.com/@asmrchurch">
          <img 
            src={`${process.env.PUBLIC_URL}/static/images/tube2.jpg`}
            alt="x" 
            style={{ height: '130px' }}
          />
        </a>
      </div>

      <div className="kirikan">
        <a target="_blank" rel="noopener noreferrer" href="https://www.pixiv.net/en/users/107379276">
          <img 
            src={`${process.env.PUBLIC_URL}/static/images/pixiv.jpg`}
            alt="x" 
            style={{ height: '130px' }}
          />
        </a>
      </div>

      <div className="kirikan">
        <a target="_blank" rel="noopener noreferrer" href="https://www.tiktok.com/@sexybible">
          <img 
            src={`${process.env.PUBLIC_URL}/static/images/tiktok.jpg`}
            alt="x"
            style={{ height: '130px' }}
          />
        </a>
      </div>

      <div className="kirikan">
        <a target="_blank" rel="noopener noreferrer" href="https://asmrchruch.bandcamp.com/">
          <img 
            src={`${process.env.PUBLIC_URL}/static/images/bandcamp.jpg`}
            alt="x"
            style={{ height: '130px' }}
          />
        </a>
      </div>
    </div>
  );
}

export default Ad;
-e 


// File: src/components/BibleList.js
import React from 'react';
import './styles.css';

function BibleList({ title, type, books }) {
  return (
    <div className="section">
      <h1>{title}</h1>
      <div>
        {books.map(([route, displayName]) => (
          <div className="li" key={route}>
            <a href={`/bible/${route}?type=${type}`}>{type === 'en' ? route : displayName}</a>
          </div>
        ))}
      </div>
    </div>
  );
}

export default BibleList;
-e 


// File: src/components/Footer.js
import React from 'react';

function Footer() {
  return (
    <footer style={{ textAlign: 'center', padding: '10px', fontSize: '14px', color: '#333' }}>
      ASMRキリスト教会 all rights reserved.
    </footer>
  );
}

export default Footer;
-e 


// File: src/components/Ham.js
import React, { useState, useEffect, useRef } from 'react';
import './Ham.css';

function Ham() {
  const [isOpen, setIsOpen] = useState(false);
  const menuRef = useRef(null);  // Use a ref to track the menu container

  const handleClick = () => {
    setIsOpen(!isOpen);
  };

  const handleOutsideClick = (e) => {
    // Close the menu if the click is outside the menu and the hamburger button
    if (menuRef.current && !menuRef.current.contains(e.target)) {
      setIsOpen(false);
    }
  };

  // Close the menu when clicking outside or a menu item is clicked
  useEffect(() => {
    if (isOpen) {
      document.addEventListener('mousedown', handleOutsideClick);
    } else {
      document.removeEventListener('mousedown', handleOutsideClick);
    }
    return () => {
      document.removeEventListener('mousedown', handleOutsideClick);
    };
  }, [isOpen]);

  // Function to close the menu when a link is clicked
  const handleLinkClick = () => {
    setIsOpen(false);
  };

  return (
    <div className="hamburger-menu" ref={menuRef}>
      <div className="hamburger" onClick={handleClick}>
        <div className={`line ${isOpen ? 'open' : ''}`}></div>
        <div className={`line ${isOpen ? 'open' : ''}`}></div>
        <div className={`line ${isOpen ? 'open' : ''}`}></div>
      </div>
      <nav className={`nav-menu ${isOpen ? 'open' : ''}`}>
        <ul>
          <li className="hmb"><a href="/" onClick={handleLinkClick}>Home</a></li>
          <li className="hmb"><a href="/blog" onClick={handleLinkClick}>Blog</a></li>
          <li className="hmb"><a href="/sermon" onClick={handleLinkClick}>説教</a></li>
          <li className="hmb"><a href="/manga" onClick={handleLinkClick}>漫画</a></li>
        </ul>
      </nav>
    </div>
  );
}

export default Ham;
-e 


// File: src/components/Header.js
import React, { useState, useEffect } from 'react';
import { Helmet } from 'react-helmet';
import '../styles.css';
import Ham from './Ham';

function Header({ bible, title, description, url, image, subon }) {
  const [pageType, setState] = useState('norm');

  useEffect(() => {
    const urlParams = new URLSearchParams(window.location.search);
    const currentRuby = urlParams.get('type');
    setState(currentRuby || 'norm');
  }, []);

  const toggleRuby = () => {
    const urlParams = new URLSearchParams(window.location.search);
    let newState;

    if (pageType === 'norm') {
      newState = 'ruby';
    } else if (pageType === 'ruby') {
      newState = 'en';
    } else {
      newState = 'norm';
    }

    urlParams.set('type', newState);
    window.location.search = urlParams.toString(); // Reload the page with the new state

    setState(newState); // Update the state
  };

  const toggleLang = () => {
    const urlParams = new URLSearchParams(window.location.search);
    let newState;

    if (pageType === 'norm') {
      newState = 'en';
    } else {
      newState = 'norm';
    }

    urlParams.set('type', newState);
    window.location.search = urlParams.toString(); // Reload the page with the new state

    setState(newState); // Update the state
  };

  return (
    <div>
      <div className="header">
        <Helmet>
          <meta charSet="UTF-8" />
          <link rel="icon" href="/static/favicon/favicon.ico" />
          <meta name="viewport" content="width=device-width, initial-scale=1.0" />
          <title>{title || "ASMRキリスト教会"}</title>
          <meta name="description" content={description || "10代〜20代の若者へ..."} />
          <meta name="keywords" content="聖書, キリスト教, ASMR, 教会" />
          
          {/* Open Graph / Facebook */}
          <meta property="og:type" content="article" />
          <meta property="og:title" content={title || "ASMRキリスト教会"} />
          <meta property="og:description" content={description || "10代〜20代の若者へ..."} />
          <meta property="og:url" content={url || "https://www.asmrchurch.com"} />
          <meta property="og:image" content={image || "https://www.asmrchurch.com/static/images/kirikan.jpg"} />

          {/* Twitter */}
          <meta name="twitter:card" content="summary_large_image" />
          <meta name="twitter:title" content={title || "ASMRキリスト教会"} />
          <meta name="twitter:description" content={description || "10代〜20代の若者へ..."} />
          <meta name="twitter:url" content={url || "https://www.asmrchurch.com"} />
          <meta name="twitter:image" content={image || "https://www.asmrchurch.com/static/images/kirikan.jpg"} />
        </Helmet>

        <div className="c1">
          <a href="/">聖書ASMR</a>
        </div>

        <div className="c3">
          <a target="_blank" rel="noopener noreferrer" href="https://x.com/asmrchurch">
            <img
              src={`${process.env.PUBLIC_URL}/static/images/x.png`}
              alt="X (formerly Twitter) logo"
              style={{ width: '50px' }}
            />
          </a>
          <a target="_blank" rel="noopener noreferrer" href="https://www.youtube.com/@asmrchurch">
            <img
              src={`${process.env.PUBLIC_URL}/static/images/youtube.png`}
              alt="YouTube logo"
              style={{ width: '50px' }}
            />
          </a>
        </div>

        <div className="ham">
          <Ham />
        </div>
      </div>
     
     {subon === true && (
       <div className="csub">
         <div className="ll">
           <a className="al" href="?type=norm">日本語</a> |
           <a className="al" href="?type=ruby">かな</a> |
           <a className="al" href="?type=en">English</a>
         </div>
       </div>
     )}
    </div>
  );
}

export default Header;
-e 


// File: src/components/ListComponent.js
import React, { useState, useEffect } from 'react';
import './styles.css';
import '../blog.css';
import Header from '../components/Header';
import Footer from '../components/Footer';
import MarkDown from '../components/MarkDown';

function ListComponent({ type, title }) {
  const [articles, setArticles] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const postsPerPage = 5;

  useEffect(() => {
    fetch(`/static/markdown/${type}/list.json`)
      .then((response) => response.json())
      .then((data) => setArticles(data.articles))
      .catch((error) => console.error('Error fetching list:', error));
  }, [type]);

  // Calculate the current articles to display
  const indexOfLastPost = currentPage * postsPerPage;
  const indexOfFirstPost = indexOfLastPost - postsPerPage;
  const currentArticles = articles.slice().reverse().slice(indexOfFirstPost, indexOfLastPost);

  // Change page
  const nextPage = () => {
    if (currentPage < Math.ceil(articles.length / postsPerPage)) {
      setCurrentPage(currentPage + 1);
    }
  };

  const prevPage = () => {
    if (currentPage > 1) {
      setCurrentPage(currentPage - 1);
    }
  };

  return (
    <div>
      <Header />
      <div className="blog-section">
        <h1>{title}</h1>
        <hr />
        <div className="blog-list">
          {currentArticles.map((id) => (
            <div key={id}>
              <MarkDown path={`/${type}/${id}`} preview={true} type={type}/>
              <div className="readarticle">
                  <a href={`/${type}/${id}`}> 続きを読む </a>
              </div>
              <hr />
            </div>
          ))}
        </div>
        {/* Pagination controls */}
        <div className="pagination">
          <button onClick={prevPage} disabled={currentPage === 1}>
           ← 
          </button>
          <span className="pagecount">{currentPage} / {Math.ceil(articles.length / postsPerPage)}</span>
          <button onClick={nextPage} disabled={currentPage === Math.ceil(articles.length / postsPerPage)}>
          →
          </button>
        </div>
      </div>
      <Footer />
    </div>
  );
}

export default ListComponent;
-e 


// File: src/components/MarkDown.js
import React, { useState, useEffect } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import '../blog.css';
import Share from './Share';

function MarkDown({ path, preview, type }) {
  const [markdown, setMarkdown] = useState('');
  const [title, setTitle] = useState('');
  const url = `https://www.asmrchurch.com${path}`;

  useEffect(() => {
    fetch(`/static/markdown${path}.md`)
      .then((response) => {
        if (response.ok) {
          return response.text();
        } else {
          throw new Error('Markdown file not found');
        }
      })
      .then((text) => {
        setMarkdown(text);

        const firstTitleLine = text.split('\n').find(line => line.startsWith('#'));
        if (firstTitleLine) {
          const firstTitle = firstTitleLine.replace('# ', ''); // Strip leading "# "
          setTitle(firstTitle);
        }
      })
      .catch((error) => {
        console.error(error);
        setMarkdown('# 404 Not Found\nThe requested markdown file could not be found.');
      });
  }, [path]);

  // If preview mode is on, only show the first three lines
  const previewContent = preview ? markdown.split('\n').slice(0, 10).join('\n') : markdown;

  return (
    <div>
      <div className={`${type === 'manga' ? 'manga' : 'blog-section'}`}>
        <ReactMarkdown children={previewContent} remarkPlugins={[remarkGfm]} />
      </div>
      {/* Show the Share component only if it's not in preview mode */}
      {!preview && (
        <Share title={`【ASMRキリスト教会】${title} @asmrchurch #聖書 #ASMR #キリスト教`} url={url} />
      )}
    </div>
  );
}

export default MarkDown;
-e 


// File: src/components/PayComponent.js
import React, { useState, useEffect } from "react";
import Header from '../components/Header';

const ProductDisplay = () => (
  <div className="product">
    <div>
      <div className="productmain">
        <div className="description">
            <h3>ASMRキリスト教会をサポートしてください！</h3>
            <h5>ASMRキリスト教会は、聖書ASMRの製造、口語訳聖書のアーカイブ保存公開、若者の伝道活動、いのちのASMR電話、その他日本のキリスト教をプロテスタントの観点から維持・発展させる活動を継続しております。もし当教会の理念に賛同いただける方は、献金サポートしていただけますと弊社の活動の重要な資金源になります。</h5>
        </div>
      </div>

<span className="pad">
<stripe-buy-button
  buy-button-id="buy_btn_1QHPjSJrEFc0aoshlEXLL0iI"
  publishable-key="pk_live_51L77y9JrEFc0aoshDbT8faRDJBWQJjQTGvMb6jngK3GGGpMtIYf8omncPkMd8e0be0ZsfG2yEWaxYdMSlGSS9pgX00RNzmWvfw"
> </stripe-buy-button>
</span>

<span className="pad">
<stripe-buy-button
  buy-button-id="buy_btn_1QHPZqJrEFc0aoshadCn7Xkb"
  publishable-key="pk_live_51L77y9JrEFc0aoshDbT8faRDJBWQJjQTGvMb6jngK3GGGpMtIYf8omncPkMd8e0be0ZsfG2yEWaxYdMSlGSS9pgX00RNzmWvfw"
> </stripe-buy-button>
</span>

<span className="pad">
<stripe-buy-button
  buy-button-id="buy_btn_1QHQ7nJrEFc0aoshQi8yT9A0"
  publishable-key="pk_live_51L77y9JrEFc0aoshDbT8faRDJBWQJjQTGvMb6jngK3GGGpMtIYf8omncPkMd8e0be0ZsfG2yEWaxYdMSlGSS9pgX00RNzmWvfw"
>
</stripe-buy-button>
</span>

    </div>
  </div>
);

const Message = ({ message }) => (
  <section>
    <p>{message}</p>
  </section>
);

export default function PayComponent() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    // Check to see if this is a redirect back from Checkout
    const query = new URLSearchParams(window.location.search);

    if (query.get("success")) {
      setMessage("Order placed! You will receive an email confirmation.");
    }

    if (query.get("canceled")) {
      setMessage(
        "Order canceled -- continue to shop around and checkout when you're ready."
      );
    }
  }, []);

  return message ? (
    <Message message={message} />
  ) : (
    <ProductDisplay />
  );
}

-e 


// File: src/components/Share.js
import React from 'react';
import { 
  FacebookShareButton, 
  TwitterShareButton, 
  EmailShareButton, 
  RedditShareButton, 
  LinkedinShareButton 
} from 'react-share';
import { 
  FacebookIcon, 
  XIcon, 
  EmailIcon, 
  RedditIcon, 
  LinkedinIcon 
} from 'react-share';

const Share = ({title, url}) => {
  return (
    <div className="sharecontainer">
      <span className="tt"> 布教する: </span>
      <div className="share">

        {/* X (X) Share Button */}
        <TwitterShareButton url={url} title={title}>
          <XIcon size={32} round={false} />
        </TwitterShareButton>

        {/* Facebook Share Button */}
        <FacebookShareButton url={url} quote={title}>
          <FacebookIcon size={32} round={false} />
        </FacebookShareButton>

        {/* Email Share Button */}
        <EmailShareButton url={url} subject={title} body="Check this out:">
          <EmailIcon size={32} round={false} />
        </EmailShareButton>

        {/* Reddit Share Button */}
        <RedditShareButton url={url} title={title}>
          <RedditIcon size={32} round={false} />
        </RedditShareButton>

        {/* LinkedIn Share Button */}
        <LinkedinShareButton url={url} title={title} summary={title}>
          <LinkedinIcon size={32} round={false} />
        </LinkedinShareButton>
      </div>
    </div>
  );
};

export default Share;
-e 


// File: src/index.js
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

const rootElement = document.getElementById('root');
const root = ReactDOM.createRoot(rootElement);

root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
-e 


// File: src/pages/Bible.js
import React, { useState, useEffect } from 'react';
import { useParams, useSearchParams } from 'react-router-dom';
import Header from '../components/Header';
import Footer from '../components/Footer';

function Bible() {
  const { section } = useParams();
  const [searchParams, setSearchParams] = useSearchParams();
  const [content, setContent] = useState('');

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
    <div>
      <Header bible={true} subon={true}/>
      <div className="content">
        <section>
          <div dangerouslySetInnerHTML={{ __html: content }} />
        </section>
      </div>
      <Footer />
    </div>
  );
}

export default Bible;
-e 


// File: src/pages/Blog.js
import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import Header from '../components/Header';
import MarkDown from '../components/MarkDown';
import Footer from '../components/Footer';
import '../blog.css';

function Blog() {
  const [markdown, setMarkdown] = useState('');
  const { id } = useParams();

  return (
    <div>
      <Header />
      <MarkDown path={`/blog/${id}`} />
      <div className="return">
      <a href="/blog">ブログ一覧</a>
      </div>
      <Footer />
    </div>
  );
}

export default Blog;
-e 


// File: src/pages/Caption.js
import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import Header from '../components/Header';
import Footer from '../components/Footer';
import MarkDown from '../components/MarkDown';
import '../blog.css';

// 名言集
function Caption() {
  const [markdown, setMarkdown] = useState('');

  useEffect(() => {
    fetch(`/static/markdown/caption.md`)
      .then((response) => {
        if (response.ok) {
          return response.text();
        } else {
          throw new Error('Markdown file not found'); // Handle errors
        }
      })
      .then((text) => setMarkdown(text))
      .catch((error) => {
        console.error(error);
        setMarkdown('# 404 Not Found\nThe requested markdown file could not be found.');
      });
  });

  return (
    <div>
      <Header />
      <div className="blog-section">
        <ReactMarkdown children={markdown} remarkPlugins={[remarkGfm]} />
      </div>
      <Footer />
    </div>
  );
}

export default Caption;
-e 


// File: src/pages/Home.js
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
        <Ad />
      </div>
      <PayComponent />
      <Footer />
    </div>
  );
}

export default Home;
-e 


// File: src/pages/Manga.js
import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import Header from '../components/Header';
import MarkDown from '../components/MarkDown';
import Footer from '../components/Footer';
import '../blog.css';

function Manga() {
  const [markdown, setMarkdown] = useState('');
  const { id } = useParams();

  return (
    <div>
      <Header />
      <MarkDown path={`/love/${id}`} />
      <div className="return">
      <a href="/blog">恋愛講座一覧</a>
      </div>
      <Footer />
    </div>
  );
}

export default Manga;
-e 


// File: src/pages/Pay.js
import React, { useState, useEffect } from "react";
import Header from '../components/Header';
import PayComponent from '../components/PayComponent';

export default function Pay() {
      
  return (
      <div>
      <Header subon={true} />
      <PayComponent />
      </div>
  )
}
-e 


// File: src/pages/Sermon.js
import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import Header from '../components/Header';
import MarkDown from '../components/MarkDown';
import Footer from '../components/Footer';
import '../blog.css';

function Sermon() {
  const [markdown, setMarkdown] = useState('');
  const { id } = useParams();

  return (
    <div>
      <Header />
      <MarkDown path={`/sermon/${id}`} />
      <div className="return">
        <a href="/sermon">説教一覧</a>
      </div>
      <Footer />
    </div>
  );
}

export default Sermon;
-e 


// File: src/reportWebVitals.js
const reportWebVitals = onPerfEntry => {
  if (onPerfEntry && onPerfEntry instanceof Function) {
    import('web-vitals').then(({ getCLS, getFID, getFCP, getLCP, getTTFB }) => {
      getCLS(onPerfEntry);
      getFID(onPerfEntry);
      getFCP(onPerfEntry);
      getLCP(onPerfEntry);
      getTTFB(onPerfEntry);
    });
  }
};

export default reportWebVitals;
-e 


// File: src/setupTests.js
// jest-dom adds custom jest matchers for asserting on DOM nodes.
// allows you to do things like:
// expect(element).toHaveTextContent(/react/i)
// learn more: https://github.com/testing-library/jest-dom
import '@testing-library/jest-dom';
-e 


