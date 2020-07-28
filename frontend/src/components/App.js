import React from "react";
import ReactDOM from "react-dom";

export default function App() {
  return <h1>This is React test</h1>;
}

const container = document.getElementById("app");
ReactDOM.render(<App />, container);
