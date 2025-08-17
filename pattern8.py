#      *
#     ***
#    *****
#  1234567
# abcdefghi
n=5
for i in range(1,n+1):
    aplha = 97
    print(" "*(n-i),end="")
    for j in range(1,(i*2)):
        if i <= 3:
            print("*", end="")
        elif i == 4:
            print(j,end="")
        else:
            print(chr(aplha), end="")
            aplha += 1
    print()
n=5
for i in range(1,n+1):
    aplha = 65
    print(" "*(n-i),end="")
    for j in range(1,(i*2)):
        if i <= 3:
            print("*", end="")
        elif i == 4:
            print(j,end="")
        else:
            print(chr(aplha), end="")
            aplha += 1
    print()
