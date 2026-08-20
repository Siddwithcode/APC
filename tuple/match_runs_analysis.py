# Store runs scored in 10 matches
runs = (45, 82, 0, 102, 34, 67, 12, 58, 71, 9)

total_runs = sum(runs)
highest_score = max(runs)
lowest_score = min(runs)
average_score = total_runs / len(runs)

print("Runs scored in 10 matches:", runs)
print("Total Runs    :", total_runs)
print("Highest Score :", highest_score)
print("Lowest Score  :", lowest_score)
print("Average Score :", average_score)
