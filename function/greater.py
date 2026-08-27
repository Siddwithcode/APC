def greater(a, b):
    if a > b:
        return a
    else:
        return b


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Greater number =", greater(num1, num2))