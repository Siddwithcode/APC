n = int(input("Enter how many numbers: "))

i = 1

num = int(input("Enter a number: "))
smallest = num

while i < n:
    num = int(input("Enter a number: "))
    if num < smallest:
        smallest = num
    i = i + 1

print("Smallest number =", smallest)