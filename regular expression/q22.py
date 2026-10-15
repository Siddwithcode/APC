import re

s = "Invoice INV123 Date 15-10-2026 Amount 2500"

invoice = re.findall(r'INV\d+', s)
date = re.findall(r'\d{2}-\d{2}-\d{4}', s)
amount = re.findall(r'Amount\s+(\d+)', s)

print("Invoice:", invoice)
print("Date:", date)
print("Amount:", amount)