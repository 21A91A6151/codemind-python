x=int(input())
d1,i,n=0,0,0
for i in range(x):
    k=int(input())
    i=0
    d1=0
    while k!=0:
        d=k%10
        k=k//10
        d1=d1+d*pow(2,i)
        i+=1
    print(d1)
    
    