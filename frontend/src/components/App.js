import React, { Fragment } from "react";
import ReactDOM from "react-dom";

import Store from "./Store";
import Checkout from "./Checkout";

import { BrowserRouter as Router, Route, Link, Switch } from "react-router-dom";

export default function App() {
  return (
    <Router>
      <Fragment>
        <Switch>
          <Route path="/" exact component={Store} />
          {/*<Route path="/checkout/:product_id" component={Checkout} />*/}
        </Switch>
      </Fragment>
    </Router>
  );
}

const container = document.getElementById("app");
ReactDOM.render(<App />, container);
