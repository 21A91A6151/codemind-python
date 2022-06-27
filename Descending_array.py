x=int(input())
l=list(map(int,input().split()))
#print(l)
k=sorted(l)
k=k[::-1]
#print(k)
if k==l:
    print("yes")
else:
    print("no")