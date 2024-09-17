import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './pages/Home';
import Bible from './pages/Bible';
import Blog from './pages/Blog';
import Sermon from './pages/Sermon';
import Caption from './pages/Caption';
import Love from './pages/Love';
import ListComponent from './components/ListComponent';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/bible/:section" element={<Bible />} />
        <Route path="/blog" element={<ListComponent type="blog" title={`ブログ`}/>} />
        <Route path="/blog/:id" element={<Blog />} />
        <Route path="/sermon/:id" element={<Sermon />} />
        <Route path="/love/:id" element={<Love />} />
        <Route path="/love" element={<ListComponent type="love" title={`恋愛講座`}/>} />
        <Route path="/sermon" element={<ListComponent type="sermon" title={`説教`}/>} />
        <Route path="/caption" element={<Caption />} />
      </Routes>
    </Router>
  );
}

export default App;

