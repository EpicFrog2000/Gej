//charts below

var ctx1 = document.getElementById('count_chart').getContext('2d');
var chartData1 = {
  labels: chartData1.map(function (entry) { return entry.date; }),
  datasets: [{
    label: 'Ilość',
    data: chartData1.map(function (entry) { return entry.count; }),
    backgroundColor: 'rgba(75, 192, 192, 0.2)',
    borderColor: 'rgba(75, 192, 192, 1)',
    borderWidth: 1
  }]
};
var count_chart = new Chart(ctx1, {
  type: 'line',
  data: chartData1,
  options: {}
});

var ctx2 = document.getElementById('historic_etat_chart').getContext('2d');
var chartData2 = {
  labels: chartData2.map(function (entry) { return entry.date; }),
  datasets: [{
    label: 'pełny etat',
    data: chartData2.map(function (entry) { return entry['pełny etat']; }),
    backgroundColor: 'rgba(54, 162, 235, 0.2)',
    borderColor: 'rgba(54, 162, 235, 1)',
    borderWidth: 1
  }, {
    label: 'część etatu',
    data: chartData2.map(function (entry) { return entry['część etatu']; }),
    backgroundColor: 'rgba(255, 99, 132, 0.2)',
    borderColor: 'rgba(255, 99, 132, 1)',
    borderWidth: 1
  }, {
    label: 'dodatkowa / tymczasowa',
    data: chartData2.map(function (entry) { return entry['dodatkowa / tymczasowa']; }),
    backgroundColor: 'rgba(255, 206, 86, 0.2)',
    borderColor: 'rgba(255, 206, 86, 1)',
    borderWidth: 1
  }]
};
var historic_etat_chart = new Chart(ctx2, {
  type: 'line',
  data: chartData2,
  options: {}
});

var ctx3 = document.getElementById('historic_kontrakt_data').getContext('2d');
var chartData3 = {
  labels: chartData3.map(function (entry) { return entry.date; }),
  datasets: [{
    label: 'umowa o pracę',
    data: chartData3.map(function (entry) { return entry['umowa o pracę']; }),
    backgroundColor: 'rgba(54, 162, 235, 0.2)',
    borderColor: 'rgba(54, 162, 235, 1)',
    borderWidth: 1
  }, {
    label: 'kontrakt B2B',
    data: chartData3.map(function (entry) { return entry['kontrakt B2B']; }),
    backgroundColor: 'rgba(255, 99, 132, 0.2)',
    borderColor: 'rgba(255, 99, 132, 1)',
    borderWidth: 1
  }, {
    label: 'umowa zlecenie',
    data: chartData3.map(function (entry) { return entry['umowa zlecenie']; }),
    backgroundColor: 'rgba(255, 206, 86, 0.2)',
    borderColor: 'rgba(255, 206, 86, 1)',
    borderWidth: 1
  }, {
    label: 'umowa o staż / praktyki',
    data: chartData3.map(function (entry) { return entry['umowa o staż / praktyki']; }),
    backgroundColor: 'rgba(0, 206, 86, 0.2)', 
    borderColor: 'rgba(0, 206, 86, 1)',
    borderWidth: 1
  }, {
    label: 'umowa o dzieło',
    data: chartData3.map(function (entry) { return entry['umowa o dzieło']; }),
    backgroundColor: 'rgba(0, 50, 86, 0.2)', 
    borderColor: 'rgba(0, 50, 86, 1)',
    borderWidth: 1
  }, {
    label: 'umowa na zastępstwo',
    data: chartData3.map(function (entry) { return entry['umowa na zastępstwo']; }),
    backgroundColor: 'rgba(255, 255, 255, 0.2)', 
    borderColor: 'rgba(255, 255, 255, 1)',
    borderWidth: 1
  }]
};
var historic_kontrakt_data = new Chart(ctx3, {
  type: 'line',
  data: chartData3,
  options: {}
});

var ctx4 = document.getElementById('historic_management_level').getContext('2d');
var chartData4 = {
  labels: chartData4.map(function (entry) { return entry.date; }),
  datasets: [{
    label: 'Mid',
    data: chartData4.map(function (entry) { return entry['Mid']; }),
    backgroundColor: 'rgba(54, 162, 235, 0.2)',
    borderColor: 'rgba(54, 162, 235, 1)',
    borderWidth: 1
  }, {
    label: 'asystent',
    data: chartData4.map(function (entry) { return entry['asystent']; }),
    backgroundColor: 'rgba(255, 99, 132, 0.2)',
    borderColor: 'rgba(255, 99, 132, 1)',
    borderWidth: 1
  }, {
    label: 'Junior',
    data: chartData4.map(function (entry) { return entry['Junior']; }),
    backgroundColor: 'rgba(255, 206, 86, 0.2)',
    borderColor: 'rgba(255, 206, 86, 1)',
    borderWidth: 1
  }, {
    label: 'Senior',
    data: chartData4.map(function (entry) { return entry['Senior']; }),
    backgroundColor: 'rgba(0, 206, 86, 0.2)', 
    borderColor: 'rgba(0, 206, 86, 1)',
    borderWidth: 1
  }, {
    label: 'ekspert',
    data: chartData4.map(function (entry) { return entry['ekspert']; }),
    backgroundColor: 'rgba(0, 50, 86, 0.2)', 
    borderColor: 'rgba(0, 50, 86, 1)',
    borderWidth: 1
  }, {
    label: 'team_manager',
    data: chartData4.map(function (entry) { return entry['team_manager']; }),
    backgroundColor: 'rgba(255, 255, 255, 0.2)', 
    borderColor: 'rgba(255, 255, 255, 1)',
    borderWidth: 1
  }, {
    label: 'menedżer',
    data: chartData4.map(function (entry) { return entry['menedżer']; }),
    backgroundColor: 'rgba(100, 0, 250, 0.2)', 
    borderColor: 'rgba(100, 0, 250, 1)',
    borderWidth: 1
  }, {
    label: 'praktykant / stażysta',
    data: chartData4.map(function (entry) { return entry['praktykant / stażysta']; }),
    backgroundColor: 'rgba(54, 162, 235, 0.2)', 
    borderColor: 'rgba(54, 162, 235, 1)',
    borderWidth: 1
  }, {
    label: 'dyrektor',
    data: chartData4.map(function (entry) { return entry['dyrektor']; }),
    backgroundColor: 'rgba(75, 192, 192, 0.2)', 
    borderColor: 'rgba(75, 192, 192, 1)',
    borderWidth: 1
  }]
};
var historic_management_level = new Chart(ctx4, {
  type: 'line',
  data: chartData4,
  options: {}
});

