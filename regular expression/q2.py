import re

s="i am a class student whose name is Amit and Aman "
result=re.findall(r'\b[Aa]\w*',s)
print(result)