var fs = require("fs");
var csv = require("csv");

// Get timestamp & filename from arguments
var givenTimestamp = parseTimestamp(process.argv[2]);
var filename = process.argv[3];

// Open file and run checking code when loaded
fs.readFile(filename, "utf8", parseData);

function parseData (err, data) {
    csv.parse(data, checkShows);
}

function checkShows (err, tvShows) {
    var show = tvShows.reduce(compareTimes);

    // output current show variable
    console.log(show.name, show.seekTime);
}

function compareTimes (previousValue, currentValue) {
    if (currentValue[0] < givenTimestamp) {
        return {
            'name': currentValue[1],
            'seekTime': Math.abs(currentValue[0] - givenTimestamp)
        };
    } else {
        return previousValue;
    }
}

function parseTimestamp (timestamp) {
    if (timestamp.indexOf('-') > -1) {
       timestamp = new Date(timestamp).getTime() / 1000;
    }
    return timestamp;
}