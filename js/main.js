var app = angular.module('ballerApp', []);

var game1 = {'numPlayers': 4, 'location': '601 F St NW, Washington, DC 20004', 'time': '4:00 PM', 'intensity': 'Hardcore'};
var game2 = {'numPlayers': 6, 'location': '1523 Someroad Rd, Fredericksburg Va', 'time': '12:00 PM', 'intensity': 'Fun'};
var game3 = {'numPlayers': 2, 'location': '742 Evergreen Terrace, Springfield Va', 'time': '9:30 AM', 'intensity': 'Intense'};

app.controller('ballerController', function($scope) {
        
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

        $scope.upcomingGames = [game1, game2, game3];

        $scope.submit = function submit() {
           console.log($scope.signUp); 
        };
        
        $scope.getFirstAddr = function getFirstAddr() {
            console.log($scope.upcomingGames[0].location);
            var converted = "https://www.google.com/maps/embed/v1/search?q=";
            converted.concat(encodeURIComponent($scope.upcomingGames[0].location.trim()));
            converted.concat("&zoom=17&key=AIzaSyCFgAJIwC4I6oYusMKlM4yd1Z2KZiMRInU");

            return converted;
        };
});
