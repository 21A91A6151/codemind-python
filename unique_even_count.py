x=int(input())
l=list(map(int,input().split()))
s=[]
c=0
for i in range(len(l)):
    if l[i]%2==0:
        if l[i] not in s:
            s.append(l[i])
            c+=1
print(c)