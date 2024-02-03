// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-app.js";
import { getFirestore, collection, collectionGroup, query, where, getDocs } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-firestore.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-analytics.js";
//import { getDatabase, ref, child, get } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-database.js";
//import { getDatabase, ref, child, get } from "firebase/database";

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


//THE FOLLOWING MIGHT BE FOR A DIFFERENT TYPE OF FIREBASE DATABASE, CHECK LATER
//const dbRef = ref(getDatabase());
//let diningLocationSnapshot;
// Get a snapshot of all dining options within diningLocations from the firebase database
//get(child(dbRef, `diningLocations`)).then((snapshot) => {
//  if (snapshot.exists()) {
//    diningLocationSnapshot = snapshot.val();
//    console.log(snapshot.val());
//  } else {
//    console.log("No data available");
//  }
//}).catch((error) => {
//  console.error(error);
//});
//        let allLocationsArray = ['BuildPizza','CiaoBella', 'ElGallo', 'ForbesAveSubs', 'GranosPizza',
//        'Hunan', 'Nourish', 'RevolutionNoodle', 'Tahini', 'TepperTaqueria', 'TheExchange',
//        'TrueBurger', 'Underground', 'UrbanRevolution', 'Wild Blue'];
//for (let i = 0; i<allLocationsArray.length; i++) {
//    location = allLocationsArray[i];
//    // Get a snapshot of food items from a specific location from the firebase database
//    get(child(dbRef, `diningLocations/${location}/locationFoodItems`)).then((snapshot) => {
//      if (snapshot.exists()) {
//        locationFoodItemsSnapshot = snapshot.val;
//        console.log(snapshot.val());
//      } else {
//        console.log("No data available");
//      }
//    }).catch((error) => {
//      console.error(error);
//    });
//}


// Establish collection group for Dining Places, then collections for food items and their nutrition
//const diningLocationColl = collection(db, "diningLocations");
const mealItemColl = collectionGroup(db, "locationFoodItems");
const allFoodItems = query(mealItemColl, where('b12', '>=', 0));
const querySnapshot = await getDocs(allFoodItems);
querySnapshot.forEach((doc) => {
    console.log(doc.id, ' => ', doc.data());
});
