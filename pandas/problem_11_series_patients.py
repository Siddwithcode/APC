import pandas as pd
s = pd.Series({101: 45, 102: 65, 103: 70, 104: 30})
print(s.mean())
print(s.idxmax(), s.idxmin())
print(s[s > 60])