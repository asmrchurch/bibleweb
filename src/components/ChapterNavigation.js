import React, { useState, useEffect } from 'react';
import './ChapterNavigation.css';

function ChapterNavigation({ htmlContent, currentChapter, onChapterClick }) {
  const [chapters, setChapters] = useState([]);

  useEffect(() => {
    if (htmlContent) {
      // Parse HTML to find all chapter headings
      const parser = new DOMParser();
      const doc = parser.parseFromString(htmlContent, 'text/html');
      
      // Find all h3 elements with chapter IDs
      const chapterElements = doc.querySelectorAll('h3[id^="c"]');
      const chapterList = Array.from(chapterElements).map((elem) => {
        const id = elem.id;
        const number = parseInt(id.substring(1));
        const text = elem.textContent;
        return { id, number, text };
      });
      
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