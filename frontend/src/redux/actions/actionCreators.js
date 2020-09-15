import { ADD_ITEM_TO_CART, DELETE_ITEM_FROM_CART } from "./actionTypes";

function addItemToCart(item) {
  return {
    type: ADD_ITEM_TO_CART,
    payload: item,
  };
}

function deleteItemFromCart(item_id) {
  return {
    type: DELETE_ITEM_FROM_CART,
    payload: item_id,
  };
}
