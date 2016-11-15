def keyword_usage( string, keywords ):
	
	words = string.split()
	result = ()
	
	for keyword in keywords:
		if keyword in words:
			result = result + (True,)
		else:
			result = result + (False,)
			
	s = 'er'.join(['cat', 'pillar'])
	
	alist = [2*i for i in range(4) if i%3 == 0]
	print(alist)
	
	return result