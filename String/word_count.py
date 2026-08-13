sentence = input("Enter a sentence: ")
words = sentence.split()
count = 0
for w in words:
    count = count + 1
print("Total words:", count)