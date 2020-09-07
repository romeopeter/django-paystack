import React, { Fragment } from "react";
import ReactDOM from "react-dom";

import Home from "./store/Home";

import { BrowserRouter as Router, Route, Link, Switch } from "react-router-dom";

export default function App() {
  return <Home />;
}

const container = document.getElementById("app");
ReactDOM.render(<App />, container);
