x=int(input())
temp=x
temp1=x
c=0
ec=0
oc=0
while x>0:
    d=x%10
    x=x//10
    c+=1
while temp>0:
    d=temp%10
    if d%2==0:
        ec+=1
    temp=temp//10
while temp1>0:
    d=temp1%10
    if d%2==1:
        oc+=1
    temp1=temp1//10
if(c==ec):
    print("Even")
elif(c==oc):
    print("Odd")
else:
    print("Mixed")