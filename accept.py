
numbers = []

for i in range(10):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)


total = sum(numbers)
average = total / len(numbers)


print("Numbers:", numbers)
print("Sum =", total)
print("Average =", average)