import React from 'react';
import { Link } from 'react-router-dom';
import PayComponent from './PayComponent';

function Footer() {
  return (
    <div>
    <PayComponent />
    <footer style={{ textAlign: 'center', padding: '10px', fontSize: '14px', color: '#333' }}>
      <div style={{ marginBottom: '10px' }}>
        <Link to="/privacy" style={{ color: '#666', textDecoration: 'none', fontSize: '12px' }}>
          プライバシーポリシー
        </Link>
      </div>
      ASMRキリスト教会 all rights reserved.
    </footer>
    </div>
  );
}

export default Footer;
