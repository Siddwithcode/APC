# Create a tuple
original_tuple = ("apple", "banana", "cherry")
print("Original Tuple:", original_tuple)

# Convert to list
temp_list = list(original_tuple)

# Modify an element
temp_list[1] = "blueberry"

# Convert back to tuple
modified_tuple = tuple(temp_list)

print("Modified Tuple:", modified_tuple)
