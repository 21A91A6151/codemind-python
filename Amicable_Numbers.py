x=int(input())
y=int(input())
k=0
s=0
for i in range(1,x):
    if x%i==0:
        k=k+i
for i in range(1,y):
    if y%i==0:
        s=s+i
if s==x and k==y:
    print("Amicable")
else:
    print("Not Amicable")