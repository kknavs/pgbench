angular.module('pgbenchServices', ['ngResource'])
    .factory('Measures', function($resource){
        return $resource('/api/v1/measures', {}, {
            query: {method:'GET', isArray:false}
        });
    });
