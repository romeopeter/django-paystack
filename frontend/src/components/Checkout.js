import React, { Fragment } from "react";

import DocTitle from "./utilities/DocTitle";

export default function Checkout({
  match: {
    params: { product_id },
  },
  history,
}) {
  return (
    <Fragment>
      {/*HTML document title*/}
      <DocTitle title="Checkout" />

      <button onClick={() => history.push("/")}>Back</button>

      <h1>Checkout</h1>
      <span>Item id is {product_id}</span>
    </Fragment>
  );
}
