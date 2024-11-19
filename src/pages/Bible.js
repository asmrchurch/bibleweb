import React, { useState, useEffect } from 'react';
import { useParams, useSearchParams } from 'react-router-dom';
import Header from '../components/Header';
import Footer from '../components/Footer';
import PayComponent from '../components/PayComponent';

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
    <div className="bibleframe">
      <Header bible={true} subon={true}/>
      <div className="content" dangerouslySetInnerHTML={{ __html: content }} />
      <Footer />
    </div>
  );
}

export default Bible;
