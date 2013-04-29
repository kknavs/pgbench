$(document).ready(function () {

    $("#graph").click(function(){
        var x = angular.element('[ng-controller=pgbenchCtrl]').scope().measures['objects'];
        var y = new Array(x.length) ;
        //mora bit nova spremenljivka, drugače se vrednosti prepišejo
       $.each(x, function(index, val) {
           y[index] = val.TPSConnEstablish;
        });
        alert(y);

    });


});