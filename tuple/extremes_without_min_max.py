# Store numbers in a tuple
numbers = (23, 56, 12, 89, 45, 6, 78)

# Initialize largest and smallest with the first element
largest = numbers[0]
smallest = numbers[0]

# Loop to find largest and smallest
for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Tuple:", numbers)
print("Largest number:", largest)
print("Smallest number:", smallest)
