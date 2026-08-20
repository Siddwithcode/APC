# Store temperatures of seven days in a tuple
temperatures = (31.5, 32.0, 29.8, 30.5, 33.0, 34.2, 31.0)

max_temp = max(temperatures)
min_temp = min(temperatures)
avg_temp = sum(temperatures) / len(temperatures)

print("Temperatures of 7 days:", temperatures)
print(f"Maximum Temperature : {max_temp}°C")
print(f"Minimum Temperature : {min_temp}°C")
print(f"Average Temperature : {avg_temp:.2f}°C")
