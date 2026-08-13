t = (10, 20, 30, 40)

print("Original Tuple:", t)

lst = list(t)

lst[2] = 100

t = tuple(lst)

print("Modified Tuple:", t)