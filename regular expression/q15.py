import re

s = "I love #Python and #Coding"

result = re.findall(r'#\w+', s)
print(result)