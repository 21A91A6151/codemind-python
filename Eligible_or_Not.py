for i in range(int(input())):
    a,b,c=map(int,input().split())
    if(c>=a and c<b):
        print("YES")
    else:
        print("NO")