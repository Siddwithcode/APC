import re

s = "Ravi likes apples and mangoes"
result = re.findall(r'\b\w+s\b', s)
print(result)