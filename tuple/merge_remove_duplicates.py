# Merge two tuples and remove duplicate elements
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)

merged_unique = tuple(set(tuple1 + tuple2))

print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
print("Merged and De-duplicated Tuple:", merged_unique)
