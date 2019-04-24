import React, { Component } from 'react';

class HeroInPool extends Component {
  getThumbnail = () => {
    return (
      '/thumbnails/'+this.props.name+'.png'
    )
  }
  render() {
    const name = this.props.hero.name
    return (
      <button onClick={this.props.addHero.bind(this, name)}>
        <img src={this.getThumbnail()} alt='lol'></img>
      </button>
    )
  }
}

export default HeroInPool;
