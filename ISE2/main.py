import mymodule

marks = []

for i in range(3):
    m = int(input("Enter marks: "))
    marks.append(m)

t = mymodule.total(marks)
p = mymodule.percentage(marks)
g = mymodule.grade(p)

print("Total:", t)
print("Percentage:", round(p, 2))
print("Grade:", g)