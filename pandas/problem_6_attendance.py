import pandas as pd
data = {'Student_ID': [1, 2, 3], 'Name': ['Liam', 'Noah', 'Oliver'], 'Department': ['CS', 'IT', 'CS'], 'Total_Classes': [40, 40, 40], 'Classes_Attended': [35, 25, 38]}
df = pd.DataFrame(data)
df['Attendance Percentage'] = (df['Classes_Attended'] / df['Total_Classes']) * 100
print(df[df['Attendance Percentage'] < 75])