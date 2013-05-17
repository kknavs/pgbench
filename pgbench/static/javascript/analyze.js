angular.element(document).ready(function () {
    var refreshIntervalId;

    refreshIntervalId = setInterval(function () {
            if (angular.element('[ng-controller=pgbenchCtrl]').scope().measures['objects'] != undefined) {
                clearInterval(refreshIntervalId);

                var c = $("#placeholder");
                var data = getAllData();
                var choice = $("#radio");
                var names =
                    {'scalingFactor': 'Scaling factor',
                        'threads': 'Threads',
                        'clients': 'Clients',
                        'transactionsPerClient': 'Transactions per client',
                        'transactions': 'Transactions',
                        'TPS': 'TPS',
                        'TPSConnEstablish': 'TPS (including)'
                    }
                    ;
                for (i = 0; i < data.length; i++) {
                    temp = names[data[i].label];
                    key = getKey(names, temp);
                    if (i == 0) {
                        choice.append("<input checked type='radio' name='selection' value='" + key + "' style='vertical-align: middle; margin: 0px;'>" + temp + "&nbsp;&nbsp;");
                    }
                    else {
                        choice.append("<input type='radio' name='selection' value='" + key + "' style='vertical-align: middle; margin: 0px;'>" + temp + "&nbsp;&nbsp;");
                    }
                }

                $("input[name='selection']").change(function () {
                    plotSelected(c, this.value);
                });

                sel = $("input[name='selection']:checked");
                console.log(sel.val());
                plotSelected(c, sel.val());
            }
        },
        50
    )
    ;
});

function plotSelected(c, val) {
    data = [];
    temp = prepData(getData(val));
    data.push({label: val, data: temp});
    plotGraph(c, data);
}

function getKey(data, value) {
    for (var key in data) {
        if (data[key] == value) {
            return key;
        }
    }
    return null;
}

function getAllData() {
    var columns = ['scalingFactor', 'threads', 'clients',
        'transactionsPerClient', 'transactions',
        'TPS', 'TPSConnEstablish'];
    var data = [];
    for (i = 0; i < columns.length; i++) {
        var str = columns[i];
        data.push({label: str, data: prepData(getData(str))});
    }
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
    var legend = $(".legend");
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
        colors: ["#ffff00"],
        legend: {
            show: false,
            backgroundOpacity: 0.5,
            container: legend
        }
    };
    $.plot(x, d1, options);
}
