import re

s = "<p>Hello!!!   Python</p>"

s = re.sub(r'<[^>]+>', '', s)
s = re.sub(r'[!]+', '', s)
s = re.sub(r'\s+', ' ', s).strip()

print(s)