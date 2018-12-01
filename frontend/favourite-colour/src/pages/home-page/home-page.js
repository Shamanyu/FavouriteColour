import React, {Component} from "react";
import { Redirect } from 'react-router';

import './home-page.css';

class HomePage extends Component {
  state = {
    navigate: false
  }

  render() {
    const { navigate } = this.state;

    if (navigate) {
      return <Redirect to="/results" push={true} />
    }

    return (
        <div className="home-page">
            <div className="options" id="blue-option" onClick={() => this.setState({ navigate: true })}></div>
            <div className="options" id="yellow-option" onClick={() => this.setState({ navigate: true })}></div>
            <div className="options" id="red-option" onClick={() => this.setState({ navigate: true })}></div>
        </div>
    );
  }
}

export default HomePage;
