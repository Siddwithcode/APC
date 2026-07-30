import math

x = float(input("Enter value of x (in radians): "))
n = int(input("Enter the maximum power (even number): "))

sum = 1
sign = -1

for i in range(2, n + 1, 2):
    fact = 1
    for j in range(1, i + 1):
        fact = fact * j

    sum = sum + sign * (x ** i) / fact
    sign = sign * -1

print("Cos(x) =", sum)