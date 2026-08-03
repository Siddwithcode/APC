s = input("Enter a string: ")
upper = 0
lower = 0
for ch in s:
    if ch.isupper():
        upper = upper + 1
    if ch.islower():
        lower = lower + 1
print("Uppercase:", upper)
print("Lowercase:", lower)