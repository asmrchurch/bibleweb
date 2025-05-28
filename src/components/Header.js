import React, { useState, useEffect } from 'react';
import { Helmet } from 'react-helmet';
import '../styles.css';
import Ham from './Ham';

function Header({ bible, title, description, url, image, subon }) {
  const [pageType, setPageType] = useState('norm');
  const [isSmartphone, setIsSmartphone] = useState(false);

  useEffect(() => {
    const handleResize = () => {
      setIsSmartphone(window.innerWidth < 768);
    };

    // Initial check and listener for resize
    handleResize();
    window.addEventListener('resize', handleResize);

    // Cleanup listener
    return () => window.removeEventListener('resize', handleResize);
  }, []);

  useEffect(() => {
    const urlParams = new URLSearchParams(window.location.search);
    const currentRuby = urlParams.get('type');
    setPageType(currentRuby || 'norm');
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

    setPageType(newState); // Update the state
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

    setPageType(newState); // Update the state
  };

  return (
    <div>

      <div className="header">
        <Helmet>
          <script>
            {`
              !function(e,t,n,s,u,a){
                e.twq||(s=e.twq=function(){
                  s.exe?s.exe.apply(s,arguments):s.queue.push(arguments);
                },
                s.version='1.1',
                s.queue=[],
                u=t.createElement(n),
                u.async=!0,
                u.src='https://static.ads-twitter.com/uwt.js',
                a=t.getElementsByTagName(n)[0],
                a.parentNode.insertBefore(u,a))
              }(window,document,'script');
              twq('config','puq2w');
            `}
          </script>
          <script async src="https://www.googletagmanager.com/gtag/js?id=AW-16949700128"></script>
          <script>
            {`
              window.dataLayer = window.dataLayer || [];
              function gtag(){dataLayer.push(arguments);}
              gtag('js', new Date());
              gtag('config', 'AW-16949700128');
            `}
          </script>
        
          <meta charSet="UTF-8" />
          <link rel="icon" href="/static/favicon/favicon.ico" />
          <meta name="viewport" content="width=device-width, initial-scale=1.0" />
          <title>{title || "ASMRキリスト教会"}</title>
          <meta name="description" content={description || "10代〜20代の若者へ..."} />
          <meta name="keywords" content="聖書, キリスト教, ASMR, 教会" />
        
          {/* Open Graph / Facebook */}
          <meta property="og:type" content="article" />
          <meta property="og:title" content={title || "ASMRキリスト教会"} />
          <meta property="og:description" content={description || "口語訳聖書 旧約：1955年版・新約：1954年版 ルビ付き・振り仮名付き"} />
          <meta property="og:url" content={url || "https://www.asmrchurch.com"} />
          <meta property="og:image" content={image || "https://www.asmrchurch.com/static/images/i4.jpg"} />
        
          {/* Twitter */}
          <meta name="twitter:card" content="summary_large_image" />
          <meta name="twitter:title" content={title || "ASMRキリスト教会"} />
          <meta name="twitter:description" content={description || "10代〜20代の若者へ..."} />
          <meta name="twitter:url" content={url || "https://www.asmrchurch.com"} />
          <meta name="twitter:image" content={image || "https://www.asmrchurch.com/static/images/i4.jpg"} />
        </Helmet>

        <div className="c1">
          <a href="/">ASMRキリスト教会</a>
        </div>

        <div className="c11">
        {!isSmartphone && (
               <span>
               <span className="ind"><a href="/" >Home</a></span> 
               <span className="pipe">| </span>
               <span className="ind"><a href="/article/2">概要</a></span> 
               <span className="pipe">| </span>
               <span className="ind"><a href="https://note.com/asmrchurch/m/m1c9750805e96">Blog</a></span> 
               <span className="pipe">| </span>
               <span className="ind"><a href="/sermon">説教</a></span> 
               <span className="pipe">| </span>
               <span className="ind"><a href="/qa">Q&A</a></span>
               <span className="pipe">| </span>
               <span className="ind"><a href="https://suzuri.jp/asmrchurch2">SHOP</a></span>
               </span>
        )}
        </div>

        <div className="c3">
          <a target="_blank" rel="noopener noreferrer" href="https://www.youtube.com/@asmrchurch">
            <img
              className="logo"
              src={`${process.env.PUBLIC_URL}/static/images/youtube.png`}
              alt="YouTube logo"
            />
          </a>
        </div>

        {/* Render Ham only for smartphones */}
        {isSmartphone && (
          <div className="ham">
            <Ham />
          </div>
        )}

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
