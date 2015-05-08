var redis = require('redis');
var client = redis.createClient();

client.on('connect',function() {
	console.log('connected to redis');
});

var word1 = 'the'
var word2 = 'room'
//check for word 1 and word 2
client.hgetall('hi', function(err, object) {
    var value = object[word1];
    if(value == undefined) {
    	console.log("No word found ")
    	return
    }
    //console.log(value.slice(1,-1))
    //The variable value is a string which needs to be made into an iterative 
    values = value.slice(1,-1).split(')], ')
    values[values.length -1] = values[values.length -1].slice(0,-2)		
    max_value = 0
    string = ''
    //console.log(values)
    for (v in values) {
    	var tuple = values[v];
    	//console.log(values[v])
    	tuple = tuple.split(':')
    	key = tuple[0].slice(1,-1)		//Done
    	tuple = tuple[1].slice(4).split(',')
    	word = tuple[0].slice(0,-1)
    	prob = parseInt(tuple[1].slice(1))
    	//console.log(key)
    	
    	if(key == word2) {
    		console.log(word)
    		console.log(prob)
    		if(max_value < prob) {
    			string = word
    		}	
    	}
    }
	console.log(string)  
});
