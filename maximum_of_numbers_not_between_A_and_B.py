x=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
s=[]
for i in range(len(l)):
    if l[i]>=a and l[i]<=b:
        continue
    else:
        s.append(l[i])
h=len(s)
if h==0:
    print("-1")
else:
    print(max(s))
        