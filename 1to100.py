def print_numbers(n):
    if n > 100:
        return
    print(n)
    print_numbers(n + 1)

print_numbers(1)
print("\n".join(map(str, range(1, 101))))
