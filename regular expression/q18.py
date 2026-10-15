import re

s = "My PIN is 413001 and another is 416001"

result = re.findall(r'\b[1-9]\d{5}\b', s)
print(result)