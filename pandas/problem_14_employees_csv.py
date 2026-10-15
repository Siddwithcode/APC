import pandas as pd
df = pd.read_csv('employees.csv')
print(df[df['Department'] == 'CSE'])
print(df['Salary'].mean())
print(df['Salary'].max(), df['Salary'].min())
print(df[df['Salary'] > 50000])
print(df.groupby('Department')['Salary'].mean())