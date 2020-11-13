import React, { Fragment } from "react";

import { Link, withRouter } from "react-router-dom";
import { connect } from "react-redux";

function Layout({ children, cart }) {
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
            <i className="fab fa-github-alt"></i>
          </a>
        </i>
        <i>
          <a href="https://twitter.com/_romeopeter">
            <i className="fab fa-twitter"></i>
          </a>
        </i>
        <i>
          <a href="https://instagram.com/_romeopeter">
            <i className="fab fa-instagram"></i>
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
          <Link to="/cart">
            <i className="fas fa-shopping-cart"></i> {cart ? cart.length : 0}
          </Link>
        </div>
      </nav>
      <main>{children}</main>
      <footer>{footer}</footer>
    </Fragment>
  );
}

const mapStateToProps = (state) => {
  const { cart } = state;
  return { cart };
};

export default connect(mapStateToProps, null)(Layout);
