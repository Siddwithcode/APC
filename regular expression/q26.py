import re

s = "DOI: 10.1234/abc.5678 Year: 2024 Email: abc@gmail.com URL: https://example.com"

doi = re.findall(r'10\.\d{4,9}/[^\s]+', s)
year = re.findall(r'\b(?:19|20)\d{2}\b', s)
email = re.findall(r'[\w.-]+@[\w.-]+\.\w+', s)
url = re.findall(r'https?://\S+', s)

print("DOI:", doi)
print("Year:", year)
print("Email:", email)
print("URL:", url)