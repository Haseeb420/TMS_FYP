import React from "react";
import { useState, useEffect } from "react";
// import { Link } from "react-router-dom";
import axios from "axios";
import TMSHeader from "../shared/TMSHeader";
import PackageCard from "./PackageCard";
import TMSFooter from "../shared/TMSFooter";

var Packages = () => {
  const [packagesList, setPackagesList] = useState([]);

  useEffect(() => {
    async function fetchData() {
      try {
        let url = "http://127.0.0.1:8000/tms_api/packages_api";
        const resutl = await axios.get(url, {
          headers: {
            Authorization: "Token 3e6d228ed10d57a2061861cb109011aca43fb122",
          },
        });
        setPackagesList(resutl.data);
        console.log(resutl.data);
      } catch (err) {
        console.log(err);
      }
    }
    fetchData();
  }, []);

  return (
    <>
      <TMSHeader />
      <div className="container">
        <div className="row my-5">
          {packagesList.map((p) => (
            <>
              <PackageCard key={p.PackageId} packageObj={p} />
              <PackageCard key={4} packageObj={p} />
              <PackageCard key={5} packageObj={p} />
              <PackageCard key={6} packageObj={p} />
              <PackageCard key={7} packageObj={p} />
              <PackageCard key={8} packageObj={p} />
              <PackageCard key={9} packageObj={p} />
              <PackageCard key={10} packageObj={p} />
            </>
          ))}
        </div>
      </div>
      <TMSFooter />
    </>
  );
};

export default Packages;
