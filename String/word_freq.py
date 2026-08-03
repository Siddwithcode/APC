paragraph = input("Enter a paragraph: ")
words = paragraph.lower().split()
checked = []

for w in words:
    if w not in checked:
        count = 0
        for x in words:
            if x == w:
                count = count + 1
        print(w, ":", count)
        checked.append(w)