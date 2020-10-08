import React from "react";
import ReactDOM from "react-dom";

import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

import { Provider } from "react-redux";
import { createStore } from "redux";
import rootReducer from "../redux/reducers/rootReducer";

import Home from "./store/Home";
import Men from "./store/Men";
import Women from "./store/Women";

export default function App() {
  return <Home />;
}

const container = document.getElementById("app");
ReactDOM.render(
  <Provider store={createStore(rootReducer)}>
    <Router>
      <Route path="/" exact component={Home} />
      <Route path="/men" component={Men} />
      <Route path="/women" component={Women} />
    </Router>
  </Provider>,
  container
);
