import React from 'react';
import './styles.css';

function Ad() {
  return (
    <div className="section ad">
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

        <div className="symbol">
          <a target="_blank" rel="noopener noreferrer" href="https://note.com/asmrchurch">
            <img
              src={`${process.env.PUBLIC_URL}/static/images/note.png`}
              alt="note"
              style={{ height: '50px' }}
            />
          </a>
        </div>
      </div>
    </div>
  );
}

// AdIcons - Reusable icons component
export function AdIcons() {
  return (
    <div className="symbols">
      <div className="symbol">
        <a target="_blank" rel="noopener noreferrer" href="https://www.dlsite.com/home/work/=/product_id/RJ433352.html">
          <img
            src={`${process.env.PUBLIC_URL}/static/images/dlsite.png`}
            alt="dlsite"
            style={{ height: '50px' }}
          />
        </a>
      </div>

      <div className="symbol">
        <a target="_blank" rel="noopener noreferrer" href="https://www.youtube.com/@asmrchurch">
          <img
            src={`${process.env.PUBLIC_URL}/static/images/youtube.png`}
            alt="youtube"
            style={{ height: '80px' }}
          />
        </a>
      </div>

      <div className="symbol">
        <a target="_blank" rel="noopener noreferrer" href="https://www.pixiv.net/en/users/107379276">
          <img
            src={`${process.env.PUBLIC_URL}/static/images/pixiv.png`}
            alt="pixiv"
            style={{ height: '50px' }}
          />
        </a>
      </div>

      <div className="symbol">
        <a target="_blank" rel="noopener noreferrer" href="https://www.tiktok.com/@sexybible">
          <img
            src={`${process.env.PUBLIC_URL}/static/images/tiktok.png`}
            alt="tiktok"
            style={{ height: '50px' }}
          />
        </a>
      </div>

      <div className="symbol">
        <a target="_blank" rel="noopener noreferrer" href="https://asmrchruch.bandcamp.com/">
          <img
            src={`${process.env.PUBLIC_URL}/static/images/bandcamp.png`}
            alt="bandcamp"
            style={{ height: '70px' }}
          />
        </a>
      </div>

      <div className="symbol">
        <a target="_blank" rel="noopener noreferrer" href="https://discord.com/invite/wpwSjjnSs8">
          <img
            src={`${process.env.PUBLIC_URL}/static/images/discord.png`}
            alt="discord"
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
            alt="podcast"
            style={{ height: '50px' }}
          />
        </a>
      </div>

      <div className="symbol">
        <a target="_blank" rel="noopener noreferrer" href="https://note.com/asmrchurch">
          <img
            src={`${process.env.PUBLIC_URL}/static/images/note.png`}
            alt="note"
            style={{ height: '50px' }}
          />
        </a>
      </div>

      <div className="symbol">
        <a target="_blank" rel="noopener noreferrer" href="https://apps.apple.com/jp/app/%E5%8F%A3%E8%AA%9E%E8%A8%B3%E8%81%96%E6%9B%B8-asmr%E3%82%AD%E3%83%AA%E3%82%B9%E3%83%88%E6%95%99%E4%BC%9A/id6747372843">
          <img
            src={`${process.env.PUBLIC_URL}/static/images/ios.jpg`}
            alt="iOS App"
            style={{ width: '100%' }}
          />
        </a>
      </div>
    </div>
  );
}

export default Ad;
