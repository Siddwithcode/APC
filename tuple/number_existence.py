# Store some numbers in a tuple
numbers = (10, 25, 30, 45, 50, 75, 100)
print("Tuple of numbers:", numbers)

# Accept a number from the user
user_num = float(input("Enter a number to check: "))

# Check existence
if user_num.is_integer():
    check_num = int(user_num)
else:
    check_num = user_num

if check_num in numbers:
    print(f"The number {check_num} exists in the tuple.")
else:
    print(f"The number {check_num} does not exist in the tuple.")
