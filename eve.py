
numbers = []
for i in range(15):
    num = int(input("Enter an integer: "))
    numbers.append(num)


even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even= even + 1
    else:
        odd = odd + 1


print("Numbers:", numbers)
print("Even numbers:", even)
print("Odd numbers:", odd)