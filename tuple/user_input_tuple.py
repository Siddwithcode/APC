# Accept five numbers from user and store them in a list
numbers_list = []
print("Enter 5 numbers:")
for i in range(5):
    num = float(input(f"Enter number {i+1}: "))
    numbers_list.append(num)

# Convert the list into a tuple
numbers_tuple = tuple(numbers_list)

print("List of numbers:", numbers_list)
print("Tuple of numbers:", numbers_tuple)
