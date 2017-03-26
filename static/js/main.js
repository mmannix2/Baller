var app = angular.module('ballerApp', []);
var socket = io.connect('http://' + document.domain + ':' + location.port + '/baller');

app.controller('ballerController', function($scope) {
        
        /*
        $scope.invert = function invert(button) {
            button = !(button);
        };
        */

        $scope.signUp = {
            'name': '',
            'phone': '',
            'available': {
                'sun': true,
                'mon': true,
                'tue': true,
                'wed': true,
                'thu': true,
                'fri': true,
                'sat': true
            },
            'intensity': {
                'fun': false,
                'intense': false,
                'hardcore': false
            },
            'reminder': false
        };
        
        $scope.startAGame = {
            'address': '',
            'city': '',
            'state': '',
            'zip': '',
            'tipOff': '',
            'day': '',
            'intensity': {
                'fun': false,
                'intense': false,
                'hardcore': false
            }
        };

        $scope.upcomingGames = []; 

        $scope.submitSignUp = function submitSignUp() {
            console.log($scope.signUp); 
            
            socket.emit('submitSignUp', signUp);
        };
        
        $scope.submitStartAGame = function submitStartAGame() {
            console.log($scope.startAGame); 
            
            socket.emit('submitStartAGame', startAGame);
        };

        socket.on('connect', function() {
            console.log('Connected.');
        });

        socket.on('upcomingGamesLoaded', function(data) {
            console.log(data);
        });
});
