import React from 'react';
import './styles.css';

function Ad() {
  return (
    <div className="section ad">
     <h1>記事一覧</h1>
     <div className="">
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
        <div>
          <a target="_blank" rel="noopener noreferrer" href="/english">
           聖書で学ぶ！受験英語🇬🇧
          </a>
        </div>
        <div>
          <a target="_blank" rel="noopener noreferrer" href="/actor">
           聖書ASMR・声優図鑑
          </a>
        </div>
        <div>
          <a target="_blank" rel="noopener noreferrer" href="/article/1">
            いのちのASMR電話
          </a>
        </div>
      </div>

      <div className="symbols">
        <div className="symbol">
          <a target="_blank" rel="noopener noreferrer" href="https://www.dlsite.com/home/work/=/product_id/RJ433352.html">
            <img 
              src={`${process.env.PUBLIC_URL}/static/images/dlsite.png`}
              alt="x" 
              style={{ height: '50px' }}
            />
          </a>
        </div>

        <div className="symbol">
          <a target="_blank" rel="noopener noreferrer" href="https://www.youtube.com/@asmrchurch">
            <img 
              src={`${process.env.PUBLIC_URL}/static/images/youtube.png`}
              alt="x" 
              style={{ height: '80px' }}
            />
          </a>
        </div>

        <div className="symbol">
          <a target="_blank" rel="noopener noreferrer" href="https://www.pixiv.net/en/users/107379276">
            <img 
              src={`${process.env.PUBLIC_URL}/static/images/pixiv.png`}
              alt="x" 
              style={{ height: '50px' }}
            />
          </a>
        </div>

        <div className="symbol">
          <a target="_blank" rel="noopener noreferrer" href="https://www.tiktok.com/@sexybible">
            <img 
              src={`${process.env.PUBLIC_URL}/static/images/tiktok.png`}
              alt="x"
              style={{ height: '50px' }}
            />
          </a>
        </div>

        <div className="symbol">
          <a target="_blank" rel="noopener noreferrer" href="https://asmrchruch.bandcamp.com/">
            <img 
              src={`${process.env.PUBLIC_URL}/static/images/bandcamp.png`}
              alt="x"
              style={{ height: '70px' }}
            />
          </a>
        </div>

        <div className="symbol">
          <a target="_blank" rel="noopener noreferrer" href="https://discord.com/invite/wpwSjjnSs8">
            <img 
              src={`${process.env.PUBLIC_URL}/static/images/discord.png`}
              alt="x"
              style={{ height: '70px' }}
            />
          </a>
        </div>

        <div className="symbol">
          <a target="_blank" rel="noopener noreferrer" href="https://x.com/asmrchurch">
            <img 
              src={`${process.env.PUBLIC_URL}/static/images/x.png`}
              alt="x"
              style={{ height: '70px' }}
            />
          </a>
        </div>

        <div className="symbol">
          <a target="_blank" rel="noopener noreferrer" href="https://podcasts.apple.com/us/podcast/asmrキリスト教会/id1772229960">
            <img 
              src={`${process.env.PUBLIC_URL}/static/images/podcast.png`}
              alt="x"
              style={{ height: '50px' }}
            />
          </a>
        </div>

      </div>
    </div>
  );
}

export default Ad;
