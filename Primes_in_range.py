def prime(i):
    for j in range(2,int(i**0.5+1)):
        if i%j==0:
            return 0
    else:
        return 1
x=int(input())
y=int(input())
k=0
for i in range(x,y+1):
    if i==1:
        continue
    if prime(i) and i!=1:
        k+=1
print(k)