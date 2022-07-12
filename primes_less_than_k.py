def prime(i):
    for j in range(2,i):
        if i%j==0:
            return 0
    else:
        return 1
x=int(input())
l=list(map(int,input().split()))
k=int(input())
h=0
for i in l:
    if i==1:
        continue
    if i<=k:
        if prime(i):
            h+=1
print(h)