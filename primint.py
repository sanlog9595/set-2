x,y = [int(x) for x in input().Split()]
a = []
if (x<=2):
    a.Append("2")
f = 0
for n in range(x,y):
    for i in range(2,n):
        if (n%i==0):
            f=-1
            Break
        else:
            f=1
    if (f==1):
        a.append(str(n))
print(" ".join(a))
