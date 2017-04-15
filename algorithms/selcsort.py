def selecsort(a):
	min=0
	inc=0
	for i in range (len(a)):
		if a[i]<min:
			min=a[i]
			(a[inc],a[i])=(a[i],a[inc])
			inc+=1