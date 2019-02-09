var defaultURL = "/1999";

// function buildAlbumPanel(album_title) {
    // var albumURL = "/album_title/"
// }


function buildPlot() {
  var artist = [];
  var album = [];
  var scores = [];
  var years = [];

  d3.json(defaultURL).then(function(data) {
  for (var i=0; i < data.length; i++) {
      if (data[i].score >= 9.0){
        artist.push(data[i].artist)
        album.push(data[i].album_title)
        years.push(data[i].year)
        scores.push(data[i].score)
      }
  }
  console.log(artist);
  var trace1 = {
    type: "bar",
    x: album,
    y: scores
  };

  var layout = {
    title: "Top Albums per Year",
    xaxis: {
      title: "Album"
    },
    yaxis: {
      title: "Score"
    },
    height: 500,
    width: 700,
    orientation: 'h'
  }

  var data = [trace1];
  Plotly.plot('bar', data, layout);
})};
buildPlot()
//Update the plot with new data
function updatePlotly(newdata) {
  Plotly.restyle("bar", "x", [newdata.x]);
  Plotly.restyle("bar", "y", [newdata.y]);
}

// Get new data whenever the dropdown selection changes
function getData(route) {
  console.log(route);
  var artist1 = [];
  var album1 = [];
  var scores1 = [];
  var years1 = []
  d3.json(`/${route}`).then(function(data) {
  for (var i=0; i < data.length; i++) {
    if (data[i].score >= 9.0){
        artist1.push(data[i].artist)
        album1.push(data[i].album_title)
        years1.push(data[i].year)
        scores1.push(data[i].score)
    }  
  }
  var trace = {
    x: album1,
    y: scores1
  }
    console.log("trace data", trace);
    updatePlotly(trace);
  });
}