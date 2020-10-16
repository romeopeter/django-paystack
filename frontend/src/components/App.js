import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

// Redux
import { createStore } from "redux";
import { Provider } from "react-redux";
import store from "../redux/store/store";
import rootReducer from "../redux/reducers/rootReducer";

// Components
import Home from "./store/Home";
import Men from "./store/Men";
import Women from "./store/Women";
import Cart from "./store/Cart";

const container = document.getElementById("app");
ReactDOM.render(
  <Provider store={store}>
    <Router>
      <Route path="/" exact component={Home} />
      <Route path="/men" component={Men} />
      <Route path="/women" component={Women} />
      <Route path="/Cart" component={Cart} />
    </Router>
  </Provider>,
  container
);
