numbers = []

for i in range(5):
    n = int(input("Enter a number: "))
    numbers.append(n)

t = tuple(numbers)

print("List:", numbers)
print("Tuple:", t)