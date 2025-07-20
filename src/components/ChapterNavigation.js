import React, { useState, useEffect } from 'react';
import './ChapterNavigation.css';

function ChapterNavigation({ htmlContent, currentChapter, onChapterClick }) {
  const [chapters, setChapters] = useState([]);

  useEffect(() => {
    if (htmlContent) {
      // Parse HTML to find all chapter headings
      const parser = new DOMParser();
      const doc = parser.parseFromString(htmlContent, 'text/html');
      
      // Find all h3 elements with chapter IDs (normal version)
      let chapterElements = doc.querySelectorAll('h3[id^="c"]');
      let chapterList = [];
      
      if (chapterElements.length > 0) {
        // Normal version structure
        chapterList = Array.from(chapterElements).map((elem) => {
          const id = elem.id;
          const number = parseInt(id.substring(1));
          const text = elem.textContent;
          return { id, number, text };
        });
      } else {
        // Ruby version structure - look for div.chapter with numeric IDs
        const rubyChapterElements = doc.querySelectorAll('div.chapter[id]');
        chapterList = Array.from(rubyChapterElements).map((elem) => {
          const id = elem.id;
          const number = parseInt(id);
          const h3 = elem.querySelector('h3.chapter');
          const text = h3 ? h3.textContent : `第${number}章`;
          return { id, number, text };
        });
      }
      
      setChapters(chapterList);
    }
  }, [htmlContent]);

  const scrollToChapter = (chapterId) => {
    const element = document.getElementById(chapterId);
    if (element) {
      const yOffset = -60; // Offset for fixed header only
      const y = element.getBoundingClientRect().top + window.pageYOffset + yOffset;
      window.scrollTo({ top: y, behavior: 'smooth' });
      if (onChapterClick) {
        onChapterClick(chapterId);
      }
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