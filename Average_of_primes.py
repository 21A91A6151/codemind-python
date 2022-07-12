def prime(i):
    for j in range(2,int(i**0.5+1)):
        if i%j==0:
            return 0
    else:
        return 1
x=int(input())
l=list(map(int,input().split()))
k=0
h=0
for i in l:
    if i==1:
        continue
    if prime(i):
        k=k+i
        h+=1
s=k/h
print("{:.2f}".format(s))