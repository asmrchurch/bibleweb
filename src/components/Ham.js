import React, { useState, useEffect, useRef } from 'react';
import './Ham.css';

function Ham() {
  const [isOpen, setIsOpen] = useState(false);
  const menuRef = useRef(null);  // Use a ref to track the menu container

  const handleClick = () => {
    setIsOpen(!isOpen);
  };

  const handleOutsideClick = (e) => {
    // Close the menu if the click is outside the menu and the hamburger button
    if (menuRef.current && !menuRef.current.contains(e.target)) {
      setIsOpen(false);
    }
  };

  // Close the menu when clicking outside or a menu item is clicked
  useEffect(() => {
    if (isOpen) {
      document.addEventListener('mousedown', handleOutsideClick);
    } else {
      document.removeEventListener('mousedown', handleOutsideClick);
    }
    return () => {
      document.removeEventListener('mousedown', handleOutsideClick);
    };
  }, [isOpen]);

  // Function to close the menu when a link is clicked
  const handleLinkClick = () => {
    setIsOpen(false);
  };

  return (
    <div className="hamburger-menu" ref={menuRef}>
      <div className="hamburger" onClick={handleClick}>
        <div className={`line ${isOpen ? 'open' : ''}`}></div>
        <div className={`line ${isOpen ? 'open' : ''}`}></div>
        <div className={`line ${isOpen ? 'open' : ''}`}></div>
      </div>
      <nav className={`nav-menu ${isOpen ? 'open' : ''}`}>
        <ul>
          <li className="hmb"><a href="/" onClick={handleLinkClick}>Home</a></li>
          <li className="hmb"><a href="/article/2" onClick={handleLinkClick}>概要</a></li>
          <li className="hmb"><a href="https://note.com/asmrchurch/m/m1c9750805e96" onClick={handleLinkClick}>Blog</a></li>
          <li className="hmb"><a href="/sermon" onClick={handleLinkClick}>説教</a></li>
          <li className="hmb"><a href="/seiroku" onClick={handleLinkClick}>聖録CH</a></li>
          <li className="hmb"><a href="/qa" onClick={handleLinkClick}>Q&A</a></li>
          <li className="hmb"><a href="https://suzuri.jp/asmrchurch2" onClick={handleLinkClick}>SHOP</a></li>
        </ul>
      </nav>
    </div>
  );
}

export default Ham;
