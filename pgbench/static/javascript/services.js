angular.module('pgbenchServices', ['ngResource'])
    .factory('Measures', function($resource){
        return $resource('/api/v1/measures', {}, {
            query: {method:'GET', isArray:false}
        });
    })
   .factory('SearchM', function($resource){
        return $resource('/api/v1/measures/search', {}, {
            query: {method:'GET', isArray:false}
        });
    });
