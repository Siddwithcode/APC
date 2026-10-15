import pandas as pd
df = pd.read_csv('patients.csv')
print(df[df['Age'] > 60])
print(df['Medical_Expense'].mean())
print(df.loc[df['Medical_Expense'].idxmax()])
print(df['Disease'].value_counts())
print(df[df['Medical_Expense'] > 50000])