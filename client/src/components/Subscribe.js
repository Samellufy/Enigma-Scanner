import { Link } from 'react-router-dom';
import React, { useEffect, useState } from 'react'
import firebase from 'firebase/compat/app';
import 'firebase/compat/auth';
import './Subscribe.css';
const Subscribe = (props)=>{
  const [userId, setUserId] = useState("");

  useEffect(()=>{
    const unsubscribe = firebase.auth().onAuthStateChanged((user) => {
      if (user) {
        setUserId(user.uid);
      } else {
        // User is signed out.
        // You can handle this case if needed.
      }
    });

  }, []);
  const checkout = (plan)=>{
    console.log(userId)
  };
  
    return(
        <div className="sub_container">
            <div className="sub_scan_content">
        <div className="sub_wrap">
          <img src="/images/expertise.jpeg" alt="comprihensive" />
          <h1>
          Pro Version
          </h1>
          <hr></hr>
          <p>
            Enigma Scanner Pro version utilizes advanced scanning techniques to
            comprehensively detect a wide range of vulnerabilities and generate actionable report.
          </p>
          <Link to='/payment'>
          <button onClick={() => checkout(Number(5999))}>$5999 Pay Now</button>
          </Link>
        </div>
        </div>
        </div>
    )
};
export default Subscribe;