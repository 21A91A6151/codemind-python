x=int,input()
l=list(map(int,input().split()))
for i in l:
    i=abs(i)
    i=str(i)
    print(len(i),end=" ")