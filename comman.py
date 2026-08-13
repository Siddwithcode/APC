
tuple1 = (10, 20, 30, 40, 50)
tuple2 = (30, 40, 50, 60, 70)

common = ()

for x in tuple1:
    if x in tuple2:
        common = common + (x,)

print("Common Elements:", common)






















