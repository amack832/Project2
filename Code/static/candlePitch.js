var defaultURL = "/electronic";
d3.json(defaultURL).then(function(data) {
  var trace1 = {
    type: "scatter",
    mode: "lines",
    x: data.year,
    y: data.avg_score
  };
  
  var data = [trace1];
  Plotly.plot('line', data);
});

// Update the plot with new data
function updatePlotly(newdata) {
  Plotly.restyle("line", "x", [newdata.x]);
  Plotly.restyle("line", "y", [newdata.y]);
}

// Get new data whenever the dropdown selection changes
function getData(route) {
  console.log(route);
  d3.json(`/${route}`).then(function(data) {
    console.log("newdata", data);
    updatePlotly(data);
  });
}
