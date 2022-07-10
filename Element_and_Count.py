x=int(input())
l=list(map(int,input().split()))
s=[]
for i in l:
    if i not in s:
        s.append(i)
        k=l.count(i)
        print(i,k,end=" ")