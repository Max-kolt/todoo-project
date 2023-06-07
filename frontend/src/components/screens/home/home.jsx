import React, { useEffect, useState } from "react";
import { Button, TextField } from "@mui/material";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import DefaultTabs from "../../ui/tabs/tab";

export default function Home() {
  const [search, setSearch] = useState("");
  const [user, setUser] = useState({
    username: "user1",
    fname: "Nick",
    lname: "Kolosov",
  });
  const navigate = useNavigate();

  // useEffect(async () => {
  //   const token = `${localStorage.getItem(
  //     "auth_token_type"
  //   )} ${localStorage.getItem("auth_token")}`;

  //   await axios
  //     .get("http://127.0.0.1:8080/user/", { headers: { Authorization: token } })
  //     .then((responce) => {
  //       console.log(responce);
  //     })
  //     .catch((error) => {
  //       console.log(responce);
  //       navigate("/auth");
  //     });
  // });

  const logout = () => {
    localStorage.clear();
    navigate("/auth");
  };

  return (
    <>
      <div className="head">
        <TextField
          nChange={(event) => setSearch(event.target.value)}
          id="outlined-basic"
          placeholder="Search"
          variant="outlined"
        />
        <h1>Records</h1>
        <div className="profile">
          <h3>{user.username}</h3>
          <Button variant="outlined" onClick={logout}>
            log out
          </Button>
        </div>
      </div>
      <div className="main-layout">
        <h1>
          {user.fname} {user.lname}
        </h1>
        <div className="records-list">
          <DefaultTabs />
        </div>
      </div>
    </>
  );
}
