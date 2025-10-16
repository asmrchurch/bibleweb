import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import Header from '../components/Header';
import MarkDown from '../components/MarkDown';
import Footer from '../components/Footer';
import { AdIcons } from '../components/Ad';
import '../blog.css';

function Sermon() {
  const [markdown, setMarkdown] = useState('');
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [image, setImage] = useState('');
  const { id } = useParams();

  useEffect(() => {
    // Fetch the markdown file to extract metadata
    fetch(`/static/markdown/sermon/${id}.md`)
      .then((response) => {
        if (response.ok) {
          return response.text();
        } else {
          throw new Error('Markdown file not found');
        }
      })
      .then((text) => {
        const lines = text.split('\n');

        // Extract title (first H1)
        const firstTitleLine = lines.find(line => line.startsWith('#'));
        if (firstTitleLine) {
          const extractedTitle = firstTitleLine.replace(/^#\s*/, '');
          setTitle(extractedTitle);
        }

        // Extract description (first paragraph after title, limit to 150 chars)
        const titleIndex = lines.findIndex(line => line.startsWith('#'));
        let descText = '';
        for (let i = titleIndex + 1; i < lines.length; i++) {
          const line = lines[i].trim();
          // Skip empty lines and image markdown
          if (line && !line.startsWith('!') && !line.startsWith('#')) {
            descText = line;
            break;
          }
        }
        // Remove markdown formatting and limit length
        const cleanDesc = descText.replace(/[*_`~[\]()]/g, '').substring(0, 150);
        setDescription(cleanDesc || '説教の内容をお読みください。');

        // Extract first image
        const imageMatch = text.match(/!\[.*?\]\((.*?)\)/);
        if (imageMatch && imageMatch[1]) {
          const imagePath = imageMatch[1];
          setImage(`https://www.asmrchurch.com${imagePath}`);
        } else {
          setImage('https://www.asmrchurch.com/static/images/i4.jpg');
        }
      })
      .catch((error) => {
        console.error(error);
        setTitle('説教');
        setDescription('ASMRキリスト教会の説教');
        setImage('https://www.asmrchurch.com/static/images/i4.jpg');
      });
  }, [id]);

  const url = `https://www.asmrchurch.com/sermon/${id}`;

  return (
    <div>
      <div className="bibleframe">
      <Header
        title={title || '説教 - ASMRキリスト教会'}
        description={description}
        url={url}
        image={image}
      />

      <div className="flex-container">
        <div className="left-area">
          <AdIcons />
        </div>

      <div className="content">
        <MarkDown path={`/sermon/${id}`} />
        <div className="return">
          <a href="/sermon">説教一覧</a>
        </div>
        <div className="mobile-ads">
          <AdIcons />
        </div>
      </div>

      <div className="right-area">
        <span className="pad">
          <stripe-buy-button
            buy-button-id="buy_btn_1QiEyXJrEFc0aoshZrg6uGA0"
            publishable-key="pk_live_51L77y9JrEFc0aoshDbT8faRDJBWQJjQTGvMb8e0be0ZsfG2yEWaxYdMSlGSS9pgX00RNzmWvfw"
          >
          </stripe-buy-button>
        </span>
      </div>
      </div>
      </div>
      <Footer />
    </div>
  );
}

export default Sermon;
