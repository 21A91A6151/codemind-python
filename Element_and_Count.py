x=int(input())
l=list(map(int,input().split()))
s=[]
for i in l:
    k=l.count(i)
    if i not in s:
        s.append(i)
        print(i,k,end=" ")