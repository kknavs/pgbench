angular.element(document).ready(function () {

        var refreshIntervalId;

        refreshIntervalId = setInterval(function () {
                    if (angular.element('[ng-controller=pgbenchCtrl]').scope().measures['objects']!=undefined){
                        clearInterval(refreshIntervalId);
                        var t = getData("TPSConnEstablish");
                        var c = $("#placeholder");
                        var d = prepData(t);
                        plotGraph(c, d);
                    }
                },
                500
        )
        ;
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
