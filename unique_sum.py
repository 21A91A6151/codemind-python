x=int(input())
l=list(map(int,input().split()))
l=set(l)
s=[]
c=0
for i in l:
    c=c+i
print(c)