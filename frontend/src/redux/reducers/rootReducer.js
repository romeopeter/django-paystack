import { combineReducers } from "redux";

import cartReducer from "./cartReducer";

const rootReducer = combineReducers({
  cart: cartReducer,
});

console.log(rootReducer);

export default rootReducer;
