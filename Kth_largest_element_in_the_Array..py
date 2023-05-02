x=int(input())
l=list(map(int,input().split()))
k=int(input())
l=set(l)
l=sorted(l)
l=l[::-1]
print(l[k-1])