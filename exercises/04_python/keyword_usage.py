def keyword_usage( string, keywords ):
	
	words = string.split()
	result = ()
	
	for keyword in keywords:
		if keyword in words:
			result = result + (True,)
		else:
			result = result + (False,)
	
	return result