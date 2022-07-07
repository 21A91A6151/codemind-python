x=input()
s=len(x)
c=0
for i in x:
    if x.count(i)==1:
        c+=1
if c==s:
    print("True")
else:
    print("False")