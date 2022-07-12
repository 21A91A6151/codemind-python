x=input()
a=0
e=0
h=0
o=0
z=0
u=0
for i in x:
    if i in 'a':
        a+=1
    elif i in 'e':
        e+=1
    elif i in 'i':
        h+=1
    elif i in 'o':
        o+=1
    elif i in 'u':
        u+=1
if a==0:
    z+=1
    print("a",end=" ")
if e==0:
    z+=1
    print("e",end=" ")
if h==0:
    z+=1
    print("i",end=" ")
if o==0:
    z+=1
    print("o",end=" ")
if u==0:
    z+=1
    print("u",end=" ")
if z==0:
    print("0",end=" ")