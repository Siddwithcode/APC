import pandas as pd
df = pd.read_csv('weather.csv')
print(df['Temperature'].max(), df['Temperature'].min(), df['Temperature'].mean())
print(df[df['Temperature'] > 35])
print(df.groupby('City')['Temperature'].mean())