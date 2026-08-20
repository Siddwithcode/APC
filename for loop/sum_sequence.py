n = int(input("Enter n: "))
fact = 1
sum_val = 1.0
for i in range(1, n + 1):
    fact *= i
    sum_val += 1 / fact
print("Sum =", sum_val)