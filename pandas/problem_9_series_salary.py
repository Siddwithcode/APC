import pandas as pd
s = pd.Series({'John': 45000, 'Sara': 60000, 'Mike': 30000, 'Emma': 80000})
print(s)
print(s.max(), s.min(), s.mean())
print(s[s > 50000])