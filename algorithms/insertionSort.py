def isort(a):
	for i in range(len(a)):
		pos=i
		while pos>0 and a[pos]<a[i-1]:
			(a[pos],a[i-1])=(a[i-1],a[pos])
			pos -= 1
	print (a)