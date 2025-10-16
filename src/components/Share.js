import React from 'react';
import {
  FacebookShareButton,
  TwitterShareButton,
  EmailShareButton,
  RedditShareButton,
  LinkedinShareButton
} from 'react-share';
import {
  FacebookIcon,
  XIcon,
  EmailIcon,
  RedditIcon,
  LinkedinIcon
} from 'react-share';

// Custom Blogger Share Button
const BloggerShareButton = ({ url, title, text, image, children }) => {
  // Create content with image and text (max 5000 chars)
  const truncatedText = text && text.length > 5000 ? text.substring(0, 5000) + '...' : (text || '');

  // Build HTML content: image + text + link at bottom
  const imageTag = image ? `<img src="${image}" alt="${title}" style="max-width:100%;height:auto;"><br><br>` : '';
  const content = `${imageTag}${truncatedText}<br><br><a href="${url}">${url}</a>`;

  const bloggerUrl = `https://www.blogger.com/blog-this.g?u=${encodeURIComponent(url)}&n=${encodeURIComponent(title)}&t=${encodeURIComponent(content)}`;

  return (
    <a
      href={bloggerUrl}
      target="_blank"
      rel="noopener noreferrer"
      style={{ display: 'inline-block', cursor: 'pointer' }}
    >
      {children}
    </a>
  );
};

// Custom Blogger Icon
const BloggerIcon = ({ size = 32 }) => (
  <svg
    viewBox="0 0 24 24"
    width={size}
    height={size}
    style={{ display: 'block' }}
  >
    <rect width="24" height="24" fill="#FF5722" />
    <path
      d="M10.5 9h3c.28 0 .5.22.5.5s-.22.5-.5.5h-3c-.28 0-.5-.22-.5-.5s.22-.5.5-.5zm0 5h3c.28 0 .5.22.5.5s-.22.5-.5.5h-3c-.28 0-.5-.22-.5-.5s.22-.5.5-.5zm6.5-7h-2.5V5c0-1.1-.9-2-2-2h-4C7.9 3 7 3.9 7 5v4c0 1.1.9 2 2 2v1c0 1.1.9 2 2 2v3c0 1.1.9 2 2 2h4c1.1 0 2-.9 2-2V9c0-1.1-.9-2-2-2z"
      fill="white"
    />
  </svg>
);

const Share = ({title, url, text, image}) => {
  return (
    <div className="sharecontainer">
      <span className="tt"> 布教する: </span>
      <div className="share">

        {/* X (X) Share Button */}
        <TwitterShareButton url={url} title={title}>
          <XIcon size={32} round={false} />
        </TwitterShareButton>

        {/* Facebook Share Button */}
        <FacebookShareButton url={url} quote={title}>
          <FacebookIcon size={32} round={false} />
        </FacebookShareButton>

        {/* Email Share Button */}
        <EmailShareButton url={url} subject={title} body="Check this out:">
          <EmailIcon size={32} round={false} />
        </EmailShareButton>

        {/* Reddit Share Button */}
        <RedditShareButton url={url} title={title}>
          <RedditIcon size={32} round={false} />
        </RedditShareButton>

        {/* LinkedIn Share Button */}
        <LinkedinShareButton url={url} title={title} summary={title}>
          <LinkedinIcon size={32} round={false} />
        </LinkedinShareButton>

        {/* Blogger Share Button */}
        <BloggerShareButton url={url} title={title} text={text} image={image}>
          <BloggerIcon size={32} />
        </BloggerShareButton>
      </div>
    </div>
  );
};

export default Share;
