import React, { Component } from 'react';
import {BrowserRouter, Switch, Route} from 'react-router-dom';

import './App.css';
import HomePage from './pages/home-page';
import ResultsPage from './pages/results-page';
import Error404Page from './pages/error-404-page';

class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <Switch>
            <Route path="/" exact component={HomePage}/>
            <Route path="/results" exact component={ResultsPage}/>
            <Route path component={Error404Page}/>
        </Switch>
      </BrowserRouter>
    );
  }
}

export default App;
