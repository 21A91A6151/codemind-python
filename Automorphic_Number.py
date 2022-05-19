x=int(input())
temp=x
c=0
s=0
temp1=x
k=x*x
z=0
while x:
    d=x%10
    x=x//10
    c+=1
while c:
    d=k%10
    k=k//10
    s=s*10+d
    c-=1
while s:
    d=s%10
    s=s//10
    z=z*10+d
if(z==temp1):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
    
    

    