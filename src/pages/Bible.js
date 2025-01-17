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
      <Header bible={true} subon={true} />
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
            <div dangerouslySetInnerHTML={{ __html: content }} />
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
              src="https://bandcamp.com/EmbeddedPlayer/album=3869678226/size=large/bgcol=333333/linkcol=e99708/transparent=true/"
              seamless
            >
              <a href="https://asmrchruch.bandcamp.com/album/asmr-32">
                旧​​​約​​​聖​​​書​​​ASMR​​​｜​​​詩篇 by ASMRキリスト教会
              </a>
            </iframe>
          </span>
        </div>
      </div>
      <Footer />
    </div>
  );
}

export default Bible;
