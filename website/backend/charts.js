var ctx = document.getElementById('historic_etat_chart').getContext('2d');
fetch('../backend/data_for_charts.php')
  .then(response => response.json())
  .then(data => {
    var etat_data = data.historic_etat;
    console.log(data.historic_etat);
    var labels = etat_data.map(item => item.date);
    var pe = etat_data.map(item => parseInt(item['pełny etat']));
    var ce = etat_data.map(item => parseInt(item['część etatu']));
    var dt = etat_data.map(item => parseInt(item['dodatkowa / tymczasowa']));

    var chartData = {
      labels: labels,
      datasets: [{
        label: 'pełny etat',
        data: pe,
        backgroundColor: 'rgba(54, 162, 235, 0.2)',
        borderColor: 'rgba(54, 162, 235, 1)',
        borderWidth: 1
      }, {
        label: 'część etatu',
        data: ce,
        backgroundColor: 'rgba(255, 99, 132, 0.2)',
        borderColor: 'rgba(255, 99, 132, 1)',
        borderWidth: 1
      }, {
        label: 'dodatkowa / tymczasowa',
        data: dt,
        backgroundColor: 'rgba(255, 206, 86, 0.2)',
        borderColor: 'rgba(255, 206, 86, 1)',
        borderWidth: 1
      }]
    };

  var historic_etat_chart = new Chart(ctx, {
      type: 'line',
      data: chartData,
      options: {}
  });
})
.catch(error => console.error('Error fetching data:', error));

var ctx2 = document.getElementById('work_type_etat_chart').getContext('2d');
fetch('../backend/data_for_charts.php')
  .then(response => response.json())
  .then(data => {
    var work_type_data = data.historic_work_type; 
    var labels = work_type_data.map(item => item.date);
    var ph = work_type_data.map(item => parseInt(item['praca hybrydowa']));
    var pz = work_type_data.map(item => parseInt(item['praca zdalna']));
    var ps = work_type_data.map(item => parseInt(item['praca stacjonarna']));
    var pm = work_type_data.map(item => parseInt(item['praca mobilna']));
    var chartData = {
      labels: labels,
      datasets: [{
        label: 'praca hybrydowa',
        data: ph,
        backgroundColor: 'rgba(54, 162, 235, 0.2)',
        borderColor: 'rgba(54, 162, 235, 1)',
        borderWidth: 1
      }, {
        label: 'praca zdalna',
        data: pz,
        backgroundColor: 'rgba(255, 99, 132, 0.2)',
        borderColor: 'rgba(255, 99, 132, 1)',
        borderWidth: 1
      }, {
        label: 'praca stacjonarna',
        data: ps,
        backgroundColor: 'rgba(255, 206, 86, 0.2)',
        borderColor: 'rgba(255, 206, 86, 1)',
        borderWidth: 1
      }, {
        label: 'praca mobilna',
        data: pm,
        backgroundColor: 'rgba(0, 206, 86, 0.2)',
        borderColor: 'rgba(0, 206, 86, 1)',
        borderWidth: 1
      }]
    };

  var work_type_etat_chart = new Chart(ctx2, {
      type: 'line',
      data: chartData,
      options: {}
  });
})
.catch(error => console.error('Error fetching data:', error));

var ctx3 = document.getElementById('count_chart').getContext('2d');
fetch('../backend/data_for_charts.php')
  .then(response => response.json())
  .then(data => {
    var historic_count_data = data.historic_count;
    var labels = historic_count_data.map(item => item.date);
    var c = historic_count_data.map(item => parseInt(item['count']));
    var chartData = {
      labels: labels,
      datasets: [{
        label: 'ilosc ofert',
        data: c, 
        backgroundColor: 'rgba(54, 162, 235, 0.2)',
        borderColor: 'rgba(54, 162, 235, 1)',
        borderWidth: 1
      }]
    };

    var count_chart = new Chart(ctx3, {
      type: 'line',
      data: chartData,
      options: {}
    });
  })
  .catch(error => console.error('Error fetching data:', error));

