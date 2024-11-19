import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import Header from '../components/Header';
import MarkDown from '../components/MarkDown';
import Footer from '../components/Footer';
import '../blog.css';

function Article() {
  const [markdown, setMarkdown] = useState('');
  const { id } = useParams();

  return (
    <div>
      <Header />
      <div className="cont2">
        <MarkDown path={`/article/${id}`} />
        <div className="return">
        </div>
        <a href="/article">記事一覧</a>
      </div>
      <Footer />
    </div>
  );
}

export default Article;
