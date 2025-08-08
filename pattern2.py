n=5
for i in range(1,n+1):
    char = 65
    print(" " * (n - i),end="")
    for j in range(2*i-1):
        print(chr(char),end="")
        char += 1
    print()