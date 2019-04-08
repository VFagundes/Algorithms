var _initial = '2019-04-07T18:57:28.593Z';
var fromTime = new Date(_initial);
var toTime = new Date();

var differenceTravel = toTime.getTime() - fromTime.getTime();
var seconds = Math.floor((differenceTravel) / (1000));
console.log(seconds,toTime,_initial);