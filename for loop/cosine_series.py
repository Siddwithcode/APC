x = float(input("Enter x (in radians): "))
n = int(input("Enter number of terms: "))
sum_val = 1.0
factorial = 1
sign = -1
for i in range(2, 2 * n, 2):
    factorial *= i * (i - 1)
    sum_val += sign * (x ** i) / factorial
    sign *= -1
print("cos(x) approx =", sum_val)