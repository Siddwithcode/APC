# Create a tuple of employee IDs
employee_ids = (101, 102, 103, 104, 105)

# ID to search
target_id = 103

# Find index of target_id
if target_id in employee_ids:
    index = employee_ids.index(target_id)
    print(f"Employee ID {target_id} found at index: {index}")
else:
    print(f"Employee ID {target_id} not found in the tuple.")
