var fs = require("fs");
var csv = require("csv");

var currentShow;

fs.readFile("../tv_schedule_1.csv", "utf8", parseData);

function parseData (err, data) {
    csv.parse(data, checkShows);
}

function checkShows (err, tvShows) {

    var givenTimestamp = 1453805100;

    // loop through each tv show in turn
    tvShows.forEach(function (tvShow) {
        var timestamp = tvShow[0];
        var name = tvShow[1];

        // for each TV show, compare its timestamp to the given timestamp
        // if it's poxitive, this show is in the past, store in current tv show variable
        if (timestamp < givenTimestamp) {
            currentShow = name;
        }
    });

    // output current show variable
    console.log(currentShow);
}
