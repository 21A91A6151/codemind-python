import math
x=int(input())
l=list(map(int,input().split()))
s=[]
for i in l:
    i=abs(i)
    i=str(i)
    i=len(i)
    s.append(i)
k=max(s)
for i in range(len(s)):
    if s[i]==k:
        print(l[i],end=" ")