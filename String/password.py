password = input("Enter password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

for ch in password:
    if ch.isupper():
        has_upper = True
    if ch.islower():
        has_lower = True
    if ch.isdigit():
        has_digit = True
    if not ch.isalnum():
        has_special = True

if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
    print("Valid Password")
else:
    print("Invalid Password")