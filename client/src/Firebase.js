// Import the functions you need from the SDKs you need
import firebase from 'firebase/compat/app';
import 'firebase/compat/firestore';
import 'firebase/compat/auth';
import 'firebase/compat/storage';

// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyD__UEx9K6Y3j9hKWhTK7mqxi9eq5LW5w4",
  authDomain: "clone-71e05.firebaseapp.com",
  projectId: "clone-71e05",
  storageBucket: "clone-71e05.appspot.com",
  messagingSenderId: "1092707174620",
  appId: "1:1092707174620:web:5c96957c0df8b94ea68c19",
  measurementId: "G-5KLG4SHLEN"
};

// Initialize Firebase
const firebaseApp = firebase.initializeApp(firebaseConfig);
const db = firebaseApp.firestore();
const auth = firebase.auth()
const provider = new firebase.auth.GoogleAuthProvider();
const storage = firebase.storage()

export {auth,provider,storage};
export default db;