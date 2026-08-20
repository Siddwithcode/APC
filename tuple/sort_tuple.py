# Convert a tuple into a sorted tuple
original_tuple = (42, 15, 8, 93, 71, 25)
print("Original Tuple:", original_tuple)

ascending_sorted = tuple(sorted(original_tuple))
print("Sorted (Ascending) :", ascending_sorted)

descending_sorted = tuple(sorted(original_tuple, reverse=True))
print("Sorted (Descending):", descending_sorted)
