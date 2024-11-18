import React from 'react';
import PayComponent from './PayComponent';

function Footer() {
  return (
    <div>
    <PayComponent />
    <footer style={{ textAlign: 'center', padding: '10px', fontSize: '14px', color: '#333' }}>
      ASMRキリスト教会 all rights reserved.
    </footer>
    </div>
  );
}

export default Footer;
