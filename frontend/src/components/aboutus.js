import React from 'react';
import './aboutus.css';
import ImageWithText from './ImageWithText';
import TextWithImage from './TextWithImage';

const AboutUs = () => {
  return (
    
    <div className="container">
      <div className='image-aboutus'>
        <img src='http://www.iftr.in/assests/img/about.jpg' alt='aboutus image'/>
      </div>
      <div className='catchy-statement'>
        <p className='headerpara'>Indigenous and Frontier Technology Research Centre</p>
        <h1 className='statement-header'>Connect Science and Technology with Development</h1>
        <p className='statement-para'>20+ Years as a not-for-profit organization to help women in rural areas to stand on their own legs by using an evolving technology – eco-friendly paper production using agricultural wastes.</p>
      </div>
      <div>
     <ImageWithText/>
     <TextWithImage/>
     </div>
      <p className='headerpara'>Meet Our Team</p>
      <div className="row about-div2">
      <div className="container-div">
          <div className="hover-div">
            <img className='hover-image' src='https://t4.ftcdn.net/jpg/00/65/77/27/240_F_65772719_A1UV5kLi5nCEWI0BNLLiFaBPEkUbv5Fv.jpg' alt='person1'/>
            <h3 className="honer-h3">Mr D. K. Raju</h3>
          </div>
        </div>
        <div className="container-div">
          <div className="hover-div">
          <img className='hover-image' src='https://t4.ftcdn.net/jpg/00/65/77/27/240_F_65772719_A1UV5kLi5nCEWI0BNLLiFaBPEkUbv5Fv.jpg' alt='person2'/>
            <h3 className="honer-h3">Mr C. Muthunayagam</h3>
            
          </div>
        </div>
        <div className="container-div">
          <div className="hover-div">
            <img className='hover-image' src='https://t4.ftcdn.net/jpg/00/65/77/27/240_F_65772719_A1UV5kLi5nCEWI0BNLLiFaBPEkUbv5Fv.jpg' alt='person3'/>
            <h3 className="honer-h3">Mr. T. S. Sivasankaran</h3>
          </div>
        </div>
      </div>
    </div>
    
  );
};

export default AboutUs;
