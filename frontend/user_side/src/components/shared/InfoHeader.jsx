import React from "react";
import { Link } from "react-router-dom";

function InfoHeader() {
  return (
    <nav className="navbar navbar-expand-lg navbar-light " id="infoHeader">
      <div className="container-fluid">
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#SMNavbar"
          aria-controls="SMNavbar"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>

        {/* <a className="navbar-brand" href="#">Navbar</a>
                <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#infoHeaderbtn" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button> */}

        <ul className="nav ms-auto justify-content-end" id="">
          <li className="nav-item">
            <a
              className="nav-link active disabled"
              disabled
              aria-current="page"
              href="/#"
            >
              Toll Number : 0800-0002003
            </a>
          </li>
          <li className="nav-item">
            <Link className="nav-link" to="login">
              SignIN
            </Link>
          </li>
          <li className="nav-item">
            <a className="nav-link" href="/#">
              SignUP
            </a>
          </li>
        </ul>
      </div>
    </nav>
  );
}

export default InfoHeader;
