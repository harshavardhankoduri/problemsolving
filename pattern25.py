n=5
for i in range(n):
    print(" "*(n-i-1),end="")
    for j in range(2*i+1):
        if j==0 or j==2*i:
            print("*",end="")
        else:
            print(" ",end="")
    print()