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
                $scope.$apply(function(){
                   $scope.searchM=data;
                });
            },
            error: function(result){
                    alert(result.status + ' ' + result.statusText);
            }
        });
    }
};


