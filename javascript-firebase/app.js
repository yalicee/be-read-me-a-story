import { initializeApp } from "firebase/app";
import { connectDatabaseEmulator, getDatabase } from "firebase/database";

const firebaseConfig = {
  apiKey: "AIzaSyCrYjJFtmuugy0_yHm2i1mPTT5b-bSkRaY",
  authDomain: "read-me-a-story-18a8d.firebaseapp.com",
  databaseURL:
    "https://read-me-a-story-18a8d-default-rtdb.europe-west1.firebasedatabase.app",
  projectId: "read-me-a-story-18a8d",
  storageBucket: "read-me-a-story-18a8d.appspot.com",
  messagingSenderId: "987054138841",
  appId: "1:987054138841:web:cc5ad91496f52ef3de25c8",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Initialize Realtime database
const database = getDatabase(app);

if (location.hosting === "localhost") {
  config = {
    databaseURL: "http://localhost:9000/?ns=stories",
  };
  connectDatabaseEmulator(database, "localhost", 9000);
}

App(firebase.initializeApp(config));
