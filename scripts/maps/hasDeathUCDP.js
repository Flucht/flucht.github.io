function hasDeathUCDP(theObject) {
  document.getElementById('media-container-row').innerHTML = "<div class='map' id='map'></div>";

  var map = L.map('map').setView([35, 20], 2);

  L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
    maxZoom: 18,
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

  info.update = function (props) {
    this._div.innerHTML = '<h4>Total Displaced Population</h4>' +  (props ?
      '<b>' + props.name + '</b><br />' + props.hasDeathUCDP + ' people'
      : 'Hover over a state');
  };

  info.addTo(map);

  // get color depending on total displaced population
  function getColor(d) {
    return d > 2000000 ? '#800026' :
        d > 1000000  ? '#BD0026' :
        d > 500000  ? '#E31A1C' :
        d > 250000  ? '#FC4E2A' :
        d > 100000   ? '#FD8D3C' :
        d > 50000   ? '#FEB24C' :
        d > 25000   ? '#FED976' :
              '#FFEDA0';
  }

  function style(feature) {
    return {
      weight: 2,
      opacity: 1,
      color: 'white',
      dashArray: '3',
      fillOpacity: 0.7,
      fillColor: getColor(feature.properties.hasDeathUCDP)
    };
  }

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
      grades = [0, 25000, 50000, 100000, 250000, 500000, 1000000, 2000000],
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
