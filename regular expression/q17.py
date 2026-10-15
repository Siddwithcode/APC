import re

s = "Python is is very very easy"

result = re.findall(r'\b(\w+)\s+\1\b', s, re.I)
print(result)