var ctx4 = document.getElementById('kontrakt_chart').getContext('2d');
fetch('../backend/data_for_charts.php')
  .then(response => response.json())
  .then(data => {
    var kontrakt_data = data.historic_kontrakt;
    var labels = kontrakt_data.map(item => item.date);
    var uop = kontrakt_data.map(item => parseInt(item['umowa o pracę']));
    var b2b = kontrakt_data.map(item => parseInt(item['kontrakt B2B']));
    var uz = kontrakt_data.map(item => parseInt(item['umowa zlecenie']));
    var uosp = kontrakt_data.map(item => parseInt(item['umowa o staż / praktyki']));
    var uod = kontrakt_data.map(item => parseInt(item['umowa o dzieło']));
    var uoz = kontrakt_data.map(item => parseInt(item['umowa na zastępstwo']));
    var chartData = {
      labels: labels,
      datasets: [{
        label: 'umowa o pracę',
        data: uop,
        backgroundColor: 'rgba(54, 162, 235, 0.2)',
        borderColor: 'rgba(54, 162, 235, 1)',
        borderWidth: 1
      }, {
        label: 'kontrakt B2B',
        data: b2b,
        backgroundColor: 'rgba(255, 99, 132, 0.2)',
        borderColor: 'rgba(255, 99, 132, 1)',
        borderWidth: 1
      }, {
        label: 'umowa zlecenie',
        data: uz,
        backgroundColor: 'rgba(255, 206, 86, 0.2)',
        borderColor: 'rgba(255, 206, 86, 1)',
        borderWidth: 1
      }, {
        label: 'umowa o staż / praktyki',
        data: uosp,
        backgroundColor: 'rgba(0, 206, 86, 0.2)', 
        borderColor: 'rgba(0, 206, 86, 1)',
        borderWidth: 1
      }, {
        label: 'umowa o dzieło',
        data: uod,
        backgroundColor: 'rgba(0, 50, 86, 0.2)', 
        borderColor: 'rgba(0, 50, 86, 1)',
        borderWidth: 1
      }, {
        label: 'umowa na zastępstwo',
        data: uoz,
        backgroundColor: 'rgba(255, 255, 255, 0.2)', 
        borderColor: 'rgba(255, 255, 255, 1)',
        borderWidth: 1
      }]
    };

    
    var kontrakt_chart = new Chart(ctx4, {
      type: 'line',
      data: chartData,
      options: {}
    });
  })
  .catch(error => console.error('Error fetching data:', error));

var ctx5 = document.getElementById('management_level_chart').getContext('2d');
fetch('../backend/data_for_charts.php')
  .then(response => response.json())
  .then(data => {
    var management_level_data = data.historic_management_level;
    var labels = management_level_data.map(item => item.date);
    var Mid = management_level_data.map(item => parseInt(item['Mid']));
    var asystent = management_level_data.map(item => parseInt(item['asystent']));
    var Junior = management_level_data.map(item => parseInt(item['Junior']));
    var Senior = management_level_data.map(item => parseInt(item['Senior']));
    var ekspert = management_level_data.map(item => parseInt(item['ekspert']));
    var team_manager = management_level_data.map(item => parseInt(item['team manager']));
    var menedżer = management_level_data.map(item => parseInt(item['menedżer']));
    var prakstaz = management_level_data.map(item => parseInt(item['praktykant / stażysta']));
    var dyrektor = management_level_data.map(item => parseInt(item['dyrektor']));
    var chartData = {
      labels: labels,
      datasets: [{
        label: 'Mid',
        data: Mid,
        backgroundColor: 'rgba(54, 162, 235, 0.2)',
        borderColor: 'rgba(54, 162, 235, 1)',
        borderWidth: 1
      }, {
        label: 'asystent',
        data: asystent,
        backgroundColor: 'rgba(255, 99, 132, 0.2)',
        borderColor: 'rgba(255, 99, 132, 1)',
        borderWidth: 1
      }, {
        label: 'Junior',
        data: Junior,
        backgroundColor: 'rgba(255, 206, 86, 0.2)',
        borderColor: 'rgba(255, 206, 86, 1)',
        borderWidth: 1
      }, {
        label: 'Senior',
        data: Senior,
        backgroundColor: 'rgba(0, 206, 86, 0.2)', 
        borderColor: 'rgba(0, 206, 86, 1)',
        borderWidth: 1
      }, {
        label: 'ekspert',
        data: ekspert,
        backgroundColor: 'rgba(0, 50, 86, 0.2)', 
        borderColor: 'rgba(0, 50, 86, 1)',
        borderWidth: 1
      }, {
        label: 'team_manager',
        data: team_manager,
        backgroundColor: 'rgba(255, 255, 255, 0.2)', 
        borderColor: 'rgba(255, 255, 255, 1)',
        borderWidth: 1
      }, {
        label: 'menedżer',
        data: menedżer,
        backgroundColor: 'rgba(100, 0, 250, 0.2)', 
        borderColor: 'rgba(100, 0, 250, 1)',
        borderWidth: 1
      }, {
        label: 'praktykant / stażysta',
        data: prakstaz,
        backgroundColor: 'rgba(54, 162, 235, 0.2)', 
        borderColor: 'rgba(54, 162, 235, 1)',
        borderWidth: 1
      }, {
        label: 'dyrektor',
        data: dyrektor,
        backgroundColor: 'rgba(75, 192, 192, 0.2)', 
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 1
      }]
    };

    var management_level_chart = new Chart(ctx5, {
      type: 'line',
      data: chartData,
      options: {}
    });
  })
  .catch(error => console.error('Error fetching data:', error));

