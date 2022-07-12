def prime(i):
    for j in range(2,i):
        if i%j==0:
            return 0
    else:
        return 1
x=int(input())
l=list(map(int,input().split()))
k=0
for i in l:
    if i==1:
        continue
    if prime(i):
        k=k+1
print(k)