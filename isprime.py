def isprime(x):
	if(x==1):
		print ("x is prime")
		return
	for i in range(2,x):
		if x%i == 0:
			p="x is not prime"
			return(p)
	print ("x is prime")