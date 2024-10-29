import React, { useState, useEffect } from 'react';
import './App.css';
import QuoteDisplay from './components/QuoteDisplay';

function App() {
  const [quote, setQuote] = useState('');
  const [author, setAuthor] = useState('');

  // Fetching a random quote from Quotable API
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
