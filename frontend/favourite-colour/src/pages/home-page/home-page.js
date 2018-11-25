import React, {Component} from "react";

import './home-page.css';

class HomePage extends Component {
  render() {
    return (
        <div className="home-page">
            <div className="options" id="blue-option"></div>
            <div className="options" id="yellow-option"></div>
            <div className="options" id="red-option"></div>
        </div>
    );
  }
}

export default HomePage;
