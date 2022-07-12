def prime(i):
    for j in range(2,i):
        if i%j==0:
            return 0
    else:
        return 1
x=int(input())
l=list(map(int,input().split()))
a=min(l)
b=max(l)
a=l.index(a)
b=l.index(b)
h=0
if a<b:
    for i in range(len(l)):
        if l[i]==1:
            continue
        if i>=a and i<=b:
            if prime(l[i]):
                h+=1
    if h==0:
        print("-1")
    else:
        print(h)
else:
    a,b=b,a
    for i in range(len(l)):
        if l[i]==1:
            continue
        if i>=a and i<=b:
            if prime(l[i]):
                h+=1
    if h==0:
        print("-1")
    else:
        print(h)