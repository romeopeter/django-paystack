import { ADD_ITEM_TO_CART, DELETE_ITEM_FROM_CART } from "./actionTypes";

export function addItemToCart(item) {
  return {
    type: ADD_ITEM_TO_CART,
    payload: item,
  };
}

export function deleteItemFromCart(item_id) {
  return {
    type: DELETE_ITEM_FROM_CART,
    payload: item_id,
  };
}
