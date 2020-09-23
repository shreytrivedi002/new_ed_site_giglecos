// //  web  Firebase configuration

const firebaseConfig = {
    apiKey: "AIzaSyAF6U5eAcc8vSc1nrUbk29eOh4LBu10oF0",
    authDomain: "edwebsite-8be8a.firebaseapp.com",
    databaseURL: "https://edwebsite-8be8a.firebaseio.com",
    projectId: "edwebsite-8be8a",
    storageBucket: "edwebsite-8be8a.appspot.com",
    messagingSenderId: "777803280977",
    appId: "1:777803280977:web:62d9d71dc2123223a77e70",
    measurementId: "G-TJN8JQ7EKG"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
firebase.analytics();
var storage = firebase.storage();

var element = document.getElementById('visitorCount');


// Get a reference to the database service
var database = firebase.database();
// const rootRef = database.ref('count');


var m = 1


// read database
async function readData() {
    var countVisit = firebase.database().ref();
    countVisit.once('value').then(function(snap) {
        // updateStarCount(postElement, snap.val());
        // console.log(snap.val()['count']);
        var prev = snap.val()['count'] + 1;
        // alert(prev);
        writeUserData(prev)

    });
}



// write data to database
async function writeUserData(counts) {
    await firebase.database().ref().set({
        count: counts
    });
    updateVisitCount(counts)
}


async function updateVisitCount(n) {
    element.innerText = n

}




readData()