import React, { useEffect, useState } from "react";

import { withRouter } from "react-router-dom";
import { connect } from "react-redux";

import { addItemToCart } from "../../redux/actions/actionCreators";

function ProductUI({ product, addItemToCart }) {
  const [state, setState] = useState([]);

  useEffect(() => {
    const getCookie = (name) => {
      let cookieValue = null;

      if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let cookie of cookies) {
          const aCookie = cookie.trim();

          // Check cookie name match
          if (aCookie.substring(0, name.length + 1) === name + "=") {
            cookieValue = decodeURIComponent(
              aCookie.substring(name.length + 1)
            );
            break;
          }
        }
      }

      return cookieValue;
    };

    fetch("/carts/", {
      headers: {
        "Content-Type": "application/json;charset=utf-8",
        "X-CSRFToken": getCookie("csrftoken"),
      },
      method: "POST",
      body: state.length === 0 ? "No Cart" : JSON.stringify(state),
      mode: "same-origin",
    })
      .then((res) => {
        if (res.ok === 200) {
          console.log(res.json());
        }
      })
      .catch((err) => {
        throw new Error(err);
      });
  }, [state]);

  const addToCart = (
    event,
    productID,
    productName,
    productPrice,
    productImage
  ) => {
    const cartItems = {
      productID: productID,
      productName: productName,
      productPrice: productPrice,
      productImage: productImage,
    };

    // Add cart item to store (redux store)
    // addItemToCart(cartItems);
    console.log(cartItems);
  };

  return (
    <div className="w-full md:w-1/2 mr-2">
      <div className="rounded overflow-hidden shadow-md">
        <img className="w-full h-64" src={product.image} alt={product.name} />
        <div className="px-6 py-4">
          <h1 className="font-bold text-xl mb-2">{product.name}</h1>
          <p className="text-gray-700 text-base">{product.description}</p>
        </div>
        <div className="px-6 py-4 mb-2">
          <span className="inline-block bg-green-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2">
            {`₦${product.price}`}
          </span>
        </div>
        <div className="px-6 py-4">
          <button
            onClick={() =>
              addToCart(
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
  );
}

export default withRouter(
  connect(null, { addItemToCart: addItemToCart })(ProductUI)
);
