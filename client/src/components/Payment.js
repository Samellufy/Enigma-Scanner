import React, { useEffect, useState } from 'react';
import "./Payment.css";
import firebase from 'firebase/compat/app';
import 'firebase/compat/auth';
import './Subscribe.css';
import { Link } from 'react-router-dom';


function PaymentForm() {
    const [userId, setUserId] = useState("");
    const [isSubscribed, setIsSubscribed] = useState(false);

    useEffect(() => {
        const unsubscribe = firebase.auth().onAuthStateChanged(async (user) => {
            if (user) {
                setUserId(user.uid);
                checkSubscription(user.uid)
            } else {
                // User is signed out.
                // You can handle this case if needed.
            }
        });

        return () => {
            unsubscribe();
        };
    }, []);

    const checkout = async () => {
        try {
            console.log(userId);
            // Create a new collection 'subscribedUsers' and add the user to it
            firebase.firestore().collection('subscribedUsers').add({
                userId: userId,
                // You can add more user information here if needed
            });

            console.log("User subscribed successfully!");
        } catch (error) {
            console.error("Error subscribing user:", error);
        }
    };

    const checkSubscription = async (userId) => {
        try {
            const subscribedUsersRef = firebase.firestore().collection('subscribedUsers');
            const querySnapshot = await subscribedUsersRef.where('userId', '==', userId).get();
    
            if (!querySnapshot.empty && querySnapshot.docs.length > 0) {
                // User document exists in the collection, indicating subscription
                setIsSubscribed(true);
                console.log("user subscribed");

            } else {
                // User document does not exist in the collection, indicating no subscription
                setIsSubscribed(false);
                console.log("user not subscribed");
            }
        } catch (error) {
            console.error("Error checking subscription:", error);
            setIsSubscribed(false); // Set subscription status to false in case of an error
        }
    };
    console.log(isSubscribed);
    return (
        <div className="pay_container">
            <div className="pay_scan_content">
                <div className="pay_wrap">
                    <h1>
                        Credit Card
                    </h1>
                    <img src="https://i.imgur.com/2ISgYja.png" alt="Paypal" />
                    <img src="https://i.imgur.com/W1vtnOV.png" alt="Paypal" />
                    <img src="https://i.imgur.com/35tC99g.png" alt="Paypal" />
                    <img src="https://i.imgur.com/2ISgYja.png" alt="Paypal" />
                    <hr></hr>
                    <div className='pay_from_input'>
                        <input type='text' autoComplete='off' required='required'/>
                        <span>Card Number</span>
                    </div>
                    <div className='pay_expiry_input'>
                        <input type='date' autoComplete='off' required='required'/>
                        <span>Expiry Date</span>
                    </div>
                    <div className='pay_cvv_input'>
                        <input type='text' autoComplete='off' required='required'/>
                        <span>CVC/CVV</span>
                    </div>
                    <p> Your transaction is secured with ssl certificate</p>
                    {isSubscribed ? (
                    <button onClick={checkout}>Pro User</button>
                ) : (
                    <Link to='/scan'>
                    <button onClick={checkout}>Pay</button>
                    </Link>
                )}
                </div>
            </div>
        </div>
    );
}

export default PaymentForm;
