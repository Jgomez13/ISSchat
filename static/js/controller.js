
var ISSChatApp = angular.module('ISSChatApp',[]);

ISSChatApp.controller('ChatController', function($scope){
	console.log('new Doing Something'); 
	var socket = io.connect('http://'+ document.domain + ':'
		+ location.port +'/iss');

	$scope.messages= [];
	$scope.name = '';
	$scope.text = '';
	$scope.setName = function setName(){
		socket.emit('identify', $scope.name)
	};

	socket.on('message',function(msg){
		console.log('in message');
		console.log(msg);
		$scope.messages.push(msg);
		$scope.$apply(); // applies message in the view next to Some messages here!
		var elem = document.getElementById('msgpane'); //grabs the message from 
														//input to the msgpane
		elem.scrollTop = elem.scrollHeight;

	});

	socket.on('connect',function(){
		console.log('connected');

	});

});
