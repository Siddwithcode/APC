import re

s = "Hello World\tPython\nCode"
result = re.findall(r'[ \t\n]', s)
print(result)