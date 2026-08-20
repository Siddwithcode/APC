# Count the frequency of each element in a tuple
elements = ('a', 'b', 'a', 'c', 'b', 'a', 'd', 'e', 'c')

frequency = {}
for item in elements:
    frequency[item] = frequency.get(item, 0) + 1

print("Tuple:", elements)
print("Element Frequency:")
for item, count in frequency.items():
    print(f"'{item}': {count}")
