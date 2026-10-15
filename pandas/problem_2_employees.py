import pandas as pd
data = {'Employee ID': [101, 102, 103, 104], 'Employee Name': ['John', 'Sara', 'Mike', 'Emma'], 'Department': ['IT', 'HR', 'IT', 'Finance'], 'Salary': [60000, 45000, 80000, 55000], 'Experience': [3, 2, 7, 4]}
df = pd.DataFrame(data)
print(df[df['Salary'] > 50000])
print(df['Salary'].mean(), df['Salary'].max())
print(df.loc[df['Experience'].idxmax()])