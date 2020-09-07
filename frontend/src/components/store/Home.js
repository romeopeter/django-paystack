import React, { Fragment, useEffect, useState } from "react";

import Layout from "./Layout";

import { Link } from "react-router-dom";
import SimpleCrypto from "simple-crypto-js";

// import bgImage from "./images/bgImage.jpg";

export default function Home() {
  return (
    <Layout>
      <div id="landing-page">
        <div id="home-title">
          <h1 className="text-5xl font-medium lead-tight mb-10">
            Fashionably Exurberant
          </h1>
          <hr className="border-1 border-red-600 w-50" />
        </div>
        <div id="home-image">
          <img src="" alt="home-image" />
        </div>
      </div>
    </Layout>
  );
}
