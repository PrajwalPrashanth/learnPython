def min(b,a):
	minpos=b
	for i in range(b,len(a)):
		if a[i]<a[minpos]:
			minpos=i
	return (minpos)
def selecsort(a):
	for i in range(len(a)):
		m=min(i,a)
		if a[i]>a[m]:
			(a[i],a[m])=(a[m],a[i])
	print (a)