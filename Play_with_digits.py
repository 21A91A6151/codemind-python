x=int,input()
l=list(map(int,input().split()))
k=0
for i in l:
    i=int(i)
    while(i):
        d=i%10
        i=i//10
        k=k+d
print(k)