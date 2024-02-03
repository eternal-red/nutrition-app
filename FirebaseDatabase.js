// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-app.js";
import { getFirestore, collection, collectionGroup, query, where, getDocs } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-firestore.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-analytics.js";

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

var allMealLocations = {}

const mealItemColl = collectionGroup(db, "locationFoodItems");
const allFoodItems = query(mealItemColl, where('b12', '>=', 0));
const querySnapshot = await getDocs(allFoodItems);
querySnapshot.forEach((doc) => {
    //doc.data() returns a dictionary containing the name, location, and nutrition facts of the food
    //example of potential data:
    //{iron: 1, zinc: 0.64, calcium: 60, magnesium: 5, b12: 0, vitaminD: 0, name: "Pizza", location:"The Edge"}
    foodData = doc.data();
    //foodData[location] would result in a string of the location
    foodLocation = foodData[location];
    console.log(doc.id, ' => ',foodData);
});
