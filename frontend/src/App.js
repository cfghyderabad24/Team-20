import './App.css';
import Login_farmer from './components/Login_farmer';
import { Routes, Route, BrowserRouter } from "react-router-dom";
import Navbar from './components/Navbar';
import Register_farmer from './components/Register_farmer';
import Login_admin from './components/Login_admin';
import Register_admin from './components/Register_admin';
import AboutUs from './components/aboutus';

function App() {
  return (
    <div>
      <BrowserRouter>
      <Navbar />
      <Routes>
          <Route path="/login_farmer" element={<Login_farmer />} />
          <Route path="/register_farmer" element={<Register_farmer/>} />
          <Route path="/login_admin" element={<Login_admin />} />
          <Route path="/register_admin" element={<Register_admin />} />
          <Route path="/aboutus" element={<AboutUs />} />
          
      </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
