x=int(input())
l=list(map(int,input().split()))
c=0
k=min(l)
k=str(k)
s=len(k)
for i in l:
    i=str(i)
    if len(i)==s:
        c+=1
print(c)
        