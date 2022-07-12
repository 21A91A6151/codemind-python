x=int(input())
l=list(map(int,input().split()))
s=[]
for i in l:
    if l.count(i)==i:
        s.append(i)
if len(s)==0:
    print("-1")
else:
    print(min(s),max(s))