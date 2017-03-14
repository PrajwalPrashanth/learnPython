def isprime(x):
	if(x==1):
		return ("x is prime")
	for i in range(2,x):
		if x%i == 0:
			p="x is not prime"
			return(p)
	return ("x is prime")
def primesUpto(n):
	plist = [1]
	for i in range(2,n+1):
		if isprime(i) == "x is prime":
			plist = plist + [i]
	print (plist)