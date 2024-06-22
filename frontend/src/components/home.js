import React from 'react';
import './home.css'; 
const Home = () => {
    const scrollingContainerRef = React.useRef(null);
    const [currentIndex, setCurrentIndex] = React.useState(0);
    const [isAutoScrolling, setIsAutoScrolling] = React.useState(true);
    const [selectedGalleryIndex, setSelectedGalleryIndex] = React.useState(null);
    const [isImageMaximized, setIsImageMaximized] = React.useState(false);
    const images = [
        "https://aginvestcanada.com/wp-content/uploads/2020/04/Agriculture-01.jpeg",
      "https://www8.gmanews.tv/webpics/v3/2012/07/_OMI4356.jpg",
      "https://cdn.thewire.in/wp-content/uploads/2017/12/28145521/agriculture-copy.jpg",
      "https://wallpapercave.com/wp/wp6592172.jpg"
    ];

    const handlePrev = () => {
        setCurrentIndex((prevIndex) => (prevIndex - 1 + images.length) % images.length);
        setIsAutoScrolling(false);
    };

    const handleNext = () => {
        setCurrentIndex((prevIndex) => (prevIndex + 1) % images.length);
        setIsAutoScrolling(false);
    };

    React.useEffect(() => {
        const container = scrollingContainerRef.current;
        let interval;
    
        if (container && isAutoScrolling) {
            interval = setInterval(() => {
                setCurrentIndex((prevIndex) => (prevIndex + 1) % images.length);
            }, 5000);
        }
    
        return () => clearInterval(interval);
    }, [isAutoScrolling]);
    

    React.useEffect(() => {
        const container = scrollingContainerRef.current;
        if (container) {
            container.scrollLeft = currentIndex * container.offsetWidth;
        }
    }, [currentIndex]);

    const startAutoScroll = () => {
        setIsAutoScrolling(true);
    };

    const stopAutoScroll = () => {
        setIsAutoScrolling(false);
    };

    const handleDotClick = (index) => {
        setCurrentIndex(index);
        setIsAutoScrolling(false);
    };

    const handleImageClick = (index) => {
        setSelectedGalleryIndex(index);
    };

    const handleImageMouseEnter = () => {
        setIsImageMaximized(true);
    };

    const handleImageMouseLeave = () => {
        setIsImageMaximized(false);
    };
    const photoGallery = [
      "https://aginvestcanada.com/wp-content/uploads/2020/04/Agriculture-01.jpeg",
      "https://www8.gmanews.tv/webpics/v3/2012/07/_OMI4356.jpg",
      "https://cdn.thewire.in/wp-content/uploads/2017/12/28145521/agriculture-copy.jpg",
      "https://wallpapercave.com/wp/wp6592172.jpg",
      "https://www.caleidoscope.in/wp-content/uploads/2020/12/Indian-Agriculture-04.jpg",
      "https://www.watercalculator.org/wp-content/uploads/2017/04/iStock_000010933844_1950.jpg"
    ];

    const buttonData = [
        { label: "Agriculture", text: "Farming happens through community in different parts and different agroclimatic regions. The most important area is the plains where major staple food crops including but not limited to millets, paddy, vegetables and other cash crops are grown. " },
        { label: "Biological Diversity", text: "Promote Ecological Regenerative Agricultural practices in the farms and help the farmers understand how to preserve their ecosystem for better coexistence of plants." },
        { label: "Education", text: "Everyone has the right to education. Education is a basic human right for all and is important for everyone to make the most of their lives. Having an education helps people to access all of their other human rights. " },
    ];

    return (
      <div>
        <div className="containerStyles" onMouseEnter={startAutoScroll} onMouseLeave={stopAutoScroll}>
            <div className="contentStyles">
                <div className="scrollingImagesContainerStyles" ref={scrollingContainerRef}>
                    {images.map((image, index) => (
                        <img key={index} src={image} alt={`Image ${index + 1}`} className="scrollImage" />
                    ))}
                </div>
                <div className="dotsContainer">
                    {images.map((_, index) => (
                        <span
                            key={index}
                            className={`scrollDot ${index === currentIndex ? "activeDot" : ""}`}
                            onClick={() => handleDotClick(index)}
                        ></span>
                    ))}
                </div>
                <div className="textContainer">
                    <img
                        src="https://tse3.mm.bing.net/th?id=OIP.fJ8b-NpHiXp2CM0gPYT6nwHaFj&pid=Api&P=0&h=180"
                        alt="Description of the image"
                        className="imageStyles"
                    />
                    <div className="textContent">
                        <h1 className="mainHeaderStyles">OUR PROGRAMMES</h1>
                        <p className="paragraphStyles">

                        IFTR aims to accelerate the use of modern science and technology for the development of interventions to improve the livelihoods of people and society at large. IFTR will act as a vehicle for taking new technologies/skills to the masses. For this, IFTR will acquire, adopt, adapt, retrofit appropriate science and technology products/processes to provide solutions to practical problems faced by people. Wherever possible, IFTR will also strive to develop suitable technologies/interventions.
                        </p>
                    </div>
                </div>
                <div className="buttonContainer">
                    {buttonData.map(({ label, text }, index) => (
                        <div key={index} className="buttonWithText">
                            <button className="buttonStyles">
                                {label}
                            </button>
                            <p className="buttonTextStyles">{text}</p>
                        </div>
                    ))}
                </div>
                <div className="photoGalleryContainer">
                <h2 className="galleryTitle">Photo Gallery</h2>
        
                    <div className="photoGallery">
                        {photoGallery.map((imageUrl, index) => (
                            <img
                                key={index}
                                src={imageUrl}
                                alt={`Gallery Image ${index + 1}`}
                                className={`galleryImage ${selectedGalleryIndex === index ? 'selected' : ''} ${isImageMaximized ? 'maximized' : ''}`}
                                onClick={() => handleImageClick(index)}
                                onMouseEnter={handleImageMouseEnter}
                                onMouseLeave={handleImageMouseLeave}
                            />
                        ))}
                    </div>
                </div>
              <div className="additionalImageContainer">
                <img
                src="http://www.iftr.in/assests/img/iftrlogo.png"
                alt="Additional Image"
                className="additionalImage"
                />

                    <div className="textContent1">
                      <h1 className="mainHeaderStyles1">Indigenous and Frontier Technology Research Centre</h1>
                    <p className='textContent1para'>Design, Develop and Disseminate Technologies for the Masses for Sustainable happiness.</p>
                    </div>
                    <div className="textContent2">
                      <h1 className="mainHeaderStyles2">REACH US</h1>
                      <p className="para">
                        🏠G1, Shah Flats, 5, 1st Street, Thillai Ganga Nagar, Nanganallur, Chennai 600061. <br/>
                        📞+91 94456 01599<br/>
                        ✉️info@iftr.in
                        </p>
                    </div>
                    <div className="textContent1">
                      <h1 className="mainHeaderStyles1">OUR PROGRAMMES</h1>
                      <ul className="additionalImageList">
                      <li className="additionalImageText">Education</li>
                      <li className="additionalImageText">BioDiversity</li>
                      <li className="additionalImageText">Environment</li>
                      <li className="additionalImageText">Agriculture</li>
                      <li className="additionalImageText">Community Development</li>
                      <li className="additionalImageText">Food Security and Nutrition</li>
                      </ul>
                    
                    </div>
                </div>
                </div>
              </div>
            
        </div>
    );
};

export default Home;


