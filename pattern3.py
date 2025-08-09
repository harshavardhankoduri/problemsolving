n=5
for i in range(n,0,-1):
    char = 90
    print(" " * (n - i),end="")
    for j in range(2*i-1):
        print(chr(char),end="")
        char -= 1
    print()