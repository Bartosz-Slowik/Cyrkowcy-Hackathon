var express = require('express');
var app = express();
var path = require('path');
const { v4: uuidv4 } = require('uuid');

//app.use(express.static(__dirname)); // Current directory is root
app.use(express.static(path.join(__dirname, 'public'))); //  "public" off of current is root

var meeting_list=new Array();


app.post("/make", (req, res, next) => {
    let meeting = {
        uuid: uuidv4(),
        hmm: "hmmm"
    }
    res.json(meeting);
});


app.listen(80);
console.log('Listening on port 80');