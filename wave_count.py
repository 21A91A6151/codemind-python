x=int(input())
l=list(map(int,input().split()))
k=0
h=0
for i in range(0,len(l)-2,2):
    if l[i]<l[i+1] and l[i+1]>l[i+2]:
        h+=1
    else:
        k+=1
if k>0:
    print("-1")
else:
    print(h)