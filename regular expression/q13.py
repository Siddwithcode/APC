import re

s = "Dates are 15-08-2026 and 10-10-2026"

result = re.findall(r'\b\d{2}-\d{2}-\d{4}\b', s)
print(result)