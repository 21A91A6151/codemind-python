x=int(input())
l=list(map(int,input().split()))
l=sorted(l)
if(x%2!=0):
    print(l[len(l)//2])
else:
    print(l[(len(l)+1)//2])