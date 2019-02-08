var defaultURL = '/pitchData';

function buildPlot() {
    // create lists for each genre
    var rockYears = [];
    var rockScores = [];
    var metalYears = [];
    var metalScores = [];
    var popYears = [];
    var popScores = [];
    var rapYears = [];
    var rapScores = [];
    var electroYears = [];
    var electroScores = [];
    var jazzYears = [];
    var jazzScores = [];
    var folkYears = [];
    var folkScores = [];
    var globalYears = [];
    var globalScores = [];

    d3.json(defaultURL).then(function(data) {
        // Loop though data and place into proper list
        for (var i=0 ; i < data.length ; i++) {
            if (data.genre == "rock") {
                rockYears.push(data[i].year);
                rockScores.push(data[i].score);
            } else if (data.genre == "metal") {
                metalYears.push(data[i].year);
                metalScores.push(data[i].score);
            } else if (data.genre == "pop/r&b") {
                popYears.push(data[i].year);
                popScores.push(data[i].score);
            } else if (data.genre == "rap") {
                rapYears.push(data[i].year);
                rapScores.push(data[i].score);
            } else if (data.genre == "electronic") {
                electroYears.push(data[i].year);
                electroScores.push(data[i].score);
            } else if (data.genre == "jazz") {
                jazzYears.push(data[i].year);
                jazzScores.push(data[i].score);
            } else if (data.genre == "folk/country") {
                folkYears.push(data[i].year);
                folkScores.push(data[i].score);
            } else if (data.genre == "global") {
                globalYears.push(data[i].year);
                globalScores.push(data[i].score);
            }
        };

        // Load lists into traces
        var trace1 = {
            type: 'scatter',
            mode: 'markers',
            x: rockYears,
            y: rockScores,
            marker: {
                size: 5,
                color: blue,
                opacity: 0.3
            }
        };

        var trace2 = {
            type: 'scatter',
            mode: 'markers',
            x: metalYears,
            y: metalScores,
            marker: {
                size: 5,
                color: red,
                opacity: 0.3
            }
        };

        var trace3 = {
            type: 'scatter',
            mode: 'markers',
            x: popYears,
            y: popScores,
            marker: {
                size: 5,
                color: cyan,
                opacity: 0.3
            }
        };

        var trace4 = {
            type: 'scatter',
            mode: 'markers',
            x: rapYears,
            y: rapScores,
            marker: {
                size: 5,
                color: green,
                opacity: 0.3
            }
        };

        var trace5 = {
            type: 'scatter',
            mode: 'markers',
            x: electroYears,
            y: electroScores,
            marker: {
                size: 5,
                color: orange,
                opacity: 0.3
            }
        };

        var trace6 = {
            type: 'scatter',
            mode: 'markers',
            x: jazzYears,
            y: jazzScores,
            marker: {
                size: 5,
                color: purple,
                opacity: 0.3
            }
        };

        var trace7 = {
            type: 'scatter',
            mode: 'markers',
            x: folkYears,
            y: folkScores,
            marker: {
                size: 5,
                color: grey,
                opacity: 0.3
            }
        };

        var trace8 = {
            type: 'scatter',
            mode: 'markers',
            x: globalYears,
            y: globalScores,
            marker: {
                size: 5,
                color: pink,
                opacity: 0.3
            }
        };

        var layout = {
            title: "Visualization of Pitchfork Data",
            xaxis: {
                title: "Years"
            },
            yaxis: {
                title: "Score"
            },
            legend = true
        }
        
        var data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8]

        Plotly.plot('scatter', data, layout);
    })
}
buildPlot();