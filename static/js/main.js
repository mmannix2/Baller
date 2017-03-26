var app = angular.module('ballerApp', []);

app.controller('ballerController', function($scope) {
        
        var socket = io.connect('https://' + document.domain + ':' + location.port + '/baller');
        
        $scope.signUp = [];
        $scope.signUp.available = {
            'sun': true,
            'mon': true,
            'tue': true,
            'wed': true,
            'thu': true,
            'fri': true,
            'sat': true
        };

        $scope.upcomingGames = undefined; 

        $scope.submit = function submit() {
           console.log($scope.signUp); 
        };

        socket.on('connect', function() {
            console.log('Connected.');
        });
});
