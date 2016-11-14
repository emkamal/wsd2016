def keyword_usage( string, keywords ):
	
	result = ()
	
	for keyword in keywords:
		if keyword in string:
			result = result + (True,)
		else:
			result = result + (False,)
	
	return result