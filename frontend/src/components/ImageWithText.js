import React from 'react';
import './ImageWithText.css';
const ImageWithText = () => {
  return (
    <div className="image-with-text-container">
      <img 
        src="http://wallpapercave.com/wp/wp1886357.jpg" // Replace with your image URL
        alt="event image"
        className="image"
      />
      <div className="text-container">
        <h2 className="heading">OUR MISSION</h2>
        <p className="heading-underline">____</p>
        <p className="description">
          
IFTR aims to help maintain the society self-sustainably by carrying out programmes of social/rural importance for providing livelihood, income generation, and upliftment of poor through various means. IFTR will strive to restore the dignity and quality of life of masses by eliminating barriers to success through research, innovation, education, entrepreneurial development, design, develop and disseminate simple interventions. IFTR firmly believes in bridging the indigenous and traditional knowledge, wisdom and practices and using scientific advancement to bring a transition in human life for sustainable happiness by conservation and effective use of resources. IFTR is open for collaboration with like-minded organizations / Institutions / Commercial organizations and prepared to take up research and implementation programmes/projects that suit to its expertise to make this world happier. Let us all make our world a better place for all to have a sustainable life.
{/*         
Design, Develop and Disseminate Technologies for the Masses for Sustainable happiness. */}
        </p>
      </div>
    </div>
  );
};

export default ImageWithText;