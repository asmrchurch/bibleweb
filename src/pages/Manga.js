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
      <div className="cont2">
      <MarkDown path={`/manga/${id}`} />
      <div className="return">
      </div>
      <a href="/manga">漫画一覧</a>
      </div>
      <Footer />
    </div>
  );
}

export default Manga;
