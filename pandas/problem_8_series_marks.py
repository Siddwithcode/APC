import pandas as pd
s = pd.Series({'Alice': 85, 'Bob': 92, 'Charlie': 65, 'David': 78})
print(s)
print(s['Bob'])
print(s.max(), s.min(), s.mean())
print(s[s > 75])