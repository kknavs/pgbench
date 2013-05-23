angular.module('pgbench', ['pgbenchServices']).filter('isodate', function(){
   return function(datetime){
       //začasna rešitev, ne vem zakaj v db datumu manjka offset
 	   return datetime.split(".")[0]+".000+0200";
   };
});

//preverjanje, če jquery selektor obstaja
$.fn.exists = function () {
    return this.length !== 0;
};



