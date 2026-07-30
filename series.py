n = int(input("Enter the value of n: "))

fact = 1
i = 1
sum = 1

while i <= n:
    fact = fact * i
    sum = sum + (1 / fact)
    i = i + 1

print("Sum of the series =", sum)