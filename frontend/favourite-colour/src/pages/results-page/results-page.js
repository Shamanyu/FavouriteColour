import React, {Component} from "react";
import $ from 'jquery';

import './results-page.css';

class ResultsPage extends Component {

    constructor(props) {
        super(props);
        document.body.style.backgroundColor = this.fetchColour();
    }

    fetchColour = () => {
        var colour = "#FFFFFF";
        $.ajax({
            async: false,
            url: "http://localhost:5001/colour",
            type: 'GET',
            success: function(res) {
                colour = res;
            }
        });
        return colour;
    }

    render() {
        return(<div></div>);
    }


}

export default ResultsPage;
