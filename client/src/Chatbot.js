// Chatbot.js

import React, { useState } from 'react';
import axios from 'axios';
import './Chatbot.css'; // Import CSS file for styling

const Chatbot = () => {
  const [userInput, setUserInput] = useState('');
  const [chats, setChats] = useState([]);

  const handleChange = (e) => {
    setUserInput(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const { data } = await axios.post('http://localhost:5000/chat', {
        user_input: userInput
      });
      const newChats = [...chats, { user: userInput, bot: data.response }];
      setChats(newChats);
      setUserInput(''); // Clear input after submission
    } catch (error) {
      console.error('Error fetching response:', error);
    }
  };

  return (
    <div className="chatbot-container">
      <div className="chatbot-chat">
        {chats.map((chat, index) => (
          <div key={index}>
            <div className="chatbot-user">{chat.user}</div>
            <div className="chatbot-response">{chat.bot}</div>
          </div>
        ))}
      </div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={userInput}
          onChange={handleChange}
          placeholder="Type your message here..."
          className="chatbot-input"
        />
        <button type="submit" className="chatbot-button">Send</button>
      </form>
        {/* {response && <p>{response}</p>} */}
    </div>
  );
};

export default Chatbot;
