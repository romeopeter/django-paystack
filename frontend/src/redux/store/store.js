import { createStore, applyMiddleware } from "redux";

import rootReducer from "../reducers/rootReducer";

import thunk from "redux-thunk";

import composeWithDevTools from "redux-devtools-extension";

const middleware = [thunk];

const initialState = {
  cart: [],
};

const store = createStore(
  rootReducer,
  initialState,
  composeWithDevTools(applyMiddleware(...middleware))
);

export default store;
