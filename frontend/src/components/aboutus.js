import React from 'react';
import './aboutus.css';
import ImageWithText from './ImageWithText';
import TextWithImage from './TextWithImage';

const AboutUs = () => {
  return (
    
    <div className="container">
      <div className='image-aboutus'>
        <img src='https://images.pexels.com/photos/3563173/pexels-photo-3563173.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1' alt='aboutus image'/>
      </div>
      <div className='catchy-statement'>
        <p className='headerpara'>THE PLANNING PARADISE</p>
        <h1 className='statement-header'>A Complete Event Management Solution</h1>
        <p className='statement-para'>Where success isn't just a goal; it's the standard, exceeding expectations with every occasion.</p>
      </div>
      <div>
     <ImageWithText/>
     <TextWithImage/>
     </div>
      <p className='headerpara'>Meet Our Team</p>
      <div className="row about-div2">
      <div className="container-div">
          <div className="hover-div">
            <img className='hover-image' src='https://images.pexels.com/photos/206551/pexels-photo-206551.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2' alt='person1'/>
            <h3 className="honer-h3">Rashmika Chaluvadi</h3>
          </div>
        </div>
        <div className="container-div">
          <div className="hover-div">
          <img className='hover-image' src='https://images.pexels.com/photos/8561345/pexels-photo-8561345.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2' alt='person2'/>
            <h3 className="honer-h3">Varsha Guduguntla</h3>
            
          </div>
        </div>
        <div className="container-div">
          <div className="hover-div">
            <img className='hover-image' src='https://images.pexels.com/photos/785435/pexels-photo-785435.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2' alt='person3'/>
            <h3 className="honer-h3">Keerthi Lagisetty</h3>
          </div>
        </div>
      </div>
    </div>
    
  );
};

export default AboutUs;
