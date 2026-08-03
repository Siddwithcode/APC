msg = input("Enter message: ")
shift = int(input("Enter shift value: "))

encrypted = ""
for ch in msg:
    if ch.isalpha():
        base = ord('A') if ch.isupper() else ord('a')
        new_char = chr((ord(ch) - base + shift) % 26 + base)
        encrypted = encrypted + new_char
    else:
        encrypted = encrypted + ch

print("Encrypted:", encrypted)

decrypted = ""
for ch in encrypted:
    if ch.isalpha():
        base = ord('A') if ch.isupper() else ord('a')
        new_char = chr((ord(ch) - base - shift) % 26 + base)
        decrypted = decrypted + new_char
    else:
        decrypted = decrypted + ch

print("Decrypted:", decrypted)