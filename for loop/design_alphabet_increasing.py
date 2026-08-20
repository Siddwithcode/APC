n = int(input("Enter n: "))
for i in range(1, n + 1):
    line = ''
    for j in range(i):
        line += chr(65 + j) + ' '
    print(line.rstrip())