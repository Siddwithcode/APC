n = int(input("Enter number of terms: "))

a = 0
b = 1
count = 1

while count <= n:
    print(a)
    c = a + b
    a = b
    b = c
    count = count + 1