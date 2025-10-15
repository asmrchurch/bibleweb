import React, { useState, useEffect } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import './ChapterNavigation.css';

function ChapterNavigation({ htmlContent, currentChapter, onChapterClick }) {
  const navigate = useNavigate();
  const location = useLocation();
  const [chapters, setChapters] = useState([]);

  useEffect(() => {
    if (htmlContent) {
      // Parse HTML to find all chapter headings
      const parser = new DOMParser();
      const doc = parser.parseFromString(htmlContent, 'text/html');
      
      // First try Ruby version structure - look for div.chapter with numeric IDs
      let rubyChapterElements = doc.querySelectorAll('div.chapter[id]');
      let chapterList = [];
      
      if (rubyChapterElements.length > 0) {
        // Ruby version structure
        chapterList = Array.from(rubyChapterElements).map((elem) => {
          const id = elem.id;
          const number = parseInt(id);
          const h3 = elem.querySelector('h3.chapter');
          const text = h3 ? h3.textContent : `第${number}章`;
          return { id, number, text };
        });
      } else {
        // Normal version structure - look for div elements with numeric IDs and h3 children
        const normChapterElements = doc.querySelectorAll('div[id]');
        chapterList = Array.from(normChapterElements)
          .filter((elem) => {
            const id = elem.id;
            return /^\d+$/.test(id) && elem.querySelector('h3'); // Only divs with numeric IDs and h3 children
          })
          .map((elem) => {
            const id = elem.id;
            const number = parseInt(id);
            const h3 = elem.querySelector('h3');
            const text = h3 ? h3.textContent : `第${number}章`;
            return { id, number, text };
          });
      }
      
      setChapters(chapterList);
    }
  }, [htmlContent]);

  const scrollToChapter = (chapterId) => {
    // Check if we're on a verse-specific URL (e.g., /bible/genesis/1/1)
    const verseUrlPattern = /^\/bible\/[^/]+\/\d+\/\d+/;

    if (verseUrlPattern.test(location.pathname)) {
      // We're on a verse-specific URL, need to navigate back to book URL
      const bookPath = location.pathname.split('/').slice(0, 3).join('/');
      const searchParams = new URLSearchParams(location.search);
      navigate(`${bookPath}?${searchParams.toString()}`, { replace: true });

      // Wait for navigation, then scroll
      setTimeout(() => {
        const element = document.getElementById(chapterId);
        if (element) {
          const yOffset = -60;
          const y = element.getBoundingClientRect().top + window.pageYOffset + yOffset;
          window.scrollTo({ top: y, behavior: 'smooth' });
        }
      }, 100);
    } else {
      // Normal scroll behavior
      const element = document.getElementById(chapterId);
      if (element) {
        const yOffset = -60; // Offset for fixed header only
        const y = element.getBoundingClientRect().top + window.pageYOffset + yOffset;
        window.scrollTo({ top: y, behavior: 'smooth' });
      }
    }

    if (onChapterClick) {
      onChapterClick(chapterId);
    }
  };

  if (chapters.length === 0) {
    return null;
  }

  return (
    <div className="chapter-navigation">
      <div className="chapter-nav-container">
        <div className="chapter-buttons">
          {chapters.map((chapter) => (
            <button
              key={chapter.id}
              className={`chapter-btn ${currentChapter === chapter.id ? 'active' : ''}`}
              onClick={() => scrollToChapter(chapter.id)}
              title={chapter.text}
            >
              {chapter.number}
            </button>
          ))}
        </div>
      </div>
    </div>
  );
}

export default ChapterNavigation;