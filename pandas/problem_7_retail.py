import pandas as pd
data = {'Product_ID': [10, 11, 12], 'Product_Name': ['Desk', 'Chair', 'Lamp'], 'Category': ['Furniture', 'Furniture', 'Decor'], 'Price': [5000, 2500, 800], 'Quantity': [3, 5, 10]}
df = pd.DataFrame(data)
df['Total_Sales'] = df['Price'] * df['Quantity']
print(df[df['Total_Sales'] > 10000])
print(df.loc[df['Total_Sales'].idxmax()])
print(df['Total_Sales'].mean())