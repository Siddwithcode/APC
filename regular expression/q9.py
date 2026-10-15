import re

s = "Hello@123 #Python!"
result = re.sub(r'[^a-zA-Z0-9 ]', '', s)
print(result)