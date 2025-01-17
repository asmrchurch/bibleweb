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
      <div className="bibleframe">
      <Header />

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
        <MarkDown path={`/sermon/${id}`} />
        <div className="return">
          <a href="/sermon">説教一覧</a>
        </div>
      </div>
      </div>
      </div>
      <Footer />
    </div>
  );
}

export default Sermon;
