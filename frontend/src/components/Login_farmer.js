import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import './login.css';

const Login_farmer= () => {
//   const [formData, setFormData] = useState({
//     email: "",
//     password: "",
//     role: "",
//   });

//   const handleChange = (e) => {
//     const { name, value } = e.target;
//     setFormData({
//       ...formData,
//       [name]: value,
//     });
//   };

//   const handleSubmit = (e) => {
//     e.preventDefault();

  return (
    <div className="login-container">
      <h2 className="login-title">Login Page</h2>
      <form>
        <div>
          <label className="login-label">Email:</label>
          <input
            type="email"
            name="email"
            className="login-input"
          />
        </div>
        <div>
          <label className="login-label">Password:</label>
          <input
            type="password"
            name="password"
            className="login-input"
          />
        </div>
        <div>
          <button type="submit" className="login-button">Login</button>
        </div>
        <p className="login-label">
          Don't have an account? <Link to="/register_admin"><span className="link-label">Register here</span></Link>
        </p>
      </form>
    </div>
  );
};
export default Login_farmer;
