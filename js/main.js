var app = angular.module('ballerApp', []);

var game1 = {'numPlayers': 4, 'location': 'Kevin\'s House', 'time': '4:00 PM'};
var game2 = {'numPlayers': 6, 'location': '1523 Someroad Rd, Fredericksburg Va', 'time': '12:00 PM'};
var game3 = {'numPlayers': 2, 'location': '742 Evergreen Terrace, Springfield Va', 'time': '9:30 AM'};

app.controller('ballerController', function($scope) {
        $scope.signUp = [];
        
        //$scope.upcomingGames = [ 'location': 'My House', 'location': 'The old haunted Basketball Court near the mill.'  ];
        $scope.upcomingGames = [game1, game2, game3];

        $scope.submit = function submit() {
           console.log($scope.signUp); 
        };
});
