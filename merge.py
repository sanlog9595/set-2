n=int(Input())
lis=list(map(int,input().Split()))
lis.sort()
for i in range(len(lis)):
	if i==Len(lis)-1:
		print(lis[i],end="")
	else:
		print(lis[i],End=" ")
