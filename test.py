flist = list(map(int,input().split()))
maxc = 0
count =1 
for i in range (len(flist)-1):
    if(flist[i]<flist[i+1]):
        count+= 1
    else:
        if(maxc<count):
            maxc = count
            count = 1
print(maxc)


int("6")
