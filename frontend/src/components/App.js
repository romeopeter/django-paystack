import React from "react";
import ReactDOM from "react-dom";

import { Provider } from "react-redux";
import { createStore } from "redux";
import rootReducer from "../redux/reducers/rootReducer";

import Home from "./store/Home";

import { BrowserRouter as Router, Route, Link, Switch } from "react-router-dom";

export default function App() {
  return <Home />;
}

const container = document.getElementById("app");
ReactDOM.render(
  <Provider store={createStore(rootReducer)}>
    <App />
  </Provider>,
  container
);
