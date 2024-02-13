import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { auth, provider } from '../Firebase';
import './Header.css';
import { useDispatch, useSelector } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import { selectUserName, selectUserPhoto, setUserLoginDetails, setSignOutState } from '../features/user/userSlice';

const Header = () => {
    const dispatch = useDispatch();
    const history = useNavigate();
    const userName = useSelector(selectUserName);
    const userPhoto = useSelector(selectUserPhoto);
    const [isLoggingOut, setIsLoggingOut] = useState(false);

    useEffect(() => {
        const checkUserAuth = async () => {
            auth.onAuthStateChanged(async (user) => {
                if (user) {
                    setUser(user);
                    history("/home");
                }
            });
        };
        checkUserAuth();
    }, []);

    const handleAuth = async () => {
        if (!userName) {
            try {
                const result = await auth.signInWithPopup(provider);
                setUser(result.user);
            } catch (error) {
                console.log(error.message);
            }
        } else {
            try {
                await auth.signOut();
                dispatch(setSignOutState);
                setIsLoggingOut(true);
                history("/");
            } catch (error) {
                console.log(error.message);
            }
        }
    };

    const setUser = (user) => {
        dispatch(
            setUserLoginDetails({
                name: user.displayName,
                email: user.email,
                photo: user.photoURL,
            })
        );
    };

     return (
        <nav>
            <div>
                <img className='header_logo' src='/images/enigma-scanner-scans-web-vulnerability-high-resolution-logo-transparent.png' alt='Logo' />
            </div>
            {(!userName || isLoggingOut) ?
                <div className='login-btn'>
                    <button onClick={handleAuth}>Login</button>
                </div>
                :
                <>
                    <div className='nav-menue'>
                        <Link to='/home'>
                            <img src='/icon/home-icon.svg' alt='home_icon' />
                            <span>Home</span>
                        </Link>
                        <Link to='/about'>
                            <img src='/icon/search-icon.svg' alt='home_icon' />
                            <span>About Us</span>
                        </Link>
                        <Link to='/contact'>
                            <img src='/icon/original-icon.svg' alt='home_icon' />
                            <span>Contact Us</span>
                        </Link>
                        <Link to='/scan'>
                            <img src='/icon/watchlist-icon.svg' alt='home_icon' />
                            <span>Scan</span>
                        </Link>
                    </div>
                    <div className='login-btn'>
                        <div className='log-out'>
                            <img className='userImage' src={userPhoto} alt={userName} />
                            <span onClick={handleAuth} className='sign-out'>Sign Out</span>
                        </div>
                    </div>
                </>
            }
        </nav>
    );
}

export default Header;  
