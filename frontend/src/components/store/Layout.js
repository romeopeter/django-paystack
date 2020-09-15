import React, { Fragment } from "react";

export default function Layout({ children }) {
  const footer = (
    <div className="text-center text-md p-5 shadow-sm" id="creator-credit">
      <h4>
        Created by <a href="#">Romeo Peter</a>
      </h4>
      <div id="contact-icon">
        <i>
          <a href="https://upwork.com/RomeoPeter">UpWork</a>
        </i>
        <i>
          <a href="https://gitub.com/Romeo-Peter">Github</a>
        </i>
        <i>
          <a href="https://twitter.com/_romeopeter">Twitter</a>
        </i>
        <i>
          <a href="https://instagram.com/_romeopeter">Instagram</a>
        </i>
      </div>
    </div>
  );

  return (
    <Fragment>
      <nav>
        <h1 id="logo" className="font-bold text-md text-black lead-tight mb-5">
          <a href="/">Showroom</a>
        </h1>
        <ul>
          <li>Men</li>
          <li>Women</li>
        </ul>
        <div className="cart">
          {/*<i class="fas fa-shopping-cart"></i>*/}
          Carts 0
        </div>
      </nav>
      <main>{children}</main>
      <footer>{footer}</footer>
    </Fragment>
  );
}
