import React from "react";
import { Link } from "react-router-dom";
function NavBar(props) {
  return (
    <nav className="navbar d-sm-none d-md-block  navbar-expand-lg navbar-dark NavBar">
      {/* <a className="navbar-brand" href="/#">
          <img src={props.logoName} alt="malik" className="tms_logo" />
        </a> */}
      <div className="collapse navbar-collapse" id="navbarSupportedContent">
        <ul className="navbar-nav mx-auto mb-2 mb-lg-0">
          <li className="nav-item">
            <a className="nav-link active" aria-current="page" href="/#">
              Home
            </a>
          </li>
          <li className="nav-item">
            <Link className="nav-link" to="/packages">
              Packages
            </Link>
          </li>
          <li className="nav-item">
            <Link className="nav-link" to="/about">
              About US
            </Link>
          </li>
          <li className="nav-item">
            <a className="nav-link" href="/#">
              Contact US
            </a>
          </li>

          <li className="nav-item">
            <a className="nav-link" href="/#">
              Privact Policy
            </a>
          </li>
        </ul>
      </div>
    </nav>
  );
}

export default NavBar;
