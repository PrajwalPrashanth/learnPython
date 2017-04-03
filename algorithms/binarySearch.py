def bsearch(list,k,a,b):
	if(a-b)==0:
		return("not found")
	mid=(a+b)//2
	if list[mid]==k:
		return("found")
	elif(k>list[mid]):
		return(bsearch(list,k,mid+1,b))
	else:
		return(bsearch(list,k,a,mid))