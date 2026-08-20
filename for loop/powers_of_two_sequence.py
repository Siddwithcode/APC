

n = int(input("Enter n: "))

value = 1
for _ in range(n*2): 
    if value > n**2: 
        break
    print(value, end=" ")
    value *= 2

print()
