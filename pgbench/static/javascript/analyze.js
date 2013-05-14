angular.element(document).ready(function () {
    var refreshIntervalId;

    refreshIntervalId = setInterval(function () {
            if (angular.element('[ng-controller=pgbenchCtrl]').scope().measures['objects'] != undefined) {
                clearInterval(refreshIntervalId);
                var data = getAllData();
                var c = $("#placeholder");
                plotGraph(c, data);
            }
        },
        50
    )
    ;
});

function getAllData() {
    var columns = ['scalingFactor', 'threads', 'clients',
        'transactionsPerClient', 'transactions',
        'TPS', 'TPSConnEstablish'];
    var data = [];
    for (i = 0; i < columns.length; i++) {
        var str = columns[i];
        data.push({label: str, data: prepData(getData(str))});
    }
    //data.remove(data.getIndex("threads"));
    return data;
}

function getData(col) {
    var x = angular.element('[ng-controller=pgbenchCtrl]').scope().measures['objects'];
    var y = new Array(x.length);
    $.each(x, function (index, val) {
        y[index] = val[col];
    });
    return y;
}

function prepData(data) {
    var d = [];
    for (var i = 0; i < data.length; i++) {
        var temp = data[i];
        if (temp != null) {
            d.push([i, data[i]]);
        }
    }
    return d;
}

function plotGraph(x, d1) {
    var options = {
        series: {
            bars: {
                show: true,
                barWidth: 1
            }
        },
        xaxis: {
            //max: 50
        },
        yaxis: {
            //max: 5000
        },
        colors: ["#ffff00"]
    };
    $.plot(x, d1, options);
}
