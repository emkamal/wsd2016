function keywordusage(text, keywords){
	result = [];
	
	for(var i = 0, l = keywords.length; i < l; i++){
		if( text.indexOf(keywords[i]) == -1 ){
			result[i] = false;
		}
		else{
			result[i] = true;
		}
	}
	
	return result;
}

function frequencies(text, wordlist){
	result = {};
	
	for(var i = 0, l = wordlist.length; i < l; i++){
		var regex = new RegExp( wordlist[i], 'g' );
		wordcount = text.match(regex).length;
		
		result[wordlist[i]] = wordcount 
	}
	
	return result;
}


function rotate(array, steps=1){
	if(steps == 0){
		return array;
	}
	else if(steps > 0){
		for(var i = 0; i < steps; i++){
			lastEl = array.pop();
			array.unshift(lastEl);
		}
	}
	else{
		for(var i = 0; i > steps; i--){
			firstEl = array.shift();
			array.push(firstEl);
		}
	}
	return array;
}

function arrayRotate(arr, count) {
  count -= arr.length * Math.floor(count / arr.length)
  arr.push.apply(arr, arr.splice(0, count))
  return arr
}