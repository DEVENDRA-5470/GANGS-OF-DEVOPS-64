import React from "react";
import RegisterUser from "./Components/RegisterUser";
import Account from "./Components/Accounts";
// import LoginUser from "./Components/LoginUser"; // optional
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./Components/Home";
import Navbar from "./Components/Navbar";

const App = () => {
  return (
    <Router>
      <div>
       {/* navbar */}
        <Navbar/>
      
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/register" element={<RegisterUser />} />
          <Route path="/account" element={<Account />} />
          
        </Routes>
      </div>
    </Router>
  );
};

export default App;
