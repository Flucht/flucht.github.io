var chart

function updateMap(predicate) {
  document.getElementById('media-container-row').innerHTML = "<div class='map' id='map'></div>";

  var southWest = L.latLng(-89.98155760646617, -180),
      northEast = L.latLng(89.99346179538875, 180);
  var bounds = L.latLngBounds(southWest, northEast);

  var map = L.map('map', {center: [35, 0], zoom: 2, maxBounds: bounds, maxBoundsViscosity: 1.0,});

  L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
    minZoom: 2, maxZoom: 7,
    attribution: 'Map &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a>, ' +
      '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
      'Imagery &copy; <a href="https://www.mapbox.com/">Mapbox</a>',
    id: 'mapbox/streets-v11'
  }).addTo(map);

  // control that shows state info on hover
  var info = L.control();

  info.onAdd = function (map) {
    this._div = L.DomUtil.create('div', 'info');
    this.update();
    return this._div;
  };

  function convertNumber(numb) {
    if (numb > 999) {
      numb = Math.round(numb).toLocaleString('de')
    } else {
      numb = +(Math.round(numb + "e+2")  + "e-2")
    }
    return numb
  }

  info.update = function (props) {
    this._div.innerHTML = '<h4>' + info_labels[predicate].title + '</h4>' +  (props ?
      '<b>' + props.name + '</b><br />' + convertNumber(props[predicate]["average"]) + ' ' + info_labels[predicate].type + ' (average/year)'
      : 'Hover over a state');

    if (document.getElementById("data-description") != null) {
      document.getElementById("data-description").innerHTML = '<b>Description:</b>' + '<br /><p>' + info_labels[predicate].description + '</p>' + '<b>Data provider:</b>' + '<br /><p>' + info_labels[predicate].provider + '</p>';
    }
  };

  info.addTo(map);

  var max
  var step = []
  function getMax(arr, prop) {
    for (var i=0 ; i<arr.length ; i++) {
      if (max == null || parseFloat(arr[i]['properties'][prop]['average']) > parseFloat(max)){
        max = arr[i]['properties'][prop]['average'];
      }
    }
    if (String(parseInt(max)).length > 2) {
      var d = Math.pow(10, String(parseInt(max)).length-2);
      max = Math.ceil(max/d)*d;
    }
    if (max > 100000) {
      step = [Math.round(max*0.8), Math.round(max*0.6), Math.round(max*0.4), Math.round(max*0.1), Math.round(max*0.01), Math.round(max*0.001), step_0 = Math.round(max*0.0005)]
    } else {
      step = [Math.round(max*1), Math.round(max*0.85), Math.round(max*0.7), Math.round(max*0.55), Math.round(max*0.4), Math.round(max*0.25), step_0 = Math.round(max*0.1)]
    }

    return max;
  }

  function getColor(d) {
    if(max == null){
      getMax(nationsData['features'], predicate)
    }
    return d > step[0] ? '#990000' :
        d > step[1] ? '#DD310B' :
        d > step[2] ? '#ED5E19' :
        d > step[3] ? '#FF7D14' :
        d > step[4] ? '#FF9035' :
        d > step[5] ? '#FFA851' :
        d > step[6] ? '#FFC37F' :
              '#FFE1BF';
  }

  function style(feature) {
    return {
      weight: 2,
      opacity: 1,
      color: 'white',
      dashArray: '3',
      fillOpacity: 0.7,
      fillColor: getColor(feature.properties[predicate]['average'])
    };
  }

  function chartData(props) {
    data = []

    if (props != "emptyChart"){
      years.forEach(
        year => data.push(props[predicate][year])
      )
    }

    return data
  }

  function destroyChart() {
    if (chart != null){
      chart.destroy();
    }
  }

  function updateChart(props) {
    destroyChart();

    if (document.getElementById('map-graph') != null) {
      chart = new Chart(document.getElementById('map-graph'),{
        "type":"bar",
        "data":{
          "labels":years,
          "datasets":[{
            "label":info_labels[predicate].title,
            "data": chartData(props),
            "fill":false,
            "backgroundColor":"rgba(247, 94, 25, 0.2)",
            "borderColor":"rgb(247, 94, 25)",
            "borderWidth":1
          }]
        },"options":{
          "scales":{
            "yAxes":[{
              "ticks":{
                "beginAtZero":true
              }
            }]
          }
        }
      });
    }
  }

  updateChart('emptyChart');

  function highlightFeature(e) {
    var layer = e.target;

    layer.setStyle({
      weight: 5,
      color: '#666',
      dashArray: '',
      fillOpacity: 0.7
    });

    if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
      layer.bringToFront();
    }

    info.update(layer.feature.properties);
    updateChart(layer.feature.properties);
  }

  var geojson;

  function resetHighlight(e) {
    geojson.resetStyle(e.target);
    info.update();
  }

  function zoomToFeature(e) {
    map.fitBounds(e.target.getBounds());
  }

  function onEachFeature(feature, layer) {
    layer.on({
      mouseover: highlightFeature,
      mouseout: resetHighlight,
      click: zoomToFeature
    });
  }

  geojson = L.geoJson(nationsData, {
    style: style,
    onEachFeature: onEachFeature
  }).addTo(map);

  map.attributionControl.addAttribution('Data &copy; <a href="http://flucht.github.io/">Flucht</a>');


  var legend = L.control({position: 'bottomright'});

  legend.onAdd = function (map) {

    var div = L.DomUtil.create('div', 'info legend'),
      grades = [0, step[6], step[5], step[4], step[3], step[2], step[1], step[0]],
      labels = [],
      from, to;

    for (var i = 0; i < grades.length; i++) {
      from = grades[i];
      to = grades[i + 1];

      labels.push(
        '<i style="background:' + getColor(from + 1) + '"></i> ' +
        from + (to ? '&ndash;' + to : '+'));
    }

    div.innerHTML = labels.join('<br>');
    return div;
  };

  legend.addTo(map);
}
