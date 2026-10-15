import pandas as pd
data = {'Product ID': [201, 202, 203], 'Product Name': ['Laptop', 'Mouse', 'Keyboard'], 'Category': ['Electronics', 'Accessories', 'Accessories'], 'Price': [50000, 1000, 2000], 'Quantity': [5, 50, 30]}
df = pd.DataFrame(data)
df['Total Amount'] = df['Price'] * df['Quantity']
print(df.loc[df['Total Amount'].idxmax()])