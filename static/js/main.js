var app = angular.module('ballerApp', []);
var socket = io.connect('http://' + document.domain + ':' + location.port + '/baller');

app.controller('ballerController', function($scope) {
        
        $scope.signUp = {
            'name': '',
            'phone': '',
            'zip': '',
            'zipRange': '',
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
            
            socket.emit('submitSignUp', {
                'signUp': signUp
            });
            /*
                'name': signUp.name,
                'phone': signUp.phone,
                'zip': signUp.zip,
                'zipRange': signUp.zipRange,
                'available': signUp.available,
            });
            */
                /*
                'fun': signUp.intensity['fun'],
                'intense': signUp.intensity['intense'],
                'hardcore': signUp.intensity['hardcore']
            });
                */
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
            $scope.upcomingGames = data;
            $scope.$apply();
        });
});
