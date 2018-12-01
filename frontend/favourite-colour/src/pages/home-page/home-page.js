import React, {Component} from "react";
import { Redirect } from 'react-router';

import './home-page.css';
import $ from "jquery";

class HomePage extends Component {

    state = {
        navigate: false
    }


    addVote = (colour) => {
        $.ajax({
            async: false,
            url: "http://localhost:5001/vote",
            type: 'POST',
            data: {
                colour: colour,
            }
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
