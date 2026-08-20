# Store 15 integers in a tuple
numbers = (12, 7, 19, 24, 30, 5, 8, 11, 42, 55, 60, 67, 72, 81, 90)

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Tuple of 15 integers:", numbers)
print("Count of Even numbers:", even_count)
print("Count of Odd numbers:", odd_count)
