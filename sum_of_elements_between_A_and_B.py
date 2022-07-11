x=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
s=[]
k=0
for i in range(len(l)):
    if l[i]>=a and l[i]<=b:
        s.append(l[i])
    else:
        continue
for i in s:
    k=k+i
print(k)