import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Button, TextField } from "@mui/material";
import "axios";
import axios from "axios";

const RegisterForm = () => {
  const navigator = useNavigate();
  const [regInfo, setRegInfo] = useState({
    username: "",
    fname: "",
    lname: "",
    password: "",
  });

  // POST запрос на backend для создания пользователя
  // возвращает jwt токен
  const onSubmitHandler = async (event) => {
    event.preventDefault();
    await axios
      .post("http://127.0.0.1:8080/auth/register ", regInfo)
      .then((response) => {
        localStorage.setItem("auth_token", response.data.result.access_token);
        localStorage.setItem(
          "auth_token_type",
          response.data.result.token_type
        );
        navigator("/");
        window.location.reload();
      })
      .catch((error) => {
        alert(error.response.data.detail);
      });
  };

  //Запись в state данных полей
  const onChangeForm = (label, event) => {
    switch (label) {
      case "username":
        setRegInfo({ ...regInfo, username: event.target.value });
        break;
      case "fname":
        setRegInfo({ ...regInfo, fname: event.target.value });
        break;
      case "lname":
        setRegInfo({ ...regInfo, lname: event.target.value });
        break;
      case "password":
        setRegInfo({ ...regInfo, password: event.target.value });
        break;
    }
  };

  return (
    <form onSubmit={(event) => onSubmitHandler(event)}>
      <div className="form">
        <TextField
          onChange={(event) => onChangeForm("username", event)}
          label="Username"
          type="text"
          className="input"
          required
        />
        <TextField
          onChange={(event) => onChangeForm("fname", event)}
          label="First name"
          type="text"
          className="input"
          required
        />
        <TextField
          onChange={(event) => onChangeForm("lname", event)}
          label="Last name"
          type="text"
          className="input"
          required
        />
        <TextField
          onChange={(event) => onChangeForm("password", event)}
          label="Password"
          type="password"
          className="input"
          required
        />

        <Button variant="contained" type="submit" className="input">
          Log In
        </Button>
      </div>
    </form>
  );
};

export default RegisterForm;
