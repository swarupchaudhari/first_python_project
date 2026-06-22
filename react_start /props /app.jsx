import React from 'react';
import Card from './components/Card';

const App = () => {
  return (
    <div className="parent">
      <Card
        user="Swarup"
        age={20}
        img="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=500"
      />

      <Card
        user="Sahil"
        age={21}
        img="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=500"
      />

      <Card
        user="Karan"
        age={17}
        img="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=500"
      />
    </div>
  );
};

export default App;