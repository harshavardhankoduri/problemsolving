n=5
value=65
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(chr(value), end="")
        value += 1
    print()