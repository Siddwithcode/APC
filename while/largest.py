n = int(input("Enter how many numbers: "))

i = 1

num = int(input("Enter a number: "))
largest = num

while i < n:
    num = int(input("Enter a number: "))
    if num > largest:
        largest = num
    i = i + 1

print("Largest number =", largest)