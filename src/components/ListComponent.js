import React, { useState, useEffect } from 'react';
import './styles.css';
import '../blog.css';
import './NewsGrid.css';
import Header from '../components/Header';
import Footer from '../components/Footer';

function ListComponent({ type, title }) {
  const [articles, setArticles] = useState([]);
  const [articlesWithMeta, setArticlesWithMeta] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const postsPerPage = 12;

  useEffect(() => {
    fetch(`/static/markdown/${type}/list.json`)
      .then((response) => response.json())
      .then((data) => setArticles(data.articles))
      .catch((error) => console.error('Error fetching list:', error));
  }, [type]);

  // Fetch metadata for each article
  useEffect(() => {
    if (articles.length === 0) return;

    const fetchMetadata = async () => {
      const reversedArticles = articles.slice().reverse();
      const metaPromises = reversedArticles.map(async (article) => {
        try {
          const response = await fetch(`/static/markdown/${type}/${article.id}.md`);
          const text = await response.text();

          // Extract title (first H1)
          const titleMatch = text.match(/^#\s+(.+)$/m);
          const extractedTitle = titleMatch ? titleMatch[1] : 'タイトルなし';

          // Extract first image
          const imageMatch = text.match(/!\[.*?\]\((.*?)\)/);
          const image = imageMatch && imageMatch[1]
            ? imageMatch[1]
            : '/static/images/i4.jpg';

          // Extract description (first paragraph after title)
          const lines = text.split('\n');
          let description = '';
          let foundTitle = false;
          for (let line of lines) {
            if (line.startsWith('#')) {
              foundTitle = true;
              continue;
            }
            if (foundTitle && line.trim() && !line.startsWith('!') && !line.startsWith('[') && !line.startsWith('*')) {
              description = line.replace(/[*_`~[\]()]/g, '').substring(0, 100);
              break;
            }
          }

          return {
            ...article,
            title: extractedTitle,
            image,
            description
          };
        } catch (error) {
          console.error(`Error fetching metadata for ${article.id}:`, error);
          return {
            ...article,
            title: 'タイトルなし',
            image: '/static/images/i4.jpg',
            description: ''
          };
        }
      });

      const metaData = await Promise.all(metaPromises);
      setArticlesWithMeta(metaData);
    };

    fetchMetadata();
  }, [articles, type]);

  // Calculate the current articles to display
  const indexOfLastPost = currentPage * postsPerPage;
  const indexOfFirstPost = indexOfLastPost - postsPerPage;
  const currentArticles = articlesWithMeta.slice(indexOfFirstPost, indexOfLastPost);

  // Change page
  const nextPage = () => {
    if (currentPage < Math.ceil(articlesWithMeta.length / postsPerPage)) {
      setCurrentPage(currentPage + 1);
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  };

  const prevPage = () => {
    if (currentPage > 1) {
      setCurrentPage(currentPage - 1);
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  };

  // Set OG tags based on type
  const metaTitle = type === 'blog' ? 'ブログ - ASMRキリスト教会' : `${title} - ASMRキリスト教会`;
  const metaDescription = type === 'blog'
    ? 'ASMRキリスト教会のブログ記事一覧。聖書、信仰、日常について綴っています。'
    : `${title}の一覧ページです。`;
  const metaImage = type === 'blog'
    ? 'https://www.asmrchurch.com/static/images/c5.jpg'
    : 'https://www.asmrchurch.com/static/images/i4.jpg';
  const metaUrl = `https://www.asmrchurch.com/${type}`;

  return (
    <div>
      <Header
        title={metaTitle}
        description={metaDescription}
        url={metaUrl}
        image={metaImage}
      />
      <div className="news-container">
        <h1 className="news-title">{title}</h1>

        {/* Featured Article (Latest) */}
        {currentArticles.length > 0 && (
          <a href={`/${type}/${currentArticles[0].id}`} className="featured-article">
            <div
              className="featured-image"
              style={{ backgroundImage: `url(${currentArticles[0].image})` }}
            >
              <div className="featured-overlay">
                <span className="featured-date">{currentArticles[0].creationDate}</span>
                <h2 className="featured-title">{currentArticles[0].title}</h2>
                <p className="featured-description">{currentArticles[0].description}</p>
              </div>
            </div>
          </a>
        )}

        {/* Grid of Articles */}
        <div className="news-grid">
          {currentArticles.slice(1).map((article) => (
            <a
              key={article.id}
              href={`/${type}/${article.id}`}
              className="news-card"
            >
              <div
                className="news-card-image"
                style={{ backgroundImage: `url(${article.image})` }}
              />
              <div className="news-card-content">
                <span className="news-card-date">{article.creationDate}</span>
                <h3 className="news-card-title">{article.title}</h3>
                <p className="news-card-description">{article.description}</p>
              </div>
            </a>
          ))}
        </div>

        {/* Pagination controls */}
        <div className="pagination">
          <button onClick={prevPage} disabled={currentPage === 1} className="pagination-btn">
            ← 前へ
          </button>
          <span className="pagecount">
            {currentPage} / {Math.ceil(articlesWithMeta.length / postsPerPage)}
          </span>
          <button
            onClick={nextPage}
            disabled={currentPage === Math.ceil(articlesWithMeta.length / postsPerPage)}
            className="pagination-btn"
          >
            次へ →
          </button>
        </div>
      </div>
      <Footer />
    </div>
  );
}

export default ListComponent;

