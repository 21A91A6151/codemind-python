x=int(input())
l=list(map(int,input().split()))
y=int(input())
m=list(map(int,input().split()))
h=int(input())
c=0
for i in range(x):
    if l[i]<=h and m[i]>=h:
        c+=1
print(c)
    