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
