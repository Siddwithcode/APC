import pandas as pd
data = {'Student ID': [1, 2, 3, 4, 5], 'Student Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'], 'Python Marks': [80, 90, 70, 85, 60], 'DBMS Marks': [75, 88, 65, 90, 70], 'Mathematics Marks': [85, 92, 75, 88, 65]}
df = pd.DataFrame(data)
df['Total Marks'] = df[['Python Marks', 'DBMS Marks', 'Mathematics Marks']].sum(axis=1)
df['Average Marks'] = df[['Python Marks', 'DBMS Marks', 'Mathematics Marks']].mean(axis=1)
print(df[df['Average Marks'] > 75])