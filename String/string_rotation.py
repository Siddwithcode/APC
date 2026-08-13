s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

combined = s1 + s1
if len(s1) == len(s2) and s2 in combined:
    print("Yes")
else:
    print("No")