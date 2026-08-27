def palindrome(text, start, end):

    if start >= end:
        return True

    if text[start] != text[end]:
        return False

    return palindrome(text, start + 1, end - 1)


text = input("Enter a string: ")

result = palindrome(text, 0, len(text) - 1)

if result:
    print("Palindrome")
else:
    print("Not Palindrome")