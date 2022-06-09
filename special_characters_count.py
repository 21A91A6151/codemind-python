x=input()
c=0
for i in x:
    if i.isdigit():
        continue
    elif i.isalpha():
        continue
    elif i==chr(32):
        continue
    else:
        c+=1
print(c)