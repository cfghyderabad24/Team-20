import React from 'react';
import './ImageWithText.css';
const ImageWithText = () => {
  return (
    <div className="image-with-text-container">
      <img 
        src="https://images.pexels.com/photos/1306791/pexels-photo-1306791.jpeg?auto=compress&cs=tinysrgb&w=600" // Replace with your image URL
        alt="event image"
        className="image"
      />
      <div className="text-container">
        <h2 className="heading">OUR MISSION</h2>
        <p className="heading-underline">____</p>
        <p className="description">
        Our mission is to create unforgettable experiences through meticulous planning and execution that reflects the unique personalities of our clients. We exceed expectations, bringing joy and lasting memories to every celebration. Staying at the forefront of event design, we embrace innovation and explore cutting-edge concepts to deliver fresh experiences. Our dedication includes personalized service excellence, tailoring each detail to our clients' unique vision. With a blend of creativity, modern aesthetics, and a commitment to sustainability, we aim to surpass expectations and make each event an exceptional and cherished affair.
        </p>
      </div>
    </div>
  );
};

export default ImageWithText;