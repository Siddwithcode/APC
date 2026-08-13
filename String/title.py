sentence = input("Enter a sentence: ")
words = sentence.split()
result = ""
for w in words:
    first_letter = w[0].upper()
    rest_letters = w[1:]
    result = result + first_letter + rest_letters + " "
print("Title Case:", result)