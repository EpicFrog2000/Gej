
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

//---

var uniqueDates = [...new Set(chartData2.map(item => item.date))];
var uniqueRanges = [...new Set(chartData2.map(item => item.experience_range))];
var dataSets = [];
uniqueRanges.forEach(range => {
  var rangeData = uniqueDates.map(date => {
    var dataItem = chartData2.find(item => item.date === date && item.experience_range === range);
    return dataItem ? dataItem.count_in_range : 0;
  });
  dataSets.push({
    label: range + " lat",
    data: rangeData,
    backgroundColor: getRandomColor(0.2),
    borderColor: getRandomColor(1),
    borderWidth: 1,
  });
});
var ctx = document.getElementById("historic_doswiadczenie_chart").getContext("2d");
var myChart = new Chart(ctx, {
  type: "line",
  data: {
    labels: uniqueDates,
    datasets: dataSets,  },
});

//---

var uniqueDates = [...new Set(chartData3.map(item => item.date))];
var uniqueKategorie = [...new Set(chartData3.map(item => item.kategoria))];
var dataSets = [];

uniqueKategorie.forEach(kategoria => {
  var kategoriaData = uniqueDates.map(date => {
    var dataItem = chartData3.find(item => item.date === date && item.kategoria === kategoria);
    return dataItem ? dataItem.count : 0;
  });

  dataSets.push({
    label: kategoria,
    data: kategoriaData,
    backgroundColor: getRandomColor(0.2),
    borderColor: getRandomColor(1),
    borderWidth: 1,
  });
});

var ctx2 = document.getElementById("historic_kategoria_chart").getContext("2d");
var myChart = new Chart(ctx2, {
  type: "line",
  data: {
    labels: uniqueDates,
    datasets: dataSets,  },
});

var uniqueDates = [...new Set(chartData4.map(item => item.date))];
var uniqueLokacje = [...new Set(chartData4.map(item => item.lokacja))];
var dataSets = [];

uniqueLokacje.forEach(lokacja => {
  var lokacjaData = uniqueDates.map(date => {
    var dataItem = chartData4.find(item => item.date === date && item.lokacja === lokacja);
    return dataItem ? dataItem.count : 0;
  });

  dataSets.push({
    label: lokacja,
    data: lokacjaData,
    backgroundColor: getRandomColor(0.2),
    borderColor: getRandomColor(1),
    borderWidth: 1,
  });
});

var ctx2 = document.getElementById("historic_lokacja_chart").getContext("2d");
var myChart = new Chart(ctx2, {
  type: "line",
  data: {
    labels: uniqueDates,
    datasets: dataSets,  },
});

var uniqueDates = [...new Set(chartData5.map(item => item.date))];
var uniqueRanges = [...new Set(chartData5.map(item => item.salary_range))];
var dataSets = [];
uniqueRanges.forEach(range => {
  var rangeData = uniqueDates.map(date => {
    var dataItem = chartData5.find(item => item.date === date && item.salary_range === range);
    return dataItem ? dataItem.count_in_range : 0;
  });
  dataSets.push({
    label: range + " pln",
    data: rangeData,
    backgroundColor: getRandomColor(0.2),
    borderColor: getRandomColor(1),
    borderWidth: 1,
  });
});
var ctx = document.getElementById("historic_salary_chart").getContext("2d");
var myChart = new Chart(ctx, {
  type: "line",
  data: {
    labels: uniqueDates,
    datasets: dataSets,  },
});

var uniqueDates = [...new Set(chartData6.map(item => item.date))];
var uniqueRanges = [...new Set(chartData6.map(item => item.seniority))];
var dataSets = [];
uniqueRanges.forEach(range => {
  var rangeData = uniqueDates.map(date => {
    var dataItem = chartData6.find(item => item.date === date && item.seniority === range);
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
var ctx = document.getElementById("historic_seniority_chart").getContext("2d");
var myChart = new Chart(ctx, {
  type: "line",
  data: {
    labels: uniqueDates,
    datasets: dataSets,  },
});

var uniqueDates = [...new Set(chartData7.map(item => item.date))];
var uniqueRanges = [...new Set(chartData7.map(item => item.wymaganie))];
var dataSets = [];
uniqueRanges.forEach(range => {
  var rangeData = uniqueDates.map(date => {
    var dataItem = chartData7.find(item => item.date === date && item.wymaganie === range);
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
var ctx = document.getElementById("historic_wymagania_must_chart").getContext("2d");
var myChart = new Chart(ctx, {
  type: "line",
  data: {
    labels: uniqueDates,
    datasets: dataSets,  },
});

var uniqueDates = [...new Set(chartData8.map(item => item.date))];
var uniqueRanges = [...new Set(chartData8.map(item => item.wymaganie))];
var dataSets = [];
uniqueRanges.forEach(range => {
  var rangeData = uniqueDates.map(date => {
    var dataItem = chartData8.find(item => item.date === date && item.wymaganie === range);
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
var ctx = document.getElementById("historic_wymagania_nice_chart").getContext("2d");
var myChart = new Chart(ctx, {
  type: "line",
  data: {
    labels: uniqueDates,
    datasets: dataSets,    
  },
});

// Function to generate random colors
function getRandomColor(opacity) {
  var color = 'rgba(';
  for (var i = 0; i < 3; i++) {
    color += Math.floor(Math.random() * 256) + ',';
  }
  color += opacity + ')'; 
  return color;
}