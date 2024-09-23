import React, { useState, useEffect } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import '../blog.css';
import Share from './Share';

function MarkDown({ path, preview, type }) {
  const [markdown, setMarkdown] = useState('');
  const [title, setTitle] = useState('');
  const url = `https://www.asmrchurch.com${path}`;

  useEffect(() => {
    fetch(`/static/markdown${path}.md`)
      .then((response) => {
        if (response.ok) {
          return response.text();
        } else {
          throw new Error('Markdown file not found');
        }
      })
      .then((text) => {
        setMarkdown(text);

        const firstTitleLine = text.split('\n').find(line => line.startsWith('#'));
        if (firstTitleLine) {
          const firstTitle = firstTitleLine.replace('# ', ''); // Strip leading "# "
          setTitle(firstTitle);
        }
      })
      .catch((error) => {
        console.error(error);
        setMarkdown('# 404 Not Found\nThe requested markdown file could not be found.');
      });
  }, [path]);

  // If preview mode is on, only show the first three lines
  const previewContent = preview ? markdown.split('\n').slice(0, 10).join('\n') : markdown;

  return (
    <div>
      <div className={`${type === 'manga' ? 'manga' : 'blog-section'}`}>
        <ReactMarkdown children={previewContent} remarkPlugins={[remarkGfm]} />
      </div>
      {/* Show the Share component only if it's not in preview mode */}
      {!preview && (
        <Share title={`【ASMRキリスト教会】${title} @asmrchurch #聖書 #ASMR #キリスト教`} url={url} />
      )}
    </div>
  );
}

export default MarkDown;
