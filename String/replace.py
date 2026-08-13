s = input("Enter a string: ")
old_char = input("Enter character to replace: ")
new_char = input("Enter new character: ")

result = ""
for ch in s:
    if ch == old_char:
        result = result + new_char
    else:
        result = result + ch
print("Result:", result)