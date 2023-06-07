import React, { useState } from "react";
import LoginForm from "./forms/Login";
import RegisterForm from "./forms/Register";

export default function Auth() {
  //
  const [page, setPage] = useState("Login");

  const forms = {
    login: <LoginForm setPage={setPage} />,
    register: <RegisterForm setPage={setPage} />,
  };

  return (
    <div className="auth-layout">
      <div className="auth-pannel">
        <h1>{page}</h1>

        {forms[page.toLowerCase()]}

        {page == "Login" ? (
          <p>
            Don't have an account?{" "}
            <a onClick={() => setPage("Register")}>Register</a>
          </p>
        ) : (
          <p>
            Do you have an account?{" "}
            <a onClick={() => setPage("Login")}>Log in</a>
          </p>
        )}
      </div>
    </div>
  );
}
