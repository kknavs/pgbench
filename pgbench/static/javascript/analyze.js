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
                for (var i = 0; i < data.length; i++) {
                    var temp = names[data[i].label];
                    var key = getKey(names, temp);
                    if (i == 0) {
                        choice.append("<input checked type='radio' name='selection' value='" + key + "'><label>" + temp + "</label>");
                    }
                    else {
                        choice.append("<input type='radio' name='selection' value='" + key + "'><label>" + temp + "</label>");
                    }
                }

                $("input[name='selection']").change(function () {
                    plotSelected(c, this.value);
                });

                var sel = $("input[name='selection']:checked");
                //console.log(sel.val());
                plotSelected(c, sel.val());
            }
        },
        50
    )
    ;
});

function plotSelected(c, val) {
    var colors = {'scalingFactor': '#0000ff',
            'threads': '#00ff00',
            'clients': '#ff0000',
            'transactionsPerClient': '#ff00ff',
            'transactions': '#ffff00',
            'TPS': '#00ffff',
            'TPSConnEstablish': '#ffffff'
        }
        ;
    var data = [];
    var temp = prepData(getData(val));
    var color = colors[val];
    data.push({label: val, data: temp, color: color});
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
    for (var i = 0; i < columns.length; i++) {
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

function plotGraph(x, d1, color) {
    var c;
    if (color == undefined) {
        c = "#ffff00";
    }
    else {
        c = color;
    }
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
        colors: [c],
        legend: {
            show: false,
            backgroundOpacity: 0.5,
            container: legend
        }
    };
    $.plot(x, d1, options);
}
