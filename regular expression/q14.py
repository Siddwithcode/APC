import re

s = "Visit https://google.com and http://example.com"

result = re.findall(r'https?://\S+', s)
print(result)