import React from 'react';
import './styles.css';

function Ad() {
  return (
    <div className="section ad">
      <h1></h1>

      <div>
        <div>
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
        </div>
      </div>
      
      <div className="">
        <a target="_blank" rel="noopener noreferrer" href="https://www.dlsite.com/home/work/=/product_id/RJ433352.html">
          <img 
            src={`${process.env.PUBLIC_URL}/static/images/dlsite.png`}
            alt="x" 
            style={{ height: '35px' }}
          />
        </a>
      </div>

      <div className="">
      <iframe
        width="100%"
        src="https://www.youtube.com/embed/videoseries?si=ZBTKC0dj3cqZi8o6&amp;list=PLDCOwaH2cXdbuMI9_DB3sfd3Bpp2JHFmr"
        title="YouTube video player"
        frameBorder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        referrerPolicy="strict-origin-when-cross-origin"
        allowFullScreen
      ></iframe>
      </div>

      <div className="">
      <iframe
        width="100%"
        src="https://www.youtube.com/embed/videoseries?si=-5p_8r09By3tOHtM&amp;list=PLKI5DIl1FM15uwG9QtAoeElYJrF43YyN9"
        title="YouTube video player"
        frameBorder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        referrerPolicy="strict-origin-when-cross-origin"
        allowFullScreen
      ></iframe>
      </div>

      <div className="">
        <iframe
        height="162"
        width="375"
        src="https://suzuri.jp/asmrchurch2/16625378/full-graphic-t-shirt/xl/white/embed"
        title="Suzuri Embed"
        frameBorder="0"
        allowFullScreen
      ></iframe>
      </div>
    </div>
  );
}

export default Ad;
