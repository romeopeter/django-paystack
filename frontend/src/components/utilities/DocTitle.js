import React from "react";
import PropTypes from "prop-types";

const DocTitle = (props) => {
  // HTML document title
  const docTitle = `${props.title} | Django payment`;
  document.title = docTitle;

  return null;
};

DocTitle.propTypes = {
  title: PropTypes.string.isRequired,
};

export default DocTitle;
