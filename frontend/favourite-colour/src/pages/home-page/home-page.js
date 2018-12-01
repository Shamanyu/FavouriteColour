import React, {Component} from "react";
import { Redirect } from 'react-router';

import './home-page.css';

class HomePage extends Component {
    state = {
        navigate: false
    }

    constructor(props) {
        super(props);
        this.addVote = this.addVote.bind(this);
    }

    addVote = (colour) => {
        fetch('http://localhost:5001/vote', {
          method: 'POST',
          headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
          },
          body: JSON.stringify({
                colour: colour,
          })
        });
        this.setState({ navigate: true });
    }

    render(){
        const { navigate } = this.state;

        if (navigate) {
            return <Redirect to="/results" push={true} />
        }

        return (
            <div className="home-page">
                <div className="options" id="blue-option" onClick={this.addVote.bind(this, 'blue')}></div>
                <div className="options" id="yellow-option" onClick={this.addVote.bind(this, 'yellow')}></div>
                <div className="options" id="red-option" onClick={this.addVote.bind(this, 'red')}></div>
            </div>
        );
    }
}

export default HomePage;
