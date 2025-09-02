n=5
for i in range(n,0,-1):
    a=97
    b=65
    for j in range(1,i+1):
        if i>=n-1:
            print(j,end="")
        elif i==3:
            print(chr(a),end="")
        elif i==2:
            print(chr(b),end="")
        elif i==1:
            print("*",end="")
        a+=1
        b+=1
    print()