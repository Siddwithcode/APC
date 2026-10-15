import pandas as pd
s = pd.Series({'Alice': 80, 'Bob': 95, 'Charlie': 60})
print(s.mean())
print(s[s < 75])
print(s[s > 90])
print(s.idxmax())