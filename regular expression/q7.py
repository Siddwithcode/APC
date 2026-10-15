import re

s = "Apple Mango Chair Ball"
result = re.findall(r'\b\w{5}\b', s)
print(result)