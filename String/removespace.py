s = input("Enter a string: ")
result = ""
for ch in s:
    if ch != " ":
        result = result + ch
print("Without spaces:", result)