var ctx5 = document.getElementById('historic_work_type').getContext('2d');
var chartData5 = {
  labels: chartData5.map(function (entry) { return entry.date; }),
  datasets: [{
    label: 'praca hybrydowa',
    data: chartData5.map(function (entry) { return entry['praca hybrydowa']; }),
    backgroundColor: 'rgba(54, 162, 235, 0.2)',
    borderColor: 'rgba(54, 162, 235, 1)',
    borderWidth: 1
  }, {
    label: 'praca zdalna',
    data: chartData5.map(function (entry) { return entry['praca zdalna']; }),
    backgroundColor: 'rgba(255, 99, 132, 0.2)',
    borderColor: 'rgba(255, 99, 132, 1)',
    borderWidth: 1
  }, {
    label: 'praca stacjonarna',
    data: chartData5.map(function (entry) { return entry['praca stacjonarna']; }),
    backgroundColor: 'rgba(255, 206, 86, 0.2)',
    borderColor: 'rgba(255, 206, 86, 1)',
    borderWidth: 1
  }, {
    label: 'praca mobilna',
    data: chartData5.map(function (entry) { return entry['praca mobilna']; }),
    backgroundColor: 'rgba(0, 206, 86, 0.2)',
    borderColor: 'rgba(0, 206, 86, 1)',
    borderWidth: 1
  }]
};
var historic_work_type = new Chart(ctx5, {
  type: 'line',
  data: chartData5,
  options: {}
});


var uniqueDates = [...new Set(chartData6.map(item => item.date))];
var uniqueRanges = [...new Set(chartData6.map(item => item.technologia))];
var dataSets = [];
uniqueRanges.forEach(range => {
  var rangeData = uniqueDates.map(date => {
    var dataItem = chartData6.find(item => item.date === date && item.technologia === range);
    return dataItem ? dataItem.count : 0;
  });
  dataSets.push({
    label: range,
    data: rangeData,
    backgroundColor: getRandomColor(0.2),
    borderColor: getRandomColor(1),
    borderWidth: 1,
  });
});
var ctx = document.getElementById("historic_technologie_mile_widziane").getContext("2d");
var myChart = new Chart(ctx, {
  type: "line",
  data: {
    labels: uniqueDates,
    datasets: dataSets,

  },
  
});

var uniqueDates = [...new Set(chartData7.map(item => item.date))];
var uniqueRanges = [...new Set(chartData7.map(item => item.technologia))];
var dataSets = [];
uniqueRanges.forEach(range => {
  var rangeData = uniqueDates.map(date => {
    var dataItem = chartData7.find(item => item.date === date && item.technologia === range);
    return dataItem ? dataItem.count : 0;
  });
  dataSets.push({
    label: range,
    data: rangeData,
    backgroundColor: getRandomColor(0.2),
    borderColor: getRandomColor(1),
    borderWidth: 1,
  });
});
var ctx = document.getElementById("historic_technologie_wymagane").getContext("2d");
var myChart = new Chart(ctx, {
  type: "line",
  data: {
    labels: uniqueDates,
    datasets: dataSets,

  },
  
});

var uniqueDates = [...new Set(chartData8.map(item => item.date))];
var uniqueRanges = [...new Set(chartData8.map(item => item.location))];
var dataSets = [];
uniqueRanges.forEach(range => {
  var rangeData = uniqueDates.map(date => {
    var dataItem = chartData8.find(item => item.date === date && item.location === range);
    return dataItem ? dataItem.count : 0;
  });
  dataSets.push({
    label: range,
    data: rangeData,
    backgroundColor: getRandomColor(0.2),
    borderColor: getRandomColor(1),
    borderWidth: 1,
  });
});
var ctx = document.getElementById("historic_location").getContext("2d");
var myChart = new Chart(ctx, {
  type: "line",
  data: {
    labels: uniqueDates,
    datasets: dataSets,
  },
  
});

function getRandomColor(opacity) {
    var color = 'rgba(';
    for (var i = 0; i < 3; i++) {
      color += Math.floor(Math.random() * 256) + ',';
    }
    color += opacity + ')'; 
    return color;
}

function addDataset(chart, label, data) {
    chart.data.datasets.push({
      label: label,
      data: data,
      stack: data,
      backgroundColor: getRandomColor(0.2),
      borderColor: getRandomColor(1),
      borderWidth: 1,
    });
    chart.update();
} 