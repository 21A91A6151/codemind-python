x=int(input())
k=x*x
s=0
while k:
    d=k%10
    k=k//10
    s=s+d
if s==x:
    print("Neon Number")
else:
    print("Not Neon Number")