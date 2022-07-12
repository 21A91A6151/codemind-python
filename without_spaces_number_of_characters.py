x=input()
k=0
for i in x:
    if i in " ":
        continue
    else:
        k+=1
print(k)