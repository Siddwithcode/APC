tuple1 = (10, 20, 30, 40)
tuple2 = (30, 40, 50, 60)

merged = tuple1 + tuple2

result = ()

for x in merged:
    if x not in result:
        result = result + (x,)

print("Merged Tuple:", result)