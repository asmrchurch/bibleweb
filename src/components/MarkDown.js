import React, { useState, useEffect } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import rehypeRaw from 'rehype-raw';
import '../blog.css';
import Share from './Share';

function MarkDown({ path, preview, type }) {
  const [markdown, setMarkdown] = useState('');
  const [title, setTitle] = useState('');
  const [firstImage, setFirstImage] = useState('');
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
        const lines = text.split('\n');
        const firstTitleLine = lines.find(line => line.startsWith('#'));

        if (firstTitleLine) {
          const firstTitle = firstTitleLine.replace('# ', '');
          setTitle(firstTitle);
        }

        // Extract first image
        const imageMatch = text.match(/!\[.*?\]\((.*?)\)/);
        if (imageMatch && imageMatch[1]) {
          setFirstImage(`https://www.asmrchurch.com${imageMatch[1]}`);
        } else {
          setFirstImage('https://www.asmrchurch.com/static/images/i4.jpg');
        }

        const dateLineIndex = lines.findIndex(line => /^\*\d{4}-\d{2}-\d{2}\*$/.test(line.trim()));
        let updatedText = lines.join('\n');

        if (updatedText.includes('[anna]')) {
          updatedText = updatedText.replace(/\[anna\]/g, 
            `<div class="author-inline">
              <span class="iconpos">
                <img src='/static/images/anna.jpg' alt="斎藤アンナ" class="author-inline-icon" />
              </span>
              <span class="author">By 斎藤アンナ</span>
            </div>`
          );
        } else if (updatedText.includes('[claude]')) {
          updatedText = updatedText.replace(/\[claude\]/g, 
            `<div class="author-inline">
              <span class="iconpos">
                <img src='/static/images/claude.png' alt="Claude" class="author-inline-icon" />
              </span>
              <span class="author">By Claude</span>
            </div>`
          );
        } else if (updatedText.includes('[sugano]')) {
          updatedText = updatedText.replace(/\[sugano\]/g, 
            `<div class="author-inline">
              <span class="iconpos">
                <img src='/static/images/sugano.jpg' alt="菅野契（管理人）" class="author-inline-icon" />
              </span>
              <span class="author">By 菅野契（管理人）</span>
            </div>`
          );
        } else {
          updatedText = updatedText.replace(
             /(\*\d{4}-\d{2}-\d{2}\*)/,
             (match) => {
               return `${match}<br>
         <div class="author-inline">
           <span class="iconpos">
             <img src='/static/images/chatgpt.png' alt="ChatGPT" class="author-inline-icon" />
           </span>
           <span class="author">By ChatGPT</span>
         </div>`;
             }
           );
        }

        if (dateLineIndex !== -1) {
          lines.splice(
            dateLineIndex + 1,
            0,
            updatedText
          );
        }

        setMarkdown(updatedText);
      })
      .catch((error) => {
        console.error(error);
        setMarkdown('');
      });
  }, [path]);

  const previewContent = preview ? markdown.split('\n').slice(0, 20).join('\n') : markdown;

  return (
    <div>
      <div className={`${type === 'manga' ? 'manga' : 'blog-section'}`}>
        <ReactMarkdown
          children={previewContent}
          remarkPlugins={[remarkGfm]}
          rehypePlugins={[rehypeRaw]}
          skipHtml={false}
          components={{
            div: ({ node, ...props }) => <div {...props} />,
            img: ({ node, ...props }) => <img {...props} />,
            a: ({ node, href, children, ...props }) => {
              // Check if this is the YouTube channel link
              if (href === 'https://youtube.com/@asmrchurch' || href === 'http://youtube.com/@asmrchurch') {
                return (
                  <a href={href} target="_blank" rel="noopener noreferrer" {...props} className="youtube-thumbnail-link">
                    <img
                      src="/static/images/thumbnail.png"
                      alt="YouTube Channel"
                      className="youtube-thumbnail"
                    />
                  </a>
                );
              }
              // Default link rendering
              return <a href={href} {...props}>{children}</a>;
            },
          }}
        />
      </div>

      {/* Share Section */}
      {!preview && (
        <Share
          title={`【ASMRキリスト教会】${title} @asmrchurch #聖書 #ASMR #キリスト教`}
          url={url}
          text={markdown}
          image={firstImage}
        />
      )}
    </div>
  );
}

export default MarkDown;
