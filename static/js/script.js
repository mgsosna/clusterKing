// Uses variables from constants.js and plot_functions.js

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
    xhr.open("POST", URLS.data.moons);
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

function getLabels(algo) {

    var json = JSON.stringify(savedData);

    var xhr = new XMLHttpRequest();
    xhr.open("POST", URLS.algo[algo]);
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onreadystatechange = handleData;
    xhr.send(json);

    function handleData() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            var newData = JSON.parse(xhr.responseText.split(', '));
            var array_of_objects = eval("[" + newData + "]")[0];
            updatePlot(array_of_objects, `Moons\nwith ${ALGO_NAMES[algo]}`);
        }
    }
}


function onlyUnique(value, index, self) {
  return self.indexOf(value) === index;
}

// event listeners
d3.select("#moon-submit").on("click", moonSubmit);
d3.select("#cluster-submit").on("click", function() {
    var algo = d3.select("#algo").property("value");
    getLabels(algo);
});
