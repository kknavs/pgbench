$(document).ready(function () {

    $("#graph").click(function () {
        var x = angular.element('[ng-controller=pgbenchCtrl]').scope().measures['objects'];
        var y = new Array(x.length);
        //mora bit nova spremenljivka, drugače se vrednosti prepišejo
        $.each(x, function (index, val) {
            y[index] = val.TPSConnEstablish;
        });
        alert(y);
    });

});

function getData(col) {
    var x = angular.element('[ng-controller=pgbenchCtrl]').scope().measures['objects'];
    var y = new Array(x.length);
    $.each(x, function (index, val) {
        y[index] = val[col];
    });
    return y;
}

function prepData(data) {
    var d = []
    for (var i = 0; i < data.length; i++) {
        d.push([i, data[i]]);
    }
    return d;
}

function plotGraph(x, d1) {
    $.plot(x, [ d1 ], {
        series: {
            bars: {
                show: true,
                barWidth: 0.6
            }
        },
        xaxis: {
            //max: 50
        },
        yaxis: {
            //max: 5000
        },
        colors: ["#ffff00"]
    });
}
