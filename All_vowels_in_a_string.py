x=input()
a=0
e=0
k=0
o=0
u=0
for i in x:
    if i in 'a':
        a+=1
    elif i in 'e':
        e+=1
    elif i in 'i':
        k+=1
    elif i in 'o':
        o+=1
    elif i in 'u':
        u+=1
    else:
        pass
if a>=1 and e>=1 and k>=1 and o>=1 and u>=1:
    print("True")
else:
    print("False")