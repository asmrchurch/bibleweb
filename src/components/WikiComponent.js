import React, { useState, useEffect } from 'react';
import './styles.css';
import '../blog.css';
import Header from '../components/Header';
import Footer from '../components/Footer';

function WikiComponent({ type, title }) {
  const [articles, setArticles] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);

  useEffect(() => {
    fetch(`/static/markdown/${type}/list.json`)
      .then((response) => response.json())
      .then((data) => {
        const sortedArticles = data.articles.sort((a, b) => 
          a.title.localeCompare(b.title) // Sorting articles by title alphabetically
        );
        setArticles(sortedArticles);
      })
      .catch((error) => console.error('Error fetching list:', error));
  }, [type]);

  return (
    <div>
      <Header />
      <div className="blog-section-container">
        <h1 className="kirikantitle">{title}</h1>
        <div className="blog-list">
          {articles.map(({ id, title, creationDate }) => (
            <div key={id}>
              <div className="readarticle">
                <a className="ttz" href={`/${type}/${id}`}> {title} </a>
              </div>
            </div>
          ))}
        </div>
      </div>
      <Footer />
    </div>
  );
}

export default WikiComponent;

