import React, { Fragment, useEffect, useState } from "react";

import { Link } from "react-router-dom";

import DocTitle from "./utilities/DocTitle";

export default function Store() {
  const [state, setState] = useState([]);
  const [carts, setCarts] = useState([]);

  useEffect(() => {
    fetch("/api/products/", {
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

  useEffect(() => {
    // console.log(carts);
    // Send data to backend
  }, [carts]);

  const addProductToCart = (
    event,
    productID,
    productName,
    productPrice,
    productImage
  ) => {
    const cartItem = {
      productID: productID,
      productName: productName,
      productPrice: productPrice,
      productImage: productImage,
    };

    if (!carts.some((cartItem) => cartItem.productID === productID)) {
      setCarts((prevCarts) => [...prevCarts, cartItem]);
      event.target.textContent = "Added To Cart";
    }
  };

  return (
    <Fragment>
      {/*HTML document title*/}
      <DocTitle title="Store"></DocTitle>

      <div className="mx-auto p-6">
        <div className="w-full lg:max-w-full mt-30 mb-10">
          <h1 className="font-bold text-center text-xl text-gray-600 lead-tight p-5 Product-header">
            BUY LUXURY FASHION PRODUCTS
          </h1>
          <div className="cart"></div>
        </div>

        {/*Two columns*/}
        <div className="w-full md:flex mb-4 px-2">
          {state.length < 1
            ? "Loading"
            : state.map((product) => (
                <div className="w-full md:w-1/2 mr-2" key={product.id}>
                  <div className="rounded overflow-hidden shadow-md">
                    <img
                      className="w-full h-64"
                      src={product.image}
                      alt={product.name}
                    />
                    <div className="px-6 py-4">
                      <h1 className="font-bold text-xl mb-2">{product.name}</h1>
                      <p className="text-gray-700 text-base">
                        {product.description}
                      </p>
                    </div>
                    <div className="px-6 py-4 mb-2">
                      <span className="inline-block bg-green-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2">
                        {`₦${product.price}`}
                      </span>
                    </div>
                    <div className="px-6 py-4">
                      <button
                        onClick={() =>
                          addProductToCart(
                            event,
                            product.id,
                            product.name,
                            product.price,
                            product.image
                          )
                        }
                        className="block w-full text-center bg-green-600 hover:bg-green-500 text-white px-4 py-2"
                      >
                        Add To Cart
                      </button>
                    </div>
                  </div>
                </div>
              ))}
        </div>
      </div>
    </Fragment>
  );
}
