import React from "react";
import TMSFooter from "../shared/TMSFooter";
import TMSHeader from "../shared/TMSHeader";
import LoginForm from "./LoginForm";

function LoginPage() {
  return (
    <>
      <TMSHeader />
      <div className="container">
        <div className="row my-5">
          <div className="col-4 mx-auto p-3 bg-white">
            <LoginForm />
          </div>
        </div>
      </div>
      <TMSFooter />
    </>
  );
}
export default LoginPage;
