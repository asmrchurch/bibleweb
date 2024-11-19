import React, { useState, useEffect } from 'react';
import './styles.css';
import '../blog.css';
import Header from '../components/Header';
import Footer from '../components/Footer';
import MarkDown from '../components/MarkDown';

function ListComponent({ type, title }) {
  const [articles, setArticles] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const postsPerPage = 5;

  useEffect(() => {
    fetch(`/static/markdown/${type}/list.json`)
      .then((response) => response.json())
      .then((data) => setArticles(data.articles))
      .catch((error) => console.error('Error fetching list:', error));
  }, [type]);

  // Calculate the current articles to display
  const indexOfLastPost = currentPage * postsPerPage;
  const indexOfFirstPost = indexOfLastPost - postsPerPage;
  const currentArticles = articles.slice().reverse().slice(indexOfFirstPost, indexOfLastPost);

  // Change page
  const nextPage = () => {
    if (currentPage < Math.ceil(articles.length / postsPerPage)) {
      setCurrentPage(currentPage + 1);
    }
  };

  const prevPage = () => {
    if (currentPage > 1) {
      setCurrentPage(currentPage - 1);
    }
  };

  return (
    <div>
      <Header />
      <div className="blog-section-container">
        <h1 class="kirikantitle">{title}</h1>
        <hr />
        <div className="blog-list">
          {currentArticles.map((id) => (
            <div key={id}>
              <MarkDown path={`/${type}/${id}`} preview={true} type={type}/>
              <div className="readarticle">
                  <a className="ttz" href={`/${type}/${id}`}> 続きを読む </a>
              </div>
              <hr />
            </div>
          ))}
        </div>
        {/* Pagination controls */}
        <div className="pagination">
          <button onClick={prevPage} disabled={currentPage === 1}>
           ← 
          </button>
          <span className="pagecount">{currentPage} / {Math.ceil(articles.length / postsPerPage)}</span>
          <button onClick={nextPage} disabled={currentPage === Math.ceil(articles.length / postsPerPage)}>
          →
          </button>
        </div>
      </div>
      <Footer />
    </div>
  );
}

export default ListComponent;
