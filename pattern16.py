n=5
for i in range(1,n+1):
    a=97
    b=65
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        if i==1:
            print("*",end="")
        elif i==2:
            print("@",end="")
        elif i==3:
            print("#",end="")
        elif i==4:
            print(chr(a),end="")
        elif i==5:
            print(chr(b),end="")  
        a+=1      
        b+=1
    print()
            