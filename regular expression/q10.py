import re

s = "Python is easy to learn"
result = re.findall(r'\b\w+\b', s)
print(len(result))