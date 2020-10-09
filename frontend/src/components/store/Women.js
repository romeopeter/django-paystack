import React, { useEffect, useState } from "react";

import Layout from "./Layout";
import ProductUI from "./ProductUI";

export default function Women() {
  const [state, setState] = useState([]);

  useEffect(() => {
    fetch("/api/v1/products", {
      method: "GET",
      headers: {
        "Content-Type": "application/json;charset=utf-8",
      },
    })
      .then((response) => {
        if (response.ok) {
          return response.json();
        }
        return `HTTP-Error:${response.status}`;
      })
      .then((data) => {
        setState(data);
      });
  }, []);

  return (
    <Layout>
      <div className="mx-auto p-6">
        {/*Two columns*/}
        <div className="w-full md:flex mb-4 px-2">
          {state.length < 1
            ? "Loading"
            : state.map((product) => {
                if (product.sex === "F" || product.sex === "U") {
                  return <ProductUI product={product} key={product.id} />;
                }
              })}
        </div>
      </div>
    </Layout>
  );
}
