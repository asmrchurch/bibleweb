import React, { useEffect, useState, useMemo } from 'react';
import { useSearchParams } from 'react-router-dom';
import Header from '../components/Header';
import Footer from '../components/Footer';
import './styles.css';
import './main.css';

function Seiroku() {
  const [searchParams, setSearchParams] = useSearchParams();
  const [type, setType] = useState('ja');

  // ★ YouTube 動画 ID を配列で管理
  const videoIds = useMemo(
    () => [
      'Jml_XWiIjUM',
      '3TaCxGKxkpg',
      'x9wowC6htIE',
      'WKhTQrIhVXk',
      'J_qVacRsqg4',
      'P92uvy7tMVU',
    ],
    []
  );

  useEffect(() => {
    let urlType = searchParams.get('type') || 'norm';
    if (!['norm', 'en'].includes(urlType)) {
      urlType = 'norm';
      setSearchParams({ type: 'norm' });
    }
    setType(urlType);
  }, [searchParams, setSearchParams]);

  return (
    <div className="body">
      <Header subon={true} />
      <div className="container2">
        <br />
        <div className="video-embed">
          {videoIds.map((id) => (
            <iframe
              key={id}
              width="100%"
              height="500"
              src={`https://www.youtube.com/embed/${id}`}
              title={`YouTube video ${id}`}
              frameBorder="0"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
              allowFullScreen
            />
          ))}
        </div>
      </div>
      <Footer />
    </div>
  );
}

export default Seiroku;
