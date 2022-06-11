import React from "react";
import Navbar from "./NavBar";
import tms_logo from "../../assets/logo/1.png";
import InfoHeader from "./InfoHeader";
import TitleHeader from "./TitleHeader";
import SMNavbar from "./SMNavbar";
function TMSHeader() {
  return (
    <>
      <InfoHeader />
      <SMNavbar />
      <TitleHeader />
      <Navbar logoName={tms_logo} />
    </>
  );
}

export default TMSHeader;
