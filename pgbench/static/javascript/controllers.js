function pgbenchCtrl($scope, Measures) {
    $scope.measures = Measures.query();
    $scope.alertTPS = function(){
        var x = $scope.measures['objects'];
        var y = new Array(x.length) ;
        //mora bit nova spremenljivka, drugače se vrednosti prepišejo
       $.each(x, function(index, val) {
           y[index] = val.TPSConnEstablish;
        });
        alert(y);
    }
}
