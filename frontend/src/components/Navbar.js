import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';

import './Navbar.css';

function Navbar() {
    const [showDropdown, setShowDropdown] = useState(false);
  const handleDropdownToggle = () => {
    setShowDropdown(!showDropdown);
  };
  
  return (
    <nav className="navbar">
      <Link to="/" className="navbar-brand">
      <img src="http://www.iftr.in/assests/img/iftrlogo.png" alt="Logo" className="logo-image" />
      <span className="logo-text">IFTR</span>
      </Link>
      <ul className="navbar-nav">
        <>
        <li className="nav-item">
          <div className="nav-link" onClick={handleDropdownToggle}>
            Login
              <ul className="dropdown">
                <li>
                  <Link to="/login_farmer" className="nav-link">
                    Farmer
                  </Link>
                </li>
                <li>
                  <Link to="/login_admin" className="nav-link">
                    Admin
                  </Link>
                </li>
              </ul>
          </div>
        </li>
        <li className="nav-item">
          <div className="nav-link" onClick={handleDropdownToggle}>
            Register
            {showDropdown && (
              <ul className="dropdown">
                <li>
                  <Link to="/register_farmer" className="nav-link">
                    Farmer
                  </Link>
                </li>
                <li>
                  <Link to="/register_admin" className="nav-link">
                    Admin
                  </Link>
                </li>
              </ul>
            )}
          </div>
        </li></>
        <li className="nav-item">
          <Link to="/" className="nav-link">
            Home
          </Link>
        </li>
        <>
        <li className="nav-item">
          <Link to="/dashboard" className="nav-link">
            Dashboard
          </Link>
        </li>
        <li className="nav-item">
          <Link to="/aboutus" className="nav-link">
            AboutUs
          </Link>
        </li>
        <li className="nav-item">
        </li></>

      </ul>
    </nav>
  );
}
export default Navbar;
