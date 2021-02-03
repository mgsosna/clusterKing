// Uses variables from constants.js and plot_functions.js

// To be updated by
var savedData;

function onSubmit(dtype) {

    var inputs = getInputs(dtype);

    json = JSON.stringify(inputs);

    var xhr = new XMLHttpRequest();
    xhr.open("POST", URLS.data[dtype]);
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onreadystatechange = handleData;
    xhr.send(json);

    function handleData() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            var newData = JSON.parse(xhr.responseText.split(', '));
            createPlot(newData, capitalize(dtype));
            savedData = newData;
        }
    }

    d3.select("#algo_block").style('display', 'inline-block');
}

function getInputs(dtype) {

    if (['blobs', 'moons'].includes(dtype)) {
        return {
            noise: d3.select("#noise").property("value"),
            x_offset: d3.select("#x-offset").property("value"),
            y_offset: d3.select("#y-offset").property("value")
        };
    }

    else if (dtype === "rings") {
        return {
            noise: d3.select("#noise").property("value"),
            multiplier: d3.select("#multiplier").property("value")
        };
    }
}

function capitalize(string) {
    return string[0].toUpperCase() + string.slice(1)
}

function getLabels(dtype, algo) {

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
            updatePlot(array_of_objects, `${capitalize(dtype)}\nwith ${ALGO_NAMES[algo]}`);
        }
    }
}


function onlyUnique(value, index, self) {
  return self.indexOf(value) === index;
}

// event listeners
d3.select("#blob-submit").on("click", i => onSubmit("blobs"));
d3.select("#moon-submit").on("click", i => onSubmit("moons"));
d3.select("#ring-submit").on("click", i => onSubmit("rings"));
d3.select("#cluster-submit").on("click", function() {
    var dtype = d3.select("#dtype").text();
    var algo = d3.select("#algo").property("value");
    getLabels(dtype, algo);
});
