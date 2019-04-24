import React, { Component } from 'react';
import HeroInPool from './HeroInPool';

class HeroPool extends Component {
  render() {
    return this.props.heroPool.map((hero) => (
        <div className='row'>
            <HeroInPool key={hero.id} name={hero.name} hero={hero} addHero={this.props.addHero}/>
        </div>
    ))
  }
}

export default HeroPool;
