
function addCell(tr, val) {
    var td = document.createElement('td');

    td.innerHTML = val;
    td.classList.add("body-item");
    td.classList.add("mbr-fonts-style");
    td.classList.add("display-7");

    tr.appendChild(td)
  }


  function addRow(tbl, name, properties) {
    var tr = document.createElement('tr');

    addCell(tr, name);

    for (var i = 0; i < properties.length; i++) {
      addCell(tr, properties[i]['total']);
    }

    tbl.appendChild(tr)
  }

  function createTable() {
    tbl = document.getElementById('tbody');
    var array = nationsData['features'];

    for (var i = 0; i < array.length; i++) {
      var properties = [
        array[i].properties.hasTotal,
        array[i].properties.hasDemocracy,
        array[i].properties.hasGDPCapConstant,
        array[i].properties.hasGDPCapGrowth,
        array[i].properties.hasIncomeCapConstant,
        array[i].properties.hasIncomeCapGrowth,
        array[i].properties.hasUnemploymentILO,
        array[i].properties.hasUnemploymentNational,
        array[i].properties.hasDeathUCDP,
        array[i].properties.hasDeathsTerrorism,
        array[i].properties.hasWoundedTerrorism
        ]

      addRow(tbl, array[i].properties.name, properties);
    }

  }

  createTable()
