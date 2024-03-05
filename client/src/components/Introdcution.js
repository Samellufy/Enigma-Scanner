import "./Introduction.css";
import { Link } from "react-router-dom";
import Technology from "./Technologies";
import Working from "./Working";

const Introduction = (props) => {
  return (
    <div className="intro_container">
      <div className="inner_content">
        <h1>
          INTRODUCTION <br /> TO ENIGMA SCANNER
        </h1>
        <img src="/icon/Component 1intro_arrow.png" alt="arrow" />
        <p>
          In an age where cyber threats are ever-present, Enigma Scanner
          empowers you to stay ahead of the curve, fortifying your web
          applications against potential vulnerabilities and safeguarding your
          digital assets with confidence
        </p>
      </div>
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
      <div className="inner_content">
        <h1>
          WHY SCAN WITH
          <br /> ENIGMA SCANNER
        </h1>
        <img src="/icon/Component 1intro_arrow.png" alt="arrow" />
        <p>
          Scan with Enigma Scanner for peace of mind and proactive security
          measures. Our advanced scanning technology meticulously identifies
          vulnerabilities, ranging from SQL injection to information disclosure,
          ensuring the robustness of your web applications. With intuitive
          usability and customizable options, Enigma Scanner provides actionable
          reports that empower you to prioritize and address potential threats
          efficiently.
        </p>
      </div>
      <div className="why_scan_content">
        <div className="why_wrap">
          <img src="/images/comprehesive.webp" alt="comprihensive" />
          <h1>
            Detection
          </h1>
          <hr></hr>
          <p>
            Enigma Scanner utilizes advanced scanning techniques to
            comprehensively detect a wide range of vulnerabilities.
          </p>
        </div>
        <div className="why_wrap">
          <img src="/images/ease_of_use.png" alt="comprihensive" />
          <h1>Ease of Use</h1>
          <hr></hr>
          <p>
            Enigma Scanner simplifies the scanning process, allowing you to
            focus on addressing vulnerabilities efficiently.
          </p>
        </div>
        <div className="why_wrap">
          <img src="/images/actionable_rporting.png" alt="comprihensive" />
          <h1>Reporting</h1>
          <hr></hr>
          <p>
            These reports empower organizations to prioritize and address
            vulnerabilities effectively, helping to strengthen their overall
            security posture.
          </p>
        </div>
        <div className="why_wrap">
          <img
            src="/images/continous_updates_supports.jpg"
            alt="comprihensive"
          />
          <h1>
            Updates
          </h1>
          <hr></hr>
          <p>
            Enigma Scanner offers customizable scanning options to suit the
            unique needs of each organization
          </p>
        </div>
        <div className="why_wrap">
          <img src="/images/integration.jpeg" alt="comprihensive" />
          <h1>
          Integration
          </h1>
          <hr></hr>
          <p>
          Enigma Scanner seamlessly integrates with existing security tools and platforms.
          </p>
        </div>
      </div>
      <Technology/>
      <Working/>
    </div>
  );
};

export default Introduction;
