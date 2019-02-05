// set up the SVG for graph
var svgHeight = 960;
var svgWidth = 500;

var margin = {
    top: 20,
    right: 40,
    bottom: 60,
    left: 100
};

var svg = d3.select("#svg-area")
    .append("svg")
    .attr("height", svgHeight)
    .attr("width", svgWidth)
;

var chartGroup = svg.append("g")
    .attr("transform", `translate(${margin.left}, ${margin.top})`)
;

genreNames = ["rock", "pop/r&b", "rap", "folk/country", "metal", "jazz", "electronic", "global"];

var defaultURL = "/pitchdata";

function findTop(genreName, selectedYear) {
    var max;
    // Loop through pitchfork data 
    for (var i=0 ; i<defaultURL.length ; i++) {
        // Make sure we are only checking the right year
        if (defaultURL[i][genre] == genreName) {
            if (parseFloat(defaultURL[i]["year"]) == selectedYear) {
                // Check the review score
                if (!max || parseFloat(defaultURL[i]["score"]) > parseFloat(max["score"])) {
                    max = arr[i];

                // Tie breaker
                } else if (parseFloat(defaultURL[i]["score"]) == parseFloat(max["score"])) {
                    var rollingAlbum1 = null;
                    var rollingAlbum2 = null;
                    var tieData = d3.csv("/db/RS-albumlist");

                    // Check whether albums appear
                    for (var j=0 ; j<tieData.length ; j++) {
                        if (tieData[j]["album_title"] == max["album_title"]) {
                            rollingAlbum1 = tieData[j];
                        } else if (tieData[j]["album_title"] == arr[i]["album_title"]) {
                            rollingAlbum2 = tieData[j];
                        }
                    };

                    // If albums don't appear, check if artists show
                    for (var k=0 ; k<tieData.length ; k++) {
                        if (rollingAlbum1 == null && rollingAlbum2 == null) {
                            if (tieData[k]["artist"] == max["artist"]) {
                                rollingBand1 = tieData[k];
                            } else if (tieData[k]["artist"] == arr[i]["artist"]) {
                                rollingBand2 = tieData[k];
                            }
                        } else if (rollingAlbum1 == null && rollingAlbum2 != null) {
                            break;
                        } else if (rollingAlbum1 != null && rollingAlbum2 == null) {
                            max = defaultURL[i];
                            break;
                        }
                    };

                    // If neither the albums nor the artists show up, shrug and move to the next
                }
            }
        }
    }
    return max;
}

// Load up the graph
function buildCharts(selectedYear) {

    // Loop through to determine top score for Rock
    var rockTop = findTop("rock", selectedYear);

    // Loop through to determine top score for Pop/R&B
    var popTop = findTop("pop/r&b", selectedYear);

    // Loop through to determine top score for Rap
    var rapTop = findTop("rap", selectedYear);

    // Loop through to determine top score for Folk/Country
    var countryTop = findTop("folk/country", selectedYear);

    // Loop through to determine top score for Metal
    var metalTop = findTop("metal", selectedYear);

    // Loop through to determine top score for Jazz
    var jazzTop = findTop("jazz", selectedYear);

    // Loop through to determine top score for Electronic
    var electroTop = findTop("electronic", selectedYear);

    // Loop through to determine top score for Global
    var globalTop = findTop("global", selectedYear);

    // Load top scores into a list and store genre names for plotting
    topAlbumScores = [rockTop[score], popTop[score], rapTop[score], countryTop[score], metalTop[score], jazzTop[score], electroTop[score], globalTop[score]];

    // Set the trace, data, and layout for plotting
    var trace1 = {
        x: genreNames,
        y: topAlbumScores,
        type: "bar"
    };

    var data = [trace1];

    var layout = {
        title: "Top Album Review by Genre",
        xaxis: "Review Score (10 Point Scale)",
        yaxis: "Genre Name"
    };

    // Plot out the data
    Plotly.newPlot("plot", data, layout);

    // Create group to add tooltips to later
    var barGroup = chartGroup.selectAll("bar");

    // Add hover and on-click elements to show album charted
    var toolTip = d3.tip()
        .attr("class", "tooltip")
        .offset([80, -60])
        .html(function(d) {
            return(`<strong>${d.album_title}</strong><hr>Artist: ${d.artist}</hr><br /><a href=${d.url}>Review</a>`)
        })
    ;

    chartGroup.call(toolTip);

    barGroup.on("mouseover", function(d) {
        toolTip.show(d, this);
    })
    .on("mouseout", function(d) {
        toolTip.hide(d);
    })
    .on("click", function(d) {
        toolTip.show(d, this);
    });
};

// Change year based on selection and reload graph
function updatePlotly() {
    var selection = d3.select(this).property('value')

    buildCharts(selection);
};

function init() {
    buildCharts(1999);
};

init();