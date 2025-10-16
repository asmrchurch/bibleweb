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
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [image, setImage] = useState('');
  const { id } = useParams();

  useEffect(() => {
    // Fetch the markdown file to extract metadata
    fetch(`/static/markdown/blog/${id}.md`)
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
        setDescription(cleanDesc || 'ASMRキリスト教会のブログ');

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
        setTitle('ブログ');
        setDescription('ASMRキリスト教会のブログ');
        setImage('https://www.asmrchurch.com/static/images/i4.jpg');
      });
  }, [id]);

  const url = `https://www.asmrchurch.com/blog/${id}`;

  return (
    <div>
      <Header
        title={title || 'ブログ - ASMRキリスト教会'}
        description={description}
        url={url}
        image={image}
      />
      <div className="cont2">
        <MarkDown path={`/blog/${id}`} />
        <a href="/blog">ブログ一覧</a>
        <div className="return">
        </div>
      </div>
      <Footer />
    </div>
  );
}

export default Blog;
