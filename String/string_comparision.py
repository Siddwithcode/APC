s = input("Enter a string: ")
compressed = ""
i = 0

while i < len(s):
    count = 1
    while i + 1 < len(s) and s[i] == s[i + 1]:
        count = count + 1
        i = i + 1
    compressed = compressed + s[i] + str(count)
    i = i + 1

if len(compressed) < len(s):
    print("Compressed:", compressed)
else:
    print("Original:", s)