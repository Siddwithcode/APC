import re
s="hello world is the programers first code which exectues properly"
result=re.findall(r'[aeiouAEIOU]',s)
print(result)
print(len(result))