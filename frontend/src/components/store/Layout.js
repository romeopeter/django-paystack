import React, { Fragment } from "react";

import { Link } from "react-router-dom";

export default function Layout({ children }) {
  const footer = (
    <div className="text-center text-md p-5 shadow-sm" id="creator-credit">
      <h4>
        Created by <a href="https://romeopeter.com">Romeo Peter</a>
      </h4>
      <div id="contact-icon">
        <i>
          <a href="https://upwork.com/RomeoPeter">
            <i>UpWork</i>
          </a>
        </i>
        <i>
          <a href="https://gitub.com/Romeo-Peter">
            <i class="fab fa-github-alt"></i>
          </a>
        </i>
        <i>
          <a href="https://twitter.com/_romeopeter">
            <i class="fab fa-twitter"></i>
          </a>
        </i>
        <i>
          <a href="https://instagram.com/_romeopeter">
            <i class="fab fa-instagram"></i>
          </a>
        </i>
      </div>
    </div>
  );

  return (
    <Fragment>
      <nav>
        <h1 id="logo" className="font-bold text-md text-black lead-tight mb-5">
          <Link to="/">Showroom</Link>
        </h1>
        <ul>
          <li>
            <Link to="/men">Men</Link>
          </li>
          <li>
            <Link to="/women">Women</Link>
          </li>
        </ul>
        <div className="cart">
          {/*<i className="fas fa-shopping-cart"></i>*/}
          <Link to="/checkout">Carts 0</Link>
        </div>
      </nav>
      <main>{children}</main>
      <footer>{footer}</footer>
    </Fragment>
  );
}
