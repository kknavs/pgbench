function pgbenchCtrl($scope, Measures) {
    $scope.measures = Measures.query();
          $scope.message = '';


        $scope.columnDefs = [
            { "mDataProp": "id", "aTargets":[0]},
            { "mDataProp": "title", "aTargets":[1] },
            { "mDataProp": "user", "aTargets":[2] },
            { "mDataProp": 'date', "aTargets":[3]},
            { "mDataProp": "transactionType", "aTargets":[4] },
            { "mDataProp": "scalingFactor", "aTargets":[5] },
            { "mDataProp": "threads", "aTargets":[6]},
            { "mDataProp": "clients", "aTargets":[7] },
            { "mDataProp": "transactionsPerClient", "aTargets":[8] },
            { "mDataProp": "transactions", "aTargets":[9]},
            { "mDataProp": "TPS", "aTargets":[10] },
            { "mDataProp": "TPSConnEstablish", "aTargets":[11] },
            { "mDataProp": "fields", "aTargets":[12] }
        ];

        $scope.overrideOptions = {
            "bStateSave": true,
            "iCookieDuration": 2419200, /* 1 month */
            "bJQueryUI": false,
            "bPaginate":true,
            "bLengthChange": true,
            "bFilter": false,
            "bInfo": true,
            "bDestroy": true,
            "bSortClasses": true,
            "sPaginationType": "full_numbers",
            "oLanguage": {
            "sSearch": "Search all columns:"
        }, "sDom": '<"top"i>rt<"bottom"plf><"clear">'
        };
}

function pgbenchCtrlS($scope, SearchM) {
      $scope.message = '';

        $scope.myCallback = function(nRow, aData, iDisplayIndex, iDisplayIndexFull) {
            $('td:eq(2)', nRow).bind('click', function() {
                $scope.$apply(function() {
                    $scope.someClickHandler(aData);
                });
            });
            return nRow;
        };

        $scope.someClickHandler = function(info) {
            $scope.message = 'clicked: '+ info.price;
        };


        $scope.columnDefs = [
            { "mDataProp": "id", "aTargets":[0]},
            { "mDataProp": "title", "aTargets":[1] },
            { "mDataProp": "user", "aTargets":[2] },
            { "mDataProp": 'date', "aTargets":[3]},
            { "mDataProp": "transactionType", "aTargets":[4] },
            { "mDataProp": "scalingFactor", "aTargets":[5] },
            { "mDataProp": "threads", "aTargets":[6]},
            { "mDataProp": "clients", "aTargets":[7] },
            { "mDataProp": "transactionsPerClient", "aTargets":[8] },
            { "mDataProp": "transactions", "aTargets":[9]},
            { "mDataProp": "TPS", "aTargets":[10] },
            { "mDataProp": "TPSConnEstablish", "aTargets":[11] },
            { "mDataProp": "fields", "aTargets":[12] }
        ];

        $scope.overrideOptions = {
            "bStateSave": true,
            "iCookieDuration": 2419200, /* 1 month */
            "bJQueryUI": false,
            "bPaginate":true,
            "bLengthChange": true,
            "bFilter": false,
            "bInfo": true,
            "bDestroy": true,
            "bSortClasses": true,
            "sPaginationType": "full_numbers",
            "oLanguage": {
            "sSearch": "Search all columns:"
        }, "sDom": '<"top"i>rt<"bottom"plf><"clear">'
        //"asStripeClasses":['even','odd']  za barvanje sode-lihe vrstice
        };


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
}
