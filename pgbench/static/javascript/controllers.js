function pgbenchCtrl($scope, Measures) {
    $scope.measures = Measures.query();
}

function pgbenchCtrlS($scope, SearchM) {
    $scope.searchM = SearchM.query();
    $scope.find = function(q){
        $.ajax({
            type: 'GET',
            url: '../api/v1/measures/search/?format=json',
            contentType: "application/json; charset=utf-8",
            data: {'q':q},
            dataType:'json',
            success: function (data) {
                $scope.searchM=data;
                //alert(data['objects'].length);
                var s='<tr><th>Id</th> <th>Title</th></tr>' //other poss.?
                console.log(data['objects'].length);
                for (var i = 0; i < data['objects'].length; i++) {
                 s+="<tr> <td>" + data['objects'][i]['id'] + "</td><td>" + data['objects'][i]['title'] + "</td></tr>"
                }
                $('.table').html(s);
            },
            error: function(result){
                    alert(result.status + ' ' + result.statusText);
            }
        });
    }
};


