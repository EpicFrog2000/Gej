
var ctx = document.getElementById('count_chart').getContext('2d');
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
var chart = new Chart(ctx, {
  type: 'line',
  data: chartData1,
  options: {}
});

var ctx = document.getElementById('historic_jezyki_chart').getContext('2d');
var chartData3 = {
  labels: chartData3.map(function (entry) { return entry["date"]; }),
  datasets: [{
    label: "english",
    data: chartData3.map(function (entry) { return entry["english"]; }),
    backgroundColor: 'rgba(75, 192, 192, 0.2)',
    borderColor: 'rgba(75, 192, 192, 1)',
    borderWidth: 1
},
{
  label: 'polish',
  data: chartData3.map(function (entry) { return entry["polish"]; }),
  backgroundColor: 'rgba(192, 75, 75, 0.2)',
  borderColor: 'rgba(192, 75, 75, 1)',
  borderWidth: 1
}]
};
var historic_wynagrodzenie_chart = new Chart(ctx, {
  type: 'line',
  data: chartData3,
  options: {}
});

var ctx = document.getElementById('historic_tryb_chart').getContext('2d');
var chartData4 = {
  labels: chartData4.map(function (entry) { return entry["date"]; }),
  datasets: [{
    label: "tryb hybrydowo",
    data: chartData4.map(function (entry) { return entry["tryb_hybrydowo"]; }),
    backgroundColor: 'rgba(75, 192, 192, 0.2)',
    borderColor: 'rgba(75, 192, 192, 1)',
    borderWidth: 1
},
{
  label: 'tryb zdalnie',
  data: chartData4.map(function (entry) { return entry["tryb_zdalnie"]; }),
  backgroundColor: 'rgba(192, 75, 75, 0.2)',
  borderColor: 'rgba(192, 75, 75, 1)',
  borderWidth: 1
}]
};
var historic_wynagrodzenie_chart = new Chart(ctx, {
  type: 'line',
  data: chartData4,
  options: {}
});

var ctx = document.getElementById('historic_wymiar_chart').getContext('2d');
var chartData5 = {
  labels: chartData5.map(function (entry) { return entry["date"]; }),
  datasets: [{
    label: "Pełny etat",
    data: chartData5.map(function (entry) { return entry["Pełny etat"]; }),
    backgroundColor: 'rgba(75, 192, 192, 0.2)',
    borderColor: 'rgba(75, 192, 192, 1)',
    borderWidth: 1
},
{
  label: 'Stała',
  data: chartData5.map(function (entry) { return entry["Stała"]; }),
  backgroundColor: 'rgba(192, 75, 75, 0.2)',
  borderColor: 'rgba(192, 75, 75, 1)',
  borderWidth: 1
},
{
  label: 'Podwykonawstwo',
  data: chartData5.map(function (entry) { return entry["Podwykonawstwo"]; }),
  backgroundColor: 'rgba(75, 192, 75, 0.2)',
  borderColor: 'rgba(75, 192, 75, 1)',
  borderWidth: 1
},
{
  label: 'Staż/Praktyka',
  data: chartData5.map(function (entry) { return entry["Staż/Praktyka"]; }),
  backgroundColor: 'rgba(192, 192, 75, 0.2)',
  borderColor: 'rgba(192, 192, 75, 1)',
  borderWidth: 1
},
{
  label: 'Tymczasowa',
  data: chartData5.map(function (entry) { return entry["Tymczasowa"]; }),
  backgroundColor: 'rgba(75, 75, 192, 0.2)',
  borderColor: 'rgba(75, 75, 192, 1)',
  borderWidth: 1
},
{
  label: 'Część etatu',
  data: chartData5.map(function (entry) { return entry["Część etatu"]; }),
  backgroundColor: 'rgba(75, 75, 0, 0.2)',
  borderColor: 'rgba(75, 75, 0, 1)',
  borderWidth: 1
},
{
  label: 'Wolontariat',
  data: chartData5.map(function (entry) { return entry["Wolontariat"]; }),
  backgroundColor: 'rgba(100, 0, 192, 0.2)',
  borderColor: 'rgba(75, 0, 192, 1)',
  borderWidth: 1
}]
};
var historic_wynagrodzenie_chart = new Chart(ctx, {
  type: 'line',
  data: chartData5,
  options: {}
});

