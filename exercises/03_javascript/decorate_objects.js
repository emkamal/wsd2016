function addPersonMethods(p){
	
	p.greet = function(greetingString){
		console.log(greetingString+", my name is "+p.name);
	}
	
	p.compareAge = function(anotherPersonObject){
		if(p.age == anotherPersonObject.age){
			console.log("My name is "+p.name+" and I'm equally young as "+anotherPersonObject.name);
		}
		else if(p.age > anotherPersonObject.age){
			console.log("My name is "+p.name+" and I'm older than "+anotherPersonObject.name);
		}
		else{
			console.log("My name is "+p.name+" and I'm younger than "+anotherPersonObject.name);
		}
	}
	
	p.namesake = function(anotherPersonObject){
		if(p.name != anotherPersonObject.name){
			console.log("We have different names, "+anotherPersonObject.name+" and I.");
		}
		else{
			console.log("We have the same names, "+anotherPersonObject.name+" and I!");
		}
	}
	
	return p;
}