// TODO
// Make below charts create in diffrent thread
// ----

var ctx6 = document.getElementById('historic_technologie_wymagane').getContext('2d');

function getRandomColor(opacity) {
  var color = 'rgba(';
  for (var i = 0; i < 3; i++) {
    color += Math.floor(Math.random() * 256) + ',';
  }
  color += opacity + ')'; 
  return color;
}

function addDataset(chart, label, data) {
  // Add the new dataset to the chart

  chart.data.datasets.push({
    label: label,
    data: data,
    stack: data,
    backgroundColor: getRandomColor(0.2),
    borderColor: getRandomColor(1),
    borderWidth: 1
  });

  // Update the chart
  chart.update();
} 

fetch('../backend/data_for_charts.php')
  .then(response => response.json())
  .then(data => {
    var historic_technologie_wymagane = data.historic_technologie_wymagane;

    var dateSet = new Set(historic_technologie_wymagane.map(item => item.date));
    var dates = Array.from(dateSet);

    var techSet = new Set(historic_technologie_wymagane.map(item => item.technologia));
    var technologies = Array.from(techSet);

    var initialData = {
      labels: dates,
      datasets: []
    };

    var historic_technologie_wymagane_chart = new Chart(ctx6, {
      type: 'bar',
      data: initialData,
      options: {
        responsive: true,
        interaction: {
          intersect: false,
        },
        scales: {
          x: {
            stacked: true,
          },
          y: {
            stacked: true
          }
        }
      }
    });
    
const result = {};

for (const element of technologies) {
  const dateCountMap = new Map();
  for (const item of historic_technologie_wymagane) {
    if (item.technologia === element) {
      dateCountMap.set(item.date, item.count);
    }
  }

  const elementData = dates.map(date => ({ date, count: dateCountMap.get(date) || 0 }));
  result[element] = elementData;

  addDataset(historic_technologie_wymagane_chart, element, elementData.map(pair => pair.count));
}

})
.catch(error => {
  console.error('Error fetching data:', error);
});

var ctx7 = document.getElementById('historic_technologie_mile_widziane').getContext('2d');

fetch('../backend/data_for_charts.php')
  .then(response => response.json())
  .then(data => {
    var historic_technologie_mile_widziane = data.historic_technologie_mile_widziane;

    var dateSet = new Set(historic_technologie_mile_widziane.map(item => item.date));
    var dates = Array.from(dateSet);

    var techSet = new Set(historic_technologie_mile_widziane.map(item => item.technologia));
    var technologies = Array.from(techSet);

    var initialData = {
      labels: dates,
      datasets: []
    };

    var historic_technologie_mile_widziane_chart = new Chart(ctx7, {
      type: 'bar',
      data: initialData,
      options: {
        responsive: true,
        interaction: {
          intersect: false,
        },
        scales: {
          x: {
            stacked: true,
          },
          y: {
            stacked: true
          }
        }
      }
    });
    
const result = {};

for (const element of technologies) {
  const dateCountMap = new Map();
  for (const item of historic_technologie_mile_widziane) {
    if (item.technologia === element) {
      dateCountMap.set(item.date, item.count);
    }
  }

  const elementData = dates.map(date => ({ date, count: dateCountMap.get(date) || 0 }));
  result[element] = elementData;

  addDataset(historic_technologie_mile_widziane_chart, element, elementData.map(pair => pair.count));
}

})
.catch(error => {
  console.error('Error fetching data:', error);
});
