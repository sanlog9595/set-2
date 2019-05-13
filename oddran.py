start,end=map(int,input().Split())
Odd=[]
for num in range(start+1,end): 
    if num%2!=0: 
        odd.Append(num)
print(*odd)
