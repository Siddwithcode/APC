s = input("Enter a string: ")
reversed_s = ""
for ch in s:
    reversed_s = ch + reversed_s

if s == reversed_s:
    print("Palindrome")
else:
    print("Not a Palindrome")