// Import and configure the Firebase SDK
// These scripts are made available when the app is served or deployed on Firebase Hosting
// If you do not serve/host your project using Firebase Hosting see https://firebase.google.com/docs/web/setup
// importScripts('/__/firebase/7.12.0/firebase-app.js');
// importScripts('/__/firebase/7.12.0/firebase-messaging.js');
// importScripts('/__/firebase/init.js');

importScripts('https://www.gstatic.com/firebasejs/7.12.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/7.12.0/firebase-messaging.js');

// Initialize the Firebase app in the service worker by passing in
// your app's Firebase config object.
// https://firebase.google.com/docs/web/setup#config-object
firebase.initializeApp({
 apiKey: "AIzaSyDv6Gp9lUVuCDWX80uh3eLIninJwrJ6zEA",
 authDomain: "health-service-2680a.firebaseapp.com",
 databaseURL: "https://health-service-2680a.firebaseio.com",
 projectId: "health-service-2680a",
 storageBucket: "health-service-2680a.appspot.com",
 messagingSenderId: "565226908168",
 appId: "1:565226908168:web:869d5bdebf588272f4ffbd",
 measurementId: "G-LTX07QZ209"
});

const messaging = firebase.messaging();