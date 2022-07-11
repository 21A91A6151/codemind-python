x=int(input())
l=list(map(int,input().split()))
k=0
for i in range(3,len(l)):
    if l[i]==l[i-1]+l[i-2]:
        k+=1
if k+3==x:
    print("yes")
else:
    print("no")
