// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-app.js";
import { getFirestore, collection, collectionGroup, doc, getDoc, getDocs } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-firestore.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-analytics.js";
//import { getAnalytics, collection, collectionGroup, getDoc, getDocs } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-analytics.js";

// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyB7zKfUa2TQwzAwUWkB3AjOZoN4zoyn86E",
  authDomain: "cmfood-e95e1.firebaseapp.com",
  projectId: "cmfood-e95e1",
  storageBucket: "cmfood-e95e1.appspot.com",
  messagingSenderId: "554997097235",
  appId: "1:554997097235:web:dfd79881df5405ddc6f0e6",
  measurementId: "G-71Q9TVVCDL"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const db = getFirestore(app);
const analytics = getAnalytics(app);

console.log('test');

// Establish collection group for Dining Places, then collections for food items and their nutrition
const diningLocationColl = collection(db, "diningLocations");
const mealItemColl = collectionGroup(db, "locationFoodItems");

//This should later extract data from the database
function findAllMeals() {

}
