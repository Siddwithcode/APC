import re

s = "# This is a comment\nprint('Hello')"

result = re.findall(r'(?m)^\s*#.*$', s)
print(result)