import math

num = int(input("Enter a number: "))

root = int(math.sqrt(num))

if root * root != num:
    print("Square root is not an integer.")
else:
    prime = True

    if root <= 1:
        prime = False
    else:
        for i in range(2, root):
            if root % i == 0:
                prime = False
                break

    if prime:
        print("Square root =", root)
        print("Square root is Prime")
    else:
        print("Square root =", root)
        print("Square root is Not Prime")