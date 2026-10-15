import pandas as pd
data = {'Order_ID': [1001, 1002, 1003], 'Customer': ['Alice', 'Bob', 'Charlie'], 'Product': ['Phone', 'Tablet', 'Watch'], 'Quantity': [1, 2, 3], 'Price': [20000, 15000, 5000], 'Discount': [1000, 1500, 500]}
df = pd.DataFrame(data)
df['Final Amount'] = (df['Quantity'] * df['Price']) - df['Discount']
print(df)
print(df[df['Final Amount'] > 5000])
print(df.loc[df['Final Amount'].idxmax()])
print(df['Final Amount'].mean())