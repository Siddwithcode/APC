sentence = input("Enter a sentence: ")
words = sentence.split()
reversed_sentence = ""

for w in words:
    reversed_sentence = w + " " + reversed_sentence

print("Reversed:", reversed_sentence)