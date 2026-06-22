import React from 'react';
import Card from './components/Card';

const App = () => {
  return (
    <div className="parent">
      <Card user="Swarup" age={20} />
      <Card user="Sahil" age={21} />
      <Card user="Karan" age={17} />
    </div>
  );
};

export default App;