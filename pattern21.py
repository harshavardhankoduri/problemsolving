n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == n or j == n:
            print("*", end="")
        elif i == 2 and j == 4:
            print("*",end="")
        elif i ==3  and j == 3:
            print("*",end="")
        elif i == 4 and j == 2:
            print("*",end="")
        else:
            print(" ", end="")   
    print()