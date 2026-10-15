import re

s = "Name: Amit, Roll: 101, Marks: 85"

name = re.findall(r'Name:\s*(\w+)', s)
roll = re.findall(r'Roll:\s*(\d+)', s)
marks = re.findall(r'Marks:\s*(\d+)', s)

print("Name:", name)
print("Roll:", roll)
print("Marks:", marks)