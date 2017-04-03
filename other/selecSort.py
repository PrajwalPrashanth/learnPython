def sSort(list):
	min = list[0]
	slist = []
	while len(slist) != len(list):
		for i in range(len(list)):
			if(min>list[i]):
				min=list[i]
		slist.append(min)
		list.remove(min)
	retrun(slist)
		