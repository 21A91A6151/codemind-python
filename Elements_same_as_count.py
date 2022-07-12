x=int(input())
l=list(map(int,input().split()))
s=[]
for i in l:
    if l.count(i)==i:
        if i not in s:
            s.append(i)
k=len(s)
if k==0:
    print("-1")
else:
    print(*s)