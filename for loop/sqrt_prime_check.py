import math

num = int(input("Enter a number: "))
root = int(math.sqrt(num))

if root * root != num:
    print("Square root is not an integer")
elif root < 2:
    print("Square root is not prime")
else:
    for i in range(2, int(math.sqrt(root)) + 1):
        if root % i == 0:
            print("Square root is not prime")
            break
    else:
        print("Square root is prime")
