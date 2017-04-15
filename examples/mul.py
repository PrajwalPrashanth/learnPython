def mul(m,n):
	if (n==0):
		return 0
	return m+mul(m,n-1)
	
	