import React, { Component } from 'react';
import {BrowserRouter, Switch, Route} from 'react-router-dom';

import './App.css';
import HomePage from './pages/home-page';
import ResultsPage from './pages/results-page';

class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <Switch>
            <Route path="/" exact component={HomePage}/>
            <Route path="/results" exact component={ResultsPage}/>
        </Switch>
      </BrowserRouter>
    );
  }
}

export default App;
