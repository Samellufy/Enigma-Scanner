import './Footer.css';
import { Link } from 'react-router-dom';
const Footer = (props)=>{
    return(
        <div className="footer">
            <div className='footer1'>
                <img src='/images/enigma-scanner-scans-web-vulnerability-high-resolution-logo-transparent.png' alt='logo'/>
            </div>
            <div className='footer2'>
                <Link to='/about'>
                    <span>About</span>
                </Link>
                <Link to='/contact'>
                    <span>Contact</span>
                </Link>
                <Link to='/scan'>
                    <span>Scan</span>
                </Link>
            </div>
            <div className='footer3'>
                <span>Socialize With Enigma</span><br/>
                <img src='/icon/facebookfacebook.png' alt='facebook'/>
                <img src='/icon/twitter.png' alt='facebook'/>
                <img src='/icon/linkedin.png' alt='facebook'/>
                <img src='/icon/youtube.png' alt='facebook'/>
                <img src='/icon/instagram.png' alt='facebook'/>
                <img src='/icon/pinterest.png' alt='facebook'/><br/>
                <Link to='/scan'>
                    <button>Scan Your Website</button>
                </Link>
            </div>
        </div>
    )
};
export default Footer;