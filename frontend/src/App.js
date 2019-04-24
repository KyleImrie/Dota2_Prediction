import React, { Component } from 'react';
import './App.css';

import HeroPool from './components/HeroPool';
import RadiantHeroes from './components/RadiantHeroes';
import DireHeroes from './components/DireHeroes';

class App extends Component {

  state = {
    heroPool: [
      {
        id: 1,
        name: 'EarthShaker' 
      },
      {
        id: 2,
        name: 'Enchantress'
      },
      {
        id: 3,
        name: 'Sven'
      },
    ],
    radiantTeam : []
  }

  addHero = (name) => {
    this.setState({ })
  }
  render() {
    return (
      <div>
        <div className='rows'>
          <HeroPool heroPool={this.state.heroPool} addHero={this.addHero}/>
        </div>
        <RadiantHeroes />
        <DireHeroes />
      </div>
    );
  }
}

export default App;
