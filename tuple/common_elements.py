# Create two tuples and find the common elements
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)

common = tuple(set(tuple1) & set(tuple2))

print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
print("Common elements:", common)
