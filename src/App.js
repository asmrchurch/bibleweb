import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './pages/Home';
import Bible from './pages/Bible';
import Blog from './pages/Blog';
import Article from './pages/Article';
import Wiki from './pages/Wiki';
import Actor from './pages/Actor';
import English from './pages/English';
import Sermon from './pages/Sermon';
import Caption from './pages/Caption';
import Manga from './pages/Manga';
import Pay from './pages/Pay';
import ListComponent from './components/ListComponent';
import WikiComponent from './components/WikiComponent';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/bible/:section" element={<Bible />} />
        <Route path="/blog" element={<ListComponent type="blog" title={`ブログ`}/>} />
        <Route path="/blog/:id" element={<Blog />} />
        <Route path="/actor/:id" element={<Actor />} />
        <Route path="/actor" element={<ListComponent type="actor" title={`声優図鑑`}/>} />
        <Route path="/wiki/:id" element={<Wiki />} />
        <Route path="/wiki" element={<WikiComponent type="wiki" title={`聖書ASMRウィキ`}/>} />
        <Route path="/english/:id" element={<English />} />
        <Route path="/english" element={<ListComponent type="english" title={`英語講座`}/>} />

        <Route path="/article/:id" element={<Article />} />
        <Route path="/article" element={<ListComponent type="article" title={`記事`}/>} />
        <Route path="/sermon/:id" element={<Sermon />} />
        <Route path="/manga/:id" element={<Manga />} />
        <Route path="/manga" element={<ListComponent type="manga" title={`漫画`}/>} />
        <Route path="/sermon" element={<ListComponent type="sermon" title={`説教`}/>} />
        <Route path="/caption" element={<Caption />} />
        <Route path="/pay" element={<Pay />} />
      </Routes>
    </Router>
  );
}

export default App;

