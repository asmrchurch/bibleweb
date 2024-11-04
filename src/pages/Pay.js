import React, { useState, useEffect } from "react";
import Header from '../components/Header';
import PayComponent from '../components/PayComponent';

export default function Pay() {
      
  return (
      <div>
      <Header subon={true} />
      <PayComponent />
      </div>
  )
}
