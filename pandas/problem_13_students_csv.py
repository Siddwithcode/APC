import pandas as pd
df = pd.read_csv('students.csv')
print(df.head())
print(df.tail())
df['Total'] = df[['Python', 'DBMS', 'Maths']].sum(axis=1)
df['Average'] = df[['Python', 'DBMS', 'Maths']].mean(axis=1)
print(df[df['Average'] > 75])
print(df.loc[df['Average'].idxmax()])
print(df[['Python', 'DBMS', 'Maths']].mean())