import {
  ADD_ITEM_TO_CART,
  DELETE_ITEM_FROM_CART,
} from "../actions/actionTypes";

export default function cartReducer(state = [], action) {
  switch (action.type) {
    case ADD_ITEM_TO_CART:
      return [...state, action.payload];
    case DELETE_ITEM_FROM_CART:
      return state.filter((item) => item.id !== action.payload);
    default:
      return state;
  }
}
