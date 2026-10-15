import re

s = "Hello     Python   World"
result = re.sub(r' +', ' ', s)
print(result)