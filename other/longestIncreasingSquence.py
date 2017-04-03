def lseq(flist):
	max = 0
	count =1 
	for i in range (len(flist)-1):
		if (flist[i]<flsit[i+1]):
			count += 1
		else:
			if(max<count):
				max = count
			count = 1
		print(max)

lseq(int(input().split(" ")))