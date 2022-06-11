import React from "react";
import { FaUserCircle } from "react-icons/fa";
function TMSFooter() {
  return (
    <div className="container-fluid footer">
      <div className="row">
        <div className="col-6 mx-auto">
          <h6 className="text-center">Royal Travelss</h6>
        </div>
      </div>
      <div className="row">
        <div className="col-12">
          <div className="container">
            <div className="row">
              <div className="col-3 offset-1 section-01">
                <h5>Locations</h5>
                <hr />
                <ul>
                  <li>Azad Kashmir</li>
                  <li>Hunza / Gilgit</li>
                  <li>Naran / Kagan</li>
                  <li>Balochistan </li>
                  <li>Swat </li>
                  <li>Nathia Gali </li>
                  <li>Islamabad</li>
                  <li>Khyber Pakhtunkhwa</li>
                  <li>Karachi</li>
                  <li>Lahore</li>
                </ul>
              </div>
              <div className="col-3 offset-1 section-02">
                <h5>Packages</h5>
                <hr />
                <ul>
                  <li>Single Person</li>
                  <li>Family Tour</li>
                  <li>Friends Packages</li>
                </ul>
              </div>
              <div className="col-3 offset-1 section-03">
                <h5>Keep in Tocuh with us</h5>
                <FaUserCircle />

                <hr />
              </div>
            </div>
            <hr />
            <p className="text-center cc">copyright@ Royal Travels 2022</p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default TMSFooter;
