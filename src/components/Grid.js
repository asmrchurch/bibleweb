import React from "react";
import Header from '../components/Header';
import Footer from '../components/Footer';

const GridComponent = ({ title, data }) => {
  return (
    <div>
      <Header />
      <div className="gridtitlepad">{title}</div>
      <h1 className="gridtitle">{title}</h1>
      <div className="gridbox">
        {data.map((item) => {
          const imgSrc = item.image
            ? `/static/images/chars/${item.image}`
            : "/static/images/chars/default.jpg";

          return (
            <div key={item.id} className="grid-object">
              <img src={imgSrc} alt={item.title} className="icon-1" />
              <div className="grid-text">
                <h3 className="grid-text-title">{item.title}</h3>
                <p className="grid-text-description">{item.description}</p>
              </div>
            </div>
          );
        })}
      </div>
      <Footer />
    </div>
  );
};

export default GridComponent;
