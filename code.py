npx create-react-app daily-motivation
cd daily-motivation
npm start
import React, { useState, useEffect } from 'react';
import './App.css';
import QuoteDisplay from './components/QuoteDisplay';

function App() {
  const [quote, setQuote] = useState('');
  const [author, setAuthor] = useState('');

  // Fetching quote from API
  useEffect(() => {
    fetchQuote();
  }, []);

  const fetchQuote = async () => {
    try {
      const response = await fetch('https://api.quotable.io/random');
      const data = await response.json();
      setQuote(data.content);
      setAuthor(data.author);
    } catch (error) {
      console.error('Error fetching the quote:', error);
    }
  };

  return (
    <div className="App">
      <h1>Daily Motivational Quote</h1>
      <QuoteDisplay quote={quote} author={author} />
      <button onClick={fetchQuote}>Get Another Quote</button>
    </div>
  );
}

export default App;
import React from 'react';

function QuoteDisplay({ quote, author }) {
  return (
    <div>
      <p>"{quote}"</p>
      <p>- {author}</p>
    </div>
  );
}

export default QuoteDisplay;
