const BLOBS_URL = "/data/blobs";
const MOONS_URL = "/data/moons";
const RINGS_URL = "/data/rings";
const UNIFORM_URL = "/data/uniform";

const KMEANS_URL = "/cluster/kmeans";

// More than two in case algo thinks there's more
const colors = ['orange', 'purple', 'red', 'green'];
const names = ['A', 'B', 'C', 'D'];

// To be updated by
var savedData;

function moonSubmit() {

    var inputs = {
            noise: d3.select("#noise").property("value"),
            x_offset: d3.select("#x-offset").property("value"),
            y_offset: d3.select("#y-offset").property("value")
        };

    json = JSON.stringify(inputs);

    var xhr = new XMLHttpRequest();
    xhr.open("POST", MOONS_URL);
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onreadystatechange = handleData;
    xhr.send(json);

    function handleData() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            var newData = JSON.parse(xhr.responseText.split(', '));
            createPlot(newData, "Moons");
            savedData = newData;
        }
    }

    d3.select("#algo_block").style('display', 'inline-block');
}

function createPlot(inputData, title) {

    var trace = {x: inputData.x,
                 y: inputData.y,
                 type: "scatter",
                 mode: "markers"};

    var data = [trace];

    var layout = {
        title: title
    };

    Plotly.newPlot("plot", data, layout)

}

function updatePlot(newData, title) {

    var dataForPlot = [];
    var clusters = newData.map(d => d.cluster);
    var unique = clusters.filter(onlyUnique);

    unique.forEach(cluster => {

        var filteredData = newData.filter(d => d.cluster === cluster);

        var trace = {x: filteredData.map(d => d.x),
                     y: filteredData.map(d => d.y),
                     mode: "markers",
                     type: "scatter",
                     marker:
                        {color: colors[+cluster],
                         size: 9},
                     name: names[+cluster]};

        dataForPlot.push(trace);
    });

    var layout = {title: title};

    Plotly.newPlot("plot", dataForPlot, layout);

}

function getLabels() {
    var json = JSON.stringify(savedData);

    var xhr = new XMLHttpRequest();
    xhr.open("POST", KMEANS_URL);
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onreadystatechange = handleData;
    xhr.send(json);

    function handleData() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            var newData = JSON.parse(xhr.responseText.split(', '));
            var array_of_objects = eval("[" + newData + "]")[0];
            updatePlot(array_of_objects, "Moons\nwith k-means");
        }
    }
}

function onlyUnique(value, index, self) {
  return self.indexOf(value) === index;
}

// event listeners
d3.select("#moon-submit").on("click", moonSubmit);
d3.select("#cluster-submit").on("click", getLabels);
