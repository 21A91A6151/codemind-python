x,y=map(int,input().split())
l=list(map(int,input().split()))
k=list(map(int,input().split()))
for i in k:
    if i in l and k.count(i)==1:
        continue
    else:
        print("No")
        break
else:
    print("Yes")