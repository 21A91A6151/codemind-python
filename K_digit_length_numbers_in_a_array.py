x,y=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in range(len(l)):
    l[i]=abs(l[i])
    l[i]=str(l[i])
    if len(l[i])==y:
        c+=1
print(c)