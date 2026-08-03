s = input("Enter a string: ")
seen = ""
duplicates = ""
for ch in s:
    if ch in seen:
        if ch not in duplicates:
            duplicates = duplicates + ch
    else:
        seen = seen + ch
print("Duplicates:", duplicates)