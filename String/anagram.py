s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

s1 = s1.replace(" ", "").lower()
s2 = s2.replace(" ", "").lower()

sorted1 = sorted(s1)
sorted2 = sorted(s2)

if sorted1 == sorted2:
    print("Anagrams")
else:
    print("Not Anagrams")