x=input()
z=input()
v=0
for i in range(len(x)):
    if x[i]==z:
        v+=1
        print("True")
        print(i)
        break
if(v==0):
    print("False")
        
    