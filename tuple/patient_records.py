# Create a tuple containing patient records
patient_records = (
    (1001, "Alice Smith", 34, "A+"),
    (1002, "Bob Jones", 45, "O-"),
    (1003, "Charlie Brown", 29, "B+"),
    (1004, "David Davis", 60, "A+"),
    (1005, "Eva Green", 22, "O+")
)

# Display all records
print("--- All Patient Records ---")
for record in patient_records:
    print(f"ID: {record[0]} | Name: {record[1]} | Age: {record[2]} | Blood Group: {record[3]}")

# Search for a patient by ID
print("\n--- Search Patient by ID ---")
search_id = 1003
found = False
for record in patient_records:
    if record[0] == search_id:
        print(f"Patient Found - Name: {record[1]}, Age: {record[2]}, Blood Group: {record[3]}")
        found = True
        break
if not found:
    print(f"Patient with ID {search_id} not found.")

# Count the total number of patients
print("\nTotal number of patients:", len(patient_records))

# Display patients with a specific blood group
target_bg = "A+"
print(f"\n--- Patients with Blood Group {target_bg} ---")
for record in patient_records:
    if record[3] == target_bg:
        print(f"ID: {record[0]} | Name: {record[1]} | Age: {record[2]}")
