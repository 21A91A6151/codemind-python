x=int(input())
s=x*x
temp=s
k=0
while(s):
    d=s%10
    s=s//10
    k=k+d
if(temp%k==0):
    print("True")
else:
    print("False")