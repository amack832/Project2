var defaultURL = "/electronic";
function buildPlot() {
  d3.json(defaultURL).then(function(data) {
  for (var i=0; i <data.length; i++) {
    var years = data[i].year;
    var genre = data[i].genre;
    var score = data[i].avg_score;
  }
  var trace1 = {
    type: "scatter",
    mode: "lines",
    x: years,
    y: score
  };
  var data = [trace1];
  Plotly.plot('line', data);
})};
buildPlot()
// Update the plot with new data
function updatePlotly(newdata) {
  Plotly.restyle(buildPlot, "line", "x", [newdata.x]);
  Plotly.restyle(buildPlot, "line", "y", [newdata.y]);
}

// Get new data whenever the dropdown selection changes
function getData(route) {
  console.log(route);
  d3.json(`/${route}`).then(function(data) {
    console.log("newdata", data);
    updatePlotly(data);
  });
}
