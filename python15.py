n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1:
            print("*",end="")
        elif i==n:
            print("*",end="")
        elif j==1:
            print("*",end="")
        elif j==n:
            print("*",end="")
        else:
            print(" ",end="")
    print()