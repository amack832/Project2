// Set route
var defaultURL = '/pitchtotals';

// create lists for each genre
var rockCounts = [];
var metalCounts = [];
var popCounts = [];
var rapCounts = [];
var electroCounts = [];
var jazzCounts = [];
var folkCounts = [];
var globalCounts = [];

// Create list of years
var years = [1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012];

function buildPlot() {

    d3.json(defaultURL).then(function(data) {
        // Loop through years to make sure data is stored in proper order
        for (var j=1999 ; j < 2013 ; j++) {
            // Loop though data
            for (var i=0 ; i < data.length ; i++) {
                // Place data into proper genre's list
                if (data[i].genre == "rock" && data[i].year == j) {
                    rockCounts.push(data[i].genre_count);
                    console.log(rockCounts);
                } else if (data[i].genre == "metal" && data[i].year == j) {
                    metalCounts.push(data[i].genre_count);
                } else if (data[i].genre == "pop/r&b" && data[i].year == j) {
                    popCounts.push(data[i].genre_count);
                } else if (data[i].genre == "rap" && data[i].year == j) {
                    rapCounts.push(data[i].genre_count);
                } else if (data[i].genre == "electronic" && data[i].year == j) {
                    electroCounts.push(data[i].genre_count);
                } else if (data[i].genre == "jazz" && data[i].year == j) {
                    jazzCounts.push(data[i].genre_count);
                } else if (data[i].genre == "folk/country" && data[i].year == j) {
                    folkCounts.push(data[i].genre_count);
                } else if (data[i].genre == "global" && data[i].year == j) {
                    globalCounts.push(data[i].genre_count);
                }

            }
        };

        // Load lists into traces
        var trace1 = {
            x: years,
            y: rockCounts,
            name: "Rock",
            type: "bar"
        };

        var trace2 = {
            x: years,
            y: metalCounts,
            name: "Metal",
            type: "bar"
        };

        var trace3 = {
            x: years,
            y: popCounts,
            name: "Pop/R&B",
            type: "bar"
        };

        var trace4 = {
            x: years,
            y: rapCounts,
            name: "Rap",
            type: "bar"
        };

        var trace5 = {
            x: years,
            y: electroCounts,
            name: "Electronic",
            type: "bar"
        };

        var trace6 = {
            x: years,
            y: jazzCounts,
            name: "Jazz",
            type: "bar"
        };

        var trace7 = {
            x: years,
            y: folkCounts,
            name: "Folk/Country",
            type: "bar"
        };

        var trace8 = {
            x: years,
            y: globalCounts,
            name: "Global",
            type: "bar"
        };

        // Set layout for graph
        var layout = {
            barmode: 'stack',
            title: "Number of Albums Reviewed by Genre Per Year",
            xaxis: {
                title: "Years"
            },
            yaxis: {
                title: "# of Reviews"
            },
            legend: true
        }
        
        // Compile traces into single list
        var data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8];

        // Plot that bad boy
        Plotly.plot('barStack', data, layout);
    })
}
buildPlot();
console.log(rockCounts);