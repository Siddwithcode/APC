import pandas as pd
s = pd.Series({'Book': 500, 'Pen': 50, 'Bag': 1200})
print(s)
print(s * 1.10)
print(s.idxmax())
print(s[s > 1000])