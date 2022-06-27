x=int(input())
z=0
l=list(map(int,input().split()))
k=set(l)
k=list(k)
for i in range(len(k)):
    if k[i]%2==0:
        z=z+k[i]
print(z)