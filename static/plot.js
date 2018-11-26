function getWindow(lastDate) {
    var window = $('meta[name=x_window]').attr("content");
    var lastDateObj = new Date(lastDate);
    var windowDateObj = lastDateObj.setSeconds(lastDateObj.getSeconds() - window);
    return windowDateObj;
}

function makePlotly( x, y ){
    var plotDiv = document.getElementById("plot");
    var traces = [{
        x: x,
        y: y
    }];
    var windowDateObj = getWindow(x[x.length - 1])
    var layout = {
        font: {size: 18},
        margin: { t: 0 },
        xaxis: {
            range: [windowDateObj,  x[x.length - 1]],
            rangeslider: {range: [x[0], x[x.length - 1]]},
            type: 'date'
        },
        yaxis: {
            range: [0, 110]
        }
    };

    var additional_params = {
        responsive: true
    };

    Plotly.plot(plotDiv, traces, layout, additional_params);
};
var plot_start = 0;

function streamPlotly( x, y ){
    var plotDiv = document.getElementById("plot");
    var data_update = {x: [x], y: [y]}
    var windowDateObj = getWindow(x)
    var layout_update = {xaxis: {
        range: [windowDateObj, x[x.length - 1]],
        rangeslider: {range: [plot_start, x[x.length - 1]]}
    }};
    Plotly.update(plotDiv, {}, layout_update)
    Plotly.extendTraces(plotDiv, data_update, [0])
};

var url = 'http://' + document.domain + ':' + location.port
var socket = io.connect(url);

socket.on('connect', function(msg) {
    console.log('connected to websocket on ' + url);
});

socket.on('bootstrap', function (msg) {
    plot_start = msg.x[0];
    makePlotly( msg.x, msg.y )
});

socket.on('update', function (msg) {
    streamPlotly( msg.x, msg.y )
});