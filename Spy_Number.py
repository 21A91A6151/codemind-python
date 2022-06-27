x=int(input())
k=str(x)
s=0
h=1
for i in k:
    i=int(i)
    s+=i
for i in k:
    i=int(i)
    h*=i
if h==s:
    print("Spy Number")
else:
    print("Not Spy Number")