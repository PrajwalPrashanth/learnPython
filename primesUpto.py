def primesUpto(n):
	plist = [1]
	for i in range(3,n):
		if n%i:
			plist = plist + [i]
			n = n + 2
	plist + [n]
	print (plist)