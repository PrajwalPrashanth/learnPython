def prime(p):
	if(p==1):
		return(1)
	for i in range(p-1,2,-1):
		if p%i == 0:
			return(0)
	return(1)
def maxPrimeFac(n):
	for i in range(n,1,-2):
		if (n%i == 0):
			if (prime(i) == 1):
				return i
