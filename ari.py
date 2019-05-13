a = [int(i) for i in input().split()]
K=0
for i in range(1,a[0]+1):
K+=a[1]+(i-1)*a[2]
print(K)
