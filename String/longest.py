sentence = input("Enter a sentence: ")
words = sentence.split()
longest = words[0]
for w in words:
    if len(w) > len(longest):
        longest = w
print("Longest word:", longest)