import re

n = input("Enter vehicle number: ")

if re.fullmatch(r'[A-Z]{2}\d{2}[A-Z]{2}\d{4}', n):
    print("Valid format")
else:
    print("Invalid format")