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

    // Sort ascending
    unique = unique.sort((a,b) => a - b);

    unique.forEach(cluster => {

        var filteredData = newData.filter(d => d.cluster === cluster);

        var trace = {x: filteredData.map(d => d.x),
                     y: filteredData.map(d => d.y),
                     mode: "markers",
                     type: "scatter",
                     marker:
                        {color: colors[+cluster]},
                     name: names[+cluster]};

        dataForPlot.push(trace);
    });

    var layout = {title: title};

    Plotly.newPlot("plot", dataForPlot, layout);

}
