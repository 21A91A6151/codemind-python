x=int(input())
l=list(map(int,input().split()))
k=l[::-1]
s=[]
for i in range(x//2):
    s.append(l[i])
    s.append(k[i])
if x%2!=0:
    s.append(l[x//2])
    s.append("0")
print(*s)
        