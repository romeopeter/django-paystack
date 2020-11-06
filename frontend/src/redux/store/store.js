import { createStore, applyMiddleware, compose } from "redux";

import rootReducer from "../reducers/rootReducer";

import thunk from "redux-thunk";

import { composeWithDevTools } from "redux-devtools-extension";

const middleware = [thunk];

const initialState = {
  cart: [],
};

const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
const store = createStore(
  rootReducer,
  initialState,
  composeWithDevTools(applyMiddleware(...middleware))
);

export default store;
