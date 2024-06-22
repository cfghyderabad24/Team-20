import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import './register.css'; 
import axios from "axios";
const Register_admin = () => {
  return (
    <div>
    <div className="register-container">
      <h2 className="register-title">Register Page</h2>
      <form>
        <div>
          <label className="register-label">Username:</label>
          <input
            type="text"
            name="username"
            className="register-input"
          />
        </div>
        <div>
          <label className="register-label">Email:</label>
          <input
            type="email"
            name="email"
            className="register-input"
          />
        </div>
        <div>
          <label className="register-label">Password:</label>
          <input
            type="password"
            name="password"
            className="register-input"
          />
        </div>
        <div>
          <button type="submit" className="register-button">Register</button>
        </div>
        <p className="register-label">
          Already have an account? <Link to="/login_admin"  className="link-label">Login here</Link>
        </p>
      </form>
    </div>
    </div>
  );
};

export default Register_admin;
