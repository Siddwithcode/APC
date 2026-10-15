import pandas as pd
data = {'Patient ID': [1, 2, 3], 'Patient Name': ['Tom', 'Jerry', 'Spike'], 'Age': [45, 65, 70], 'Disease': ['Flu', 'Diabetes', 'BP'], 'Medical Charges': [15000, 55000, 60000]}
df = pd.DataFrame(data)
print(df[df['Age'] > 60])
print(df['Medical Charges'].mean(), df['Medical Charges'].max())
print(df[df['Medical Charges'] > 50000])