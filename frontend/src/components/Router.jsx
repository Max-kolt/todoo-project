import { BrowserRouter, Route, Routes } from "react-router-dom";
import Home from "./screens/home/home";
import Auth from "./screens/auth/auth";

const Router = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/auth" element={<Auth />} />

        <Route path="*" element={<h1>Page not found</h1>} />
      </Routes>
    </BrowserRouter>
  );
};

export default Router;
