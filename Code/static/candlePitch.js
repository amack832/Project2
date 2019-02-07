var defaultURL = "/electronic";

function buildPlot() {
  var years = []
  var scores = []
  d3.json(defaultURL).then(function(data) {
  for (var i=0; i < data.length; i++) {
    years.push(data[i].year)
    scores.push(data[i].avg_score)
  }
  console.log(years);
  var trace1 = {
    type: "scatter",
    mode: "lines",
    x: years,
    y: scores
  };

  var layout = {
    title: "Average Genre Score per Year",
    xaxis: {
      title: "Years"
    },
    yaxis: {
      title: "Average Score"
    },
    height: 300,
    width: 750
  }
  var data = [trace1];
  Plotly.plot('line', data, layout);
})};
buildPlot()
//Update the plot with new data
function updatePlotly(newdata) {
  Plotly.restyle("line", "x", [newdata.x]);
  Plotly.restyle("line", "y", [newdata.y]);
}

// Get new data whenever the dropdown selection changes
function getData(route) {
  console.log(route);
  var years1 = []
  var scores1 = []
  d3.json(`/${route}`).then(function(data) {
  for (var i=0; i < data.length; i++) {
    years1.push(data[i].year)
    scores1.push(data[i].avg_score)
  }
  var trace = {
    x: years1,
    y: scores1
  }
    console.log("trace data", trace);
    updatePlotly(trace);
  });
}
