n=5
num=1
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        if i==n:
            print("*",end="")
        else:
            print(num,end="")
            num+=1
    print()