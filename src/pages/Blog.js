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
