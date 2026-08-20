# Store elements in a tuple
numbers = (10, 20, 30, 40, 50)

# Calculate sum and length to find average
total_sum = sum(numbers)
count = len(numbers)
average = total_sum / count if count > 0 else 0

print("Tuple:", numbers)
print("Average of elements:", average)
