s = input("Enter a string: ")
target = input("Enter character to count: ")
count = 0
for ch in s:
    if ch == target:
        count = count + 1
print("Count:", count)