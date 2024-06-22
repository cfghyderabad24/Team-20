import React from 'react';
import './TextWithImage.css'; 

const TextWithImage = () => {
  return (
    <div className="new-text-with-image-container">
      <div className="new-text-container">
        <h2 className="new-heading">THE PLANNING PARADISE</h2>
        <p className="header-underline">____</p>
        <p className="new-description">
        Planning Paradise is passionate about crafting charmingly timeless and elegant luxurious weddings and events at stunning venues throughout the world. As the leading wedding designers and event organizers in Hyderabad and Bangalore, we are renowned to create authentic experiences worth cherishing for a lifetime. Choosing Planning Paradise for wedding planning services ensures you and your loved ones can focus on enjoying your time together instead of worrying about the nuisances related to wedding planning. At Planning Paradise, we have highly specialized wedding planners to create a customized timeline for your wedding day while outlining exactly how everything will be managed from start to finish.
        </p>
      </div>
      <img
        src="https://images.squarespace-cdn.com/content/v1/60df244e7cdd8439545be644/fd4dd92f-5d4e-4bb5-85a3-10949c033fdb/TPP+FINAL-01.png" // Replace with your image URL
        alt="Your Alt Text"
        className="new-image"
      />
    </div>
  );
};

export default TextWithImage;