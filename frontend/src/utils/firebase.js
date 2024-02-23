// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: process.env._FIRE_BASE,
  authDomain: "blog-87f44.firebaseapp.com",
  projectId: "blog-87f44",
  storageBucket: "blog-87f44.appspot.com",
  messagingSenderId: "319266519991",
  appId: "1:319266519991:web:b872a3410648adff54c632"
};

// Initialize Firebase
export const app = initializeApp(firebaseConfig);

