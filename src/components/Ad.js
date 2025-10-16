import React from 'react';
import './styles.css';

function Ad() {
  return (
    <div className="section ad">
      <div className="">
        <div className="amensec">
        </div>
        <div>
          <stripe-buy-button
            buy-button-id="buy_btn_1QiEyXJrEFc0aoshZrg6uGA0"
            publishable-key="pk_live_51L77y9JrEFc0aoshDbT8faRDJBWQJjQTGvMb6jngK3GGGpMtIYf8omncPkMd8e0be0ZsfG2yEWaxYdMSlGSS9pgX00RNzmWvfw"
          >
          </stripe-buy-button>
        </div>
        <div>
          <a target="_blank" rel="noopener noreferrer" href="/characters">
            キャラクター紹介
          </a>
        </div>
        <div>
          <a href="/article/3">
            使徒信条
          </a>
        </div>
        <div>
          <a href="/article/4">
            主の祈り
          </a>
        </div>
        <div>
          <a target="_blank" rel="noopener noreferrer" href="/wiki">
            聖書ASMRウィキ
          </a>
        </div>
        <div>
          <a target="_blank" rel="noopener noreferrer" href="/article/1">
            いのちのASMR電話
          </a>
        </div>
        <div>
          <a target="_blank" rel="noopener noreferrer" href="/caption">
            コスパ名言集
          </a>
        </div>
        <div>
          <a target="_blank" rel="noopener noreferrer" href="https://www.kirishin.com/2024/05/19/66663/">
            メディア掲載: キリスト新聞様
          </a>
        </div>
      </div>

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