var ctx = document.getElementById('historic_wykrztalcenie_chart').getContext('2d');
var chartData6 = {
  labels: chartData6.map(function (entry) { return entry["date"]; }),
  datasets: [{
    label: "Licencjat",
    data: chartData6.map(function (entry) { return entry["Licencjat"]; }),
    backgroundColor: 'rgba(75, 192, 192, 0.2)',
    borderColor: 'rgba(75, 192, 192, 1)',
    borderWidth: 1
},
{
  label: 'Magister',
  data: chartData6.map(function (entry) { return entry["Magister"]; }),
  backgroundColor: 'rgba(192, 75, 75, 0.2)',
  borderColor: 'rgba(192, 75, 75, 1)',
  borderWidth: 1
},
{
  label: 'Inżynier',
  data: chartData6.map(function (entry) { return entry["Inżynier"]; }),
  backgroundColor: 'rgba(75, 192, 75, 0.2)',
  borderColor: 'rgba(75, 192, 75, 1)',
  borderWidth: 1
},
{
  label: 'Średnie',
  data: chartData6.map(function (entry) { return entry["Średnie"]; }),
  backgroundColor: 'rgba(192, 192, 75, 0.2)',
  borderColor: 'rgba(192, 192, 75, 1)',
  borderWidth: 1
},
{
  label: 'Średnie techniczne/branżowe',
  data: chartData6.map(function (entry) { return entry["Średnie techniczne/branżowe"]; }),
  backgroundColor: 'rgba(75, 75, 192, 0.2)',
  borderColor: 'rgba(75, 75, 192, 1)',
  borderWidth: 1
},
{
  label: 'Doktor',
  data: chartData6.map(function (entry) { return entry["Doktor"]; }),
  backgroundColor: 'rgba(75, 75, 0, 0.2)',
  borderColor: 'rgba(75, 75, 0, 1)',
  borderWidth: 1
},
{
  label: 'Zasadnicze zawodowe/branżowe',
  data: chartData6.map(function (entry) { return entry["Zasadnicze zawodowe/branżowe"]; }),
  backgroundColor: 'rgba(100, 0, 192, 0.2)',
  borderColor: 'rgba(75, 0, 192, 1)',
  borderWidth: 1
},
{
  label: 'Podstawowe',
  data: chartData6.map(function (entry) { return entry["Podstawowe"]; }),
  backgroundColor: 'rgba(75, 0, 0, 0.2)',
  borderColor: 'rgba(75, 0, 0, 1)',
  borderWidth: 1
}]
};
var historic_wynagrodzenie_chart = new Chart(ctx, {
  type: 'line',
  data: chartData6,
  options: {}
});

var uniqueDates = [...new Set(chartData7.map(item => item['date']))];
var uniqueRanges = [...new Set(chartData7.map(item => item['firma']))];
var dataSets = [];
uniqueRanges.forEach(range => {
  var rangeData = uniqueDates.map(date => {
    var dataItem = chartData7.find(item => item['date'] === date && item['firma'] === range);
    return dataItem ? dataItem['ilosc'] : 0;
  });
  dataSets.push({
    label: range,
    data: rangeData,
    backgroundColor: getRandomColor(0.2),
    borderColor: getRandomColor(1),
    borderWidth: 1,
  });
});
var ctx = document.getElementById("historic_firmy_chart").getContext("2d");
var myChart = new Chart(ctx, {
  type: "line",
  data: {
    labels: uniqueDates,
    datasets: dataSets,    
  },
});

var uniqueDates = [...new Set(chartData8.map(item => item['date']))];
var uniqueRanges = [...new Set(chartData8.map(item => item['lokalizacja']))];
var dataSets = [];
uniqueRanges.forEach(range => {
  var rangeData = uniqueDates.map(date => {
    var dataItem = chartData8.find(item => item['date'] === date && item['lokalizacja'] === range);
    return dataItem ? dataItem['ilosc'] : 0;
  });
  dataSets.push({
    label: range,
    data: rangeData,
    backgroundColor: getRandomColor(0.2),
    borderColor: getRandomColor(1),
    borderWidth: 1,
  });
});
var ctx = document.getElementById("historic_lokalizacja_chart").getContext("2d");
var myChart = new Chart(ctx, {
  type: "line",
  data: {
    labels: uniqueDates,
    datasets: dataSets,    
  },
});


var uniqueDates = [...new Set(chartData2.map(item => item['date']))];
var uniqueRanges = [...new Set(chartData2.map(item => item['nazwa']))];
var dataSets = [];
uniqueRanges.forEach(range => {
  var rangeData = uniqueDates.map(date => {
    var dataItem = chartData2.find(item => item['date'] === date && item['nazwa'] === range);
    return dataItem ? dataItem['ilosc'] : 0;
  });
  dataSets.push({
    label: range,
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