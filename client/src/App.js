import { BrowserRouter as Router,Routes,Route } from  'react-router-dom';
// import React, { useState, useEffect } from "react";
import './App.css';
import Scanner from './components/Scan';
import Login from './components/Login';
import Header from './components/Header';
import Home from './components/Home';
import About from './components/About';
import Contact from './components/Contact';
// import Header from './components/Header';

function App() {
  return (
    <div className="App">
      <Router>
        <Header/>
        <Routes>
          <Route exact path="/" element={<Login/>}/>
          <Route exact path='/home' element={<Home/>}/>
          <Route exact path='/contact' element={<Contact/>}/>
          <Route exact path='/about' element={<About/>}/>
          <Route exact path="/scan" element={<Scanner/>}/>
        </Routes>
      </Router>
    </div>
  );
}

export default App;
