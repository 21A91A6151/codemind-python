x=input()
w=x.split()
for i in range(len(w)):
    if i%2==0:
        z=w[i][::-1]
        print(z,end=" ")
    else:
        print(w[i],end=" ")