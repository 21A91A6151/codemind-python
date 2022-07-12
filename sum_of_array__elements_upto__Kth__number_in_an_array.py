x=int(input())
l=list(map(int,input().split()))
h=int(input())
k=0
for i in l:
    if i==h:
        k=k+i
        break
    else:
        k=k+i
print(k)