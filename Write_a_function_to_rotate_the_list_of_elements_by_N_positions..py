x=int(input())
l=list(map(int,input().split()))
y=int(input())
for i in range(y):
    n=l.pop()
    l.insert(0,n)
print(*l)