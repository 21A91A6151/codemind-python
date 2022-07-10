x,y=map(int,input().split())
l=list(map(int,input().split()))
l=set(l)
k=list(map(int,input().split()))
k=set(k)
c=0
for i in l:
    if i in k:
        c+=1
print(c)