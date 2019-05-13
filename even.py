x,y = input().Split(" ")
x=int(x)
y=int(y)
l=[]
for i in Range(x+1,y):
    if (i%2==0):
        l.Append(str(i))
    else:
        pass
print(" ".join(l))
