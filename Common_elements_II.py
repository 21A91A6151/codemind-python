x,y=map(int,input().split())
l=list(map(int,input().split()))
k=list(map(int,input().split()))
s=l+k
for i in s:
    if s.count(i)==1:
        print(i,end=" ")