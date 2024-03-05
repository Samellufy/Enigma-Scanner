import { BrowserRouter as Router,Routes,Route } from  'react-router-dom';
// import React, { useState, useEffect } from "react";
import './App.css';
import Scanner from './components/Scan';
import Login from './components/Login';
import Header from './components/Header';
import Home from './components/Home';
import About from './components/About';
import Contact from './components/Contact';
import Subscribe from './components/Subscribe';
import Payment from './components/Payment';
import Success from './components/Success';
import Chatbot from './Chatbot';
// import Header from './components/Header';

function App() {
  return (
    <div className="App">
      <Router>
        <Header/>
        <Routes>
          <Route exact path="/" element={<Login/>}/>
          <Route exact path='/home' element={<Home/>}/>
          <Route exact path='/payment' element={<Payment/>}/>
          <Route exact path='/contact' element={<Contact/>}/>
          <Route exact path='/about' element={<About/>}/>
          <Route exact path="/scan" element={<Scanner/>}/>
          <Route exact path='/subscribe' element={<Subscribe/>}/>
          <Route exact path='/success' element={<Success/>}/>
          <Route exact path='/chat' element={<Chatbot/>}/>
        </Routes>
      </Router>
    </div>
  );
}

export default App;
