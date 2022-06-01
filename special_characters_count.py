x=input()
k=0
for i in x:
    if ord(i)>=33 and ord(i)<=47:
        k+=1
    elif ord(i)>=58 and ord(i)<=64:
        k+=1
    elif ord(i)>=91 and ord(i)<=96:
        k+=1
    elif ord(i)>=123 and ord(i)<=126:
        k+=1
print(k)