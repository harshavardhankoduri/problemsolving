rows = 5
for i in range(rows):
    num_chars = 2 * i + 1
    start_char = i % 2
    line = ''.join(str((start_char + j) % 2) for j in range(num_chars))
    print(line.center(2 * rows - 1))