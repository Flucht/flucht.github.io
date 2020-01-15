Chart.defaults.global.pointHitDetectionRadius = 1;

function updateChart(input_nation, predicate_1, predicate_2) {
  var customTooltips = function(tooltip) {
    // Tooltip Element
    var tooltipEl = document.getElementById('chartjs-tooltip');

    if (!tooltipEl) {
      tooltipEl = document.createElement('div');
      tooltipEl.id = 'chartjs-tooltip';
      tooltipEl.innerHTML = '<table></table>';
      this._chart.canvas.parentNode.appendChild(tooltipEl);
    }

    // Hide if no tooltip
    if (tooltip.opacity === 0) {
      tooltipEl.style.opacity = 0;
      return;
    }

    // Set caret Position
    tooltipEl.classList.remove('above', 'below', 'no-transform');
    if (tooltip.yAlign) {
      tooltipEl.classList.add(tooltip.yAlign);
    } else {
      tooltipEl.classList.add('no-transform');
    }

    function getBody(bodyItem) {
      return bodyItem.lines;
    }

    // Set Text
    if (tooltip.body) {
      var titleLines = tooltip.title || [];
      var bodyLines = tooltip.body.map(getBody);

      var innerHtml = '<thead>';

      titleLines.forEach(function(title) {
        innerHtml += '<tr><th>' + title + '</th></tr>';
      });
      innerHtml += '</thead><tbody>';

      bodyLines.forEach(function(body, i) {
        var colors = tooltip.labelColors[i];
        var style = 'background:' + colors.backgroundColor;
        style += '; border-color:' + colors.borderColor;
        style += '; border-width: 2px';
        var span = '<span class="chartjs-tooltip-key" style="' + style + '"></span>';
        innerHtml += '<tr><td>' + span + body + '</td></tr>';
      });
      innerHtml += '</tbody>';

      var tableRoot = tooltipEl.querySelector('table');
      tableRoot.innerHTML = innerHtml;
    }

    var positionY = this._chart.canvas.offsetTop;
    var positionX = this._chart.canvas.offsetLeft;

    // Display, position, and set styles for font
    tooltipEl.style.opacity = 1;
    tooltipEl.style.left = positionX + tooltip.caretX + 'px';
    tooltipEl.style.top = positionY + tooltip.caretY + 'px';
    tooltipEl.style.fontFamily = tooltip._bodyFontFamily;
    tooltipEl.style.fontSize = tooltip.bodyFontSize + 'px';
    tooltipEl.style.fontStyle = tooltip._bodyFontStyle;
    tooltipEl.style.padding = tooltip.yPadding + 'px ' + tooltip.xPadding + 'px';
  };

  function chartData(props) {
    var nation = nationsData['features'].find(feature => feature.properties.name === input_nation)

    data = []

    if (props != "emptyChart"){
      years.forEach(
        year => data.push(nation['properties'][props][year])
      )
    }

    return data
  }

  var lineChartData = {
    labels: years,
    datasets: [{
      label: info_labels[predicate_1].title,
      borderColor: 'rgba(247, 94, 25, 0.4)',
      pointBackgroundColor: 'rgb(247, 94, 25)',
      fill: false,
      data: chartData(predicate_1),
      yAxisID: 'y-axis-1'
    }, {
      label: info_labels[predicate_2].title,
      borderColor: 'rgba(83, 161, 214, 0.4)',
      pointBackgroundColor: 'rgb(83, 161, 214)',
      fill: false,
      data: chartData(predicate_2),
      yAxisID: 'y-axis-2'
    }]
  };

  var chartEl = document.getElementById('chart');
  window.myLine = new Chart(chartEl, {
    type: 'line',
    data: lineChartData,
    options: {
      // title: {
      //   display: true,
      //   text: 'Configure Your Own'
      // },
      scales: {
						yAxes: [{
							type: 'linear',
							display: true,
							position: 'left',
							id: 'y-axis-1',
						}, {
							type: 'linear',
							display: true,
							position: 'right',
							id: 'y-axis-2',

							gridLines: {
								drawOnChartArea: false,
							},
						}],
					},
      tooltips: {
        enabled: false,
        mode: 'index',
        position: 'nearest',
        custom: customTooltips
      }
    }
  });
}
