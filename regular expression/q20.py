import re

s = "Files: abc.py, photo.jpg, notes.txt"

result = re.findall(r'\.([A-Za-z0-9]+)\b', s)
print(result)