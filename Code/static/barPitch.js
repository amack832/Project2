// set up the SVG for graph
var svgHeight = window.innerHeight;
var svgWidth = window.innerWidth;

var margin = {
    top: 50,
    right: 50,
    bottom: 50,
    left: 50
};

var height = svgHeight - margin.top - margin.bottom;
var width = svgWidth - margin.left - margin.right;

var svgArea = d3.select("body").select("svg");

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
    var max = [];

    d3.json(defaultURL).then(function(data) {

    // Loop through pitchfork data 
    for (var i=0 ; i<data.length ; i++) {
        // Make sure we are only checking the right year
        if (data[i][genre] == genreName) {
            if (parseFloat(data[i]["year"]) == selectedYear) {
                // Check the review score
                if (!max || parseFloat(data[i]["score"]) > parseFloat(max["score"])) {
                    max = arr[i];

                // Tie breaker
                } else if (parseFloat(data[i]["score"]) == parseFloat(max["score"])) {
                    var rollingAlbum1 = [];
                    var rollingAlbum2 = [];
                    var rollingBand1 = [];
                    var rollingBand2 = [];
                    var tieData = d3.csv("/db/RS-albumlist.csv");

                    // Check whether albums appear
                    for (var j=0 ; j<tieData.length ; j++) {
                        if (tieData[j]["album_title"] == max["album_title"]) {
                            rollingAlbum1 = tieData[j];
                        } else if (tieData[j]["album_title"] == arr[i]["album_title"]) {
                            rollingAlbum2 = tieData[j];
                        }
                    };

                    // If albums don't appear, check if artists show
                    if (rollingAlbum1 == [] && rollingAlbum2 == []) {
                        for (var k=0 ; k<tieData.length ; k++) {
                            if (tieData[k]["artist"] == max["artist"]) {
                                rollingBand1 = tieData[k];
                            } else if (tieData[k]["artist"] == arr[i]["artist"]) {
                                rollingBand2 = tieData[k];
                            }
                        }

                        if (rollingBand1 == [] && rollingBand2 == []) {
                            // Keep on looping
                        } else if (rollingBand1 != [] && rollingBand2 == []) {
                            break;
                        } else if (rollingBand1 == [] && rollingBand2 != []){
                            max = data[i];
                        }
                        
                    } else if (rollingAlbum1 != [] && rollingAlbum2 == []) {
                        break;
                    } else if (rollingAlbum1 == [] && rollingAlbum2 == []) {
                        max = data[i];
                        break;
                    };

                    // If neither the albums nor the artists show up, shrug and move on
                }
            }
        }
    }});
    return max;
}

// Load up the graph
function buildCharts(selectedYear) {

    if (!svgArea.empty()) {
        svgArea.remove();
    };

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
    const xScale = d3.scaleBand()
        .range([0, width])
        .domain(genreNames.length)
        .padding(0.4)
    ;

    const yScale = d3.scaleLinear()
        .range([height, 0])
        .domain([5, 10])
    ;

    const makeYLines = () => d3.axisLeft().scale(yScale);

    // Create axes for plot and place horizontal lines
    chartGroup.append('g')
        .attr('transform', `translate(0, ${height})`)
        .call(d3.axisBottom(xScale))
    ;

    chartGroup.append('g')
        .call(d3.axisLeft(yScale))
    ;

    chartGroup.append('g')
        .attr('class', 'grid')
        .call(makeYLines()
            .tickSize(-width, 0, 0)
            .tickFormat('')
        )
    ;

    // Populate graph
    var barGroup = chartGroup.selectAll()
        .data(topAlbumScores)
        .enter()
        .append('g')
    ;

    barGroup.append('rect')
        .attr('class', 'bar')
        .attr('x', xScale(genreNames))
        .attr('y', d => yScale(d.score))
        .attr('height', d => height - yScale(d.score))
        .attr('width', xScale.bandwidth())
    ;

    // X Label
    svg.append('text')
        .attr('class', 'label')
        .attr('x', -(height / 2) - margin)
        .attr('y', margin / 2.4)
        .attr('transform', 'rotate(-90)')
        .attr('text-anchor', 'middle')
        .text('Review Score (10 Point Scale)')
    ;

    // Y Label
    svg.append('text')
        .attr('class', 'label')
        .attr('x', width / 2 + margin)
        .attr('y', height + margin * 1.7)
        .attr('text-anchor', 'middle')
        .text('Genre Names')
    ;

    // Title
    svg.append('text')
        .attr('class', 'title')
        .attr('x', width / 2 + margin)
        .attr('y', 40)
        .attr('text-anchor', 'middle')
        .text('Top Album Review by Genre')
    ;

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