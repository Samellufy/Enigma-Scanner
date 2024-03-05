import "./About.css";
import { Link } from "react-router-dom";
import Technology from "./Technologies";
import Working from "./Working";
import Footer from "./Footer";

const About = (props) => {
  return (
    <div className="container">
      <div className="inner_base_content">
        <img src="/images/aboutus_1.png" alt="about us" />
        <h1>
          ABOUT <br /> ENIGMA SCANNER
        </h1>
        <p>
          At Enigma Scanner, we are dedicated to empowering organizations to
          secure their digital assets and protect against cyber threats. With a
          passion for innovation and a commitment to excellence, we strive to
          deliver cutting-edge solutions that make a meaningful impact in
          today's dynamic cybersecurity landscape.Our mission at Enigma Scanner
          is simple: to provide robust and reliable cybersecurity solutions that
          enable businesses to thrive in the digital age. We believe that every
          organization, regardless of size or industry, deserves access to
          best-in-class security tools to safeguard their online presence and
          mitigate risk effectively.
        </p>
        <Link to="/contact">
          <button>LET'S GET IN TOUCH</button>
        </Link>
      </div>
      <div className="why_scan_content">
        <div className="why_wrap">
          <img src="/images/expertise.jpeg" alt="comprihensive" />
          <h1>
          Expertise
          </h1>
          <hr></hr>
          <p>
            Enigma Scanner utilizes advanced scanning techniques to
            comprehensively detect a wide range of vulnerabilities.
          </p>
        </div>
        <div className="why_wrap">
          <img src="/images/inovation.jpeg" alt="comprihensive" />
          <h1>Innovation</h1>
          <hr></hr>
          <p>
            Enigma Scanner simplifies the scanning process, allowing you to
            focus on addressing vulnerabilities efficiently.
          </p>
        </div>
        <div className="why_wrap">
          <img src="/images/traning.jpeg" alt="comprihensive" />
          <h1>Training</h1>
          <hr></hr>
          <p>
            These reports empower organizations to prioritize and address
            vulnerabilities effectively, helping to strengthen their overall
            security posture.
          </p>
        </div>
        <div className="why_wrap">
          <img
            src="/images/scalability.jpeg"
            alt="comprihensive"
          />
          <h1>
          Scalability
          </h1>
          <hr></hr>
          <p>
            Enigma Scanner offers customizable scanning options to suit the
            unique needs of each organization
          </p>
        </div>
        <div className="why_wrap">
          <img src="/images/collabration.gif" alt="comprihensive" />
          <h1>
          Collaboration
          </h1>
          <hr></hr>
          <p>
          Enigma Scanner seamlessly integrates with existing security tools and platforms.
          </p>
        </div>
      </div>
      <Footer/>
    </div>
  );
};

export default About;
